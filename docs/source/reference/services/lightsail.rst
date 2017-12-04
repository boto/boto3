

*********
Lightsail
*********

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: Lightsail.Client

  A low-level client representing Amazon Lightsail::

    
    import boto3
    
    client = boto3.client('lightsail')

  
  These are the available methods:
  
  *   :py:meth:`~Lightsail.Client.allocate_static_ip`

  
  *   :py:meth:`~Lightsail.Client.attach_disk`

  
  *   :py:meth:`~Lightsail.Client.attach_instances_to_load_balancer`

  
  *   :py:meth:`~Lightsail.Client.attach_load_balancer_tls_certificate`

  
  *   :py:meth:`~Lightsail.Client.attach_static_ip`

  
  *   :py:meth:`~Lightsail.Client.can_paginate`

  
  *   :py:meth:`~Lightsail.Client.close_instance_public_ports`

  
  *   :py:meth:`~Lightsail.Client.create_disk`

  
  *   :py:meth:`~Lightsail.Client.create_disk_from_snapshot`

  
  *   :py:meth:`~Lightsail.Client.create_disk_snapshot`

  
  *   :py:meth:`~Lightsail.Client.create_domain`

  
  *   :py:meth:`~Lightsail.Client.create_domain_entry`

  
  *   :py:meth:`~Lightsail.Client.create_instance_snapshot`

  
  *   :py:meth:`~Lightsail.Client.create_instances`

  
  *   :py:meth:`~Lightsail.Client.create_instances_from_snapshot`

  
  *   :py:meth:`~Lightsail.Client.create_key_pair`

  
  *   :py:meth:`~Lightsail.Client.create_load_balancer`

  
  *   :py:meth:`~Lightsail.Client.create_load_balancer_tls_certificate`

  
  *   :py:meth:`~Lightsail.Client.delete_disk`

  
  *   :py:meth:`~Lightsail.Client.delete_disk_snapshot`

  
  *   :py:meth:`~Lightsail.Client.delete_domain`

  
  *   :py:meth:`~Lightsail.Client.delete_domain_entry`

  
  *   :py:meth:`~Lightsail.Client.delete_instance`

  
  *   :py:meth:`~Lightsail.Client.delete_instance_snapshot`

  
  *   :py:meth:`~Lightsail.Client.delete_key_pair`

  
  *   :py:meth:`~Lightsail.Client.delete_load_balancer`

  
  *   :py:meth:`~Lightsail.Client.delete_load_balancer_tls_certificate`

  
  *   :py:meth:`~Lightsail.Client.detach_disk`

  
  *   :py:meth:`~Lightsail.Client.detach_instances_from_load_balancer`

  
  *   :py:meth:`~Lightsail.Client.detach_static_ip`

  
  *   :py:meth:`~Lightsail.Client.download_default_key_pair`

  
  *   :py:meth:`~Lightsail.Client.generate_presigned_url`

  
  *   :py:meth:`~Lightsail.Client.get_active_names`

  
  *   :py:meth:`~Lightsail.Client.get_blueprints`

  
  *   :py:meth:`~Lightsail.Client.get_bundles`

  
  *   :py:meth:`~Lightsail.Client.get_disk`

  
  *   :py:meth:`~Lightsail.Client.get_disk_snapshot`

  
  *   :py:meth:`~Lightsail.Client.get_disk_snapshots`

  
  *   :py:meth:`~Lightsail.Client.get_disks`

  
  *   :py:meth:`~Lightsail.Client.get_domain`

  
  *   :py:meth:`~Lightsail.Client.get_domains`

  
  *   :py:meth:`~Lightsail.Client.get_instance`

  
  *   :py:meth:`~Lightsail.Client.get_instance_access_details`

  
  *   :py:meth:`~Lightsail.Client.get_instance_metric_data`

  
  *   :py:meth:`~Lightsail.Client.get_instance_port_states`

  
  *   :py:meth:`~Lightsail.Client.get_instance_snapshot`

  
  *   :py:meth:`~Lightsail.Client.get_instance_snapshots`

  
  *   :py:meth:`~Lightsail.Client.get_instance_state`

  
  *   :py:meth:`~Lightsail.Client.get_instances`

  
  *   :py:meth:`~Lightsail.Client.get_key_pair`

  
  *   :py:meth:`~Lightsail.Client.get_key_pairs`

  
  *   :py:meth:`~Lightsail.Client.get_load_balancer`

  
  *   :py:meth:`~Lightsail.Client.get_load_balancer_metric_data`

  
  *   :py:meth:`~Lightsail.Client.get_load_balancer_tls_certificates`

  
  *   :py:meth:`~Lightsail.Client.get_load_balancers`

  
  *   :py:meth:`~Lightsail.Client.get_operation`

  
  *   :py:meth:`~Lightsail.Client.get_operations`

  
  *   :py:meth:`~Lightsail.Client.get_operations_for_resource`

  
  *   :py:meth:`~Lightsail.Client.get_paginator`

  
  *   :py:meth:`~Lightsail.Client.get_regions`

  
  *   :py:meth:`~Lightsail.Client.get_static_ip`

  
  *   :py:meth:`~Lightsail.Client.get_static_ips`

  
  *   :py:meth:`~Lightsail.Client.get_waiter`

  
  *   :py:meth:`~Lightsail.Client.import_key_pair`

  
  *   :py:meth:`~Lightsail.Client.is_vpc_peered`

  
  *   :py:meth:`~Lightsail.Client.open_instance_public_ports`

  
  *   :py:meth:`~Lightsail.Client.peer_vpc`

  
  *   :py:meth:`~Lightsail.Client.put_instance_public_ports`

  
  *   :py:meth:`~Lightsail.Client.reboot_instance`

  
  *   :py:meth:`~Lightsail.Client.release_static_ip`

  
  *   :py:meth:`~Lightsail.Client.start_instance`

  
  *   :py:meth:`~Lightsail.Client.stop_instance`

  
  *   :py:meth:`~Lightsail.Client.unpeer_vpc`

  
  *   :py:meth:`~Lightsail.Client.update_domain_entry`

  
  *   :py:meth:`~Lightsail.Client.update_load_balancer_attribute`

  

  .. py:method:: allocate_static_ip(**kwargs)

    

    Allocates a static IP address.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/AllocateStaticIp>`_    


    **Request Syntax** 
    ::

      response = client.allocate_static_ip(
          staticIpName='string'
      )
    :type staticIpName: string
    :param staticIpName: **[REQUIRED]** 

      The name of the static IP address.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An array of key-value pairs containing information about the static IP address you allocated.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

  .. py:method:: attach_disk(**kwargs)

    

    Attaches a block storage disk to a running or stopped Lightsail instance and exposes it to the instance with the specified disk name.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/AttachDisk>`_    


    **Request Syntax** 
    ::

      response = client.attach_disk(
          diskName='string',
          instanceName='string',
          diskPath='string'
      )
    :type diskName: string
    :param diskName: **[REQUIRED]** 

      The unique Lightsail disk name (e.g., ``my-disk`` ).

      

    
    :type instanceName: string
    :param instanceName: **[REQUIRED]** 

      The name of the Lightsail instance where you want to utilize the storage disk.

      

    
    :type diskPath: string
    :param diskPath: **[REQUIRED]** 

      The disk path to expose to the instance (e.g., ``/dev/xvdf`` ).

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An object describing the API operations.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

  .. py:method:: attach_instances_to_load_balancer(**kwargs)

    

    Attaches one or more Lightsail instances to a load balancer.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/AttachInstancesToLoadBalancer>`_    


    **Request Syntax** 
    ::

      response = client.attach_instances_to_load_balancer(
          loadBalancerName='string',
          instanceNames=[
              'string',
          ]
      )
    :type loadBalancerName: string
    :param loadBalancerName: **[REQUIRED]** 

      The name of the load balancer.

      

    
    :type instanceNames: list
    :param instanceNames: **[REQUIRED]** 

      An array of strings representing the instance name(s) you want to attach to your load balancer.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An object representing the API operations.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

  .. py:method:: attach_load_balancer_tls_certificate(**kwargs)

    

    Attaches a Transport Layer Security (TLS) certificate to your load balancer.

     

    TLS is just an updated, more secure version of Secure Socket Layer (SSL).

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/AttachLoadBalancerTlsCertificate>`_    


    **Request Syntax** 
    ::

      response = client.attach_load_balancer_tls_certificate(
          loadBalancerName='string',
          certificateName='string'
      )
    :type loadBalancerName: string
    :param loadBalancerName: **[REQUIRED]** 

      The name of the load balancer to which you want to associate the TLS/SSL certificate.

      

    
    :type certificateName: string
    :param certificateName: **[REQUIRED]** 

      The name of your TLS/SSL certificate.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An object representing the API operations.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

  .. py:method:: attach_static_ip(**kwargs)

    

    Attaches a static IP address to a specific Amazon Lightsail instance.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/AttachStaticIp>`_    


    **Request Syntax** 
    ::

      response = client.attach_static_ip(
          staticIpName='string',
          instanceName='string'
      )
    :type staticIpName: string
    :param staticIpName: **[REQUIRED]** 

      The name of the static IP.

      

    
    :type instanceName: string
    :param instanceName: **[REQUIRED]** 

      The instance name to which you want to attach the static IP address.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An array of key-value pairs containing information about your API operations.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

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


  .. py:method:: close_instance_public_ports(**kwargs)

    

    Closes the public ports on a specific Amazon Lightsail instance.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CloseInstancePublicPorts>`_    


    **Request Syntax** 
    ::

      response = client.close_instance_public_ports(
          portInfo={
              'fromPort': 123,
              'toPort': 123,
              'protocol': 'tcp'|'all'|'udp'
          },
          instanceName='string'
      )
    :type portInfo: dict
    :param portInfo: **[REQUIRED]** 

      Information about the public port you are trying to close.

      

    
      - **fromPort** *(integer) --* 

        The first port in the range.

        

      
      - **toPort** *(integer) --* 

        The last port in the range.

        

      
      - **protocol** *(string) --* 

        The protocol. 

        

      
    
    :type instanceName: string
    :param instanceName: **[REQUIRED]** 

      The name of the instance on which you're attempting to close the public ports.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operation': {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operation** *(dict) --* 

          An array of key-value pairs that contains information about the operation.

          
          

          - **id** *(string) --* 

            The ID of the operation.

            
          

          - **resourceName** *(string) --* 

            The resource name.

            
          

          - **resourceType** *(string) --* 

            The resource type. 

            
          

          - **createdAt** *(datetime) --* 

            The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

            
          

          - **location** *(dict) --* 

            The region and Availability Zone.

            
            

            - **availabilityZone** *(string) --* 

              The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

              
            

            - **regionName** *(string) --* 

              The AWS Region name.

              
        
          

          - **isTerminal** *(boolean) --* 

            A Boolean value indicating whether the operation is terminal.

            
          

          - **operationDetails** *(string) --* 

            Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

            
          

          - **operationType** *(string) --* 

            The type of operation. 

            
          

          - **status** *(string) --* 

            The status of the operation. 

            
          

          - **statusChangedAt** *(datetime) --* 

            The timestamp when the status was changed (e.g., ``1479816991.349`` ).

            
          

          - **errorCode** *(string) --* 

            The error code.

            
          

          - **errorDetails** *(string) --* 

            The error details.

            
      
    

  .. py:method:: create_disk(**kwargs)

    

    Creates a block storage disk that can be attached to a Lightsail instance in the same Availability Zone (e.g., ``us-east-2a`` ). The disk is created in the regional endpoint that you send the HTTP request to. For more information, see `Regions and Availability Zones in Lightsail <https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateDisk>`_    


    **Request Syntax** 
    ::

      response = client.create_disk(
          diskName='string',
          availabilityZone='string',
          sizeInGb=123
      )
    :type diskName: string
    :param diskName: **[REQUIRED]** 

      The unique Lightsail disk name (e.g., ``my-disk`` ).

      

    
    :type availabilityZone: string
    :param availabilityZone: **[REQUIRED]** 

      The Availability Zone where you want to create the disk (e.g., ``us-east-2a`` ). Choose the same Availability Zone as the Lightsail instance where you want to create the disk.

       

      Use the GetRegions operation to list the Availability Zones where Lightsail is currently available.

      

    
    :type sizeInGb: integer
    :param sizeInGb: **[REQUIRED]** 

      The size of the disk in GB (e.g., ``32`` ).

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An object describing the API operations.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

  .. py:method:: create_disk_from_snapshot(**kwargs)

    

    Creates a block storage disk from a disk snapshot that can be attached to a Lightsail instance in the same Availability Zone (e.g., ``us-east-2a`` ). The disk is created in the regional endpoint that you send the HTTP request to. For more information, see `Regions and Availability Zones in Lightsail <https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateDiskFromSnapshot>`_    


    **Request Syntax** 
    ::

      response = client.create_disk_from_snapshot(
          diskName='string',
          diskSnapshotName='string',
          availabilityZone='string',
          sizeInGb=123
      )
    :type diskName: string
    :param diskName: **[REQUIRED]** 

      The unique Lightsail disk name (e.g., ``my-disk`` ).

      

    
    :type diskSnapshotName: string
    :param diskSnapshotName: **[REQUIRED]** 

      The name of the disk snapshot (e.g., ``my-snapshot`` ) from which to create the new storage disk.

      

    
    :type availabilityZone: string
    :param availabilityZone: **[REQUIRED]** 

      The Availability Zone where you want to create the disk (e.g., ``us-east-2a`` ). Choose the same Availability Zone as the Lightsail instance where you want to create the disk.

       

      Use the GetRegions operation to list the Availability Zones where Lightsail is currently available.

      

    
    :type sizeInGb: integer
    :param sizeInGb: **[REQUIRED]** 

      The size of the disk in GB (e.g., ``32`` ).

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An object describing the API operations.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

  .. py:method:: create_disk_snapshot(**kwargs)

    

    Creates a snapshot of a block storage disk. You can use snapshots for backups, to make copies of disks, and to save data before shutting down a Lightsail instance.

     

    You can take a snapshot of an attached disk that is in use; however, snapshots only capture data that has been written to your disk at the time the snapshot command is issued. This may exclude any data that has been cached by any applications or the operating system. If you can pause any file systems on the disk long enough to take a snapshot, your snapshot should be complete. Nevertheless, if you cannot pause all file writes to the disk, you should unmount the disk from within the Lightsail instance, issue the create disk snapshot command, and then remount the disk to ensure a consistent and complete snapshot. You may remount and use your disk while the snapshot status is pending.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateDiskSnapshot>`_    


    **Request Syntax** 
    ::

      response = client.create_disk_snapshot(
          diskName='string',
          diskSnapshotName='string'
      )
    :type diskName: string
    :param diskName: **[REQUIRED]** 

      The unique name of the source disk (e.g., ``my-source-disk`` ).

      

    
    :type diskSnapshotName: string
    :param diskSnapshotName: **[REQUIRED]** 

      The name of the destination disk snapshot (e.g., ``my-disk-snapshot`` ) based on the source disk.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An object describing the API operations.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

  .. py:method:: create_domain(**kwargs)

    

    Creates a domain resource for the specified domain (e.g., example.com).

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateDomain>`_    


    **Request Syntax** 
    ::

      response = client.create_domain(
          domainName='string'
      )
    :type domainName: string
    :param domainName: **[REQUIRED]** 

      The domain name to manage (e.g., ``example.com`` ).

       

      .. note::

         

        You cannot register a new domain name using Lightsail. You must register a domain name using Amazon Route 53 or another domain name registrar. If you have already registered your domain, you can enter its name in this parameter to manage the DNS records for that domain.

         

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operation': {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operation** *(dict) --* 

          An array of key-value pairs containing information about the domain resource you created.

          
          

          - **id** *(string) --* 

            The ID of the operation.

            
          

          - **resourceName** *(string) --* 

            The resource name.

            
          

          - **resourceType** *(string) --* 

            The resource type. 

            
          

          - **createdAt** *(datetime) --* 

            The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

            
          

          - **location** *(dict) --* 

            The region and Availability Zone.

            
            

            - **availabilityZone** *(string) --* 

              The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

              
            

            - **regionName** *(string) --* 

              The AWS Region name.

              
        
          

          - **isTerminal** *(boolean) --* 

            A Boolean value indicating whether the operation is terminal.

            
          

          - **operationDetails** *(string) --* 

            Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

            
          

          - **operationType** *(string) --* 

            The type of operation. 

            
          

          - **status** *(string) --* 

            The status of the operation. 

            
          

          - **statusChangedAt** *(datetime) --* 

            The timestamp when the status was changed (e.g., ``1479816991.349`` ).

            
          

          - **errorCode** *(string) --* 

            The error code.

            
          

          - **errorDetails** *(string) --* 

            The error details.

            
      
    

  .. py:method:: create_domain_entry(**kwargs)

    

    Creates one of the following entry records associated with the domain: A record, CNAME record, TXT record, or MX record.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateDomainEntry>`_    


    **Request Syntax** 
    ::

      response = client.create_domain_entry(
          domainName='string',
          domainEntry={
              'id': 'string',
              'name': 'string',
              'target': 'string',
              'isAlias': True|False,
              'type': 'string',
              'options': {
                  'string': 'string'
              }
          }
      )
    :type domainName: string
    :param domainName: **[REQUIRED]** 

      The domain name (e.g., ``example.com`` ) for which you want to create the domain entry.

      

    
    :type domainEntry: dict
    :param domainEntry: **[REQUIRED]** 

      An array of key-value pairs containing information about the domain entry request.

      

    
      - **id** *(string) --* 

        The ID of the domain recordset entry.

        

      
      - **name** *(string) --* 

        The name of the domain.

        

      
      - **target** *(string) --* 

        The target AWS name server (e.g., ``ns-111.awsdns-22.com.`` ).

        

      
      - **isAlias** *(boolean) --* 

        When ``true`` , specifies whether the domain entry is an alias used by the Lightsail load balancer.

        

      
      - **type** *(string) --* 

        The type of domain entry (e.g., ``SOA`` or ``NS`` ).

        

      
      - **options** *(dict) --* 

        (Deprecated) The options for the domain entry.

         

        .. note::

           

          In releases prior to November 29, 2017, this parameter was not included in the API response. It is now deprecated.

           

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operation': {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operation** *(dict) --* 

          An array of key-value pairs containing information about the operation.

          
          

          - **id** *(string) --* 

            The ID of the operation.

            
          

          - **resourceName** *(string) --* 

            The resource name.

            
          

          - **resourceType** *(string) --* 

            The resource type. 

            
          

          - **createdAt** *(datetime) --* 

            The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

            
          

          - **location** *(dict) --* 

            The region and Availability Zone.

            
            

            - **availabilityZone** *(string) --* 

              The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

              
            

            - **regionName** *(string) --* 

              The AWS Region name.

              
        
          

          - **isTerminal** *(boolean) --* 

            A Boolean value indicating whether the operation is terminal.

            
          

          - **operationDetails** *(string) --* 

            Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

            
          

          - **operationType** *(string) --* 

            The type of operation. 

            
          

          - **status** *(string) --* 

            The status of the operation. 

            
          

          - **statusChangedAt** *(datetime) --* 

            The timestamp when the status was changed (e.g., ``1479816991.349`` ).

            
          

          - **errorCode** *(string) --* 

            The error code.

            
          

          - **errorDetails** *(string) --* 

            The error details.

            
      
    

  .. py:method:: create_instance_snapshot(**kwargs)

    

    Creates a snapshot of a specific virtual private server, or *instance* . You can use a snapshot to create a new instance that is based on that snapshot.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateInstanceSnapshot>`_    


    **Request Syntax** 
    ::

      response = client.create_instance_snapshot(
          instanceSnapshotName='string',
          instanceName='string'
      )
    :type instanceSnapshotName: string
    :param instanceSnapshotName: **[REQUIRED]** 

      The name for your new snapshot.

      

    
    :type instanceName: string
    :param instanceName: **[REQUIRED]** 

      The Lightsail instance on which to base your snapshot.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An array of key-value pairs containing information about the results of your create instances snapshot request.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

  .. py:method:: create_instances(**kwargs)

    

    Creates one or more Amazon Lightsail virtual private servers, or *instances* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateInstances>`_    


    **Request Syntax** 
    ::

      response = client.create_instances(
          instanceNames=[
              'string',
          ],
          availabilityZone='string',
          customImageName='string',
          blueprintId='string',
          bundleId='string',
          userData='string',
          keyPairName='string'
      )
    :type instanceNames: list
    :param instanceNames: **[REQUIRED]** 

      The names to use for your new Lightsail instances. Separate multiple values using quotation marks and commas, for example: ``["MyFirstInstance","MySecondInstance"]``  

      

    
      - *(string) --* 

      
  
    :type availabilityZone: string
    :param availabilityZone: **[REQUIRED]** 

      The Availability Zone in which to create your instance. Use the following format: ``us-east-2a`` (case sensitive). You can get a list of availability zones by using the `get regions <http://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetRegions.html>`__ operation. Be sure to add the ``include availability zones`` parameter to your request.

      

    
    :type customImageName: string
    :param customImageName: 

      (Deprecated) The name for your custom image.

       

      .. note::

         

        In releases prior to June 12, 2017, this parameter was ignored by the API. It is now deprecated.

         

      

    
    :type blueprintId: string
    :param blueprintId: **[REQUIRED]** 

      The ID for a virtual private server image (e.g., ``app_wordpress_4_4`` or ``app_lamp_7_0`` ). Use the get blueprints operation to return a list of available images (or *blueprints* ).

      

    
    :type bundleId: string
    :param bundleId: **[REQUIRED]** 

      The bundle of specification information for your virtual private server (or *instance* ), including the pricing plan (e.g., ``micro_1_0`` ).

      

    
    :type userData: string
    :param userData: 

      A launch script you can create that configures a server with additional user data. For example, you might want to run ``apt-get -y update`` .

       

      .. note::

         

        Depending on the machine image you choose, the command to get software on your instance varies. Amazon Linux and CentOS use ``yum`` , Debian and Ubuntu use ``apt-get`` , and FreeBSD uses ``pkg`` . For a complete list, see the `Dev Guide <https://lightsail.aws.amazon.com/ls/docs/getting-started/article/compare-options-choose-lightsail-instance-image>`__ .

         

      

    
    :type keyPairName: string
    :param keyPairName: 

      The name of your key pair.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An array of key-value pairs containing information about the results of your create instances request.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

  .. py:method:: create_instances_from_snapshot(**kwargs)

    

    Uses a specific snapshot as a blueprint for creating one or more new instances that are based on that identical configuration.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateInstancesFromSnapshot>`_    


    **Request Syntax** 
    ::

      response = client.create_instances_from_snapshot(
          instanceNames=[
              'string',
          ],
          attachedDiskMapping={
              'string': [
                  {
                      'originalDiskPath': 'string',
                      'newDiskName': 'string'
                  },
              ]
          },
          availabilityZone='string',
          instanceSnapshotName='string',
          bundleId='string',
          userData='string',
          keyPairName='string'
      )
    :type instanceNames: list
    :param instanceNames: **[REQUIRED]** 

      The names for your new instances.

      

    
      - *(string) --* 

      
  
    :type attachedDiskMapping: dict
    :param attachedDiskMapping: 

      An object containing information about one or more disk mappings.

      

    
      - *(string) --* 

      
        - *(list) --* 

        
          - *(dict) --* 

            Describes a block storage disk mapping.

            

          
            - **originalDiskPath** *(string) --* 

              The original disk path exposed to the instance (for example, ``/dev/sdh`` ).

              

            
            - **newDiskName** *(string) --* 

              The new disk name (e.g., ``my-new-disk`` ).

              

            
          
      
  

    :type availabilityZone: string
    :param availabilityZone: **[REQUIRED]** 

      The Availability Zone where you want to create your instances. Use the following formatting: ``us-east-2a`` (case sensitive). You can get a list of availability zones by using the `get regions <http://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetRegions.html>`__ operation. Be sure to add the ``include availability zones`` parameter to your request.

      

    
    :type instanceSnapshotName: string
    :param instanceSnapshotName: **[REQUIRED]** 

      The name of the instance snapshot on which you are basing your new instances. Use the get instance snapshots operation to return information about your existing snapshots.

      

    
    :type bundleId: string
    :param bundleId: **[REQUIRED]** 

      The bundle of specification information for your virtual private server (or *instance* ), including the pricing plan (e.g., ``micro_1_0`` ).

      

    
    :type userData: string
    :param userData: 

      You can create a launch script that configures a server with additional user data. For example, ``apt-get -y update`` .

       

      .. note::

         

        Depending on the machine image you choose, the command to get software on your instance varies. Amazon Linux and CentOS use ``yum`` , Debian and Ubuntu use ``apt-get`` , and FreeBSD uses ``pkg`` . For a complete list, see the `Dev Guide <http://lightsail.aws.amazon.com/ls/docs/getting-started/articles/pre-installed-apps>`__ .

         

      

    
    :type keyPairName: string
    :param keyPairName: 

      The name for your key pair.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An array of key-value pairs containing information about the results of your create instances from snapshot request.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

  .. py:method:: create_key_pair(**kwargs)

    

    Creates sn SSH key pair.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateKeyPair>`_    


    **Request Syntax** 
    ::

      response = client.create_key_pair(
          keyPairName='string'
      )
    :type keyPairName: string
    :param keyPairName: **[REQUIRED]** 

      The name for your new key pair.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'keyPair': {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                'fingerprint': 'string'
            },
            'publicKeyBase64': 'string',
            'privateKeyBase64': 'string',
            'operation': {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **keyPair** *(dict) --* 

          An array of key-value pairs containing information about the new key pair you just created.

          
          

          - **name** *(string) --* 

            The friendly name of the SSH key pair.

            
          

          - **arn** *(string) --* 

            The Amazon Resource Name (ARN) of the key pair (e.g., ``arn:aws:lightsail:us-east-2:123456789101:KeyPair/05859e3d-331d-48ba-9034-12345EXAMPLE`` ).

            
          

          - **supportCode** *(string) --* 

            The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

            
          

          - **createdAt** *(datetime) --* 

            The timestamp when the key pair was created (e.g., ``1479816991.349`` ).

            
          

          - **location** *(dict) --* 

            The region name and Availability Zone where the key pair was created.

            
            

            - **availabilityZone** *(string) --* 

              The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

              
            

            - **regionName** *(string) --* 

              The AWS Region name.

              
        
          

          - **resourceType** *(string) --* 

            The resource type (usually ``KeyPair`` ).

            
          

          - **fingerprint** *(string) --* 

            The RSA fingerprint of the key pair.

            
      
        

        - **publicKeyBase64** *(string) --* 

          A base64-encoded public key of the ``ssh-rsa`` type.

          
        

        - **privateKeyBase64** *(string) --* 

          A base64-encoded RSA private key.

          
        

        - **operation** *(dict) --* 

          An array of key-value pairs containing information about the results of your create key pair request.

          
          

          - **id** *(string) --* 

            The ID of the operation.

            
          

          - **resourceName** *(string) --* 

            The resource name.

            
          

          - **resourceType** *(string) --* 

            The resource type. 

            
          

          - **createdAt** *(datetime) --* 

            The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

            
          

          - **location** *(dict) --* 

            The region and Availability Zone.

            
            

            - **availabilityZone** *(string) --* 

              The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

              
            

            - **regionName** *(string) --* 

              The AWS Region name.

              
        
          

          - **isTerminal** *(boolean) --* 

            A Boolean value indicating whether the operation is terminal.

            
          

          - **operationDetails** *(string) --* 

            Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

            
          

          - **operationType** *(string) --* 

            The type of operation. 

            
          

          - **status** *(string) --* 

            The status of the operation. 

            
          

          - **statusChangedAt** *(datetime) --* 

            The timestamp when the status was changed (e.g., ``1479816991.349`` ).

            
          

          - **errorCode** *(string) --* 

            The error code.

            
          

          - **errorDetails** *(string) --* 

            The error details.

            
      
    

  .. py:method:: create_load_balancer(**kwargs)

    

    Creates a Lightsail load balancer.

     

    When you create a load balancer, you can specify certificates and port settings. You can create up to 5 load balancers per AWS Region in your account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateLoadBalancer>`_    


    **Request Syntax** 
    ::

      response = client.create_load_balancer(
          loadBalancerName='string',
          instancePort=123,
          healthCheckPath='string',
          certificateName='string',
          certificateDomainName='string',
          certificateAlternativeNames=[
              'string',
          ]
      )
    :type loadBalancerName: string
    :param loadBalancerName: **[REQUIRED]** 

      The name of your load balancer.

      

    
    :type instancePort: integer
    :param instancePort: **[REQUIRED]** 

      The instance port where you're creating your load balancer.

      

    
    :type healthCheckPath: string
    :param healthCheckPath: 

      The path you provided to perform the load balancer health check. If you didn't specify a health check path, Lightsail uses the root path of your website (e.g., ``"/"`` ).

      

    
    :type certificateName: string
    :param certificateName: 

      The name of the TLS/SSL certificate.

       

      If you specify ``certificateName`` , then ``certificateDomainName`` is required (and vice-versa).

      

    
    :type certificateDomainName: string
    :param certificateDomainName: 

      The domain name with which your certificate is associated (e.g., ``example.com`` ).

       

      If you specify ``certificateDomainName`` , then ``certificateName`` is required (and vice-versa).

      

    
    :type certificateAlternativeNames: list
    :param certificateAlternativeNames: 

      The alternative domain names to use with your TLS/SSL certificate (e.g., ``www.example.com`` , ``www.ejemplo.com`` , ``ejemplo.com`` ).

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An object containing information about the API operations.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

  .. py:method:: create_load_balancer_tls_certificate(**kwargs)

    

    Creates a Lightsail load balancer TLS certificate.

     

    TLS is just an updated, more secure version of Secure Socket Layer (SSL).

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateLoadBalancerTlsCertificate>`_    


    **Request Syntax** 
    ::

      response = client.create_load_balancer_tls_certificate(
          loadBalancerName='string',
          certificateName='string',
          certificateDomainName='string',
          certificateAlternativeNames=[
              'string',
          ]
      )
    :type loadBalancerName: string
    :param loadBalancerName: **[REQUIRED]** 

      The load balancer name where you want to create the TLS/SSL certificate.

      

    
    :type certificateName: string
    :param certificateName: **[REQUIRED]** 

      The TLS/SSL certificate name.

      

    
    :type certificateDomainName: string
    :param certificateDomainName: **[REQUIRED]** 

      The domain name (e.g., ``example.com`` ) for your TLS/SSL certificate.

      

    
    :type certificateAlternativeNames: list
    :param certificateAlternativeNames: 

      An array of strings listing alternative domain names for your TLS/SSL certificate.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An object containing information about the API operations.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

  .. py:method:: delete_disk(**kwargs)

    

    Deletes the specified block storage disk. The disk must be in the ``available`` state (not attached to a Lightsail instance).

     

    .. note::

       

      The disk may remain in the ``deleting`` state for several minutes.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DeleteDisk>`_    


    **Request Syntax** 
    ::

      response = client.delete_disk(
          diskName='string'
      )
    :type diskName: string
    :param diskName: **[REQUIRED]** 

      The unique name of the disk you want to delete (e.g., ``my-disk`` ).

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An object describing the API operations.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

  .. py:method:: delete_disk_snapshot(**kwargs)

    

    Deletes the specified disk snapshot.

     

    When you make periodic snapshots of a disk, the snapshots are incremental, and only the blocks on the device that have changed since your last snapshot are saved in the new snapshot. When you delete a snapshot, only the data not needed for any other snapshot is removed. So regardless of which prior snapshots have been deleted, all active snapshots will have access to all the information needed to restore the disk.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DeleteDiskSnapshot>`_    


    **Request Syntax** 
    ::

      response = client.delete_disk_snapshot(
          diskSnapshotName='string'
      )
    :type diskSnapshotName: string
    :param diskSnapshotName: **[REQUIRED]** 

      The name of the disk snapshot you want to delete (e.g., ``my-disk-snapshot`` ).

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An object describing the API operations.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

  .. py:method:: delete_domain(**kwargs)

    

    Deletes the specified domain recordset and all of its domain records.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DeleteDomain>`_    


    **Request Syntax** 
    ::

      response = client.delete_domain(
          domainName='string'
      )
    :type domainName: string
    :param domainName: **[REQUIRED]** 

      The specific domain name to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operation': {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operation** *(dict) --* 

          An array of key-value pairs containing information about the results of your delete domain request.

          
          

          - **id** *(string) --* 

            The ID of the operation.

            
          

          - **resourceName** *(string) --* 

            The resource name.

            
          

          - **resourceType** *(string) --* 

            The resource type. 

            
          

          - **createdAt** *(datetime) --* 

            The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

            
          

          - **location** *(dict) --* 

            The region and Availability Zone.

            
            

            - **availabilityZone** *(string) --* 

              The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

              
            

            - **regionName** *(string) --* 

              The AWS Region name.

              
        
          

          - **isTerminal** *(boolean) --* 

            A Boolean value indicating whether the operation is terminal.

            
          

          - **operationDetails** *(string) --* 

            Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

            
          

          - **operationType** *(string) --* 

            The type of operation. 

            
          

          - **status** *(string) --* 

            The status of the operation. 

            
          

          - **statusChangedAt** *(datetime) --* 

            The timestamp when the status was changed (e.g., ``1479816991.349`` ).

            
          

          - **errorCode** *(string) --* 

            The error code.

            
          

          - **errorDetails** *(string) --* 

            The error details.

            
      
    

  .. py:method:: delete_domain_entry(**kwargs)

    

    Deletes a specific domain entry.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DeleteDomainEntry>`_    


    **Request Syntax** 
    ::

      response = client.delete_domain_entry(
          domainName='string',
          domainEntry={
              'id': 'string',
              'name': 'string',
              'target': 'string',
              'isAlias': True|False,
              'type': 'string',
              'options': {
                  'string': 'string'
              }
          }
      )
    :type domainName: string
    :param domainName: **[REQUIRED]** 

      The name of the domain entry to delete.

      

    
    :type domainEntry: dict
    :param domainEntry: **[REQUIRED]** 

      An array of key-value pairs containing information about your domain entries.

      

    
      - **id** *(string) --* 

        The ID of the domain recordset entry.

        

      
      - **name** *(string) --* 

        The name of the domain.

        

      
      - **target** *(string) --* 

        The target AWS name server (e.g., ``ns-111.awsdns-22.com.`` ).

        

      
      - **isAlias** *(boolean) --* 

        When ``true`` , specifies whether the domain entry is an alias used by the Lightsail load balancer.

        

      
      - **type** *(string) --* 

        The type of domain entry (e.g., ``SOA`` or ``NS`` ).

        

      
      - **options** *(dict) --* 

        (Deprecated) The options for the domain entry.

         

        .. note::

           

          In releases prior to November 29, 2017, this parameter was not included in the API response. It is now deprecated.

           

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operation': {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operation** *(dict) --* 

          An array of key-value pairs containing information about the results of your delete domain entry request.

          
          

          - **id** *(string) --* 

            The ID of the operation.

            
          

          - **resourceName** *(string) --* 

            The resource name.

            
          

          - **resourceType** *(string) --* 

            The resource type. 

            
          

          - **createdAt** *(datetime) --* 

            The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

            
          

          - **location** *(dict) --* 

            The region and Availability Zone.

            
            

            - **availabilityZone** *(string) --* 

              The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

              
            

            - **regionName** *(string) --* 

              The AWS Region name.

              
        
          

          - **isTerminal** *(boolean) --* 

            A Boolean value indicating whether the operation is terminal.

            
          

          - **operationDetails** *(string) --* 

            Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

            
          

          - **operationType** *(string) --* 

            The type of operation. 

            
          

          - **status** *(string) --* 

            The status of the operation. 

            
          

          - **statusChangedAt** *(datetime) --* 

            The timestamp when the status was changed (e.g., ``1479816991.349`` ).

            
          

          - **errorCode** *(string) --* 

            The error code.

            
          

          - **errorDetails** *(string) --* 

            The error details.

            
      
    

  .. py:method:: delete_instance(**kwargs)

    

    Deletes a specific Amazon Lightsail virtual private server, or *instance* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DeleteInstance>`_    


    **Request Syntax** 
    ::

      response = client.delete_instance(
          instanceName='string'
      )
    :type instanceName: string
    :param instanceName: **[REQUIRED]** 

      The name of the instance to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An array of key-value pairs containing information about the results of your delete instance request.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

  .. py:method:: delete_instance_snapshot(**kwargs)

    

    Deletes a specific snapshot of a virtual private server (or *instance* ).

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DeleteInstanceSnapshot>`_    


    **Request Syntax** 
    ::

      response = client.delete_instance_snapshot(
          instanceSnapshotName='string'
      )
    :type instanceSnapshotName: string
    :param instanceSnapshotName: **[REQUIRED]** 

      The name of the snapshot to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An array of key-value pairs containing information about the results of your delete instance snapshot request.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

  .. py:method:: delete_key_pair(**kwargs)

    

    Deletes a specific SSH key pair.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DeleteKeyPair>`_    


    **Request Syntax** 
    ::

      response = client.delete_key_pair(
          keyPairName='string'
      )
    :type keyPairName: string
    :param keyPairName: **[REQUIRED]** 

      The name of the key pair to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operation': {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operation** *(dict) --* 

          An array of key-value pairs containing information about the results of your delete key pair request.

          
          

          - **id** *(string) --* 

            The ID of the operation.

            
          

          - **resourceName** *(string) --* 

            The resource name.

            
          

          - **resourceType** *(string) --* 

            The resource type. 

            
          

          - **createdAt** *(datetime) --* 

            The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

            
          

          - **location** *(dict) --* 

            The region and Availability Zone.

            
            

            - **availabilityZone** *(string) --* 

              The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

              
            

            - **regionName** *(string) --* 

              The AWS Region name.

              
        
          

          - **isTerminal** *(boolean) --* 

            A Boolean value indicating whether the operation is terminal.

            
          

          - **operationDetails** *(string) --* 

            Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

            
          

          - **operationType** *(string) --* 

            The type of operation. 

            
          

          - **status** *(string) --* 

            The status of the operation. 

            
          

          - **statusChangedAt** *(datetime) --* 

            The timestamp when the status was changed (e.g., ``1479816991.349`` ).

            
          

          - **errorCode** *(string) --* 

            The error code.

            
          

          - **errorDetails** *(string) --* 

            The error details.

            
      
    

  .. py:method:: delete_load_balancer(**kwargs)

    

    Deletes a Lightsail load balancer.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DeleteLoadBalancer>`_    


    **Request Syntax** 
    ::

      response = client.delete_load_balancer(
          loadBalancerName='string'
      )
    :type loadBalancerName: string
    :param loadBalancerName: **[REQUIRED]** 

      The name of the load balancer you want to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An object describing the API operations.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

  .. py:method:: delete_load_balancer_tls_certificate(**kwargs)

    

    Deletes a TLS/SSL certificate associated with a Lightsail load balancer.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DeleteLoadBalancerTlsCertificate>`_    


    **Request Syntax** 
    ::

      response = client.delete_load_balancer_tls_certificate(
          loadBalancerName='string',
          certificateName='string',
          force=True|False
      )
    :type loadBalancerName: string
    :param loadBalancerName: **[REQUIRED]** 

      The load balancer name.

      

    
    :type certificateName: string
    :param certificateName: **[REQUIRED]** 

      The TLS/SSL certificate name.

      

    
    :type force: boolean
    :param force: 

      When ``true`` , forces the deletion of a TLS/SSL certificate.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An object describing the API operations.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

  .. py:method:: detach_disk(**kwargs)

    

    Detaches a stopped block storage disk from a Lightsail instance. Make sure to unmount any file systems on the device within your operating system before stopping the instance and detaching the disk.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DetachDisk>`_    


    **Request Syntax** 
    ::

      response = client.detach_disk(
          diskName='string'
      )
    :type diskName: string
    :param diskName: **[REQUIRED]** 

      The unique name of the disk you want to detach from your instance (e.g., ``my-disk`` ).

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An object describing the API operations.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

  .. py:method:: detach_instances_from_load_balancer(**kwargs)

    

    Detaches the specified instances from a Lightsail load balancer.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DetachInstancesFromLoadBalancer>`_    


    **Request Syntax** 
    ::

      response = client.detach_instances_from_load_balancer(
          loadBalancerName='string',
          instanceNames=[
              'string',
          ]
      )
    :type loadBalancerName: string
    :param loadBalancerName: **[REQUIRED]** 

      The name of the Lightsail load balancer.

      

    
    :type instanceNames: list
    :param instanceNames: **[REQUIRED]** 

      An array of strings containing the names of the instances you want to detach from the load balancer.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An object describing the API operations.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

  .. py:method:: detach_static_ip(**kwargs)

    

    Detaches a static IP from the Amazon Lightsail instance to which it is attached.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DetachStaticIp>`_    


    **Request Syntax** 
    ::

      response = client.detach_static_ip(
          staticIpName='string'
      )
    :type staticIpName: string
    :param staticIpName: **[REQUIRED]** 

      The name of the static IP to detach from the instance.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An array of key-value pairs containing information about the results of your detach static IP request.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

  .. py:method:: download_default_key_pair()

    

    Downloads the default SSH key pair from the user's account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/DownloadDefaultKeyPair>`_    


    **Request Syntax** 
    ::

      response = client.download_default_key_pair()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'publicKeyBase64': 'string',
            'privateKeyBase64': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **publicKeyBase64** *(string) --* 

          A base64-encoded public key of the ``ssh-rsa`` type.

          
        

        - **privateKeyBase64** *(string) --* 

          A base64-encoded RSA private key.

          
    

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


  .. py:method:: get_active_names(**kwargs)

    

    Returns the names of all active (not deleted) resources.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetActiveNames>`_    


    **Request Syntax** 
    ::

      response = client.get_active_names(
          pageToken='string'
      )
    :type pageToken: string
    :param pageToken: 

      A token used for paginating results from your get active names request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'activeNames': [
                'string',
            ],
            'nextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **activeNames** *(list) --* 

          The list of active names returned by the get active names request.

          
          

          - *(string) --* 
      
        

        - **nextPageToken** *(string) --* 

          A token used for advancing to the next page of results from your get active names request.

          
    

  .. py:method:: get_blueprints(**kwargs)

    

    Returns the list of available instance images, or *blueprints* . You can use a blueprint to create a new virtual private server already running a specific operating system, as well as a preinstalled app or development stack. The software each instance is running depends on the blueprint image you choose.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetBlueprints>`_    


    **Request Syntax** 
    ::

      response = client.get_blueprints(
          includeInactive=True|False,
          pageToken='string'
      )
    :type includeInactive: boolean
    :param includeInactive: 

      A Boolean value indicating whether to include inactive results in your request.

      

    
    :type pageToken: string
    :param pageToken: 

      A token used for advancing to the next page of results from your get blueprints request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'blueprints': [
                {
                    'blueprintId': 'string',
                    'name': 'string',
                    'group': 'string',
                    'type': 'os'|'app',
                    'description': 'string',
                    'isActive': True|False,
                    'minPower': 123,
                    'version': 'string',
                    'versionCode': 'string',
                    'productUrl': 'string',
                    'licenseUrl': 'string',
                    'platform': 'LINUX_UNIX'|'WINDOWS'
                },
            ],
            'nextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **blueprints** *(list) --* 

          An array of key-value pairs that contains information about the available blueprints.

          
          

          - *(dict) --* 

            Describes a blueprint (a virtual private server image).

            
            

            - **blueprintId** *(string) --* 

              The ID for the virtual private server image (e.g., ``app_wordpress_4_4`` or ``app_lamp_7_0`` ).

              
            

            - **name** *(string) --* 

              The friendly name of the blueprint (e.g., ``Amazon Linux`` ).

              
            

            - **group** *(string) --* 

              The group name of the blueprint (e.g., ``amazon-linux`` ).

              
            

            - **type** *(string) --* 

              The type of the blueprint (e.g., ``os`` or ``app`` ).

              
            

            - **description** *(string) --* 

              The description of the blueprint.

              
            

            - **isActive** *(boolean) --* 

              A Boolean value indicating whether the blueprint is active. When you update your blueprints, you will inactivate old blueprints and keep the most recent versions active.

              
            

            - **minPower** *(integer) --* 

              The minimum bundle power required to run this blueprint. For example, you need a bundle with a power value of 500 or more to create an instance that uses a blueprint with a minimum power value of 500. ``0`` indicates that the blueprint runs on all instance sizes. 

              
            

            - **version** *(string) --* 

              The version number of the operating system, application, or stack (e.g., ``2016.03.0`` ).

              
            

            - **versionCode** *(string) --* 

              The version code.

              
            

            - **productUrl** *(string) --* 

              The product URL to learn more about the image or blueprint.

              
            

            - **licenseUrl** *(string) --* 

              The end-user license agreement URL for the image or blueprint.

              
            

            - **platform** *(string) --* 

              The operating system platform (either Linux/Unix-based or Windows Server-based) of the blueprint.

              
        
      
        

        - **nextPageToken** *(string) --* 

          A token used for advancing to the next page of results from your get blueprints request.

          
    

  .. py:method:: get_bundles(**kwargs)

    

    Returns the list of bundles that are available for purchase. A bundle describes the specs for your virtual private server (or *instance* ).

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetBundles>`_    


    **Request Syntax** 
    ::

      response = client.get_bundles(
          includeInactive=True|False,
          pageToken='string'
      )
    :type includeInactive: boolean
    :param includeInactive: 

      A Boolean value that indicates whether to include inactive bundle results in your request.

      

    
    :type pageToken: string
    :param pageToken: 

      A token used for advancing to the next page of results from your get bundles request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'bundles': [
                {
                    'price': ...,
                    'cpuCount': 123,
                    'diskSizeInGb': 123,
                    'bundleId': 'string',
                    'instanceType': 'string',
                    'isActive': True|False,
                    'name': 'string',
                    'power': 123,
                    'ramSizeInGb': ...,
                    'transferPerMonthInGb': 123,
                    'supportedPlatforms': [
                        'LINUX_UNIX'|'WINDOWS',
                    ]
                },
            ],
            'nextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **bundles** *(list) --* 

          An array of key-value pairs that contains information about the available bundles.

          
          

          - *(dict) --* 

            Describes a bundle, which is a set of specs describing your virtual private server (or *instance* ).

            
            

            - **price** *(float) --* 

              The price in US dollars (e.g., ``5.0`` ).

              
            

            - **cpuCount** *(integer) --* 

              The number of vCPUs included in the bundle (e.g., ``2`` ).

              
            

            - **diskSizeInGb** *(integer) --* 

              The size of the SSD (e.g., ``30`` ).

              
            

            - **bundleId** *(string) --* 

              The bundle ID (e.g., ``micro_1_0`` ).

              
            

            - **instanceType** *(string) --* 

              The Amazon EC2 instance type (e.g., ``t2.micro`` ).

              
            

            - **isActive** *(boolean) --* 

              A Boolean value indicating whether the bundle is active.

              
            

            - **name** *(string) --* 

              A friendly name for the bundle (e.g., ``Micro`` ).

              
            

            - **power** *(integer) --* 

              A numeric value that represents the power of the bundle (e.g., ``500`` ). You can use the bundle's power value in conjunction with a blueprint's minimum power value to determine whether the blueprint will run on the bundle. For example, you need a bundle with a power value of 500 or more to create an instance that uses a blueprint with a minimum power value of 500.

              
            

            - **ramSizeInGb** *(float) --* 

              The amount of RAM in GB (e.g., ``2.0`` ).

              
            

            - **transferPerMonthInGb** *(integer) --* 

              The data transfer rate per month in GB (e.g., ``2000`` ).

              
            

            - **supportedPlatforms** *(list) --* 

              The operating system platform (Linux/Unix-based or Windows Server-based) that the bundle supports. You can only launch a ``WINDOWS`` bundle on a blueprint that supports the ``WINDOWS`` platform. ``LINUX_UNIX`` blueprints require a ``LINUX_UNIX`` bundle.

              
              

              - *(string) --* 
          
        
      
        

        - **nextPageToken** *(string) --* 

          A token used for advancing to the next page of results from your get active names request.

          
    

  .. py:method:: get_disk(**kwargs)

    

    Returns information about a specific block storage disk.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetDisk>`_    


    **Request Syntax** 
    ::

      response = client.get_disk(
          diskName='string'
      )
    :type diskName: string
    :param diskName: **[REQUIRED]** 

      The name of the disk (e.g., ``my-disk`` ).

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'disk': {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                'sizeInGb': 123,
                'isSystemDisk': True|False,
                'iops': 123,
                'path': 'string',
                'state': 'pending'|'error'|'available'|'in-use'|'unknown',
                'attachedTo': 'string',
                'isAttached': True|False,
                'attachmentState': 'string',
                'gbInUse': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **disk** *(dict) --* 

          An object containing information about the disk.

          
          

          - **name** *(string) --* 

            The unique name of the disk.

            
          

          - **arn** *(string) --* 

            The Amazon Resource Name (ARN) of the disk.

            
          

          - **supportCode** *(string) --* 

            The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

            
          

          - **createdAt** *(datetime) --* 

            The date when the disk was created.

            
          

          - **location** *(dict) --* 

            The AWS Region and Availability Zone where the disk is located.

            
            

            - **availabilityZone** *(string) --* 

              The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

              
            

            - **regionName** *(string) --* 

              The AWS Region name.

              
        
          

          - **resourceType** *(string) --* 

            The Lightsail resource type (e.g., ``Disk`` ).

            
          

          - **sizeInGb** *(integer) --* 

            The size of the disk in GB.

            
          

          - **isSystemDisk** *(boolean) --* 

            A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).

            
          

          - **iops** *(integer) --* 

            The input/output operations per second (IOPS) of the disk.

            
          

          - **path** *(string) --* 

            The disk path.

            
          

          - **state** *(string) --* 

            Describes the status of the disk.

            
          

          - **attachedTo** *(string) --* 

            The resources to which the disk is attached.

            
          

          - **isAttached** *(boolean) --* 

            A Boolean value indicating whether the disk is attached.

            
          

          - **attachmentState** *(string) --* 

            (Deprecated) The attachment state of the disk.

             

            .. note::

               

              In releases prior to November 14, 2017, this parameter returned ``attached`` for system disks in the API response. It is now deprecated, but still included in the response. Use ``isAttached`` instead.

               

            
          

          - **gbInUse** *(integer) --* 

            (Deprecated) The number of GB in use by the disk.

             

            .. note::

               

              In releases prior to November 14, 2017, this parameter was not included in the API response. It is now deprecated.

               

            
      
    

  .. py:method:: get_disk_snapshot(**kwargs)

    

    Returns information about a specific block storage disk snapshot.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetDiskSnapshot>`_    


    **Request Syntax** 
    ::

      response = client.get_disk_snapshot(
          diskSnapshotName='string'
      )
    :type diskSnapshotName: string
    :param diskSnapshotName: **[REQUIRED]** 

      The name of the disk snapshot (e.g., ``my-disk-snapshot`` ).

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'diskSnapshot': {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                'sizeInGb': 123,
                'state': 'pending'|'completed'|'error'|'unknown',
                'progress': 'string',
                'fromDiskName': 'string',
                'fromDiskArn': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **diskSnapshot** *(dict) --* 

          An object containing information about the disk snapshot.

          
          

          - **name** *(string) --* 

            The name of the disk snapshot (e.g., ``my-disk-snapshot`` ).

            
          

          - **arn** *(string) --* 

            The Amazon Resource Name (ARN) of the disk snapshot.

            
          

          - **supportCode** *(string) --* 

            The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

            
          

          - **createdAt** *(datetime) --* 

            The date when the disk snapshot was created.

            
          

          - **location** *(dict) --* 

            The AWS Region and Availability Zone where the disk snapshot was created.

            
            

            - **availabilityZone** *(string) --* 

              The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

              
            

            - **regionName** *(string) --* 

              The AWS Region name.

              
        
          

          - **resourceType** *(string) --* 

            The Lightsail resource type (e.g., ``DiskSnapshot`` ).

            
          

          - **sizeInGb** *(integer) --* 

            The size of the disk in GB.

            
          

          - **state** *(string) --* 

            The status of the disk snapshot operation.

            
          

          - **progress** *(string) --* 

            The progress of the disk snapshot operation.

            
          

          - **fromDiskName** *(string) --* 

            The unique name of the source disk from which you are creating the disk snapshot.

            
          

          - **fromDiskArn** *(string) --* 

            The Amazon Resource Name (ARN) of the source disk from which you are creating the disk snapshot.

            
      
    

  .. py:method:: get_disk_snapshots(**kwargs)

    

    Returns information about all block storage disk snapshots in your AWS account and region.

     

    If you are describing a long list of disk snapshots, you can paginate the output to make the list more manageable. You can use the pageToken and nextPageToken values to retrieve the next items in the list.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetDiskSnapshots>`_    


    **Request Syntax** 
    ::

      response = client.get_disk_snapshots(
          pageToken='string'
      )
    :type pageToken: string
    :param pageToken: 

      A token used for advancing to the next page of results from your GetDiskSnapshots request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'diskSnapshots': [
                {
                    'name': 'string',
                    'arn': 'string',
                    'supportCode': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'sizeInGb': 123,
                    'state': 'pending'|'completed'|'error'|'unknown',
                    'progress': 'string',
                    'fromDiskName': 'string',
                    'fromDiskArn': 'string'
                },
            ],
            'nextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **diskSnapshots** *(list) --* 

          An array of objects containing information about all block storage disk snapshots.

          
          

          - *(dict) --* 

            Describes a block storage disk snapshot.

            
            

            - **name** *(string) --* 

              The name of the disk snapshot (e.g., ``my-disk-snapshot`` ).

              
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the disk snapshot.

              
            

            - **supportCode** *(string) --* 

              The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

              
            

            - **createdAt** *(datetime) --* 

              The date when the disk snapshot was created.

              
            

            - **location** *(dict) --* 

              The AWS Region and Availability Zone where the disk snapshot was created.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **resourceType** *(string) --* 

              The Lightsail resource type (e.g., ``DiskSnapshot`` ).

              
            

            - **sizeInGb** *(integer) --* 

              The size of the disk in GB.

              
            

            - **state** *(string) --* 

              The status of the disk snapshot operation.

              
            

            - **progress** *(string) --* 

              The progress of the disk snapshot operation.

              
            

            - **fromDiskName** *(string) --* 

              The unique name of the source disk from which you are creating the disk snapshot.

              
            

            - **fromDiskArn** *(string) --* 

              The Amazon Resource Name (ARN) of the source disk from which you are creating the disk snapshot.

              
        
      
        

        - **nextPageToken** *(string) --* 

          A token used for advancing to the next page of results from your GetDiskSnapshots request.

          
    

  .. py:method:: get_disks(**kwargs)

    

    Returns information about all block storage disks in your AWS account and region.

     

    If you are describing a long list of disks, you can paginate the output to make the list more manageable. You can use the pageToken and nextPageToken values to retrieve the next items in the list.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetDisks>`_    


    **Request Syntax** 
    ::

      response = client.get_disks(
          pageToken='string'
      )
    :type pageToken: string
    :param pageToken: 

      A token used for advancing to the next page of results from your GetDisks request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'disks': [
                {
                    'name': 'string',
                    'arn': 'string',
                    'supportCode': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'sizeInGb': 123,
                    'isSystemDisk': True|False,
                    'iops': 123,
                    'path': 'string',
                    'state': 'pending'|'error'|'available'|'in-use'|'unknown',
                    'attachedTo': 'string',
                    'isAttached': True|False,
                    'attachmentState': 'string',
                    'gbInUse': 123
                },
            ],
            'nextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **disks** *(list) --* 

          An array of objects containing information about all block storage disks.

          
          

          - *(dict) --* 

            Describes a system disk or an block storage disk.

            
            

            - **name** *(string) --* 

              The unique name of the disk.

              
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the disk.

              
            

            - **supportCode** *(string) --* 

              The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

              
            

            - **createdAt** *(datetime) --* 

              The date when the disk was created.

              
            

            - **location** *(dict) --* 

              The AWS Region and Availability Zone where the disk is located.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **resourceType** *(string) --* 

              The Lightsail resource type (e.g., ``Disk`` ).

              
            

            - **sizeInGb** *(integer) --* 

              The size of the disk in GB.

              
            

            - **isSystemDisk** *(boolean) --* 

              A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).

              
            

            - **iops** *(integer) --* 

              The input/output operations per second (IOPS) of the disk.

              
            

            - **path** *(string) --* 

              The disk path.

              
            

            - **state** *(string) --* 

              Describes the status of the disk.

              
            

            - **attachedTo** *(string) --* 

              The resources to which the disk is attached.

              
            

            - **isAttached** *(boolean) --* 

              A Boolean value indicating whether the disk is attached.

              
            

            - **attachmentState** *(string) --* 

              (Deprecated) The attachment state of the disk.

               

              .. note::

                 

                In releases prior to November 14, 2017, this parameter returned ``attached`` for system disks in the API response. It is now deprecated, but still included in the response. Use ``isAttached`` instead.

                 

              
            

            - **gbInUse** *(integer) --* 

              (Deprecated) The number of GB in use by the disk.

               

              .. note::

                 

                In releases prior to November 14, 2017, this parameter was not included in the API response. It is now deprecated.

                 

              
        
      
        

        - **nextPageToken** *(string) --* 

          A token used for advancing to the next page of results from your GetDisks request.

          
    

  .. py:method:: get_domain(**kwargs)

    

    Returns information about a specific domain recordset.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetDomain>`_    


    **Request Syntax** 
    ::

      response = client.get_domain(
          domainName='string'
      )
    :type domainName: string
    :param domainName: **[REQUIRED]** 

      The domain name for which your want to return information about.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'domain': {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                'domainEntries': [
                    {
                        'id': 'string',
                        'name': 'string',
                        'target': 'string',
                        'isAlias': True|False,
                        'type': 'string',
                        'options': {
                            'string': 'string'
                        }
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **domain** *(dict) --* 

          An array of key-value pairs containing information about your get domain request.

          
          

          - **name** *(string) --* 

            The name of the domain.

            
          

          - **arn** *(string) --* 

            The Amazon Resource Name (ARN) of the domain recordset (e.g., ``arn:aws:lightsail:global:123456789101:Domain/824cede0-abc7-4f84-8dbc-12345EXAMPLE`` ).

            
          

          - **supportCode** *(string) --* 

            The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

            
          

          - **createdAt** *(datetime) --* 

            The date when the domain recordset was created.

            
          

          - **location** *(dict) --* 

            The AWS Region and Availability Zones where the domain recordset was created.

            
            

            - **availabilityZone** *(string) --* 

              The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

              
            

            - **regionName** *(string) --* 

              The AWS Region name.

              
        
          

          - **resourceType** *(string) --* 

            The resource type. 

            
          

          - **domainEntries** *(list) --* 

            An array of key-value pairs containing information about the domain entries.

            
            

            - *(dict) --* 

              Describes a domain recordset entry.

              
              

              - **id** *(string) --* 

                The ID of the domain recordset entry.

                
              

              - **name** *(string) --* 

                The name of the domain.

                
              

              - **target** *(string) --* 

                The target AWS name server (e.g., ``ns-111.awsdns-22.com.`` ).

                
              

              - **isAlias** *(boolean) --* 

                When ``true`` , specifies whether the domain entry is an alias used by the Lightsail load balancer.

                
              

              - **type** *(string) --* 

                The type of domain entry (e.g., ``SOA`` or ``NS`` ).

                
              

              - **options** *(dict) --* 

                (Deprecated) The options for the domain entry.

                 

                .. note::

                   

                  In releases prior to November 29, 2017, this parameter was not included in the API response. It is now deprecated.

                   

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
          
        
      
    

  .. py:method:: get_domains(**kwargs)

    

    Returns a list of all domains in the user's account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetDomains>`_    


    **Request Syntax** 
    ::

      response = client.get_domains(
          pageToken='string'
      )
    :type pageToken: string
    :param pageToken: 

      A token used for advancing to the next page of results from your get domains request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'domains': [
                {
                    'name': 'string',
                    'arn': 'string',
                    'supportCode': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'domainEntries': [
                        {
                            'id': 'string',
                            'name': 'string',
                            'target': 'string',
                            'isAlias': True|False,
                            'type': 'string',
                            'options': {
                                'string': 'string'
                            }
                        },
                    ]
                },
            ],
            'nextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **domains** *(list) --* 

          An array of key-value pairs containing information about each of the domain entries in the user's account.

          
          

          - *(dict) --* 

            Describes a domain where you are storing recordsets in Lightsail.

            
            

            - **name** *(string) --* 

              The name of the domain.

              
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the domain recordset (e.g., ``arn:aws:lightsail:global:123456789101:Domain/824cede0-abc7-4f84-8dbc-12345EXAMPLE`` ).

              
            

            - **supportCode** *(string) --* 

              The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

              
            

            - **createdAt** *(datetime) --* 

              The date when the domain recordset was created.

              
            

            - **location** *(dict) --* 

              The AWS Region and Availability Zones where the domain recordset was created.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **domainEntries** *(list) --* 

              An array of key-value pairs containing information about the domain entries.

              
              

              - *(dict) --* 

                Describes a domain recordset entry.

                
                

                - **id** *(string) --* 

                  The ID of the domain recordset entry.

                  
                

                - **name** *(string) --* 

                  The name of the domain.

                  
                

                - **target** *(string) --* 

                  The target AWS name server (e.g., ``ns-111.awsdns-22.com.`` ).

                  
                

                - **isAlias** *(boolean) --* 

                  When ``true`` , specifies whether the domain entry is an alias used by the Lightsail load balancer.

                  
                

                - **type** *(string) --* 

                  The type of domain entry (e.g., ``SOA`` or ``NS`` ).

                  
                

                - **options** *(dict) --* 

                  (Deprecated) The options for the domain entry.

                   

                  .. note::

                     

                    In releases prior to November 29, 2017, this parameter was not included in the API response. It is now deprecated.

                     

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
            
          
        
      
        

        - **nextPageToken** *(string) --* 

          A token used for advancing to the next page of results from your get active names request.

          
    

  .. py:method:: get_instance(**kwargs)

    

    Returns information about a specific Amazon Lightsail instance, which is a virtual private server.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetInstance>`_    


    **Request Syntax** 
    ::

      response = client.get_instance(
          instanceName='string'
      )
    :type instanceName: string
    :param instanceName: **[REQUIRED]** 

      The name of the instance.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'instance': {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                'blueprintId': 'string',
                'blueprintName': 'string',
                'bundleId': 'string',
                'isStaticIp': True|False,
                'privateIpAddress': 'string',
                'publicIpAddress': 'string',
                'ipv6Address': 'string',
                'hardware': {
                    'cpuCount': 123,
                    'disks': [
                        {
                            'name': 'string',
                            'arn': 'string',
                            'supportCode': 'string',
                            'createdAt': datetime(2015, 1, 1),
                            'location': {
                                'availabilityZone': 'string',
                                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                            },
                            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                            'sizeInGb': 123,
                            'isSystemDisk': True|False,
                            'iops': 123,
                            'path': 'string',
                            'state': 'pending'|'error'|'available'|'in-use'|'unknown',
                            'attachedTo': 'string',
                            'isAttached': True|False,
                            'attachmentState': 'string',
                            'gbInUse': 123
                        },
                    ],
                    'ramSizeInGb': ...
                },
                'networking': {
                    'monthlyTransfer': {
                        'gbPerMonthAllocated': 123
                    },
                    'ports': [
                        {
                            'fromPort': 123,
                            'toPort': 123,
                            'protocol': 'tcp'|'all'|'udp',
                            'accessFrom': 'string',
                            'accessType': 'Public'|'Private',
                            'commonName': 'string',
                            'accessDirection': 'inbound'|'outbound'
                        },
                    ]
                },
                'state': {
                    'code': 123,
                    'name': 'string'
                },
                'username': 'string',
                'sshKeyName': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **instance** *(dict) --* 

          An array of key-value pairs containing information about the specified instance.

          
          

          - **name** *(string) --* 

            The name the user gave the instance (e.g., ``Amazon_Linux-1GB-Ohio-1`` ).

            
          

          - **arn** *(string) --* 

            The Amazon Resource Name (ARN) of the instance (e.g., ``arn:aws:lightsail:us-east-2:123456789101:Instance/244ad76f-8aad-4741-809f-12345EXAMPLE`` ).

            
          

          - **supportCode** *(string) --* 

            The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

            
          

          - **createdAt** *(datetime) --* 

            The timestamp when the instance was created (e.g., ``1479734909.17`` ).

            
          

          - **location** *(dict) --* 

            The region name and availability zone where the instance is located.

            
            

            - **availabilityZone** *(string) --* 

              The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

              
            

            - **regionName** *(string) --* 

              The AWS Region name.

              
        
          

          - **resourceType** *(string) --* 

            The type of resource (usually ``Instance`` ).

            
          

          - **blueprintId** *(string) --* 

            The blueprint ID (e.g., ``os_amlinux_2016_03`` ).

            
          

          - **blueprintName** *(string) --* 

            The friendly name of the blueprint (e.g., ``Amazon Linux`` ).

            
          

          - **bundleId** *(string) --* 

            The bundle for the instance (e.g., ``micro_1_0`` ).

            
          

          - **isStaticIp** *(boolean) --* 

            A Boolean value indicating whether this instance has a static IP assigned to it.

            
          

          - **privateIpAddress** *(string) --* 

            The private IP address of the instance.

            
          

          - **publicIpAddress** *(string) --* 

            The public IP address of the instance.

            
          

          - **ipv6Address** *(string) --* 

            The IPv6 address of the instance.

            
          

          - **hardware** *(dict) --* 

            The size of the vCPU and the amount of RAM for the instance.

            
            

            - **cpuCount** *(integer) --* 

              The number of vCPUs the instance has.

              
            

            - **disks** *(list) --* 

              The disks attached to the instance.

              
              

              - *(dict) --* 

                Describes a system disk or an block storage disk.

                
                

                - **name** *(string) --* 

                  The unique name of the disk.

                  
                

                - **arn** *(string) --* 

                  The Amazon Resource Name (ARN) of the disk.

                  
                

                - **supportCode** *(string) --* 

                  The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

                  
                

                - **createdAt** *(datetime) --* 

                  The date when the disk was created.

                  
                

                - **location** *(dict) --* 

                  The AWS Region and Availability Zone where the disk is located.

                  
                  

                  - **availabilityZone** *(string) --* 

                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                    
                  

                  - **regionName** *(string) --* 

                    The AWS Region name.

                    
              
                

                - **resourceType** *(string) --* 

                  The Lightsail resource type (e.g., ``Disk`` ).

                  
                

                - **sizeInGb** *(integer) --* 

                  The size of the disk in GB.

                  
                

                - **isSystemDisk** *(boolean) --* 

                  A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).

                  
                

                - **iops** *(integer) --* 

                  The input/output operations per second (IOPS) of the disk.

                  
                

                - **path** *(string) --* 

                  The disk path.

                  
                

                - **state** *(string) --* 

                  Describes the status of the disk.

                  
                

                - **attachedTo** *(string) --* 

                  The resources to which the disk is attached.

                  
                

                - **isAttached** *(boolean) --* 

                  A Boolean value indicating whether the disk is attached.

                  
                

                - **attachmentState** *(string) --* 

                  (Deprecated) The attachment state of the disk.

                   

                  .. note::

                     

                    In releases prior to November 14, 2017, this parameter returned ``attached`` for system disks in the API response. It is now deprecated, but still included in the response. Use ``isAttached`` instead.

                     

                  
                

                - **gbInUse** *(integer) --* 

                  (Deprecated) The number of GB in use by the disk.

                   

                  .. note::

                     

                    In releases prior to November 14, 2017, this parameter was not included in the API response. It is now deprecated.

                     

                  
            
          
            

            - **ramSizeInGb** *(float) --* 

              The amount of RAM in GB on the instance (e.g., ``1.0`` ).

              
        
          

          - **networking** *(dict) --* 

            Information about the public ports and monthly data transfer rates for the instance.

            
            

            - **monthlyTransfer** *(dict) --* 

              The amount of data in GB allocated for monthly data transfers.

              
              

              - **gbPerMonthAllocated** *(integer) --* 

                The amount allocated per month (in GB).

                
          
            

            - **ports** *(list) --* 

              An array of key-value pairs containing information about the ports on the instance.

              
              

              - *(dict) --* 

                Describes information about the instance ports.

                
                

                - **fromPort** *(integer) --* 

                  The first port in the range.

                  
                

                - **toPort** *(integer) --* 

                  The last port in the range.

                  
                

                - **protocol** *(string) --* 

                  The protocol being used. Can be one of the following.

                   

                   
                  * ``tcp`` - Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesn't require reliable data stream service, use UDP instead. 
                   
                  * ``all`` - All transport layer protocol types. For more general information, see `Transport layer <https://en.wikipedia.org/wiki/Transport_layer>`__ on Wikipedia. 
                   
                  * ``udp`` - With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that don't require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead. 
                   

                  
                

                - **accessFrom** *(string) --* 

                  The location from which access is allowed (e.g., ``Anywhere (0.0.0.0/0)`` ).

                  
                

                - **accessType** *(string) --* 

                  The type of access (``Public`` or ``Private`` ).

                  
                

                - **commonName** *(string) --* 

                  The common name.

                  
                

                - **accessDirection** *(string) --* 

                  The access direction (``inbound`` or ``outbound`` ).

                  
            
          
        
          

          - **state** *(dict) --* 

            The status code and the state (e.g., ``running`` ) for the instance.

            
            

            - **code** *(integer) --* 

              The status code for the instance.

              
            

            - **name** *(string) --* 

              The state of the instance (e.g., ``running`` or ``pending`` ).

              
        
          

          - **username** *(string) --* 

            The user name for connecting to the instance (e.g., ``ec2-user`` ).

            
          

          - **sshKeyName** *(string) --* 

            The name of the SSH key being used to connect to the instance (e.g., ``LightsailDefaultKeyPair`` ).

            
      
    

  .. py:method:: get_instance_access_details(**kwargs)

    

    Returns temporary SSH keys you can use to connect to a specific virtual private server, or *instance* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetInstanceAccessDetails>`_    


    **Request Syntax** 
    ::

      response = client.get_instance_access_details(
          instanceName='string',
          protocol='ssh'|'rdp'
      )
    :type instanceName: string
    :param instanceName: **[REQUIRED]** 

      The name of the instance to access.

      

    
    :type protocol: string
    :param protocol: 

      The protocol to use to connect to your instance. Defaults to ``ssh`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'accessDetails': {
                'certKey': 'string',
                'expiresAt': datetime(2015, 1, 1),
                'ipAddress': 'string',
                'password': 'string',
                'passwordData': {
                    'ciphertext': 'string',
                    'keyPairName': 'string'
                },
                'privateKey': 'string',
                'protocol': 'ssh'|'rdp',
                'instanceName': 'string',
                'username': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **accessDetails** *(dict) --* 

          An array of key-value pairs containing information about a get instance access request.

          
          

          - **certKey** *(string) --* 

            For SSH access, the public key to use when accessing your instance For OpenSSH clients (e.g., command line SSH), you should save this value to ``tempkey-cert.pub`` .

            
          

          - **expiresAt** *(datetime) --* 

            For SSH access, the date on which the temporary keys expire.

            
          

          - **ipAddress** *(string) --* 

            The public IP address of the Amazon Lightsail instance.

            
          

          - **password** *(string) --* 

            For RDP access, the password for your Amazon Lightsail instance. Password will be an empty string if the password for your new instance is not ready yet. When you create an instance, it can take up to 15 minutes for the instance to be ready.

             

            .. note::

               

              If you create an instance using any key pair other than the default (``LightsailDefaultKeyPair`` ), ``password`` will always be an empty string.

               

              If you change the Administrator password on the instance, Lightsail will continue to return the original password value. When accessing the instance using RDP, you need to manually enter the Administrator password after changing it from the default.

               

            
          

          - **passwordData** *(dict) --* 

            For a Windows Server-based instance, an object with the data you can use to retrieve your password. This is only needed if ``password`` is empty and the instance is not new (and therefore the password is not ready yet). When you create an instance, it can take up to 15 minutes for the instance to be ready.

            
            

            - **ciphertext** *(string) --* 

              The encrypted password. Ciphertext will be an empty string if access to your new instance is not ready yet. When you create an instance, it can take up to 15 minutes for the instance to be ready.

               

              .. note::

                 

                If you use the default key pair (``LightsailDefaultKeyPair`` ), the decrypted password will be available in the password field.

                 

                If you are using a custom key pair, you need to use your own means of decryption.

                 

                If you change the Administrator password on the instance, Lightsail will continue to return the original ciphertext value. When accessing the instance using RDP, you need to manually enter the Administrator password after changing it from the default.

                 

              
            

            - **keyPairName** *(string) --* 

              The name of the key pair that you used when creating your instance. If no key pair name was specified when creating the instance, Lightsail uses the default key pair (``LightsailDefaultKeyPair`` ).

               

              If you are using a custom key pair, you need to use your own means of decrypting your password using the ``ciphertext`` . Lightsail creates the ciphertext by encrypting your password with the public key part of this key pair.

              
        
          

          - **privateKey** *(string) --* 

            For SSH access, the temporary private key. For OpenSSH clients (e.g., command line SSH), you should save this value to ``tempkey`` ).

            
          

          - **protocol** *(string) --* 

            The protocol for these Amazon Lightsail instance access details.

            
          

          - **instanceName** *(string) --* 

            The name of this Amazon Lightsail instance.

            
          

          - **username** *(string) --* 

            The user name to use when logging in to the Amazon Lightsail instance.

            
      
    

  .. py:method:: get_instance_metric_data(**kwargs)

    

    Returns the data points for the specified Amazon Lightsail instance metric, given an instance name.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetInstanceMetricData>`_    


    **Request Syntax** 
    ::

      response = client.get_instance_metric_data(
          instanceName='string',
          metricName='CPUUtilization'|'NetworkIn'|'NetworkOut'|'StatusCheckFailed'|'StatusCheckFailed_Instance'|'StatusCheckFailed_System',
          period=123,
          startTime=datetime(2015, 1, 1),
          endTime=datetime(2015, 1, 1),
          unit='Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
          statistics=[
              'Minimum'|'Maximum'|'Sum'|'Average'|'SampleCount',
          ]
      )
    :type instanceName: string
    :param instanceName: **[REQUIRED]** 

      The name of the instance for which you want to get metrics data.

      

    
    :type metricName: string
    :param metricName: **[REQUIRED]** 

      The metric name to get data about. 

      

    
    :type period: integer
    :param period: **[REQUIRED]** 

      The time period for which you are requesting data.

      

    
    :type startTime: datetime
    :param startTime: **[REQUIRED]** 

      The start time of the time period.

      

    
    :type endTime: datetime
    :param endTime: **[REQUIRED]** 

      The end time of the time period.

      

    
    :type unit: string
    :param unit: **[REQUIRED]** 

      The unit. The list of valid values is below.

      

    
    :type statistics: list
    :param statistics: **[REQUIRED]** 

      The instance statistics. 

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'metricName': 'CPUUtilization'|'NetworkIn'|'NetworkOut'|'StatusCheckFailed'|'StatusCheckFailed_Instance'|'StatusCheckFailed_System',
            'metricData': [
                {
                    'average': 123.0,
                    'maximum': 123.0,
                    'minimum': 123.0,
                    'sampleCount': 123.0,
                    'sum': 123.0,
                    'timestamp': datetime(2015, 1, 1),
                    'unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **metricName** *(string) --* 

          The metric name to return data for.

          
        

        - **metricData** *(list) --* 

          An array of key-value pairs containing information about the results of your get instance metric data request.

          
          

          - *(dict) --* 

            Describes the metric data point.

            
            

            - **average** *(float) --* 

              The average.

              
            

            - **maximum** *(float) --* 

              The maximum.

              
            

            - **minimum** *(float) --* 

              The minimum.

              
            

            - **sampleCount** *(float) --* 

              The sample count.

              
            

            - **sum** *(float) --* 

              The sum.

              
            

            - **timestamp** *(datetime) --* 

              The timestamp (e.g., ``1479816991.349`` ).

              
            

            - **unit** *(string) --* 

              The unit. 

              
        
      
    

  .. py:method:: get_instance_port_states(**kwargs)

    

    Returns the port states for a specific virtual private server, or *instance* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetInstancePortStates>`_    


    **Request Syntax** 
    ::

      response = client.get_instance_port_states(
          instanceName='string'
      )
    :type instanceName: string
    :param instanceName: **[REQUIRED]** 

      The name of the instance.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'portStates': [
                {
                    'fromPort': 123,
                    'toPort': 123,
                    'protocol': 'tcp'|'all'|'udp',
                    'state': 'open'|'closed'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **portStates** *(list) --* 

          Information about the port states resulting from your request.

          
          

          - *(dict) --* 

            Describes the port state.

            
            

            - **fromPort** *(integer) --* 

              The first port in the range.

              
            

            - **toPort** *(integer) --* 

              The last port in the range.

              
            

            - **protocol** *(string) --* 

              The protocol being used. Can be one of the following.

               

               
              * ``tcp`` - Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesn't require reliable data stream service, use UDP instead. 
               
              * ``all`` - All transport layer protocol types. For more general information, see `Transport layer <https://en.wikipedia.org/wiki/Transport_layer>`__ on Wikipedia. 
               
              * ``udp`` - With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that don't require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead. 
               

              
            

            - **state** *(string) --* 

              Specifies whether the instance port is ``open`` or ``closed`` .

              
        
      
    

  .. py:method:: get_instance_snapshot(**kwargs)

    

    Returns information about a specific instance snapshot.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetInstanceSnapshot>`_    


    **Request Syntax** 
    ::

      response = client.get_instance_snapshot(
          instanceSnapshotName='string'
      )
    :type instanceSnapshotName: string
    :param instanceSnapshotName: **[REQUIRED]** 

      The name of the snapshot for which you are requesting information.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'instanceSnapshot': {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                'state': 'pending'|'error'|'available',
                'progress': 'string',
                'fromAttachedDisks': [
                    {
                        'name': 'string',
                        'arn': 'string',
                        'supportCode': 'string',
                        'createdAt': datetime(2015, 1, 1),
                        'location': {
                            'availabilityZone': 'string',
                            'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                        },
                        'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                        'sizeInGb': 123,
                        'isSystemDisk': True|False,
                        'iops': 123,
                        'path': 'string',
                        'state': 'pending'|'error'|'available'|'in-use'|'unknown',
                        'attachedTo': 'string',
                        'isAttached': True|False,
                        'attachmentState': 'string',
                        'gbInUse': 123
                    },
                ],
                'fromInstanceName': 'string',
                'fromInstanceArn': 'string',
                'fromBlueprintId': 'string',
                'fromBundleId': 'string',
                'sizeInGb': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **instanceSnapshot** *(dict) --* 

          An array of key-value pairs containing information about the results of your get instance snapshot request.

          
          

          - **name** *(string) --* 

            The name of the snapshot.

            
          

          - **arn** *(string) --* 

            The Amazon Resource Name (ARN) of the snapshot (e.g., ``arn:aws:lightsail:us-east-2:123456789101:InstanceSnapshot/d23b5706-3322-4d83-81e5-12345EXAMPLE`` ).

            
          

          - **supportCode** *(string) --* 

            The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

            
          

          - **createdAt** *(datetime) --* 

            The timestamp when the snapshot was created (e.g., ``1479907467.024`` ).

            
          

          - **location** *(dict) --* 

            The region name and availability zone where you created the snapshot.

            
            

            - **availabilityZone** *(string) --* 

              The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

              
            

            - **regionName** *(string) --* 

              The AWS Region name.

              
        
          

          - **resourceType** *(string) --* 

            The type of resource (usually ``InstanceSnapshot`` ).

            
          

          - **state** *(string) --* 

            The state the snapshot is in.

            
          

          - **progress** *(string) --* 

            The progress of the snapshot.

            
          

          - **fromAttachedDisks** *(list) --* 

            An array of disk objects containing information about all block storage disks.

            
            

            - *(dict) --* 

              Describes a system disk or an block storage disk.

              
              

              - **name** *(string) --* 

                The unique name of the disk.

                
              

              - **arn** *(string) --* 

                The Amazon Resource Name (ARN) of the disk.

                
              

              - **supportCode** *(string) --* 

                The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

                
              

              - **createdAt** *(datetime) --* 

                The date when the disk was created.

                
              

              - **location** *(dict) --* 

                The AWS Region and Availability Zone where the disk is located.

                
                

                - **availabilityZone** *(string) --* 

                  The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                  
                

                - **regionName** *(string) --* 

                  The AWS Region name.

                  
            
              

              - **resourceType** *(string) --* 

                The Lightsail resource type (e.g., ``Disk`` ).

                
              

              - **sizeInGb** *(integer) --* 

                The size of the disk in GB.

                
              

              - **isSystemDisk** *(boolean) --* 

                A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).

                
              

              - **iops** *(integer) --* 

                The input/output operations per second (IOPS) of the disk.

                
              

              - **path** *(string) --* 

                The disk path.

                
              

              - **state** *(string) --* 

                Describes the status of the disk.

                
              

              - **attachedTo** *(string) --* 

                The resources to which the disk is attached.

                
              

              - **isAttached** *(boolean) --* 

                A Boolean value indicating whether the disk is attached.

                
              

              - **attachmentState** *(string) --* 

                (Deprecated) The attachment state of the disk.

                 

                .. note::

                   

                  In releases prior to November 14, 2017, this parameter returned ``attached`` for system disks in the API response. It is now deprecated, but still included in the response. Use ``isAttached`` instead.

                   

                
              

              - **gbInUse** *(integer) --* 

                (Deprecated) The number of GB in use by the disk.

                 

                .. note::

                   

                  In releases prior to November 14, 2017, this parameter was not included in the API response. It is now deprecated.

                   

                
          
        
          

          - **fromInstanceName** *(string) --* 

            The instance from which the snapshot was created.

            
          

          - **fromInstanceArn** *(string) --* 

            The Amazon Resource Name (ARN) of the instance from which the snapshot was created (e.g., ``arn:aws:lightsail:us-east-2:123456789101:Instance/64b8404c-ccb1-430b-8daf-12345EXAMPLE`` ).

            
          

          - **fromBlueprintId** *(string) --* 

            The blueprint ID from which you created the snapshot (e.g., ``os_debian_8_3`` ). A blueprint is a virtual private server (or *instance* ) image used to create instances quickly.

            
          

          - **fromBundleId** *(string) --* 

            The bundle ID from which you created the snapshot (e.g., ``micro_1_0`` ).

            
          

          - **sizeInGb** *(integer) --* 

            The size in GB of the SSD.

            
      
    

  .. py:method:: get_instance_snapshots(**kwargs)

    

    Returns all instance snapshots for the user's account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetInstanceSnapshots>`_    


    **Request Syntax** 
    ::

      response = client.get_instance_snapshots(
          pageToken='string'
      )
    :type pageToken: string
    :param pageToken: 

      A token used for advancing to the next page of results from your get instance snapshots request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'instanceSnapshots': [
                {
                    'name': 'string',
                    'arn': 'string',
                    'supportCode': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'state': 'pending'|'error'|'available',
                    'progress': 'string',
                    'fromAttachedDisks': [
                        {
                            'name': 'string',
                            'arn': 'string',
                            'supportCode': 'string',
                            'createdAt': datetime(2015, 1, 1),
                            'location': {
                                'availabilityZone': 'string',
                                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                            },
                            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                            'sizeInGb': 123,
                            'isSystemDisk': True|False,
                            'iops': 123,
                            'path': 'string',
                            'state': 'pending'|'error'|'available'|'in-use'|'unknown',
                            'attachedTo': 'string',
                            'isAttached': True|False,
                            'attachmentState': 'string',
                            'gbInUse': 123
                        },
                    ],
                    'fromInstanceName': 'string',
                    'fromInstanceArn': 'string',
                    'fromBlueprintId': 'string',
                    'fromBundleId': 'string',
                    'sizeInGb': 123
                },
            ],
            'nextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **instanceSnapshots** *(list) --* 

          An array of key-value pairs containing information about the results of your get instance snapshots request.

          
          

          - *(dict) --* 

            Describes the snapshot of the virtual private server, or *instance* .

            
            

            - **name** *(string) --* 

              The name of the snapshot.

              
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the snapshot (e.g., ``arn:aws:lightsail:us-east-2:123456789101:InstanceSnapshot/d23b5706-3322-4d83-81e5-12345EXAMPLE`` ).

              
            

            - **supportCode** *(string) --* 

              The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the snapshot was created (e.g., ``1479907467.024`` ).

              
            

            - **location** *(dict) --* 

              The region name and availability zone where you created the snapshot.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **resourceType** *(string) --* 

              The type of resource (usually ``InstanceSnapshot`` ).

              
            

            - **state** *(string) --* 

              The state the snapshot is in.

              
            

            - **progress** *(string) --* 

              The progress of the snapshot.

              
            

            - **fromAttachedDisks** *(list) --* 

              An array of disk objects containing information about all block storage disks.

              
              

              - *(dict) --* 

                Describes a system disk or an block storage disk.

                
                

                - **name** *(string) --* 

                  The unique name of the disk.

                  
                

                - **arn** *(string) --* 

                  The Amazon Resource Name (ARN) of the disk.

                  
                

                - **supportCode** *(string) --* 

                  The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

                  
                

                - **createdAt** *(datetime) --* 

                  The date when the disk was created.

                  
                

                - **location** *(dict) --* 

                  The AWS Region and Availability Zone where the disk is located.

                  
                  

                  - **availabilityZone** *(string) --* 

                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                    
                  

                  - **regionName** *(string) --* 

                    The AWS Region name.

                    
              
                

                - **resourceType** *(string) --* 

                  The Lightsail resource type (e.g., ``Disk`` ).

                  
                

                - **sizeInGb** *(integer) --* 

                  The size of the disk in GB.

                  
                

                - **isSystemDisk** *(boolean) --* 

                  A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).

                  
                

                - **iops** *(integer) --* 

                  The input/output operations per second (IOPS) of the disk.

                  
                

                - **path** *(string) --* 

                  The disk path.

                  
                

                - **state** *(string) --* 

                  Describes the status of the disk.

                  
                

                - **attachedTo** *(string) --* 

                  The resources to which the disk is attached.

                  
                

                - **isAttached** *(boolean) --* 

                  A Boolean value indicating whether the disk is attached.

                  
                

                - **attachmentState** *(string) --* 

                  (Deprecated) The attachment state of the disk.

                   

                  .. note::

                     

                    In releases prior to November 14, 2017, this parameter returned ``attached`` for system disks in the API response. It is now deprecated, but still included in the response. Use ``isAttached`` instead.

                     

                  
                

                - **gbInUse** *(integer) --* 

                  (Deprecated) The number of GB in use by the disk.

                   

                  .. note::

                     

                    In releases prior to November 14, 2017, this parameter was not included in the API response. It is now deprecated.

                     

                  
            
          
            

            - **fromInstanceName** *(string) --* 

              The instance from which the snapshot was created.

              
            

            - **fromInstanceArn** *(string) --* 

              The Amazon Resource Name (ARN) of the instance from which the snapshot was created (e.g., ``arn:aws:lightsail:us-east-2:123456789101:Instance/64b8404c-ccb1-430b-8daf-12345EXAMPLE`` ).

              
            

            - **fromBlueprintId** *(string) --* 

              The blueprint ID from which you created the snapshot (e.g., ``os_debian_8_3`` ). A blueprint is a virtual private server (or *instance* ) image used to create instances quickly.

              
            

            - **fromBundleId** *(string) --* 

              The bundle ID from which you created the snapshot (e.g., ``micro_1_0`` ).

              
            

            - **sizeInGb** *(integer) --* 

              The size in GB of the SSD.

              
        
      
        

        - **nextPageToken** *(string) --* 

          A token used for advancing to the next page of results from your get instance snapshots request.

          
    

  .. py:method:: get_instance_state(**kwargs)

    

    Returns the state of a specific instance. Works on one instance at a time.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetInstanceState>`_    


    **Request Syntax** 
    ::

      response = client.get_instance_state(
          instanceName='string'
      )
    :type instanceName: string
    :param instanceName: **[REQUIRED]** 

      The name of the instance to get state information about.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'state': {
                'code': 123,
                'name': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **state** *(dict) --* 

          The state of the instance.

          
          

          - **code** *(integer) --* 

            The status code for the instance.

            
          

          - **name** *(string) --* 

            The state of the instance (e.g., ``running`` or ``pending`` ).

            
      
    

  .. py:method:: get_instances(**kwargs)

    

    Returns information about all Amazon Lightsail virtual private servers, or *instances* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetInstances>`_    


    **Request Syntax** 
    ::

      response = client.get_instances(
          pageToken='string'
      )
    :type pageToken: string
    :param pageToken: 

      A token used for advancing to the next page of results from your get instances request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'instances': [
                {
                    'name': 'string',
                    'arn': 'string',
                    'supportCode': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'blueprintId': 'string',
                    'blueprintName': 'string',
                    'bundleId': 'string',
                    'isStaticIp': True|False,
                    'privateIpAddress': 'string',
                    'publicIpAddress': 'string',
                    'ipv6Address': 'string',
                    'hardware': {
                        'cpuCount': 123,
                        'disks': [
                            {
                                'name': 'string',
                                'arn': 'string',
                                'supportCode': 'string',
                                'createdAt': datetime(2015, 1, 1),
                                'location': {
                                    'availabilityZone': 'string',
                                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                                },
                                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                                'sizeInGb': 123,
                                'isSystemDisk': True|False,
                                'iops': 123,
                                'path': 'string',
                                'state': 'pending'|'error'|'available'|'in-use'|'unknown',
                                'attachedTo': 'string',
                                'isAttached': True|False,
                                'attachmentState': 'string',
                                'gbInUse': 123
                            },
                        ],
                        'ramSizeInGb': ...
                    },
                    'networking': {
                        'monthlyTransfer': {
                            'gbPerMonthAllocated': 123
                        },
                        'ports': [
                            {
                                'fromPort': 123,
                                'toPort': 123,
                                'protocol': 'tcp'|'all'|'udp',
                                'accessFrom': 'string',
                                'accessType': 'Public'|'Private',
                                'commonName': 'string',
                                'accessDirection': 'inbound'|'outbound'
                            },
                        ]
                    },
                    'state': {
                        'code': 123,
                        'name': 'string'
                    },
                    'username': 'string',
                    'sshKeyName': 'string'
                },
            ],
            'nextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **instances** *(list) --* 

          An array of key-value pairs containing information about your instances.

          
          

          - *(dict) --* 

            Describes an instance (a virtual private server).

            
            

            - **name** *(string) --* 

              The name the user gave the instance (e.g., ``Amazon_Linux-1GB-Ohio-1`` ).

              
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the instance (e.g., ``arn:aws:lightsail:us-east-2:123456789101:Instance/244ad76f-8aad-4741-809f-12345EXAMPLE`` ).

              
            

            - **supportCode** *(string) --* 

              The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the instance was created (e.g., ``1479734909.17`` ).

              
            

            - **location** *(dict) --* 

              The region name and availability zone where the instance is located.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **resourceType** *(string) --* 

              The type of resource (usually ``Instance`` ).

              
            

            - **blueprintId** *(string) --* 

              The blueprint ID (e.g., ``os_amlinux_2016_03`` ).

              
            

            - **blueprintName** *(string) --* 

              The friendly name of the blueprint (e.g., ``Amazon Linux`` ).

              
            

            - **bundleId** *(string) --* 

              The bundle for the instance (e.g., ``micro_1_0`` ).

              
            

            - **isStaticIp** *(boolean) --* 

              A Boolean value indicating whether this instance has a static IP assigned to it.

              
            

            - **privateIpAddress** *(string) --* 

              The private IP address of the instance.

              
            

            - **publicIpAddress** *(string) --* 

              The public IP address of the instance.

              
            

            - **ipv6Address** *(string) --* 

              The IPv6 address of the instance.

              
            

            - **hardware** *(dict) --* 

              The size of the vCPU and the amount of RAM for the instance.

              
              

              - **cpuCount** *(integer) --* 

                The number of vCPUs the instance has.

                
              

              - **disks** *(list) --* 

                The disks attached to the instance.

                
                

                - *(dict) --* 

                  Describes a system disk or an block storage disk.

                  
                  

                  - **name** *(string) --* 

                    The unique name of the disk.

                    
                  

                  - **arn** *(string) --* 

                    The Amazon Resource Name (ARN) of the disk.

                    
                  

                  - **supportCode** *(string) --* 

                    The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

                    
                  

                  - **createdAt** *(datetime) --* 

                    The date when the disk was created.

                    
                  

                  - **location** *(dict) --* 

                    The AWS Region and Availability Zone where the disk is located.

                    
                    

                    - **availabilityZone** *(string) --* 

                      The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                      
                    

                    - **regionName** *(string) --* 

                      The AWS Region name.

                      
                
                  

                  - **resourceType** *(string) --* 

                    The Lightsail resource type (e.g., ``Disk`` ).

                    
                  

                  - **sizeInGb** *(integer) --* 

                    The size of the disk in GB.

                    
                  

                  - **isSystemDisk** *(boolean) --* 

                    A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).

                    
                  

                  - **iops** *(integer) --* 

                    The input/output operations per second (IOPS) of the disk.

                    
                  

                  - **path** *(string) --* 

                    The disk path.

                    
                  

                  - **state** *(string) --* 

                    Describes the status of the disk.

                    
                  

                  - **attachedTo** *(string) --* 

                    The resources to which the disk is attached.

                    
                  

                  - **isAttached** *(boolean) --* 

                    A Boolean value indicating whether the disk is attached.

                    
                  

                  - **attachmentState** *(string) --* 

                    (Deprecated) The attachment state of the disk.

                     

                    .. note::

                       

                      In releases prior to November 14, 2017, this parameter returned ``attached`` for system disks in the API response. It is now deprecated, but still included in the response. Use ``isAttached`` instead.

                       

                    
                  

                  - **gbInUse** *(integer) --* 

                    (Deprecated) The number of GB in use by the disk.

                     

                    .. note::

                       

                      In releases prior to November 14, 2017, this parameter was not included in the API response. It is now deprecated.

                       

                    
              
            
              

              - **ramSizeInGb** *(float) --* 

                The amount of RAM in GB on the instance (e.g., ``1.0`` ).

                
          
            

            - **networking** *(dict) --* 

              Information about the public ports and monthly data transfer rates for the instance.

              
              

              - **monthlyTransfer** *(dict) --* 

                The amount of data in GB allocated for monthly data transfers.

                
                

                - **gbPerMonthAllocated** *(integer) --* 

                  The amount allocated per month (in GB).

                  
            
              

              - **ports** *(list) --* 

                An array of key-value pairs containing information about the ports on the instance.

                
                

                - *(dict) --* 

                  Describes information about the instance ports.

                  
                  

                  - **fromPort** *(integer) --* 

                    The first port in the range.

                    
                  

                  - **toPort** *(integer) --* 

                    The last port in the range.

                    
                  

                  - **protocol** *(string) --* 

                    The protocol being used. Can be one of the following.

                     

                     
                    * ``tcp`` - Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesn't require reliable data stream service, use UDP instead. 
                     
                    * ``all`` - All transport layer protocol types. For more general information, see `Transport layer <https://en.wikipedia.org/wiki/Transport_layer>`__ on Wikipedia. 
                     
                    * ``udp`` - With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that don't require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead. 
                     

                    
                  

                  - **accessFrom** *(string) --* 

                    The location from which access is allowed (e.g., ``Anywhere (0.0.0.0/0)`` ).

                    
                  

                  - **accessType** *(string) --* 

                    The type of access (``Public`` or ``Private`` ).

                    
                  

                  - **commonName** *(string) --* 

                    The common name.

                    
                  

                  - **accessDirection** *(string) --* 

                    The access direction (``inbound`` or ``outbound`` ).

                    
              
            
          
            

            - **state** *(dict) --* 

              The status code and the state (e.g., ``running`` ) for the instance.

              
              

              - **code** *(integer) --* 

                The status code for the instance.

                
              

              - **name** *(string) --* 

                The state of the instance (e.g., ``running`` or ``pending`` ).

                
          
            

            - **username** *(string) --* 

              The user name for connecting to the instance (e.g., ``ec2-user`` ).

              
            

            - **sshKeyName** *(string) --* 

              The name of the SSH key being used to connect to the instance (e.g., ``LightsailDefaultKeyPair`` ).

              
        
      
        

        - **nextPageToken** *(string) --* 

          A token used for advancing to the next page of results from your get instances request.

          
    

  .. py:method:: get_key_pair(**kwargs)

    

    Returns information about a specific key pair.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetKeyPair>`_    


    **Request Syntax** 
    ::

      response = client.get_key_pair(
          keyPairName='string'
      )
    :type keyPairName: string
    :param keyPairName: **[REQUIRED]** 

      The name of the key pair for which you are requesting information.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'keyPair': {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                'fingerprint': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **keyPair** *(dict) --* 

          An array of key-value pairs containing information about the key pair.

          
          

          - **name** *(string) --* 

            The friendly name of the SSH key pair.

            
          

          - **arn** *(string) --* 

            The Amazon Resource Name (ARN) of the key pair (e.g., ``arn:aws:lightsail:us-east-2:123456789101:KeyPair/05859e3d-331d-48ba-9034-12345EXAMPLE`` ).

            
          

          - **supportCode** *(string) --* 

            The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

            
          

          - **createdAt** *(datetime) --* 

            The timestamp when the key pair was created (e.g., ``1479816991.349`` ).

            
          

          - **location** *(dict) --* 

            The region name and Availability Zone where the key pair was created.

            
            

            - **availabilityZone** *(string) --* 

              The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

              
            

            - **regionName** *(string) --* 

              The AWS Region name.

              
        
          

          - **resourceType** *(string) --* 

            The resource type (usually ``KeyPair`` ).

            
          

          - **fingerprint** *(string) --* 

            The RSA fingerprint of the key pair.

            
      
    

  .. py:method:: get_key_pairs(**kwargs)

    

    Returns information about all key pairs in the user's account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetKeyPairs>`_    


    **Request Syntax** 
    ::

      response = client.get_key_pairs(
          pageToken='string'
      )
    :type pageToken: string
    :param pageToken: 

      A token used for advancing to the next page of results from your get key pairs request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'keyPairs': [
                {
                    'name': 'string',
                    'arn': 'string',
                    'supportCode': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'fingerprint': 'string'
                },
            ],
            'nextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **keyPairs** *(list) --* 

          An array of key-value pairs containing information about the key pairs.

          
          

          - *(dict) --* 

            Describes the SSH key pair.

            
            

            - **name** *(string) --* 

              The friendly name of the SSH key pair.

              
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the key pair (e.g., ``arn:aws:lightsail:us-east-2:123456789101:KeyPair/05859e3d-331d-48ba-9034-12345EXAMPLE`` ).

              
            

            - **supportCode** *(string) --* 

              The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the key pair was created (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region name and Availability Zone where the key pair was created.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **resourceType** *(string) --* 

              The resource type (usually ``KeyPair`` ).

              
            

            - **fingerprint** *(string) --* 

              The RSA fingerprint of the key pair.

              
        
      
        

        - **nextPageToken** *(string) --* 

          A token used for advancing to the next page of results from your get key pairs request.

          
    

  .. py:method:: get_load_balancer(**kwargs)

    

    Returns information about the specified Lightsail load balancer.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetLoadBalancer>`_    


    **Request Syntax** 
    ::

      response = client.get_load_balancer(
          loadBalancerName='string'
      )
    :type loadBalancerName: string
    :param loadBalancerName: **[REQUIRED]** 

      The name of the load balancer.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'loadBalancer': {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                'dnsName': 'string',
                'state': 'active'|'provisioning'|'active_impaired'|'failed'|'unknown',
                'protocol': 'HTTP_HTTPS'|'HTTP',
                'publicPorts': [
                    123,
                ],
                'healthCheckPath': 'string',
                'instancePort': 123,
                'instanceHealthSummary': [
                    {
                        'instanceName': 'string',
                        'instanceHealth': 'initial'|'healthy'|'unhealthy'|'unused'|'draining'|'unavailable',
                        'instanceHealthReason': 'Lb.RegistrationInProgress'|'Lb.InitialHealthChecking'|'Lb.InternalError'|'Instance.ResponseCodeMismatch'|'Instance.Timeout'|'Instance.FailedHealthChecks'|'Instance.NotRegistered'|'Instance.NotInUse'|'Instance.DeregistrationInProgress'|'Instance.InvalidState'|'Instance.IpUnusable'
                    },
                ],
                'tlsCertificateSummaries': [
                    {
                        'name': 'string',
                        'isAttached': True|False
                    },
                ],
                'configurationOptions': {
                    'string': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **loadBalancer** *(dict) --* 

          An object containing information about your load balancer.

          
          

          - **name** *(string) --* 

            The name of the load balancer (e.g., ``my-load-balancer`` ).

            
          

          - **arn** *(string) --* 

            The Amazon Resource Name (ARN) of the load balancer.

            
          

          - **supportCode** *(string) --* 

            The support code. Include this code in your email to support when you have questions about your Lightsail load balancer. This code enables our support team to look up your Lightsail information more easily.

            
          

          - **createdAt** *(datetime) --* 

            The date when your load balancer was created.

            
          

          - **location** *(dict) --* 

            The AWS Region and Availability Zone where your load balancer was created (e.g., ``us-east-2a`` ).

            
            

            - **availabilityZone** *(string) --* 

              The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

              
            

            - **regionName** *(string) --* 

              The AWS Region name.

              
        
          

          - **resourceType** *(string) --* 

            The resource type (e.g., ``LoadBalancer`` .

            
          

          - **dnsName** *(string) --* 

            The DNS name of your Lightsail load balancer.

            
          

          - **state** *(string) --* 

            The status of your load balancer. Valid values are below.

            
          

          - **protocol** *(string) --* 

            The protocol you have enabled for your load balancer. Valid values are below.

            
          

          - **publicPorts** *(list) --* 

            An array of public port settings for your load balancer.

            
            

            - *(integer) --* 
        
          

          - **healthCheckPath** *(string) --* 

            The path you specified to perform your health checks. If no path is specified, the load balancer tries to make a request to the default (root) page.

            
          

          - **instancePort** *(integer) --* 

            The instance port where the load balancer is listening.

            
          

          - **instanceHealthSummary** *(list) --* 

            An array of InstanceHealthSummary objects describing the health of the load balancer.

            
            

            - *(dict) --* 

              Describes information about the health of the instance.

              
              

              - **instanceName** *(string) --* 

                The name of the Lightsail instance for which you are requesting health check data.

                
              

              - **instanceHealth** *(string) --* 

                Describes the overall instance health. Valid values are below.

                
              

              - **instanceHealthReason** *(string) --* 

                More information about the instance health. Valid values are below.

                
          
        
          

          - **tlsCertificateSummaries** *(list) --* 

            An array of LoadBalancerTlsCertificateSummary objects that provide additional information about the TLS/SSL certificates.

            
            

            - *(dict) --* 

              Provides a summary of TLS/SSL certificate metadata.

              
              

              - **name** *(string) --* 

                The name of the TLS/SSL certificate.

                
              

              - **isAttached** *(boolean) --* 

                When ``true`` , the TLS/SSL certificate is attached to the Lightsail load balancer.

                
          
        
          

          - **configurationOptions** *(dict) --* 

            A string to string map of the configuration options for your load balancer. Valid values are listed below.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
      
    

  .. py:method:: get_load_balancer_metric_data(**kwargs)

    

    Returns information about health metrics for your Lightsail load balancer.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetLoadBalancerMetricData>`_    


    **Request Syntax** 
    ::

      response = client.get_load_balancer_metric_data(
          loadBalancerName='string',
          metricName='ClientTLSNegotiationErrorCount'|'HealthyHostCount'|'UnhealthyHostCount'|'HTTPCode_LB_4XX_Count'|'HTTPCode_LB_5XX_Count'|'HTTPCode_Instance_2XX_Count'|'HTTPCode_Instance_3XX_Count'|'HTTPCode_Instance_4XX_Count'|'HTTPCode_Instance_5XX_Count'|'InstanceResponseTime'|'RejectedConnectionCount'|'RequestCount',
          period=123,
          startTime=datetime(2015, 1, 1),
          endTime=datetime(2015, 1, 1),
          unit='Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
          statistics=[
              'Minimum'|'Maximum'|'Sum'|'Average'|'SampleCount',
          ]
      )
    :type loadBalancerName: string
    :param loadBalancerName: **[REQUIRED]** 

      The name of the load balancer.

      

    
    :type metricName: string
    :param metricName: **[REQUIRED]** 

      The metric about which you want to return information. Valid values are listed below, along with the most useful ``statistics`` to include in your request.

       

       
      * **``ClientTLSNegotiationErrorCount`` ** - The number of TLS connections initiated by the client that did not establish a session with the load balancer. Possible causes include a mismatch of ciphers or protocols.  ``Statistics`` : The most useful statistic is ``Sum`` . 
       
      * **``HealthyHostCount`` ** - The number of target instances that are considered healthy.  ``Statistics`` : The most useful statistic are ``Average`` , ``Minimum`` , and ``Maximum`` . 
       
      * **``UnhealthyHostCount`` ** - The number of target instances that are considered unhealthy.  ``Statistics`` : The most useful statistic are ``Average`` , ``Minimum`` , and ``Maximum`` . 
       
      * **``HTTPCode_LB_4XX_Count`` ** - The number of HTTP 4XX client error codes that originate from the load balancer. Client errors are generated when requests are malformed or incomplete. These requests have not been received by the target instance. This count does not include any response codes generated by the target instances.  ``Statistics`` : The most useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum`` , and ``Average`` all return ``1`` . 
       
      * **``HTTPCode_LB_5XX_Count`` ** - The number of HTTP 5XX server error codes that originate from the load balancer. This count does not include any response codes generated by the target instances.  ``Statistics`` : The most useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum`` , and ``Average`` all return ``1`` . Note that ``Minimum`` , ``Maximum`` , and ``Average`` all return ``1`` . 
       
      * **``HTTPCode_Instance_2XX_Count`` ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.  ``Statistics`` : The most useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum`` , and ``Average`` all return ``1`` . 
       
      * **``HTTPCode_Instance_3XX_Count`` ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.   ``Statistics`` : The most useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum`` , and ``Average`` all return ``1`` . 
       
      * **``HTTPCode_Instance_4XX_Count`` ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.  ``Statistics`` : The most useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum`` , and ``Average`` all return ``1`` . 
       
      * **``HTTPCode_Instance_5XX_Count`` ** - The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.  ``Statistics`` : The most useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum`` , and ``Average`` all return ``1`` . 
       
      * **``InstanceResponseTime`` ** - The time elapsed, in seconds, after the request leaves the load balancer until a response from the target instance is received.  ``Statistics`` : The most useful statistic is ``Average`` . 
       
      * **``RejectedConnectionCount`` ** - The number of connections that were rejected because the load balancer had reached its maximum number of connections.  ``Statistics`` : The most useful statistic is ``Sum`` . 
       
      * **``RequestCount`` ** - The number of requests processed over IPv4. This count includes only the requests with a response generated by a target instance of the load balancer.  ``Statistics`` : The most useful statistic is ``Sum`` . Note that ``Minimum`` , ``Maximum`` , and ``Average`` all return ``1`` . 
       

      

    
    :type period: integer
    :param period: **[REQUIRED]** 

      The time period duration for your health data request.

      

    
    :type startTime: datetime
    :param startTime: **[REQUIRED]** 

      The start time of the period.

      

    
    :type endTime: datetime
    :param endTime: **[REQUIRED]** 

      The end time of the period.

      

    
    :type unit: string
    :param unit: **[REQUIRED]** 

      The unit for the time period request. Valid values are listed below.

      

    
    :type statistics: list
    :param statistics: **[REQUIRED]** 

      An array of statistics that you want to request metrics for. Valid values are listed below.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'metricName': 'ClientTLSNegotiationErrorCount'|'HealthyHostCount'|'UnhealthyHostCount'|'HTTPCode_LB_4XX_Count'|'HTTPCode_LB_5XX_Count'|'HTTPCode_Instance_2XX_Count'|'HTTPCode_Instance_3XX_Count'|'HTTPCode_Instance_4XX_Count'|'HTTPCode_Instance_5XX_Count'|'InstanceResponseTime'|'RejectedConnectionCount'|'RequestCount',
            'metricData': [
                {
                    'average': 123.0,
                    'maximum': 123.0,
                    'minimum': 123.0,
                    'sampleCount': 123.0,
                    'sum': 123.0,
                    'timestamp': datetime(2015, 1, 1),
                    'unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **metricName** *(string) --* 

          The metric about which you are receiving information. Valid values are listed below.

          
        

        - **metricData** *(list) --* 

          An array of metric datapoint objects.

          
          

          - *(dict) --* 

            Describes the metric data point.

            
            

            - **average** *(float) --* 

              The average.

              
            

            - **maximum** *(float) --* 

              The maximum.

              
            

            - **minimum** *(float) --* 

              The minimum.

              
            

            - **sampleCount** *(float) --* 

              The sample count.

              
            

            - **sum** *(float) --* 

              The sum.

              
            

            - **timestamp** *(datetime) --* 

              The timestamp (e.g., ``1479816991.349`` ).

              
            

            - **unit** *(string) --* 

              The unit. 

              
        
      
    

  .. py:method:: get_load_balancer_tls_certificates(**kwargs)

    

    Returns information about the TLS certificates that are associated with the specified Lightsail load balancer.

     

    TLS is just an updated, more secure version of Secure Socket Layer (SSL).

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetLoadBalancerTlsCertificates>`_    


    **Request Syntax** 
    ::

      response = client.get_load_balancer_tls_certificates(
          loadBalancerName='string'
      )
    :type loadBalancerName: string
    :param loadBalancerName: **[REQUIRED]** 

      The name of the load balancer where you stored your TLS/SSL certificate.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'tlsCertificates': [
                {
                    'name': 'string',
                    'arn': 'string',
                    'supportCode': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'loadBalancerName': 'string',
                    'isAttached': True|False,
                    'status': 'PENDING_VALIDATION'|'ISSUED'|'INACTIVE'|'EXPIRED'|'VALIDATION_TIMED_OUT'|'REVOKED'|'FAILED'|'UNKNOWN',
                    'domainName': 'string',
                    'domainValidationRecords': [
                        {
                            'name': 'string',
                            'type': 'string',
                            'value': 'string',
                            'validationStatus': 'PENDING_VALIDATION'|'FAILED'|'SUCCESS',
                            'domainName': 'string'
                        },
                    ],
                    'failureReason': 'NO_AVAILABLE_CONTACTS'|'ADDITIONAL_VERIFICATION_REQUIRED'|'DOMAIN_NOT_ALLOWED'|'INVALID_PUBLIC_DOMAIN'|'OTHER',
                    'issuedAt': datetime(2015, 1, 1),
                    'issuer': 'string',
                    'keyAlgorithm': 'string',
                    'notAfter': datetime(2015, 1, 1),
                    'notBefore': datetime(2015, 1, 1),
                    'renewalSummary': {
                        'renewalStatus': 'PENDING_AUTO_RENEWAL'|'PENDING_VALIDATION'|'SUCCESS'|'FAILED',
                        'domainValidationOptions': [
                            {
                                'domainName': 'string',
                                'validationStatus': 'PENDING_VALIDATION'|'FAILED'|'SUCCESS'
                            },
                        ]
                    },
                    'revocationReason': 'UNSPECIFIED'|'KEY_COMPROMISE'|'CA_COMPROMISE'|'AFFILIATION_CHANGED'|'SUPERCEDED'|'CESSATION_OF_OPERATION'|'CERTIFICATE_HOLD'|'REMOVE_FROM_CRL'|'PRIVILEGE_WITHDRAWN'|'A_A_COMPROMISE',
                    'revokedAt': datetime(2015, 1, 1),
                    'serial': 'string',
                    'signatureAlgorithm': 'string',
                    'subject': 'string',
                    'subjectAlternativeNames': [
                        'string',
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **tlsCertificates** *(list) --* 

          An array of LoadBalancerTlsCertificate objects describing your TLS/SSL certificates.

          
          

          - *(dict) --* 

            Describes a load balancer TLS/SSL certificate.

             

            TLS is just an updated, more secure version of Secure Socket Layer (SSL).

            
            

            - **name** *(string) --* 

              The name of the TLS/SSL certificate (e.g., ``my-certificate`` ).

              
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the TLS/SSL certificate.

              
            

            - **supportCode** *(string) --* 

              The support code. Include this code in your email to support when you have questions about your Lightsail load balancer or TLS/SSL certificate. This code enables our support team to look up your Lightsail information more easily.

              
            

            - **createdAt** *(datetime) --* 

              The time when you created your TLS/SSL certificate.

              
            

            - **location** *(dict) --* 

              The AWS Region and Availability Zone where you created your certificate.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **resourceType** *(string) --* 

              The resource type (e.g., ``LoadBalancerTlsCertificate`` .

              
            

            - **loadBalancerName** *(string) --* 

              The load balancer name where your TLS/SSL certificate is attached.

              
            

            - **isAttached** *(boolean) --* 

              When ``true`` , the TLS/SSL certificate is attached to the Lightsail load balancer.

              
            

            - **status** *(string) --* 

              The status of the TLS/SSL certificate. Valid values are below.

              
            

            - **domainName** *(string) --* 

              The domain name for your TLS/SSL certificate.

              
            

            - **domainValidationRecords** *(list) --* 

              An array of LoadBalancerTlsCertificateDomainValidationRecord objects describing the records.

              
              

              - *(dict) --* 

                Describes the validation record of each domain name in the TLS/SSL certificate.

                
                

                - **name** *(string) --* 

                  A fully qualified domain name in the certificate. For example, ``example.com`` .

                  
                

                - **type** *(string) --* 

                  The type of validation record. For example, ``CNAME`` for domain validation.

                  
                

                - **value** *(string) --* 

                  The value for that type.

                  
                

                - **validationStatus** *(string) --* 

                  The validation status. Valid values are listed below.

                  
                

                - **domainName** *(string) --* 

                  The domain name against which your TLS/SSL certificate was validated.

                  
            
          
            

            - **failureReason** *(string) --* 

              The reason for the TLS/SSL certificate validation failure.

              
            

            - **issuedAt** *(datetime) --* 

              The time when the TLS/SSL certificate was issued.

              
            

            - **issuer** *(string) --* 

              The issuer of the certificate.

              
            

            - **keyAlgorithm** *(string) --* 

              The algorithm that was used to generate the key pair (the public and private key).

              
            

            - **notAfter** *(datetime) --* 

              The timestamp when the TLS/SSL certificate expires.

              
            

            - **notBefore** *(datetime) --* 

              The timestamp when the TLS/SSL certificate is first valid.

              
            

            - **renewalSummary** *(dict) --* 

              An object containing information about the status of Lightsail's managed renewal for the certificate.

              
              

              - **renewalStatus** *(string) --* 

                The status of Lightsail's managed renewal of the certificate. Valid values are listed below.

                
              

              - **domainValidationOptions** *(list) --* 

                Contains information about the validation of each domain name in the certificate, as it pertains to Lightsail's managed renewal. This is different from the initial validation that occurs as a result of the RequestCertificate request.

                
                

                - *(dict) --* 

                  Contains information about the domain names on a TLS/SSL certificate that you will use to validate domain ownership.

                  
                  

                  - **domainName** *(string) --* 

                    A fully qualified domain name in the certificate request.

                    
                  

                  - **validationStatus** *(string) --* 

                    The status of the domain validation. Valid values are listed below.

                    
              
            
          
            

            - **revocationReason** *(string) --* 

              The reason the certificate was revoked. Valid values are below.

              
            

            - **revokedAt** *(datetime) --* 

              The timestamp when the TLS/SSL certificate was revoked.

              
            

            - **serial** *(string) --* 

              The serial number of the certificate.

              
            

            - **signatureAlgorithm** *(string) --* 

              The algorithm that was used to sign the certificate.

              
            

            - **subject** *(string) --* 

              The name of the entity that is associated with the public key contained in the certificate.

              
            

            - **subjectAlternativeNames** *(list) --* 

              One or more domain names (subject alternative names) included in the certificate. This list contains the domain names that are bound to the public key that is contained in the certificate. The subject alternative names include the canonical domain name (CN) of the certificate and additional domain names that can be used to connect to the website.

              
              

              - *(string) --* 
          
        
      
    

  .. py:method:: get_load_balancers(**kwargs)

    

    Returns information about all load balancers in an account.

     

    If you are describing a long list of load balancers, you can paginate the output to make the list more manageable. You can use the pageToken and nextPageToken values to retrieve the next items in the list.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetLoadBalancers>`_    


    **Request Syntax** 
    ::

      response = client.get_load_balancers(
          pageToken='string'
      )
    :type pageToken: string
    :param pageToken: 

      A token used for paginating the results from your GetLoadBalancers request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'loadBalancers': [
                {
                    'name': 'string',
                    'arn': 'string',
                    'supportCode': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'dnsName': 'string',
                    'state': 'active'|'provisioning'|'active_impaired'|'failed'|'unknown',
                    'protocol': 'HTTP_HTTPS'|'HTTP',
                    'publicPorts': [
                        123,
                    ],
                    'healthCheckPath': 'string',
                    'instancePort': 123,
                    'instanceHealthSummary': [
                        {
                            'instanceName': 'string',
                            'instanceHealth': 'initial'|'healthy'|'unhealthy'|'unused'|'draining'|'unavailable',
                            'instanceHealthReason': 'Lb.RegistrationInProgress'|'Lb.InitialHealthChecking'|'Lb.InternalError'|'Instance.ResponseCodeMismatch'|'Instance.Timeout'|'Instance.FailedHealthChecks'|'Instance.NotRegistered'|'Instance.NotInUse'|'Instance.DeregistrationInProgress'|'Instance.InvalidState'|'Instance.IpUnusable'
                        },
                    ],
                    'tlsCertificateSummaries': [
                        {
                            'name': 'string',
                            'isAttached': True|False
                        },
                    ],
                    'configurationOptions': {
                        'string': 'string'
                    }
                },
            ],
            'nextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **loadBalancers** *(list) --* 

          An array of LoadBalancer objects describing your load balancers.

          
          

          - *(dict) --* 

            Describes the Lightsail load balancer.

            
            

            - **name** *(string) --* 

              The name of the load balancer (e.g., ``my-load-balancer`` ).

              
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the load balancer.

              
            

            - **supportCode** *(string) --* 

              The support code. Include this code in your email to support when you have questions about your Lightsail load balancer. This code enables our support team to look up your Lightsail information more easily.

              
            

            - **createdAt** *(datetime) --* 

              The date when your load balancer was created.

              
            

            - **location** *(dict) --* 

              The AWS Region and Availability Zone where your load balancer was created (e.g., ``us-east-2a`` ).

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **resourceType** *(string) --* 

              The resource type (e.g., ``LoadBalancer`` .

              
            

            - **dnsName** *(string) --* 

              The DNS name of your Lightsail load balancer.

              
            

            - **state** *(string) --* 

              The status of your load balancer. Valid values are below.

              
            

            - **protocol** *(string) --* 

              The protocol you have enabled for your load balancer. Valid values are below.

              
            

            - **publicPorts** *(list) --* 

              An array of public port settings for your load balancer.

              
              

              - *(integer) --* 
          
            

            - **healthCheckPath** *(string) --* 

              The path you specified to perform your health checks. If no path is specified, the load balancer tries to make a request to the default (root) page.

              
            

            - **instancePort** *(integer) --* 

              The instance port where the load balancer is listening.

              
            

            - **instanceHealthSummary** *(list) --* 

              An array of InstanceHealthSummary objects describing the health of the load balancer.

              
              

              - *(dict) --* 

                Describes information about the health of the instance.

                
                

                - **instanceName** *(string) --* 

                  The name of the Lightsail instance for which you are requesting health check data.

                  
                

                - **instanceHealth** *(string) --* 

                  Describes the overall instance health. Valid values are below.

                  
                

                - **instanceHealthReason** *(string) --* 

                  More information about the instance health. Valid values are below.

                  
            
          
            

            - **tlsCertificateSummaries** *(list) --* 

              An array of LoadBalancerTlsCertificateSummary objects that provide additional information about the TLS/SSL certificates.

              
              

              - *(dict) --* 

                Provides a summary of TLS/SSL certificate metadata.

                
                

                - **name** *(string) --* 

                  The name of the TLS/SSL certificate.

                  
                

                - **isAttached** *(boolean) --* 

                  When ``true`` , the TLS/SSL certificate is attached to the Lightsail load balancer.

                  
            
          
            

            - **configurationOptions** *(dict) --* 

              A string to string map of the configuration options for your load balancer. Valid values are listed below.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
        
      
        

        - **nextPageToken** *(string) --* 

          A token used for advancing to the next page of results from your GetLoadBalancers request.

          
    

  .. py:method:: get_operation(**kwargs)

    

    Returns information about a specific operation. Operations include events such as when you create an instance, allocate a static IP, attach a static IP, and so on.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetOperation>`_    


    **Request Syntax** 
    ::

      response = client.get_operation(
          operationId='string'
      )
    :type operationId: string
    :param operationId: **[REQUIRED]** 

      A GUID used to identify the operation.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operation': {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operation** *(dict) --* 

          An array of key-value pairs containing information about the results of your get operation request.

          
          

          - **id** *(string) --* 

            The ID of the operation.

            
          

          - **resourceName** *(string) --* 

            The resource name.

            
          

          - **resourceType** *(string) --* 

            The resource type. 

            
          

          - **createdAt** *(datetime) --* 

            The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

            
          

          - **location** *(dict) --* 

            The region and Availability Zone.

            
            

            - **availabilityZone** *(string) --* 

              The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

              
            

            - **regionName** *(string) --* 

              The AWS Region name.

              
        
          

          - **isTerminal** *(boolean) --* 

            A Boolean value indicating whether the operation is terminal.

            
          

          - **operationDetails** *(string) --* 

            Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

            
          

          - **operationType** *(string) --* 

            The type of operation. 

            
          

          - **status** *(string) --* 

            The status of the operation. 

            
          

          - **statusChangedAt** *(datetime) --* 

            The timestamp when the status was changed (e.g., ``1479816991.349`` ).

            
          

          - **errorCode** *(string) --* 

            The error code.

            
          

          - **errorDetails** *(string) --* 

            The error details.

            
      
    

  .. py:method:: get_operations(**kwargs)

    

    Returns information about all operations.

     

    Results are returned from oldest to newest, up to a maximum of 200. Results can be paged by making each subsequent call to ``GetOperations`` use the maximum (last) ``statusChangedAt`` value from the previous request.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetOperations>`_    


    **Request Syntax** 
    ::

      response = client.get_operations(
          pageToken='string'
      )
    :type pageToken: string
    :param pageToken: 

      A token used for advancing to the next page of results from your get operations request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ],
            'nextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An array of key-value pairs containing information about the results of your get operations request.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
        

        - **nextPageToken** *(string) --* 

          A token used for advancing to the next page of results from your get operations request.

          
    

  .. py:method:: get_operations_for_resource(**kwargs)

    

    Gets operations for a specific resource (e.g., an instance or a static IP).

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetOperationsForResource>`_    


    **Request Syntax** 
    ::

      response = client.get_operations_for_resource(
          resourceName='string',
          pageToken='string'
      )
    :type resourceName: string
    :param resourceName: **[REQUIRED]** 

      The name of the resource for which you are requesting information.

      

    
    :type pageToken: string
    :param pageToken: 

      A token used for advancing to the next page of results from your get operations for resource request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ],
            'nextPageCount': 'string',
            'nextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An array of key-value pairs containing information about the results of your get operations for resource request.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
        

        - **nextPageCount** *(string) --* 

          (Deprecated) Returns the number of pages of results that remain.

           

          .. note::

             

            In releases prior to June 12, 2017, this parameter returned ``null`` by the API. It is now deprecated, and the API returns the ``nextPageToken`` parameter instead.

             

          
        

        - **nextPageToken** *(string) --* 

          An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

          
    

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


  .. py:method:: get_regions(**kwargs)

    

    Returns a list of all valid regions for Amazon Lightsail. Use the ``include availability zones`` parameter to also return the availability zones in a region.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetRegions>`_    


    **Request Syntax** 
    ::

      response = client.get_regions(
          includeAvailabilityZones=True|False
      )
    :type includeAvailabilityZones: boolean
    :param includeAvailabilityZones: 

      A Boolean value indicating whether to also include Availability Zones in your get regions request. Availability Zones are indicated with a letter: e.g., ``us-east-2a`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'regions': [
                {
                    'continentCode': 'string',
                    'description': 'string',
                    'displayName': 'string',
                    'name': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2',
                    'availabilityZones': [
                        {
                            'zoneName': 'string',
                            'state': 'string'
                        },
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **regions** *(list) --* 

          An array of key-value pairs containing information about your get regions request.

          
          

          - *(dict) --* 

            Describes the AWS Region.

            
            

            - **continentCode** *(string) --* 

              The continent code (e.g., ``NA`` , meaning North America).

              
            

            - **description** *(string) --* 

              The description of the AWS Region (e.g., ``This region is recommended to serve users in the eastern United States and eastern Canada`` ).

              
            

            - **displayName** *(string) --* 

              The display name (e.g., ``Ohio`` ).

              
            

            - **name** *(string) --* 

              The region name (e.g., ``us-east-2`` ).

              
            

            - **availabilityZones** *(list) --* 

              The Availability Zones. Follows the format ``us-east-2a`` (case-sensitive).

              
              

              - *(dict) --* 

                Describes an Availability Zone.

                
                

                - **zoneName** *(string) --* 

                  The name of the Availability Zone. The format is ``us-east-2a`` (case-sensitive).

                  
                

                - **state** *(string) --* 

                  The state of the Availability Zone.

                  
            
          
        
      
    

  .. py:method:: get_static_ip(**kwargs)

    

    Returns information about a specific static IP.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetStaticIp>`_    


    **Request Syntax** 
    ::

      response = client.get_static_ip(
          staticIpName='string'
      )
    :type staticIpName: string
    :param staticIpName: **[REQUIRED]** 

      The name of the static IP in Lightsail.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'staticIp': {
                'name': 'string',
                'arn': 'string',
                'supportCode': 'string',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                'ipAddress': 'string',
                'attachedTo': 'string',
                'isAttached': True|False
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **staticIp** *(dict) --* 

          An array of key-value pairs containing information about the requested static IP.

          
          

          - **name** *(string) --* 

            The name of the static IP (e.g., ``StaticIP-Ohio-EXAMPLE`` ).

            
          

          - **arn** *(string) --* 

            The Amazon Resource Name (ARN) of the static IP (e.g., ``arn:aws:lightsail:us-east-2:123456789101:StaticIp/9cbb4a9e-f8e3-4dfe-b57e-12345EXAMPLE`` ).

            
          

          - **supportCode** *(string) --* 

            The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

            
          

          - **createdAt** *(datetime) --* 

            The timestamp when the static IP was created (e.g., ``1479735304.222`` ).

            
          

          - **location** *(dict) --* 

            The region and Availability Zone where the static IP was created.

            
            

            - **availabilityZone** *(string) --* 

              The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

              
            

            - **regionName** *(string) --* 

              The AWS Region name.

              
        
          

          - **resourceType** *(string) --* 

            The resource type (usually ``StaticIp`` ).

            
          

          - **ipAddress** *(string) --* 

            The static IP address.

            
          

          - **attachedTo** *(string) --* 

            The instance where the static IP is attached (e.g., ``Amazon_Linux-1GB-Ohio-1`` ).

            
          

          - **isAttached** *(boolean) --* 

            A Boolean value indicating whether the static IP is attached.

            
      
    

  .. py:method:: get_static_ips(**kwargs)

    

    Returns information about all static IPs in the user's account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetStaticIps>`_    


    **Request Syntax** 
    ::

      response = client.get_static_ips(
          pageToken='string'
      )
    :type pageToken: string
    :param pageToken: 

      A token used for advancing to the next page of results from your get static IPs request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'staticIps': [
                {
                    'name': 'string',
                    'arn': 'string',
                    'supportCode': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'ipAddress': 'string',
                    'attachedTo': 'string',
                    'isAttached': True|False
                },
            ],
            'nextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **staticIps** *(list) --* 

          An array of key-value pairs containing information about your get static IPs request.

          
          

          - *(dict) --* 

            Describes the static IP.

            
            

            - **name** *(string) --* 

              The name of the static IP (e.g., ``StaticIP-Ohio-EXAMPLE`` ).

              
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the static IP (e.g., ``arn:aws:lightsail:us-east-2:123456789101:StaticIp/9cbb4a9e-f8e3-4dfe-b57e-12345EXAMPLE`` ).

              
            

            - **supportCode** *(string) --* 

              The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the static IP was created (e.g., ``1479735304.222`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone where the static IP was created.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **resourceType** *(string) --* 

              The resource type (usually ``StaticIp`` ).

              
            

            - **ipAddress** *(string) --* 

              The static IP address.

              
            

            - **attachedTo** *(string) --* 

              The instance where the static IP is attached (e.g., ``Amazon_Linux-1GB-Ohio-1`` ).

              
            

            - **isAttached** *(boolean) --* 

              A Boolean value indicating whether the static IP is attached.

              
        
      
        

        - **nextPageToken** *(string) --* 

          A token used for advancing to the next page of results from your get static IPs request.

          
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: import_key_pair(**kwargs)

    

    Imports a public SSH key from a specific key pair.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/ImportKeyPair>`_    


    **Request Syntax** 
    ::

      response = client.import_key_pair(
          keyPairName='string',
          publicKeyBase64='string'
      )
    :type keyPairName: string
    :param keyPairName: **[REQUIRED]** 

      The name of the key pair for which you want to import the public key.

      

    
    :type publicKeyBase64: string
    :param publicKeyBase64: **[REQUIRED]** 

      A base64-encoded public key of the ``ssh-rsa`` type.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operation': {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operation** *(dict) --* 

          An array of key-value pairs containing information about the request operation.

          
          

          - **id** *(string) --* 

            The ID of the operation.

            
          

          - **resourceName** *(string) --* 

            The resource name.

            
          

          - **resourceType** *(string) --* 

            The resource type. 

            
          

          - **createdAt** *(datetime) --* 

            The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

            
          

          - **location** *(dict) --* 

            The region and Availability Zone.

            
            

            - **availabilityZone** *(string) --* 

              The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

              
            

            - **regionName** *(string) --* 

              The AWS Region name.

              
        
          

          - **isTerminal** *(boolean) --* 

            A Boolean value indicating whether the operation is terminal.

            
          

          - **operationDetails** *(string) --* 

            Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

            
          

          - **operationType** *(string) --* 

            The type of operation. 

            
          

          - **status** *(string) --* 

            The status of the operation. 

            
          

          - **statusChangedAt** *(datetime) --* 

            The timestamp when the status was changed (e.g., ``1479816991.349`` ).

            
          

          - **errorCode** *(string) --* 

            The error code.

            
          

          - **errorDetails** *(string) --* 

            The error details.

            
      
    

  .. py:method:: is_vpc_peered()

    

    Returns a Boolean value indicating whether your Lightsail VPC is peered.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/IsVpcPeered>`_    


    **Request Syntax** 
    ::

      response = client.is_vpc_peered()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'isPeered': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **isPeered** *(boolean) --* 

          Returns ``true`` if the Lightsail VPC is peered; otherwise, ``false`` .

          
    

  .. py:method:: open_instance_public_ports(**kwargs)

    

    Adds public ports to an Amazon Lightsail instance.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/OpenInstancePublicPorts>`_    


    **Request Syntax** 
    ::

      response = client.open_instance_public_ports(
          portInfo={
              'fromPort': 123,
              'toPort': 123,
              'protocol': 'tcp'|'all'|'udp'
          },
          instanceName='string'
      )
    :type portInfo: dict
    :param portInfo: **[REQUIRED]** 

      An array of key-value pairs containing information about the port mappings.

      

    
      - **fromPort** *(integer) --* 

        The first port in the range.

        

      
      - **toPort** *(integer) --* 

        The last port in the range.

        

      
      - **protocol** *(string) --* 

        The protocol. 

        

      
    
    :type instanceName: string
    :param instanceName: **[REQUIRED]** 

      The name of the instance for which you want to open the public ports.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operation': {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operation** *(dict) --* 

          An array of key-value pairs containing information about the request operation.

          
          

          - **id** *(string) --* 

            The ID of the operation.

            
          

          - **resourceName** *(string) --* 

            The resource name.

            
          

          - **resourceType** *(string) --* 

            The resource type. 

            
          

          - **createdAt** *(datetime) --* 

            The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

            
          

          - **location** *(dict) --* 

            The region and Availability Zone.

            
            

            - **availabilityZone** *(string) --* 

              The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

              
            

            - **regionName** *(string) --* 

              The AWS Region name.

              
        
          

          - **isTerminal** *(boolean) --* 

            A Boolean value indicating whether the operation is terminal.

            
          

          - **operationDetails** *(string) --* 

            Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

            
          

          - **operationType** *(string) --* 

            The type of operation. 

            
          

          - **status** *(string) --* 

            The status of the operation. 

            
          

          - **statusChangedAt** *(datetime) --* 

            The timestamp when the status was changed (e.g., ``1479816991.349`` ).

            
          

          - **errorCode** *(string) --* 

            The error code.

            
          

          - **errorDetails** *(string) --* 

            The error details.

            
      
    

  .. py:method:: peer_vpc()

    

    Tries to peer the Lightsail VPC with the user's default VPC.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/PeerVpc>`_    


    **Request Syntax** 
    ::

      response = client.peer_vpc()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operation': {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operation** *(dict) --* 

          An array of key-value pairs containing information about the request operation.

          
          

          - **id** *(string) --* 

            The ID of the operation.

            
          

          - **resourceName** *(string) --* 

            The resource name.

            
          

          - **resourceType** *(string) --* 

            The resource type. 

            
          

          - **createdAt** *(datetime) --* 

            The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

            
          

          - **location** *(dict) --* 

            The region and Availability Zone.

            
            

            - **availabilityZone** *(string) --* 

              The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

              
            

            - **regionName** *(string) --* 

              The AWS Region name.

              
        
          

          - **isTerminal** *(boolean) --* 

            A Boolean value indicating whether the operation is terminal.

            
          

          - **operationDetails** *(string) --* 

            Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

            
          

          - **operationType** *(string) --* 

            The type of operation. 

            
          

          - **status** *(string) --* 

            The status of the operation. 

            
          

          - **statusChangedAt** *(datetime) --* 

            The timestamp when the status was changed (e.g., ``1479816991.349`` ).

            
          

          - **errorCode** *(string) --* 

            The error code.

            
          

          - **errorDetails** *(string) --* 

            The error details.

            
      
    

  .. py:method:: put_instance_public_ports(**kwargs)

    

    Sets the specified open ports for an Amazon Lightsail instance, and closes all ports for every protocol not included in the current request.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/PutInstancePublicPorts>`_    


    **Request Syntax** 
    ::

      response = client.put_instance_public_ports(
          portInfos=[
              {
                  'fromPort': 123,
                  'toPort': 123,
                  'protocol': 'tcp'|'all'|'udp'
              },
          ],
          instanceName='string'
      )
    :type portInfos: list
    :param portInfos: **[REQUIRED]** 

      Specifies information about the public port(s).

      

    
      - *(dict) --* 

        Describes information about the ports on your virtual private server (or *instance* ).

        

      
        - **fromPort** *(integer) --* 

          The first port in the range.

          

        
        - **toPort** *(integer) --* 

          The last port in the range.

          

        
        - **protocol** *(string) --* 

          The protocol. 

          

        
      
  
    :type instanceName: string
    :param instanceName: **[REQUIRED]** 

      The Lightsail instance name of the public port(s) you are setting.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operation': {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operation** *(dict) --* 

          Describes metadata about the operation you just executed.

          
          

          - **id** *(string) --* 

            The ID of the operation.

            
          

          - **resourceName** *(string) --* 

            The resource name.

            
          

          - **resourceType** *(string) --* 

            The resource type. 

            
          

          - **createdAt** *(datetime) --* 

            The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

            
          

          - **location** *(dict) --* 

            The region and Availability Zone.

            
            

            - **availabilityZone** *(string) --* 

              The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

              
            

            - **regionName** *(string) --* 

              The AWS Region name.

              
        
          

          - **isTerminal** *(boolean) --* 

            A Boolean value indicating whether the operation is terminal.

            
          

          - **operationDetails** *(string) --* 

            Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

            
          

          - **operationType** *(string) --* 

            The type of operation. 

            
          

          - **status** *(string) --* 

            The status of the operation. 

            
          

          - **statusChangedAt** *(datetime) --* 

            The timestamp when the status was changed (e.g., ``1479816991.349`` ).

            
          

          - **errorCode** *(string) --* 

            The error code.

            
          

          - **errorDetails** *(string) --* 

            The error details.

            
      
    

  .. py:method:: reboot_instance(**kwargs)

    

    Restarts a specific instance. When your Amazon Lightsail instance is finished rebooting, Lightsail assigns a new public IP address. To use the same IP address after restarting, create a static IP address and attach it to the instance.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/RebootInstance>`_    


    **Request Syntax** 
    ::

      response = client.reboot_instance(
          instanceName='string'
      )
    :type instanceName: string
    :param instanceName: **[REQUIRED]** 

      The name of the instance to reboot.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An array of key-value pairs containing information about the request operation.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

  .. py:method:: release_static_ip(**kwargs)

    

    Deletes a specific static IP from your account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/ReleaseStaticIp>`_    


    **Request Syntax** 
    ::

      response = client.release_static_ip(
          staticIpName='string'
      )
    :type staticIpName: string
    :param staticIpName: **[REQUIRED]** 

      The name of the static IP to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An array of key-value pairs containing information about the request operation.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

  .. py:method:: start_instance(**kwargs)

    

    Starts a specific Amazon Lightsail instance from a stopped state. To restart an instance, use the reboot instance operation.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/StartInstance>`_    


    **Request Syntax** 
    ::

      response = client.start_instance(
          instanceName='string'
      )
    :type instanceName: string
    :param instanceName: **[REQUIRED]** 

      The name of the instance (a virtual private server) to start.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An array of key-value pairs containing information about the request operation.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

  .. py:method:: stop_instance(**kwargs)

    

    Stops a specific Amazon Lightsail instance that is currently running.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/StopInstance>`_    


    **Request Syntax** 
    ::

      response = client.stop_instance(
          instanceName='string',
          force=True|False
      )
    :type instanceName: string
    :param instanceName: **[REQUIRED]** 

      The name of the instance (a virtual private server) to stop.

      

    
    :type force: boolean
    :param force: 

      When set to ``True`` , forces a Lightsail instance that is stuck in a ``stopping`` state to stop.

       

      .. warning::

         

        Only use the ``force`` parameter if your instance is stuck in the ``stopping`` state. In any other state, your instance should stop normally without adding this parameter to your API request.

         

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An array of key-value pairs containing information about the request operation.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

  .. py:method:: unpeer_vpc()

    

    Attempts to unpeer the Lightsail VPC from the user's default VPC.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/UnpeerVpc>`_    


    **Request Syntax** 
    ::

      response = client.unpeer_vpc()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operation': {
                'id': 'string',
                'resourceName': 'string',
                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                'createdAt': datetime(2015, 1, 1),
                'location': {
                    'availabilityZone': 'string',
                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                },
                'isTerminal': True|False,
                'operationDetails': 'string',
                'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                'statusChangedAt': datetime(2015, 1, 1),
                'errorCode': 'string',
                'errorDetails': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operation** *(dict) --* 

          An array of key-value pairs containing information about the request operation.

          
          

          - **id** *(string) --* 

            The ID of the operation.

            
          

          - **resourceName** *(string) --* 

            The resource name.

            
          

          - **resourceType** *(string) --* 

            The resource type. 

            
          

          - **createdAt** *(datetime) --* 

            The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

            
          

          - **location** *(dict) --* 

            The region and Availability Zone.

            
            

            - **availabilityZone** *(string) --* 

              The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

              
            

            - **regionName** *(string) --* 

              The AWS Region name.

              
        
          

          - **isTerminal** *(boolean) --* 

            A Boolean value indicating whether the operation is terminal.

            
          

          - **operationDetails** *(string) --* 

            Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

            
          

          - **operationType** *(string) --* 

            The type of operation. 

            
          

          - **status** *(string) --* 

            The status of the operation. 

            
          

          - **statusChangedAt** *(datetime) --* 

            The timestamp when the status was changed (e.g., ``1479816991.349`` ).

            
          

          - **errorCode** *(string) --* 

            The error code.

            
          

          - **errorDetails** *(string) --* 

            The error details.

            
      
    

  .. py:method:: update_domain_entry(**kwargs)

    

    Updates a domain recordset after it is created.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/UpdateDomainEntry>`_    


    **Request Syntax** 
    ::

      response = client.update_domain_entry(
          domainName='string',
          domainEntry={
              'id': 'string',
              'name': 'string',
              'target': 'string',
              'isAlias': True|False,
              'type': 'string',
              'options': {
                  'string': 'string'
              }
          }
      )
    :type domainName: string
    :param domainName: **[REQUIRED]** 

      The name of the domain recordset to update.

      

    
    :type domainEntry: dict
    :param domainEntry: **[REQUIRED]** 

      An array of key-value pairs containing information about the domain entry.

      

    
      - **id** *(string) --* 

        The ID of the domain recordset entry.

        

      
      - **name** *(string) --* 

        The name of the domain.

        

      
      - **target** *(string) --* 

        The target AWS name server (e.g., ``ns-111.awsdns-22.com.`` ).

        

      
      - **isAlias** *(boolean) --* 

        When ``true`` , specifies whether the domain entry is an alias used by the Lightsail load balancer.

        

      
      - **type** *(string) --* 

        The type of domain entry (e.g., ``SOA`` or ``NS`` ).

        

      
      - **options** *(dict) --* 

        (Deprecated) The options for the domain entry.

         

        .. note::

           

          In releases prior to November 29, 2017, this parameter was not included in the API response. It is now deprecated.

           

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An array of key-value pairs containing information about the request operation.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

  .. py:method:: update_load_balancer_attribute(**kwargs)

    

    Updates the specified attribute for a load balancer.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/UpdateLoadBalancerAttribute>`_    


    **Request Syntax** 
    ::

      response = client.update_load_balancer_attribute(
          loadBalancerName='string',
          attributeName='HealthCheckPath'|'SessionStickinessEnabled'|'SessionStickiness_LB_CookieDurationSeconds',
          attributeValue='string'
      )
    :type loadBalancerName: string
    :param loadBalancerName: **[REQUIRED]** 

      The name of the load balancer that you want to modify.

      

    
    :type attributeName: string
    :param attributeName: **[REQUIRED]** 

      The name of the attribute you want to update. Valid values are below.

      

    
    :type attributeValue: string
    :param attributeValue: **[REQUIRED]** 

      The value that you want to specify for the attribute name.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An object describing the API operations.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
    

==========
Paginators
==========


The available paginators are:

* :py:class:`Lightsail.Paginator.GetActiveNames`


* :py:class:`Lightsail.Paginator.GetBlueprints`


* :py:class:`Lightsail.Paginator.GetBundles`


* :py:class:`Lightsail.Paginator.GetDomains`


* :py:class:`Lightsail.Paginator.GetInstanceSnapshots`


* :py:class:`Lightsail.Paginator.GetInstances`


* :py:class:`Lightsail.Paginator.GetKeyPairs`


* :py:class:`Lightsail.Paginator.GetOperations`


* :py:class:`Lightsail.Paginator.GetStaticIps`



.. py:class:: Lightsail.Paginator.GetActiveNames

  ::

    
    paginator = client.get_paginator('get_active_names')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_active_names`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetActiveNames>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
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
            'activeNames': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **activeNames** *(list) --* 

          The list of active names returned by the get active names request.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: Lightsail.Paginator.GetBlueprints

  ::

    
    paginator = client.get_paginator('get_blueprints')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_blueprints`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetBlueprints>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          includeInactive=True|False,
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type includeInactive: boolean
    :param includeInactive: 

      A Boolean value indicating whether to include inactive results in your request.

      

    
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
            'blueprints': [
                {
                    'blueprintId': 'string',
                    'name': 'string',
                    'group': 'string',
                    'type': 'os'|'app',
                    'description': 'string',
                    'isActive': True|False,
                    'minPower': 123,
                    'version': 'string',
                    'versionCode': 'string',
                    'productUrl': 'string',
                    'licenseUrl': 'string',
                    'platform': 'LINUX_UNIX'|'WINDOWS'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **blueprints** *(list) --* 

          An array of key-value pairs that contains information about the available blueprints.

          
          

          - *(dict) --* 

            Describes a blueprint (a virtual private server image).

            
            

            - **blueprintId** *(string) --* 

              The ID for the virtual private server image (e.g., ``app_wordpress_4_4`` or ``app_lamp_7_0`` ).

              
            

            - **name** *(string) --* 

              The friendly name of the blueprint (e.g., ``Amazon Linux`` ).

              
            

            - **group** *(string) --* 

              The group name of the blueprint (e.g., ``amazon-linux`` ).

              
            

            - **type** *(string) --* 

              The type of the blueprint (e.g., ``os`` or ``app`` ).

              
            

            - **description** *(string) --* 

              The description of the blueprint.

              
            

            - **isActive** *(boolean) --* 

              A Boolean value indicating whether the blueprint is active. When you update your blueprints, you will inactivate old blueprints and keep the most recent versions active.

              
            

            - **minPower** *(integer) --* 

              The minimum bundle power required to run this blueprint. For example, you need a bundle with a power value of 500 or more to create an instance that uses a blueprint with a minimum power value of 500. ``0`` indicates that the blueprint runs on all instance sizes. 

              
            

            - **version** *(string) --* 

              The version number of the operating system, application, or stack (e.g., ``2016.03.0`` ).

              
            

            - **versionCode** *(string) --* 

              The version code.

              
            

            - **productUrl** *(string) --* 

              The product URL to learn more about the image or blueprint.

              
            

            - **licenseUrl** *(string) --* 

              The end-user license agreement URL for the image or blueprint.

              
            

            - **platform** *(string) --* 

              The operating system platform (either Linux/Unix-based or Windows Server-based) of the blueprint.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: Lightsail.Paginator.GetBundles

  ::

    
    paginator = client.get_paginator('get_bundles')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_bundles`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetBundles>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          includeInactive=True|False,
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type includeInactive: boolean
    :param includeInactive: 

      A Boolean value that indicates whether to include inactive bundle results in your request.

      

    
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
            'bundles': [
                {
                    'price': ...,
                    'cpuCount': 123,
                    'diskSizeInGb': 123,
                    'bundleId': 'string',
                    'instanceType': 'string',
                    'isActive': True|False,
                    'name': 'string',
                    'power': 123,
                    'ramSizeInGb': ...,
                    'transferPerMonthInGb': 123,
                    'supportedPlatforms': [
                        'LINUX_UNIX'|'WINDOWS',
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **bundles** *(list) --* 

          An array of key-value pairs that contains information about the available bundles.

          
          

          - *(dict) --* 

            Describes a bundle, which is a set of specs describing your virtual private server (or *instance* ).

            
            

            - **price** *(float) --* 

              The price in US dollars (e.g., ``5.0`` ).

              
            

            - **cpuCount** *(integer) --* 

              The number of vCPUs included in the bundle (e.g., ``2`` ).

              
            

            - **diskSizeInGb** *(integer) --* 

              The size of the SSD (e.g., ``30`` ).

              
            

            - **bundleId** *(string) --* 

              The bundle ID (e.g., ``micro_1_0`` ).

              
            

            - **instanceType** *(string) --* 

              The Amazon EC2 instance type (e.g., ``t2.micro`` ).

              
            

            - **isActive** *(boolean) --* 

              A Boolean value indicating whether the bundle is active.

              
            

            - **name** *(string) --* 

              A friendly name for the bundle (e.g., ``Micro`` ).

              
            

            - **power** *(integer) --* 

              A numeric value that represents the power of the bundle (e.g., ``500`` ). You can use the bundle's power value in conjunction with a blueprint's minimum power value to determine whether the blueprint will run on the bundle. For example, you need a bundle with a power value of 500 or more to create an instance that uses a blueprint with a minimum power value of 500.

              
            

            - **ramSizeInGb** *(float) --* 

              The amount of RAM in GB (e.g., ``2.0`` ).

              
            

            - **transferPerMonthInGb** *(integer) --* 

              The data transfer rate per month in GB (e.g., ``2000`` ).

              
            

            - **supportedPlatforms** *(list) --* 

              The operating system platform (Linux/Unix-based or Windows Server-based) that the bundle supports. You can only launch a ``WINDOWS`` bundle on a blueprint that supports the ``WINDOWS`` platform. ``LINUX_UNIX`` blueprints require a ``LINUX_UNIX`` bundle.

              
              

              - *(string) --* 
          
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: Lightsail.Paginator.GetDomains

  ::

    
    paginator = client.get_paginator('get_domains')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_domains`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetDomains>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
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
            'domains': [
                {
                    'name': 'string',
                    'arn': 'string',
                    'supportCode': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'domainEntries': [
                        {
                            'id': 'string',
                            'name': 'string',
                            'target': 'string',
                            'isAlias': True|False,
                            'type': 'string',
                            'options': {
                                'string': 'string'
                            }
                        },
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **domains** *(list) --* 

          An array of key-value pairs containing information about each of the domain entries in the user's account.

          
          

          - *(dict) --* 

            Describes a domain where you are storing recordsets in Lightsail.

            
            

            - **name** *(string) --* 

              The name of the domain.

              
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the domain recordset (e.g., ``arn:aws:lightsail:global:123456789101:Domain/824cede0-abc7-4f84-8dbc-12345EXAMPLE`` ).

              
            

            - **supportCode** *(string) --* 

              The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

              
            

            - **createdAt** *(datetime) --* 

              The date when the domain recordset was created.

              
            

            - **location** *(dict) --* 

              The AWS Region and Availability Zones where the domain recordset was created.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **domainEntries** *(list) --* 

              An array of key-value pairs containing information about the domain entries.

              
              

              - *(dict) --* 

                Describes a domain recordset entry.

                
                

                - **id** *(string) --* 

                  The ID of the domain recordset entry.

                  
                

                - **name** *(string) --* 

                  The name of the domain.

                  
                

                - **target** *(string) --* 

                  The target AWS name server (e.g., ``ns-111.awsdns-22.com.`` ).

                  
                

                - **isAlias** *(boolean) --* 

                  When ``true`` , specifies whether the domain entry is an alias used by the Lightsail load balancer.

                  
                

                - **type** *(string) --* 

                  The type of domain entry (e.g., ``SOA`` or ``NS`` ).

                  
                

                - **options** *(dict) --* 

                  (Deprecated) The options for the domain entry.

                   

                  .. note::

                     

                    In releases prior to November 29, 2017, this parameter was not included in the API response. It is now deprecated.

                     

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
            
          
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: Lightsail.Paginator.GetInstanceSnapshots

  ::

    
    paginator = client.get_paginator('get_instance_snapshots')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_instance_snapshots`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetInstanceSnapshots>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
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
            'instanceSnapshots': [
                {
                    'name': 'string',
                    'arn': 'string',
                    'supportCode': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'state': 'pending'|'error'|'available',
                    'progress': 'string',
                    'fromAttachedDisks': [
                        {
                            'name': 'string',
                            'arn': 'string',
                            'supportCode': 'string',
                            'createdAt': datetime(2015, 1, 1),
                            'location': {
                                'availabilityZone': 'string',
                                'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                            },
                            'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                            'sizeInGb': 123,
                            'isSystemDisk': True|False,
                            'iops': 123,
                            'path': 'string',
                            'state': 'pending'|'error'|'available'|'in-use'|'unknown',
                            'attachedTo': 'string',
                            'isAttached': True|False,
                            'attachmentState': 'string',
                            'gbInUse': 123
                        },
                    ],
                    'fromInstanceName': 'string',
                    'fromInstanceArn': 'string',
                    'fromBlueprintId': 'string',
                    'fromBundleId': 'string',
                    'sizeInGb': 123
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **instanceSnapshots** *(list) --* 

          An array of key-value pairs containing information about the results of your get instance snapshots request.

          
          

          - *(dict) --* 

            Describes the snapshot of the virtual private server, or *instance* .

            
            

            - **name** *(string) --* 

              The name of the snapshot.

              
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the snapshot (e.g., ``arn:aws:lightsail:us-east-2:123456789101:InstanceSnapshot/d23b5706-3322-4d83-81e5-12345EXAMPLE`` ).

              
            

            - **supportCode** *(string) --* 

              The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the snapshot was created (e.g., ``1479907467.024`` ).

              
            

            - **location** *(dict) --* 

              The region name and availability zone where you created the snapshot.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **resourceType** *(string) --* 

              The type of resource (usually ``InstanceSnapshot`` ).

              
            

            - **state** *(string) --* 

              The state the snapshot is in.

              
            

            - **progress** *(string) --* 

              The progress of the snapshot.

              
            

            - **fromAttachedDisks** *(list) --* 

              An array of disk objects containing information about all block storage disks.

              
              

              - *(dict) --* 

                Describes a system disk or an block storage disk.

                
                

                - **name** *(string) --* 

                  The unique name of the disk.

                  
                

                - **arn** *(string) --* 

                  The Amazon Resource Name (ARN) of the disk.

                  
                

                - **supportCode** *(string) --* 

                  The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

                  
                

                - **createdAt** *(datetime) --* 

                  The date when the disk was created.

                  
                

                - **location** *(dict) --* 

                  The AWS Region and Availability Zone where the disk is located.

                  
                  

                  - **availabilityZone** *(string) --* 

                    The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                    
                  

                  - **regionName** *(string) --* 

                    The AWS Region name.

                    
              
                

                - **resourceType** *(string) --* 

                  The Lightsail resource type (e.g., ``Disk`` ).

                  
                

                - **sizeInGb** *(integer) --* 

                  The size of the disk in GB.

                  
                

                - **isSystemDisk** *(boolean) --* 

                  A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).

                  
                

                - **iops** *(integer) --* 

                  The input/output operations per second (IOPS) of the disk.

                  
                

                - **path** *(string) --* 

                  The disk path.

                  
                

                - **state** *(string) --* 

                  Describes the status of the disk.

                  
                

                - **attachedTo** *(string) --* 

                  The resources to which the disk is attached.

                  
                

                - **isAttached** *(boolean) --* 

                  A Boolean value indicating whether the disk is attached.

                  
                

                - **attachmentState** *(string) --* 

                  (Deprecated) The attachment state of the disk.

                   

                  .. note::

                     

                    In releases prior to November 14, 2017, this parameter returned ``attached`` for system disks in the API response. It is now deprecated, but still included in the response. Use ``isAttached`` instead.

                     

                  
                

                - **gbInUse** *(integer) --* 

                  (Deprecated) The number of GB in use by the disk.

                   

                  .. note::

                     

                    In releases prior to November 14, 2017, this parameter was not included in the API response. It is now deprecated.

                     

                  
            
          
            

            - **fromInstanceName** *(string) --* 

              The instance from which the snapshot was created.

              
            

            - **fromInstanceArn** *(string) --* 

              The Amazon Resource Name (ARN) of the instance from which the snapshot was created (e.g., ``arn:aws:lightsail:us-east-2:123456789101:Instance/64b8404c-ccb1-430b-8daf-12345EXAMPLE`` ).

              
            

            - **fromBlueprintId** *(string) --* 

              The blueprint ID from which you created the snapshot (e.g., ``os_debian_8_3`` ). A blueprint is a virtual private server (or *instance* ) image used to create instances quickly.

              
            

            - **fromBundleId** *(string) --* 

              The bundle ID from which you created the snapshot (e.g., ``micro_1_0`` ).

              
            

            - **sizeInGb** *(integer) --* 

              The size in GB of the SSD.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: Lightsail.Paginator.GetInstances

  ::

    
    paginator = client.get_paginator('get_instances')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_instances`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetInstances>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
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
            'instances': [
                {
                    'name': 'string',
                    'arn': 'string',
                    'supportCode': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'blueprintId': 'string',
                    'blueprintName': 'string',
                    'bundleId': 'string',
                    'isStaticIp': True|False,
                    'privateIpAddress': 'string',
                    'publicIpAddress': 'string',
                    'ipv6Address': 'string',
                    'hardware': {
                        'cpuCount': 123,
                        'disks': [
                            {
                                'name': 'string',
                                'arn': 'string',
                                'supportCode': 'string',
                                'createdAt': datetime(2015, 1, 1),
                                'location': {
                                    'availabilityZone': 'string',
                                    'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                                },
                                'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                                'sizeInGb': 123,
                                'isSystemDisk': True|False,
                                'iops': 123,
                                'path': 'string',
                                'state': 'pending'|'error'|'available'|'in-use'|'unknown',
                                'attachedTo': 'string',
                                'isAttached': True|False,
                                'attachmentState': 'string',
                                'gbInUse': 123
                            },
                        ],
                        'ramSizeInGb': ...
                    },
                    'networking': {
                        'monthlyTransfer': {
                            'gbPerMonthAllocated': 123
                        },
                        'ports': [
                            {
                                'fromPort': 123,
                                'toPort': 123,
                                'protocol': 'tcp'|'all'|'udp',
                                'accessFrom': 'string',
                                'accessType': 'Public'|'Private',
                                'commonName': 'string',
                                'accessDirection': 'inbound'|'outbound'
                            },
                        ]
                    },
                    'state': {
                        'code': 123,
                        'name': 'string'
                    },
                    'username': 'string',
                    'sshKeyName': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **instances** *(list) --* 

          An array of key-value pairs containing information about your instances.

          
          

          - *(dict) --* 

            Describes an instance (a virtual private server).

            
            

            - **name** *(string) --* 

              The name the user gave the instance (e.g., ``Amazon_Linux-1GB-Ohio-1`` ).

              
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the instance (e.g., ``arn:aws:lightsail:us-east-2:123456789101:Instance/244ad76f-8aad-4741-809f-12345EXAMPLE`` ).

              
            

            - **supportCode** *(string) --* 

              The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the instance was created (e.g., ``1479734909.17`` ).

              
            

            - **location** *(dict) --* 

              The region name and availability zone where the instance is located.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **resourceType** *(string) --* 

              The type of resource (usually ``Instance`` ).

              
            

            - **blueprintId** *(string) --* 

              The blueprint ID (e.g., ``os_amlinux_2016_03`` ).

              
            

            - **blueprintName** *(string) --* 

              The friendly name of the blueprint (e.g., ``Amazon Linux`` ).

              
            

            - **bundleId** *(string) --* 

              The bundle for the instance (e.g., ``micro_1_0`` ).

              
            

            - **isStaticIp** *(boolean) --* 

              A Boolean value indicating whether this instance has a static IP assigned to it.

              
            

            - **privateIpAddress** *(string) --* 

              The private IP address of the instance.

              
            

            - **publicIpAddress** *(string) --* 

              The public IP address of the instance.

              
            

            - **ipv6Address** *(string) --* 

              The IPv6 address of the instance.

              
            

            - **hardware** *(dict) --* 

              The size of the vCPU and the amount of RAM for the instance.

              
              

              - **cpuCount** *(integer) --* 

                The number of vCPUs the instance has.

                
              

              - **disks** *(list) --* 

                The disks attached to the instance.

                
                

                - *(dict) --* 

                  Describes a system disk or an block storage disk.

                  
                  

                  - **name** *(string) --* 

                    The unique name of the disk.

                    
                  

                  - **arn** *(string) --* 

                    The Amazon Resource Name (ARN) of the disk.

                    
                  

                  - **supportCode** *(string) --* 

                    The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

                    
                  

                  - **createdAt** *(datetime) --* 

                    The date when the disk was created.

                    
                  

                  - **location** *(dict) --* 

                    The AWS Region and Availability Zone where the disk is located.

                    
                    

                    - **availabilityZone** *(string) --* 

                      The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                      
                    

                    - **regionName** *(string) --* 

                      The AWS Region name.

                      
                
                  

                  - **resourceType** *(string) --* 

                    The Lightsail resource type (e.g., ``Disk`` ).

                    
                  

                  - **sizeInGb** *(integer) --* 

                    The size of the disk in GB.

                    
                  

                  - **isSystemDisk** *(boolean) --* 

                    A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).

                    
                  

                  - **iops** *(integer) --* 

                    The input/output operations per second (IOPS) of the disk.

                    
                  

                  - **path** *(string) --* 

                    The disk path.

                    
                  

                  - **state** *(string) --* 

                    Describes the status of the disk.

                    
                  

                  - **attachedTo** *(string) --* 

                    The resources to which the disk is attached.

                    
                  

                  - **isAttached** *(boolean) --* 

                    A Boolean value indicating whether the disk is attached.

                    
                  

                  - **attachmentState** *(string) --* 

                    (Deprecated) The attachment state of the disk.

                     

                    .. note::

                       

                      In releases prior to November 14, 2017, this parameter returned ``attached`` for system disks in the API response. It is now deprecated, but still included in the response. Use ``isAttached`` instead.

                       

                    
                  

                  - **gbInUse** *(integer) --* 

                    (Deprecated) The number of GB in use by the disk.

                     

                    .. note::

                       

                      In releases prior to November 14, 2017, this parameter was not included in the API response. It is now deprecated.

                       

                    
              
            
              

              - **ramSizeInGb** *(float) --* 

                The amount of RAM in GB on the instance (e.g., ``1.0`` ).

                
          
            

            - **networking** *(dict) --* 

              Information about the public ports and monthly data transfer rates for the instance.

              
              

              - **monthlyTransfer** *(dict) --* 

                The amount of data in GB allocated for monthly data transfers.

                
                

                - **gbPerMonthAllocated** *(integer) --* 

                  The amount allocated per month (in GB).

                  
            
              

              - **ports** *(list) --* 

                An array of key-value pairs containing information about the ports on the instance.

                
                

                - *(dict) --* 

                  Describes information about the instance ports.

                  
                  

                  - **fromPort** *(integer) --* 

                    The first port in the range.

                    
                  

                  - **toPort** *(integer) --* 

                    The last port in the range.

                    
                  

                  - **protocol** *(string) --* 

                    The protocol being used. Can be one of the following.

                     

                     
                    * ``tcp`` - Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesn't require reliable data stream service, use UDP instead. 
                     
                    * ``all`` - All transport layer protocol types. For more general information, see `Transport layer <https://en.wikipedia.org/wiki/Transport_layer>`__ on Wikipedia. 
                     
                    * ``udp`` - With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that don't require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead. 
                     

                    
                  

                  - **accessFrom** *(string) --* 

                    The location from which access is allowed (e.g., ``Anywhere (0.0.0.0/0)`` ).

                    
                  

                  - **accessType** *(string) --* 

                    The type of access (``Public`` or ``Private`` ).

                    
                  

                  - **commonName** *(string) --* 

                    The common name.

                    
                  

                  - **accessDirection** *(string) --* 

                    The access direction (``inbound`` or ``outbound`` ).

                    
              
            
          
            

            - **state** *(dict) --* 

              The status code and the state (e.g., ``running`` ) for the instance.

              
              

              - **code** *(integer) --* 

                The status code for the instance.

                
              

              - **name** *(string) --* 

                The state of the instance (e.g., ``running`` or ``pending`` ).

                
          
            

            - **username** *(string) --* 

              The user name for connecting to the instance (e.g., ``ec2-user`` ).

              
            

            - **sshKeyName** *(string) --* 

              The name of the SSH key being used to connect to the instance (e.g., ``LightsailDefaultKeyPair`` ).

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: Lightsail.Paginator.GetKeyPairs

  ::

    
    paginator = client.get_paginator('get_key_pairs')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_key_pairs`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetKeyPairs>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
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
            'keyPairs': [
                {
                    'name': 'string',
                    'arn': 'string',
                    'supportCode': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'fingerprint': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **keyPairs** *(list) --* 

          An array of key-value pairs containing information about the key pairs.

          
          

          - *(dict) --* 

            Describes the SSH key pair.

            
            

            - **name** *(string) --* 

              The friendly name of the SSH key pair.

              
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the key pair (e.g., ``arn:aws:lightsail:us-east-2:123456789101:KeyPair/05859e3d-331d-48ba-9034-12345EXAMPLE`` ).

              
            

            - **supportCode** *(string) --* 

              The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the key pair was created (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region name and Availability Zone where the key pair was created.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **resourceType** *(string) --* 

              The resource type (usually ``KeyPair`` ).

              
            

            - **fingerprint** *(string) --* 

              The RSA fingerprint of the key pair.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: Lightsail.Paginator.GetOperations

  ::

    
    paginator = client.get_paginator('get_operations')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_operations`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetOperations>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
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
            'operations': [
                {
                    'id': 'string',
                    'resourceName': 'string',
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'isTerminal': True|False,
                    'operationDetails': 'string',
                    'operationType': 'DeleteInstance'|'CreateInstance'|'StopInstance'|'StartInstance'|'RebootInstance'|'OpenInstancePublicPorts'|'PutInstancePublicPorts'|'CloseInstancePublicPorts'|'AllocateStaticIp'|'ReleaseStaticIp'|'AttachStaticIp'|'DetachStaticIp'|'UpdateDomainEntry'|'DeleteDomainEntry'|'CreateDomain'|'DeleteDomain'|'CreateInstanceSnapshot'|'DeleteInstanceSnapshot'|'CreateInstancesFromSnapshot'|'CreateLoadBalancer'|'DeleteLoadBalancer'|'AttachInstancesToLoadBalancer'|'DetachInstancesFromLoadBalancer'|'UpdateLoadBalancerAttribute'|'CreateLoadBalancerTlsCertificate'|'DeleteLoadBalancerTlsCertificate'|'AttachLoadBalancerTlsCertificate'|'CreateDisk'|'DeleteDisk'|'AttachDisk'|'DetachDisk'|'CreateDiskSnapshot'|'DeleteDiskSnapshot'|'CreateDiskFromSnapshot',
                    'status': 'NotStarted'|'Started'|'Failed'|'Completed',
                    'statusChangedAt': datetime(2015, 1, 1),
                    'errorCode': 'string',
                    'errorDetails': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **operations** *(list) --* 

          An array of key-value pairs containing information about the results of your get operations request.

          
          

          - *(dict) --* 

            Describes the API operation.

            
            

            - **id** *(string) --* 

              The ID of the operation.

              
            

            - **resourceName** *(string) --* 

              The resource name.

              
            

            - **resourceType** *(string) --* 

              The resource type. 

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the operation was initialized (e.g., ``1479816991.349`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **isTerminal** *(boolean) --* 

              A Boolean value indicating whether the operation is terminal.

              
            

            - **operationDetails** *(string) --* 

              Details about the operation (e.g., ``Debian-1GB-Ohio-1`` ).

              
            

            - **operationType** *(string) --* 

              The type of operation. 

              
            

            - **status** *(string) --* 

              The status of the operation. 

              
            

            - **statusChangedAt** *(datetime) --* 

              The timestamp when the status was changed (e.g., ``1479816991.349`` ).

              
            

            - **errorCode** *(string) --* 

              The error code.

              
            

            - **errorDetails** *(string) --* 

              The error details.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: Lightsail.Paginator.GetStaticIps

  ::

    
    paginator = client.get_paginator('get_static_ips')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Lightsail.Client.get_static_ips`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetStaticIps>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
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
            'staticIps': [
                {
                    'name': 'string',
                    'arn': 'string',
                    'supportCode': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'location': {
                        'availabilityZone': 'string',
                        'regionName': 'us-east-1'|'us-east-2'|'us-west-1'|'us-west-2'|'eu-west-1'|'eu-central-1'|'ap-south-1'|'ap-southeast-1'|'ap-southeast-2'|'ap-northeast-1'|'ap-northeast-2'
                    },
                    'resourceType': 'Instance'|'StaticIp'|'KeyPair'|'InstanceSnapshot'|'Domain'|'PeeredVpc'|'LoadBalancer'|'LoadBalancerTlsCertificate'|'Disk'|'DiskSnapshot',
                    'ipAddress': 'string',
                    'attachedTo': 'string',
                    'isAttached': True|False
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **staticIps** *(list) --* 

          An array of key-value pairs containing information about your get static IPs request.

          
          

          - *(dict) --* 

            Describes the static IP.

            
            

            - **name** *(string) --* 

              The name of the static IP (e.g., ``StaticIP-Ohio-EXAMPLE`` ).

              
            

            - **arn** *(string) --* 

              The Amazon Resource Name (ARN) of the static IP (e.g., ``arn:aws:lightsail:us-east-2:123456789101:StaticIp/9cbb4a9e-f8e3-4dfe-b57e-12345EXAMPLE`` ).

              
            

            - **supportCode** *(string) --* 

              The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.

              
            

            - **createdAt** *(datetime) --* 

              The timestamp when the static IP was created (e.g., ``1479735304.222`` ).

              
            

            - **location** *(dict) --* 

              The region and Availability Zone where the static IP was created.

              
              

              - **availabilityZone** *(string) --* 

                The Availability Zone. Follows the format ``us-east-2a`` (case-sensitive).

                
              

              - **regionName** *(string) --* 

                The AWS Region name.

                
          
            

            - **resourceType** *(string) --* 

              The resource type (usually ``StaticIp`` ).

              
            

            - **ipAddress** *(string) --* 

              The static IP address.

              
            

            - **attachedTo** *(string) --* 

              The instance where the static IP is attached (e.g., ``Amazon_Linux-1GB-Ohio-1`` ).

              
            

            - **isAttached** *(boolean) --* 

              A Boolean value indicating whether the static IP is attached.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    