

********************
ElasticsearchService
********************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: ElasticsearchService.Client

  A low-level client representing Amazon Elasticsearch Service::

    
    import boto3
    
    client = boto3.client('es')

  
  These are the available methods:
  
  *   :py:meth:`~ElasticsearchService.Client.add_tags`

  
  *   :py:meth:`~ElasticsearchService.Client.can_paginate`

  
  *   :py:meth:`~ElasticsearchService.Client.create_elasticsearch_domain`

  
  *   :py:meth:`~ElasticsearchService.Client.delete_elasticsearch_domain`

  
  *   :py:meth:`~ElasticsearchService.Client.delete_elasticsearch_service_role`

  
  *   :py:meth:`~ElasticsearchService.Client.describe_elasticsearch_domain`

  
  *   :py:meth:`~ElasticsearchService.Client.describe_elasticsearch_domain_config`

  
  *   :py:meth:`~ElasticsearchService.Client.describe_elasticsearch_domains`

  
  *   :py:meth:`~ElasticsearchService.Client.describe_elasticsearch_instance_type_limits`

  
  *   :py:meth:`~ElasticsearchService.Client.generate_presigned_url`

  
  *   :py:meth:`~ElasticsearchService.Client.get_paginator`

  
  *   :py:meth:`~ElasticsearchService.Client.get_waiter`

  
  *   :py:meth:`~ElasticsearchService.Client.list_domain_names`

  
  *   :py:meth:`~ElasticsearchService.Client.list_elasticsearch_instance_types`

  
  *   :py:meth:`~ElasticsearchService.Client.list_elasticsearch_versions`

  
  *   :py:meth:`~ElasticsearchService.Client.list_tags`

  
  *   :py:meth:`~ElasticsearchService.Client.remove_tags`

  
  *   :py:meth:`~ElasticsearchService.Client.update_elasticsearch_domain_config`

  

  .. py:method:: add_tags(**kwargs)

    

    Attaches tags to an existing Elasticsearch domain. Tags are a set of case-sensitive key value pairs. An Elasticsearch domain may have up to 10 tags. See `Tagging Amazon Elasticsearch Service Domains for more information. <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-awsresorcetagging>`__ 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/AddTags>`_    


    **Request Syntax** 
    ::

      response = client.add_tags(
          ARN='string',
          TagList=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type ARN: string
    :param ARN: **[REQUIRED]** 

      Specify the ``ARN`` for which you want to add the tags.

      

    
    :type TagList: list
    :param TagList: **[REQUIRED]** 

      List of ``Tag`` that need to be added for the Elasticsearch domain. 

      

    
      - *(dict) --* 

        Specifies a key value pair for a resource tag.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          Specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for the Elasticsearch domain to which they are attached.

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          Specifies the ``TagValue`` , the value assigned to the corresponding tag key. Tag values can be null and do not have to be unique in a tag set. For example, you can have a key value pair in a tag set of ``project : Trinity`` and ``cost-center : Trinity`` 

          

        
      
  
    
    :returns: None

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


  .. py:method:: create_elasticsearch_domain(**kwargs)

    

    Creates a new Elasticsearch domain. For more information, see `Creating Elasticsearch Domains <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomains>`__ in the *Amazon Elasticsearch Service Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/CreateElasticsearchDomain>`_    


    **Request Syntax** 
    ::

      response = client.create_elasticsearch_domain(
          DomainName='string',
          ElasticsearchVersion='string',
          ElasticsearchClusterConfig={
              'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
              'InstanceCount': 123,
              'DedicatedMasterEnabled': True|False,
              'ZoneAwarenessEnabled': True|False,
              'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
              'DedicatedMasterCount': 123
          },
          EBSOptions={
              'EBSEnabled': True|False,
              'VolumeType': 'standard'|'gp2'|'io1',
              'VolumeSize': 123,
              'Iops': 123
          },
          AccessPolicies='string',
          SnapshotOptions={
              'AutomatedSnapshotStartHour': 123
          },
          VPCOptions={
              'SubnetIds': [
                  'string',
              ],
              'SecurityGroupIds': [
                  'string',
              ]
          },
          EncryptionAtRestOptions={
              'Enabled': True|False,
              'KmsKeyId': 'string'
          },
          AdvancedOptions={
              'string': 'string'
          },
          LogPublishingOptions={
              'string': {
                  'CloudWatchLogsLogGroupArn': 'string',
                  'Enabled': True|False
              }
          }
      )
    :type DomainName: string
    :param DomainName: **[REQUIRED]** 

      The name of the Elasticsearch domain that you are creating. Domain names are unique across the domains owned by an account within an AWS region. Domain names must start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).

      

    
    :type ElasticsearchVersion: string
    :param ElasticsearchVersion: 

      String of format X.Y to specify version for the Elasticsearch domain eg. "1.5" or "2.3". For more information, see `Creating Elasticsearch Domains <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomains>`__ in the *Amazon Elasticsearch Service Developer Guide* .

      

    
    :type ElasticsearchClusterConfig: dict
    :param ElasticsearchClusterConfig: 

      Configuration options for an Elasticsearch domain. Specifies the instance type and number of instances in the domain cluster. 

      

    
      - **InstanceType** *(string) --* 

        The instance type for an Elasticsearch cluster.

        

      
      - **InstanceCount** *(integer) --* 

        The number of instances in the specified domain cluster.

        

      
      - **DedicatedMasterEnabled** *(boolean) --* 

        A boolean value to indicate whether a dedicated master node is enabled. See `About Dedicated Master Nodes <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__ for more information.

        

      
      - **ZoneAwarenessEnabled** *(boolean) --* 

        A boolean value to indicate whether zone awareness is enabled. See `About Zone Awareness <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__ for more information.

        

      
      - **DedicatedMasterType** *(string) --* 

        The instance type for a dedicated master node.

        

      
      - **DedicatedMasterCount** *(integer) --* 

        Total number of dedicated master nodes, active and on standby, for the cluster.

        

      
    
    :type EBSOptions: dict
    :param EBSOptions: 

      Options to enable, disable and specify the type and size of EBS storage volumes. 

      

    
      - **EBSEnabled** *(boolean) --* 

        Specifies whether EBS-based storage is enabled.

        

      
      - **VolumeType** *(string) --* 

        Specifies the volume type for EBS-based storage.

        

      
      - **VolumeSize** *(integer) --* 

        Integer to specify the size of an EBS volume.

        

      
      - **Iops** *(integer) --* 

        Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).

        

      
    
    :type AccessPolicies: string
    :param AccessPolicies: 

      IAM access policy as a JSON-formatted string.

      

    
    :type SnapshotOptions: dict
    :param SnapshotOptions: 

      Option to set time, in UTC format, of the daily automated snapshot. Default value is 0 hours. 

      

    
      - **AutomatedSnapshotStartHour** *(integer) --* 

        Specifies the time, in UTC format, when the service takes a daily automated snapshot of the specified Elasticsearch domain. Default value is ``0`` hours.

        

      
    
    :type VPCOptions: dict
    :param VPCOptions: 

      Options to specify the subnets and security groups for VPC endpoint. For more information, see `Creating a VPC <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-creating-vpc>`__ in *VPC Endpoints for Amazon Elasticsearch Service Domains* 

      

    
      - **SubnetIds** *(list) --* 

        Specifies the subnets for VPC endpoint.

        

      
        - *(string) --* 

        
    
      - **SecurityGroupIds** *(list) --* 

        Specifies the security groups for VPC endpoint.

        

      
        - *(string) --* 

        
    
    
    :type EncryptionAtRestOptions: dict
    :param EncryptionAtRestOptions: 

      Specifies the Encryption At Rest Options.

      

    
      - **Enabled** *(boolean) --* 

        Specifies the option to enable Encryption At Rest.

        

      
      - **KmsKeyId** *(string) --* 

        Specifies the KMS Key ID for Encryption At Rest options.

        

      
    
    :type AdvancedOptions: dict
    :param AdvancedOptions: 

      Option to allow references to indices in an HTTP request body. Must be ``false`` when configuring access to individual sub-resources. By default, the value is ``true`` . See `Configuration Advanced Options <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-advanced-options>`__ for more information.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type LogPublishingOptions: dict
    :param LogPublishingOptions: 

      Map of ``LogType`` and ``LogPublishingOption`` , each containing options to publish a given type of Elasticsearch log.

      

    
      - *(string) --* 

        Type of Log File, it can be one of the following: 

         
        * INDEX_SLOW_LOGS: Index slow logs contains insert requests that took more time than configured index query log threshold to execute.
         
        * SEARCH_SLOW_LOGS: Search slow logs contains search queries that took more time than configured search query log threshold to execute.
         

         

        

      
        - *(dict) --* 

          Log Publishing option that is set for given domain. Attributes and their details: 

           
          * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be published.
           
          * Enabled: Whether the log publishing for given log type is enabled or not
           

           

          

        
          - **CloudWatchLogsLogGroupArn** *(string) --* 

            ARN of the Cloudwatch log group to which log needs to be published.

            

          
          - **Enabled** *(boolean) --* 

            Specifies whether given log publishing option is enabled or not.

            

          
        
  

    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DomainStatus': {
                'DomainId': 'string',
                'DomainName': 'string',
                'ARN': 'string',
                'Created': True|False,
                'Deleted': True|False,
                'Endpoint': 'string',
                'Endpoints': {
                    'string': 'string'
                },
                'Processing': True|False,
                'ElasticsearchVersion': 'string',
                'ElasticsearchClusterConfig': {
                    'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                    'InstanceCount': 123,
                    'DedicatedMasterEnabled': True|False,
                    'ZoneAwarenessEnabled': True|False,
                    'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                    'DedicatedMasterCount': 123
                },
                'EBSOptions': {
                    'EBSEnabled': True|False,
                    'VolumeType': 'standard'|'gp2'|'io1',
                    'VolumeSize': 123,
                    'Iops': 123
                },
                'AccessPolicies': 'string',
                'SnapshotOptions': {
                    'AutomatedSnapshotStartHour': 123
                },
                'VPCOptions': {
                    'VPCId': 'string',
                    'SubnetIds': [
                        'string',
                    ],
                    'AvailabilityZones': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ]
                },
                'EncryptionAtRestOptions': {
                    'Enabled': True|False,
                    'KmsKeyId': 'string'
                },
                'AdvancedOptions': {
                    'string': 'string'
                },
                'LogPublishingOptions': {
                    'string': {
                        'CloudWatchLogsLogGroupArn': 'string',
                        'Enabled': True|False
                    }
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        The result of a ``CreateElasticsearchDomain`` operation. Contains the status of the newly created Elasticsearch domain.

        
        

        - **DomainStatus** *(dict) --* 

          The status of the newly created Elasticsearch domain. 

          
          

          - **DomainId** *(string) --* 

            The unique identifier for the specified Elasticsearch domain.

            
          

          - **DomainName** *(string) --* 

            The name of an Elasticsearch domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).

            
          

          - **ARN** *(string) --* 

            The Amazon resource name (ARN) of an Elasticsearch domain. See `Identifiers for IAM Entities <http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html>`__ in *Using AWS Identity and Access Management* for more information.

            
          

          - **Created** *(boolean) --* 

            The domain creation status. ``True`` if the creation of an Elasticsearch domain is complete. ``False`` if domain creation is still in progress.

            
          

          - **Deleted** *(boolean) --* 

            The domain deletion status. ``True`` if a delete request has been received for the domain but resource cleanup is still in progress. ``False`` if the domain has not been deleted. Once domain deletion is complete, the status of the domain is no longer returned.

            
          

          - **Endpoint** *(string) --* 

            The Elasticsearch domain endpoint that you use to submit index and search requests.

            
          

          - **Endpoints** *(dict) --* 

            Map containing the Elasticsearch domain endpoints used to submit index and search requests. Example ``key, value`` : ``'vpc','vpc-endpoint-h2dsd34efgyghrtguk5gt6j2foh4.us-east-1.es.amazonaws.com'`` .

            
            

            - *(string) --* 
              

              - *(string) --* 

                The endpoint to which service requests are submitted. For example, ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.es.amazonaws.com`` or ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.es.amazonaws.com`` .

                
        
      
          

          - **Processing** *(boolean) --* 

            The status of the Elasticsearch domain configuration. ``True`` if Amazon Elasticsearch Service is processing configuration changes. ``False`` if the configuration is active.

            
          

          - **ElasticsearchVersion** *(string) --* 
          

          - **ElasticsearchClusterConfig** *(dict) --* 

            The type and number of instances in the domain cluster.

            
            

            - **InstanceType** *(string) --* 

              The instance type for an Elasticsearch cluster.

              
            

            - **InstanceCount** *(integer) --* 

              The number of instances in the specified domain cluster.

              
            

            - **DedicatedMasterEnabled** *(boolean) --* 

              A boolean value to indicate whether a dedicated master node is enabled. See `About Dedicated Master Nodes <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__ for more information.

              
            

            - **ZoneAwarenessEnabled** *(boolean) --* 

              A boolean value to indicate whether zone awareness is enabled. See `About Zone Awareness <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__ for more information.

              
            

            - **DedicatedMasterType** *(string) --* 

              The instance type for a dedicated master node.

              
            

            - **DedicatedMasterCount** *(integer) --* 

              Total number of dedicated master nodes, active and on standby, for the cluster.

              
        
          

          - **EBSOptions** *(dict) --* 

            The ``EBSOptions`` for the specified domain. See `Configuring EBS-based Storage <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs>`__ for more information.

            
            

            - **EBSEnabled** *(boolean) --* 

              Specifies whether EBS-based storage is enabled.

              
            

            - **VolumeType** *(string) --* 

              Specifies the volume type for EBS-based storage.

              
            

            - **VolumeSize** *(integer) --* 

              Integer to specify the size of an EBS volume.

              
            

            - **Iops** *(integer) --* 

              Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).

              
        
          

          - **AccessPolicies** *(string) --* 

            IAM access policy as a JSON-formatted string.

            
          

          - **SnapshotOptions** *(dict) --* 

            Specifies the status of the ``SnapshotOptions`` 

            
            

            - **AutomatedSnapshotStartHour** *(integer) --* 

              Specifies the time, in UTC format, when the service takes a daily automated snapshot of the specified Elasticsearch domain. Default value is ``0`` hours.

              
        
          

          - **VPCOptions** *(dict) --* 

            The ``VPCOptions`` for the specified domain. For more information, see `VPC Endpoints for Amazon Elasticsearch Service Domains <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html>`__ .

            
            

            - **VPCId** *(string) --* 

              The VPC Id for the Elasticsearch domain. Exists only if the domain was created with VPCOptions.

              
            

            - **SubnetIds** *(list) --* 

              Specifies the subnets for VPC endpoint.

              
              

              - *(string) --* 
          
            

            - **AvailabilityZones** *(list) --* 

              The availability zones for the Elasticsearch domain. Exists only if the domain was created with VPCOptions.

              
              

              - *(string) --* 
          
            

            - **SecurityGroupIds** *(list) --* 

              Specifies the security groups for VPC endpoint.

              
              

              - *(string) --* 
          
        
          

          - **EncryptionAtRestOptions** *(dict) --* 

            Specifies the status of the ``EncryptionAtRestOptions`` .

            
            

            - **Enabled** *(boolean) --* 

              Specifies the option to enable Encryption At Rest.

              
            

            - **KmsKeyId** *(string) --* 

              Specifies the KMS Key ID for Encryption At Rest options.

              
        
          

          - **AdvancedOptions** *(dict) --* 

            Specifies the status of the ``AdvancedOptions`` 

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **LogPublishingOptions** *(dict) --* 

            Log publishing options for the given domain.

            
            

            - *(string) --* 

              Type of Log File, it can be one of the following: 

               
              * INDEX_SLOW_LOGS: Index slow logs contains insert requests that took more time than configured index query log threshold to execute.
               
              * SEARCH_SLOW_LOGS: Search slow logs contains search queries that took more time than configured search query log threshold to execute.
               

               

              
              

              - *(dict) --* 

                Log Publishing option that is set for given domain. Attributes and their details: 

                 
                * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be published.
                 
                * Enabled: Whether the log publishing for given log type is enabled or not
                 

                 

                
                

                - **CloudWatchLogsLogGroupArn** *(string) --* 

                  ARN of the Cloudwatch log group to which log needs to be published.

                  
                

                - **Enabled** *(boolean) --* 

                  Specifies whether given log publishing option is enabled or not.

                  
            
        
      
      
    

  .. py:method:: delete_elasticsearch_domain(**kwargs)

    

    Permanently deletes the specified Elasticsearch domain and all of its data. Once a domain is deleted, it cannot be recovered.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/DeleteElasticsearchDomain>`_    


    **Request Syntax** 
    ::

      response = client.delete_elasticsearch_domain(
          DomainName='string'
      )
    :type DomainName: string
    :param DomainName: **[REQUIRED]** 

      The name of the Elasticsearch domain that you want to permanently delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DomainStatus': {
                'DomainId': 'string',
                'DomainName': 'string',
                'ARN': 'string',
                'Created': True|False,
                'Deleted': True|False,
                'Endpoint': 'string',
                'Endpoints': {
                    'string': 'string'
                },
                'Processing': True|False,
                'ElasticsearchVersion': 'string',
                'ElasticsearchClusterConfig': {
                    'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                    'InstanceCount': 123,
                    'DedicatedMasterEnabled': True|False,
                    'ZoneAwarenessEnabled': True|False,
                    'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                    'DedicatedMasterCount': 123
                },
                'EBSOptions': {
                    'EBSEnabled': True|False,
                    'VolumeType': 'standard'|'gp2'|'io1',
                    'VolumeSize': 123,
                    'Iops': 123
                },
                'AccessPolicies': 'string',
                'SnapshotOptions': {
                    'AutomatedSnapshotStartHour': 123
                },
                'VPCOptions': {
                    'VPCId': 'string',
                    'SubnetIds': [
                        'string',
                    ],
                    'AvailabilityZones': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ]
                },
                'EncryptionAtRestOptions': {
                    'Enabled': True|False,
                    'KmsKeyId': 'string'
                },
                'AdvancedOptions': {
                    'string': 'string'
                },
                'LogPublishingOptions': {
                    'string': {
                        'CloudWatchLogsLogGroupArn': 'string',
                        'Enabled': True|False
                    }
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        The result of a ``DeleteElasticsearchDomain`` request. Contains the status of the pending deletion, or no status if the domain and all of its resources have been deleted.

        
        

        - **DomainStatus** *(dict) --* 

          The status of the Elasticsearch domain being deleted.

          
          

          - **DomainId** *(string) --* 

            The unique identifier for the specified Elasticsearch domain.

            
          

          - **DomainName** *(string) --* 

            The name of an Elasticsearch domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).

            
          

          - **ARN** *(string) --* 

            The Amazon resource name (ARN) of an Elasticsearch domain. See `Identifiers for IAM Entities <http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html>`__ in *Using AWS Identity and Access Management* for more information.

            
          

          - **Created** *(boolean) --* 

            The domain creation status. ``True`` if the creation of an Elasticsearch domain is complete. ``False`` if domain creation is still in progress.

            
          

          - **Deleted** *(boolean) --* 

            The domain deletion status. ``True`` if a delete request has been received for the domain but resource cleanup is still in progress. ``False`` if the domain has not been deleted. Once domain deletion is complete, the status of the domain is no longer returned.

            
          

          - **Endpoint** *(string) --* 

            The Elasticsearch domain endpoint that you use to submit index and search requests.

            
          

          - **Endpoints** *(dict) --* 

            Map containing the Elasticsearch domain endpoints used to submit index and search requests. Example ``key, value`` : ``'vpc','vpc-endpoint-h2dsd34efgyghrtguk5gt6j2foh4.us-east-1.es.amazonaws.com'`` .

            
            

            - *(string) --* 
              

              - *(string) --* 

                The endpoint to which service requests are submitted. For example, ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.es.amazonaws.com`` or ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.es.amazonaws.com`` .

                
        
      
          

          - **Processing** *(boolean) --* 

            The status of the Elasticsearch domain configuration. ``True`` if Amazon Elasticsearch Service is processing configuration changes. ``False`` if the configuration is active.

            
          

          - **ElasticsearchVersion** *(string) --* 
          

          - **ElasticsearchClusterConfig** *(dict) --* 

            The type and number of instances in the domain cluster.

            
            

            - **InstanceType** *(string) --* 

              The instance type for an Elasticsearch cluster.

              
            

            - **InstanceCount** *(integer) --* 

              The number of instances in the specified domain cluster.

              
            

            - **DedicatedMasterEnabled** *(boolean) --* 

              A boolean value to indicate whether a dedicated master node is enabled. See `About Dedicated Master Nodes <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__ for more information.

              
            

            - **ZoneAwarenessEnabled** *(boolean) --* 

              A boolean value to indicate whether zone awareness is enabled. See `About Zone Awareness <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__ for more information.

              
            

            - **DedicatedMasterType** *(string) --* 

              The instance type for a dedicated master node.

              
            

            - **DedicatedMasterCount** *(integer) --* 

              Total number of dedicated master nodes, active and on standby, for the cluster.

              
        
          

          - **EBSOptions** *(dict) --* 

            The ``EBSOptions`` for the specified domain. See `Configuring EBS-based Storage <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs>`__ for more information.

            
            

            - **EBSEnabled** *(boolean) --* 

              Specifies whether EBS-based storage is enabled.

              
            

            - **VolumeType** *(string) --* 

              Specifies the volume type for EBS-based storage.

              
            

            - **VolumeSize** *(integer) --* 

              Integer to specify the size of an EBS volume.

              
            

            - **Iops** *(integer) --* 

              Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).

              
        
          

          - **AccessPolicies** *(string) --* 

            IAM access policy as a JSON-formatted string.

            
          

          - **SnapshotOptions** *(dict) --* 

            Specifies the status of the ``SnapshotOptions`` 

            
            

            - **AutomatedSnapshotStartHour** *(integer) --* 

              Specifies the time, in UTC format, when the service takes a daily automated snapshot of the specified Elasticsearch domain. Default value is ``0`` hours.

              
        
          

          - **VPCOptions** *(dict) --* 

            The ``VPCOptions`` for the specified domain. For more information, see `VPC Endpoints for Amazon Elasticsearch Service Domains <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html>`__ .

            
            

            - **VPCId** *(string) --* 

              The VPC Id for the Elasticsearch domain. Exists only if the domain was created with VPCOptions.

              
            

            - **SubnetIds** *(list) --* 

              Specifies the subnets for VPC endpoint.

              
              

              - *(string) --* 
          
            

            - **AvailabilityZones** *(list) --* 

              The availability zones for the Elasticsearch domain. Exists only if the domain was created with VPCOptions.

              
              

              - *(string) --* 
          
            

            - **SecurityGroupIds** *(list) --* 

              Specifies the security groups for VPC endpoint.

              
              

              - *(string) --* 
          
        
          

          - **EncryptionAtRestOptions** *(dict) --* 

            Specifies the status of the ``EncryptionAtRestOptions`` .

            
            

            - **Enabled** *(boolean) --* 

              Specifies the option to enable Encryption At Rest.

              
            

            - **KmsKeyId** *(string) --* 

              Specifies the KMS Key ID for Encryption At Rest options.

              
        
          

          - **AdvancedOptions** *(dict) --* 

            Specifies the status of the ``AdvancedOptions`` 

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **LogPublishingOptions** *(dict) --* 

            Log publishing options for the given domain.

            
            

            - *(string) --* 

              Type of Log File, it can be one of the following: 

               
              * INDEX_SLOW_LOGS: Index slow logs contains insert requests that took more time than configured index query log threshold to execute.
               
              * SEARCH_SLOW_LOGS: Search slow logs contains search queries that took more time than configured search query log threshold to execute.
               

               

              
              

              - *(dict) --* 

                Log Publishing option that is set for given domain. Attributes and their details: 

                 
                * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be published.
                 
                * Enabled: Whether the log publishing for given log type is enabled or not
                 

                 

                
                

                - **CloudWatchLogsLogGroupArn** *(string) --* 

                  ARN of the Cloudwatch log group to which log needs to be published.

                  
                

                - **Enabled** *(boolean) --* 

                  Specifies whether given log publishing option is enabled or not.

                  
            
        
      
      
    

  .. py:method:: delete_elasticsearch_service_role()

    

    Deletes the service-linked role that Elasticsearch Service uses to manage and maintain VPC domains. Role deletion will fail if any existing VPC domains use the role. You must delete any such Elasticsearch domains before deleting the role. See `Deleting Elasticsearch Service Role <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-enabling-slr>`__ in *VPC Endpoints for Amazon Elasticsearch Service Domains* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/DeleteElasticsearchServiceRole>`_    


    **Request Syntax** 

    ::

      response = client.delete_elasticsearch_service_role()
    :returns: None

  .. py:method:: describe_elasticsearch_domain(**kwargs)

    

    Returns domain configuration information about the specified Elasticsearch domain, including the domain ID, domain endpoint, and domain ARN.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/DescribeElasticsearchDomain>`_    


    **Request Syntax** 
    ::

      response = client.describe_elasticsearch_domain(
          DomainName='string'
      )
    :type DomainName: string
    :param DomainName: **[REQUIRED]** 

      The name of the Elasticsearch domain for which you want information.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DomainStatus': {
                'DomainId': 'string',
                'DomainName': 'string',
                'ARN': 'string',
                'Created': True|False,
                'Deleted': True|False,
                'Endpoint': 'string',
                'Endpoints': {
                    'string': 'string'
                },
                'Processing': True|False,
                'ElasticsearchVersion': 'string',
                'ElasticsearchClusterConfig': {
                    'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                    'InstanceCount': 123,
                    'DedicatedMasterEnabled': True|False,
                    'ZoneAwarenessEnabled': True|False,
                    'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                    'DedicatedMasterCount': 123
                },
                'EBSOptions': {
                    'EBSEnabled': True|False,
                    'VolumeType': 'standard'|'gp2'|'io1',
                    'VolumeSize': 123,
                    'Iops': 123
                },
                'AccessPolicies': 'string',
                'SnapshotOptions': {
                    'AutomatedSnapshotStartHour': 123
                },
                'VPCOptions': {
                    'VPCId': 'string',
                    'SubnetIds': [
                        'string',
                    ],
                    'AvailabilityZones': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ]
                },
                'EncryptionAtRestOptions': {
                    'Enabled': True|False,
                    'KmsKeyId': 'string'
                },
                'AdvancedOptions': {
                    'string': 'string'
                },
                'LogPublishingOptions': {
                    'string': {
                        'CloudWatchLogsLogGroupArn': 'string',
                        'Enabled': True|False
                    }
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        The result of a ``DescribeElasticsearchDomain`` request. Contains the status of the domain specified in the request.

        
        

        - **DomainStatus** *(dict) --* 

          The current status of the Elasticsearch domain.

          
          

          - **DomainId** *(string) --* 

            The unique identifier for the specified Elasticsearch domain.

            
          

          - **DomainName** *(string) --* 

            The name of an Elasticsearch domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).

            
          

          - **ARN** *(string) --* 

            The Amazon resource name (ARN) of an Elasticsearch domain. See `Identifiers for IAM Entities <http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html>`__ in *Using AWS Identity and Access Management* for more information.

            
          

          - **Created** *(boolean) --* 

            The domain creation status. ``True`` if the creation of an Elasticsearch domain is complete. ``False`` if domain creation is still in progress.

            
          

          - **Deleted** *(boolean) --* 

            The domain deletion status. ``True`` if a delete request has been received for the domain but resource cleanup is still in progress. ``False`` if the domain has not been deleted. Once domain deletion is complete, the status of the domain is no longer returned.

            
          

          - **Endpoint** *(string) --* 

            The Elasticsearch domain endpoint that you use to submit index and search requests.

            
          

          - **Endpoints** *(dict) --* 

            Map containing the Elasticsearch domain endpoints used to submit index and search requests. Example ``key, value`` : ``'vpc','vpc-endpoint-h2dsd34efgyghrtguk5gt6j2foh4.us-east-1.es.amazonaws.com'`` .

            
            

            - *(string) --* 
              

              - *(string) --* 

                The endpoint to which service requests are submitted. For example, ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.es.amazonaws.com`` or ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.es.amazonaws.com`` .

                
        
      
          

          - **Processing** *(boolean) --* 

            The status of the Elasticsearch domain configuration. ``True`` if Amazon Elasticsearch Service is processing configuration changes. ``False`` if the configuration is active.

            
          

          - **ElasticsearchVersion** *(string) --* 
          

          - **ElasticsearchClusterConfig** *(dict) --* 

            The type and number of instances in the domain cluster.

            
            

            - **InstanceType** *(string) --* 

              The instance type for an Elasticsearch cluster.

              
            

            - **InstanceCount** *(integer) --* 

              The number of instances in the specified domain cluster.

              
            

            - **DedicatedMasterEnabled** *(boolean) --* 

              A boolean value to indicate whether a dedicated master node is enabled. See `About Dedicated Master Nodes <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__ for more information.

              
            

            - **ZoneAwarenessEnabled** *(boolean) --* 

              A boolean value to indicate whether zone awareness is enabled. See `About Zone Awareness <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__ for more information.

              
            

            - **DedicatedMasterType** *(string) --* 

              The instance type for a dedicated master node.

              
            

            - **DedicatedMasterCount** *(integer) --* 

              Total number of dedicated master nodes, active and on standby, for the cluster.

              
        
          

          - **EBSOptions** *(dict) --* 

            The ``EBSOptions`` for the specified domain. See `Configuring EBS-based Storage <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs>`__ for more information.

            
            

            - **EBSEnabled** *(boolean) --* 

              Specifies whether EBS-based storage is enabled.

              
            

            - **VolumeType** *(string) --* 

              Specifies the volume type for EBS-based storage.

              
            

            - **VolumeSize** *(integer) --* 

              Integer to specify the size of an EBS volume.

              
            

            - **Iops** *(integer) --* 

              Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).

              
        
          

          - **AccessPolicies** *(string) --* 

            IAM access policy as a JSON-formatted string.

            
          

          - **SnapshotOptions** *(dict) --* 

            Specifies the status of the ``SnapshotOptions`` 

            
            

            - **AutomatedSnapshotStartHour** *(integer) --* 

              Specifies the time, in UTC format, when the service takes a daily automated snapshot of the specified Elasticsearch domain. Default value is ``0`` hours.

              
        
          

          - **VPCOptions** *(dict) --* 

            The ``VPCOptions`` for the specified domain. For more information, see `VPC Endpoints for Amazon Elasticsearch Service Domains <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html>`__ .

            
            

            - **VPCId** *(string) --* 

              The VPC Id for the Elasticsearch domain. Exists only if the domain was created with VPCOptions.

              
            

            - **SubnetIds** *(list) --* 

              Specifies the subnets for VPC endpoint.

              
              

              - *(string) --* 
          
            

            - **AvailabilityZones** *(list) --* 

              The availability zones for the Elasticsearch domain. Exists only if the domain was created with VPCOptions.

              
              

              - *(string) --* 
          
            

            - **SecurityGroupIds** *(list) --* 

              Specifies the security groups for VPC endpoint.

              
              

              - *(string) --* 
          
        
          

          - **EncryptionAtRestOptions** *(dict) --* 

            Specifies the status of the ``EncryptionAtRestOptions`` .

            
            

            - **Enabled** *(boolean) --* 

              Specifies the option to enable Encryption At Rest.

              
            

            - **KmsKeyId** *(string) --* 

              Specifies the KMS Key ID for Encryption At Rest options.

              
        
          

          - **AdvancedOptions** *(dict) --* 

            Specifies the status of the ``AdvancedOptions`` 

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **LogPublishingOptions** *(dict) --* 

            Log publishing options for the given domain.

            
            

            - *(string) --* 

              Type of Log File, it can be one of the following: 

               
              * INDEX_SLOW_LOGS: Index slow logs contains insert requests that took more time than configured index query log threshold to execute.
               
              * SEARCH_SLOW_LOGS: Search slow logs contains search queries that took more time than configured search query log threshold to execute.
               

               

              
              

              - *(dict) --* 

                Log Publishing option that is set for given domain. Attributes and their details: 

                 
                * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be published.
                 
                * Enabled: Whether the log publishing for given log type is enabled or not
                 

                 

                
                

                - **CloudWatchLogsLogGroupArn** *(string) --* 

                  ARN of the Cloudwatch log group to which log needs to be published.

                  
                

                - **Enabled** *(boolean) --* 

                  Specifies whether given log publishing option is enabled or not.

                  
            
        
      
      
    

  .. py:method:: describe_elasticsearch_domain_config(**kwargs)

    

    Provides cluster configuration information about the specified Elasticsearch domain, such as the state, creation date, update version, and update date for cluster options.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/DescribeElasticsearchDomainConfig>`_    


    **Request Syntax** 
    ::

      response = client.describe_elasticsearch_domain_config(
          DomainName='string'
      )
    :type DomainName: string
    :param DomainName: **[REQUIRED]** 

      The Elasticsearch domain that you want to get information about.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DomainConfig': {
                'ElasticsearchVersion': {
                    'Options': 'string',
                    'Status': {
                        'CreationDate': datetime(2015, 1, 1),
                        'UpdateDate': datetime(2015, 1, 1),
                        'UpdateVersion': 123,
                        'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                        'PendingDeletion': True|False
                    }
                },
                'ElasticsearchClusterConfig': {
                    'Options': {
                        'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                        'InstanceCount': 123,
                        'DedicatedMasterEnabled': True|False,
                        'ZoneAwarenessEnabled': True|False,
                        'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                        'DedicatedMasterCount': 123
                    },
                    'Status': {
                        'CreationDate': datetime(2015, 1, 1),
                        'UpdateDate': datetime(2015, 1, 1),
                        'UpdateVersion': 123,
                        'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                        'PendingDeletion': True|False
                    }
                },
                'EBSOptions': {
                    'Options': {
                        'EBSEnabled': True|False,
                        'VolumeType': 'standard'|'gp2'|'io1',
                        'VolumeSize': 123,
                        'Iops': 123
                    },
                    'Status': {
                        'CreationDate': datetime(2015, 1, 1),
                        'UpdateDate': datetime(2015, 1, 1),
                        'UpdateVersion': 123,
                        'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                        'PendingDeletion': True|False
                    }
                },
                'AccessPolicies': {
                    'Options': 'string',
                    'Status': {
                        'CreationDate': datetime(2015, 1, 1),
                        'UpdateDate': datetime(2015, 1, 1),
                        'UpdateVersion': 123,
                        'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                        'PendingDeletion': True|False
                    }
                },
                'SnapshotOptions': {
                    'Options': {
                        'AutomatedSnapshotStartHour': 123
                    },
                    'Status': {
                        'CreationDate': datetime(2015, 1, 1),
                        'UpdateDate': datetime(2015, 1, 1),
                        'UpdateVersion': 123,
                        'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                        'PendingDeletion': True|False
                    }
                },
                'VPCOptions': {
                    'Options': {
                        'VPCId': 'string',
                        'SubnetIds': [
                            'string',
                        ],
                        'AvailabilityZones': [
                            'string',
                        ],
                        'SecurityGroupIds': [
                            'string',
                        ]
                    },
                    'Status': {
                        'CreationDate': datetime(2015, 1, 1),
                        'UpdateDate': datetime(2015, 1, 1),
                        'UpdateVersion': 123,
                        'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                        'PendingDeletion': True|False
                    }
                },
                'EncryptionAtRestOptions': {
                    'Options': {
                        'Enabled': True|False,
                        'KmsKeyId': 'string'
                    },
                    'Status': {
                        'CreationDate': datetime(2015, 1, 1),
                        'UpdateDate': datetime(2015, 1, 1),
                        'UpdateVersion': 123,
                        'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                        'PendingDeletion': True|False
                    }
                },
                'AdvancedOptions': {
                    'Options': {
                        'string': 'string'
                    },
                    'Status': {
                        'CreationDate': datetime(2015, 1, 1),
                        'UpdateDate': datetime(2015, 1, 1),
                        'UpdateVersion': 123,
                        'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                        'PendingDeletion': True|False
                    }
                },
                'LogPublishingOptions': {
                    'Options': {
                        'string': {
                            'CloudWatchLogsLogGroupArn': 'string',
                            'Enabled': True|False
                        }
                    },
                    'Status': {
                        'CreationDate': datetime(2015, 1, 1),
                        'UpdateDate': datetime(2015, 1, 1),
                        'UpdateVersion': 123,
                        'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                        'PendingDeletion': True|False
                    }
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        The result of a ``DescribeElasticsearchDomainConfig`` request. Contains the configuration information of the requested domain.

        
        

        - **DomainConfig** *(dict) --* 

          The configuration information of the domain requested in the ``DescribeElasticsearchDomainConfig`` request.

          
          

          - **ElasticsearchVersion** *(dict) --* 

            String of format X.Y to specify version for the Elasticsearch domain.

            
            

            - **Options** *(string) --* 

              Specifies the Elasticsearch version for the specified Elasticsearch domain.

              
            

            - **Status** *(dict) --* 

              Specifies the status of the Elasticsearch version options for the specified Elasticsearch domain.

              
              

              - **CreationDate** *(datetime) --* 

                Timestamp which tells the creation date for the entity.

                
              

              - **UpdateDate** *(datetime) --* 

                Timestamp which tells the last updated time for the entity.

                
              

              - **UpdateVersion** *(integer) --* 

                Specifies the latest version for the entity.

                
              

              - **State** *(string) --* 

                Provides the ``OptionState`` for the Elasticsearch domain.

                
              

              - **PendingDeletion** *(boolean) --* 

                Indicates whether the Elasticsearch domain is being deleted.

                
          
        
          

          - **ElasticsearchClusterConfig** *(dict) --* 

            Specifies the ``ElasticsearchClusterConfig`` for the Elasticsearch domain.

            
            

            - **Options** *(dict) --* 

              Specifies the cluster configuration for the specified Elasticsearch domain.

              
              

              - **InstanceType** *(string) --* 

                The instance type for an Elasticsearch cluster.

                
              

              - **InstanceCount** *(integer) --* 

                The number of instances in the specified domain cluster.

                
              

              - **DedicatedMasterEnabled** *(boolean) --* 

                A boolean value to indicate whether a dedicated master node is enabled. See `About Dedicated Master Nodes <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__ for more information.

                
              

              - **ZoneAwarenessEnabled** *(boolean) --* 

                A boolean value to indicate whether zone awareness is enabled. See `About Zone Awareness <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__ for more information.

                
              

              - **DedicatedMasterType** *(string) --* 

                The instance type for a dedicated master node.

                
              

              - **DedicatedMasterCount** *(integer) --* 

                Total number of dedicated master nodes, active and on standby, for the cluster.

                
          
            

            - **Status** *(dict) --* 

              Specifies the status of the configuration for the specified Elasticsearch domain.

              
              

              - **CreationDate** *(datetime) --* 

                Timestamp which tells the creation date for the entity.

                
              

              - **UpdateDate** *(datetime) --* 

                Timestamp which tells the last updated time for the entity.

                
              

              - **UpdateVersion** *(integer) --* 

                Specifies the latest version for the entity.

                
              

              - **State** *(string) --* 

                Provides the ``OptionState`` for the Elasticsearch domain.

                
              

              - **PendingDeletion** *(boolean) --* 

                Indicates whether the Elasticsearch domain is being deleted.

                
          
        
          

          - **EBSOptions** *(dict) --* 

            Specifies the ``EBSOptions`` for the Elasticsearch domain.

            
            

            - **Options** *(dict) --* 

              Specifies the EBS options for the specified Elasticsearch domain.

              
              

              - **EBSEnabled** *(boolean) --* 

                Specifies whether EBS-based storage is enabled.

                
              

              - **VolumeType** *(string) --* 

                Specifies the volume type for EBS-based storage.

                
              

              - **VolumeSize** *(integer) --* 

                Integer to specify the size of an EBS volume.

                
              

              - **Iops** *(integer) --* 

                Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).

                
          
            

            - **Status** *(dict) --* 

              Specifies the status of the EBS options for the specified Elasticsearch domain.

              
              

              - **CreationDate** *(datetime) --* 

                Timestamp which tells the creation date for the entity.

                
              

              - **UpdateDate** *(datetime) --* 

                Timestamp which tells the last updated time for the entity.

                
              

              - **UpdateVersion** *(integer) --* 

                Specifies the latest version for the entity.

                
              

              - **State** *(string) --* 

                Provides the ``OptionState`` for the Elasticsearch domain.

                
              

              - **PendingDeletion** *(boolean) --* 

                Indicates whether the Elasticsearch domain is being deleted.

                
          
        
          

          - **AccessPolicies** *(dict) --* 

            IAM access policy as a JSON-formatted string.

            
            

            - **Options** *(string) --* 

              The access policy configured for the Elasticsearch domain. Access policies may be resource-based, IP-based, or IAM-based. See `Configuring Access Policies <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-access-policies>`__ for more information.

              
            

            - **Status** *(dict) --* 

              The status of the access policy for the Elasticsearch domain. See ``OptionStatus`` for the status information that's included. 

              
              

              - **CreationDate** *(datetime) --* 

                Timestamp which tells the creation date for the entity.

                
              

              - **UpdateDate** *(datetime) --* 

                Timestamp which tells the last updated time for the entity.

                
              

              - **UpdateVersion** *(integer) --* 

                Specifies the latest version for the entity.

                
              

              - **State** *(string) --* 

                Provides the ``OptionState`` for the Elasticsearch domain.

                
              

              - **PendingDeletion** *(boolean) --* 

                Indicates whether the Elasticsearch domain is being deleted.

                
          
        
          

          - **SnapshotOptions** *(dict) --* 

            Specifies the ``SnapshotOptions`` for the Elasticsearch domain.

            
            

            - **Options** *(dict) --* 

              Specifies the daily snapshot options specified for the Elasticsearch domain.

              
              

              - **AutomatedSnapshotStartHour** *(integer) --* 

                Specifies the time, in UTC format, when the service takes a daily automated snapshot of the specified Elasticsearch domain. Default value is ``0`` hours.

                
          
            

            - **Status** *(dict) --* 

              Specifies the status of a daily automated snapshot.

              
              

              - **CreationDate** *(datetime) --* 

                Timestamp which tells the creation date for the entity.

                
              

              - **UpdateDate** *(datetime) --* 

                Timestamp which tells the last updated time for the entity.

                
              

              - **UpdateVersion** *(integer) --* 

                Specifies the latest version for the entity.

                
              

              - **State** *(string) --* 

                Provides the ``OptionState`` for the Elasticsearch domain.

                
              

              - **PendingDeletion** *(boolean) --* 

                Indicates whether the Elasticsearch domain is being deleted.

                
          
        
          

          - **VPCOptions** *(dict) --* 

            The ``VPCOptions`` for the specified domain. For more information, see `VPC Endpoints for Amazon Elasticsearch Service Domains <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html>`__ .

            
            

            - **Options** *(dict) --* 

              Specifies the VPC options for the specified Elasticsearch domain.

              
              

              - **VPCId** *(string) --* 

                The VPC Id for the Elasticsearch domain. Exists only if the domain was created with VPCOptions.

                
              

              - **SubnetIds** *(list) --* 

                Specifies the subnets for VPC endpoint.

                
                

                - *(string) --* 
            
              

              - **AvailabilityZones** *(list) --* 

                The availability zones for the Elasticsearch domain. Exists only if the domain was created with VPCOptions.

                
                

                - *(string) --* 
            
              

              - **SecurityGroupIds** *(list) --* 

                Specifies the security groups for VPC endpoint.

                
                

                - *(string) --* 
            
          
            

            - **Status** *(dict) --* 

              Specifies the status of the VPC options for the specified Elasticsearch domain.

              
              

              - **CreationDate** *(datetime) --* 

                Timestamp which tells the creation date for the entity.

                
              

              - **UpdateDate** *(datetime) --* 

                Timestamp which tells the last updated time for the entity.

                
              

              - **UpdateVersion** *(integer) --* 

                Specifies the latest version for the entity.

                
              

              - **State** *(string) --* 

                Provides the ``OptionState`` for the Elasticsearch domain.

                
              

              - **PendingDeletion** *(boolean) --* 

                Indicates whether the Elasticsearch domain is being deleted.

                
          
        
          

          - **EncryptionAtRestOptions** *(dict) --* 

            Specifies the ``EncryptionAtRestOptions`` for the Elasticsearch domain.

            
            

            - **Options** *(dict) --* 

              Specifies the Encryption At Rest options for the specified Elasticsearch domain.

              
              

              - **Enabled** *(boolean) --* 

                Specifies the option to enable Encryption At Rest.

                
              

              - **KmsKeyId** *(string) --* 

                Specifies the KMS Key ID for Encryption At Rest options.

                
          
            

            - **Status** *(dict) --* 

              Specifies the status of the Encryption At Rest options for the specified Elasticsearch domain.

              
              

              - **CreationDate** *(datetime) --* 

                Timestamp which tells the creation date for the entity.

                
              

              - **UpdateDate** *(datetime) --* 

                Timestamp which tells the last updated time for the entity.

                
              

              - **UpdateVersion** *(integer) --* 

                Specifies the latest version for the entity.

                
              

              - **State** *(string) --* 

                Provides the ``OptionState`` for the Elasticsearch domain.

                
              

              - **PendingDeletion** *(boolean) --* 

                Indicates whether the Elasticsearch domain is being deleted.

                
          
        
          

          - **AdvancedOptions** *(dict) --* 

            Specifies the ``AdvancedOptions`` for the domain. See `Configuring Advanced Options <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-advanced-options>`__ for more information.

            
            

            - **Options** *(dict) --* 

              Specifies the status of advanced options for the specified Elasticsearch domain.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **Status** *(dict) --* 

              Specifies the status of ``OptionStatus`` for advanced options for the specified Elasticsearch domain.

              
              

              - **CreationDate** *(datetime) --* 

                Timestamp which tells the creation date for the entity.

                
              

              - **UpdateDate** *(datetime) --* 

                Timestamp which tells the last updated time for the entity.

                
              

              - **UpdateVersion** *(integer) --* 

                Specifies the latest version for the entity.

                
              

              - **State** *(string) --* 

                Provides the ``OptionState`` for the Elasticsearch domain.

                
              

              - **PendingDeletion** *(boolean) --* 

                Indicates whether the Elasticsearch domain is being deleted.

                
          
        
          

          - **LogPublishingOptions** *(dict) --* 

            Log publishing options for the given domain.

            
            

            - **Options** *(dict) --* 

              The log publishing options configured for the Elasticsearch domain.

              
              

              - *(string) --* 

                Type of Log File, it can be one of the following: 

                 
                * INDEX_SLOW_LOGS: Index slow logs contains insert requests that took more time than configured index query log threshold to execute.
                 
                * SEARCH_SLOW_LOGS: Search slow logs contains search queries that took more time than configured search query log threshold to execute.
                 

                 

                
                

                - *(dict) --* 

                  Log Publishing option that is set for given domain. Attributes and their details: 

                   
                  * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be published.
                   
                  * Enabled: Whether the log publishing for given log type is enabled or not
                   

                   

                  
                  

                  - **CloudWatchLogsLogGroupArn** *(string) --* 

                    ARN of the Cloudwatch log group to which log needs to be published.

                    
                  

                  - **Enabled** *(boolean) --* 

                    Specifies whether given log publishing option is enabled or not.

                    
              
          
        
            

            - **Status** *(dict) --* 

              The status of the log publishing options for the Elasticsearch domain. See ``OptionStatus`` for the status information that's included. 

              
              

              - **CreationDate** *(datetime) --* 

                Timestamp which tells the creation date for the entity.

                
              

              - **UpdateDate** *(datetime) --* 

                Timestamp which tells the last updated time for the entity.

                
              

              - **UpdateVersion** *(integer) --* 

                Specifies the latest version for the entity.

                
              

              - **State** *(string) --* 

                Provides the ``OptionState`` for the Elasticsearch domain.

                
              

              - **PendingDeletion** *(boolean) --* 

                Indicates whether the Elasticsearch domain is being deleted.

                
          
        
      
    

  .. py:method:: describe_elasticsearch_domains(**kwargs)

    

    Returns domain configuration information about the specified Elasticsearch domains, including the domain ID, domain endpoint, and domain ARN.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/DescribeElasticsearchDomains>`_    


    **Request Syntax** 
    ::

      response = client.describe_elasticsearch_domains(
          DomainNames=[
              'string',
          ]
      )
    :type DomainNames: list
    :param DomainNames: **[REQUIRED]** 

      The Elasticsearch domains for which you want information.

      

    
      - *(string) --* 

        The name of an Elasticsearch domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).

        

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DomainStatusList': [
                {
                    'DomainId': 'string',
                    'DomainName': 'string',
                    'ARN': 'string',
                    'Created': True|False,
                    'Deleted': True|False,
                    'Endpoint': 'string',
                    'Endpoints': {
                        'string': 'string'
                    },
                    'Processing': True|False,
                    'ElasticsearchVersion': 'string',
                    'ElasticsearchClusterConfig': {
                        'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                        'InstanceCount': 123,
                        'DedicatedMasterEnabled': True|False,
                        'ZoneAwarenessEnabled': True|False,
                        'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                        'DedicatedMasterCount': 123
                    },
                    'EBSOptions': {
                        'EBSEnabled': True|False,
                        'VolumeType': 'standard'|'gp2'|'io1',
                        'VolumeSize': 123,
                        'Iops': 123
                    },
                    'AccessPolicies': 'string',
                    'SnapshotOptions': {
                        'AutomatedSnapshotStartHour': 123
                    },
                    'VPCOptions': {
                        'VPCId': 'string',
                        'SubnetIds': [
                            'string',
                        ],
                        'AvailabilityZones': [
                            'string',
                        ],
                        'SecurityGroupIds': [
                            'string',
                        ]
                    },
                    'EncryptionAtRestOptions': {
                        'Enabled': True|False,
                        'KmsKeyId': 'string'
                    },
                    'AdvancedOptions': {
                        'string': 'string'
                    },
                    'LogPublishingOptions': {
                        'string': {
                            'CloudWatchLogsLogGroupArn': 'string',
                            'Enabled': True|False
                        }
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        The result of a ``DescribeElasticsearchDomains`` request. Contains the status of the specified domains or all domains owned by the account.

        
        

        - **DomainStatusList** *(list) --* 

          The status of the domains requested in the ``DescribeElasticsearchDomains`` request.

          
          

          - *(dict) --* 

            The current status of an Elasticsearch domain.

            
            

            - **DomainId** *(string) --* 

              The unique identifier for the specified Elasticsearch domain.

              
            

            - **DomainName** *(string) --* 

              The name of an Elasticsearch domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).

              
            

            - **ARN** *(string) --* 

              The Amazon resource name (ARN) of an Elasticsearch domain. See `Identifiers for IAM Entities <http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html>`__ in *Using AWS Identity and Access Management* for more information.

              
            

            - **Created** *(boolean) --* 

              The domain creation status. ``True`` if the creation of an Elasticsearch domain is complete. ``False`` if domain creation is still in progress.

              
            

            - **Deleted** *(boolean) --* 

              The domain deletion status. ``True`` if a delete request has been received for the domain but resource cleanup is still in progress. ``False`` if the domain has not been deleted. Once domain deletion is complete, the status of the domain is no longer returned.

              
            

            - **Endpoint** *(string) --* 

              The Elasticsearch domain endpoint that you use to submit index and search requests.

              
            

            - **Endpoints** *(dict) --* 

              Map containing the Elasticsearch domain endpoints used to submit index and search requests. Example ``key, value`` : ``'vpc','vpc-endpoint-h2dsd34efgyghrtguk5gt6j2foh4.us-east-1.es.amazonaws.com'`` .

              
              

              - *(string) --* 
                

                - *(string) --* 

                  The endpoint to which service requests are submitted. For example, ``search-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.es.amazonaws.com`` or ``doc-imdb-movies-oopcnjfn6ugofer3zx5iadxxca.eu-west-1.es.amazonaws.com`` .

                  
          
        
            

            - **Processing** *(boolean) --* 

              The status of the Elasticsearch domain configuration. ``True`` if Amazon Elasticsearch Service is processing configuration changes. ``False`` if the configuration is active.

              
            

            - **ElasticsearchVersion** *(string) --* 
            

            - **ElasticsearchClusterConfig** *(dict) --* 

              The type and number of instances in the domain cluster.

              
              

              - **InstanceType** *(string) --* 

                The instance type for an Elasticsearch cluster.

                
              

              - **InstanceCount** *(integer) --* 

                The number of instances in the specified domain cluster.

                
              

              - **DedicatedMasterEnabled** *(boolean) --* 

                A boolean value to indicate whether a dedicated master node is enabled. See `About Dedicated Master Nodes <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__ for more information.

                
              

              - **ZoneAwarenessEnabled** *(boolean) --* 

                A boolean value to indicate whether zone awareness is enabled. See `About Zone Awareness <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__ for more information.

                
              

              - **DedicatedMasterType** *(string) --* 

                The instance type for a dedicated master node.

                
              

              - **DedicatedMasterCount** *(integer) --* 

                Total number of dedicated master nodes, active and on standby, for the cluster.

                
          
            

            - **EBSOptions** *(dict) --* 

              The ``EBSOptions`` for the specified domain. See `Configuring EBS-based Storage <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs>`__ for more information.

              
              

              - **EBSEnabled** *(boolean) --* 

                Specifies whether EBS-based storage is enabled.

                
              

              - **VolumeType** *(string) --* 

                Specifies the volume type for EBS-based storage.

                
              

              - **VolumeSize** *(integer) --* 

                Integer to specify the size of an EBS volume.

                
              

              - **Iops** *(integer) --* 

                Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).

                
          
            

            - **AccessPolicies** *(string) --* 

              IAM access policy as a JSON-formatted string.

              
            

            - **SnapshotOptions** *(dict) --* 

              Specifies the status of the ``SnapshotOptions`` 

              
              

              - **AutomatedSnapshotStartHour** *(integer) --* 

                Specifies the time, in UTC format, when the service takes a daily automated snapshot of the specified Elasticsearch domain. Default value is ``0`` hours.

                
          
            

            - **VPCOptions** *(dict) --* 

              The ``VPCOptions`` for the specified domain. For more information, see `VPC Endpoints for Amazon Elasticsearch Service Domains <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html>`__ .

              
              

              - **VPCId** *(string) --* 

                The VPC Id for the Elasticsearch domain. Exists only if the domain was created with VPCOptions.

                
              

              - **SubnetIds** *(list) --* 

                Specifies the subnets for VPC endpoint.

                
                

                - *(string) --* 
            
              

              - **AvailabilityZones** *(list) --* 

                The availability zones for the Elasticsearch domain. Exists only if the domain was created with VPCOptions.

                
                

                - *(string) --* 
            
              

              - **SecurityGroupIds** *(list) --* 

                Specifies the security groups for VPC endpoint.

                
                

                - *(string) --* 
            
          
            

            - **EncryptionAtRestOptions** *(dict) --* 

              Specifies the status of the ``EncryptionAtRestOptions`` .

              
              

              - **Enabled** *(boolean) --* 

                Specifies the option to enable Encryption At Rest.

                
              

              - **KmsKeyId** *(string) --* 

                Specifies the KMS Key ID for Encryption At Rest options.

                
          
            

            - **AdvancedOptions** *(dict) --* 

              Specifies the status of the ``AdvancedOptions`` 

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **LogPublishingOptions** *(dict) --* 

              Log publishing options for the given domain.

              
              

              - *(string) --* 

                Type of Log File, it can be one of the following: 

                 
                * INDEX_SLOW_LOGS: Index slow logs contains insert requests that took more time than configured index query log threshold to execute.
                 
                * SEARCH_SLOW_LOGS: Search slow logs contains search queries that took more time than configured search query log threshold to execute.
                 

                 

                
                

                - *(dict) --* 

                  Log Publishing option that is set for given domain. Attributes and their details: 

                   
                  * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be published.
                   
                  * Enabled: Whether the log publishing for given log type is enabled or not
                   

                   

                  
                  

                  - **CloudWatchLogsLogGroupArn** *(string) --* 

                    ARN of the Cloudwatch log group to which log needs to be published.

                    
                  

                  - **Enabled** *(boolean) --* 

                    Specifies whether given log publishing option is enabled or not.

                    
              
          
        
        
      
    

  .. py:method:: describe_elasticsearch_instance_type_limits(**kwargs)

    

    Describe Elasticsearch Limits for a given InstanceType and ElasticsearchVersion. When modifying existing Domain, specify the ``  DomainName `` to know what Limits are supported for modifying. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/DescribeElasticsearchInstanceTypeLimits>`_    


    **Request Syntax** 
    ::

      response = client.describe_elasticsearch_instance_type_limits(
          DomainName='string',
          InstanceType='m3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
          ElasticsearchVersion='string'
      )
    :type DomainName: string
    :param DomainName: 

      DomainName represents the name of the Domain that we are trying to modify. This should be present only if we are querying for Elasticsearch ``  Limits `` for existing domain. 

      

    
    :type InstanceType: string
    :param InstanceType: **[REQUIRED]** 

      The instance type for an Elasticsearch cluster for which Elasticsearch ``  Limits `` are needed. 

      

    
    :type ElasticsearchVersion: string
    :param ElasticsearchVersion: **[REQUIRED]** 

      Version of Elasticsearch for which ``  Limits `` are needed. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'LimitsByRole': {
                'string': {
                    'StorageTypes': [
                        {
                            'StorageTypeName': 'string',
                            'StorageSubTypeName': 'string',
                            'StorageTypeLimits': [
                                {
                                    'LimitName': 'string',
                                    'LimitValues': [
                                        'string',
                                    ]
                                },
                            ]
                        },
                    ],
                    'InstanceLimits': {
                        'InstanceCountLimits': {
                            'MinimumInstanceCount': 123,
                            'MaximumInstanceCount': 123
                        }
                    },
                    'AdditionalLimits': [
                        {
                            'LimitName': 'string',
                            'LimitValues': [
                                'string',
                            ]
                        },
                    ]
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Container for the parameters received from ``  DescribeElasticsearchInstanceTypeLimits `` operation. 

        
        

        - **LimitsByRole** *(dict) --* 

          Map of Role of the Instance and Limits that are applicable. Role performed by given Instance in Elasticsearch can be one of the following: 

           
          * Data: If the given InstanceType is used as Data node
           
          * Master: If the given InstanceType is used as Master node
           

           

          
          

          - *(string) --* 
            

            - *(dict) --* 

              Limits for given InstanceType and for each of it's role. Limits contains following ``  StorageTypes, ``  ``  InstanceLimits `` and ``  AdditionalLimits ``  

              
              

              - **StorageTypes** *(list) --* 

                StorageType represents the list of storage related types and attributes that are available for given InstanceType. 

                
                

                - *(dict) --* 

                  StorageTypes represents the list of storage related types and their attributes that are available for given InstanceType. 

                  
                  

                  - **StorageTypeName** *(string) --* 

                    Type of the storage. List of available storage options: 

                     
                    * instance
                    Inbuilt storage available for the given Instance 
                    * ebs
                    Elastic block storage that would be attached to the given Instance 

                     

                    
                  

                  - **StorageSubTypeName** *(string) --* 

                    SubType of the given storage type. List of available sub-storage options: For "instance" storageType we wont have any storageSubType, in case of "ebs" storageType we will have following valid storageSubTypes 

                     
                    * standard
                     
                    * gp2
                     
                    * io1
                     

                    Refer `` VolumeType`` for more information regarding above EBS storage options. 

                    
                  

                  - **StorageTypeLimits** *(list) --* 

                    List of limits that are applicable for given storage type. 

                    
                    

                    - *(dict) --* 

                      Limits that are applicable for given storage type. 

                      
                      

                      - **LimitName** *(string) --* 

                        Name of storage limits that are applicable for given storage type. If ``  StorageType `` is ebs, following storage options are applicable 

                         
                        * MinimumVolumeSize
                        Minimum amount of volume size that is applicable for given storage type.It can be empty if it is not applicable. 
                        * MaximumVolumeSize
                        Maximum amount of volume size that is applicable for given storage type.It can be empty if it is not applicable. 
                        * MaximumIops
                        Maximum amount of Iops that is applicable for given storage type.It can be empty if it is not applicable. 
                        * MinimumIops
                        Minimum amount of Iops that is applicable for given storage type.It can be empty if it is not applicable. 

                         

                        
                      

                      - **LimitValues** *(list) --* 

                        Values for the ``  StorageTypeLimit$LimitName `` . 

                        
                        

                        - *(string) --* 
                    
                  
                
              
            
              

              - **InstanceLimits** *(dict) --* 

                InstanceLimits represents the list of instance related attributes that are available for given InstanceType. 

                
                

                - **InstanceCountLimits** *(dict) --* 

                  InstanceCountLimits represents the limits on number of instances that be created in Amazon Elasticsearch for given InstanceType. 

                  
                  

                  - **MinimumInstanceCount** *(integer) --* 

                    Minimum number of Instances that can be instantiated for given InstanceType. 

                    
                  

                  - **MaximumInstanceCount** *(integer) --* 

                    Maximum number of Instances that can be instantiated for given InstanceType. 

                    
              
            
              

              - **AdditionalLimits** *(list) --* 

                List of additional limits that are specific to a given InstanceType and for each of it's ``  InstanceRole `` . 

                
                

                - *(dict) --* 

                  List of limits that are specific to a given InstanceType and for each of it's ``  InstanceRole `` . 

                  
                  

                  - **LimitName** *(string) --* 

                    Name of Additional Limit is specific to a given InstanceType and for each of it's ``  InstanceRole `` etc. Attributes and their details:  

                     
                    * MaximumNumberOfDataNodesSupported
                    This attribute will be present in Master node only to specify how much data nodes upto which given ``  ESPartitionInstanceType `` can support as master node. 
                    * MaximumNumberOfDataNodesWithoutMasterNode
                    This attribute will be present in Data node only to specify how much data nodes of given ``  ESPartitionInstanceType `` upto which you don't need any master nodes to govern them. 

                     

                    
                  

                  - **LimitValues** *(list) --* 

                    Value for given ``  AdditionalLimit$LimitName `` . 

                    
                    

                    - *(string) --* 
                
              
            
          
      
    
    

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

        


  .. py:method:: list_domain_names()

    

    Returns the name of all Elasticsearch domains owned by the current user's account. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/ListDomainNames>`_    


    **Request Syntax** 

    ::

      response = client.list_domain_names()
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DomainNames': [
                {
                    'DomainName': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        The result of a ``ListDomainNames`` operation. Contains the names of all Elasticsearch domains owned by this account.

        
        

        - **DomainNames** *(list) --* 

          List of Elasticsearch domain names.

          
          

          - *(dict) --* 
            

            - **DomainName** *(string) --* 

              Specifies the ``DomainName`` .

              
        
      
    

  .. py:method:: list_elasticsearch_instance_types(**kwargs)

    

    List all Elasticsearch instance types that are supported for given ElasticsearchVersion

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/ListElasticsearchInstanceTypes>`_    


    **Request Syntax** 
    ::

      response = client.list_elasticsearch_instance_types(
          ElasticsearchVersion='string',
          DomainName='string',
          MaxResults=123,
          NextToken='string'
      )
    :type ElasticsearchVersion: string
    :param ElasticsearchVersion: **[REQUIRED]** 

      Version of Elasticsearch for which list of supported elasticsearch instance types are needed. 

      

    
    :type DomainName: string
    :param DomainName: 

      DomainName represents the name of the Domain that we are trying to modify. This should be present only if we are querying for list of available Elasticsearch instance types when modifying existing domain. 

      

    
    :type MaxResults: integer
    :param MaxResults: 

      Set this value to limit the number of results returned. Value provided must be greater than 30 else it wont be honored. 

      

    
    :type NextToken: string
    :param NextToken: 

      NextToken should be sent in case if earlier API call produced result containing NextToken. It is used for pagination. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ElasticsearchInstanceTypes': [
                'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Container for the parameters returned by ``  ListElasticsearchInstanceTypes `` operation. 

        
        

        - **ElasticsearchInstanceTypes** *(list) --* 

          List of instance types supported by Amazon Elasticsearch service for given ``  ElasticsearchVersion ``  

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          In case if there are more results available NextToken would be present, make further request to the same API with received NextToken to paginate remaining results. 

          
    

  .. py:method:: list_elasticsearch_versions(**kwargs)

    

    List all supported Elasticsearch versions

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/ListElasticsearchVersions>`_    


    **Request Syntax** 
    ::

      response = client.list_elasticsearch_versions(
          MaxResults=123,
          NextToken='string'
      )
    :type MaxResults: integer
    :param MaxResults: 

      Set this value to limit the number of results returned. Value provided must be greater than 10 else it wont be honored. 

      

    
    :type NextToken: string
    :param NextToken: 

      Paginated APIs accepts NextToken input to returns next page results and provides a NextToken output in the response which can be used by the client to retrieve more results. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ElasticsearchVersions': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Container for the parameters for response received from ``  ListElasticsearchVersions `` operation. 

        
        

        - **ElasticsearchVersions** *(list) --* 

          List of supported elastic search versions. 

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          Paginated APIs accepts NextToken input to returns next page results and provides a NextToken output in the response which can be used by the client to retrieve more results. 

          
    

  .. py:method:: list_tags(**kwargs)

    

    Returns all tags for the given Elasticsearch domain.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/ListTags>`_    


    **Request Syntax** 
    ::

      response = client.list_tags(
          ARN='string'
      )
    :type ARN: string
    :param ARN: **[REQUIRED]** 

      Specify the ``ARN`` for the Elasticsearch domain to which the tags are attached that you want to view.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TagList': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        The result of a ``ListTags`` operation. Contains tags for all requested Elasticsearch domains.

        
        

        - **TagList** *(list) --* 

          List of ``Tag`` for the requested Elasticsearch domain.

          
          

          - *(dict) --* 

            Specifies a key value pair for a resource tag.

            
            

            - **Key** *(string) --* 

              Specifies the ``TagKey`` , the name of the tag. Tag keys must be unique for the Elasticsearch domain to which they are attached.

              
            

            - **Value** *(string) --* 

              Specifies the ``TagValue`` , the value assigned to the corresponding tag key. Tag values can be null and do not have to be unique in a tag set. For example, you can have a key value pair in a tag set of ``project : Trinity`` and ``cost-center : Trinity`` 

              
        
      
    

  .. py:method:: remove_tags(**kwargs)

    

    Removes the specified set of tags from the specified Elasticsearch domain.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/RemoveTags>`_    


    **Request Syntax** 
    ::

      response = client.remove_tags(
          ARN='string',
          TagKeys=[
              'string',
          ]
      )
    :type ARN: string
    :param ARN: **[REQUIRED]** 

      Specifies the ``ARN`` for the Elasticsearch domain from which you want to delete the specified tags.

      

    
    :type TagKeys: list
    :param TagKeys: **[REQUIRED]** 

      Specifies the ``TagKey`` list which you want to remove from the Elasticsearch domain.

      

    
      - *(string) --* 

      
  
    
    :returns: None

  .. py:method:: update_elasticsearch_domain_config(**kwargs)

    

    Modifies the cluster configuration of the specified Elasticsearch domain, setting as setting the instance type and the number of instances. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/UpdateElasticsearchDomainConfig>`_    


    **Request Syntax** 
    ::

      response = client.update_elasticsearch_domain_config(
          DomainName='string',
          ElasticsearchClusterConfig={
              'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
              'InstanceCount': 123,
              'DedicatedMasterEnabled': True|False,
              'ZoneAwarenessEnabled': True|False,
              'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
              'DedicatedMasterCount': 123
          },
          EBSOptions={
              'EBSEnabled': True|False,
              'VolumeType': 'standard'|'gp2'|'io1',
              'VolumeSize': 123,
              'Iops': 123
          },
          SnapshotOptions={
              'AutomatedSnapshotStartHour': 123
          },
          VPCOptions={
              'SubnetIds': [
                  'string',
              ],
              'SecurityGroupIds': [
                  'string',
              ]
          },
          AdvancedOptions={
              'string': 'string'
          },
          AccessPolicies='string',
          LogPublishingOptions={
              'string': {
                  'CloudWatchLogsLogGroupArn': 'string',
                  'Enabled': True|False
              }
          }
      )
    :type DomainName: string
    :param DomainName: **[REQUIRED]** 

      The name of the Elasticsearch domain that you are updating. 

      

    
    :type ElasticsearchClusterConfig: dict
    :param ElasticsearchClusterConfig: 

      The type and number of instances to instantiate for the domain cluster.

      

    
      - **InstanceType** *(string) --* 

        The instance type for an Elasticsearch cluster.

        

      
      - **InstanceCount** *(integer) --* 

        The number of instances in the specified domain cluster.

        

      
      - **DedicatedMasterEnabled** *(boolean) --* 

        A boolean value to indicate whether a dedicated master node is enabled. See `About Dedicated Master Nodes <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__ for more information.

        

      
      - **ZoneAwarenessEnabled** *(boolean) --* 

        A boolean value to indicate whether zone awareness is enabled. See `About Zone Awareness <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__ for more information.

        

      
      - **DedicatedMasterType** *(string) --* 

        The instance type for a dedicated master node.

        

      
      - **DedicatedMasterCount** *(integer) --* 

        Total number of dedicated master nodes, active and on standby, for the cluster.

        

      
    
    :type EBSOptions: dict
    :param EBSOptions: 

      Specify the type and size of the EBS volume that you want to use. 

      

    
      - **EBSEnabled** *(boolean) --* 

        Specifies whether EBS-based storage is enabled.

        

      
      - **VolumeType** *(string) --* 

        Specifies the volume type for EBS-based storage.

        

      
      - **VolumeSize** *(integer) --* 

        Integer to specify the size of an EBS volume.

        

      
      - **Iops** *(integer) --* 

        Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).

        

      
    
    :type SnapshotOptions: dict
    :param SnapshotOptions: 

      Option to set the time, in UTC format, for the daily automated snapshot. Default value is ``0`` hours. 

      

    
      - **AutomatedSnapshotStartHour** *(integer) --* 

        Specifies the time, in UTC format, when the service takes a daily automated snapshot of the specified Elasticsearch domain. Default value is ``0`` hours.

        

      
    
    :type VPCOptions: dict
    :param VPCOptions: 

      Options to specify the subnets and security groups for VPC endpoint. For more information, see `Creating a VPC <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-creating-vpc>`__ in *VPC Endpoints for Amazon Elasticsearch Service Domains* 

      

    
      - **SubnetIds** *(list) --* 

        Specifies the subnets for VPC endpoint.

        

      
        - *(string) --* 

        
    
      - **SecurityGroupIds** *(list) --* 

        Specifies the security groups for VPC endpoint.

        

      
        - *(string) --* 

        
    
    
    :type AdvancedOptions: dict
    :param AdvancedOptions: 

      Modifies the advanced option to allow references to indices in an HTTP request body. Must be ``false`` when configuring access to individual sub-resources. By default, the value is ``true`` . See `Configuration Advanced Options <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-advanced-options>`__ for more information.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type AccessPolicies: string
    :param AccessPolicies: 

      IAM access policy as a JSON-formatted string.

      

    
    :type LogPublishingOptions: dict
    :param LogPublishingOptions: 

      Map of ``LogType`` and ``LogPublishingOption`` , each containing options to publish a given type of Elasticsearch log.

      

    
      - *(string) --* 

        Type of Log File, it can be one of the following: 

         
        * INDEX_SLOW_LOGS: Index slow logs contains insert requests that took more time than configured index query log threshold to execute.
         
        * SEARCH_SLOW_LOGS: Search slow logs contains search queries that took more time than configured search query log threshold to execute.
         

         

        

      
        - *(dict) --* 

          Log Publishing option that is set for given domain. Attributes and their details: 

           
          * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be published.
           
          * Enabled: Whether the log publishing for given log type is enabled or not
           

           

          

        
          - **CloudWatchLogsLogGroupArn** *(string) --* 

            ARN of the Cloudwatch log group to which log needs to be published.

            

          
          - **Enabled** *(boolean) --* 

            Specifies whether given log publishing option is enabled or not.

            

          
        
  

    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DomainConfig': {
                'ElasticsearchVersion': {
                    'Options': 'string',
                    'Status': {
                        'CreationDate': datetime(2015, 1, 1),
                        'UpdateDate': datetime(2015, 1, 1),
                        'UpdateVersion': 123,
                        'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                        'PendingDeletion': True|False
                    }
                },
                'ElasticsearchClusterConfig': {
                    'Options': {
                        'InstanceType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                        'InstanceCount': 123,
                        'DedicatedMasterEnabled': True|False,
                        'ZoneAwarenessEnabled': True|False,
                        'DedicatedMasterType': 'm3.medium.elasticsearch'|'m3.large.elasticsearch'|'m3.xlarge.elasticsearch'|'m3.2xlarge.elasticsearch'|'m4.large.elasticsearch'|'m4.xlarge.elasticsearch'|'m4.2xlarge.elasticsearch'|'m4.4xlarge.elasticsearch'|'m4.10xlarge.elasticsearch'|'t2.micro.elasticsearch'|'t2.small.elasticsearch'|'t2.medium.elasticsearch'|'r3.large.elasticsearch'|'r3.xlarge.elasticsearch'|'r3.2xlarge.elasticsearch'|'r3.4xlarge.elasticsearch'|'r3.8xlarge.elasticsearch'|'i2.xlarge.elasticsearch'|'i2.2xlarge.elasticsearch'|'d2.xlarge.elasticsearch'|'d2.2xlarge.elasticsearch'|'d2.4xlarge.elasticsearch'|'d2.8xlarge.elasticsearch'|'c4.large.elasticsearch'|'c4.xlarge.elasticsearch'|'c4.2xlarge.elasticsearch'|'c4.4xlarge.elasticsearch'|'c4.8xlarge.elasticsearch'|'r4.large.elasticsearch'|'r4.xlarge.elasticsearch'|'r4.2xlarge.elasticsearch'|'r4.4xlarge.elasticsearch'|'r4.8xlarge.elasticsearch'|'r4.16xlarge.elasticsearch'|'i3.large.elasticsearch'|'i3.xlarge.elasticsearch'|'i3.2xlarge.elasticsearch'|'i3.4xlarge.elasticsearch'|'i3.8xlarge.elasticsearch'|'i3.16xlarge.elasticsearch',
                        'DedicatedMasterCount': 123
                    },
                    'Status': {
                        'CreationDate': datetime(2015, 1, 1),
                        'UpdateDate': datetime(2015, 1, 1),
                        'UpdateVersion': 123,
                        'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                        'PendingDeletion': True|False
                    }
                },
                'EBSOptions': {
                    'Options': {
                        'EBSEnabled': True|False,
                        'VolumeType': 'standard'|'gp2'|'io1',
                        'VolumeSize': 123,
                        'Iops': 123
                    },
                    'Status': {
                        'CreationDate': datetime(2015, 1, 1),
                        'UpdateDate': datetime(2015, 1, 1),
                        'UpdateVersion': 123,
                        'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                        'PendingDeletion': True|False
                    }
                },
                'AccessPolicies': {
                    'Options': 'string',
                    'Status': {
                        'CreationDate': datetime(2015, 1, 1),
                        'UpdateDate': datetime(2015, 1, 1),
                        'UpdateVersion': 123,
                        'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                        'PendingDeletion': True|False
                    }
                },
                'SnapshotOptions': {
                    'Options': {
                        'AutomatedSnapshotStartHour': 123
                    },
                    'Status': {
                        'CreationDate': datetime(2015, 1, 1),
                        'UpdateDate': datetime(2015, 1, 1),
                        'UpdateVersion': 123,
                        'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                        'PendingDeletion': True|False
                    }
                },
                'VPCOptions': {
                    'Options': {
                        'VPCId': 'string',
                        'SubnetIds': [
                            'string',
                        ],
                        'AvailabilityZones': [
                            'string',
                        ],
                        'SecurityGroupIds': [
                            'string',
                        ]
                    },
                    'Status': {
                        'CreationDate': datetime(2015, 1, 1),
                        'UpdateDate': datetime(2015, 1, 1),
                        'UpdateVersion': 123,
                        'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                        'PendingDeletion': True|False
                    }
                },
                'EncryptionAtRestOptions': {
                    'Options': {
                        'Enabled': True|False,
                        'KmsKeyId': 'string'
                    },
                    'Status': {
                        'CreationDate': datetime(2015, 1, 1),
                        'UpdateDate': datetime(2015, 1, 1),
                        'UpdateVersion': 123,
                        'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                        'PendingDeletion': True|False
                    }
                },
                'AdvancedOptions': {
                    'Options': {
                        'string': 'string'
                    },
                    'Status': {
                        'CreationDate': datetime(2015, 1, 1),
                        'UpdateDate': datetime(2015, 1, 1),
                        'UpdateVersion': 123,
                        'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                        'PendingDeletion': True|False
                    }
                },
                'LogPublishingOptions': {
                    'Options': {
                        'string': {
                            'CloudWatchLogsLogGroupArn': 'string',
                            'Enabled': True|False
                        }
                    },
                    'Status': {
                        'CreationDate': datetime(2015, 1, 1),
                        'UpdateDate': datetime(2015, 1, 1),
                        'UpdateVersion': 123,
                        'State': 'RequiresIndexDocuments'|'Processing'|'Active',
                        'PendingDeletion': True|False
                    }
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        The result of an ``UpdateElasticsearchDomain`` request. Contains the status of the Elasticsearch domain being updated.

        
        

        - **DomainConfig** *(dict) --* 

          The status of the updated Elasticsearch domain. 

          
          

          - **ElasticsearchVersion** *(dict) --* 

            String of format X.Y to specify version for the Elasticsearch domain.

            
            

            - **Options** *(string) --* 

              Specifies the Elasticsearch version for the specified Elasticsearch domain.

              
            

            - **Status** *(dict) --* 

              Specifies the status of the Elasticsearch version options for the specified Elasticsearch domain.

              
              

              - **CreationDate** *(datetime) --* 

                Timestamp which tells the creation date for the entity.

                
              

              - **UpdateDate** *(datetime) --* 

                Timestamp which tells the last updated time for the entity.

                
              

              - **UpdateVersion** *(integer) --* 

                Specifies the latest version for the entity.

                
              

              - **State** *(string) --* 

                Provides the ``OptionState`` for the Elasticsearch domain.

                
              

              - **PendingDeletion** *(boolean) --* 

                Indicates whether the Elasticsearch domain is being deleted.

                
          
        
          

          - **ElasticsearchClusterConfig** *(dict) --* 

            Specifies the ``ElasticsearchClusterConfig`` for the Elasticsearch domain.

            
            

            - **Options** *(dict) --* 

              Specifies the cluster configuration for the specified Elasticsearch domain.

              
              

              - **InstanceType** *(string) --* 

                The instance type for an Elasticsearch cluster.

                
              

              - **InstanceCount** *(integer) --* 

                The number of instances in the specified domain cluster.

                
              

              - **DedicatedMasterEnabled** *(boolean) --* 

                A boolean value to indicate whether a dedicated master node is enabled. See `About Dedicated Master Nodes <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-dedicatedmasternodes>`__ for more information.

                
              

              - **ZoneAwarenessEnabled** *(boolean) --* 

                A boolean value to indicate whether zone awareness is enabled. See `About Zone Awareness <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-managedomains.html#es-managedomains-zoneawareness>`__ for more information.

                
              

              - **DedicatedMasterType** *(string) --* 

                The instance type for a dedicated master node.

                
              

              - **DedicatedMasterCount** *(integer) --* 

                Total number of dedicated master nodes, active and on standby, for the cluster.

                
          
            

            - **Status** *(dict) --* 

              Specifies the status of the configuration for the specified Elasticsearch domain.

              
              

              - **CreationDate** *(datetime) --* 

                Timestamp which tells the creation date for the entity.

                
              

              - **UpdateDate** *(datetime) --* 

                Timestamp which tells the last updated time for the entity.

                
              

              - **UpdateVersion** *(integer) --* 

                Specifies the latest version for the entity.

                
              

              - **State** *(string) --* 

                Provides the ``OptionState`` for the Elasticsearch domain.

                
              

              - **PendingDeletion** *(boolean) --* 

                Indicates whether the Elasticsearch domain is being deleted.

                
          
        
          

          - **EBSOptions** *(dict) --* 

            Specifies the ``EBSOptions`` for the Elasticsearch domain.

            
            

            - **Options** *(dict) --* 

              Specifies the EBS options for the specified Elasticsearch domain.

              
              

              - **EBSEnabled** *(boolean) --* 

                Specifies whether EBS-based storage is enabled.

                
              

              - **VolumeType** *(string) --* 

                Specifies the volume type for EBS-based storage.

                
              

              - **VolumeSize** *(integer) --* 

                Integer to specify the size of an EBS volume.

                
              

              - **Iops** *(integer) --* 

                Specifies the IOPD for a Provisioned IOPS EBS volume (SSD).

                
          
            

            - **Status** *(dict) --* 

              Specifies the status of the EBS options for the specified Elasticsearch domain.

              
              

              - **CreationDate** *(datetime) --* 

                Timestamp which tells the creation date for the entity.

                
              

              - **UpdateDate** *(datetime) --* 

                Timestamp which tells the last updated time for the entity.

                
              

              - **UpdateVersion** *(integer) --* 

                Specifies the latest version for the entity.

                
              

              - **State** *(string) --* 

                Provides the ``OptionState`` for the Elasticsearch domain.

                
              

              - **PendingDeletion** *(boolean) --* 

                Indicates whether the Elasticsearch domain is being deleted.

                
          
        
          

          - **AccessPolicies** *(dict) --* 

            IAM access policy as a JSON-formatted string.

            
            

            - **Options** *(string) --* 

              The access policy configured for the Elasticsearch domain. Access policies may be resource-based, IP-based, or IAM-based. See `Configuring Access Policies <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-access-policies>`__ for more information.

              
            

            - **Status** *(dict) --* 

              The status of the access policy for the Elasticsearch domain. See ``OptionStatus`` for the status information that's included. 

              
              

              - **CreationDate** *(datetime) --* 

                Timestamp which tells the creation date for the entity.

                
              

              - **UpdateDate** *(datetime) --* 

                Timestamp which tells the last updated time for the entity.

                
              

              - **UpdateVersion** *(integer) --* 

                Specifies the latest version for the entity.

                
              

              - **State** *(string) --* 

                Provides the ``OptionState`` for the Elasticsearch domain.

                
              

              - **PendingDeletion** *(boolean) --* 

                Indicates whether the Elasticsearch domain is being deleted.

                
          
        
          

          - **SnapshotOptions** *(dict) --* 

            Specifies the ``SnapshotOptions`` for the Elasticsearch domain.

            
            

            - **Options** *(dict) --* 

              Specifies the daily snapshot options specified for the Elasticsearch domain.

              
              

              - **AutomatedSnapshotStartHour** *(integer) --* 

                Specifies the time, in UTC format, when the service takes a daily automated snapshot of the specified Elasticsearch domain. Default value is ``0`` hours.

                
          
            

            - **Status** *(dict) --* 

              Specifies the status of a daily automated snapshot.

              
              

              - **CreationDate** *(datetime) --* 

                Timestamp which tells the creation date for the entity.

                
              

              - **UpdateDate** *(datetime) --* 

                Timestamp which tells the last updated time for the entity.

                
              

              - **UpdateVersion** *(integer) --* 

                Specifies the latest version for the entity.

                
              

              - **State** *(string) --* 

                Provides the ``OptionState`` for the Elasticsearch domain.

                
              

              - **PendingDeletion** *(boolean) --* 

                Indicates whether the Elasticsearch domain is being deleted.

                
          
        
          

          - **VPCOptions** *(dict) --* 

            The ``VPCOptions`` for the specified domain. For more information, see `VPC Endpoints for Amazon Elasticsearch Service Domains <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html>`__ .

            
            

            - **Options** *(dict) --* 

              Specifies the VPC options for the specified Elasticsearch domain.

              
              

              - **VPCId** *(string) --* 

                The VPC Id for the Elasticsearch domain. Exists only if the domain was created with VPCOptions.

                
              

              - **SubnetIds** *(list) --* 

                Specifies the subnets for VPC endpoint.

                
                

                - *(string) --* 
            
              

              - **AvailabilityZones** *(list) --* 

                The availability zones for the Elasticsearch domain. Exists only if the domain was created with VPCOptions.

                
                

                - *(string) --* 
            
              

              - **SecurityGroupIds** *(list) --* 

                Specifies the security groups for VPC endpoint.

                
                

                - *(string) --* 
            
          
            

            - **Status** *(dict) --* 

              Specifies the status of the VPC options for the specified Elasticsearch domain.

              
              

              - **CreationDate** *(datetime) --* 

                Timestamp which tells the creation date for the entity.

                
              

              - **UpdateDate** *(datetime) --* 

                Timestamp which tells the last updated time for the entity.

                
              

              - **UpdateVersion** *(integer) --* 

                Specifies the latest version for the entity.

                
              

              - **State** *(string) --* 

                Provides the ``OptionState`` for the Elasticsearch domain.

                
              

              - **PendingDeletion** *(boolean) --* 

                Indicates whether the Elasticsearch domain is being deleted.

                
          
        
          

          - **EncryptionAtRestOptions** *(dict) --* 

            Specifies the ``EncryptionAtRestOptions`` for the Elasticsearch domain.

            
            

            - **Options** *(dict) --* 

              Specifies the Encryption At Rest options for the specified Elasticsearch domain.

              
              

              - **Enabled** *(boolean) --* 

                Specifies the option to enable Encryption At Rest.

                
              

              - **KmsKeyId** *(string) --* 

                Specifies the KMS Key ID for Encryption At Rest options.

                
          
            

            - **Status** *(dict) --* 

              Specifies the status of the Encryption At Rest options for the specified Elasticsearch domain.

              
              

              - **CreationDate** *(datetime) --* 

                Timestamp which tells the creation date for the entity.

                
              

              - **UpdateDate** *(datetime) --* 

                Timestamp which tells the last updated time for the entity.

                
              

              - **UpdateVersion** *(integer) --* 

                Specifies the latest version for the entity.

                
              

              - **State** *(string) --* 

                Provides the ``OptionState`` for the Elasticsearch domain.

                
              

              - **PendingDeletion** *(boolean) --* 

                Indicates whether the Elasticsearch domain is being deleted.

                
          
        
          

          - **AdvancedOptions** *(dict) --* 

            Specifies the ``AdvancedOptions`` for the domain. See `Configuring Advanced Options <http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-advanced-options>`__ for more information.

            
            

            - **Options** *(dict) --* 

              Specifies the status of advanced options for the specified Elasticsearch domain.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **Status** *(dict) --* 

              Specifies the status of ``OptionStatus`` for advanced options for the specified Elasticsearch domain.

              
              

              - **CreationDate** *(datetime) --* 

                Timestamp which tells the creation date for the entity.

                
              

              - **UpdateDate** *(datetime) --* 

                Timestamp which tells the last updated time for the entity.

                
              

              - **UpdateVersion** *(integer) --* 

                Specifies the latest version for the entity.

                
              

              - **State** *(string) --* 

                Provides the ``OptionState`` for the Elasticsearch domain.

                
              

              - **PendingDeletion** *(boolean) --* 

                Indicates whether the Elasticsearch domain is being deleted.

                
          
        
          

          - **LogPublishingOptions** *(dict) --* 

            Log publishing options for the given domain.

            
            

            - **Options** *(dict) --* 

              The log publishing options configured for the Elasticsearch domain.

              
              

              - *(string) --* 

                Type of Log File, it can be one of the following: 

                 
                * INDEX_SLOW_LOGS: Index slow logs contains insert requests that took more time than configured index query log threshold to execute.
                 
                * SEARCH_SLOW_LOGS: Search slow logs contains search queries that took more time than configured search query log threshold to execute.
                 

                 

                
                

                - *(dict) --* 

                  Log Publishing option that is set for given domain. Attributes and their details: 

                   
                  * CloudWatchLogsLogGroupArn: ARN of the Cloudwatch log group to which log needs to be published.
                   
                  * Enabled: Whether the log publishing for given log type is enabled or not
                   

                   

                  
                  

                  - **CloudWatchLogsLogGroupArn** *(string) --* 

                    ARN of the Cloudwatch log group to which log needs to be published.

                    
                  

                  - **Enabled** *(boolean) --* 

                    Specifies whether given log publishing option is enabled or not.

                    
              
          
        
            

            - **Status** *(dict) --* 

              The status of the log publishing options for the Elasticsearch domain. See ``OptionStatus`` for the status information that's included. 

              
              

              - **CreationDate** *(datetime) --* 

                Timestamp which tells the creation date for the entity.

                
              

              - **UpdateDate** *(datetime) --* 

                Timestamp which tells the last updated time for the entity.

                
              

              - **UpdateVersion** *(integer) --* 

                Specifies the latest version for the entity.

                
              

              - **State** *(string) --* 

                Provides the ``OptionState`` for the Elasticsearch domain.

                
              

              - **PendingDeletion** *(boolean) --* 

                Indicates whether the Elasticsearch domain is being deleted.

                
          
        
      
    

==========
Paginators
==========


The available paginators are:
