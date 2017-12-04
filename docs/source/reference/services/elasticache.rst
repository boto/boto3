

***********
ElastiCache
***********

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: ElastiCache.Client

  A low-level client representing Amazon ElastiCache::

    
    import boto3
    
    client = boto3.client('elasticache')

  
  These are the available methods:
  
  *   :py:meth:`~ElastiCache.Client.add_tags_to_resource`

  
  *   :py:meth:`~ElastiCache.Client.authorize_cache_security_group_ingress`

  
  *   :py:meth:`~ElastiCache.Client.can_paginate`

  
  *   :py:meth:`~ElastiCache.Client.copy_snapshot`

  
  *   :py:meth:`~ElastiCache.Client.create_cache_cluster`

  
  *   :py:meth:`~ElastiCache.Client.create_cache_parameter_group`

  
  *   :py:meth:`~ElastiCache.Client.create_cache_security_group`

  
  *   :py:meth:`~ElastiCache.Client.create_cache_subnet_group`

  
  *   :py:meth:`~ElastiCache.Client.create_replication_group`

  
  *   :py:meth:`~ElastiCache.Client.create_snapshot`

  
  *   :py:meth:`~ElastiCache.Client.delete_cache_cluster`

  
  *   :py:meth:`~ElastiCache.Client.delete_cache_parameter_group`

  
  *   :py:meth:`~ElastiCache.Client.delete_cache_security_group`

  
  *   :py:meth:`~ElastiCache.Client.delete_cache_subnet_group`

  
  *   :py:meth:`~ElastiCache.Client.delete_replication_group`

  
  *   :py:meth:`~ElastiCache.Client.delete_snapshot`

  
  *   :py:meth:`~ElastiCache.Client.describe_cache_clusters`

  
  *   :py:meth:`~ElastiCache.Client.describe_cache_engine_versions`

  
  *   :py:meth:`~ElastiCache.Client.describe_cache_parameter_groups`

  
  *   :py:meth:`~ElastiCache.Client.describe_cache_parameters`

  
  *   :py:meth:`~ElastiCache.Client.describe_cache_security_groups`

  
  *   :py:meth:`~ElastiCache.Client.describe_cache_subnet_groups`

  
  *   :py:meth:`~ElastiCache.Client.describe_engine_default_parameters`

  
  *   :py:meth:`~ElastiCache.Client.describe_events`

  
  *   :py:meth:`~ElastiCache.Client.describe_replication_groups`

  
  *   :py:meth:`~ElastiCache.Client.describe_reserved_cache_nodes`

  
  *   :py:meth:`~ElastiCache.Client.describe_reserved_cache_nodes_offerings`

  
  *   :py:meth:`~ElastiCache.Client.describe_snapshots`

  
  *   :py:meth:`~ElastiCache.Client.generate_presigned_url`

  
  *   :py:meth:`~ElastiCache.Client.get_paginator`

  
  *   :py:meth:`~ElastiCache.Client.get_waiter`

  
  *   :py:meth:`~ElastiCache.Client.list_allowed_node_type_modifications`

  
  *   :py:meth:`~ElastiCache.Client.list_tags_for_resource`

  
  *   :py:meth:`~ElastiCache.Client.modify_cache_cluster`

  
  *   :py:meth:`~ElastiCache.Client.modify_cache_parameter_group`

  
  *   :py:meth:`~ElastiCache.Client.modify_cache_subnet_group`

  
  *   :py:meth:`~ElastiCache.Client.modify_replication_group`

  
  *   :py:meth:`~ElastiCache.Client.modify_replication_group_shard_configuration`

  
  *   :py:meth:`~ElastiCache.Client.purchase_reserved_cache_nodes_offering`

  
  *   :py:meth:`~ElastiCache.Client.reboot_cache_cluster`

  
  *   :py:meth:`~ElastiCache.Client.remove_tags_from_resource`

  
  *   :py:meth:`~ElastiCache.Client.reset_cache_parameter_group`

  
  *   :py:meth:`~ElastiCache.Client.revoke_cache_security_group_ingress`

  
  *   :py:meth:`~ElastiCache.Client.test_failover`

  

  .. py:method:: add_tags_to_resource(**kwargs)

    

    Adds up to 50 cost allocation tags to the named resource. A cost allocation tag is a key-value pair where the key and value are case-sensitive. You can use cost allocation tags to categorize and track your AWS costs.

     

    When you apply tags to your ElastiCache resources, AWS generates a cost allocation report as a comma-separated value (CSV) file with your usage and costs aggregated by your tags. You can apply tags that represent business categories (such as cost centers, application names, or owners) to organize your costs across multiple services. For more information, see `Using Cost Allocation Tags in Amazon ElastiCache <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Tagging.html>`__ in the *ElastiCache User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/AddTagsToResource>`_    


    **Request Syntax** 
    ::

      response = client.add_tags_to_resource(
          ResourceName='string',
          Tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type ResourceName: string
    :param ResourceName: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the resource to which the tags are to be added, for example ``arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster`` or ``arn:aws:elasticache:us-west-2:0123456789:snapshot:mySnapshot`` . ElastiCache resources are *cluster* and *snapshot* .

       

      For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      

    
    :type Tags: list
    :param Tags: **[REQUIRED]** 

      A list of cost allocation tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value.

      

    
      - *(dict) --* 

        A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. A tag with a null Value is permitted.

        

      
        - **Key** *(string) --* 

          The key for the tag. May not be null.

          

        
        - **Value** *(string) --* 

          The tag's value. May be null.

          

        
      
  
    
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

        Represents the output from the ``AddTagsToResource`` , ``ListTagsForResource`` , and ``RemoveTagsFromResource`` operations.

        
        

        - **TagList** *(list) --* 

          A list of cost allocation tags as key-value pairs.

          
          

          - *(dict) --* 

            A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. A tag with a null Value is permitted.

            
            

            - **Key** *(string) --* 

              The key for the tag. May not be null.

              
            

            - **Value** *(string) --* 

              The tag's value. May be null.

              
        
      
    

  .. py:method:: authorize_cache_security_group_ingress(**kwargs)

    

    Allows network ingress to a cache security group. Applications using ElastiCache must be running on Amazon EC2, and Amazon EC2 security groups are used as the authorization mechanism.

     

    .. note::

       

      You cannot authorize ingress from an Amazon EC2 security group in one region to an ElastiCache cluster in another region.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/AuthorizeCacheSecurityGroupIngress>`_    


    **Request Syntax** 
    ::

      response = client.authorize_cache_security_group_ingress(
          CacheSecurityGroupName='string',
          EC2SecurityGroupName='string',
          EC2SecurityGroupOwnerId='string'
      )
    :type CacheSecurityGroupName: string
    :param CacheSecurityGroupName: **[REQUIRED]** 

      The cache security group that allows network ingress.

      

    
    :type EC2SecurityGroupName: string
    :param EC2SecurityGroupName: **[REQUIRED]** 

      The Amazon EC2 security group to be authorized for ingress to the cache security group.

      

    
    :type EC2SecurityGroupOwnerId: string
    :param EC2SecurityGroupOwnerId: **[REQUIRED]** 

      The AWS account number of the Amazon EC2 security group owner. Note that this is not the same thing as an AWS access key ID - you must provide a valid AWS account number for this parameter.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CacheSecurityGroup': {
                'OwnerId': 'string',
                'CacheSecurityGroupName': 'string',
                'Description': 'string',
                'EC2SecurityGroups': [
                    {
                        'Status': 'string',
                        'EC2SecurityGroupName': 'string',
                        'EC2SecurityGroupOwnerId': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CacheSecurityGroup** *(dict) --* 

          Represents the output of one of the following operations:

           

           
          * ``AuthorizeCacheSecurityGroupIngress``   
           
          * ``CreateCacheSecurityGroup``   
           
          * ``RevokeCacheSecurityGroupIngress``   
           

          
          

          - **OwnerId** *(string) --* 

            The AWS account ID of the cache security group owner.

            
          

          - **CacheSecurityGroupName** *(string) --* 

            The name of the cache security group.

            
          

          - **Description** *(string) --* 

            The description of the cache security group.

            
          

          - **EC2SecurityGroups** *(list) --* 

            A list of Amazon EC2 security groups that are associated with this cache security group.

            
            

            - *(dict) --* 

              Provides ownership and status information for an Amazon EC2 security group.

              
              

              - **Status** *(string) --* 

                The status of the Amazon EC2 security group.

                
              

              - **EC2SecurityGroupName** *(string) --* 

                The name of the Amazon EC2 security group.

                
              

              - **EC2SecurityGroupOwnerId** *(string) --* 

                The AWS account ID of the Amazon EC2 security group owner.

                
          
        
      
    

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


  .. py:method:: copy_snapshot(**kwargs)

    

    Makes a copy of an existing snapshot.

     

    .. note::

       

      This operation is valid for Redis only.

       

     

    .. warning::

       

      Users or groups that have permissions to use the ``CopySnapshot`` operation can create their own Amazon S3 buckets and copy snapshots to it. To control access to your snapshots, use an IAM policy to control who has the ability to use the ``CopySnapshot`` operation. For more information about using IAM to control the use of ElastiCache operations, see `Exporting Snapshots <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Snapshots.Exporting.html>`__ and `Authentication & Access Control <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/IAM.html>`__ .

       

     

    You could receive the following error messages.

     

     **Error Messages**  

     

     
    * **Error Message:** The S3 bucket %s is outside of the region.  **Solution:** Create an Amazon S3 bucket in the same region as your snapshot. For more information, see `Step 1\: Create an Amazon S3 Bucket <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Snapshots.Exporting.html#Snapshots.Exporting.CreateBucket>`__ in the ElastiCache User Guide. 
     
    * **Error Message:** The S3 bucket %s does not exist.  **Solution:** Create an Amazon S3 bucket in the same region as your snapshot. For more information, see `Step 1\: Create an Amazon S3 Bucket <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Snapshots.Exporting.html#Snapshots.Exporting.CreateBucket>`__ in the ElastiCache User Guide. 
     
    * **Error Message:** The S3 bucket %s is not owned by the authenticated user.  **Solution:** Create an Amazon S3 bucket in the same region as your snapshot. For more information, see `Step 1\: Create an Amazon S3 Bucket <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Snapshots.Exporting.html#Snapshots.Exporting.CreateBucket>`__ in the ElastiCache User Guide. 
     
    * **Error Message:** The authenticated user does not have sufficient permissions to perform the desired activity.  **Solution:** Contact your system administrator to get the needed permissions. 
     
    * **Error Message:** The S3 bucket %s already contains an object with key %s.  **Solution:** Give the ``TargetSnapshotName`` a new and unique value. If exporting a snapshot, you could alternatively create a new Amazon S3 bucket and use this same value for ``TargetSnapshotName`` . 
     
    * **Error Message:** ElastiCache has not been granted READ permissions %s on the S3 Bucket.  **Solution:** Add List and Read permissions on the bucket. For more information, see `Step 2\: Grant ElastiCache Access to Your Amazon S3 Bucket <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Snapshots.Exporting.html#Snapshots.Exporting.GrantAccess>`__ in the ElastiCache User Guide. 
     
    * **Error Message:** ElastiCache has not been granted WRITE permissions %s on the S3 Bucket.  **Solution:** Add Upload/Delete permissions on the bucket. For more information, see `Step 2\: Grant ElastiCache Access to Your Amazon S3 Bucket <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Snapshots.Exporting.html#Snapshots.Exporting.GrantAccess>`__ in the ElastiCache User Guide. 
     
    * **Error Message:** ElastiCache has not been granted READ_ACP permissions %s on the S3 Bucket.  **Solution:** Add View Permissions on the bucket. For more information, see `Step 2\: Grant ElastiCache Access to Your Amazon S3 Bucket <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Snapshots.Exporting.html#Snapshots.Exporting.GrantAccess>`__ in the ElastiCache User Guide. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/CopySnapshot>`_    


    **Request Syntax** 
    ::

      response = client.copy_snapshot(
          SourceSnapshotName='string',
          TargetSnapshotName='string',
          TargetBucket='string'
      )
    :type SourceSnapshotName: string
    :param SourceSnapshotName: **[REQUIRED]** 

      The name of an existing snapshot from which to make a copy.

      

    
    :type TargetSnapshotName: string
    :param TargetSnapshotName: **[REQUIRED]** 

      A name for the snapshot copy. ElastiCache does not permit overwriting a snapshot, therefore this name must be unique within its context - ElastiCache or an Amazon S3 bucket if exporting.

      

    
    :type TargetBucket: string
    :param TargetBucket: 

      The Amazon S3 bucket to which the snapshot is exported. This parameter is used only when exporting a snapshot for external access.

       

      When using this parameter to export a snapshot, be sure Amazon ElastiCache has the needed permissions to this S3 bucket. For more information, see `Step 2\: Grant ElastiCache Access to Your Amazon S3 Bucket <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Snapshots.Exporting.html#Snapshots.Exporting.GrantAccess>`__ in the *Amazon ElastiCache User Guide* .

       

      For more information, see `Exporting a Snapshot <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Snapshots.Exporting.html>`__ in the *Amazon ElastiCache User Guide* .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Snapshot': {
                'SnapshotName': 'string',
                'ReplicationGroupId': 'string',
                'ReplicationGroupDescription': 'string',
                'CacheClusterId': 'string',
                'SnapshotStatus': 'string',
                'SnapshotSource': 'string',
                'CacheNodeType': 'string',
                'Engine': 'string',
                'EngineVersion': 'string',
                'NumCacheNodes': 123,
                'PreferredAvailabilityZone': 'string',
                'CacheClusterCreateTime': datetime(2015, 1, 1),
                'PreferredMaintenanceWindow': 'string',
                'TopicArn': 'string',
                'Port': 123,
                'CacheParameterGroupName': 'string',
                'CacheSubnetGroupName': 'string',
                'VpcId': 'string',
                'AutoMinorVersionUpgrade': True|False,
                'SnapshotRetentionLimit': 123,
                'SnapshotWindow': 'string',
                'NumNodeGroups': 123,
                'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                'NodeSnapshots': [
                    {
                        'CacheClusterId': 'string',
                        'NodeGroupId': 'string',
                        'CacheNodeId': 'string',
                        'NodeGroupConfiguration': {
                            'Slots': 'string',
                            'ReplicaCount': 123,
                            'PrimaryAvailabilityZone': 'string',
                            'ReplicaAvailabilityZones': [
                                'string',
                            ]
                        },
                        'CacheSize': 'string',
                        'CacheNodeCreateTime': datetime(2015, 1, 1),
                        'SnapshotCreateTime': datetime(2015, 1, 1)
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Snapshot** *(dict) --* 

          Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.

          
          

          - **SnapshotName** *(string) --* 

            The name of a snapshot. For an automatic snapshot, the name is system-generated. For a manual snapshot, this is the user-provided name.

            
          

          - **ReplicationGroupId** *(string) --* 

            The unique identifier of the source replication group.

            
          

          - **ReplicationGroupDescription** *(string) --* 

            A description of the source replication group.

            
          

          - **CacheClusterId** *(string) --* 

            The user-supplied identifier of the source cluster.

            
          

          - **SnapshotStatus** *(string) --* 

            The status of the snapshot. Valid values: ``creating`` | ``available`` | ``restoring`` | ``copying`` | ``deleting`` .

            
          

          - **SnapshotSource** *(string) --* 

            Indicates whether the snapshot is from an automatic backup (``automated`` ) or was created manually (``manual`` ).

            
          

          - **CacheNodeType** *(string) --* 

            The name of the compute and memory capacity node type for the source cluster.

             

            The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

             

             
            * General purpose: 

               
              * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
               
              * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
               

             
             
            * Compute optimized: 

               
              * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
               

             
             
            * Memory optimized: 

               
              * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
               
              * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
               

             
             

             

             **Notes:**  

             

             
            * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
             
            * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
             
            * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
             
            * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
             

             

            For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

            
          

          - **Engine** *(string) --* 

            The name of the cache engine (``memcached`` or ``redis`` ) used by the source cluster.

            
          

          - **EngineVersion** *(string) --* 

            The version of the cache engine version that is used by the source cluster.

            
          

          - **NumCacheNodes** *(integer) --* 

            The number of cache nodes in the source cluster.

             

            For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

            
          

          - **PreferredAvailabilityZone** *(string) --* 

            The name of the Availability Zone in which the source cluster is located.

            
          

          - **CacheClusterCreateTime** *(datetime) --* 

            The date and time when the source cluster was created.

            
          

          - **PreferredMaintenanceWindow** *(string) --* 

            Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.

             

            Valid values for ``ddd`` are:

             

             
            * ``sun``   
             
            * ``mon``   
             
            * ``tue``   
             
            * ``wed``   
             
            * ``thu``   
             
            * ``fri``   
             
            * ``sat``   
             

             

            Example: ``sun:23:00-mon:01:30``  

            
          

          - **TopicArn** *(string) --* 

            The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing notifications.

            
          

          - **Port** *(integer) --* 

            The port number used by each cache nodes in the source cluster.

            
          

          - **CacheParameterGroupName** *(string) --* 

            The cache parameter group that is associated with the source cluster.

            
          

          - **CacheSubnetGroupName** *(string) --* 

            The name of the cache subnet group associated with the source cluster.

            
          

          - **VpcId** *(string) --* 

            The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the source cluster.

            
          

          - **AutoMinorVersionUpgrade** *(boolean) --* 

            This parameter is currently disabled.

            
          

          - **SnapshotRetentionLimit** *(integer) --* 

            For an automatic snapshot, the number of days for which ElastiCache retains the snapshot before deleting it.

             

            For manual snapshots, this field reflects the ``SnapshotRetentionLimit`` for the source cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots do not expire, and can only be deleted using the ``DeleteSnapshot`` operation. 

             

             **Important** If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

            
          

          - **SnapshotWindow** *(string) --* 

            The daily time range during which ElastiCache takes daily snapshots of the source cluster.

            
          

          - **NumNodeGroups** *(integer) --* 

            The number of node groups (shards) in this snapshot. When restoring from a snapshot, the number of node groups (shards) in the snapshot and in the restored replication group must be the same.

            
          

          - **AutomaticFailover** *(string) --* 

            Indicates the status of Multi-AZ with automatic failover for the source Redis replication group.

             

            Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

             

             
            * Redis versions earlier than 2.8.6. 
             
            * Redis (cluster mode disabled): T1 and T2 cache node types. 
             
            * Redis (cluster mode enabled): T1 node types. 
             

            
          

          - **NodeSnapshots** *(list) --* 

            A list of the cache nodes in the source cluster.

            
            

            - *(dict) --* 

              Represents an individual cache node in a snapshot of a cluster.

              
              

              - **CacheClusterId** *(string) --* 

                A unique identifier for the source cluster.

                
              

              - **NodeGroupId** *(string) --* 

                A unique identifier for the source node group (shard).

                
              

              - **CacheNodeId** *(string) --* 

                The cache node identifier for the node in the source cluster.

                
              

              - **NodeGroupConfiguration** *(dict) --* 

                The configuration for the source node group (shard).

                
                

                - **Slots** *(string) --* 

                  A string that specifies the keyspace for a particular node group. Keyspaces range from 0 to 16,383. The string is in the format ``startkey-endkey`` .

                   

                  Example: ``"0-3999"``  

                  
                

                - **ReplicaCount** *(integer) --* 

                  The number of read replica nodes in this node group (shard).

                  
                

                - **PrimaryAvailabilityZone** *(string) --* 

                  The Availability Zone where the primary node of this node group (shard) is launched.

                  
                

                - **ReplicaAvailabilityZones** *(list) --* 

                  A list of Availability Zones to be used for the read replicas. The number of Availability Zones in this list must match the value of ``ReplicaCount`` or ``ReplicasPerNodeGroup`` if not specified.

                  
                  

                  - *(string) --* 
              
            
              

              - **CacheSize** *(string) --* 

                The size of the cache on the source cache node.

                
              

              - **CacheNodeCreateTime** *(datetime) --* 

                The date and time when the cache node was created in the source cluster.

                
              

              - **SnapshotCreateTime** *(datetime) --* 

                The date and time when the source node's metadata and cache data set was obtained for the snapshot.

                
          
        
      
    

  .. py:method:: create_cache_cluster(**kwargs)

    

    Creates a cluster. All nodes in the cluster run the same protocol-compliant cache engine software, either Memcached or Redis.

     

    .. warning::

       

      Due to current limitations on Redis (cluster mode disabled), this operation or parameter is not supported on Redis (cluster mode enabled) replication groups.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/CreateCacheCluster>`_    


    **Request Syntax** 
    ::

      response = client.create_cache_cluster(
          CacheClusterId='string',
          ReplicationGroupId='string',
          AZMode='single-az'|'cross-az',
          PreferredAvailabilityZone='string',
          PreferredAvailabilityZones=[
              'string',
          ],
          NumCacheNodes=123,
          CacheNodeType='string',
          Engine='string',
          EngineVersion='string',
          CacheParameterGroupName='string',
          CacheSubnetGroupName='string',
          CacheSecurityGroupNames=[
              'string',
          ],
          SecurityGroupIds=[
              'string',
          ],
          Tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ],
          SnapshotArns=[
              'string',
          ],
          SnapshotName='string',
          PreferredMaintenanceWindow='string',
          Port=123,
          NotificationTopicArn='string',
          AutoMinorVersionUpgrade=True|False,
          SnapshotRetentionLimit=123,
          SnapshotWindow='string',
          AuthToken='string'
      )
    :type CacheClusterId: string
    :param CacheClusterId: **[REQUIRED]** 

      The node group (shard) identifier. This parameter is stored as a lowercase string.

       

       **Constraints:**  

       

       
      * A name must contain from 1 to 20 alphanumeric characters or hyphens. 
       
      * The first character must be a letter. 
       
      * A name cannot end with a hyphen or contain two consecutive hyphens. 
       

      

    
    :type ReplicationGroupId: string
    :param ReplicationGroupId: 

      .. warning::

         

        Due to current limitations on Redis (cluster mode disabled), this operation or parameter is not supported on Redis (cluster mode enabled) replication groups.

         

       

      The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.

       

      If the specified replication group is Multi-AZ enabled and the Availability Zone is not specified, the cluster is created in Availability Zones that provide the best spread of read replicas across Availability Zones.

       

      .. note::

         

        This parameter is only valid if the ``Engine`` parameter is ``redis`` .

         

      

    
    :type AZMode: string
    :param AZMode: 

      Specifies whether the nodes in this Memcached cluster are created in a single Availability Zone or created across multiple Availability Zones in the cluster's region.

       

      This parameter is only supported for Memcached clusters.

       

      If the ``AZMode`` and ``PreferredAvailabilityZones`` are not specified, ElastiCache assumes ``single-az`` mode.

      

    
    :type PreferredAvailabilityZone: string
    :param PreferredAvailabilityZone: 

      The EC2 Availability Zone in which the cluster is created.

       

      All nodes belonging to this Memcached cluster are placed in the preferred Availability Zone. If you want to create your nodes across multiple Availability Zones, use ``PreferredAvailabilityZones`` .

       

      Default: System chosen Availability Zone.

      

    
    :type PreferredAvailabilityZones: list
    :param PreferredAvailabilityZones: 

      A list of the Availability Zones in which cache nodes are created. The order of the zones in the list is not important.

       

      This option is only supported on Memcached.

       

      .. note::

         

        If you are creating your cluster in an Amazon VPC (recommended) you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group.

         

        The number of Availability Zones listed must equal the value of ``NumCacheNodes`` .

         

       

      If you want all the nodes in the same Availability Zone, use ``PreferredAvailabilityZone`` instead, or repeat the Availability Zone multiple times in the list.

       

      Default: System chosen Availability Zones.

      

    
      - *(string) --* 

      
  
    :type NumCacheNodes: integer
    :param NumCacheNodes: 

      The initial number of cache nodes that the cluster has.

       

      For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

       

      If you need more than 20 nodes for your Memcached cluster, please fill out the ElastiCache Limit Increase Request form at `http\://aws.amazon.com/contact-us/elasticache-node-limit-request/ <http://aws.amazon.com/contact-us/elasticache-node-limit-request/>`__ .

      

    
    :type CacheNodeType: string
    :param CacheNodeType: 

      The compute and memory capacity of the nodes in the node group (shard).

       

      The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

       

       
      * General purpose: 

         
        * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
         
        * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
         

       
       
      * Compute optimized: 

         
        * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
         

       
       
      * Memory optimized: 

         
        * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
         
        * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
         

       
       

       

       **Notes:**  

       

       
      * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
       
      * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
       
      * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
       
      * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
       

       

      For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

      

    
    :type Engine: string
    :param Engine: 

      The name of the cache engine to be used for this cluster.

       

      Valid values for this parameter are: ``memcached`` | ``redis``  

      

    
    :type EngineVersion: string
    :param EngineVersion: 

      The version number of the cache engine to be used for this cluster. To view the supported cache engine versions, use the DescribeCacheEngineVersions operation.

       

       **Important:** You can upgrade to a newer engine version (see `Selecting a Cache Engine and Version <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/SelectEngine.html#VersionManagement>`__ ), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster or replication group and create it anew with the earlier engine version. 

      

    
    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: 

      The name of the parameter group to associate with this cluster. If this argument is omitted, the default parameter group for the specified engine is used. You cannot use any parameter group which has ``cluster-enabled='yes'`` when creating a cluster.

      

    
    :type CacheSubnetGroupName: string
    :param CacheSubnetGroupName: 

      The name of the subnet group to be used for the cluster.

       

      Use this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud (Amazon VPC).

       

      .. warning::

         

        If you're going to launch your cluster in an Amazon VPC, you need to create a subnet group before you start creating a cluster. For more information, see `Subnets and Subnet Groups <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/SubnetGroups.html>`__ .

         

      

    
    :type CacheSecurityGroupNames: list
    :param CacheSecurityGroupNames: 

      A list of security group names to associate with this cluster.

       

      Use this parameter only when you are creating a cluster outside of an Amazon Virtual Private Cloud (Amazon VPC).

      

    
      - *(string) --* 

      
  
    :type SecurityGroupIds: list
    :param SecurityGroupIds: 

      One or more VPC security groups associated with the cluster.

       

      Use this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud (Amazon VPC).

      

    
      - *(string) --* 

      
  
    :type Tags: list
    :param Tags: 

      A list of cost allocation tags to be added to this resource.

      

    
      - *(dict) --* 

        A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. A tag with a null Value is permitted.

        

      
        - **Key** *(string) --* 

          The key for the tag. May not be null.

          

        
        - **Value** *(string) --* 

          The tag's value. May be null.

          

        
      
  
    :type SnapshotArns: list
    :param SnapshotArns: 

      A single-element string list containing an Amazon Resource Name (ARN) that uniquely identifies a Redis RDB snapshot file stored in Amazon S3. The snapshot file is used to populate the node group (shard). The Amazon S3 object name in the ARN cannot contain any commas.

       

      .. note::

         

        This parameter is only valid if the ``Engine`` parameter is ``redis`` .

         

       

      Example of an Amazon S3 ARN: ``arn:aws:s3:::my_bucket/snapshot1.rdb``  

      

    
      - *(string) --* 

      
  
    :type SnapshotName: string
    :param SnapshotName: 

      The name of a Redis snapshot from which to restore data into the new node group (shard). The snapshot status changes to ``restoring`` while the new node group (shard) is being created.

       

      .. note::

         

        This parameter is only valid if the ``Engine`` parameter is ``redis`` .

         

      

    
    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: 

      Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period. Valid values for ``ddd`` are:

       

      Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.

       

      Valid values for ``ddd`` are:

       

       
      * ``sun``   
       
      * ``mon``   
       
      * ``tue``   
       
      * ``wed``   
       
      * ``thu``   
       
      * ``fri``   
       
      * ``sat``   
       

       

      Example: ``sun:23:00-mon:01:30``  

      

    
    :type Port: integer
    :param Port: 

      The port number on which each of the cache nodes accepts connections.

      

    
    :type NotificationTopicArn: string
    :param NotificationTopicArn: 

      The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.

       

      .. note::

         

        The Amazon SNS topic owner must be the same as the cluster owner.

         

      

    
    :type AutoMinorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: 

      This parameter is currently disabled.

      

    
    :type SnapshotRetentionLimit: integer
    :param SnapshotRetentionLimit: 

      The number of days for which ElastiCache retains automatic snapshots before deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot taken today is retained for 5 days before being deleted.

       

      .. note::

         

        This parameter is only valid if the ``Engine`` parameter is ``redis`` .

         

       

      Default: 0 (i.e., automatic backups are disabled for this cluster).

      

    
    :type SnapshotWindow: string
    :param SnapshotWindow: 

      The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).

       

      Example: ``05:00-09:00``  

       

      If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

       

      .. note::

         

        This parameter is only valid if the ``Engine`` parameter is ``redis`` .

         

      

    
    :type AuthToken: string
    :param AuthToken: 

       **Reserved parameter.** The password used to access a password protected server.

       

      This parameter is valid only if:

       

       
      * The parameter ``TransitEncryptionEnabled`` was set to ``true`` when the cluster was created. 
       
      * The line ``requirepass`` was added to the database configuration file. 
       

       

      Password constraints:

       

       
      * Must be only printable ASCII characters. 
       
      * Must be at least 16 characters and no more than 128 characters in length. 
       
      * Cannot contain any of the following characters: '/', '"', or '@'.  
       

       

      For more information, see `AUTH password <http://redis.io/commands/AUTH>`__ at http://redis.io/commands/AUTH.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CacheCluster': {
                'CacheClusterId': 'string',
                'ConfigurationEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'ClientDownloadLandingPage': 'string',
                'CacheNodeType': 'string',
                'Engine': 'string',
                'EngineVersion': 'string',
                'CacheClusterStatus': 'string',
                'NumCacheNodes': 123,
                'PreferredAvailabilityZone': 'string',
                'CacheClusterCreateTime': datetime(2015, 1, 1),
                'PreferredMaintenanceWindow': 'string',
                'PendingModifiedValues': {
                    'NumCacheNodes': 123,
                    'CacheNodeIdsToRemove': [
                        'string',
                    ],
                    'EngineVersion': 'string',
                    'CacheNodeType': 'string'
                },
                'NotificationConfiguration': {
                    'TopicArn': 'string',
                    'TopicStatus': 'string'
                },
                'CacheSecurityGroups': [
                    {
                        'CacheSecurityGroupName': 'string',
                        'Status': 'string'
                    },
                ],
                'CacheParameterGroup': {
                    'CacheParameterGroupName': 'string',
                    'ParameterApplyStatus': 'string',
                    'CacheNodeIdsToReboot': [
                        'string',
                    ]
                },
                'CacheSubnetGroupName': 'string',
                'CacheNodes': [
                    {
                        'CacheNodeId': 'string',
                        'CacheNodeStatus': 'string',
                        'CacheNodeCreateTime': datetime(2015, 1, 1),
                        'Endpoint': {
                            'Address': 'string',
                            'Port': 123
                        },
                        'ParameterGroupStatus': 'string',
                        'SourceCacheNodeId': 'string',
                        'CustomerAvailabilityZone': 'string'
                    },
                ],
                'AutoMinorVersionUpgrade': True|False,
                'SecurityGroups': [
                    {
                        'SecurityGroupId': 'string',
                        'Status': 'string'
                    },
                ],
                'ReplicationGroupId': 'string',
                'SnapshotRetentionLimit': 123,
                'SnapshotWindow': 'string',
                'AuthTokenEnabled': True|False,
                'TransitEncryptionEnabled': True|False,
                'AtRestEncryptionEnabled': True|False
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CacheCluster** *(dict) --* 

          Contains all of the attributes of a specific cluster.

          
          

          - **CacheClusterId** *(string) --* 

            The user-supplied identifier of the cluster. This identifier is a unique key that identifies a cluster.

            
          

          - **ConfigurationEndpoint** *(dict) --* 

            Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the cluster, can be used by an application to connect to any node in the cluster. The configuration endpoint will always have ``.cfg`` in it.

             

            Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``  

            
            

            - **Address** *(string) --* 

              The DNS hostname of the cache node.

              
            

            - **Port** *(integer) --* 

              The port number that the cache engine is listening on.

              
        
          

          - **ClientDownloadLandingPage** *(string) --* 

            The URL of the web page where you can download the latest ElastiCache client library.

            
          

          - **CacheNodeType** *(string) --* 

            The name of the compute and memory capacity node type for the cluster.

             

            The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

             

             
            * General purpose: 

               
              * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
               
              * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
               

             
             
            * Compute optimized: 

               
              * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
               

             
             
            * Memory optimized: 

               
              * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
               
              * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
               

             
             

             

             **Notes:**  

             

             
            * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
             
            * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
             
            * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
             
            * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
             

             

            For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

            
          

          - **Engine** *(string) --* 

            The name of the cache engine (``memcached`` or ``redis`` ) to be used for this cluster.

            
          

          - **EngineVersion** *(string) --* 

            The version of the cache engine that is used in this cluster.

            
          

          - **CacheClusterStatus** *(string) --* 

            The current state of this cluster, one of the following values: ``available`` , ``creating`` , ``deleted`` , ``deleting`` , ``incompatible-network`` , ``modifying`` , ``rebooting cluster nodes`` , ``restore-failed`` , or ``snapshotting`` .

            
          

          - **NumCacheNodes** *(integer) --* 

            The number of cache nodes in the cluster.

             

            For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

            
          

          - **PreferredAvailabilityZone** *(string) --* 

            The name of the Availability Zone in which the cluster is located or "Multiple" if the cache nodes are located in different Availability Zones.

            
          

          - **CacheClusterCreateTime** *(datetime) --* 

            The date and time when the cluster was created.

            
          

          - **PreferredMaintenanceWindow** *(string) --* 

            Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.

             

            Valid values for ``ddd`` are:

             

             
            * ``sun``   
             
            * ``mon``   
             
            * ``tue``   
             
            * ``wed``   
             
            * ``thu``   
             
            * ``fri``   
             
            * ``sat``   
             

             

            Example: ``sun:23:00-mon:01:30``  

            
          

          - **PendingModifiedValues** *(dict) --* 

            A group of settings that are applied to the cluster in the future, or that are currently being applied.

            
            

            - **NumCacheNodes** *(integer) --* 

              The new number of cache nodes for the cluster.

               

              For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

              
            

            - **CacheNodeIdsToRemove** *(list) --* 

              A list of cache node IDs that are being removed (or will be removed) from the cluster. A node ID is a numeric identifier (0001, 0002, etc.).

              
              

              - *(string) --* 
          
            

            - **EngineVersion** *(string) --* 

              The new cache engine version that the cluster runs.

              
            

            - **CacheNodeType** *(string) --* 

              The cache node type that this cluster or replication group is scaled to.

              
        
          

          - **NotificationConfiguration** *(dict) --* 

            Describes a notification topic and its status. Notification topics are used for publishing ElastiCache events to subscribers using Amazon Simple Notification Service (SNS). 

            
            

            - **TopicArn** *(string) --* 

              The Amazon Resource Name (ARN) that identifies the topic.

              
            

            - **TopicStatus** *(string) --* 

              The current state of the topic.

              
        
          

          - **CacheSecurityGroups** *(list) --* 

            A list of cache security group elements, composed of name and status sub-elements.

            
            

            - *(dict) --* 

              Represents a cluster's status within a particular cache security group.

              
              

              - **CacheSecurityGroupName** *(string) --* 

                The name of the cache security group.

                
              

              - **Status** *(string) --* 

                The membership status in the cache security group. The status changes when a cache security group is modified, or when the cache security groups assigned to a cluster are modified.

                
          
        
          

          - **CacheParameterGroup** *(dict) --* 

            Status of the cache parameter group.

            
            

            - **CacheParameterGroupName** *(string) --* 

              The name of the cache parameter group.

              
            

            - **ParameterApplyStatus** *(string) --* 

              The status of parameter updates.

              
            

            - **CacheNodeIdsToReboot** *(list) --* 

              A list of the cache node IDs which need to be rebooted for parameter changes to be applied. A node ID is a numeric identifier (0001, 0002, etc.).

              
              

              - *(string) --* 
          
        
          

          - **CacheSubnetGroupName** *(string) --* 

            The name of the cache subnet group associated with the cluster.

            
          

          - **CacheNodes** *(list) --* 

            A list of cache nodes that are members of the cluster.

            
            

            - *(dict) --* 

              Represents an individual cache node within a cluster. Each cache node runs its own instance of the cluster's protocol-compliant caching software - either Memcached or Redis.

               

              The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

               

               
              * General purpose: 

                 
                * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
                 
                * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
                 

               
               
              * Compute optimized: 

                 
                * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
                 

               
               
              * Memory optimized: 

                 
                * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
                 
                * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
                 

               
               

               

               **Notes:**  

               

               
              * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
               
              * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
               
              * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
               
              * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
               

               

              For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

              
              

              - **CacheNodeId** *(string) --* 

                The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The combination of cluster ID and node ID uniquely identifies every cache node used in a customer's AWS account.

                
              

              - **CacheNodeStatus** *(string) --* 

                The current state of this cache node.

                
              

              - **CacheNodeCreateTime** *(datetime) --* 

                The date and time when the cache node was created.

                
              

              - **Endpoint** *(dict) --* 

                The hostname for connecting to this cache node.

                
                

                - **Address** *(string) --* 

                  The DNS hostname of the cache node.

                  
                

                - **Port** *(integer) --* 

                  The port number that the cache engine is listening on.

                  
            
              

              - **ParameterGroupStatus** *(string) --* 

                The status of the parameter group applied to this cache node.

                
              

              - **SourceCacheNodeId** *(string) --* 

                The ID of the primary node to which this read replica node is synchronized. If this field is empty, this node is not associated with a primary cluster.

                
              

              - **CustomerAvailabilityZone** *(string) --* 

                The Availability Zone where this node was created and now resides.

                
          
        
          

          - **AutoMinorVersionUpgrade** *(boolean) --* 

            This parameter is currently disabled.

            
          

          - **SecurityGroups** *(list) --* 

            A list of VPC Security Groups associated with the cluster.

            
            

            - *(dict) --* 

              Represents a single cache security group and its status.

              
              

              - **SecurityGroupId** *(string) --* 

                The identifier of the cache security group.

                
              

              - **Status** *(string) --* 

                The status of the cache security group membership. The status changes whenever a cache security group is modified, or when the cache security groups assigned to a cluster are modified.

                
          
        
          

          - **ReplicationGroupId** *(string) --* 

            The replication group to which this cluster belongs. If this field is empty, the cluster is not associated with any replication group.

            
          

          - **SnapshotRetentionLimit** *(integer) --* 

            The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was taken today is retained for 5 days before being deleted.

             

            .. warning::

               

              If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

               

            
          

          - **SnapshotWindow** *(string) --* 

            The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your cluster.

             

            Example: ``05:00-09:00``  

            
          

          - **AuthTokenEnabled** *(boolean) --* 

            A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

             

            Default: ``false``  

            
          

          - **TransitEncryptionEnabled** *(boolean) --* 

            A flag that enables in-transit encryption when set to ``true`` .

             

            You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created. To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to ``true`` when you create a cluster.

             

            Default: ``false``  

            
          

          - **AtRestEncryptionEnabled** *(boolean) --* 

            A flag that enables encryption at-rest when set to ``true`` .

             

            You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To enable at-rest encryption on a cluster you must set ``AtRestEncryptionEnabled`` to ``true`` when you create a cluster.

             

            Default: ``false``  

            
      
    

  .. py:method:: create_cache_parameter_group(**kwargs)

    

    Creates a new Amazon ElastiCache cache parameter group. An ElastiCache cache parameter group is a collection of parameters and their values that are applied to all of the nodes in any cluster or replication group using the CacheParameterGroup.

     

    A newly created CacheParameterGroup is an exact duplicate of the default parameter group for the CacheParameterGroupFamily. To customize the newly created CacheParameterGroup you can change the values of specific parameters. For more information, see:

     

     
    * `ModifyCacheParameterGroup <http://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ModifyCacheParameterGroup.html>`__ in the ElastiCache API Reference. 
     
    * `Parameters and Parameter Groups <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/ParameterGroups.html>`__ in the ElastiCache User Guide. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/CreateCacheParameterGroup>`_    


    **Request Syntax** 
    ::

      response = client.create_cache_parameter_group(
          CacheParameterGroupName='string',
          CacheParameterGroupFamily='string',
          Description='string'
      )
    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: **[REQUIRED]** 

      A user-specified name for the cache parameter group.

      

    
    :type CacheParameterGroupFamily: string
    :param CacheParameterGroupFamily: **[REQUIRED]** 

      The name of the cache parameter group family that the cache parameter group can be used with.

       

      Valid values are: ``memcached1.4`` | ``redis2.6`` | ``redis2.8`` | ``redis3.2``  

      

    
    :type Description: string
    :param Description: **[REQUIRED]** 

      A user-specified description for the cache parameter group.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CacheParameterGroup': {
                'CacheParameterGroupName': 'string',
                'CacheParameterGroupFamily': 'string',
                'Description': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CacheParameterGroup** *(dict) --* 

          Represents the output of a ``CreateCacheParameterGroup`` operation.

          
          

          - **CacheParameterGroupName** *(string) --* 

            The name of the cache parameter group.

            
          

          - **CacheParameterGroupFamily** *(string) --* 

            The name of the cache parameter group family that this cache parameter group is compatible with.

             

            Valid values are: ``memcached1.4`` | ``redis2.6`` | ``redis2.8`` | ``redis3.2``  

            
          

          - **Description** *(string) --* 

            The description for this cache parameter group.

            
      
    

  .. py:method:: create_cache_security_group(**kwargs)

    

    Creates a new cache security group. Use a cache security group to control access to one or more clusters.

     

    Cache security groups are only used when you are creating a cluster outside of an Amazon Virtual Private Cloud (Amazon VPC). If you are creating a cluster inside of a VPC, use a cache subnet group instead. For more information, see `CreateCacheSubnetGroup <http://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateCacheSubnetGroup.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/CreateCacheSecurityGroup>`_    


    **Request Syntax** 
    ::

      response = client.create_cache_security_group(
          CacheSecurityGroupName='string',
          Description='string'
      )
    :type CacheSecurityGroupName: string
    :param CacheSecurityGroupName: **[REQUIRED]** 

      A name for the cache security group. This value is stored as a lowercase string.

       

      Constraints: Must contain no more than 255 alphanumeric characters. Cannot be the word "Default".

       

      Example: ``mysecuritygroup``  

      

    
    :type Description: string
    :param Description: **[REQUIRED]** 

      A description for the cache security group.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CacheSecurityGroup': {
                'OwnerId': 'string',
                'CacheSecurityGroupName': 'string',
                'Description': 'string',
                'EC2SecurityGroups': [
                    {
                        'Status': 'string',
                        'EC2SecurityGroupName': 'string',
                        'EC2SecurityGroupOwnerId': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CacheSecurityGroup** *(dict) --* 

          Represents the output of one of the following operations:

           

           
          * ``AuthorizeCacheSecurityGroupIngress``   
           
          * ``CreateCacheSecurityGroup``   
           
          * ``RevokeCacheSecurityGroupIngress``   
           

          
          

          - **OwnerId** *(string) --* 

            The AWS account ID of the cache security group owner.

            
          

          - **CacheSecurityGroupName** *(string) --* 

            The name of the cache security group.

            
          

          - **Description** *(string) --* 

            The description of the cache security group.

            
          

          - **EC2SecurityGroups** *(list) --* 

            A list of Amazon EC2 security groups that are associated with this cache security group.

            
            

            - *(dict) --* 

              Provides ownership and status information for an Amazon EC2 security group.

              
              

              - **Status** *(string) --* 

                The status of the Amazon EC2 security group.

                
              

              - **EC2SecurityGroupName** *(string) --* 

                The name of the Amazon EC2 security group.

                
              

              - **EC2SecurityGroupOwnerId** *(string) --* 

                The AWS account ID of the Amazon EC2 security group owner.

                
          
        
      
    

  .. py:method:: create_cache_subnet_group(**kwargs)

    

    Creates a new cache subnet group.

     

    Use this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud (Amazon VPC).

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/CreateCacheSubnetGroup>`_    


    **Request Syntax** 
    ::

      response = client.create_cache_subnet_group(
          CacheSubnetGroupName='string',
          CacheSubnetGroupDescription='string',
          SubnetIds=[
              'string',
          ]
      )
    :type CacheSubnetGroupName: string
    :param CacheSubnetGroupName: **[REQUIRED]** 

      A name for the cache subnet group. This value is stored as a lowercase string.

       

      Constraints: Must contain no more than 255 alphanumeric characters or hyphens.

       

      Example: ``mysubnetgroup``  

      

    
    :type CacheSubnetGroupDescription: string
    :param CacheSubnetGroupDescription: **[REQUIRED]** 

      A description for the cache subnet group.

      

    
    :type SubnetIds: list
    :param SubnetIds: **[REQUIRED]** 

      A list of VPC subnet IDs for the cache subnet group.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CacheSubnetGroup': {
                'CacheSubnetGroupName': 'string',
                'CacheSubnetGroupDescription': 'string',
                'VpcId': 'string',
                'Subnets': [
                    {
                        'SubnetIdentifier': 'string',
                        'SubnetAvailabilityZone': {
                            'Name': 'string'
                        }
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CacheSubnetGroup** *(dict) --* 

          Represents the output of one of the following operations:

           

           
          * ``CreateCacheSubnetGroup``   
           
          * ``ModifyCacheSubnetGroup``   
           

          
          

          - **CacheSubnetGroupName** *(string) --* 

            The name of the cache subnet group.

            
          

          - **CacheSubnetGroupDescription** *(string) --* 

            The description of the cache subnet group.

            
          

          - **VpcId** *(string) --* 

            The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group.

            
          

          - **Subnets** *(list) --* 

            A list of subnets associated with the cache subnet group.

            
            

            - *(dict) --* 

              Represents the subnet associated with a cluster. This parameter refers to subnets defined in Amazon Virtual Private Cloud (Amazon VPC) and used with ElastiCache.

              
              

              - **SubnetIdentifier** *(string) --* 

                The unique identifier for the subnet.

                
              

              - **SubnetAvailabilityZone** *(dict) --* 

                The Availability Zone associated with the subnet.

                
                

                - **Name** *(string) --* 

                  The name of the Availability Zone.

                  
            
          
        
      
    

  .. py:method:: create_replication_group(**kwargs)

    

    Creates a Redis (cluster mode disabled) or a Redis (cluster mode enabled) replication group.

     

    A Redis (cluster mode disabled) replication group is a collection of clusters, where one of the clusters is a read/write primary and the others are read-only replicas. Writes to the primary are asynchronously propagated to the replicas.

     

    A Redis (cluster mode enabled) replication group is a collection of 1 to 15 node groups (shards). Each node group (shard) has one read/write primary node and up to 5 read-only replica nodes. Writes to the primary are asynchronously propagated to the replicas. Redis (cluster mode enabled) replication groups partition the data across node groups (shards).

     

    When a Redis (cluster mode disabled) replication group has been successfully created, you can add one or more read replicas to it, up to a total of 5 read replicas. You cannot alter a Redis (cluster mode enabled) replication group after it has been created. However, if you need to increase or decrease the number of node groups (console: shards), you can avail yourself of ElastiCache for Redis' enhanced backup and restore. For more information, see `Restoring From a Backup with Cluster Resizing <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/backups-restoring.html>`__ in the *ElastiCache User Guide* .

     

    .. note::

       

      This operation is valid for Redis only.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/CreateReplicationGroup>`_    


    **Request Syntax** 
    ::

      response = client.create_replication_group(
          ReplicationGroupId='string',
          ReplicationGroupDescription='string',
          PrimaryClusterId='string',
          AutomaticFailoverEnabled=True|False,
          NumCacheClusters=123,
          PreferredCacheClusterAZs=[
              'string',
          ],
          NumNodeGroups=123,
          ReplicasPerNodeGroup=123,
          NodeGroupConfiguration=[
              {
                  'Slots': 'string',
                  'ReplicaCount': 123,
                  'PrimaryAvailabilityZone': 'string',
                  'ReplicaAvailabilityZones': [
                      'string',
                  ]
              },
          ],
          CacheNodeType='string',
          Engine='string',
          EngineVersion='string',
          CacheParameterGroupName='string',
          CacheSubnetGroupName='string',
          CacheSecurityGroupNames=[
              'string',
          ],
          SecurityGroupIds=[
              'string',
          ],
          Tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ],
          SnapshotArns=[
              'string',
          ],
          SnapshotName='string',
          PreferredMaintenanceWindow='string',
          Port=123,
          NotificationTopicArn='string',
          AutoMinorVersionUpgrade=True|False,
          SnapshotRetentionLimit=123,
          SnapshotWindow='string',
          AuthToken='string',
          TransitEncryptionEnabled=True|False,
          AtRestEncryptionEnabled=True|False
      )
    :type ReplicationGroupId: string
    :param ReplicationGroupId: **[REQUIRED]** 

      The replication group identifier. This parameter is stored as a lowercase string.

       

      Constraints:

       

       
      * A name must contain from 1 to 20 alphanumeric characters or hyphens. 
       
      * The first character must be a letter. 
       
      * A name cannot end with a hyphen or contain two consecutive hyphens. 
       

      

    
    :type ReplicationGroupDescription: string
    :param ReplicationGroupDescription: **[REQUIRED]** 

      A user-created description for the replication group.

      

    
    :type PrimaryClusterId: string
    :param PrimaryClusterId: 

      The identifier of the cluster that serves as the primary for this replication group. This cluster must already exist and have a status of ``available`` .

       

      This parameter is not required if ``NumCacheClusters`` , ``NumNodeGroups`` , or ``ReplicasPerNodeGroup`` is specified.

      

    
    :type AutomaticFailoverEnabled: boolean
    :param AutomaticFailoverEnabled: 

      Specifies whether a read-only replica is automatically promoted to read/write primary if the existing primary fails.

       

      If ``true`` , Multi-AZ is enabled for this replication group. If ``false`` , Multi-AZ is disabled for this replication group.

       

       ``AutomaticFailoverEnabled`` must be enabled for Redis (cluster mode enabled) replication groups.

       

      Default: false

       

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

       

       
      * Redis versions earlier than 2.8.6. 
       
      * Redis (cluster mode disabled): T1 and T2 cache node types. 
       
      * Redis (cluster mode enabled): T1 node types. 
       

      

    
    :type NumCacheClusters: integer
    :param NumCacheClusters: 

      The number of clusters this replication group initially has.

       

      This parameter is not used if there is more than one node group (shard). You should use ``ReplicasPerNodeGroup`` instead.

       

      If ``AutomaticFailoverEnabled`` is ``true`` , the value of this parameter must be at least 2. If ``AutomaticFailoverEnabled`` is ``false`` you can omit this parameter (it will default to 1), or you can explicitly set it to a value between 2 and 6.

       

      The maximum permitted value for ``NumCacheClusters`` is 6 (primary plus 5 replicas).

      

    
    :type PreferredCacheClusterAZs: list
    :param PreferredCacheClusterAZs: 

      A list of EC2 Availability Zones in which the replication group's clusters are created. The order of the Availability Zones in the list is the order in which clusters are allocated. The primary cluster is created in the first AZ in the list.

       

      This parameter is not used if there is more than one node group (shard). You should use ``NodeGroupConfiguration`` instead.

       

      .. note::

         

        If you are creating your replication group in an Amazon VPC (recommended), you can only locate clusters in Availability Zones associated with the subnets in the selected subnet group.

         

        The number of Availability Zones listed must equal the value of ``NumCacheClusters`` .

         

       

      Default: system chosen Availability Zones.

      

    
      - *(string) --* 

      
  
    :type NumNodeGroups: integer
    :param NumNodeGroups: 

      An optional parameter that specifies the number of node groups (shards) for this Redis (cluster mode enabled) replication group. For Redis (cluster mode disabled) either omit this parameter or set it to 1.

       

      Default: 1

      

    
    :type ReplicasPerNodeGroup: integer
    :param ReplicasPerNodeGroup: 

      An optional parameter that specifies the number of replica nodes in each node group (shard). Valid values are 0 to 5.

      

    
    :type NodeGroupConfiguration: list
    :param NodeGroupConfiguration: 

      A list of node group (shard) configuration options. Each node group (shard) configuration has the following: Slots, PrimaryAvailabilityZone, ReplicaAvailabilityZones, ReplicaCount.

       

      If you're creating a Redis (cluster mode disabled) or a Redis (cluster mode enabled) replication group, you can use this parameter to individually configure each node group (shard), or you can omit this parameter.

      

    
      - *(dict) --* 

        Node group (shard) configuration options. Each node group (shard) configuration has the following: ``Slots`` , ``PrimaryAvailabilityZone`` , ``ReplicaAvailabilityZones`` , ``ReplicaCount`` .

        

      
        - **Slots** *(string) --* 

          A string that specifies the keyspace for a particular node group. Keyspaces range from 0 to 16,383. The string is in the format ``startkey-endkey`` .

           

          Example: ``"0-3999"``  

          

        
        - **ReplicaCount** *(integer) --* 

          The number of read replica nodes in this node group (shard).

          

        
        - **PrimaryAvailabilityZone** *(string) --* 

          The Availability Zone where the primary node of this node group (shard) is launched.

          

        
        - **ReplicaAvailabilityZones** *(list) --* 

          A list of Availability Zones to be used for the read replicas. The number of Availability Zones in this list must match the value of ``ReplicaCount`` or ``ReplicasPerNodeGroup`` if not specified.

          

        
          - *(string) --* 

          
      
      
  
    :type CacheNodeType: string
    :param CacheNodeType: 

      The compute and memory capacity of the nodes in the node group (shard).

       

      The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

       

       
      * General purpose: 

         
        * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
         
        * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
         

       
       
      * Compute optimized: 

         
        * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
         

       
       
      * Memory optimized: 

         
        * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
         
        * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
         

       
       

       

       **Notes:**  

       

       
      * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
       
      * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
       
      * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
       
      * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
       

       

      For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

      

    
    :type Engine: string
    :param Engine: 

      The name of the cache engine to be used for the clusters in this replication group.

      

    
    :type EngineVersion: string
    :param EngineVersion: 

      The version number of the cache engine to be used for the clusters in this replication group. To view the supported cache engine versions, use the ``DescribeCacheEngineVersions`` operation.

       

       **Important:** You can upgrade to a newer engine version (see `Selecting a Cache Engine and Version <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/SelectEngine.html#VersionManagement>`__ ) in the *ElastiCache User Guide* , but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster or replication group and create it anew with the earlier engine version. 

      

    
    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: 

      The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used.

       

      If you are running Redis version 3.2.4 or later, only one node group (shard), and want to use a default parameter group, we recommend that you specify the parameter group by name. 

       

       
      * To create a Redis (cluster mode disabled) replication group, use ``CacheParameterGroupName=default.redis3.2`` . 
       
      * To create a Redis (cluster mode enabled) replication group, use ``CacheParameterGroupName=default.redis3.2.cluster.on`` . 
       

      

    
    :type CacheSubnetGroupName: string
    :param CacheSubnetGroupName: 

      The name of the cache subnet group to be used for the replication group.

       

      .. warning::

         

        If you're going to launch your cluster in an Amazon VPC, you need to create a subnet group before you start creating a cluster. For more information, see `Subnets and Subnet Groups <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/SubnetGroups.html>`__ .

         

      

    
    :type CacheSecurityGroupNames: list
    :param CacheSecurityGroupNames: 

      A list of cache security group names to associate with this replication group.

      

    
      - *(string) --* 

      
  
    :type SecurityGroupIds: list
    :param SecurityGroupIds: 

      One or more Amazon VPC security groups associated with this replication group.

       

      Use this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud (Amazon VPC).

      

    
      - *(string) --* 

      
  
    :type Tags: list
    :param Tags: 

      A list of cost allocation tags to be added to this resource. A tag is a key-value pair. A tag key does not have to be accompanied by a tag value.

      

    
      - *(dict) --* 

        A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. A tag with a null Value is permitted.

        

      
        - **Key** *(string) --* 

          The key for the tag. May not be null.

          

        
        - **Value** *(string) --* 

          The tag's value. May be null.

          

        
      
  
    :type SnapshotArns: list
    :param SnapshotArns: 

      A list of Amazon Resource Names (ARN) that uniquely identify the Redis RDB snapshot files stored in Amazon S3. The snapshot files are used to populate the new replication group. The Amazon S3 object name in the ARN cannot contain any commas. The new replication group will have the number of node groups (console: shards) specified by the parameter *NumNodeGroups* or the number of node groups configured by *NodeGroupConfiguration* regardless of the number of ARNs specified here.

       

      Example of an Amazon S3 ARN: ``arn:aws:s3:::my_bucket/snapshot1.rdb``  

      

    
      - *(string) --* 

      
  
    :type SnapshotName: string
    :param SnapshotName: 

      The name of a snapshot from which to restore data into the new replication group. The snapshot status changes to ``restoring`` while the new replication group is being created.

      

    
    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: 

      Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period. Valid values for ``ddd`` are:

       

      Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.

       

      Valid values for ``ddd`` are:

       

       
      * ``sun``   
       
      * ``mon``   
       
      * ``tue``   
       
      * ``wed``   
       
      * ``thu``   
       
      * ``fri``   
       
      * ``sat``   
       

       

      Example: ``sun:23:00-mon:01:30``  

      

    
    :type Port: integer
    :param Port: 

      The port number on which each member of the replication group accepts connections.

      

    
    :type NotificationTopicArn: string
    :param NotificationTopicArn: 

      The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.

       

      .. note::

         

        The Amazon SNS topic owner must be the same as the cluster owner.

         

      

    
    :type AutoMinorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: 

      This parameter is currently disabled.

      

    
    :type SnapshotRetentionLimit: integer
    :param SnapshotRetentionLimit: 

      The number of days for which ElastiCache retains automatic snapshots before deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was taken today is retained for 5 days before being deleted.

       

      Default: 0 (i.e., automatic backups are disabled for this cluster).

      

    
    :type SnapshotWindow: string
    :param SnapshotWindow: 

      The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).

       

      Example: ``05:00-09:00``  

       

      If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

      

    
    :type AuthToken: string
    :param AuthToken: 

       **Reserved parameter.** The password used to access a password protected server.

       

      This parameter is valid only if:

       

       
      * The parameter ``TransitEncryptionEnabled`` was set to ``true`` when the cluster was created. 
       
      * The line ``requirepass`` was added to the database configuration file. 
       

       

      Password constraints:

       

       
      * Must be only printable ASCII characters. 
       
      * Must be at least 16 characters and no more than 128 characters in length. 
       
      * Cannot contain any of the following characters: '/', '"', or '@'.  
       

       

      For more information, see `AUTH password <http://redis.io/commands/AUTH>`__ at http://redis.io/commands/AUTH.

      

    
    :type TransitEncryptionEnabled: boolean
    :param TransitEncryptionEnabled: 

      A flag that enables in-transit encryption when set to ``true`` .

       

      You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created. To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to ``true`` when you create a cluster.

       

      This parameter is valid only if the ``Engine`` parameter is ``redis`` , the ``EngineVersion`` parameter is ``3.2.4`` or later, and the cluster is being created in an Amazon VPC.

       

      If you enable in-transit encryption, you must also specify a value for ``CacheSubnetGroup`` .

       

      Default: ``false``  

      

    
    :type AtRestEncryptionEnabled: boolean
    :param AtRestEncryptionEnabled: 

      A flag that enables encryption at rest when set to ``true`` .

       

      You cannot modify the value of ``AtRestEncryptionEnabled`` after the replication group is created. To enable encryption at rest on a replication group you must set ``AtRestEncryptionEnabled`` to ``true`` when you create the replication group. 

       

      .. note::

         

        This parameter is valid only if the ``Engine`` parameter is ``redis`` and the cluster is being created in an Amazon VPC.

         

       

      Default: ``false``  

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ReplicationGroup': {
                'ReplicationGroupId': 'string',
                'Description': 'string',
                'Status': 'string',
                'PendingModifiedValues': {
                    'PrimaryClusterId': 'string',
                    'AutomaticFailoverStatus': 'enabled'|'disabled',
                    'Resharding': {
                        'SlotMigration': {
                            'ProgressPercentage': 123.0
                        }
                    }
                },
                'MemberClusters': [
                    'string',
                ],
                'NodeGroups': [
                    {
                        'NodeGroupId': 'string',
                        'Status': 'string',
                        'PrimaryEndpoint': {
                            'Address': 'string',
                            'Port': 123
                        },
                        'Slots': 'string',
                        'NodeGroupMembers': [
                            {
                                'CacheClusterId': 'string',
                                'CacheNodeId': 'string',
                                'ReadEndpoint': {
                                    'Address': 'string',
                                    'Port': 123
                                },
                                'PreferredAvailabilityZone': 'string',
                                'CurrentRole': 'string'
                            },
                        ]
                    },
                ],
                'SnapshottingClusterId': 'string',
                'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                'ConfigurationEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'SnapshotRetentionLimit': 123,
                'SnapshotWindow': 'string',
                'ClusterEnabled': True|False,
                'CacheNodeType': 'string',
                'AuthTokenEnabled': True|False,
                'TransitEncryptionEnabled': True|False,
                'AtRestEncryptionEnabled': True|False
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ReplicationGroup** *(dict) --* 

          Contains all of the attributes of a specific Redis replication group.

          
          

          - **ReplicationGroupId** *(string) --* 

            The identifier for the replication group.

            
          

          - **Description** *(string) --* 

            The user supplied description of the replication group.

            
          

          - **Status** *(string) --* 

            The current state of this replication group - ``creating`` , ``available`` , ``modifying`` , ``deleting`` , ``create-failed`` , ``snapshotting`` .

            
          

          - **PendingModifiedValues** *(dict) --* 

            A group of settings to be applied to the replication group, either immediately or during the next maintenance window.

            
            

            - **PrimaryClusterId** *(string) --* 

              The primary cluster ID that is applied immediately (if ``--apply-immediately`` was specified), or during the next maintenance window.

              
            

            - **AutomaticFailoverStatus** *(string) --* 

              Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

               

              Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

               

               
              * Redis versions earlier than 2.8.6. 
               
              * Redis (cluster mode disabled): T1 and T2 cache node types. 
               
              * Redis (cluster mode enabled): T1 node types. 
               

              
            

            - **Resharding** *(dict) --* 

              The status of an online resharding operation.

              
              

              - **SlotMigration** *(dict) --* 

                Represents the progress of an online resharding operation.

                
                

                - **ProgressPercentage** *(float) --* 

                  The percentage of the slot migration that is complete.

                  
            
          
        
          

          - **MemberClusters** *(list) --* 

            The identifiers of all the nodes that are part of this replication group.

            
            

            - *(string) --* 
        
          

          - **NodeGroups** *(list) --* 

            A list of node groups in this replication group. For Redis (cluster mode disabled) replication groups, this is a single-element list. For Redis (cluster mode enabled) replication groups, the list contains an entry for each node group (shard).

            
            

            - *(dict) --* 

              Represents a collection of cache nodes in a replication group. One node in the node group is the read/write primary node. All the other nodes are read-only Replica nodes.

              
              

              - **NodeGroupId** *(string) --* 

                The identifier for the node group (shard). A Redis (cluster mode disabled) replication group contains only 1 node group; therefore, the node group ID is 0001. A Redis (cluster mode enabled) replication group contains 1 to 15 node groups numbered 0001 to 0015. 

                
              

              - **Status** *(string) --* 

                The current state of this replication group - ``creating`` , ``available`` , etc.

                
              

              - **PrimaryEndpoint** *(dict) --* 

                The endpoint of the primary node in this node group (shard).

                
                

                - **Address** *(string) --* 

                  The DNS hostname of the cache node.

                  
                

                - **Port** *(integer) --* 

                  The port number that the cache engine is listening on.

                  
            
              

              - **Slots** *(string) --* 

                The keyspace for this node group (shard).

                
              

              - **NodeGroupMembers** *(list) --* 

                A list containing information about individual nodes within the node group (shard).

                
                

                - *(dict) --* 

                  Represents a single node within a node group (shard).

                  
                  

                  - **CacheClusterId** *(string) --* 

                    The ID of the cluster to which the node belongs.

                    
                  

                  - **CacheNodeId** *(string) --* 

                    The ID of the node within its cluster. A node ID is a numeric identifier (0001, 0002, etc.).

                    
                  

                  - **ReadEndpoint** *(dict) --* 

                    Represents the information required for client programs to connect to a cache node.

                    
                    

                    - **Address** *(string) --* 

                      The DNS hostname of the cache node.

                      
                    

                    - **Port** *(integer) --* 

                      The port number that the cache engine is listening on.

                      
                
                  

                  - **PreferredAvailabilityZone** *(string) --* 

                    The name of the Availability Zone in which the node is located.

                    
                  

                  - **CurrentRole** *(string) --* 

                    The role that is currently assigned to the node - ``primary`` or ``replica`` .

                    
              
            
          
        
          

          - **SnapshottingClusterId** *(string) --* 

            The cluster ID that is used as the daily snapshot source for the replication group.

            
          

          - **AutomaticFailover** *(string) --* 

            Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

             

            Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

             

             
            * Redis versions earlier than 2.8.6. 
             
            * Redis (cluster mode disabled): T1 and T2 cache node types. 
             
            * Redis (cluster mode enabled): T1 node types. 
             

            
          

          - **ConfigurationEndpoint** *(dict) --* 

            The configuration endpoint for this replication group. Use the configuration endpoint to connect to this replication group.

            
            

            - **Address** *(string) --* 

              The DNS hostname of the cache node.

              
            

            - **Port** *(integer) --* 

              The port number that the cache engine is listening on.

              
        
          

          - **SnapshotRetentionLimit** *(integer) --* 

            The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was taken today is retained for 5 days before being deleted.

             

            .. warning::

               

              If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

               

            
          

          - **SnapshotWindow** *(string) --* 

            The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).

             

            Example: ``05:00-09:00``  

             

            If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

             

            .. note::

               

              This parameter is only valid if the ``Engine`` parameter is ``redis`` .

               

            
          

          - **ClusterEnabled** *(boolean) --* 

            A flag indicating whether or not this replication group is cluster enabled; i.e., whether its data can be partitioned across multiple shards (API/CLI: node groups).

             

            Valid values: ``true`` | ``false``  

            
          

          - **CacheNodeType** *(string) --* 

            The name of the compute and memory capacity node type for each node in the replication group.

            
          

          - **AuthTokenEnabled** *(boolean) --* 

            A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

             

            Default: ``false``  

            
          

          - **TransitEncryptionEnabled** *(boolean) --* 

            A flag that enables in-transit encryption when set to ``true`` .

             

            You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created. To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to ``true`` when you create a cluster.

             

            Default: ``false``  

            
          

          - **AtRestEncryptionEnabled** *(boolean) --* 

            A flag that enables encryption at-rest when set to ``true`` .

             

            You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true`` when you create a cluster.

             

            Default: ``false``  

            
      
    

  .. py:method:: create_snapshot(**kwargs)

    

    Creates a copy of an entire cluster or replication group at a specific moment in time.

     

    .. note::

       

      This operation is valid for Redis only.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/CreateSnapshot>`_    


    **Request Syntax** 
    ::

      response = client.create_snapshot(
          ReplicationGroupId='string',
          CacheClusterId='string',
          SnapshotName='string'
      )
    :type ReplicationGroupId: string
    :param ReplicationGroupId: 

      The identifier of an existing replication group. The snapshot is created from this replication group.

      

    
    :type CacheClusterId: string
    :param CacheClusterId: 

      The identifier of an existing cluster. The snapshot is created from this cluster.

      

    
    :type SnapshotName: string
    :param SnapshotName: **[REQUIRED]** 

      A name for the snapshot being created.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Snapshot': {
                'SnapshotName': 'string',
                'ReplicationGroupId': 'string',
                'ReplicationGroupDescription': 'string',
                'CacheClusterId': 'string',
                'SnapshotStatus': 'string',
                'SnapshotSource': 'string',
                'CacheNodeType': 'string',
                'Engine': 'string',
                'EngineVersion': 'string',
                'NumCacheNodes': 123,
                'PreferredAvailabilityZone': 'string',
                'CacheClusterCreateTime': datetime(2015, 1, 1),
                'PreferredMaintenanceWindow': 'string',
                'TopicArn': 'string',
                'Port': 123,
                'CacheParameterGroupName': 'string',
                'CacheSubnetGroupName': 'string',
                'VpcId': 'string',
                'AutoMinorVersionUpgrade': True|False,
                'SnapshotRetentionLimit': 123,
                'SnapshotWindow': 'string',
                'NumNodeGroups': 123,
                'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                'NodeSnapshots': [
                    {
                        'CacheClusterId': 'string',
                        'NodeGroupId': 'string',
                        'CacheNodeId': 'string',
                        'NodeGroupConfiguration': {
                            'Slots': 'string',
                            'ReplicaCount': 123,
                            'PrimaryAvailabilityZone': 'string',
                            'ReplicaAvailabilityZones': [
                                'string',
                            ]
                        },
                        'CacheSize': 'string',
                        'CacheNodeCreateTime': datetime(2015, 1, 1),
                        'SnapshotCreateTime': datetime(2015, 1, 1)
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Snapshot** *(dict) --* 

          Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.

          
          

          - **SnapshotName** *(string) --* 

            The name of a snapshot. For an automatic snapshot, the name is system-generated. For a manual snapshot, this is the user-provided name.

            
          

          - **ReplicationGroupId** *(string) --* 

            The unique identifier of the source replication group.

            
          

          - **ReplicationGroupDescription** *(string) --* 

            A description of the source replication group.

            
          

          - **CacheClusterId** *(string) --* 

            The user-supplied identifier of the source cluster.

            
          

          - **SnapshotStatus** *(string) --* 

            The status of the snapshot. Valid values: ``creating`` | ``available`` | ``restoring`` | ``copying`` | ``deleting`` .

            
          

          - **SnapshotSource** *(string) --* 

            Indicates whether the snapshot is from an automatic backup (``automated`` ) or was created manually (``manual`` ).

            
          

          - **CacheNodeType** *(string) --* 

            The name of the compute and memory capacity node type for the source cluster.

             

            The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

             

             
            * General purpose: 

               
              * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
               
              * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
               

             
             
            * Compute optimized: 

               
              * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
               

             
             
            * Memory optimized: 

               
              * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
               
              * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
               

             
             

             

             **Notes:**  

             

             
            * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
             
            * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
             
            * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
             
            * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
             

             

            For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

            
          

          - **Engine** *(string) --* 

            The name of the cache engine (``memcached`` or ``redis`` ) used by the source cluster.

            
          

          - **EngineVersion** *(string) --* 

            The version of the cache engine version that is used by the source cluster.

            
          

          - **NumCacheNodes** *(integer) --* 

            The number of cache nodes in the source cluster.

             

            For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

            
          

          - **PreferredAvailabilityZone** *(string) --* 

            The name of the Availability Zone in which the source cluster is located.

            
          

          - **CacheClusterCreateTime** *(datetime) --* 

            The date and time when the source cluster was created.

            
          

          - **PreferredMaintenanceWindow** *(string) --* 

            Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.

             

            Valid values for ``ddd`` are:

             

             
            * ``sun``   
             
            * ``mon``   
             
            * ``tue``   
             
            * ``wed``   
             
            * ``thu``   
             
            * ``fri``   
             
            * ``sat``   
             

             

            Example: ``sun:23:00-mon:01:30``  

            
          

          - **TopicArn** *(string) --* 

            The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing notifications.

            
          

          - **Port** *(integer) --* 

            The port number used by each cache nodes in the source cluster.

            
          

          - **CacheParameterGroupName** *(string) --* 

            The cache parameter group that is associated with the source cluster.

            
          

          - **CacheSubnetGroupName** *(string) --* 

            The name of the cache subnet group associated with the source cluster.

            
          

          - **VpcId** *(string) --* 

            The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the source cluster.

            
          

          - **AutoMinorVersionUpgrade** *(boolean) --* 

            This parameter is currently disabled.

            
          

          - **SnapshotRetentionLimit** *(integer) --* 

            For an automatic snapshot, the number of days for which ElastiCache retains the snapshot before deleting it.

             

            For manual snapshots, this field reflects the ``SnapshotRetentionLimit`` for the source cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots do not expire, and can only be deleted using the ``DeleteSnapshot`` operation. 

             

             **Important** If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

            
          

          - **SnapshotWindow** *(string) --* 

            The daily time range during which ElastiCache takes daily snapshots of the source cluster.

            
          

          - **NumNodeGroups** *(integer) --* 

            The number of node groups (shards) in this snapshot. When restoring from a snapshot, the number of node groups (shards) in the snapshot and in the restored replication group must be the same.

            
          

          - **AutomaticFailover** *(string) --* 

            Indicates the status of Multi-AZ with automatic failover for the source Redis replication group.

             

            Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

             

             
            * Redis versions earlier than 2.8.6. 
             
            * Redis (cluster mode disabled): T1 and T2 cache node types. 
             
            * Redis (cluster mode enabled): T1 node types. 
             

            
          

          - **NodeSnapshots** *(list) --* 

            A list of the cache nodes in the source cluster.

            
            

            - *(dict) --* 

              Represents an individual cache node in a snapshot of a cluster.

              
              

              - **CacheClusterId** *(string) --* 

                A unique identifier for the source cluster.

                
              

              - **NodeGroupId** *(string) --* 

                A unique identifier for the source node group (shard).

                
              

              - **CacheNodeId** *(string) --* 

                The cache node identifier for the node in the source cluster.

                
              

              - **NodeGroupConfiguration** *(dict) --* 

                The configuration for the source node group (shard).

                
                

                - **Slots** *(string) --* 

                  A string that specifies the keyspace for a particular node group. Keyspaces range from 0 to 16,383. The string is in the format ``startkey-endkey`` .

                   

                  Example: ``"0-3999"``  

                  
                

                - **ReplicaCount** *(integer) --* 

                  The number of read replica nodes in this node group (shard).

                  
                

                - **PrimaryAvailabilityZone** *(string) --* 

                  The Availability Zone where the primary node of this node group (shard) is launched.

                  
                

                - **ReplicaAvailabilityZones** *(list) --* 

                  A list of Availability Zones to be used for the read replicas. The number of Availability Zones in this list must match the value of ``ReplicaCount`` or ``ReplicasPerNodeGroup`` if not specified.

                  
                  

                  - *(string) --* 
              
            
              

              - **CacheSize** *(string) --* 

                The size of the cache on the source cache node.

                
              

              - **CacheNodeCreateTime** *(datetime) --* 

                The date and time when the cache node was created in the source cluster.

                
              

              - **SnapshotCreateTime** *(datetime) --* 

                The date and time when the source node's metadata and cache data set was obtained for the snapshot.

                
          
        
      
    

  .. py:method:: delete_cache_cluster(**kwargs)

    

    Deletes a previously provisioned cluster. ``DeleteCacheCluster`` deletes all associated cache nodes, node endpoints and the cluster itself. When you receive a successful response from this operation, Amazon ElastiCache immediately begins deleting the cluster; you cannot cancel or revert this operation.

     

    This operation cannot be used to delete a cluster that is the last read replica of a replication group or node group (shard) that has Multi-AZ mode enabled or a cluster from a Redis (cluster mode enabled) replication group.

     

    .. warning::

       

      Due to current limitations on Redis (cluster mode disabled), this operation or parameter is not supported on Redis (cluster mode enabled) replication groups.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DeleteCacheCluster>`_    


    **Request Syntax** 
    ::

      response = client.delete_cache_cluster(
          CacheClusterId='string',
          FinalSnapshotIdentifier='string'
      )
    :type CacheClusterId: string
    :param CacheClusterId: **[REQUIRED]** 

      The cluster identifier for the cluster to be deleted. This parameter is not case sensitive.

      

    
    :type FinalSnapshotIdentifier: string
    :param FinalSnapshotIdentifier: 

      The user-supplied name of a final cluster snapshot. This is the unique name that identifies the snapshot. ElastiCache creates the snapshot, and then deletes the cluster immediately afterward.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CacheCluster': {
                'CacheClusterId': 'string',
                'ConfigurationEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'ClientDownloadLandingPage': 'string',
                'CacheNodeType': 'string',
                'Engine': 'string',
                'EngineVersion': 'string',
                'CacheClusterStatus': 'string',
                'NumCacheNodes': 123,
                'PreferredAvailabilityZone': 'string',
                'CacheClusterCreateTime': datetime(2015, 1, 1),
                'PreferredMaintenanceWindow': 'string',
                'PendingModifiedValues': {
                    'NumCacheNodes': 123,
                    'CacheNodeIdsToRemove': [
                        'string',
                    ],
                    'EngineVersion': 'string',
                    'CacheNodeType': 'string'
                },
                'NotificationConfiguration': {
                    'TopicArn': 'string',
                    'TopicStatus': 'string'
                },
                'CacheSecurityGroups': [
                    {
                        'CacheSecurityGroupName': 'string',
                        'Status': 'string'
                    },
                ],
                'CacheParameterGroup': {
                    'CacheParameterGroupName': 'string',
                    'ParameterApplyStatus': 'string',
                    'CacheNodeIdsToReboot': [
                        'string',
                    ]
                },
                'CacheSubnetGroupName': 'string',
                'CacheNodes': [
                    {
                        'CacheNodeId': 'string',
                        'CacheNodeStatus': 'string',
                        'CacheNodeCreateTime': datetime(2015, 1, 1),
                        'Endpoint': {
                            'Address': 'string',
                            'Port': 123
                        },
                        'ParameterGroupStatus': 'string',
                        'SourceCacheNodeId': 'string',
                        'CustomerAvailabilityZone': 'string'
                    },
                ],
                'AutoMinorVersionUpgrade': True|False,
                'SecurityGroups': [
                    {
                        'SecurityGroupId': 'string',
                        'Status': 'string'
                    },
                ],
                'ReplicationGroupId': 'string',
                'SnapshotRetentionLimit': 123,
                'SnapshotWindow': 'string',
                'AuthTokenEnabled': True|False,
                'TransitEncryptionEnabled': True|False,
                'AtRestEncryptionEnabled': True|False
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CacheCluster** *(dict) --* 

          Contains all of the attributes of a specific cluster.

          
          

          - **CacheClusterId** *(string) --* 

            The user-supplied identifier of the cluster. This identifier is a unique key that identifies a cluster.

            
          

          - **ConfigurationEndpoint** *(dict) --* 

            Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the cluster, can be used by an application to connect to any node in the cluster. The configuration endpoint will always have ``.cfg`` in it.

             

            Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``  

            
            

            - **Address** *(string) --* 

              The DNS hostname of the cache node.

              
            

            - **Port** *(integer) --* 

              The port number that the cache engine is listening on.

              
        
          

          - **ClientDownloadLandingPage** *(string) --* 

            The URL of the web page where you can download the latest ElastiCache client library.

            
          

          - **CacheNodeType** *(string) --* 

            The name of the compute and memory capacity node type for the cluster.

             

            The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

             

             
            * General purpose: 

               
              * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
               
              * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
               

             
             
            * Compute optimized: 

               
              * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
               

             
             
            * Memory optimized: 

               
              * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
               
              * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
               

             
             

             

             **Notes:**  

             

             
            * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
             
            * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
             
            * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
             
            * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
             

             

            For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

            
          

          - **Engine** *(string) --* 

            The name of the cache engine (``memcached`` or ``redis`` ) to be used for this cluster.

            
          

          - **EngineVersion** *(string) --* 

            The version of the cache engine that is used in this cluster.

            
          

          - **CacheClusterStatus** *(string) --* 

            The current state of this cluster, one of the following values: ``available`` , ``creating`` , ``deleted`` , ``deleting`` , ``incompatible-network`` , ``modifying`` , ``rebooting cluster nodes`` , ``restore-failed`` , or ``snapshotting`` .

            
          

          - **NumCacheNodes** *(integer) --* 

            The number of cache nodes in the cluster.

             

            For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

            
          

          - **PreferredAvailabilityZone** *(string) --* 

            The name of the Availability Zone in which the cluster is located or "Multiple" if the cache nodes are located in different Availability Zones.

            
          

          - **CacheClusterCreateTime** *(datetime) --* 

            The date and time when the cluster was created.

            
          

          - **PreferredMaintenanceWindow** *(string) --* 

            Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.

             

            Valid values for ``ddd`` are:

             

             
            * ``sun``   
             
            * ``mon``   
             
            * ``tue``   
             
            * ``wed``   
             
            * ``thu``   
             
            * ``fri``   
             
            * ``sat``   
             

             

            Example: ``sun:23:00-mon:01:30``  

            
          

          - **PendingModifiedValues** *(dict) --* 

            A group of settings that are applied to the cluster in the future, or that are currently being applied.

            
            

            - **NumCacheNodes** *(integer) --* 

              The new number of cache nodes for the cluster.

               

              For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

              
            

            - **CacheNodeIdsToRemove** *(list) --* 

              A list of cache node IDs that are being removed (or will be removed) from the cluster. A node ID is a numeric identifier (0001, 0002, etc.).

              
              

              - *(string) --* 
          
            

            - **EngineVersion** *(string) --* 

              The new cache engine version that the cluster runs.

              
            

            - **CacheNodeType** *(string) --* 

              The cache node type that this cluster or replication group is scaled to.

              
        
          

          - **NotificationConfiguration** *(dict) --* 

            Describes a notification topic and its status. Notification topics are used for publishing ElastiCache events to subscribers using Amazon Simple Notification Service (SNS). 

            
            

            - **TopicArn** *(string) --* 

              The Amazon Resource Name (ARN) that identifies the topic.

              
            

            - **TopicStatus** *(string) --* 

              The current state of the topic.

              
        
          

          - **CacheSecurityGroups** *(list) --* 

            A list of cache security group elements, composed of name and status sub-elements.

            
            

            - *(dict) --* 

              Represents a cluster's status within a particular cache security group.

              
              

              - **CacheSecurityGroupName** *(string) --* 

                The name of the cache security group.

                
              

              - **Status** *(string) --* 

                The membership status in the cache security group. The status changes when a cache security group is modified, or when the cache security groups assigned to a cluster are modified.

                
          
        
          

          - **CacheParameterGroup** *(dict) --* 

            Status of the cache parameter group.

            
            

            - **CacheParameterGroupName** *(string) --* 

              The name of the cache parameter group.

              
            

            - **ParameterApplyStatus** *(string) --* 

              The status of parameter updates.

              
            

            - **CacheNodeIdsToReboot** *(list) --* 

              A list of the cache node IDs which need to be rebooted for parameter changes to be applied. A node ID is a numeric identifier (0001, 0002, etc.).

              
              

              - *(string) --* 
          
        
          

          - **CacheSubnetGroupName** *(string) --* 

            The name of the cache subnet group associated with the cluster.

            
          

          - **CacheNodes** *(list) --* 

            A list of cache nodes that are members of the cluster.

            
            

            - *(dict) --* 

              Represents an individual cache node within a cluster. Each cache node runs its own instance of the cluster's protocol-compliant caching software - either Memcached or Redis.

               

              The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

               

               
              * General purpose: 

                 
                * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
                 
                * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
                 

               
               
              * Compute optimized: 

                 
                * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
                 

               
               
              * Memory optimized: 

                 
                * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
                 
                * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
                 

               
               

               

               **Notes:**  

               

               
              * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
               
              * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
               
              * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
               
              * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
               

               

              For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

              
              

              - **CacheNodeId** *(string) --* 

                The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The combination of cluster ID and node ID uniquely identifies every cache node used in a customer's AWS account.

                
              

              - **CacheNodeStatus** *(string) --* 

                The current state of this cache node.

                
              

              - **CacheNodeCreateTime** *(datetime) --* 

                The date and time when the cache node was created.

                
              

              - **Endpoint** *(dict) --* 

                The hostname for connecting to this cache node.

                
                

                - **Address** *(string) --* 

                  The DNS hostname of the cache node.

                  
                

                - **Port** *(integer) --* 

                  The port number that the cache engine is listening on.

                  
            
              

              - **ParameterGroupStatus** *(string) --* 

                The status of the parameter group applied to this cache node.

                
              

              - **SourceCacheNodeId** *(string) --* 

                The ID of the primary node to which this read replica node is synchronized. If this field is empty, this node is not associated with a primary cluster.

                
              

              - **CustomerAvailabilityZone** *(string) --* 

                The Availability Zone where this node was created and now resides.

                
          
        
          

          - **AutoMinorVersionUpgrade** *(boolean) --* 

            This parameter is currently disabled.

            
          

          - **SecurityGroups** *(list) --* 

            A list of VPC Security Groups associated with the cluster.

            
            

            - *(dict) --* 

              Represents a single cache security group and its status.

              
              

              - **SecurityGroupId** *(string) --* 

                The identifier of the cache security group.

                
              

              - **Status** *(string) --* 

                The status of the cache security group membership. The status changes whenever a cache security group is modified, or when the cache security groups assigned to a cluster are modified.

                
          
        
          

          - **ReplicationGroupId** *(string) --* 

            The replication group to which this cluster belongs. If this field is empty, the cluster is not associated with any replication group.

            
          

          - **SnapshotRetentionLimit** *(integer) --* 

            The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was taken today is retained for 5 days before being deleted.

             

            .. warning::

               

              If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

               

            
          

          - **SnapshotWindow** *(string) --* 

            The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your cluster.

             

            Example: ``05:00-09:00``  

            
          

          - **AuthTokenEnabled** *(boolean) --* 

            A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

             

            Default: ``false``  

            
          

          - **TransitEncryptionEnabled** *(boolean) --* 

            A flag that enables in-transit encryption when set to ``true`` .

             

            You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created. To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to ``true`` when you create a cluster.

             

            Default: ``false``  

            
          

          - **AtRestEncryptionEnabled** *(boolean) --* 

            A flag that enables encryption at-rest when set to ``true`` .

             

            You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To enable at-rest encryption on a cluster you must set ``AtRestEncryptionEnabled`` to ``true`` when you create a cluster.

             

            Default: ``false``  

            
      
    

  .. py:method:: delete_cache_parameter_group(**kwargs)

    

    Deletes the specified cache parameter group. You cannot delete a cache parameter group if it is associated with any cache clusters.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DeleteCacheParameterGroup>`_    


    **Request Syntax** 
    ::

      response = client.delete_cache_parameter_group(
          CacheParameterGroupName='string'
      )
    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: **[REQUIRED]** 

      The name of the cache parameter group to delete.

       

      .. note::

         

        The specified cache security group must not be associated with any clusters.

         

      

    
    
    :returns: None

  .. py:method:: delete_cache_security_group(**kwargs)

    

    Deletes a cache security group.

     

    .. note::

       

      You cannot delete a cache security group if it is associated with any clusters.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DeleteCacheSecurityGroup>`_    


    **Request Syntax** 
    ::

      response = client.delete_cache_security_group(
          CacheSecurityGroupName='string'
      )
    :type CacheSecurityGroupName: string
    :param CacheSecurityGroupName: **[REQUIRED]** 

      The name of the cache security group to delete.

       

      .. note::

         

        You cannot delete the default security group.

         

      

    
    
    :returns: None

  .. py:method:: delete_cache_subnet_group(**kwargs)

    

    Deletes a cache subnet group.

     

    .. note::

       

      You cannot delete a cache subnet group if it is associated with any clusters.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DeleteCacheSubnetGroup>`_    


    **Request Syntax** 
    ::

      response = client.delete_cache_subnet_group(
          CacheSubnetGroupName='string'
      )
    :type CacheSubnetGroupName: string
    :param CacheSubnetGroupName: **[REQUIRED]** 

      The name of the cache subnet group to delete.

       

      Constraints: Must contain no more than 255 alphanumeric characters or hyphens.

      

    
    
    :returns: None

  .. py:method:: delete_replication_group(**kwargs)

    

    Deletes an existing replication group. By default, this operation deletes the entire replication group, including the primary/primaries and all of the read replicas. If the replication group has only one primary, you can optionally delete only the read replicas, while retaining the primary by setting ``RetainPrimaryCluster=true`` .

     

    When you receive a successful response from this operation, Amazon ElastiCache immediately begins deleting the selected resources; you cannot cancel or revert this operation.

     

    .. note::

       

      This operation is valid for Redis only.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DeleteReplicationGroup>`_    


    **Request Syntax** 
    ::

      response = client.delete_replication_group(
          ReplicationGroupId='string',
          RetainPrimaryCluster=True|False,
          FinalSnapshotIdentifier='string'
      )
    :type ReplicationGroupId: string
    :param ReplicationGroupId: **[REQUIRED]** 

      The identifier for the cluster to be deleted. This parameter is not case sensitive.

      

    
    :type RetainPrimaryCluster: boolean
    :param RetainPrimaryCluster: 

      If set to ``true`` , all of the read replicas are deleted, but the primary node is retained.

      

    
    :type FinalSnapshotIdentifier: string
    :param FinalSnapshotIdentifier: 

      The name of a final node group (shard) snapshot. ElastiCache creates the snapshot from the primary node in the cluster, rather than one of the replicas; this is to ensure that it captures the freshest data. After the final snapshot is taken, the replication group is immediately deleted.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ReplicationGroup': {
                'ReplicationGroupId': 'string',
                'Description': 'string',
                'Status': 'string',
                'PendingModifiedValues': {
                    'PrimaryClusterId': 'string',
                    'AutomaticFailoverStatus': 'enabled'|'disabled',
                    'Resharding': {
                        'SlotMigration': {
                            'ProgressPercentage': 123.0
                        }
                    }
                },
                'MemberClusters': [
                    'string',
                ],
                'NodeGroups': [
                    {
                        'NodeGroupId': 'string',
                        'Status': 'string',
                        'PrimaryEndpoint': {
                            'Address': 'string',
                            'Port': 123
                        },
                        'Slots': 'string',
                        'NodeGroupMembers': [
                            {
                                'CacheClusterId': 'string',
                                'CacheNodeId': 'string',
                                'ReadEndpoint': {
                                    'Address': 'string',
                                    'Port': 123
                                },
                                'PreferredAvailabilityZone': 'string',
                                'CurrentRole': 'string'
                            },
                        ]
                    },
                ],
                'SnapshottingClusterId': 'string',
                'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                'ConfigurationEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'SnapshotRetentionLimit': 123,
                'SnapshotWindow': 'string',
                'ClusterEnabled': True|False,
                'CacheNodeType': 'string',
                'AuthTokenEnabled': True|False,
                'TransitEncryptionEnabled': True|False,
                'AtRestEncryptionEnabled': True|False
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ReplicationGroup** *(dict) --* 

          Contains all of the attributes of a specific Redis replication group.

          
          

          - **ReplicationGroupId** *(string) --* 

            The identifier for the replication group.

            
          

          - **Description** *(string) --* 

            The user supplied description of the replication group.

            
          

          - **Status** *(string) --* 

            The current state of this replication group - ``creating`` , ``available`` , ``modifying`` , ``deleting`` , ``create-failed`` , ``snapshotting`` .

            
          

          - **PendingModifiedValues** *(dict) --* 

            A group of settings to be applied to the replication group, either immediately or during the next maintenance window.

            
            

            - **PrimaryClusterId** *(string) --* 

              The primary cluster ID that is applied immediately (if ``--apply-immediately`` was specified), or during the next maintenance window.

              
            

            - **AutomaticFailoverStatus** *(string) --* 

              Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

               

              Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

               

               
              * Redis versions earlier than 2.8.6. 
               
              * Redis (cluster mode disabled): T1 and T2 cache node types. 
               
              * Redis (cluster mode enabled): T1 node types. 
               

              
            

            - **Resharding** *(dict) --* 

              The status of an online resharding operation.

              
              

              - **SlotMigration** *(dict) --* 

                Represents the progress of an online resharding operation.

                
                

                - **ProgressPercentage** *(float) --* 

                  The percentage of the slot migration that is complete.

                  
            
          
        
          

          - **MemberClusters** *(list) --* 

            The identifiers of all the nodes that are part of this replication group.

            
            

            - *(string) --* 
        
          

          - **NodeGroups** *(list) --* 

            A list of node groups in this replication group. For Redis (cluster mode disabled) replication groups, this is a single-element list. For Redis (cluster mode enabled) replication groups, the list contains an entry for each node group (shard).

            
            

            - *(dict) --* 

              Represents a collection of cache nodes in a replication group. One node in the node group is the read/write primary node. All the other nodes are read-only Replica nodes.

              
              

              - **NodeGroupId** *(string) --* 

                The identifier for the node group (shard). A Redis (cluster mode disabled) replication group contains only 1 node group; therefore, the node group ID is 0001. A Redis (cluster mode enabled) replication group contains 1 to 15 node groups numbered 0001 to 0015. 

                
              

              - **Status** *(string) --* 

                The current state of this replication group - ``creating`` , ``available`` , etc.

                
              

              - **PrimaryEndpoint** *(dict) --* 

                The endpoint of the primary node in this node group (shard).

                
                

                - **Address** *(string) --* 

                  The DNS hostname of the cache node.

                  
                

                - **Port** *(integer) --* 

                  The port number that the cache engine is listening on.

                  
            
              

              - **Slots** *(string) --* 

                The keyspace for this node group (shard).

                
              

              - **NodeGroupMembers** *(list) --* 

                A list containing information about individual nodes within the node group (shard).

                
                

                - *(dict) --* 

                  Represents a single node within a node group (shard).

                  
                  

                  - **CacheClusterId** *(string) --* 

                    The ID of the cluster to which the node belongs.

                    
                  

                  - **CacheNodeId** *(string) --* 

                    The ID of the node within its cluster. A node ID is a numeric identifier (0001, 0002, etc.).

                    
                  

                  - **ReadEndpoint** *(dict) --* 

                    Represents the information required for client programs to connect to a cache node.

                    
                    

                    - **Address** *(string) --* 

                      The DNS hostname of the cache node.

                      
                    

                    - **Port** *(integer) --* 

                      The port number that the cache engine is listening on.

                      
                
                  

                  - **PreferredAvailabilityZone** *(string) --* 

                    The name of the Availability Zone in which the node is located.

                    
                  

                  - **CurrentRole** *(string) --* 

                    The role that is currently assigned to the node - ``primary`` or ``replica`` .

                    
              
            
          
        
          

          - **SnapshottingClusterId** *(string) --* 

            The cluster ID that is used as the daily snapshot source for the replication group.

            
          

          - **AutomaticFailover** *(string) --* 

            Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

             

            Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

             

             
            * Redis versions earlier than 2.8.6. 
             
            * Redis (cluster mode disabled): T1 and T2 cache node types. 
             
            * Redis (cluster mode enabled): T1 node types. 
             

            
          

          - **ConfigurationEndpoint** *(dict) --* 

            The configuration endpoint for this replication group. Use the configuration endpoint to connect to this replication group.

            
            

            - **Address** *(string) --* 

              The DNS hostname of the cache node.

              
            

            - **Port** *(integer) --* 

              The port number that the cache engine is listening on.

              
        
          

          - **SnapshotRetentionLimit** *(integer) --* 

            The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was taken today is retained for 5 days before being deleted.

             

            .. warning::

               

              If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

               

            
          

          - **SnapshotWindow** *(string) --* 

            The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).

             

            Example: ``05:00-09:00``  

             

            If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

             

            .. note::

               

              This parameter is only valid if the ``Engine`` parameter is ``redis`` .

               

            
          

          - **ClusterEnabled** *(boolean) --* 

            A flag indicating whether or not this replication group is cluster enabled; i.e., whether its data can be partitioned across multiple shards (API/CLI: node groups).

             

            Valid values: ``true`` | ``false``  

            
          

          - **CacheNodeType** *(string) --* 

            The name of the compute and memory capacity node type for each node in the replication group.

            
          

          - **AuthTokenEnabled** *(boolean) --* 

            A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

             

            Default: ``false``  

            
          

          - **TransitEncryptionEnabled** *(boolean) --* 

            A flag that enables in-transit encryption when set to ``true`` .

             

            You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created. To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to ``true`` when you create a cluster.

             

            Default: ``false``  

            
          

          - **AtRestEncryptionEnabled** *(boolean) --* 

            A flag that enables encryption at-rest when set to ``true`` .

             

            You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true`` when you create a cluster.

             

            Default: ``false``  

            
      
    

  .. py:method:: delete_snapshot(**kwargs)

    

    Deletes an existing snapshot. When you receive a successful response from this operation, ElastiCache immediately begins deleting the snapshot; you cannot cancel or revert this operation.

     

    .. note::

       

      This operation is valid for Redis only.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DeleteSnapshot>`_    


    **Request Syntax** 
    ::

      response = client.delete_snapshot(
          SnapshotName='string'
      )
    :type SnapshotName: string
    :param SnapshotName: **[REQUIRED]** 

      The name of the snapshot to be deleted.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Snapshot': {
                'SnapshotName': 'string',
                'ReplicationGroupId': 'string',
                'ReplicationGroupDescription': 'string',
                'CacheClusterId': 'string',
                'SnapshotStatus': 'string',
                'SnapshotSource': 'string',
                'CacheNodeType': 'string',
                'Engine': 'string',
                'EngineVersion': 'string',
                'NumCacheNodes': 123,
                'PreferredAvailabilityZone': 'string',
                'CacheClusterCreateTime': datetime(2015, 1, 1),
                'PreferredMaintenanceWindow': 'string',
                'TopicArn': 'string',
                'Port': 123,
                'CacheParameterGroupName': 'string',
                'CacheSubnetGroupName': 'string',
                'VpcId': 'string',
                'AutoMinorVersionUpgrade': True|False,
                'SnapshotRetentionLimit': 123,
                'SnapshotWindow': 'string',
                'NumNodeGroups': 123,
                'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                'NodeSnapshots': [
                    {
                        'CacheClusterId': 'string',
                        'NodeGroupId': 'string',
                        'CacheNodeId': 'string',
                        'NodeGroupConfiguration': {
                            'Slots': 'string',
                            'ReplicaCount': 123,
                            'PrimaryAvailabilityZone': 'string',
                            'ReplicaAvailabilityZones': [
                                'string',
                            ]
                        },
                        'CacheSize': 'string',
                        'CacheNodeCreateTime': datetime(2015, 1, 1),
                        'SnapshotCreateTime': datetime(2015, 1, 1)
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Snapshot** *(dict) --* 

          Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.

          
          

          - **SnapshotName** *(string) --* 

            The name of a snapshot. For an automatic snapshot, the name is system-generated. For a manual snapshot, this is the user-provided name.

            
          

          - **ReplicationGroupId** *(string) --* 

            The unique identifier of the source replication group.

            
          

          - **ReplicationGroupDescription** *(string) --* 

            A description of the source replication group.

            
          

          - **CacheClusterId** *(string) --* 

            The user-supplied identifier of the source cluster.

            
          

          - **SnapshotStatus** *(string) --* 

            The status of the snapshot. Valid values: ``creating`` | ``available`` | ``restoring`` | ``copying`` | ``deleting`` .

            
          

          - **SnapshotSource** *(string) --* 

            Indicates whether the snapshot is from an automatic backup (``automated`` ) or was created manually (``manual`` ).

            
          

          - **CacheNodeType** *(string) --* 

            The name of the compute and memory capacity node type for the source cluster.

             

            The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

             

             
            * General purpose: 

               
              * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
               
              * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
               

             
             
            * Compute optimized: 

               
              * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
               

             
             
            * Memory optimized: 

               
              * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
               
              * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
               

             
             

             

             **Notes:**  

             

             
            * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
             
            * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
             
            * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
             
            * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
             

             

            For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

            
          

          - **Engine** *(string) --* 

            The name of the cache engine (``memcached`` or ``redis`` ) used by the source cluster.

            
          

          - **EngineVersion** *(string) --* 

            The version of the cache engine version that is used by the source cluster.

            
          

          - **NumCacheNodes** *(integer) --* 

            The number of cache nodes in the source cluster.

             

            For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

            
          

          - **PreferredAvailabilityZone** *(string) --* 

            The name of the Availability Zone in which the source cluster is located.

            
          

          - **CacheClusterCreateTime** *(datetime) --* 

            The date and time when the source cluster was created.

            
          

          - **PreferredMaintenanceWindow** *(string) --* 

            Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.

             

            Valid values for ``ddd`` are:

             

             
            * ``sun``   
             
            * ``mon``   
             
            * ``tue``   
             
            * ``wed``   
             
            * ``thu``   
             
            * ``fri``   
             
            * ``sat``   
             

             

            Example: ``sun:23:00-mon:01:30``  

            
          

          - **TopicArn** *(string) --* 

            The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing notifications.

            
          

          - **Port** *(integer) --* 

            The port number used by each cache nodes in the source cluster.

            
          

          - **CacheParameterGroupName** *(string) --* 

            The cache parameter group that is associated with the source cluster.

            
          

          - **CacheSubnetGroupName** *(string) --* 

            The name of the cache subnet group associated with the source cluster.

            
          

          - **VpcId** *(string) --* 

            The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the source cluster.

            
          

          - **AutoMinorVersionUpgrade** *(boolean) --* 

            This parameter is currently disabled.

            
          

          - **SnapshotRetentionLimit** *(integer) --* 

            For an automatic snapshot, the number of days for which ElastiCache retains the snapshot before deleting it.

             

            For manual snapshots, this field reflects the ``SnapshotRetentionLimit`` for the source cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots do not expire, and can only be deleted using the ``DeleteSnapshot`` operation. 

             

             **Important** If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

            
          

          - **SnapshotWindow** *(string) --* 

            The daily time range during which ElastiCache takes daily snapshots of the source cluster.

            
          

          - **NumNodeGroups** *(integer) --* 

            The number of node groups (shards) in this snapshot. When restoring from a snapshot, the number of node groups (shards) in the snapshot and in the restored replication group must be the same.

            
          

          - **AutomaticFailover** *(string) --* 

            Indicates the status of Multi-AZ with automatic failover for the source Redis replication group.

             

            Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

             

             
            * Redis versions earlier than 2.8.6. 
             
            * Redis (cluster mode disabled): T1 and T2 cache node types. 
             
            * Redis (cluster mode enabled): T1 node types. 
             

            
          

          - **NodeSnapshots** *(list) --* 

            A list of the cache nodes in the source cluster.

            
            

            - *(dict) --* 

              Represents an individual cache node in a snapshot of a cluster.

              
              

              - **CacheClusterId** *(string) --* 

                A unique identifier for the source cluster.

                
              

              - **NodeGroupId** *(string) --* 

                A unique identifier for the source node group (shard).

                
              

              - **CacheNodeId** *(string) --* 

                The cache node identifier for the node in the source cluster.

                
              

              - **NodeGroupConfiguration** *(dict) --* 

                The configuration for the source node group (shard).

                
                

                - **Slots** *(string) --* 

                  A string that specifies the keyspace for a particular node group. Keyspaces range from 0 to 16,383. The string is in the format ``startkey-endkey`` .

                   

                  Example: ``"0-3999"``  

                  
                

                - **ReplicaCount** *(integer) --* 

                  The number of read replica nodes in this node group (shard).

                  
                

                - **PrimaryAvailabilityZone** *(string) --* 

                  The Availability Zone where the primary node of this node group (shard) is launched.

                  
                

                - **ReplicaAvailabilityZones** *(list) --* 

                  A list of Availability Zones to be used for the read replicas. The number of Availability Zones in this list must match the value of ``ReplicaCount`` or ``ReplicasPerNodeGroup`` if not specified.

                  
                  

                  - *(string) --* 
              
            
              

              - **CacheSize** *(string) --* 

                The size of the cache on the source cache node.

                
              

              - **CacheNodeCreateTime** *(datetime) --* 

                The date and time when the cache node was created in the source cluster.

                
              

              - **SnapshotCreateTime** *(datetime) --* 

                The date and time when the source node's metadata and cache data set was obtained for the snapshot.

                
          
        
      
    

  .. py:method:: describe_cache_clusters(**kwargs)

    

    Returns information about all provisioned clusters if no cluster identifier is specified, or about a specific cache cluster if a cluster identifier is supplied.

     

    By default, abbreviated information about the clusters is returned. You can use the optional *ShowCacheNodeInfo* flag to retrieve detailed information about the cache nodes associated with the clusters. These details include the DNS address and port for the cache node endpoint.

     

    If the cluster is in the *creating* state, only cluster-level information is displayed until all of the nodes are successfully provisioned.

     

    If the cluster is in the *deleting* state, only cluster-level information is displayed.

     

    If cache nodes are currently being added to the cluster, node endpoint information and creation time for the additional nodes are not displayed until they are completely provisioned. When the cluster state is *available* , the cluster is ready for use.

     

    If cache nodes are currently being removed from the cluster, no endpoint information for the removed nodes is displayed.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheClusters>`_    


    **Request Syntax** 
    ::

      response = client.describe_cache_clusters(
          CacheClusterId='string',
          MaxRecords=123,
          Marker='string',
          ShowCacheNodeInfo=True|False,
          ShowCacheClustersNotInReplicationGroups=True|False
      )
    :type CacheClusterId: string
    :param CacheClusterId: 

      The user-supplied cluster identifier. If this parameter is specified, only information about that specific cluster is returned. This parameter isn't case sensitive.

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a marker is included in the response so that the remaining results can be retrieved.

       

      Default: 100

       

      Constraints: minimum 20; maximum 100.

      

    
    :type Marker: string
    :param Marker: 

      An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

      

    
    :type ShowCacheNodeInfo: boolean
    :param ShowCacheNodeInfo: 

      An optional flag that can be included in the ``DescribeCacheCluster`` request to retrieve information about the individual cache nodes.

      

    
    :type ShowCacheClustersNotInReplicationGroups: boolean
    :param ShowCacheClustersNotInReplicationGroups: 

      An optional flag that can be included in the ``DescribeCacheCluster`` request to show only nodes (API/CLI: clusters) that are not members of a replication group. In practice, this mean Memcached and single node Redis clusters.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Marker': 'string',
            'CacheClusters': [
                {
                    'CacheClusterId': 'string',
                    'ConfigurationEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'ClientDownloadLandingPage': 'string',
                    'CacheNodeType': 'string',
                    'Engine': 'string',
                    'EngineVersion': 'string',
                    'CacheClusterStatus': 'string',
                    'NumCacheNodes': 123,
                    'PreferredAvailabilityZone': 'string',
                    'CacheClusterCreateTime': datetime(2015, 1, 1),
                    'PreferredMaintenanceWindow': 'string',
                    'PendingModifiedValues': {
                        'NumCacheNodes': 123,
                        'CacheNodeIdsToRemove': [
                            'string',
                        ],
                        'EngineVersion': 'string',
                        'CacheNodeType': 'string'
                    },
                    'NotificationConfiguration': {
                        'TopicArn': 'string',
                        'TopicStatus': 'string'
                    },
                    'CacheSecurityGroups': [
                        {
                            'CacheSecurityGroupName': 'string',
                            'Status': 'string'
                        },
                    ],
                    'CacheParameterGroup': {
                        'CacheParameterGroupName': 'string',
                        'ParameterApplyStatus': 'string',
                        'CacheNodeIdsToReboot': [
                            'string',
                        ]
                    },
                    'CacheSubnetGroupName': 'string',
                    'CacheNodes': [
                        {
                            'CacheNodeId': 'string',
                            'CacheNodeStatus': 'string',
                            'CacheNodeCreateTime': datetime(2015, 1, 1),
                            'Endpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'ParameterGroupStatus': 'string',
                            'SourceCacheNodeId': 'string',
                            'CustomerAvailabilityZone': 'string'
                        },
                    ],
                    'AutoMinorVersionUpgrade': True|False,
                    'SecurityGroups': [
                        {
                            'SecurityGroupId': 'string',
                            'Status': 'string'
                        },
                    ],
                    'ReplicationGroupId': 'string',
                    'SnapshotRetentionLimit': 123,
                    'SnapshotWindow': 'string',
                    'AuthTokenEnabled': True|False,
                    'TransitEncryptionEnabled': True|False,
                    'AtRestEncryptionEnabled': True|False
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DescribeCacheClusters`` operation.

        
        

        - **Marker** *(string) --* 

          Provides an identifier to allow retrieval of paginated results.

          
        

        - **CacheClusters** *(list) --* 

          A list of clusters. Each item in the list contains detailed information about one cluster.

          
          

          - *(dict) --* 

            Contains all of the attributes of a specific cluster.

            
            

            - **CacheClusterId** *(string) --* 

              The user-supplied identifier of the cluster. This identifier is a unique key that identifies a cluster.

              
            

            - **ConfigurationEndpoint** *(dict) --* 

              Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the cluster, can be used by an application to connect to any node in the cluster. The configuration endpoint will always have ``.cfg`` in it.

               

              Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``  

              
              

              - **Address** *(string) --* 

                The DNS hostname of the cache node.

                
              

              - **Port** *(integer) --* 

                The port number that the cache engine is listening on.

                
          
            

            - **ClientDownloadLandingPage** *(string) --* 

              The URL of the web page where you can download the latest ElastiCache client library.

              
            

            - **CacheNodeType** *(string) --* 

              The name of the compute and memory capacity node type for the cluster.

               

              The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

               

               
              * General purpose: 

                 
                * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
                 
                * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
                 

               
               
              * Compute optimized: 

                 
                * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
                 

               
               
              * Memory optimized: 

                 
                * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
                 
                * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
                 

               
               

               

               **Notes:**  

               

               
              * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
               
              * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
               
              * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
               
              * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
               

               

              For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

              
            

            - **Engine** *(string) --* 

              The name of the cache engine (``memcached`` or ``redis`` ) to be used for this cluster.

              
            

            - **EngineVersion** *(string) --* 

              The version of the cache engine that is used in this cluster.

              
            

            - **CacheClusterStatus** *(string) --* 

              The current state of this cluster, one of the following values: ``available`` , ``creating`` , ``deleted`` , ``deleting`` , ``incompatible-network`` , ``modifying`` , ``rebooting cluster nodes`` , ``restore-failed`` , or ``snapshotting`` .

              
            

            - **NumCacheNodes** *(integer) --* 

              The number of cache nodes in the cluster.

               

              For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

              
            

            - **PreferredAvailabilityZone** *(string) --* 

              The name of the Availability Zone in which the cluster is located or "Multiple" if the cache nodes are located in different Availability Zones.

              
            

            - **CacheClusterCreateTime** *(datetime) --* 

              The date and time when the cluster was created.

              
            

            - **PreferredMaintenanceWindow** *(string) --* 

              Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.

               

              Valid values for ``ddd`` are:

               

               
              * ``sun``   
               
              * ``mon``   
               
              * ``tue``   
               
              * ``wed``   
               
              * ``thu``   
               
              * ``fri``   
               
              * ``sat``   
               

               

              Example: ``sun:23:00-mon:01:30``  

              
            

            - **PendingModifiedValues** *(dict) --* 

              A group of settings that are applied to the cluster in the future, or that are currently being applied.

              
              

              - **NumCacheNodes** *(integer) --* 

                The new number of cache nodes for the cluster.

                 

                For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

                
              

              - **CacheNodeIdsToRemove** *(list) --* 

                A list of cache node IDs that are being removed (or will be removed) from the cluster. A node ID is a numeric identifier (0001, 0002, etc.).

                
                

                - *(string) --* 
            
              

              - **EngineVersion** *(string) --* 

                The new cache engine version that the cluster runs.

                
              

              - **CacheNodeType** *(string) --* 

                The cache node type that this cluster or replication group is scaled to.

                
          
            

            - **NotificationConfiguration** *(dict) --* 

              Describes a notification topic and its status. Notification topics are used for publishing ElastiCache events to subscribers using Amazon Simple Notification Service (SNS). 

              
              

              - **TopicArn** *(string) --* 

                The Amazon Resource Name (ARN) that identifies the topic.

                
              

              - **TopicStatus** *(string) --* 

                The current state of the topic.

                
          
            

            - **CacheSecurityGroups** *(list) --* 

              A list of cache security group elements, composed of name and status sub-elements.

              
              

              - *(dict) --* 

                Represents a cluster's status within a particular cache security group.

                
                

                - **CacheSecurityGroupName** *(string) --* 

                  The name of the cache security group.

                  
                

                - **Status** *(string) --* 

                  The membership status in the cache security group. The status changes when a cache security group is modified, or when the cache security groups assigned to a cluster are modified.

                  
            
          
            

            - **CacheParameterGroup** *(dict) --* 

              Status of the cache parameter group.

              
              

              - **CacheParameterGroupName** *(string) --* 

                The name of the cache parameter group.

                
              

              - **ParameterApplyStatus** *(string) --* 

                The status of parameter updates.

                
              

              - **CacheNodeIdsToReboot** *(list) --* 

                A list of the cache node IDs which need to be rebooted for parameter changes to be applied. A node ID is a numeric identifier (0001, 0002, etc.).

                
                

                - *(string) --* 
            
          
            

            - **CacheSubnetGroupName** *(string) --* 

              The name of the cache subnet group associated with the cluster.

              
            

            - **CacheNodes** *(list) --* 

              A list of cache nodes that are members of the cluster.

              
              

              - *(dict) --* 

                Represents an individual cache node within a cluster. Each cache node runs its own instance of the cluster's protocol-compliant caching software - either Memcached or Redis.

                 

                The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

                 

                 
                * General purpose: 

                   
                  * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
                   
                  * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
                   

                 
                 
                * Compute optimized: 

                   
                  * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
                   

                 
                 
                * Memory optimized: 

                   
                  * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
                   
                  * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
                   

                 
                 

                 

                 **Notes:**  

                 

                 
                * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
                 
                * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
                 
                * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
                 
                * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
                 

                 

                For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

                
                

                - **CacheNodeId** *(string) --* 

                  The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The combination of cluster ID and node ID uniquely identifies every cache node used in a customer's AWS account.

                  
                

                - **CacheNodeStatus** *(string) --* 

                  The current state of this cache node.

                  
                

                - **CacheNodeCreateTime** *(datetime) --* 

                  The date and time when the cache node was created.

                  
                

                - **Endpoint** *(dict) --* 

                  The hostname for connecting to this cache node.

                  
                  

                  - **Address** *(string) --* 

                    The DNS hostname of the cache node.

                    
                  

                  - **Port** *(integer) --* 

                    The port number that the cache engine is listening on.

                    
              
                

                - **ParameterGroupStatus** *(string) --* 

                  The status of the parameter group applied to this cache node.

                  
                

                - **SourceCacheNodeId** *(string) --* 

                  The ID of the primary node to which this read replica node is synchronized. If this field is empty, this node is not associated with a primary cluster.

                  
                

                - **CustomerAvailabilityZone** *(string) --* 

                  The Availability Zone where this node was created and now resides.

                  
            
          
            

            - **AutoMinorVersionUpgrade** *(boolean) --* 

              This parameter is currently disabled.

              
            

            - **SecurityGroups** *(list) --* 

              A list of VPC Security Groups associated with the cluster.

              
              

              - *(dict) --* 

                Represents a single cache security group and its status.

                
                

                - **SecurityGroupId** *(string) --* 

                  The identifier of the cache security group.

                  
                

                - **Status** *(string) --* 

                  The status of the cache security group membership. The status changes whenever a cache security group is modified, or when the cache security groups assigned to a cluster are modified.

                  
            
          
            

            - **ReplicationGroupId** *(string) --* 

              The replication group to which this cluster belongs. If this field is empty, the cluster is not associated with any replication group.

              
            

            - **SnapshotRetentionLimit** *(integer) --* 

              The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was taken today is retained for 5 days before being deleted.

               

              .. warning::

                 

                If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

                 

              
            

            - **SnapshotWindow** *(string) --* 

              The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your cluster.

               

              Example: ``05:00-09:00``  

              
            

            - **AuthTokenEnabled** *(boolean) --* 

              A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

               

              Default: ``false``  

              
            

            - **TransitEncryptionEnabled** *(boolean) --* 

              A flag that enables in-transit encryption when set to ``true`` .

               

              You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created. To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to ``true`` when you create a cluster.

               

              Default: ``false``  

              
            

            - **AtRestEncryptionEnabled** *(boolean) --* 

              A flag that enables encryption at-rest when set to ``true`` .

               

              You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To enable at-rest encryption on a cluster you must set ``AtRestEncryptionEnabled`` to ``true`` when you create a cluster.

               

              Default: ``false``  

              
        
      
    

  .. py:method:: describe_cache_engine_versions(**kwargs)

    

    Returns a list of the available cache engines and their versions.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheEngineVersions>`_    


    **Request Syntax** 
    ::

      response = client.describe_cache_engine_versions(
          Engine='string',
          EngineVersion='string',
          CacheParameterGroupFamily='string',
          MaxRecords=123,
          Marker='string',
          DefaultOnly=True|False
      )
    :type Engine: string
    :param Engine: 

      The cache engine to return. Valid values: ``memcached`` | ``redis``  

      

    
    :type EngineVersion: string
    :param EngineVersion: 

      The cache engine version to return.

       

      Example: ``1.4.14``  

      

    
    :type CacheParameterGroupFamily: string
    :param CacheParameterGroupFamily: 

      The name of a specific cache parameter group family to return details for.

       

      Valid values are: ``memcached1.4`` | ``redis2.6`` | ``redis2.8`` | ``redis3.2``  

       

      Constraints:

       

       
      * Must be 1 to 255 alphanumeric characters 
       
      * First character must be a letter 
       
      * Cannot end with a hyphen or contain two consecutive hyphens 
       

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a marker is included in the response so that the remaining results can be retrieved.

       

      Default: 100

       

      Constraints: minimum 20; maximum 100.

      

    
    :type Marker: string
    :param Marker: 

      An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

      

    
    :type DefaultOnly: boolean
    :param DefaultOnly: 

      If ``true`` , specifies that only the default version of the specified engine or engine and major version combination is to be returned.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Marker': 'string',
            'CacheEngineVersions': [
                {
                    'Engine': 'string',
                    'EngineVersion': 'string',
                    'CacheParameterGroupFamily': 'string',
                    'CacheEngineDescription': 'string',
                    'CacheEngineVersionDescription': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a  DescribeCacheEngineVersions operation.

        
        

        - **Marker** *(string) --* 

          Provides an identifier to allow retrieval of paginated results.

          
        

        - **CacheEngineVersions** *(list) --* 

          A list of cache engine version details. Each element in the list contains detailed information about one cache engine version.

          
          

          - *(dict) --* 

            Provides all of the details about a particular cache engine version.

            
            

            - **Engine** *(string) --* 

              The name of the cache engine.

              
            

            - **EngineVersion** *(string) --* 

              The version number of the cache engine.

              
            

            - **CacheParameterGroupFamily** *(string) --* 

              The name of the cache parameter group family associated with this cache engine.

               

              Valid values are: ``memcached1.4`` | ``redis2.6`` | ``redis2.8`` | ``redis3.2``  

              
            

            - **CacheEngineDescription** *(string) --* 

              The description of the cache engine.

              
            

            - **CacheEngineVersionDescription** *(string) --* 

              The description of the cache engine version.

              
        
      
    

  .. py:method:: describe_cache_parameter_groups(**kwargs)

    

    Returns a list of cache parameter group descriptions. If a cache parameter group name is specified, the list contains only the descriptions for that group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheParameterGroups>`_    


    **Request Syntax** 
    ::

      response = client.describe_cache_parameter_groups(
          CacheParameterGroupName='string',
          MaxRecords=123,
          Marker='string'
      )
    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: 

      The name of a specific cache parameter group to return details for.

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a marker is included in the response so that the remaining results can be retrieved.

       

      Default: 100

       

      Constraints: minimum 20; maximum 100.

      

    
    :type Marker: string
    :param Marker: 

      An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Marker': 'string',
            'CacheParameterGroups': [
                {
                    'CacheParameterGroupName': 'string',
                    'CacheParameterGroupFamily': 'string',
                    'Description': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DescribeCacheParameterGroups`` operation.

        
        

        - **Marker** *(string) --* 

          Provides an identifier to allow retrieval of paginated results.

          
        

        - **CacheParameterGroups** *(list) --* 

          A list of cache parameter groups. Each element in the list contains detailed information about one cache parameter group.

          
          

          - *(dict) --* 

            Represents the output of a ``CreateCacheParameterGroup`` operation.

            
            

            - **CacheParameterGroupName** *(string) --* 

              The name of the cache parameter group.

              
            

            - **CacheParameterGroupFamily** *(string) --* 

              The name of the cache parameter group family that this cache parameter group is compatible with.

               

              Valid values are: ``memcached1.4`` | ``redis2.6`` | ``redis2.8`` | ``redis3.2``  

              
            

            - **Description** *(string) --* 

              The description for this cache parameter group.

              
        
      
    

  .. py:method:: describe_cache_parameters(**kwargs)

    

    Returns the detailed parameter list for a particular cache parameter group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheParameters>`_    


    **Request Syntax** 
    ::

      response = client.describe_cache_parameters(
          CacheParameterGroupName='string',
          Source='string',
          MaxRecords=123,
          Marker='string'
      )
    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: **[REQUIRED]** 

      The name of a specific cache parameter group to return details for.

      

    
    :type Source: string
    :param Source: 

      The parameter types to return.

       

      Valid values: ``user`` | ``system`` | ``engine-default``  

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a marker is included in the response so that the remaining results can be retrieved.

       

      Default: 100

       

      Constraints: minimum 20; maximum 100.

      

    
    :type Marker: string
    :param Marker: 

      An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Marker': 'string',
            'Parameters': [
                {
                    'ParameterName': 'string',
                    'ParameterValue': 'string',
                    'Description': 'string',
                    'Source': 'string',
                    'DataType': 'string',
                    'AllowedValues': 'string',
                    'IsModifiable': True|False,
                    'MinimumEngineVersion': 'string',
                    'ChangeType': 'immediate'|'requires-reboot'
                },
            ],
            'CacheNodeTypeSpecificParameters': [
                {
                    'ParameterName': 'string',
                    'Description': 'string',
                    'Source': 'string',
                    'DataType': 'string',
                    'AllowedValues': 'string',
                    'IsModifiable': True|False,
                    'MinimumEngineVersion': 'string',
                    'CacheNodeTypeSpecificValues': [
                        {
                            'CacheNodeType': 'string',
                            'Value': 'string'
                        },
                    ],
                    'ChangeType': 'immediate'|'requires-reboot'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DescribeCacheParameters`` operation.

        
        

        - **Marker** *(string) --* 

          Provides an identifier to allow retrieval of paginated results.

          
        

        - **Parameters** *(list) --* 

          A list of  Parameter instances.

          
          

          - *(dict) --* 

            Describes an individual setting that controls some aspect of ElastiCache behavior.

            
            

            - **ParameterName** *(string) --* 

              The name of the parameter.

              
            

            - **ParameterValue** *(string) --* 

              The value of the parameter.

              
            

            - **Description** *(string) --* 

              A description of the parameter.

              
            

            - **Source** *(string) --* 

              The source of the parameter.

              
            

            - **DataType** *(string) --* 

              The valid data type for the parameter.

              
            

            - **AllowedValues** *(string) --* 

              The valid range of values for the parameter.

              
            

            - **IsModifiable** *(boolean) --* 

              Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.

              
            

            - **MinimumEngineVersion** *(string) --* 

              The earliest cache engine version to which the parameter can apply.

              
            

            - **ChangeType** *(string) --* 

              Indicates whether a change to the parameter is applied immediately or requires a reboot for the change to be applied. You can force a reboot or wait until the next maintenance window's reboot. For more information, see `Rebooting a Cluster <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Clusters.Rebooting.html>`__ .

              
        
      
        

        - **CacheNodeTypeSpecificParameters** *(list) --* 

          A list of parameters specific to a particular cache node type. Each element in the list contains detailed information about one parameter.

          
          

          - *(dict) --* 

            A parameter that has a different value for each cache node type it is applied to. For example, in a Redis cluster, a ``cache.m1.large`` cache node type would have a larger ``maxmemory`` value than a ``cache.m1.small`` type.

            
            

            - **ParameterName** *(string) --* 

              The name of the parameter.

              
            

            - **Description** *(string) --* 

              A description of the parameter.

              
            

            - **Source** *(string) --* 

              The source of the parameter value.

              
            

            - **DataType** *(string) --* 

              The valid data type for the parameter.

              
            

            - **AllowedValues** *(string) --* 

              The valid range of values for the parameter.

              
            

            - **IsModifiable** *(boolean) --* 

              Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.

              
            

            - **MinimumEngineVersion** *(string) --* 

              The earliest cache engine version to which the parameter can apply.

              
            

            - **CacheNodeTypeSpecificValues** *(list) --* 

              A list of cache node types and their corresponding values for this parameter.

              
              

              - *(dict) --* 

                A value that applies only to a certain cache node type.

                
                

                - **CacheNodeType** *(string) --* 

                  The cache node type for which this value applies.

                  
                

                - **Value** *(string) --* 

                  The value for the cache node type.

                  
            
          
            

            - **ChangeType** *(string) --* 

              Indicates whether a change to the parameter is applied immediately or requires a reboot for the change to be applied. You can force a reboot or wait until the next maintenance window's reboot. For more information, see `Rebooting a Cluster <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Clusters.Rebooting.html>`__ .

              
        
      
    

  .. py:method:: describe_cache_security_groups(**kwargs)

    

    Returns a list of cache security group descriptions. If a cache security group name is specified, the list contains only the description of that group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheSecurityGroups>`_    


    **Request Syntax** 
    ::

      response = client.describe_cache_security_groups(
          CacheSecurityGroupName='string',
          MaxRecords=123,
          Marker='string'
      )
    :type CacheSecurityGroupName: string
    :param CacheSecurityGroupName: 

      The name of the cache security group to return details for.

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a marker is included in the response so that the remaining results can be retrieved.

       

      Default: 100

       

      Constraints: minimum 20; maximum 100.

      

    
    :type Marker: string
    :param Marker: 

      An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Marker': 'string',
            'CacheSecurityGroups': [
                {
                    'OwnerId': 'string',
                    'CacheSecurityGroupName': 'string',
                    'Description': 'string',
                    'EC2SecurityGroups': [
                        {
                            'Status': 'string',
                            'EC2SecurityGroupName': 'string',
                            'EC2SecurityGroupOwnerId': 'string'
                        },
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DescribeCacheSecurityGroups`` operation.

        
        

        - **Marker** *(string) --* 

          Provides an identifier to allow retrieval of paginated results.

          
        

        - **CacheSecurityGroups** *(list) --* 

          A list of cache security groups. Each element in the list contains detailed information about one group.

          
          

          - *(dict) --* 

            Represents the output of one of the following operations:

             

             
            * ``AuthorizeCacheSecurityGroupIngress``   
             
            * ``CreateCacheSecurityGroup``   
             
            * ``RevokeCacheSecurityGroupIngress``   
             

            
            

            - **OwnerId** *(string) --* 

              The AWS account ID of the cache security group owner.

              
            

            - **CacheSecurityGroupName** *(string) --* 

              The name of the cache security group.

              
            

            - **Description** *(string) --* 

              The description of the cache security group.

              
            

            - **EC2SecurityGroups** *(list) --* 

              A list of Amazon EC2 security groups that are associated with this cache security group.

              
              

              - *(dict) --* 

                Provides ownership and status information for an Amazon EC2 security group.

                
                

                - **Status** *(string) --* 

                  The status of the Amazon EC2 security group.

                  
                

                - **EC2SecurityGroupName** *(string) --* 

                  The name of the Amazon EC2 security group.

                  
                

                - **EC2SecurityGroupOwnerId** *(string) --* 

                  The AWS account ID of the Amazon EC2 security group owner.

                  
            
          
        
      
    

  .. py:method:: describe_cache_subnet_groups(**kwargs)

    

    Returns a list of cache subnet group descriptions. If a subnet group name is specified, the list contains only the description of that group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheSubnetGroups>`_    


    **Request Syntax** 
    ::

      response = client.describe_cache_subnet_groups(
          CacheSubnetGroupName='string',
          MaxRecords=123,
          Marker='string'
      )
    :type CacheSubnetGroupName: string
    :param CacheSubnetGroupName: 

      The name of the cache subnet group to return details for.

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a marker is included in the response so that the remaining results can be retrieved.

       

      Default: 100

       

      Constraints: minimum 20; maximum 100.

      

    
    :type Marker: string
    :param Marker: 

      An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Marker': 'string',
            'CacheSubnetGroups': [
                {
                    'CacheSubnetGroupName': 'string',
                    'CacheSubnetGroupDescription': 'string',
                    'VpcId': 'string',
                    'Subnets': [
                        {
                            'SubnetIdentifier': 'string',
                            'SubnetAvailabilityZone': {
                                'Name': 'string'
                            }
                        },
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DescribeCacheSubnetGroups`` operation.

        
        

        - **Marker** *(string) --* 

          Provides an identifier to allow retrieval of paginated results.

          
        

        - **CacheSubnetGroups** *(list) --* 

          A list of cache subnet groups. Each element in the list contains detailed information about one group.

          
          

          - *(dict) --* 

            Represents the output of one of the following operations:

             

             
            * ``CreateCacheSubnetGroup``   
             
            * ``ModifyCacheSubnetGroup``   
             

            
            

            - **CacheSubnetGroupName** *(string) --* 

              The name of the cache subnet group.

              
            

            - **CacheSubnetGroupDescription** *(string) --* 

              The description of the cache subnet group.

              
            

            - **VpcId** *(string) --* 

              The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group.

              
            

            - **Subnets** *(list) --* 

              A list of subnets associated with the cache subnet group.

              
              

              - *(dict) --* 

                Represents the subnet associated with a cluster. This parameter refers to subnets defined in Amazon Virtual Private Cloud (Amazon VPC) and used with ElastiCache.

                
                

                - **SubnetIdentifier** *(string) --* 

                  The unique identifier for the subnet.

                  
                

                - **SubnetAvailabilityZone** *(dict) --* 

                  The Availability Zone associated with the subnet.

                  
                  

                  - **Name** *(string) --* 

                    The name of the Availability Zone.

                    
              
            
          
        
      
    

  .. py:method:: describe_engine_default_parameters(**kwargs)

    

    Returns the default engine and system parameter information for the specified cache engine.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeEngineDefaultParameters>`_    


    **Request Syntax** 
    ::

      response = client.describe_engine_default_parameters(
          CacheParameterGroupFamily='string',
          MaxRecords=123,
          Marker='string'
      )
    :type CacheParameterGroupFamily: string
    :param CacheParameterGroupFamily: **[REQUIRED]** 

      The name of the cache parameter group family.

       

      Valid values are: ``memcached1.4`` | ``redis2.6`` | ``redis2.8`` | ``redis3.2``  

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a marker is included in the response so that the remaining results can be retrieved.

       

      Default: 100

       

      Constraints: minimum 20; maximum 100.

      

    
    :type Marker: string
    :param Marker: 

      An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'EngineDefaults': {
                'CacheParameterGroupFamily': 'string',
                'Marker': 'string',
                'Parameters': [
                    {
                        'ParameterName': 'string',
                        'ParameterValue': 'string',
                        'Description': 'string',
                        'Source': 'string',
                        'DataType': 'string',
                        'AllowedValues': 'string',
                        'IsModifiable': True|False,
                        'MinimumEngineVersion': 'string',
                        'ChangeType': 'immediate'|'requires-reboot'
                    },
                ],
                'CacheNodeTypeSpecificParameters': [
                    {
                        'ParameterName': 'string',
                        'Description': 'string',
                        'Source': 'string',
                        'DataType': 'string',
                        'AllowedValues': 'string',
                        'IsModifiable': True|False,
                        'MinimumEngineVersion': 'string',
                        'CacheNodeTypeSpecificValues': [
                            {
                                'CacheNodeType': 'string',
                                'Value': 'string'
                            },
                        ],
                        'ChangeType': 'immediate'|'requires-reboot'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **EngineDefaults** *(dict) --* 

          Represents the output of a ``DescribeEngineDefaultParameters`` operation.

          
          

          - **CacheParameterGroupFamily** *(string) --* 

            Specifies the name of the cache parameter group family to which the engine default parameters apply.

             

            Valid values are: ``memcached1.4`` | ``redis2.6`` | ``redis2.8`` | ``redis3.2``  

            
          

          - **Marker** *(string) --* 

            Provides an identifier to allow retrieval of paginated results.

            
          

          - **Parameters** *(list) --* 

            Contains a list of engine default parameters.

            
            

            - *(dict) --* 

              Describes an individual setting that controls some aspect of ElastiCache behavior.

              
              

              - **ParameterName** *(string) --* 

                The name of the parameter.

                
              

              - **ParameterValue** *(string) --* 

                The value of the parameter.

                
              

              - **Description** *(string) --* 

                A description of the parameter.

                
              

              - **Source** *(string) --* 

                The source of the parameter.

                
              

              - **DataType** *(string) --* 

                The valid data type for the parameter.

                
              

              - **AllowedValues** *(string) --* 

                The valid range of values for the parameter.

                
              

              - **IsModifiable** *(boolean) --* 

                Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.

                
              

              - **MinimumEngineVersion** *(string) --* 

                The earliest cache engine version to which the parameter can apply.

                
              

              - **ChangeType** *(string) --* 

                Indicates whether a change to the parameter is applied immediately or requires a reboot for the change to be applied. You can force a reboot or wait until the next maintenance window's reboot. For more information, see `Rebooting a Cluster <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Clusters.Rebooting.html>`__ .

                
          
        
          

          - **CacheNodeTypeSpecificParameters** *(list) --* 

            A list of parameters specific to a particular cache node type. Each element in the list contains detailed information about one parameter.

            
            

            - *(dict) --* 

              A parameter that has a different value for each cache node type it is applied to. For example, in a Redis cluster, a ``cache.m1.large`` cache node type would have a larger ``maxmemory`` value than a ``cache.m1.small`` type.

              
              

              - **ParameterName** *(string) --* 

                The name of the parameter.

                
              

              - **Description** *(string) --* 

                A description of the parameter.

                
              

              - **Source** *(string) --* 

                The source of the parameter value.

                
              

              - **DataType** *(string) --* 

                The valid data type for the parameter.

                
              

              - **AllowedValues** *(string) --* 

                The valid range of values for the parameter.

                
              

              - **IsModifiable** *(boolean) --* 

                Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.

                
              

              - **MinimumEngineVersion** *(string) --* 

                The earliest cache engine version to which the parameter can apply.

                
              

              - **CacheNodeTypeSpecificValues** *(list) --* 

                A list of cache node types and their corresponding values for this parameter.

                
                

                - *(dict) --* 

                  A value that applies only to a certain cache node type.

                  
                  

                  - **CacheNodeType** *(string) --* 

                    The cache node type for which this value applies.

                    
                  

                  - **Value** *(string) --* 

                    The value for the cache node type.

                    
              
            
              

              - **ChangeType** *(string) --* 

                Indicates whether a change to the parameter is applied immediately or requires a reboot for the change to be applied. You can force a reboot or wait until the next maintenance window's reboot. For more information, see `Rebooting a Cluster <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Clusters.Rebooting.html>`__ .

                
          
        
      
    

  .. py:method:: describe_events(**kwargs)

    

    Returns events related to clusters, cache security groups, and cache parameter groups. You can obtain events specific to a particular cluster, cache security group, or cache parameter group by providing the name as a parameter.

     

    By default, only the events occurring within the last hour are returned; however, you can retrieve up to 14 days' worth of events if necessary.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeEvents>`_    


    **Request Syntax** 
    ::

      response = client.describe_events(
          SourceIdentifier='string',
          SourceType='cache-cluster'|'cache-parameter-group'|'cache-security-group'|'cache-subnet-group'|'replication-group',
          StartTime=datetime(2015, 1, 1),
          EndTime=datetime(2015, 1, 1),
          Duration=123,
          MaxRecords=123,
          Marker='string'
      )
    :type SourceIdentifier: string
    :param SourceIdentifier: 

      The identifier of the event source for which events are returned. If not specified, all sources are included in the response.

      

    
    :type SourceType: string
    :param SourceType: 

      The event source to retrieve events for. If no value is specified, all events are returned.

      

    
    :type StartTime: datetime
    :param StartTime: 

      The beginning of the time interval to retrieve events for, specified in ISO 8601 format.

       

       **Example:** 2017-03-30T07:03:49.555Z

      

    
    :type EndTime: datetime
    :param EndTime: 

      The end of the time interval for which to retrieve events, specified in ISO 8601 format.

       

       **Example:** 2017-03-30T07:03:49.555Z

      

    
    :type Duration: integer
    :param Duration: 

      The number of minutes worth of events to retrieve.

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a marker is included in the response so that the remaining results can be retrieved.

       

      Default: 100

       

      Constraints: minimum 20; maximum 100.

      

    
    :type Marker: string
    :param Marker: 

      An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Marker': 'string',
            'Events': [
                {
                    'SourceIdentifier': 'string',
                    'SourceType': 'cache-cluster'|'cache-parameter-group'|'cache-security-group'|'cache-subnet-group'|'replication-group',
                    'Message': 'string',
                    'Date': datetime(2015, 1, 1)
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DescribeEvents`` operation.

        
        

        - **Marker** *(string) --* 

          Provides an identifier to allow retrieval of paginated results.

          
        

        - **Events** *(list) --* 

          A list of events. Each element in the list contains detailed information about one event.

          
          

          - *(dict) --* 

            Represents a single occurrence of something interesting within the system. Some examples of events are creating a cluster, adding or removing a cache node, or rebooting a node.

            
            

            - **SourceIdentifier** *(string) --* 

              The identifier for the source of the event. For example, if the event occurred at the cluster level, the identifier would be the name of the cluster.

              
            

            - **SourceType** *(string) --* 

              Specifies the origin of this event - a cluster, a parameter group, a security group, etc.

              
            

            - **Message** *(string) --* 

              The text of the event.

              
            

            - **Date** *(datetime) --* 

              The date and time when the event occurred.

              
        
      
    

  .. py:method:: describe_replication_groups(**kwargs)

    

    Returns information about a particular replication group. If no identifier is specified, ``DescribeReplicationGroups`` returns information about all replication groups.

     

    .. note::

       

      This operation is valid for Redis only.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeReplicationGroups>`_    


    **Request Syntax** 
    ::

      response = client.describe_replication_groups(
          ReplicationGroupId='string',
          MaxRecords=123,
          Marker='string'
      )
    :type ReplicationGroupId: string
    :param ReplicationGroupId: 

      The identifier for the replication group to be described. This parameter is not case sensitive.

       

      If you do not specify this parameter, information about all replication groups is returned.

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a marker is included in the response so that the remaining results can be retrieved.

       

      Default: 100

       

      Constraints: minimum 20; maximum 100.

      

    
    :type Marker: string
    :param Marker: 

      An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Marker': 'string',
            'ReplicationGroups': [
                {
                    'ReplicationGroupId': 'string',
                    'Description': 'string',
                    'Status': 'string',
                    'PendingModifiedValues': {
                        'PrimaryClusterId': 'string',
                        'AutomaticFailoverStatus': 'enabled'|'disabled',
                        'Resharding': {
                            'SlotMigration': {
                                'ProgressPercentage': 123.0
                            }
                        }
                    },
                    'MemberClusters': [
                        'string',
                    ],
                    'NodeGroups': [
                        {
                            'NodeGroupId': 'string',
                            'Status': 'string',
                            'PrimaryEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'Slots': 'string',
                            'NodeGroupMembers': [
                                {
                                    'CacheClusterId': 'string',
                                    'CacheNodeId': 'string',
                                    'ReadEndpoint': {
                                        'Address': 'string',
                                        'Port': 123
                                    },
                                    'PreferredAvailabilityZone': 'string',
                                    'CurrentRole': 'string'
                                },
                            ]
                        },
                    ],
                    'SnapshottingClusterId': 'string',
                    'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                    'ConfigurationEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'SnapshotRetentionLimit': 123,
                    'SnapshotWindow': 'string',
                    'ClusterEnabled': True|False,
                    'CacheNodeType': 'string',
                    'AuthTokenEnabled': True|False,
                    'TransitEncryptionEnabled': True|False,
                    'AtRestEncryptionEnabled': True|False
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DescribeReplicationGroups`` operation.

        
        

        - **Marker** *(string) --* 

          Provides an identifier to allow retrieval of paginated results.

          
        

        - **ReplicationGroups** *(list) --* 

          A list of replication groups. Each item in the list contains detailed information about one replication group.

          
          

          - *(dict) --* 

            Contains all of the attributes of a specific Redis replication group.

            
            

            - **ReplicationGroupId** *(string) --* 

              The identifier for the replication group.

              
            

            - **Description** *(string) --* 

              The user supplied description of the replication group.

              
            

            - **Status** *(string) --* 

              The current state of this replication group - ``creating`` , ``available`` , ``modifying`` , ``deleting`` , ``create-failed`` , ``snapshotting`` .

              
            

            - **PendingModifiedValues** *(dict) --* 

              A group of settings to be applied to the replication group, either immediately or during the next maintenance window.

              
              

              - **PrimaryClusterId** *(string) --* 

                The primary cluster ID that is applied immediately (if ``--apply-immediately`` was specified), or during the next maintenance window.

                
              

              - **AutomaticFailoverStatus** *(string) --* 

                Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

                 

                Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

                 

                 
                * Redis versions earlier than 2.8.6. 
                 
                * Redis (cluster mode disabled): T1 and T2 cache node types. 
                 
                * Redis (cluster mode enabled): T1 node types. 
                 

                
              

              - **Resharding** *(dict) --* 

                The status of an online resharding operation.

                
                

                - **SlotMigration** *(dict) --* 

                  Represents the progress of an online resharding operation.

                  
                  

                  - **ProgressPercentage** *(float) --* 

                    The percentage of the slot migration that is complete.

                    
              
            
          
            

            - **MemberClusters** *(list) --* 

              The identifiers of all the nodes that are part of this replication group.

              
              

              - *(string) --* 
          
            

            - **NodeGroups** *(list) --* 

              A list of node groups in this replication group. For Redis (cluster mode disabled) replication groups, this is a single-element list. For Redis (cluster mode enabled) replication groups, the list contains an entry for each node group (shard).

              
              

              - *(dict) --* 

                Represents a collection of cache nodes in a replication group. One node in the node group is the read/write primary node. All the other nodes are read-only Replica nodes.

                
                

                - **NodeGroupId** *(string) --* 

                  The identifier for the node group (shard). A Redis (cluster mode disabled) replication group contains only 1 node group; therefore, the node group ID is 0001. A Redis (cluster mode enabled) replication group contains 1 to 15 node groups numbered 0001 to 0015. 

                  
                

                - **Status** *(string) --* 

                  The current state of this replication group - ``creating`` , ``available`` , etc.

                  
                

                - **PrimaryEndpoint** *(dict) --* 

                  The endpoint of the primary node in this node group (shard).

                  
                  

                  - **Address** *(string) --* 

                    The DNS hostname of the cache node.

                    
                  

                  - **Port** *(integer) --* 

                    The port number that the cache engine is listening on.

                    
              
                

                - **Slots** *(string) --* 

                  The keyspace for this node group (shard).

                  
                

                - **NodeGroupMembers** *(list) --* 

                  A list containing information about individual nodes within the node group (shard).

                  
                  

                  - *(dict) --* 

                    Represents a single node within a node group (shard).

                    
                    

                    - **CacheClusterId** *(string) --* 

                      The ID of the cluster to which the node belongs.

                      
                    

                    - **CacheNodeId** *(string) --* 

                      The ID of the node within its cluster. A node ID is a numeric identifier (0001, 0002, etc.).

                      
                    

                    - **ReadEndpoint** *(dict) --* 

                      Represents the information required for client programs to connect to a cache node.

                      
                      

                      - **Address** *(string) --* 

                        The DNS hostname of the cache node.

                        
                      

                      - **Port** *(integer) --* 

                        The port number that the cache engine is listening on.

                        
                  
                    

                    - **PreferredAvailabilityZone** *(string) --* 

                      The name of the Availability Zone in which the node is located.

                      
                    

                    - **CurrentRole** *(string) --* 

                      The role that is currently assigned to the node - ``primary`` or ``replica`` .

                      
                
              
            
          
            

            - **SnapshottingClusterId** *(string) --* 

              The cluster ID that is used as the daily snapshot source for the replication group.

              
            

            - **AutomaticFailover** *(string) --* 

              Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

               

              Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

               

               
              * Redis versions earlier than 2.8.6. 
               
              * Redis (cluster mode disabled): T1 and T2 cache node types. 
               
              * Redis (cluster mode enabled): T1 node types. 
               

              
            

            - **ConfigurationEndpoint** *(dict) --* 

              The configuration endpoint for this replication group. Use the configuration endpoint to connect to this replication group.

              
              

              - **Address** *(string) --* 

                The DNS hostname of the cache node.

                
              

              - **Port** *(integer) --* 

                The port number that the cache engine is listening on.

                
          
            

            - **SnapshotRetentionLimit** *(integer) --* 

              The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was taken today is retained for 5 days before being deleted.

               

              .. warning::

                 

                If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

                 

              
            

            - **SnapshotWindow** *(string) --* 

              The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).

               

              Example: ``05:00-09:00``  

               

              If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

               

              .. note::

                 

                This parameter is only valid if the ``Engine`` parameter is ``redis`` .

                 

              
            

            - **ClusterEnabled** *(boolean) --* 

              A flag indicating whether or not this replication group is cluster enabled; i.e., whether its data can be partitioned across multiple shards (API/CLI: node groups).

               

              Valid values: ``true`` | ``false``  

              
            

            - **CacheNodeType** *(string) --* 

              The name of the compute and memory capacity node type for each node in the replication group.

              
            

            - **AuthTokenEnabled** *(boolean) --* 

              A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

               

              Default: ``false``  

              
            

            - **TransitEncryptionEnabled** *(boolean) --* 

              A flag that enables in-transit encryption when set to ``true`` .

               

              You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created. To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to ``true`` when you create a cluster.

               

              Default: ``false``  

              
            

            - **AtRestEncryptionEnabled** *(boolean) --* 

              A flag that enables encryption at-rest when set to ``true`` .

               

              You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true`` when you create a cluster.

               

              Default: ``false``  

              
        
      
    

  .. py:method:: describe_reserved_cache_nodes(**kwargs)

    

    Returns information about reserved cache nodes for this account, or about a specified reserved cache node.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeReservedCacheNodes>`_    


    **Request Syntax** 
    ::

      response = client.describe_reserved_cache_nodes(
          ReservedCacheNodeId='string',
          ReservedCacheNodesOfferingId='string',
          CacheNodeType='string',
          Duration='string',
          ProductDescription='string',
          OfferingType='string',
          MaxRecords=123,
          Marker='string'
      )
    :type ReservedCacheNodeId: string
    :param ReservedCacheNodeId: 

      The reserved cache node identifier filter value. Use this parameter to show only the reservation that matches the specified reservation ID.

      

    
    :type ReservedCacheNodesOfferingId: string
    :param ReservedCacheNodesOfferingId: 

      The offering identifier filter value. Use this parameter to show only purchased reservations matching the specified offering identifier.

      

    
    :type CacheNodeType: string
    :param CacheNodeType: 

      The cache node type filter value. Use this parameter to show only those reservations matching the specified cache node type.

       

      The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

       

       
      * General purpose: 

         
        * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
         
        * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
         

       
       
      * Compute optimized: 

         
        * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
         

       
       
      * Memory optimized: 

         
        * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
         
        * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
         

       
       

       

       **Notes:**  

       

       
      * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
       
      * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
       
      * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
       
      * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
       

       

      For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

      

    
    :type Duration: string
    :param Duration: 

      The duration filter value, specified in years or seconds. Use this parameter to show only reservations for this duration.

       

      Valid Values: ``1 | 3 | 31536000 | 94608000``  

      

    
    :type ProductDescription: string
    :param ProductDescription: 

      The product description filter value. Use this parameter to show only those reservations matching the specified product description.

      

    
    :type OfferingType: string
    :param OfferingType: 

      The offering type filter value. Use this parameter to show only the available offerings matching the specified offering type.

       

      Valid values: ``"Light Utilization"|"Medium Utilization"|"Heavy Utilization"``  

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a marker is included in the response so that the remaining results can be retrieved.

       

      Default: 100

       

      Constraints: minimum 20; maximum 100.

      

    
    :type Marker: string
    :param Marker: 

      An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Marker': 'string',
            'ReservedCacheNodes': [
                {
                    'ReservedCacheNodeId': 'string',
                    'ReservedCacheNodesOfferingId': 'string',
                    'CacheNodeType': 'string',
                    'StartTime': datetime(2015, 1, 1),
                    'Duration': 123,
                    'FixedPrice': 123.0,
                    'UsagePrice': 123.0,
                    'CacheNodeCount': 123,
                    'ProductDescription': 'string',
                    'OfferingType': 'string',
                    'State': 'string',
                    'RecurringCharges': [
                        {
                            'RecurringChargeAmount': 123.0,
                            'RecurringChargeFrequency': 'string'
                        },
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DescribeReservedCacheNodes`` operation.

        
        

        - **Marker** *(string) --* 

          Provides an identifier to allow retrieval of paginated results.

          
        

        - **ReservedCacheNodes** *(list) --* 

          A list of reserved cache nodes. Each element in the list contains detailed information about one node.

          
          

          - *(dict) --* 

            Represents the output of a ``PurchaseReservedCacheNodesOffering`` operation.

            
            

            - **ReservedCacheNodeId** *(string) --* 

              The unique identifier for the reservation.

              
            

            - **ReservedCacheNodesOfferingId** *(string) --* 

              The offering identifier.

              
            

            - **CacheNodeType** *(string) --* 

              The cache node type for the reserved cache nodes.

               

              The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

               

               
              * General purpose: 

                 
                * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
                 
                * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
                 

               
               
              * Compute optimized: 

                 
                * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
                 

               
               
              * Memory optimized: 

                 
                * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
                 
                * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
                 

               
               

               

               **Notes:**  

               

               
              * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
               
              * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
               
              * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
               
              * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
               

               

              For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

              
            

            - **StartTime** *(datetime) --* 

              The time the reservation started.

              
            

            - **Duration** *(integer) --* 

              The duration of the reservation in seconds.

              
            

            - **FixedPrice** *(float) --* 

              The fixed price charged for this reserved cache node.

              
            

            - **UsagePrice** *(float) --* 

              The hourly price charged for this reserved cache node.

              
            

            - **CacheNodeCount** *(integer) --* 

              The number of cache nodes that have been reserved.

              
            

            - **ProductDescription** *(string) --* 

              The description of the reserved cache node.

              
            

            - **OfferingType** *(string) --* 

              The offering type of this reserved cache node.

              
            

            - **State** *(string) --* 

              The state of the reserved cache node.

              
            

            - **RecurringCharges** *(list) --* 

              The recurring price charged to run this reserved cache node.

              
              

              - *(dict) --* 

                Contains the specific price and frequency of a recurring charges for a reserved cache node, or for a reserved cache node offering.

                
                

                - **RecurringChargeAmount** *(float) --* 

                  The monetary amount of the recurring charge.

                  
                

                - **RecurringChargeFrequency** *(string) --* 

                  The frequency of the recurring charge.

                  
            
          
        
      
    

  .. py:method:: describe_reserved_cache_nodes_offerings(**kwargs)

    

    Lists available reserved cache node offerings.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeReservedCacheNodesOfferings>`_    


    **Request Syntax** 
    ::

      response = client.describe_reserved_cache_nodes_offerings(
          ReservedCacheNodesOfferingId='string',
          CacheNodeType='string',
          Duration='string',
          ProductDescription='string',
          OfferingType='string',
          MaxRecords=123,
          Marker='string'
      )
    :type ReservedCacheNodesOfferingId: string
    :param ReservedCacheNodesOfferingId: 

      The offering identifier filter value. Use this parameter to show only the available offering that matches the specified reservation identifier.

       

      Example: ``438012d3-4052-4cc7-b2e3-8d3372e0e706``  

      

    
    :type CacheNodeType: string
    :param CacheNodeType: 

      The cache node type filter value. Use this parameter to show only the available offerings matching the specified cache node type.

       

      The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

       

       
      * General purpose: 

         
        * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
         
        * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
         

       
       
      * Compute optimized: 

         
        * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
         

       
       
      * Memory optimized: 

         
        * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
         
        * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
         

       
       

       

       **Notes:**  

       

       
      * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
       
      * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
       
      * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
       
      * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
       

       

      For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

      

    
    :type Duration: string
    :param Duration: 

      Duration filter value, specified in years or seconds. Use this parameter to show only reservations for a given duration.

       

      Valid Values: ``1 | 3 | 31536000 | 94608000``  

      

    
    :type ProductDescription: string
    :param ProductDescription: 

      The product description filter value. Use this parameter to show only the available offerings matching the specified product description.

      

    
    :type OfferingType: string
    :param OfferingType: 

      The offering type filter value. Use this parameter to show only the available offerings matching the specified offering type.

       

      Valid Values: ``"Light Utilization"|"Medium Utilization"|"Heavy Utilization"``  

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a marker is included in the response so that the remaining results can be retrieved.

       

      Default: 100

       

      Constraints: minimum 20; maximum 100.

      

    
    :type Marker: string
    :param Marker: 

      An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Marker': 'string',
            'ReservedCacheNodesOfferings': [
                {
                    'ReservedCacheNodesOfferingId': 'string',
                    'CacheNodeType': 'string',
                    'Duration': 123,
                    'FixedPrice': 123.0,
                    'UsagePrice': 123.0,
                    'ProductDescription': 'string',
                    'OfferingType': 'string',
                    'RecurringCharges': [
                        {
                            'RecurringChargeAmount': 123.0,
                            'RecurringChargeFrequency': 'string'
                        },
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DescribeReservedCacheNodesOfferings`` operation.

        
        

        - **Marker** *(string) --* 

          Provides an identifier to allow retrieval of paginated results.

          
        

        - **ReservedCacheNodesOfferings** *(list) --* 

          A list of reserved cache node offerings. Each element in the list contains detailed information about one offering.

          
          

          - *(dict) --* 

            Describes all of the attributes of a reserved cache node offering.

            
            

            - **ReservedCacheNodesOfferingId** *(string) --* 

              A unique identifier for the reserved cache node offering.

              
            

            - **CacheNodeType** *(string) --* 

              The cache node type for the reserved cache node.

               

              The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

               

               
              * General purpose: 

                 
                * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
                 
                * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
                 

               
               
              * Compute optimized: 

                 
                * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
                 

               
               
              * Memory optimized: 

                 
                * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
                 
                * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
                 

               
               

               

               **Notes:**  

               

               
              * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
               
              * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
               
              * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
               
              * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
               

               

              For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

              
            

            - **Duration** *(integer) --* 

              The duration of the offering. in seconds.

              
            

            - **FixedPrice** *(float) --* 

              The fixed price charged for this offering.

              
            

            - **UsagePrice** *(float) --* 

              The hourly price charged for this offering.

              
            

            - **ProductDescription** *(string) --* 

              The cache engine used by the offering.

              
            

            - **OfferingType** *(string) --* 

              The offering type.

              
            

            - **RecurringCharges** *(list) --* 

              The recurring price charged to run this reserved cache node.

              
              

              - *(dict) --* 

                Contains the specific price and frequency of a recurring charges for a reserved cache node, or for a reserved cache node offering.

                
                

                - **RecurringChargeAmount** *(float) --* 

                  The monetary amount of the recurring charge.

                  
                

                - **RecurringChargeFrequency** *(string) --* 

                  The frequency of the recurring charge.

                  
            
          
        
      
    

  .. py:method:: describe_snapshots(**kwargs)

    

    Returns information about cluster or replication group snapshots. By default, ``DescribeSnapshots`` lists all of your snapshots; it can optionally describe a single snapshot, or just the snapshots associated with a particular cache cluster.

     

    .. note::

       

      This operation is valid for Redis only.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeSnapshots>`_    


    **Request Syntax** 
    ::

      response = client.describe_snapshots(
          ReplicationGroupId='string',
          CacheClusterId='string',
          SnapshotName='string',
          SnapshotSource='string',
          Marker='string',
          MaxRecords=123,
          ShowNodeGroupConfig=True|False
      )
    :type ReplicationGroupId: string
    :param ReplicationGroupId: 

      A user-supplied replication group identifier. If this parameter is specified, only snapshots associated with that specific replication group are described.

      

    
    :type CacheClusterId: string
    :param CacheClusterId: 

      A user-supplied cluster identifier. If this parameter is specified, only snapshots associated with that specific cluster are described.

      

    
    :type SnapshotName: string
    :param SnapshotName: 

      A user-supplied name of the snapshot. If this parameter is specified, only this snapshot are described.

      

    
    :type SnapshotSource: string
    :param SnapshotSource: 

      If set to ``system`` , the output shows snapshots that were automatically created by ElastiCache. If set to ``user`` the output shows snapshots that were manually created. If omitted, the output shows both automatically and manually created snapshots.

      

    
    :type Marker: string
    :param Marker: 

      An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a marker is included in the response so that the remaining results can be retrieved.

       

      Default: 50

       

      Constraints: minimum 20; maximum 50.

      

    
    :type ShowNodeGroupConfig: boolean
    :param ShowNodeGroupConfig: 

      A Boolean value which if true, the node group (shard) configuration is included in the snapshot description.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Marker': 'string',
            'Snapshots': [
                {
                    'SnapshotName': 'string',
                    'ReplicationGroupId': 'string',
                    'ReplicationGroupDescription': 'string',
                    'CacheClusterId': 'string',
                    'SnapshotStatus': 'string',
                    'SnapshotSource': 'string',
                    'CacheNodeType': 'string',
                    'Engine': 'string',
                    'EngineVersion': 'string',
                    'NumCacheNodes': 123,
                    'PreferredAvailabilityZone': 'string',
                    'CacheClusterCreateTime': datetime(2015, 1, 1),
                    'PreferredMaintenanceWindow': 'string',
                    'TopicArn': 'string',
                    'Port': 123,
                    'CacheParameterGroupName': 'string',
                    'CacheSubnetGroupName': 'string',
                    'VpcId': 'string',
                    'AutoMinorVersionUpgrade': True|False,
                    'SnapshotRetentionLimit': 123,
                    'SnapshotWindow': 'string',
                    'NumNodeGroups': 123,
                    'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                    'NodeSnapshots': [
                        {
                            'CacheClusterId': 'string',
                            'NodeGroupId': 'string',
                            'CacheNodeId': 'string',
                            'NodeGroupConfiguration': {
                                'Slots': 'string',
                                'ReplicaCount': 123,
                                'PrimaryAvailabilityZone': 'string',
                                'ReplicaAvailabilityZones': [
                                    'string',
                                ]
                            },
                            'CacheSize': 'string',
                            'CacheNodeCreateTime': datetime(2015, 1, 1),
                            'SnapshotCreateTime': datetime(2015, 1, 1)
                        },
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DescribeSnapshots`` operation.

        
        

        - **Marker** *(string) --* 

          An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

          
        

        - **Snapshots** *(list) --* 

          A list of snapshots. Each item in the list contains detailed information about one snapshot.

          
          

          - *(dict) --* 

            Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.

            
            

            - **SnapshotName** *(string) --* 

              The name of a snapshot. For an automatic snapshot, the name is system-generated. For a manual snapshot, this is the user-provided name.

              
            

            - **ReplicationGroupId** *(string) --* 

              The unique identifier of the source replication group.

              
            

            - **ReplicationGroupDescription** *(string) --* 

              A description of the source replication group.

              
            

            - **CacheClusterId** *(string) --* 

              The user-supplied identifier of the source cluster.

              
            

            - **SnapshotStatus** *(string) --* 

              The status of the snapshot. Valid values: ``creating`` | ``available`` | ``restoring`` | ``copying`` | ``deleting`` .

              
            

            - **SnapshotSource** *(string) --* 

              Indicates whether the snapshot is from an automatic backup (``automated`` ) or was created manually (``manual`` ).

              
            

            - **CacheNodeType** *(string) --* 

              The name of the compute and memory capacity node type for the source cluster.

               

              The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

               

               
              * General purpose: 

                 
                * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
                 
                * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
                 

               
               
              * Compute optimized: 

                 
                * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
                 

               
               
              * Memory optimized: 

                 
                * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
                 
                * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
                 

               
               

               

               **Notes:**  

               

               
              * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
               
              * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
               
              * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
               
              * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
               

               

              For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

              
            

            - **Engine** *(string) --* 

              The name of the cache engine (``memcached`` or ``redis`` ) used by the source cluster.

              
            

            - **EngineVersion** *(string) --* 

              The version of the cache engine version that is used by the source cluster.

              
            

            - **NumCacheNodes** *(integer) --* 

              The number of cache nodes in the source cluster.

               

              For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

              
            

            - **PreferredAvailabilityZone** *(string) --* 

              The name of the Availability Zone in which the source cluster is located.

              
            

            - **CacheClusterCreateTime** *(datetime) --* 

              The date and time when the source cluster was created.

              
            

            - **PreferredMaintenanceWindow** *(string) --* 

              Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.

               

              Valid values for ``ddd`` are:

               

               
              * ``sun``   
               
              * ``mon``   
               
              * ``tue``   
               
              * ``wed``   
               
              * ``thu``   
               
              * ``fri``   
               
              * ``sat``   
               

               

              Example: ``sun:23:00-mon:01:30``  

              
            

            - **TopicArn** *(string) --* 

              The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing notifications.

              
            

            - **Port** *(integer) --* 

              The port number used by each cache nodes in the source cluster.

              
            

            - **CacheParameterGroupName** *(string) --* 

              The cache parameter group that is associated with the source cluster.

              
            

            - **CacheSubnetGroupName** *(string) --* 

              The name of the cache subnet group associated with the source cluster.

              
            

            - **VpcId** *(string) --* 

              The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the source cluster.

              
            

            - **AutoMinorVersionUpgrade** *(boolean) --* 

              This parameter is currently disabled.

              
            

            - **SnapshotRetentionLimit** *(integer) --* 

              For an automatic snapshot, the number of days for which ElastiCache retains the snapshot before deleting it.

               

              For manual snapshots, this field reflects the ``SnapshotRetentionLimit`` for the source cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots do not expire, and can only be deleted using the ``DeleteSnapshot`` operation. 

               

               **Important** If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

              
            

            - **SnapshotWindow** *(string) --* 

              The daily time range during which ElastiCache takes daily snapshots of the source cluster.

              
            

            - **NumNodeGroups** *(integer) --* 

              The number of node groups (shards) in this snapshot. When restoring from a snapshot, the number of node groups (shards) in the snapshot and in the restored replication group must be the same.

              
            

            - **AutomaticFailover** *(string) --* 

              Indicates the status of Multi-AZ with automatic failover for the source Redis replication group.

               

              Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

               

               
              * Redis versions earlier than 2.8.6. 
               
              * Redis (cluster mode disabled): T1 and T2 cache node types. 
               
              * Redis (cluster mode enabled): T1 node types. 
               

              
            

            - **NodeSnapshots** *(list) --* 

              A list of the cache nodes in the source cluster.

              
              

              - *(dict) --* 

                Represents an individual cache node in a snapshot of a cluster.

                
                

                - **CacheClusterId** *(string) --* 

                  A unique identifier for the source cluster.

                  
                

                - **NodeGroupId** *(string) --* 

                  A unique identifier for the source node group (shard).

                  
                

                - **CacheNodeId** *(string) --* 

                  The cache node identifier for the node in the source cluster.

                  
                

                - **NodeGroupConfiguration** *(dict) --* 

                  The configuration for the source node group (shard).

                  
                  

                  - **Slots** *(string) --* 

                    A string that specifies the keyspace for a particular node group. Keyspaces range from 0 to 16,383. The string is in the format ``startkey-endkey`` .

                     

                    Example: ``"0-3999"``  

                    
                  

                  - **ReplicaCount** *(integer) --* 

                    The number of read replica nodes in this node group (shard).

                    
                  

                  - **PrimaryAvailabilityZone** *(string) --* 

                    The Availability Zone where the primary node of this node group (shard) is launched.

                    
                  

                  - **ReplicaAvailabilityZones** *(list) --* 

                    A list of Availability Zones to be used for the read replicas. The number of Availability Zones in this list must match the value of ``ReplicaCount`` or ``ReplicasPerNodeGroup`` if not specified.

                    
                    

                    - *(string) --* 
                
              
                

                - **CacheSize** *(string) --* 

                  The size of the cache on the source cache node.

                  
                

                - **CacheNodeCreateTime** *(datetime) --* 

                  The date and time when the cache node was created in the source cluster.

                  
                

                - **SnapshotCreateTime** *(datetime) --* 

                  The date and time when the source node's metadata and cache data set was obtained for the snapshot.

                  
            
          
        
      
    

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

        


  .. py:method:: list_allowed_node_type_modifications(**kwargs)

    

    Lists all available node types that you can scale your Redis cluster's or replication group's current node type up to.

     

    When you use the ``ModifyCacheCluster`` or ``ModifyReplicationGroup`` operations to scale up your cluster or replication group, the value of the ``CacheNodeType`` parameter must be one of the node types returned by this operation.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/ListAllowedNodeTypeModifications>`_    


    **Request Syntax** 
    ::

      response = client.list_allowed_node_type_modifications(
          CacheClusterId='string',
          ReplicationGroupId='string'
      )
    :type CacheClusterId: string
    :param CacheClusterId: 

      The name of the cluster you want to scale up to a larger node instanced type. ElastiCache uses the cluster id to identify the current node type of this cluster and from that to create a list of node types you can scale up to.

       

      .. warning::

         

        You must provide a value for either the ``CacheClusterId`` or the ``ReplicationGroupId`` .

         

      

    
    :type ReplicationGroupId: string
    :param ReplicationGroupId: 

      The name of the replication group want to scale up to a larger node type. ElastiCache uses the replication group id to identify the current node type being used by this replication group, and from that to create a list of node types you can scale up to.

       

      .. warning::

         

        You must provide a value for either the ``CacheClusterId`` or the ``ReplicationGroupId`` .

         

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ScaleUpModifications': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the allowed node types you can use to modify your cluster or replication group.

        
        

        - **ScaleUpModifications** *(list) --* 

          A string list, each element of which specifies a cache node type which you can use to scale your cluster or replication group.

           

          When scaling up a Redis cluster or replication group using ``ModifyCacheCluster`` or ``ModifyReplicationGroup`` , use a value from this list for the ``CacheNodeType`` parameter.

          
          

          - *(string) --* 
      
    

  .. py:method:: list_tags_for_resource(**kwargs)

    

    Lists all cost allocation tags currently on the named resource. A ``cost allocation tag`` is a key-value pair where the key is case-sensitive and the value is optional. You can use cost allocation tags to categorize and track your AWS costs.

     

    You can have a maximum of 50 cost allocation tags on an ElastiCache resource. For more information, see `Using Cost Allocation Tags in Amazon ElastiCache <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/BestPractices.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/ListTagsForResource>`_    


    **Request Syntax** 
    ::

      response = client.list_tags_for_resource(
          ResourceName='string'
      )
    :type ResourceName: string
    :param ResourceName: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the resource for which you want the list of tags, for example ``arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster`` or ``arn:aws:elasticache:us-west-2:0123456789:snapshot:mySnapshot`` .

       

      For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      

    
    
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

        Represents the output from the ``AddTagsToResource`` , ``ListTagsForResource`` , and ``RemoveTagsFromResource`` operations.

        
        

        - **TagList** *(list) --* 

          A list of cost allocation tags as key-value pairs.

          
          

          - *(dict) --* 

            A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. A tag with a null Value is permitted.

            
            

            - **Key** *(string) --* 

              The key for the tag. May not be null.

              
            

            - **Value** *(string) --* 

              The tag's value. May be null.

              
        
      
    

  .. py:method:: modify_cache_cluster(**kwargs)

    

    Modifies the settings for a cluster. You can use this operation to change one or more cluster configuration parameters by specifying the parameters and the new values.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/ModifyCacheCluster>`_    


    **Request Syntax** 
    ::

      response = client.modify_cache_cluster(
          CacheClusterId='string',
          NumCacheNodes=123,
          CacheNodeIdsToRemove=[
              'string',
          ],
          AZMode='single-az'|'cross-az',
          NewAvailabilityZones=[
              'string',
          ],
          CacheSecurityGroupNames=[
              'string',
          ],
          SecurityGroupIds=[
              'string',
          ],
          PreferredMaintenanceWindow='string',
          NotificationTopicArn='string',
          CacheParameterGroupName='string',
          NotificationTopicStatus='string',
          ApplyImmediately=True|False,
          EngineVersion='string',
          AutoMinorVersionUpgrade=True|False,
          SnapshotRetentionLimit=123,
          SnapshotWindow='string',
          CacheNodeType='string'
      )
    :type CacheClusterId: string
    :param CacheClusterId: **[REQUIRED]** 

      The cluster identifier. This value is stored as a lowercase string.

      

    
    :type NumCacheNodes: integer
    :param NumCacheNodes: 

      The number of cache nodes that the cluster should have. If the value for ``NumCacheNodes`` is greater than the sum of the number of current cache nodes and the number of cache nodes pending creation (which may be zero), more nodes are added. If the value is less than the number of existing cache nodes, nodes are removed. If the value is equal to the number of current cache nodes, any pending add or remove requests are canceled.

       

      If you are removing cache nodes, you must use the ``CacheNodeIdsToRemove`` parameter to provide the IDs of the specific cache nodes to remove.

       

      For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

       

      .. note::

         

        Adding or removing Memcached cache nodes can be applied immediately or as a pending operation (see ``ApplyImmediately`` ).

         

        A pending operation to modify the number of cache nodes in a cluster during its maintenance window, whether by adding or removing nodes in accordance with the scale out architecture, is not queued. The customer's latest request to add or remove nodes to the cluster overrides any previous pending operations to modify the number of cache nodes in the cluster. For example, a request to remove 2 nodes would override a previous pending operation to remove 3 nodes. Similarly, a request to add 2 nodes would override a previous pending operation to remove 3 nodes and vice versa. As Memcached cache nodes may now be provisioned in different Availability Zones with flexible cache node placement, a request to add nodes does not automatically override a previous pending operation to add nodes. The customer can modify the previous pending operation to add more nodes or explicitly cancel the pending request and retry the new request. To cancel pending operations to modify the number of cache nodes in a cluster, use the ``ModifyCacheCluster`` request and set ``NumCacheNodes`` equal to the number of cache nodes currently in the cluster.

         

      

    
    :type CacheNodeIdsToRemove: list
    :param CacheNodeIdsToRemove: 

      A list of cache node IDs to be removed. A node ID is a numeric identifier (0001, 0002, etc.). This parameter is only valid when ``NumCacheNodes`` is less than the existing number of cache nodes. The number of cache node IDs supplied in this parameter must match the difference between the existing number of cache nodes in the cluster or pending cache nodes, whichever is greater, and the value of ``NumCacheNodes`` in the request.

       

      For example: If you have 3 active cache nodes, 7 pending cache nodes, and the number of cache nodes in this ``ModifyCacheCluster`` call is 5, you must list 2 (7 - 5) cache node IDs to remove.

      

    
      - *(string) --* 

      
  
    :type AZMode: string
    :param AZMode: 

      Specifies whether the new nodes in this Memcached cluster are all created in a single Availability Zone or created across multiple Availability Zones.

       

      Valid values: ``single-az`` | ``cross-az`` .

       

      This option is only supported for Memcached clusters.

       

      .. note::

         

        You cannot specify ``single-az`` if the Memcached cluster already has cache nodes in different Availability Zones. If ``cross-az`` is specified, existing Memcached nodes remain in their current Availability Zone.

         

        Only newly created nodes are located in different Availability Zones. For instructions on how to move existing Memcached nodes to different Availability Zones, see the **Availability Zone Considerations** section of `Cache Node Considerations for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheNode.Memcached.html>`__ .

         

      

    
    :type NewAvailabilityZones: list
    :param NewAvailabilityZones: 

      The list of Availability Zones where the new Memcached cache nodes are created.

       

      This parameter is only valid when ``NumCacheNodes`` in the request is greater than the sum of the number of active cache nodes and the number of cache nodes pending creation (which may be zero). The number of Availability Zones supplied in this list must match the cache nodes being added in this request.

       

      This option is only supported on Memcached clusters.

       

      Scenarios:

       

       
      * **Scenario 1:** You have 3 active nodes and wish to add 2 nodes. Specify ``NumCacheNodes=5`` (3 + 2) and optionally specify two Availability Zones for the two new nodes. 
       
      * **Scenario 2:** You have 3 active nodes and 2 nodes pending creation (from the scenario 1 call) and want to add 1 more node. Specify ``NumCacheNodes=6`` ((3 + 2) + 1) and optionally specify an Availability Zone for the new node. 
       
      * **Scenario 3:** You want to cancel all pending operations. Specify ``NumCacheNodes=3`` to cancel all pending operations. 
       

       

      The Availability Zone placement of nodes pending creation cannot be modified. If you wish to cancel any nodes pending creation, add 0 nodes by setting ``NumCacheNodes`` to the number of current nodes.

       

      If ``cross-az`` is specified, existing Memcached nodes remain in their current Availability Zone. Only newly created nodes can be located in different Availability Zones. For guidance on how to move existing Memcached nodes to different Availability Zones, see the **Availability Zone Considerations** section of `Cache Node Considerations for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheNode.Memcached.html>`__ .

       

       **Impact of new add/remove requests upon pending requests**  

       

       
      * Scenario-1 

         
        * Pending Action: Delete 
         
        * New Request: Delete 
         
        * Result: The new delete, pending or immediate, replaces the pending delete. 
         

       
       
      * Scenario-2 

         
        * Pending Action: Delete 
         
        * New Request: Create 
         
        * Result: The new create, pending or immediate, replaces the pending delete. 
         

       
       
      * Scenario-3 

         
        * Pending Action: Create 
         
        * New Request: Delete 
         
        * Result: The new delete, pending or immediate, replaces the pending create. 
         

       
       
      * Scenario-4 

         
        * Pending Action: Create 
         
        * New Request: Create 
         
        * Result: The new create is added to the pending create. 

        .. warning::

            **Important:** If the new create request is **Apply Immediately - Yes** , all creates are performed immediately. If the new create request is **Apply Immediately - No** , all creates are pending. 

         
         

       
       

      

    
      - *(string) --* 

      
  
    :type CacheSecurityGroupNames: list
    :param CacheSecurityGroupNames: 

      A list of cache security group names to authorize on this cluster. This change is asynchronously applied as soon as possible.

       

      You can use this parameter only with clusters that are created outside of an Amazon Virtual Private Cloud (Amazon VPC).

       

      Constraints: Must contain no more than 255 alphanumeric characters. Must not be "Default".

      

    
      - *(string) --* 

      
  
    :type SecurityGroupIds: list
    :param SecurityGroupIds: 

      Specifies the VPC Security Groups associated with the cluster.

       

      This parameter can be used only with clusters that are created in an Amazon Virtual Private Cloud (Amazon VPC).

      

    
      - *(string) --* 

      
  
    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: 

      Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.

       

      Valid values for ``ddd`` are:

       

       
      * ``sun``   
       
      * ``mon``   
       
      * ``tue``   
       
      * ``wed``   
       
      * ``thu``   
       
      * ``fri``   
       
      * ``sat``   
       

       

      Example: ``sun:23:00-mon:01:30``  

      

    
    :type NotificationTopicArn: string
    :param NotificationTopicArn: 

      The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications are sent.

       

      .. note::

         

        The Amazon SNS topic owner must be same as the cluster owner.

         

      

    
    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: 

      The name of the cache parameter group to apply to this cluster. This change is asynchronously applied as soon as possible for parameters when the ``ApplyImmediately`` parameter is specified as ``true`` for this request.

      

    
    :type NotificationTopicStatus: string
    :param NotificationTopicStatus: 

      The status of the Amazon SNS notification topic. Notifications are sent only if the status is ``active`` .

       

      Valid values: ``active`` | ``inactive``  

      

    
    :type ApplyImmediately: boolean
    :param ApplyImmediately: 

      If ``true`` , this parameter causes the modifications in this request and any pending modifications to be applied, asynchronously and as soon as possible, regardless of the ``PreferredMaintenanceWindow`` setting for the cluster.

       

      If ``false`` , changes to the cluster are applied on the next maintenance reboot, or the next failure reboot, whichever occurs first.

       

      .. warning::

         

        If you perform a ``ModifyCacheCluster`` before a pending modification is applied, the pending modification is replaced by the newer modification.

         

       

      Valid values: ``true`` | ``false``  

       

      Default: ``false``  

      

    
    :type EngineVersion: string
    :param EngineVersion: 

      The upgraded version of the cache engine to be run on the cache nodes.

       

       **Important:** You can upgrade to a newer engine version (see `Selecting a Cache Engine and Version <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/SelectEngine.html#VersionManagement>`__ ), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster and create it anew with the earlier engine version. 

      

    
    :type AutoMinorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: 

      This parameter is currently disabled.

      

    
    :type SnapshotRetentionLimit: integer
    :param SnapshotRetentionLimit: 

      The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was taken today is retained for 5 days before being deleted.

       

      .. note::

         

        If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

         

      

    
    :type SnapshotWindow: string
    :param SnapshotWindow: 

      The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your cluster. 

      

    
    :type CacheNodeType: string
    :param CacheNodeType: 

      A valid cache node type that you want to scale this cluster up to.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CacheCluster': {
                'CacheClusterId': 'string',
                'ConfigurationEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'ClientDownloadLandingPage': 'string',
                'CacheNodeType': 'string',
                'Engine': 'string',
                'EngineVersion': 'string',
                'CacheClusterStatus': 'string',
                'NumCacheNodes': 123,
                'PreferredAvailabilityZone': 'string',
                'CacheClusterCreateTime': datetime(2015, 1, 1),
                'PreferredMaintenanceWindow': 'string',
                'PendingModifiedValues': {
                    'NumCacheNodes': 123,
                    'CacheNodeIdsToRemove': [
                        'string',
                    ],
                    'EngineVersion': 'string',
                    'CacheNodeType': 'string'
                },
                'NotificationConfiguration': {
                    'TopicArn': 'string',
                    'TopicStatus': 'string'
                },
                'CacheSecurityGroups': [
                    {
                        'CacheSecurityGroupName': 'string',
                        'Status': 'string'
                    },
                ],
                'CacheParameterGroup': {
                    'CacheParameterGroupName': 'string',
                    'ParameterApplyStatus': 'string',
                    'CacheNodeIdsToReboot': [
                        'string',
                    ]
                },
                'CacheSubnetGroupName': 'string',
                'CacheNodes': [
                    {
                        'CacheNodeId': 'string',
                        'CacheNodeStatus': 'string',
                        'CacheNodeCreateTime': datetime(2015, 1, 1),
                        'Endpoint': {
                            'Address': 'string',
                            'Port': 123
                        },
                        'ParameterGroupStatus': 'string',
                        'SourceCacheNodeId': 'string',
                        'CustomerAvailabilityZone': 'string'
                    },
                ],
                'AutoMinorVersionUpgrade': True|False,
                'SecurityGroups': [
                    {
                        'SecurityGroupId': 'string',
                        'Status': 'string'
                    },
                ],
                'ReplicationGroupId': 'string',
                'SnapshotRetentionLimit': 123,
                'SnapshotWindow': 'string',
                'AuthTokenEnabled': True|False,
                'TransitEncryptionEnabled': True|False,
                'AtRestEncryptionEnabled': True|False
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CacheCluster** *(dict) --* 

          Contains all of the attributes of a specific cluster.

          
          

          - **CacheClusterId** *(string) --* 

            The user-supplied identifier of the cluster. This identifier is a unique key that identifies a cluster.

            
          

          - **ConfigurationEndpoint** *(dict) --* 

            Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the cluster, can be used by an application to connect to any node in the cluster. The configuration endpoint will always have ``.cfg`` in it.

             

            Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``  

            
            

            - **Address** *(string) --* 

              The DNS hostname of the cache node.

              
            

            - **Port** *(integer) --* 

              The port number that the cache engine is listening on.

              
        
          

          - **ClientDownloadLandingPage** *(string) --* 

            The URL of the web page where you can download the latest ElastiCache client library.

            
          

          - **CacheNodeType** *(string) --* 

            The name of the compute and memory capacity node type for the cluster.

             

            The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

             

             
            * General purpose: 

               
              * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
               
              * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
               

             
             
            * Compute optimized: 

               
              * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
               

             
             
            * Memory optimized: 

               
              * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
               
              * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
               

             
             

             

             **Notes:**  

             

             
            * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
             
            * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
             
            * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
             
            * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
             

             

            For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

            
          

          - **Engine** *(string) --* 

            The name of the cache engine (``memcached`` or ``redis`` ) to be used for this cluster.

            
          

          - **EngineVersion** *(string) --* 

            The version of the cache engine that is used in this cluster.

            
          

          - **CacheClusterStatus** *(string) --* 

            The current state of this cluster, one of the following values: ``available`` , ``creating`` , ``deleted`` , ``deleting`` , ``incompatible-network`` , ``modifying`` , ``rebooting cluster nodes`` , ``restore-failed`` , or ``snapshotting`` .

            
          

          - **NumCacheNodes** *(integer) --* 

            The number of cache nodes in the cluster.

             

            For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

            
          

          - **PreferredAvailabilityZone** *(string) --* 

            The name of the Availability Zone in which the cluster is located or "Multiple" if the cache nodes are located in different Availability Zones.

            
          

          - **CacheClusterCreateTime** *(datetime) --* 

            The date and time when the cluster was created.

            
          

          - **PreferredMaintenanceWindow** *(string) --* 

            Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.

             

            Valid values for ``ddd`` are:

             

             
            * ``sun``   
             
            * ``mon``   
             
            * ``tue``   
             
            * ``wed``   
             
            * ``thu``   
             
            * ``fri``   
             
            * ``sat``   
             

             

            Example: ``sun:23:00-mon:01:30``  

            
          

          - **PendingModifiedValues** *(dict) --* 

            A group of settings that are applied to the cluster in the future, or that are currently being applied.

            
            

            - **NumCacheNodes** *(integer) --* 

              The new number of cache nodes for the cluster.

               

              For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

              
            

            - **CacheNodeIdsToRemove** *(list) --* 

              A list of cache node IDs that are being removed (or will be removed) from the cluster. A node ID is a numeric identifier (0001, 0002, etc.).

              
              

              - *(string) --* 
          
            

            - **EngineVersion** *(string) --* 

              The new cache engine version that the cluster runs.

              
            

            - **CacheNodeType** *(string) --* 

              The cache node type that this cluster or replication group is scaled to.

              
        
          

          - **NotificationConfiguration** *(dict) --* 

            Describes a notification topic and its status. Notification topics are used for publishing ElastiCache events to subscribers using Amazon Simple Notification Service (SNS). 

            
            

            - **TopicArn** *(string) --* 

              The Amazon Resource Name (ARN) that identifies the topic.

              
            

            - **TopicStatus** *(string) --* 

              The current state of the topic.

              
        
          

          - **CacheSecurityGroups** *(list) --* 

            A list of cache security group elements, composed of name and status sub-elements.

            
            

            - *(dict) --* 

              Represents a cluster's status within a particular cache security group.

              
              

              - **CacheSecurityGroupName** *(string) --* 

                The name of the cache security group.

                
              

              - **Status** *(string) --* 

                The membership status in the cache security group. The status changes when a cache security group is modified, or when the cache security groups assigned to a cluster are modified.

                
          
        
          

          - **CacheParameterGroup** *(dict) --* 

            Status of the cache parameter group.

            
            

            - **CacheParameterGroupName** *(string) --* 

              The name of the cache parameter group.

              
            

            - **ParameterApplyStatus** *(string) --* 

              The status of parameter updates.

              
            

            - **CacheNodeIdsToReboot** *(list) --* 

              A list of the cache node IDs which need to be rebooted for parameter changes to be applied. A node ID is a numeric identifier (0001, 0002, etc.).

              
              

              - *(string) --* 
          
        
          

          - **CacheSubnetGroupName** *(string) --* 

            The name of the cache subnet group associated with the cluster.

            
          

          - **CacheNodes** *(list) --* 

            A list of cache nodes that are members of the cluster.

            
            

            - *(dict) --* 

              Represents an individual cache node within a cluster. Each cache node runs its own instance of the cluster's protocol-compliant caching software - either Memcached or Redis.

               

              The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

               

               
              * General purpose: 

                 
                * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
                 
                * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
                 

               
               
              * Compute optimized: 

                 
                * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
                 

               
               
              * Memory optimized: 

                 
                * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
                 
                * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
                 

               
               

               

               **Notes:**  

               

               
              * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
               
              * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
               
              * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
               
              * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
               

               

              For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

              
              

              - **CacheNodeId** *(string) --* 

                The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The combination of cluster ID and node ID uniquely identifies every cache node used in a customer's AWS account.

                
              

              - **CacheNodeStatus** *(string) --* 

                The current state of this cache node.

                
              

              - **CacheNodeCreateTime** *(datetime) --* 

                The date and time when the cache node was created.

                
              

              - **Endpoint** *(dict) --* 

                The hostname for connecting to this cache node.

                
                

                - **Address** *(string) --* 

                  The DNS hostname of the cache node.

                  
                

                - **Port** *(integer) --* 

                  The port number that the cache engine is listening on.

                  
            
              

              - **ParameterGroupStatus** *(string) --* 

                The status of the parameter group applied to this cache node.

                
              

              - **SourceCacheNodeId** *(string) --* 

                The ID of the primary node to which this read replica node is synchronized. If this field is empty, this node is not associated with a primary cluster.

                
              

              - **CustomerAvailabilityZone** *(string) --* 

                The Availability Zone where this node was created and now resides.

                
          
        
          

          - **AutoMinorVersionUpgrade** *(boolean) --* 

            This parameter is currently disabled.

            
          

          - **SecurityGroups** *(list) --* 

            A list of VPC Security Groups associated with the cluster.

            
            

            - *(dict) --* 

              Represents a single cache security group and its status.

              
              

              - **SecurityGroupId** *(string) --* 

                The identifier of the cache security group.

                
              

              - **Status** *(string) --* 

                The status of the cache security group membership. The status changes whenever a cache security group is modified, or when the cache security groups assigned to a cluster are modified.

                
          
        
          

          - **ReplicationGroupId** *(string) --* 

            The replication group to which this cluster belongs. If this field is empty, the cluster is not associated with any replication group.

            
          

          - **SnapshotRetentionLimit** *(integer) --* 

            The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was taken today is retained for 5 days before being deleted.

             

            .. warning::

               

              If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

               

            
          

          - **SnapshotWindow** *(string) --* 

            The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your cluster.

             

            Example: ``05:00-09:00``  

            
          

          - **AuthTokenEnabled** *(boolean) --* 

            A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

             

            Default: ``false``  

            
          

          - **TransitEncryptionEnabled** *(boolean) --* 

            A flag that enables in-transit encryption when set to ``true`` .

             

            You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created. To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to ``true`` when you create a cluster.

             

            Default: ``false``  

            
          

          - **AtRestEncryptionEnabled** *(boolean) --* 

            A flag that enables encryption at-rest when set to ``true`` .

             

            You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To enable at-rest encryption on a cluster you must set ``AtRestEncryptionEnabled`` to ``true`` when you create a cluster.

             

            Default: ``false``  

            
      
    

  .. py:method:: modify_cache_parameter_group(**kwargs)

    

    Modifies the parameters of a cache parameter group. You can modify up to 20 parameters in a single request by submitting a list parameter name and value pairs.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/ModifyCacheParameterGroup>`_    


    **Request Syntax** 
    ::

      response = client.modify_cache_parameter_group(
          CacheParameterGroupName='string',
          ParameterNameValues=[
              {
                  'ParameterName': 'string',
                  'ParameterValue': 'string'
              },
          ]
      )
    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: **[REQUIRED]** 

      The name of the cache parameter group to modify.

      

    
    :type ParameterNameValues: list
    :param ParameterNameValues: **[REQUIRED]** 

      An array of parameter names and values for the parameter update. You must supply at least one parameter name and value; subsequent arguments are optional. A maximum of 20 parameters may be modified per request.

      

    
      - *(dict) --* 

        Describes a name-value pair that is used to update the value of a parameter.

        

      
        - **ParameterName** *(string) --* 

          The name of the parameter.

          

        
        - **ParameterValue** *(string) --* 

          The value of the parameter.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CacheParameterGroupName': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of one of the following operations:

         

         
        * ``ModifyCacheParameterGroup``   
         
        * ``ResetCacheParameterGroup``   
         

        
        

        - **CacheParameterGroupName** *(string) --* 

          The name of the cache parameter group.

          
    

  .. py:method:: modify_cache_subnet_group(**kwargs)

    

    Modifies an existing cache subnet group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/ModifyCacheSubnetGroup>`_    


    **Request Syntax** 
    ::

      response = client.modify_cache_subnet_group(
          CacheSubnetGroupName='string',
          CacheSubnetGroupDescription='string',
          SubnetIds=[
              'string',
          ]
      )
    :type CacheSubnetGroupName: string
    :param CacheSubnetGroupName: **[REQUIRED]** 

      The name for the cache subnet group. This value is stored as a lowercase string.

       

      Constraints: Must contain no more than 255 alphanumeric characters or hyphens.

       

      Example: ``mysubnetgroup``  

      

    
    :type CacheSubnetGroupDescription: string
    :param CacheSubnetGroupDescription: 

      A description of the cache subnet group.

      

    
    :type SubnetIds: list
    :param SubnetIds: 

      The EC2 subnet IDs for the cache subnet group.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CacheSubnetGroup': {
                'CacheSubnetGroupName': 'string',
                'CacheSubnetGroupDescription': 'string',
                'VpcId': 'string',
                'Subnets': [
                    {
                        'SubnetIdentifier': 'string',
                        'SubnetAvailabilityZone': {
                            'Name': 'string'
                        }
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CacheSubnetGroup** *(dict) --* 

          Represents the output of one of the following operations:

           

           
          * ``CreateCacheSubnetGroup``   
           
          * ``ModifyCacheSubnetGroup``   
           

          
          

          - **CacheSubnetGroupName** *(string) --* 

            The name of the cache subnet group.

            
          

          - **CacheSubnetGroupDescription** *(string) --* 

            The description of the cache subnet group.

            
          

          - **VpcId** *(string) --* 

            The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group.

            
          

          - **Subnets** *(list) --* 

            A list of subnets associated with the cache subnet group.

            
            

            - *(dict) --* 

              Represents the subnet associated with a cluster. This parameter refers to subnets defined in Amazon Virtual Private Cloud (Amazon VPC) and used with ElastiCache.

              
              

              - **SubnetIdentifier** *(string) --* 

                The unique identifier for the subnet.

                
              

              - **SubnetAvailabilityZone** *(dict) --* 

                The Availability Zone associated with the subnet.

                
                

                - **Name** *(string) --* 

                  The name of the Availability Zone.

                  
            
          
        
      
    

  .. py:method:: modify_replication_group(**kwargs)

    

    Modifies the settings for a replication group.

     

    .. warning::

       

      Due to current limitations on Redis (cluster mode disabled), this operation or parameter is not supported on Redis (cluster mode enabled) replication groups.

       

     

    .. note::

       

      This operation is valid for Redis only.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/ModifyReplicationGroup>`_    


    **Request Syntax** 
    ::

      response = client.modify_replication_group(
          ReplicationGroupId='string',
          ReplicationGroupDescription='string',
          PrimaryClusterId='string',
          SnapshottingClusterId='string',
          AutomaticFailoverEnabled=True|False,
          CacheSecurityGroupNames=[
              'string',
          ],
          SecurityGroupIds=[
              'string',
          ],
          PreferredMaintenanceWindow='string',
          NotificationTopicArn='string',
          CacheParameterGroupName='string',
          NotificationTopicStatus='string',
          ApplyImmediately=True|False,
          EngineVersion='string',
          AutoMinorVersionUpgrade=True|False,
          SnapshotRetentionLimit=123,
          SnapshotWindow='string',
          CacheNodeType='string',
          NodeGroupId='string'
      )
    :type ReplicationGroupId: string
    :param ReplicationGroupId: **[REQUIRED]** 

      The identifier of the replication group to modify.

      

    
    :type ReplicationGroupDescription: string
    :param ReplicationGroupDescription: 

      A description for the replication group. Maximum length is 255 characters.

      

    
    :type PrimaryClusterId: string
    :param PrimaryClusterId: 

      For replication groups with a single primary, if this parameter is specified, ElastiCache promotes the specified cluster in the specified replication group to the primary role. The nodes of all other clusters in the replication group are read replicas.

      

    
    :type SnapshottingClusterId: string
    :param SnapshottingClusterId: 

      The cluster ID that is used as the daily snapshot source for the replication group. This parameter cannot be set for Redis (cluster mode enabled) replication groups.

      

    
    :type AutomaticFailoverEnabled: boolean
    :param AutomaticFailoverEnabled: 

      Determines whether a read replica is automatically promoted to read/write primary if the existing primary encounters a failure.

       

      Valid values: ``true`` | ``false``  

       

      Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

       

       
      * Redis versions earlier than 2.8.6. 
       
      * Redis (cluster mode disabled): T1 and T2 cache node types. 
       
      * Redis (cluster mode enabled): T1 node types. 
       

      

    
    :type CacheSecurityGroupNames: list
    :param CacheSecurityGroupNames: 

      A list of cache security group names to authorize for the clusters in this replication group. This change is asynchronously applied as soon as possible.

       

      This parameter can be used only with replication group containing clusters running outside of an Amazon Virtual Private Cloud (Amazon VPC).

       

      Constraints: Must contain no more than 255 alphanumeric characters. Must not be ``Default`` .

      

    
      - *(string) --* 

      
  
    :type SecurityGroupIds: list
    :param SecurityGroupIds: 

      Specifies the VPC Security Groups associated with the clusters in the replication group.

       

      This parameter can be used only with replication group containing clusters running in an Amazon Virtual Private Cloud (Amazon VPC).

      

    
      - *(string) --* 

      
  
    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: 

      Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.

       

      Valid values for ``ddd`` are:

       

       
      * ``sun``   
       
      * ``mon``   
       
      * ``tue``   
       
      * ``wed``   
       
      * ``thu``   
       
      * ``fri``   
       
      * ``sat``   
       

       

      Example: ``sun:23:00-mon:01:30``  

      

    
    :type NotificationTopicArn: string
    :param NotificationTopicArn: 

      The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications are sent.

       

      .. note::

         

        The Amazon SNS topic owner must be same as the replication group owner. 

         

      

    
    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: 

      The name of the cache parameter group to apply to all of the clusters in this replication group. This change is asynchronously applied as soon as possible for parameters when the ``ApplyImmediately`` parameter is specified as ``true`` for this request.

      

    
    :type NotificationTopicStatus: string
    :param NotificationTopicStatus: 

      The status of the Amazon SNS notification topic for the replication group. Notifications are sent only if the status is ``active`` .

       

      Valid values: ``active`` | ``inactive``  

      

    
    :type ApplyImmediately: boolean
    :param ApplyImmediately: 

      If ``true`` , this parameter causes the modifications in this request and any pending modifications to be applied, asynchronously and as soon as possible, regardless of the ``PreferredMaintenanceWindow`` setting for the replication group.

       

      If ``false`` , changes to the nodes in the replication group are applied on the next maintenance reboot, or the next failure reboot, whichever occurs first.

       

      Valid values: ``true`` | ``false``  

       

      Default: ``false``  

      

    
    :type EngineVersion: string
    :param EngineVersion: 

      The upgraded version of the cache engine to be run on the clusters in the replication group.

       

       **Important:** You can upgrade to a newer engine version (see `Selecting a Cache Engine and Version <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/SelectEngine.html#VersionManagement>`__ ), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing replication group and create it anew with the earlier engine version. 

      

    
    :type AutoMinorVersionUpgrade: boolean
    :param AutoMinorVersionUpgrade: 

      This parameter is currently disabled.

      

    
    :type SnapshotRetentionLimit: integer
    :param SnapshotRetentionLimit: 

      The number of days for which ElastiCache retains automatic node group (shard) snapshots before deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was taken today is retained for 5 days before being deleted.

       

       **Important** If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

      

    
    :type SnapshotWindow: string
    :param SnapshotWindow: 

      The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of the node group (shard) specified by ``SnapshottingClusterId`` .

       

      Example: ``05:00-09:00``  

       

      If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

      

    
    :type CacheNodeType: string
    :param CacheNodeType: 

      A valid cache node type that you want to scale this replication group to.

      

    
    :type NodeGroupId: string
    :param NodeGroupId: 

      The name of the Node Group (called shard in the console).

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ReplicationGroup': {
                'ReplicationGroupId': 'string',
                'Description': 'string',
                'Status': 'string',
                'PendingModifiedValues': {
                    'PrimaryClusterId': 'string',
                    'AutomaticFailoverStatus': 'enabled'|'disabled',
                    'Resharding': {
                        'SlotMigration': {
                            'ProgressPercentage': 123.0
                        }
                    }
                },
                'MemberClusters': [
                    'string',
                ],
                'NodeGroups': [
                    {
                        'NodeGroupId': 'string',
                        'Status': 'string',
                        'PrimaryEndpoint': {
                            'Address': 'string',
                            'Port': 123
                        },
                        'Slots': 'string',
                        'NodeGroupMembers': [
                            {
                                'CacheClusterId': 'string',
                                'CacheNodeId': 'string',
                                'ReadEndpoint': {
                                    'Address': 'string',
                                    'Port': 123
                                },
                                'PreferredAvailabilityZone': 'string',
                                'CurrentRole': 'string'
                            },
                        ]
                    },
                ],
                'SnapshottingClusterId': 'string',
                'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                'ConfigurationEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'SnapshotRetentionLimit': 123,
                'SnapshotWindow': 'string',
                'ClusterEnabled': True|False,
                'CacheNodeType': 'string',
                'AuthTokenEnabled': True|False,
                'TransitEncryptionEnabled': True|False,
                'AtRestEncryptionEnabled': True|False
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ReplicationGroup** *(dict) --* 

          Contains all of the attributes of a specific Redis replication group.

          
          

          - **ReplicationGroupId** *(string) --* 

            The identifier for the replication group.

            
          

          - **Description** *(string) --* 

            The user supplied description of the replication group.

            
          

          - **Status** *(string) --* 

            The current state of this replication group - ``creating`` , ``available`` , ``modifying`` , ``deleting`` , ``create-failed`` , ``snapshotting`` .

            
          

          - **PendingModifiedValues** *(dict) --* 

            A group of settings to be applied to the replication group, either immediately or during the next maintenance window.

            
            

            - **PrimaryClusterId** *(string) --* 

              The primary cluster ID that is applied immediately (if ``--apply-immediately`` was specified), or during the next maintenance window.

              
            

            - **AutomaticFailoverStatus** *(string) --* 

              Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

               

              Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

               

               
              * Redis versions earlier than 2.8.6. 
               
              * Redis (cluster mode disabled): T1 and T2 cache node types. 
               
              * Redis (cluster mode enabled): T1 node types. 
               

              
            

            - **Resharding** *(dict) --* 

              The status of an online resharding operation.

              
              

              - **SlotMigration** *(dict) --* 

                Represents the progress of an online resharding operation.

                
                

                - **ProgressPercentage** *(float) --* 

                  The percentage of the slot migration that is complete.

                  
            
          
        
          

          - **MemberClusters** *(list) --* 

            The identifiers of all the nodes that are part of this replication group.

            
            

            - *(string) --* 
        
          

          - **NodeGroups** *(list) --* 

            A list of node groups in this replication group. For Redis (cluster mode disabled) replication groups, this is a single-element list. For Redis (cluster mode enabled) replication groups, the list contains an entry for each node group (shard).

            
            

            - *(dict) --* 

              Represents a collection of cache nodes in a replication group. One node in the node group is the read/write primary node. All the other nodes are read-only Replica nodes.

              
              

              - **NodeGroupId** *(string) --* 

                The identifier for the node group (shard). A Redis (cluster mode disabled) replication group contains only 1 node group; therefore, the node group ID is 0001. A Redis (cluster mode enabled) replication group contains 1 to 15 node groups numbered 0001 to 0015. 

                
              

              - **Status** *(string) --* 

                The current state of this replication group - ``creating`` , ``available`` , etc.

                
              

              - **PrimaryEndpoint** *(dict) --* 

                The endpoint of the primary node in this node group (shard).

                
                

                - **Address** *(string) --* 

                  The DNS hostname of the cache node.

                  
                

                - **Port** *(integer) --* 

                  The port number that the cache engine is listening on.

                  
            
              

              - **Slots** *(string) --* 

                The keyspace for this node group (shard).

                
              

              - **NodeGroupMembers** *(list) --* 

                A list containing information about individual nodes within the node group (shard).

                
                

                - *(dict) --* 

                  Represents a single node within a node group (shard).

                  
                  

                  - **CacheClusterId** *(string) --* 

                    The ID of the cluster to which the node belongs.

                    
                  

                  - **CacheNodeId** *(string) --* 

                    The ID of the node within its cluster. A node ID is a numeric identifier (0001, 0002, etc.).

                    
                  

                  - **ReadEndpoint** *(dict) --* 

                    Represents the information required for client programs to connect to a cache node.

                    
                    

                    - **Address** *(string) --* 

                      The DNS hostname of the cache node.

                      
                    

                    - **Port** *(integer) --* 

                      The port number that the cache engine is listening on.

                      
                
                  

                  - **PreferredAvailabilityZone** *(string) --* 

                    The name of the Availability Zone in which the node is located.

                    
                  

                  - **CurrentRole** *(string) --* 

                    The role that is currently assigned to the node - ``primary`` or ``replica`` .

                    
              
            
          
        
          

          - **SnapshottingClusterId** *(string) --* 

            The cluster ID that is used as the daily snapshot source for the replication group.

            
          

          - **AutomaticFailover** *(string) --* 

            Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

             

            Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

             

             
            * Redis versions earlier than 2.8.6. 
             
            * Redis (cluster mode disabled): T1 and T2 cache node types. 
             
            * Redis (cluster mode enabled): T1 node types. 
             

            
          

          - **ConfigurationEndpoint** *(dict) --* 

            The configuration endpoint for this replication group. Use the configuration endpoint to connect to this replication group.

            
            

            - **Address** *(string) --* 

              The DNS hostname of the cache node.

              
            

            - **Port** *(integer) --* 

              The port number that the cache engine is listening on.

              
        
          

          - **SnapshotRetentionLimit** *(integer) --* 

            The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was taken today is retained for 5 days before being deleted.

             

            .. warning::

               

              If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

               

            
          

          - **SnapshotWindow** *(string) --* 

            The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).

             

            Example: ``05:00-09:00``  

             

            If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

             

            .. note::

               

              This parameter is only valid if the ``Engine`` parameter is ``redis`` .

               

            
          

          - **ClusterEnabled** *(boolean) --* 

            A flag indicating whether or not this replication group is cluster enabled; i.e., whether its data can be partitioned across multiple shards (API/CLI: node groups).

             

            Valid values: ``true`` | ``false``  

            
          

          - **CacheNodeType** *(string) --* 

            The name of the compute and memory capacity node type for each node in the replication group.

            
          

          - **AuthTokenEnabled** *(boolean) --* 

            A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

             

            Default: ``false``  

            
          

          - **TransitEncryptionEnabled** *(boolean) --* 

            A flag that enables in-transit encryption when set to ``true`` .

             

            You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created. To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to ``true`` when you create a cluster.

             

            Default: ``false``  

            
          

          - **AtRestEncryptionEnabled** *(boolean) --* 

            A flag that enables encryption at-rest when set to ``true`` .

             

            You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true`` when you create a cluster.

             

            Default: ``false``  

            
      
    

  .. py:method:: modify_replication_group_shard_configuration(**kwargs)

    

    Performs horizontal scaling on a Redis (cluster mode enabled) cluster with no downtime. Requires Redis engine version 3.2.10 or newer. For information on upgrading your engine to a newer version, see `Upgrading Engine Versions <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/VersionManagement.html>`__ in the Amazon ElastiCache User Guide.

     

    For more information on ElastiCache for Redis online horizontal scaling, see `ElastiCache for Redis Horizontal Scaling <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/redis-cluster-resharding-online.html>`__  

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/ModifyReplicationGroupShardConfiguration>`_    


    **Request Syntax** 
    ::

      response = client.modify_replication_group_shard_configuration(
          ReplicationGroupId='string',
          NodeGroupCount=123,
          ApplyImmediately=True|False,
          ReshardingConfiguration=[
              {
                  'PreferredAvailabilityZones': [
                      'string',
                  ]
              },
          ],
          NodeGroupsToRemove=[
              'string',
          ]
      )
    :type ReplicationGroupId: string
    :param ReplicationGroupId: **[REQUIRED]** 

      The name of the Redis (cluster mode enabled) cluster (replication group) on which the shards are to be configured.

      

    
    :type NodeGroupCount: integer
    :param NodeGroupCount: **[REQUIRED]** 

      The number of node groups (shards) that results from the modification of the shard configuration.

      

    
    :type ApplyImmediately: boolean
    :param ApplyImmediately: **[REQUIRED]** 

      Indicates that the shard reconfiguration process begins immediately. At present, the only permitted value for this parameter is ``true`` .

       

      Value: true

      

    
    :type ReshardingConfiguration: list
    :param ReshardingConfiguration: 

      Specifies the preferred availability zones for each node group in the cluster. If the value of ``NodeGroupCount`` is greater than the current number of node groups (shards), you can use this parameter to specify the preferred availability zones of the cluster's shards. If you omit this parameter ElastiCache selects availability zones for you.

       

      You can specify this parameter only if the value of ``NodeGroupCount`` is greater than the current number of node groups (shards).

      

    
      - *(dict) --* 

        A list of ``PreferredAvailabilityZones`` objects that specifies the configuration of a node group in the resharded cluster.

        

      
        - **PreferredAvailabilityZones** *(list) --* 

          A list of preferred availability zones for the nodes in this cluster.

          

        
          - *(string) --* 

          
      
      
  
    :type NodeGroupsToRemove: list
    :param NodeGroupsToRemove: 

      If the value of ``NodeGroupCount`` is less than the current number of node groups (shards), ``NodeGroupsToRemove`` is a required list of node group ids to remove from the cluster.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ReplicationGroup': {
                'ReplicationGroupId': 'string',
                'Description': 'string',
                'Status': 'string',
                'PendingModifiedValues': {
                    'PrimaryClusterId': 'string',
                    'AutomaticFailoverStatus': 'enabled'|'disabled',
                    'Resharding': {
                        'SlotMigration': {
                            'ProgressPercentage': 123.0
                        }
                    }
                },
                'MemberClusters': [
                    'string',
                ],
                'NodeGroups': [
                    {
                        'NodeGroupId': 'string',
                        'Status': 'string',
                        'PrimaryEndpoint': {
                            'Address': 'string',
                            'Port': 123
                        },
                        'Slots': 'string',
                        'NodeGroupMembers': [
                            {
                                'CacheClusterId': 'string',
                                'CacheNodeId': 'string',
                                'ReadEndpoint': {
                                    'Address': 'string',
                                    'Port': 123
                                },
                                'PreferredAvailabilityZone': 'string',
                                'CurrentRole': 'string'
                            },
                        ]
                    },
                ],
                'SnapshottingClusterId': 'string',
                'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                'ConfigurationEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'SnapshotRetentionLimit': 123,
                'SnapshotWindow': 'string',
                'ClusterEnabled': True|False,
                'CacheNodeType': 'string',
                'AuthTokenEnabled': True|False,
                'TransitEncryptionEnabled': True|False,
                'AtRestEncryptionEnabled': True|False
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ReplicationGroup** *(dict) --* 

          Contains all of the attributes of a specific Redis replication group.

          
          

          - **ReplicationGroupId** *(string) --* 

            The identifier for the replication group.

            
          

          - **Description** *(string) --* 

            The user supplied description of the replication group.

            
          

          - **Status** *(string) --* 

            The current state of this replication group - ``creating`` , ``available`` , ``modifying`` , ``deleting`` , ``create-failed`` , ``snapshotting`` .

            
          

          - **PendingModifiedValues** *(dict) --* 

            A group of settings to be applied to the replication group, either immediately or during the next maintenance window.

            
            

            - **PrimaryClusterId** *(string) --* 

              The primary cluster ID that is applied immediately (if ``--apply-immediately`` was specified), or during the next maintenance window.

              
            

            - **AutomaticFailoverStatus** *(string) --* 

              Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

               

              Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

               

               
              * Redis versions earlier than 2.8.6. 
               
              * Redis (cluster mode disabled): T1 and T2 cache node types. 
               
              * Redis (cluster mode enabled): T1 node types. 
               

              
            

            - **Resharding** *(dict) --* 

              The status of an online resharding operation.

              
              

              - **SlotMigration** *(dict) --* 

                Represents the progress of an online resharding operation.

                
                

                - **ProgressPercentage** *(float) --* 

                  The percentage of the slot migration that is complete.

                  
            
          
        
          

          - **MemberClusters** *(list) --* 

            The identifiers of all the nodes that are part of this replication group.

            
            

            - *(string) --* 
        
          

          - **NodeGroups** *(list) --* 

            A list of node groups in this replication group. For Redis (cluster mode disabled) replication groups, this is a single-element list. For Redis (cluster mode enabled) replication groups, the list contains an entry for each node group (shard).

            
            

            - *(dict) --* 

              Represents a collection of cache nodes in a replication group. One node in the node group is the read/write primary node. All the other nodes are read-only Replica nodes.

              
              

              - **NodeGroupId** *(string) --* 

                The identifier for the node group (shard). A Redis (cluster mode disabled) replication group contains only 1 node group; therefore, the node group ID is 0001. A Redis (cluster mode enabled) replication group contains 1 to 15 node groups numbered 0001 to 0015. 

                
              

              - **Status** *(string) --* 

                The current state of this replication group - ``creating`` , ``available`` , etc.

                
              

              - **PrimaryEndpoint** *(dict) --* 

                The endpoint of the primary node in this node group (shard).

                
                

                - **Address** *(string) --* 

                  The DNS hostname of the cache node.

                  
                

                - **Port** *(integer) --* 

                  The port number that the cache engine is listening on.

                  
            
              

              - **Slots** *(string) --* 

                The keyspace for this node group (shard).

                
              

              - **NodeGroupMembers** *(list) --* 

                A list containing information about individual nodes within the node group (shard).

                
                

                - *(dict) --* 

                  Represents a single node within a node group (shard).

                  
                  

                  - **CacheClusterId** *(string) --* 

                    The ID of the cluster to which the node belongs.

                    
                  

                  - **CacheNodeId** *(string) --* 

                    The ID of the node within its cluster. A node ID is a numeric identifier (0001, 0002, etc.).

                    
                  

                  - **ReadEndpoint** *(dict) --* 

                    Represents the information required for client programs to connect to a cache node.

                    
                    

                    - **Address** *(string) --* 

                      The DNS hostname of the cache node.

                      
                    

                    - **Port** *(integer) --* 

                      The port number that the cache engine is listening on.

                      
                
                  

                  - **PreferredAvailabilityZone** *(string) --* 

                    The name of the Availability Zone in which the node is located.

                    
                  

                  - **CurrentRole** *(string) --* 

                    The role that is currently assigned to the node - ``primary`` or ``replica`` .

                    
              
            
          
        
          

          - **SnapshottingClusterId** *(string) --* 

            The cluster ID that is used as the daily snapshot source for the replication group.

            
          

          - **AutomaticFailover** *(string) --* 

            Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

             

            Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

             

             
            * Redis versions earlier than 2.8.6. 
             
            * Redis (cluster mode disabled): T1 and T2 cache node types. 
             
            * Redis (cluster mode enabled): T1 node types. 
             

            
          

          - **ConfigurationEndpoint** *(dict) --* 

            The configuration endpoint for this replication group. Use the configuration endpoint to connect to this replication group.

            
            

            - **Address** *(string) --* 

              The DNS hostname of the cache node.

              
            

            - **Port** *(integer) --* 

              The port number that the cache engine is listening on.

              
        
          

          - **SnapshotRetentionLimit** *(integer) --* 

            The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was taken today is retained for 5 days before being deleted.

             

            .. warning::

               

              If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

               

            
          

          - **SnapshotWindow** *(string) --* 

            The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).

             

            Example: ``05:00-09:00``  

             

            If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

             

            .. note::

               

              This parameter is only valid if the ``Engine`` parameter is ``redis`` .

               

            
          

          - **ClusterEnabled** *(boolean) --* 

            A flag indicating whether or not this replication group is cluster enabled; i.e., whether its data can be partitioned across multiple shards (API/CLI: node groups).

             

            Valid values: ``true`` | ``false``  

            
          

          - **CacheNodeType** *(string) --* 

            The name of the compute and memory capacity node type for each node in the replication group.

            
          

          - **AuthTokenEnabled** *(boolean) --* 

            A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

             

            Default: ``false``  

            
          

          - **TransitEncryptionEnabled** *(boolean) --* 

            A flag that enables in-transit encryption when set to ``true`` .

             

            You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created. To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to ``true`` when you create a cluster.

             

            Default: ``false``  

            
          

          - **AtRestEncryptionEnabled** *(boolean) --* 

            A flag that enables encryption at-rest when set to ``true`` .

             

            You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true`` when you create a cluster.

             

            Default: ``false``  

            
      
    

  .. py:method:: purchase_reserved_cache_nodes_offering(**kwargs)

    

    Allows you to purchase a reserved cache node offering.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/PurchaseReservedCacheNodesOffering>`_    


    **Request Syntax** 
    ::

      response = client.purchase_reserved_cache_nodes_offering(
          ReservedCacheNodesOfferingId='string',
          ReservedCacheNodeId='string',
          CacheNodeCount=123
      )
    :type ReservedCacheNodesOfferingId: string
    :param ReservedCacheNodesOfferingId: **[REQUIRED]** 

      The ID of the reserved cache node offering to purchase.

       

      Example: ``438012d3-4052-4cc7-b2e3-8d3372e0e706``  

      

    
    :type ReservedCacheNodeId: string
    :param ReservedCacheNodeId: 

      A customer-specified identifier to track this reservation.

       

      .. note::

         

        The Reserved Cache Node ID is an unique customer-specified identifier to track this reservation. If this parameter is not specified, ElastiCache automatically generates an identifier for the reservation.

         

       

      Example: myreservationID

      

    
    :type CacheNodeCount: integer
    :param CacheNodeCount: 

      The number of cache node instances to reserve.

       

      Default: ``1``  

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ReservedCacheNode': {
                'ReservedCacheNodeId': 'string',
                'ReservedCacheNodesOfferingId': 'string',
                'CacheNodeType': 'string',
                'StartTime': datetime(2015, 1, 1),
                'Duration': 123,
                'FixedPrice': 123.0,
                'UsagePrice': 123.0,
                'CacheNodeCount': 123,
                'ProductDescription': 'string',
                'OfferingType': 'string',
                'State': 'string',
                'RecurringCharges': [
                    {
                        'RecurringChargeAmount': 123.0,
                        'RecurringChargeFrequency': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ReservedCacheNode** *(dict) --* 

          Represents the output of a ``PurchaseReservedCacheNodesOffering`` operation.

          
          

          - **ReservedCacheNodeId** *(string) --* 

            The unique identifier for the reservation.

            
          

          - **ReservedCacheNodesOfferingId** *(string) --* 

            The offering identifier.

            
          

          - **CacheNodeType** *(string) --* 

            The cache node type for the reserved cache nodes.

             

            The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

             

             
            * General purpose: 

               
              * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
               
              * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
               

             
             
            * Compute optimized: 

               
              * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
               

             
             
            * Memory optimized: 

               
              * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
               
              * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
               

             
             

             

             **Notes:**  

             

             
            * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
             
            * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
             
            * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
             
            * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
             

             

            For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

            
          

          - **StartTime** *(datetime) --* 

            The time the reservation started.

            
          

          - **Duration** *(integer) --* 

            The duration of the reservation in seconds.

            
          

          - **FixedPrice** *(float) --* 

            The fixed price charged for this reserved cache node.

            
          

          - **UsagePrice** *(float) --* 

            The hourly price charged for this reserved cache node.

            
          

          - **CacheNodeCount** *(integer) --* 

            The number of cache nodes that have been reserved.

            
          

          - **ProductDescription** *(string) --* 

            The description of the reserved cache node.

            
          

          - **OfferingType** *(string) --* 

            The offering type of this reserved cache node.

            
          

          - **State** *(string) --* 

            The state of the reserved cache node.

            
          

          - **RecurringCharges** *(list) --* 

            The recurring price charged to run this reserved cache node.

            
            

            - *(dict) --* 

              Contains the specific price and frequency of a recurring charges for a reserved cache node, or for a reserved cache node offering.

              
              

              - **RecurringChargeAmount** *(float) --* 

                The monetary amount of the recurring charge.

                
              

              - **RecurringChargeFrequency** *(string) --* 

                The frequency of the recurring charge.

                
          
        
      
    

  .. py:method:: reboot_cache_cluster(**kwargs)

    

    Reboots some, or all, of the cache nodes within a provisioned cluster. This operation applies any modified cache parameter groups to the cluster. The reboot operation takes place as soon as possible, and results in a momentary outage to the cluster. During the reboot, the cluster status is set to REBOOTING.

     

    The reboot causes the contents of the cache (for each cache node being rebooted) to be lost.

     

    When the reboot is complete, a cluster event is created.

     

    Rebooting a cluster is currently supported on Memcached and Redis (cluster mode disabled) clusters. Rebooting is not supported on Redis (cluster mode enabled) clusters.

     

    If you make changes to parameters that require a Redis (cluster mode enabled) cluster reboot for the changes to be applied, see `Rebooting a Cluster <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Clusters.Rebooting.htm>`__ for an alternate process.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/RebootCacheCluster>`_    


    **Request Syntax** 
    ::

      response = client.reboot_cache_cluster(
          CacheClusterId='string',
          CacheNodeIdsToReboot=[
              'string',
          ]
      )
    :type CacheClusterId: string
    :param CacheClusterId: **[REQUIRED]** 

      The cluster identifier. This parameter is stored as a lowercase string.

      

    
    :type CacheNodeIdsToReboot: list
    :param CacheNodeIdsToReboot: **[REQUIRED]** 

      A list of cache node IDs to reboot. A node ID is a numeric identifier (0001, 0002, etc.). To reboot an entire cluster, specify all of the cache node IDs.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CacheCluster': {
                'CacheClusterId': 'string',
                'ConfigurationEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'ClientDownloadLandingPage': 'string',
                'CacheNodeType': 'string',
                'Engine': 'string',
                'EngineVersion': 'string',
                'CacheClusterStatus': 'string',
                'NumCacheNodes': 123,
                'PreferredAvailabilityZone': 'string',
                'CacheClusterCreateTime': datetime(2015, 1, 1),
                'PreferredMaintenanceWindow': 'string',
                'PendingModifiedValues': {
                    'NumCacheNodes': 123,
                    'CacheNodeIdsToRemove': [
                        'string',
                    ],
                    'EngineVersion': 'string',
                    'CacheNodeType': 'string'
                },
                'NotificationConfiguration': {
                    'TopicArn': 'string',
                    'TopicStatus': 'string'
                },
                'CacheSecurityGroups': [
                    {
                        'CacheSecurityGroupName': 'string',
                        'Status': 'string'
                    },
                ],
                'CacheParameterGroup': {
                    'CacheParameterGroupName': 'string',
                    'ParameterApplyStatus': 'string',
                    'CacheNodeIdsToReboot': [
                        'string',
                    ]
                },
                'CacheSubnetGroupName': 'string',
                'CacheNodes': [
                    {
                        'CacheNodeId': 'string',
                        'CacheNodeStatus': 'string',
                        'CacheNodeCreateTime': datetime(2015, 1, 1),
                        'Endpoint': {
                            'Address': 'string',
                            'Port': 123
                        },
                        'ParameterGroupStatus': 'string',
                        'SourceCacheNodeId': 'string',
                        'CustomerAvailabilityZone': 'string'
                    },
                ],
                'AutoMinorVersionUpgrade': True|False,
                'SecurityGroups': [
                    {
                        'SecurityGroupId': 'string',
                        'Status': 'string'
                    },
                ],
                'ReplicationGroupId': 'string',
                'SnapshotRetentionLimit': 123,
                'SnapshotWindow': 'string',
                'AuthTokenEnabled': True|False,
                'TransitEncryptionEnabled': True|False,
                'AtRestEncryptionEnabled': True|False
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CacheCluster** *(dict) --* 

          Contains all of the attributes of a specific cluster.

          
          

          - **CacheClusterId** *(string) --* 

            The user-supplied identifier of the cluster. This identifier is a unique key that identifies a cluster.

            
          

          - **ConfigurationEndpoint** *(dict) --* 

            Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the cluster, can be used by an application to connect to any node in the cluster. The configuration endpoint will always have ``.cfg`` in it.

             

            Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``  

            
            

            - **Address** *(string) --* 

              The DNS hostname of the cache node.

              
            

            - **Port** *(integer) --* 

              The port number that the cache engine is listening on.

              
        
          

          - **ClientDownloadLandingPage** *(string) --* 

            The URL of the web page where you can download the latest ElastiCache client library.

            
          

          - **CacheNodeType** *(string) --* 

            The name of the compute and memory capacity node type for the cluster.

             

            The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

             

             
            * General purpose: 

               
              * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
               
              * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
               

             
             
            * Compute optimized: 

               
              * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
               

             
             
            * Memory optimized: 

               
              * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
               
              * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
               

             
             

             

             **Notes:**  

             

             
            * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
             
            * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
             
            * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
             
            * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
             

             

            For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

            
          

          - **Engine** *(string) --* 

            The name of the cache engine (``memcached`` or ``redis`` ) to be used for this cluster.

            
          

          - **EngineVersion** *(string) --* 

            The version of the cache engine that is used in this cluster.

            
          

          - **CacheClusterStatus** *(string) --* 

            The current state of this cluster, one of the following values: ``available`` , ``creating`` , ``deleted`` , ``deleting`` , ``incompatible-network`` , ``modifying`` , ``rebooting cluster nodes`` , ``restore-failed`` , or ``snapshotting`` .

            
          

          - **NumCacheNodes** *(integer) --* 

            The number of cache nodes in the cluster.

             

            For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

            
          

          - **PreferredAvailabilityZone** *(string) --* 

            The name of the Availability Zone in which the cluster is located or "Multiple" if the cache nodes are located in different Availability Zones.

            
          

          - **CacheClusterCreateTime** *(datetime) --* 

            The date and time when the cluster was created.

            
          

          - **PreferredMaintenanceWindow** *(string) --* 

            Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.

             

            Valid values for ``ddd`` are:

             

             
            * ``sun``   
             
            * ``mon``   
             
            * ``tue``   
             
            * ``wed``   
             
            * ``thu``   
             
            * ``fri``   
             
            * ``sat``   
             

             

            Example: ``sun:23:00-mon:01:30``  

            
          

          - **PendingModifiedValues** *(dict) --* 

            A group of settings that are applied to the cluster in the future, or that are currently being applied.

            
            

            - **NumCacheNodes** *(integer) --* 

              The new number of cache nodes for the cluster.

               

              For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

              
            

            - **CacheNodeIdsToRemove** *(list) --* 

              A list of cache node IDs that are being removed (or will be removed) from the cluster. A node ID is a numeric identifier (0001, 0002, etc.).

              
              

              - *(string) --* 
          
            

            - **EngineVersion** *(string) --* 

              The new cache engine version that the cluster runs.

              
            

            - **CacheNodeType** *(string) --* 

              The cache node type that this cluster or replication group is scaled to.

              
        
          

          - **NotificationConfiguration** *(dict) --* 

            Describes a notification topic and its status. Notification topics are used for publishing ElastiCache events to subscribers using Amazon Simple Notification Service (SNS). 

            
            

            - **TopicArn** *(string) --* 

              The Amazon Resource Name (ARN) that identifies the topic.

              
            

            - **TopicStatus** *(string) --* 

              The current state of the topic.

              
        
          

          - **CacheSecurityGroups** *(list) --* 

            A list of cache security group elements, composed of name and status sub-elements.

            
            

            - *(dict) --* 

              Represents a cluster's status within a particular cache security group.

              
              

              - **CacheSecurityGroupName** *(string) --* 

                The name of the cache security group.

                
              

              - **Status** *(string) --* 

                The membership status in the cache security group. The status changes when a cache security group is modified, or when the cache security groups assigned to a cluster are modified.

                
          
        
          

          - **CacheParameterGroup** *(dict) --* 

            Status of the cache parameter group.

            
            

            - **CacheParameterGroupName** *(string) --* 

              The name of the cache parameter group.

              
            

            - **ParameterApplyStatus** *(string) --* 

              The status of parameter updates.

              
            

            - **CacheNodeIdsToReboot** *(list) --* 

              A list of the cache node IDs which need to be rebooted for parameter changes to be applied. A node ID is a numeric identifier (0001, 0002, etc.).

              
              

              - *(string) --* 
          
        
          

          - **CacheSubnetGroupName** *(string) --* 

            The name of the cache subnet group associated with the cluster.

            
          

          - **CacheNodes** *(list) --* 

            A list of cache nodes that are members of the cluster.

            
            

            - *(dict) --* 

              Represents an individual cache node within a cluster. Each cache node runs its own instance of the cluster's protocol-compliant caching software - either Memcached or Redis.

               

              The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

               

               
              * General purpose: 

                 
                * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
                 
                * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
                 

               
               
              * Compute optimized: 

                 
                * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
                 

               
               
              * Memory optimized: 

                 
                * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
                 
                * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
                 

               
               

               

               **Notes:**  

               

               
              * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
               
              * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
               
              * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
               
              * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
               

               

              For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

              
              

              - **CacheNodeId** *(string) --* 

                The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The combination of cluster ID and node ID uniquely identifies every cache node used in a customer's AWS account.

                
              

              - **CacheNodeStatus** *(string) --* 

                The current state of this cache node.

                
              

              - **CacheNodeCreateTime** *(datetime) --* 

                The date and time when the cache node was created.

                
              

              - **Endpoint** *(dict) --* 

                The hostname for connecting to this cache node.

                
                

                - **Address** *(string) --* 

                  The DNS hostname of the cache node.

                  
                

                - **Port** *(integer) --* 

                  The port number that the cache engine is listening on.

                  
            
              

              - **ParameterGroupStatus** *(string) --* 

                The status of the parameter group applied to this cache node.

                
              

              - **SourceCacheNodeId** *(string) --* 

                The ID of the primary node to which this read replica node is synchronized. If this field is empty, this node is not associated with a primary cluster.

                
              

              - **CustomerAvailabilityZone** *(string) --* 

                The Availability Zone where this node was created and now resides.

                
          
        
          

          - **AutoMinorVersionUpgrade** *(boolean) --* 

            This parameter is currently disabled.

            
          

          - **SecurityGroups** *(list) --* 

            A list of VPC Security Groups associated with the cluster.

            
            

            - *(dict) --* 

              Represents a single cache security group and its status.

              
              

              - **SecurityGroupId** *(string) --* 

                The identifier of the cache security group.

                
              

              - **Status** *(string) --* 

                The status of the cache security group membership. The status changes whenever a cache security group is modified, or when the cache security groups assigned to a cluster are modified.

                
          
        
          

          - **ReplicationGroupId** *(string) --* 

            The replication group to which this cluster belongs. If this field is empty, the cluster is not associated with any replication group.

            
          

          - **SnapshotRetentionLimit** *(integer) --* 

            The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was taken today is retained for 5 days before being deleted.

             

            .. warning::

               

              If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

               

            
          

          - **SnapshotWindow** *(string) --* 

            The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your cluster.

             

            Example: ``05:00-09:00``  

            
          

          - **AuthTokenEnabled** *(boolean) --* 

            A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

             

            Default: ``false``  

            
          

          - **TransitEncryptionEnabled** *(boolean) --* 

            A flag that enables in-transit encryption when set to ``true`` .

             

            You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created. To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to ``true`` when you create a cluster.

             

            Default: ``false``  

            
          

          - **AtRestEncryptionEnabled** *(boolean) --* 

            A flag that enables encryption at-rest when set to ``true`` .

             

            You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To enable at-rest encryption on a cluster you must set ``AtRestEncryptionEnabled`` to ``true`` when you create a cluster.

             

            Default: ``false``  

            
      
    

  .. py:method:: remove_tags_from_resource(**kwargs)

    

    Removes the tags identified by the ``TagKeys`` list from the named resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/RemoveTagsFromResource>`_    


    **Request Syntax** 
    ::

      response = client.remove_tags_from_resource(
          ResourceName='string',
          TagKeys=[
              'string',
          ]
      )
    :type ResourceName: string
    :param ResourceName: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the resource from which you want the tags removed, for example ``arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster`` or ``arn:aws:elasticache:us-west-2:0123456789:snapshot:mySnapshot`` .

       

      For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      

    
    :type TagKeys: list
    :param TagKeys: **[REQUIRED]** 

      A list of ``TagKeys`` identifying the tags you want removed from the named resource.

      

    
      - *(string) --* 

      
  
    
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

        Represents the output from the ``AddTagsToResource`` , ``ListTagsForResource`` , and ``RemoveTagsFromResource`` operations.

        
        

        - **TagList** *(list) --* 

          A list of cost allocation tags as key-value pairs.

          
          

          - *(dict) --* 

            A cost allocation Tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. A tag with a null Value is permitted.

            
            

            - **Key** *(string) --* 

              The key for the tag. May not be null.

              
            

            - **Value** *(string) --* 

              The tag's value. May be null.

              
        
      
    

  .. py:method:: reset_cache_parameter_group(**kwargs)

    

    Modifies the parameters of a cache parameter group to the engine or system default value. You can reset specific parameters by submitting a list of parameter names. To reset the entire cache parameter group, specify the ``ResetAllParameters`` and ``CacheParameterGroupName`` parameters.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/ResetCacheParameterGroup>`_    


    **Request Syntax** 
    ::

      response = client.reset_cache_parameter_group(
          CacheParameterGroupName='string',
          ResetAllParameters=True|False,
          ParameterNameValues=[
              {
                  'ParameterName': 'string',
                  'ParameterValue': 'string'
              },
          ]
      )
    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: **[REQUIRED]** 

      The name of the cache parameter group to reset.

      

    
    :type ResetAllParameters: boolean
    :param ResetAllParameters: 

      If ``true`` , all parameters in the cache parameter group are reset to their default values. If ``false`` , only the parameters listed by ``ParameterNameValues`` are reset to their default values.

       

      Valid values: ``true`` | ``false``  

      

    
    :type ParameterNameValues: list
    :param ParameterNameValues: 

      An array of parameter names to reset to their default values. If ``ResetAllParameters`` is ``true`` , do not use ``ParameterNameValues`` . If ``ResetAllParameters`` is ``false`` , you must specify the name of at least one parameter to reset.

      

    
      - *(dict) --* 

        Describes a name-value pair that is used to update the value of a parameter.

        

      
        - **ParameterName** *(string) --* 

          The name of the parameter.

          

        
        - **ParameterValue** *(string) --* 

          The value of the parameter.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CacheParameterGroupName': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of one of the following operations:

         

         
        * ``ModifyCacheParameterGroup``   
         
        * ``ResetCacheParameterGroup``   
         

        
        

        - **CacheParameterGroupName** *(string) --* 

          The name of the cache parameter group.

          
    

  .. py:method:: revoke_cache_security_group_ingress(**kwargs)

    

    Revokes ingress from a cache security group. Use this operation to disallow access from an Amazon EC2 security group that had been previously authorized.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/RevokeCacheSecurityGroupIngress>`_    


    **Request Syntax** 
    ::

      response = client.revoke_cache_security_group_ingress(
          CacheSecurityGroupName='string',
          EC2SecurityGroupName='string',
          EC2SecurityGroupOwnerId='string'
      )
    :type CacheSecurityGroupName: string
    :param CacheSecurityGroupName: **[REQUIRED]** 

      The name of the cache security group to revoke ingress from.

      

    
    :type EC2SecurityGroupName: string
    :param EC2SecurityGroupName: **[REQUIRED]** 

      The name of the Amazon EC2 security group to revoke access from.

      

    
    :type EC2SecurityGroupOwnerId: string
    :param EC2SecurityGroupOwnerId: **[REQUIRED]** 

      The AWS account number of the Amazon EC2 security group owner. Note that this is not the same thing as an AWS access key ID - you must provide a valid AWS account number for this parameter.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CacheSecurityGroup': {
                'OwnerId': 'string',
                'CacheSecurityGroupName': 'string',
                'Description': 'string',
                'EC2SecurityGroups': [
                    {
                        'Status': 'string',
                        'EC2SecurityGroupName': 'string',
                        'EC2SecurityGroupOwnerId': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CacheSecurityGroup** *(dict) --* 

          Represents the output of one of the following operations:

           

           
          * ``AuthorizeCacheSecurityGroupIngress``   
           
          * ``CreateCacheSecurityGroup``   
           
          * ``RevokeCacheSecurityGroupIngress``   
           

          
          

          - **OwnerId** *(string) --* 

            The AWS account ID of the cache security group owner.

            
          

          - **CacheSecurityGroupName** *(string) --* 

            The name of the cache security group.

            
          

          - **Description** *(string) --* 

            The description of the cache security group.

            
          

          - **EC2SecurityGroups** *(list) --* 

            A list of Amazon EC2 security groups that are associated with this cache security group.

            
            

            - *(dict) --* 

              Provides ownership and status information for an Amazon EC2 security group.

              
              

              - **Status** *(string) --* 

                The status of the Amazon EC2 security group.

                
              

              - **EC2SecurityGroupName** *(string) --* 

                The name of the Amazon EC2 security group.

                
              

              - **EC2SecurityGroupOwnerId** *(string) --* 

                The AWS account ID of the Amazon EC2 security group owner.

                
          
        
      
    

  .. py:method:: test_failover(**kwargs)

    

    Represents the input of a ``TestFailover`` operation which test automatic failover on a specified node group (called shard in the console) in a replication group (called cluster in the console).

     

     **Note the following**  

     

     
    * A customer can use this operation to test automatic failover on up to 5 shards (called node groups in the ElastiCache API and AWS CLI) in any rolling 24-hour period. 
     
    * If calling this operation on shards in different clusters (called replication groups in the API and CLI), the calls can be made concurrently.   
     
    * If calling this operation multiple times on different shards in the same Redis (cluster mode enabled) replication group, the first node replacement must complete before a subsequent call can be made. 
     
    * To determine whether the node replacement is complete you can check Events using the Amazon ElastiCache console, the AWS CLI, or the ElastiCache API. Look for the following automatic failover related events, listed here in order of occurrance: 

       
      * Replication group message: ``Test Failover API called for node group <node-group-id>``   
       
      * Cache cluster message: ``Failover from master node <primary-node-id> to replica node <node-id> completed``   
       
      * Replication group message: ``Failover from master node <primary-node-id> to replica node <node-id> completed``   
       
      * Cache cluster message: ``Recovering cache nodes <node-id>``   
       
      * Cache cluster message: ``Finished recovery for cache nodes <node-id>``   
       

     

    For more information see:

     

       
      * `Viewing ElastiCache Events <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/ECEvents.Viewing.html>`__ in the *ElastiCache User Guide*   
       
      * `DescribeEvents <http://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeEvents.html>`__ in the ElastiCache API Reference 
       

     
     

     

    Also see, `Testing Multi-AZ with Automatic Failover <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/AutoFailover.html#auto-failover-test>`__ in the *ElastiCache User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/TestFailover>`_    


    **Request Syntax** 
    ::

      response = client.test_failover(
          ReplicationGroupId='string',
          NodeGroupId='string'
      )
    :type ReplicationGroupId: string
    :param ReplicationGroupId: **[REQUIRED]** 

      The name of the replication group (console: cluster) whose automatic failover is being tested by this operation.

      

    
    :type NodeGroupId: string
    :param NodeGroupId: **[REQUIRED]** 

      The name of the node group (called shard in the console) in this replication group on which automatic failover is to be tested. You may test automatic failover on up to 5 node groups in any rolling 24-hour period.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ReplicationGroup': {
                'ReplicationGroupId': 'string',
                'Description': 'string',
                'Status': 'string',
                'PendingModifiedValues': {
                    'PrimaryClusterId': 'string',
                    'AutomaticFailoverStatus': 'enabled'|'disabled',
                    'Resharding': {
                        'SlotMigration': {
                            'ProgressPercentage': 123.0
                        }
                    }
                },
                'MemberClusters': [
                    'string',
                ],
                'NodeGroups': [
                    {
                        'NodeGroupId': 'string',
                        'Status': 'string',
                        'PrimaryEndpoint': {
                            'Address': 'string',
                            'Port': 123
                        },
                        'Slots': 'string',
                        'NodeGroupMembers': [
                            {
                                'CacheClusterId': 'string',
                                'CacheNodeId': 'string',
                                'ReadEndpoint': {
                                    'Address': 'string',
                                    'Port': 123
                                },
                                'PreferredAvailabilityZone': 'string',
                                'CurrentRole': 'string'
                            },
                        ]
                    },
                ],
                'SnapshottingClusterId': 'string',
                'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                'ConfigurationEndpoint': {
                    'Address': 'string',
                    'Port': 123
                },
                'SnapshotRetentionLimit': 123,
                'SnapshotWindow': 'string',
                'ClusterEnabled': True|False,
                'CacheNodeType': 'string',
                'AuthTokenEnabled': True|False,
                'TransitEncryptionEnabled': True|False,
                'AtRestEncryptionEnabled': True|False
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ReplicationGroup** *(dict) --* 

          Contains all of the attributes of a specific Redis replication group.

          
          

          - **ReplicationGroupId** *(string) --* 

            The identifier for the replication group.

            
          

          - **Description** *(string) --* 

            The user supplied description of the replication group.

            
          

          - **Status** *(string) --* 

            The current state of this replication group - ``creating`` , ``available`` , ``modifying`` , ``deleting`` , ``create-failed`` , ``snapshotting`` .

            
          

          - **PendingModifiedValues** *(dict) --* 

            A group of settings to be applied to the replication group, either immediately or during the next maintenance window.

            
            

            - **PrimaryClusterId** *(string) --* 

              The primary cluster ID that is applied immediately (if ``--apply-immediately`` was specified), or during the next maintenance window.

              
            

            - **AutomaticFailoverStatus** *(string) --* 

              Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

               

              Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

               

               
              * Redis versions earlier than 2.8.6. 
               
              * Redis (cluster mode disabled): T1 and T2 cache node types. 
               
              * Redis (cluster mode enabled): T1 node types. 
               

              
            

            - **Resharding** *(dict) --* 

              The status of an online resharding operation.

              
              

              - **SlotMigration** *(dict) --* 

                Represents the progress of an online resharding operation.

                
                

                - **ProgressPercentage** *(float) --* 

                  The percentage of the slot migration that is complete.

                  
            
          
        
          

          - **MemberClusters** *(list) --* 

            The identifiers of all the nodes that are part of this replication group.

            
            

            - *(string) --* 
        
          

          - **NodeGroups** *(list) --* 

            A list of node groups in this replication group. For Redis (cluster mode disabled) replication groups, this is a single-element list. For Redis (cluster mode enabled) replication groups, the list contains an entry for each node group (shard).

            
            

            - *(dict) --* 

              Represents a collection of cache nodes in a replication group. One node in the node group is the read/write primary node. All the other nodes are read-only Replica nodes.

              
              

              - **NodeGroupId** *(string) --* 

                The identifier for the node group (shard). A Redis (cluster mode disabled) replication group contains only 1 node group; therefore, the node group ID is 0001. A Redis (cluster mode enabled) replication group contains 1 to 15 node groups numbered 0001 to 0015. 

                
              

              - **Status** *(string) --* 

                The current state of this replication group - ``creating`` , ``available`` , etc.

                
              

              - **PrimaryEndpoint** *(dict) --* 

                The endpoint of the primary node in this node group (shard).

                
                

                - **Address** *(string) --* 

                  The DNS hostname of the cache node.

                  
                

                - **Port** *(integer) --* 

                  The port number that the cache engine is listening on.

                  
            
              

              - **Slots** *(string) --* 

                The keyspace for this node group (shard).

                
              

              - **NodeGroupMembers** *(list) --* 

                A list containing information about individual nodes within the node group (shard).

                
                

                - *(dict) --* 

                  Represents a single node within a node group (shard).

                  
                  

                  - **CacheClusterId** *(string) --* 

                    The ID of the cluster to which the node belongs.

                    
                  

                  - **CacheNodeId** *(string) --* 

                    The ID of the node within its cluster. A node ID is a numeric identifier (0001, 0002, etc.).

                    
                  

                  - **ReadEndpoint** *(dict) --* 

                    Represents the information required for client programs to connect to a cache node.

                    
                    

                    - **Address** *(string) --* 

                      The DNS hostname of the cache node.

                      
                    

                    - **Port** *(integer) --* 

                      The port number that the cache engine is listening on.

                      
                
                  

                  - **PreferredAvailabilityZone** *(string) --* 

                    The name of the Availability Zone in which the node is located.

                    
                  

                  - **CurrentRole** *(string) --* 

                    The role that is currently assigned to the node - ``primary`` or ``replica`` .

                    
              
            
          
        
          

          - **SnapshottingClusterId** *(string) --* 

            The cluster ID that is used as the daily snapshot source for the replication group.

            
          

          - **AutomaticFailover** *(string) --* 

            Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

             

            Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

             

             
            * Redis versions earlier than 2.8.6. 
             
            * Redis (cluster mode disabled): T1 and T2 cache node types. 
             
            * Redis (cluster mode enabled): T1 node types. 
             

            
          

          - **ConfigurationEndpoint** *(dict) --* 

            The configuration endpoint for this replication group. Use the configuration endpoint to connect to this replication group.

            
            

            - **Address** *(string) --* 

              The DNS hostname of the cache node.

              
            

            - **Port** *(integer) --* 

              The port number that the cache engine is listening on.

              
        
          

          - **SnapshotRetentionLimit** *(integer) --* 

            The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was taken today is retained for 5 days before being deleted.

             

            .. warning::

               

              If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

               

            
          

          - **SnapshotWindow** *(string) --* 

            The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).

             

            Example: ``05:00-09:00``  

             

            If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

             

            .. note::

               

              This parameter is only valid if the ``Engine`` parameter is ``redis`` .

               

            
          

          - **ClusterEnabled** *(boolean) --* 

            A flag indicating whether or not this replication group is cluster enabled; i.e., whether its data can be partitioned across multiple shards (API/CLI: node groups).

             

            Valid values: ``true`` | ``false``  

            
          

          - **CacheNodeType** *(string) --* 

            The name of the compute and memory capacity node type for each node in the replication group.

            
          

          - **AuthTokenEnabled** *(boolean) --* 

            A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

             

            Default: ``false``  

            
          

          - **TransitEncryptionEnabled** *(boolean) --* 

            A flag that enables in-transit encryption when set to ``true`` .

             

            You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created. To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to ``true`` when you create a cluster.

             

            Default: ``false``  

            
          

          - **AtRestEncryptionEnabled** *(boolean) --* 

            A flag that enables encryption at-rest when set to ``true`` .

             

            You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true`` when you create a cluster.

             

            Default: ``false``  

            
      
    

==========
Paginators
==========


The available paginators are:

* :py:class:`ElastiCache.Paginator.DescribeCacheClusters`


* :py:class:`ElastiCache.Paginator.DescribeCacheEngineVersions`


* :py:class:`ElastiCache.Paginator.DescribeCacheParameterGroups`


* :py:class:`ElastiCache.Paginator.DescribeCacheParameters`


* :py:class:`ElastiCache.Paginator.DescribeCacheSecurityGroups`


* :py:class:`ElastiCache.Paginator.DescribeCacheSubnetGroups`


* :py:class:`ElastiCache.Paginator.DescribeEngineDefaultParameters`


* :py:class:`ElastiCache.Paginator.DescribeEvents`


* :py:class:`ElastiCache.Paginator.DescribeReplicationGroups`


* :py:class:`ElastiCache.Paginator.DescribeReservedCacheNodes`


* :py:class:`ElastiCache.Paginator.DescribeReservedCacheNodesOfferings`


* :py:class:`ElastiCache.Paginator.DescribeSnapshots`



.. py:class:: ElastiCache.Paginator.DescribeCacheClusters

  ::

    
    paginator = client.get_paginator('describe_cache_clusters')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ElastiCache.Client.describe_cache_clusters`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheClusters>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          CacheClusterId='string',
          ShowCacheNodeInfo=True|False,
          ShowCacheClustersNotInReplicationGroups=True|False,
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type CacheClusterId: string
    :param CacheClusterId: 

      The user-supplied cluster identifier. If this parameter is specified, only information about that specific cluster is returned. This parameter isn't case sensitive.

      

    
    :type ShowCacheNodeInfo: boolean
    :param ShowCacheNodeInfo: 

      An optional flag that can be included in the ``DescribeCacheCluster`` request to retrieve information about the individual cache nodes.

      

    
    :type ShowCacheClustersNotInReplicationGroups: boolean
    :param ShowCacheClustersNotInReplicationGroups: 

      An optional flag that can be included in the ``DescribeCacheCluster`` request to show only nodes (API/CLI: clusters) that are not members of a replication group. In practice, this mean Memcached and single node Redis clusters.

      

    
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
            'CacheClusters': [
                {
                    'CacheClusterId': 'string',
                    'ConfigurationEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'ClientDownloadLandingPage': 'string',
                    'CacheNodeType': 'string',
                    'Engine': 'string',
                    'EngineVersion': 'string',
                    'CacheClusterStatus': 'string',
                    'NumCacheNodes': 123,
                    'PreferredAvailabilityZone': 'string',
                    'CacheClusterCreateTime': datetime(2015, 1, 1),
                    'PreferredMaintenanceWindow': 'string',
                    'PendingModifiedValues': {
                        'NumCacheNodes': 123,
                        'CacheNodeIdsToRemove': [
                            'string',
                        ],
                        'EngineVersion': 'string',
                        'CacheNodeType': 'string'
                    },
                    'NotificationConfiguration': {
                        'TopicArn': 'string',
                        'TopicStatus': 'string'
                    },
                    'CacheSecurityGroups': [
                        {
                            'CacheSecurityGroupName': 'string',
                            'Status': 'string'
                        },
                    ],
                    'CacheParameterGroup': {
                        'CacheParameterGroupName': 'string',
                        'ParameterApplyStatus': 'string',
                        'CacheNodeIdsToReboot': [
                            'string',
                        ]
                    },
                    'CacheSubnetGroupName': 'string',
                    'CacheNodes': [
                        {
                            'CacheNodeId': 'string',
                            'CacheNodeStatus': 'string',
                            'CacheNodeCreateTime': datetime(2015, 1, 1),
                            'Endpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'ParameterGroupStatus': 'string',
                            'SourceCacheNodeId': 'string',
                            'CustomerAvailabilityZone': 'string'
                        },
                    ],
                    'AutoMinorVersionUpgrade': True|False,
                    'SecurityGroups': [
                        {
                            'SecurityGroupId': 'string',
                            'Status': 'string'
                        },
                    ],
                    'ReplicationGroupId': 'string',
                    'SnapshotRetentionLimit': 123,
                    'SnapshotWindow': 'string',
                    'AuthTokenEnabled': True|False,
                    'TransitEncryptionEnabled': True|False,
                    'AtRestEncryptionEnabled': True|False
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DescribeCacheClusters`` operation.

        
        

        - **CacheClusters** *(list) --* 

          A list of clusters. Each item in the list contains detailed information about one cluster.

          
          

          - *(dict) --* 

            Contains all of the attributes of a specific cluster.

            
            

            - **CacheClusterId** *(string) --* 

              The user-supplied identifier of the cluster. This identifier is a unique key that identifies a cluster.

              
            

            - **ConfigurationEndpoint** *(dict) --* 

              Represents a Memcached cluster endpoint which, if Automatic Discovery is enabled on the cluster, can be used by an application to connect to any node in the cluster. The configuration endpoint will always have ``.cfg`` in it.

               

              Example: ``mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211``  

              
              

              - **Address** *(string) --* 

                The DNS hostname of the cache node.

                
              

              - **Port** *(integer) --* 

                The port number that the cache engine is listening on.

                
          
            

            - **ClientDownloadLandingPage** *(string) --* 

              The URL of the web page where you can download the latest ElastiCache client library.

              
            

            - **CacheNodeType** *(string) --* 

              The name of the compute and memory capacity node type for the cluster.

               

              The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

               

               
              * General purpose: 

                 
                * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
                 
                * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
                 

               
               
              * Compute optimized: 

                 
                * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
                 

               
               
              * Memory optimized: 

                 
                * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
                 
                * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
                 

               
               

               

               **Notes:**  

               

               
              * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
               
              * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
               
              * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
               
              * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
               

               

              For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

              
            

            - **Engine** *(string) --* 

              The name of the cache engine (``memcached`` or ``redis`` ) to be used for this cluster.

              
            

            - **EngineVersion** *(string) --* 

              The version of the cache engine that is used in this cluster.

              
            

            - **CacheClusterStatus** *(string) --* 

              The current state of this cluster, one of the following values: ``available`` , ``creating`` , ``deleted`` , ``deleting`` , ``incompatible-network`` , ``modifying`` , ``rebooting cluster nodes`` , ``restore-failed`` , or ``snapshotting`` .

              
            

            - **NumCacheNodes** *(integer) --* 

              The number of cache nodes in the cluster.

               

              For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

              
            

            - **PreferredAvailabilityZone** *(string) --* 

              The name of the Availability Zone in which the cluster is located or "Multiple" if the cache nodes are located in different Availability Zones.

              
            

            - **CacheClusterCreateTime** *(datetime) --* 

              The date and time when the cluster was created.

              
            

            - **PreferredMaintenanceWindow** *(string) --* 

              Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.

               

              Valid values for ``ddd`` are:

               

               
              * ``sun``   
               
              * ``mon``   
               
              * ``tue``   
               
              * ``wed``   
               
              * ``thu``   
               
              * ``fri``   
               
              * ``sat``   
               

               

              Example: ``sun:23:00-mon:01:30``  

              
            

            - **PendingModifiedValues** *(dict) --* 

              A group of settings that are applied to the cluster in the future, or that are currently being applied.

              
              

              - **NumCacheNodes** *(integer) --* 

                The new number of cache nodes for the cluster.

                 

                For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

                
              

              - **CacheNodeIdsToRemove** *(list) --* 

                A list of cache node IDs that are being removed (or will be removed) from the cluster. A node ID is a numeric identifier (0001, 0002, etc.).

                
                

                - *(string) --* 
            
              

              - **EngineVersion** *(string) --* 

                The new cache engine version that the cluster runs.

                
              

              - **CacheNodeType** *(string) --* 

                The cache node type that this cluster or replication group is scaled to.

                
          
            

            - **NotificationConfiguration** *(dict) --* 

              Describes a notification topic and its status. Notification topics are used for publishing ElastiCache events to subscribers using Amazon Simple Notification Service (SNS). 

              
              

              - **TopicArn** *(string) --* 

                The Amazon Resource Name (ARN) that identifies the topic.

                
              

              - **TopicStatus** *(string) --* 

                The current state of the topic.

                
          
            

            - **CacheSecurityGroups** *(list) --* 

              A list of cache security group elements, composed of name and status sub-elements.

              
              

              - *(dict) --* 

                Represents a cluster's status within a particular cache security group.

                
                

                - **CacheSecurityGroupName** *(string) --* 

                  The name of the cache security group.

                  
                

                - **Status** *(string) --* 

                  The membership status in the cache security group. The status changes when a cache security group is modified, or when the cache security groups assigned to a cluster are modified.

                  
            
          
            

            - **CacheParameterGroup** *(dict) --* 

              Status of the cache parameter group.

              
              

              - **CacheParameterGroupName** *(string) --* 

                The name of the cache parameter group.

                
              

              - **ParameterApplyStatus** *(string) --* 

                The status of parameter updates.

                
              

              - **CacheNodeIdsToReboot** *(list) --* 

                A list of the cache node IDs which need to be rebooted for parameter changes to be applied. A node ID is a numeric identifier (0001, 0002, etc.).

                
                

                - *(string) --* 
            
          
            

            - **CacheSubnetGroupName** *(string) --* 

              The name of the cache subnet group associated with the cluster.

              
            

            - **CacheNodes** *(list) --* 

              A list of cache nodes that are members of the cluster.

              
              

              - *(dict) --* 

                Represents an individual cache node within a cluster. Each cache node runs its own instance of the cluster's protocol-compliant caching software - either Memcached or Redis.

                 

                The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

                 

                 
                * General purpose: 

                   
                  * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
                   
                  * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
                   

                 
                 
                * Compute optimized: 

                   
                  * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
                   

                 
                 
                * Memory optimized: 

                   
                  * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
                   
                  * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
                   

                 
                 

                 

                 **Notes:**  

                 

                 
                * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
                 
                * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
                 
                * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
                 
                * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
                 

                 

                For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

                
                

                - **CacheNodeId** *(string) --* 

                  The cache node identifier. A node ID is a numeric identifier (0001, 0002, etc.). The combination of cluster ID and node ID uniquely identifies every cache node used in a customer's AWS account.

                  
                

                - **CacheNodeStatus** *(string) --* 

                  The current state of this cache node.

                  
                

                - **CacheNodeCreateTime** *(datetime) --* 

                  The date and time when the cache node was created.

                  
                

                - **Endpoint** *(dict) --* 

                  The hostname for connecting to this cache node.

                  
                  

                  - **Address** *(string) --* 

                    The DNS hostname of the cache node.

                    
                  

                  - **Port** *(integer) --* 

                    The port number that the cache engine is listening on.

                    
              
                

                - **ParameterGroupStatus** *(string) --* 

                  The status of the parameter group applied to this cache node.

                  
                

                - **SourceCacheNodeId** *(string) --* 

                  The ID of the primary node to which this read replica node is synchronized. If this field is empty, this node is not associated with a primary cluster.

                  
                

                - **CustomerAvailabilityZone** *(string) --* 

                  The Availability Zone where this node was created and now resides.

                  
            
          
            

            - **AutoMinorVersionUpgrade** *(boolean) --* 

              This parameter is currently disabled.

              
            

            - **SecurityGroups** *(list) --* 

              A list of VPC Security Groups associated with the cluster.

              
              

              - *(dict) --* 

                Represents a single cache security group and its status.

                
                

                - **SecurityGroupId** *(string) --* 

                  The identifier of the cache security group.

                  
                

                - **Status** *(string) --* 

                  The status of the cache security group membership. The status changes whenever a cache security group is modified, or when the cache security groups assigned to a cluster are modified.

                  
            
          
            

            - **ReplicationGroupId** *(string) --* 

              The replication group to which this cluster belongs. If this field is empty, the cluster is not associated with any replication group.

              
            

            - **SnapshotRetentionLimit** *(integer) --* 

              The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was taken today is retained for 5 days before being deleted.

               

              .. warning::

                 

                If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

                 

              
            

            - **SnapshotWindow** *(string) --* 

              The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your cluster.

               

              Example: ``05:00-09:00``  

              
            

            - **AuthTokenEnabled** *(boolean) --* 

              A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

               

              Default: ``false``  

              
            

            - **TransitEncryptionEnabled** *(boolean) --* 

              A flag that enables in-transit encryption when set to ``true`` .

               

              You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created. To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to ``true`` when you create a cluster.

               

              Default: ``false``  

              
            

            - **AtRestEncryptionEnabled** *(boolean) --* 

              A flag that enables encryption at-rest when set to ``true`` .

               

              You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To enable at-rest encryption on a cluster you must set ``AtRestEncryptionEnabled`` to ``true`` when you create a cluster.

               

              Default: ``false``  

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: ElastiCache.Paginator.DescribeCacheEngineVersions

  ::

    
    paginator = client.get_paginator('describe_cache_engine_versions')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ElastiCache.Client.describe_cache_engine_versions`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheEngineVersions>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          Engine='string',
          EngineVersion='string',
          CacheParameterGroupFamily='string',
          DefaultOnly=True|False,
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type Engine: string
    :param Engine: 

      The cache engine to return. Valid values: ``memcached`` | ``redis``  

      

    
    :type EngineVersion: string
    :param EngineVersion: 

      The cache engine version to return.

       

      Example: ``1.4.14``  

      

    
    :type CacheParameterGroupFamily: string
    :param CacheParameterGroupFamily: 

      The name of a specific cache parameter group family to return details for.

       

      Valid values are: ``memcached1.4`` | ``redis2.6`` | ``redis2.8`` | ``redis3.2``  

       

      Constraints:

       

       
      * Must be 1 to 255 alphanumeric characters 
       
      * First character must be a letter 
       
      * Cannot end with a hyphen or contain two consecutive hyphens 
       

      

    
    :type DefaultOnly: boolean
    :param DefaultOnly: 

      If ``true`` , specifies that only the default version of the specified engine or engine and major version combination is to be returned.

      

    
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
            'CacheEngineVersions': [
                {
                    'Engine': 'string',
                    'EngineVersion': 'string',
                    'CacheParameterGroupFamily': 'string',
                    'CacheEngineDescription': 'string',
                    'CacheEngineVersionDescription': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a  DescribeCacheEngineVersions operation.

        
        

        - **CacheEngineVersions** *(list) --* 

          A list of cache engine version details. Each element in the list contains detailed information about one cache engine version.

          
          

          - *(dict) --* 

            Provides all of the details about a particular cache engine version.

            
            

            - **Engine** *(string) --* 

              The name of the cache engine.

              
            

            - **EngineVersion** *(string) --* 

              The version number of the cache engine.

              
            

            - **CacheParameterGroupFamily** *(string) --* 

              The name of the cache parameter group family associated with this cache engine.

               

              Valid values are: ``memcached1.4`` | ``redis2.6`` | ``redis2.8`` | ``redis3.2``  

              
            

            - **CacheEngineDescription** *(string) --* 

              The description of the cache engine.

              
            

            - **CacheEngineVersionDescription** *(string) --* 

              The description of the cache engine version.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: ElastiCache.Paginator.DescribeCacheParameterGroups

  ::

    
    paginator = client.get_paginator('describe_cache_parameter_groups')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ElastiCache.Client.describe_cache_parameter_groups`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheParameterGroups>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          CacheParameterGroupName='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: 

      The name of a specific cache parameter group to return details for.

      

    
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
            'CacheParameterGroups': [
                {
                    'CacheParameterGroupName': 'string',
                    'CacheParameterGroupFamily': 'string',
                    'Description': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DescribeCacheParameterGroups`` operation.

        
        

        - **CacheParameterGroups** *(list) --* 

          A list of cache parameter groups. Each element in the list contains detailed information about one cache parameter group.

          
          

          - *(dict) --* 

            Represents the output of a ``CreateCacheParameterGroup`` operation.

            
            

            - **CacheParameterGroupName** *(string) --* 

              The name of the cache parameter group.

              
            

            - **CacheParameterGroupFamily** *(string) --* 

              The name of the cache parameter group family that this cache parameter group is compatible with.

               

              Valid values are: ``memcached1.4`` | ``redis2.6`` | ``redis2.8`` | ``redis3.2``  

              
            

            - **Description** *(string) --* 

              The description for this cache parameter group.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: ElastiCache.Paginator.DescribeCacheParameters

  ::

    
    paginator = client.get_paginator('describe_cache_parameters')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ElastiCache.Client.describe_cache_parameters`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheParameters>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          CacheParameterGroupName='string',
          Source='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type CacheParameterGroupName: string
    :param CacheParameterGroupName: **[REQUIRED]** 

      The name of a specific cache parameter group to return details for.

      

    
    :type Source: string
    :param Source: 

      The parameter types to return.

       

      Valid values: ``user`` | ``system`` | ``engine-default``  

      

    
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
            'Parameters': [
                {
                    'ParameterName': 'string',
                    'ParameterValue': 'string',
                    'Description': 'string',
                    'Source': 'string',
                    'DataType': 'string',
                    'AllowedValues': 'string',
                    'IsModifiable': True|False,
                    'MinimumEngineVersion': 'string',
                    'ChangeType': 'immediate'|'requires-reboot'
                },
            ],
            'CacheNodeTypeSpecificParameters': [
                {
                    'ParameterName': 'string',
                    'Description': 'string',
                    'Source': 'string',
                    'DataType': 'string',
                    'AllowedValues': 'string',
                    'IsModifiable': True|False,
                    'MinimumEngineVersion': 'string',
                    'CacheNodeTypeSpecificValues': [
                        {
                            'CacheNodeType': 'string',
                            'Value': 'string'
                        },
                    ],
                    'ChangeType': 'immediate'|'requires-reboot'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DescribeCacheParameters`` operation.

        
        

        - **Parameters** *(list) --* 

          A list of  Parameter instances.

          
          

          - *(dict) --* 

            Describes an individual setting that controls some aspect of ElastiCache behavior.

            
            

            - **ParameterName** *(string) --* 

              The name of the parameter.

              
            

            - **ParameterValue** *(string) --* 

              The value of the parameter.

              
            

            - **Description** *(string) --* 

              A description of the parameter.

              
            

            - **Source** *(string) --* 

              The source of the parameter.

              
            

            - **DataType** *(string) --* 

              The valid data type for the parameter.

              
            

            - **AllowedValues** *(string) --* 

              The valid range of values for the parameter.

              
            

            - **IsModifiable** *(boolean) --* 

              Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.

              
            

            - **MinimumEngineVersion** *(string) --* 

              The earliest cache engine version to which the parameter can apply.

              
            

            - **ChangeType** *(string) --* 

              Indicates whether a change to the parameter is applied immediately or requires a reboot for the change to be applied. You can force a reboot or wait until the next maintenance window's reboot. For more information, see `Rebooting a Cluster <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Clusters.Rebooting.html>`__ .

              
        
      
        

        - **CacheNodeTypeSpecificParameters** *(list) --* 

          A list of parameters specific to a particular cache node type. Each element in the list contains detailed information about one parameter.

          
          

          - *(dict) --* 

            A parameter that has a different value for each cache node type it is applied to. For example, in a Redis cluster, a ``cache.m1.large`` cache node type would have a larger ``maxmemory`` value than a ``cache.m1.small`` type.

            
            

            - **ParameterName** *(string) --* 

              The name of the parameter.

              
            

            - **Description** *(string) --* 

              A description of the parameter.

              
            

            - **Source** *(string) --* 

              The source of the parameter value.

              
            

            - **DataType** *(string) --* 

              The valid data type for the parameter.

              
            

            - **AllowedValues** *(string) --* 

              The valid range of values for the parameter.

              
            

            - **IsModifiable** *(boolean) --* 

              Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.

              
            

            - **MinimumEngineVersion** *(string) --* 

              The earliest cache engine version to which the parameter can apply.

              
            

            - **CacheNodeTypeSpecificValues** *(list) --* 

              A list of cache node types and their corresponding values for this parameter.

              
              

              - *(dict) --* 

                A value that applies only to a certain cache node type.

                
                

                - **CacheNodeType** *(string) --* 

                  The cache node type for which this value applies.

                  
                

                - **Value** *(string) --* 

                  The value for the cache node type.

                  
            
          
            

            - **ChangeType** *(string) --* 

              Indicates whether a change to the parameter is applied immediately or requires a reboot for the change to be applied. You can force a reboot or wait until the next maintenance window's reboot. For more information, see `Rebooting a Cluster <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Clusters.Rebooting.html>`__ .

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: ElastiCache.Paginator.DescribeCacheSecurityGroups

  ::

    
    paginator = client.get_paginator('describe_cache_security_groups')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ElastiCache.Client.describe_cache_security_groups`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheSecurityGroups>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          CacheSecurityGroupName='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type CacheSecurityGroupName: string
    :param CacheSecurityGroupName: 

      The name of the cache security group to return details for.

      

    
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
            'CacheSecurityGroups': [
                {
                    'OwnerId': 'string',
                    'CacheSecurityGroupName': 'string',
                    'Description': 'string',
                    'EC2SecurityGroups': [
                        {
                            'Status': 'string',
                            'EC2SecurityGroupName': 'string',
                            'EC2SecurityGroupOwnerId': 'string'
                        },
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DescribeCacheSecurityGroups`` operation.

        
        

        - **CacheSecurityGroups** *(list) --* 

          A list of cache security groups. Each element in the list contains detailed information about one group.

          
          

          - *(dict) --* 

            Represents the output of one of the following operations:

             

             
            * ``AuthorizeCacheSecurityGroupIngress``   
             
            * ``CreateCacheSecurityGroup``   
             
            * ``RevokeCacheSecurityGroupIngress``   
             

            
            

            - **OwnerId** *(string) --* 

              The AWS account ID of the cache security group owner.

              
            

            - **CacheSecurityGroupName** *(string) --* 

              The name of the cache security group.

              
            

            - **Description** *(string) --* 

              The description of the cache security group.

              
            

            - **EC2SecurityGroups** *(list) --* 

              A list of Amazon EC2 security groups that are associated with this cache security group.

              
              

              - *(dict) --* 

                Provides ownership and status information for an Amazon EC2 security group.

                
                

                - **Status** *(string) --* 

                  The status of the Amazon EC2 security group.

                  
                

                - **EC2SecurityGroupName** *(string) --* 

                  The name of the Amazon EC2 security group.

                  
                

                - **EC2SecurityGroupOwnerId** *(string) --* 

                  The AWS account ID of the Amazon EC2 security group owner.

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: ElastiCache.Paginator.DescribeCacheSubnetGroups

  ::

    
    paginator = client.get_paginator('describe_cache_subnet_groups')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ElastiCache.Client.describe_cache_subnet_groups`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheSubnetGroups>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          CacheSubnetGroupName='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type CacheSubnetGroupName: string
    :param CacheSubnetGroupName: 

      The name of the cache subnet group to return details for.

      

    
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
            'CacheSubnetGroups': [
                {
                    'CacheSubnetGroupName': 'string',
                    'CacheSubnetGroupDescription': 'string',
                    'VpcId': 'string',
                    'Subnets': [
                        {
                            'SubnetIdentifier': 'string',
                            'SubnetAvailabilityZone': {
                                'Name': 'string'
                            }
                        },
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DescribeCacheSubnetGroups`` operation.

        
        

        - **CacheSubnetGroups** *(list) --* 

          A list of cache subnet groups. Each element in the list contains detailed information about one group.

          
          

          - *(dict) --* 

            Represents the output of one of the following operations:

             

             
            * ``CreateCacheSubnetGroup``   
             
            * ``ModifyCacheSubnetGroup``   
             

            
            

            - **CacheSubnetGroupName** *(string) --* 

              The name of the cache subnet group.

              
            

            - **CacheSubnetGroupDescription** *(string) --* 

              The description of the cache subnet group.

              
            

            - **VpcId** *(string) --* 

              The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group.

              
            

            - **Subnets** *(list) --* 

              A list of subnets associated with the cache subnet group.

              
              

              - *(dict) --* 

                Represents the subnet associated with a cluster. This parameter refers to subnets defined in Amazon Virtual Private Cloud (Amazon VPC) and used with ElastiCache.

                
                

                - **SubnetIdentifier** *(string) --* 

                  The unique identifier for the subnet.

                  
                

                - **SubnetAvailabilityZone** *(dict) --* 

                  The Availability Zone associated with the subnet.

                  
                  

                  - **Name** *(string) --* 

                    The name of the Availability Zone.

                    
              
            
          
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: ElastiCache.Paginator.DescribeEngineDefaultParameters

  ::

    
    paginator = client.get_paginator('describe_engine_default_parameters')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ElastiCache.Client.describe_engine_default_parameters`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeEngineDefaultParameters>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          CacheParameterGroupFamily='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type CacheParameterGroupFamily: string
    :param CacheParameterGroupFamily: **[REQUIRED]** 

      The name of the cache parameter group family.

       

      Valid values are: ``memcached1.4`` | ``redis2.6`` | ``redis2.8`` | ``redis3.2``  

      

    
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
            'EngineDefaults': {
                'CacheParameterGroupFamily': 'string',
                'Marker': 'string',
                'Parameters': [
                    {
                        'ParameterName': 'string',
                        'ParameterValue': 'string',
                        'Description': 'string',
                        'Source': 'string',
                        'DataType': 'string',
                        'AllowedValues': 'string',
                        'IsModifiable': True|False,
                        'MinimumEngineVersion': 'string',
                        'ChangeType': 'immediate'|'requires-reboot'
                    },
                ],
                'CacheNodeTypeSpecificParameters': [
                    {
                        'ParameterName': 'string',
                        'Description': 'string',
                        'Source': 'string',
                        'DataType': 'string',
                        'AllowedValues': 'string',
                        'IsModifiable': True|False,
                        'MinimumEngineVersion': 'string',
                        'CacheNodeTypeSpecificValues': [
                            {
                                'CacheNodeType': 'string',
                                'Value': 'string'
                            },
                        ],
                        'ChangeType': 'immediate'|'requires-reboot'
                    },
                ]
            },
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **EngineDefaults** *(dict) --* 

          Represents the output of a ``DescribeEngineDefaultParameters`` operation.

          
          

          - **CacheParameterGroupFamily** *(string) --* 

            Specifies the name of the cache parameter group family to which the engine default parameters apply.

             

            Valid values are: ``memcached1.4`` | ``redis2.6`` | ``redis2.8`` | ``redis3.2``  

            
          

          - **Marker** *(string) --* 

            Provides an identifier to allow retrieval of paginated results.

            
          

          - **Parameters** *(list) --* 

            Contains a list of engine default parameters.

            
            

            - *(dict) --* 

              Describes an individual setting that controls some aspect of ElastiCache behavior.

              
              

              - **ParameterName** *(string) --* 

                The name of the parameter.

                
              

              - **ParameterValue** *(string) --* 

                The value of the parameter.

                
              

              - **Description** *(string) --* 

                A description of the parameter.

                
              

              - **Source** *(string) --* 

                The source of the parameter.

                
              

              - **DataType** *(string) --* 

                The valid data type for the parameter.

                
              

              - **AllowedValues** *(string) --* 

                The valid range of values for the parameter.

                
              

              - **IsModifiable** *(boolean) --* 

                Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.

                
              

              - **MinimumEngineVersion** *(string) --* 

                The earliest cache engine version to which the parameter can apply.

                
              

              - **ChangeType** *(string) --* 

                Indicates whether a change to the parameter is applied immediately or requires a reboot for the change to be applied. You can force a reboot or wait until the next maintenance window's reboot. For more information, see `Rebooting a Cluster <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Clusters.Rebooting.html>`__ .

                
          
        
          

          - **CacheNodeTypeSpecificParameters** *(list) --* 

            A list of parameters specific to a particular cache node type. Each element in the list contains detailed information about one parameter.

            
            

            - *(dict) --* 

              A parameter that has a different value for each cache node type it is applied to. For example, in a Redis cluster, a ``cache.m1.large`` cache node type would have a larger ``maxmemory`` value than a ``cache.m1.small`` type.

              
              

              - **ParameterName** *(string) --* 

                The name of the parameter.

                
              

              - **Description** *(string) --* 

                A description of the parameter.

                
              

              - **Source** *(string) --* 

                The source of the parameter value.

                
              

              - **DataType** *(string) --* 

                The valid data type for the parameter.

                
              

              - **AllowedValues** *(string) --* 

                The valid range of values for the parameter.

                
              

              - **IsModifiable** *(boolean) --* 

                Indicates whether (``true`` ) or not (``false`` ) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.

                
              

              - **MinimumEngineVersion** *(string) --* 

                The earliest cache engine version to which the parameter can apply.

                
              

              - **CacheNodeTypeSpecificValues** *(list) --* 

                A list of cache node types and their corresponding values for this parameter.

                
                

                - *(dict) --* 

                  A value that applies only to a certain cache node type.

                  
                  

                  - **CacheNodeType** *(string) --* 

                    The cache node type for which this value applies.

                    
                  

                  - **Value** *(string) --* 

                    The value for the cache node type.

                    
              
            
              

              - **ChangeType** *(string) --* 

                Indicates whether a change to the parameter is applied immediately or requires a reboot for the change to be applied. You can force a reboot or wait until the next maintenance window's reboot. For more information, see `Rebooting a Cluster <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/Clusters.Rebooting.html>`__ .

                
          
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: ElastiCache.Paginator.DescribeEvents

  ::

    
    paginator = client.get_paginator('describe_events')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ElastiCache.Client.describe_events`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeEvents>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          SourceIdentifier='string',
          SourceType='cache-cluster'|'cache-parameter-group'|'cache-security-group'|'cache-subnet-group'|'replication-group',
          StartTime=datetime(2015, 1, 1),
          EndTime=datetime(2015, 1, 1),
          Duration=123,
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type SourceIdentifier: string
    :param SourceIdentifier: 

      The identifier of the event source for which events are returned. If not specified, all sources are included in the response.

      

    
    :type SourceType: string
    :param SourceType: 

      The event source to retrieve events for. If no value is specified, all events are returned.

      

    
    :type StartTime: datetime
    :param StartTime: 

      The beginning of the time interval to retrieve events for, specified in ISO 8601 format.

       

       **Example:** 2017-03-30T07:03:49.555Z

      

    
    :type EndTime: datetime
    :param EndTime: 

      The end of the time interval for which to retrieve events, specified in ISO 8601 format.

       

       **Example:** 2017-03-30T07:03:49.555Z

      

    
    :type Duration: integer
    :param Duration: 

      The number of minutes worth of events to retrieve.

      

    
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
            'Events': [
                {
                    'SourceIdentifier': 'string',
                    'SourceType': 'cache-cluster'|'cache-parameter-group'|'cache-security-group'|'cache-subnet-group'|'replication-group',
                    'Message': 'string',
                    'Date': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DescribeEvents`` operation.

        
        

        - **Events** *(list) --* 

          A list of events. Each element in the list contains detailed information about one event.

          
          

          - *(dict) --* 

            Represents a single occurrence of something interesting within the system. Some examples of events are creating a cluster, adding or removing a cache node, or rebooting a node.

            
            

            - **SourceIdentifier** *(string) --* 

              The identifier for the source of the event. For example, if the event occurred at the cluster level, the identifier would be the name of the cluster.

              
            

            - **SourceType** *(string) --* 

              Specifies the origin of this event - a cluster, a parameter group, a security group, etc.

              
            

            - **Message** *(string) --* 

              The text of the event.

              
            

            - **Date** *(datetime) --* 

              The date and time when the event occurred.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: ElastiCache.Paginator.DescribeReplicationGroups

  ::

    
    paginator = client.get_paginator('describe_replication_groups')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ElastiCache.Client.describe_replication_groups`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeReplicationGroups>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          ReplicationGroupId='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type ReplicationGroupId: string
    :param ReplicationGroupId: 

      The identifier for the replication group to be described. This parameter is not case sensitive.

       

      If you do not specify this parameter, information about all replication groups is returned.

      

    
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
            'ReplicationGroups': [
                {
                    'ReplicationGroupId': 'string',
                    'Description': 'string',
                    'Status': 'string',
                    'PendingModifiedValues': {
                        'PrimaryClusterId': 'string',
                        'AutomaticFailoverStatus': 'enabled'|'disabled',
                        'Resharding': {
                            'SlotMigration': {
                                'ProgressPercentage': 123.0
                            }
                        }
                    },
                    'MemberClusters': [
                        'string',
                    ],
                    'NodeGroups': [
                        {
                            'NodeGroupId': 'string',
                            'Status': 'string',
                            'PrimaryEndpoint': {
                                'Address': 'string',
                                'Port': 123
                            },
                            'Slots': 'string',
                            'NodeGroupMembers': [
                                {
                                    'CacheClusterId': 'string',
                                    'CacheNodeId': 'string',
                                    'ReadEndpoint': {
                                        'Address': 'string',
                                        'Port': 123
                                    },
                                    'PreferredAvailabilityZone': 'string',
                                    'CurrentRole': 'string'
                                },
                            ]
                        },
                    ],
                    'SnapshottingClusterId': 'string',
                    'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                    'ConfigurationEndpoint': {
                        'Address': 'string',
                        'Port': 123
                    },
                    'SnapshotRetentionLimit': 123,
                    'SnapshotWindow': 'string',
                    'ClusterEnabled': True|False,
                    'CacheNodeType': 'string',
                    'AuthTokenEnabled': True|False,
                    'TransitEncryptionEnabled': True|False,
                    'AtRestEncryptionEnabled': True|False
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DescribeReplicationGroups`` operation.

        
        

        - **ReplicationGroups** *(list) --* 

          A list of replication groups. Each item in the list contains detailed information about one replication group.

          
          

          - *(dict) --* 

            Contains all of the attributes of a specific Redis replication group.

            
            

            - **ReplicationGroupId** *(string) --* 

              The identifier for the replication group.

              
            

            - **Description** *(string) --* 

              The user supplied description of the replication group.

              
            

            - **Status** *(string) --* 

              The current state of this replication group - ``creating`` , ``available`` , ``modifying`` , ``deleting`` , ``create-failed`` , ``snapshotting`` .

              
            

            - **PendingModifiedValues** *(dict) --* 

              A group of settings to be applied to the replication group, either immediately or during the next maintenance window.

              
              

              - **PrimaryClusterId** *(string) --* 

                The primary cluster ID that is applied immediately (if ``--apply-immediately`` was specified), or during the next maintenance window.

                
              

              - **AutomaticFailoverStatus** *(string) --* 

                Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

                 

                Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

                 

                 
                * Redis versions earlier than 2.8.6. 
                 
                * Redis (cluster mode disabled): T1 and T2 cache node types. 
                 
                * Redis (cluster mode enabled): T1 node types. 
                 

                
              

              - **Resharding** *(dict) --* 

                The status of an online resharding operation.

                
                

                - **SlotMigration** *(dict) --* 

                  Represents the progress of an online resharding operation.

                  
                  

                  - **ProgressPercentage** *(float) --* 

                    The percentage of the slot migration that is complete.

                    
              
            
          
            

            - **MemberClusters** *(list) --* 

              The identifiers of all the nodes that are part of this replication group.

              
              

              - *(string) --* 
          
            

            - **NodeGroups** *(list) --* 

              A list of node groups in this replication group. For Redis (cluster mode disabled) replication groups, this is a single-element list. For Redis (cluster mode enabled) replication groups, the list contains an entry for each node group (shard).

              
              

              - *(dict) --* 

                Represents a collection of cache nodes in a replication group. One node in the node group is the read/write primary node. All the other nodes are read-only Replica nodes.

                
                

                - **NodeGroupId** *(string) --* 

                  The identifier for the node group (shard). A Redis (cluster mode disabled) replication group contains only 1 node group; therefore, the node group ID is 0001. A Redis (cluster mode enabled) replication group contains 1 to 15 node groups numbered 0001 to 0015. 

                  
                

                - **Status** *(string) --* 

                  The current state of this replication group - ``creating`` , ``available`` , etc.

                  
                

                - **PrimaryEndpoint** *(dict) --* 

                  The endpoint of the primary node in this node group (shard).

                  
                  

                  - **Address** *(string) --* 

                    The DNS hostname of the cache node.

                    
                  

                  - **Port** *(integer) --* 

                    The port number that the cache engine is listening on.

                    
              
                

                - **Slots** *(string) --* 

                  The keyspace for this node group (shard).

                  
                

                - **NodeGroupMembers** *(list) --* 

                  A list containing information about individual nodes within the node group (shard).

                  
                  

                  - *(dict) --* 

                    Represents a single node within a node group (shard).

                    
                    

                    - **CacheClusterId** *(string) --* 

                      The ID of the cluster to which the node belongs.

                      
                    

                    - **CacheNodeId** *(string) --* 

                      The ID of the node within its cluster. A node ID is a numeric identifier (0001, 0002, etc.).

                      
                    

                    - **ReadEndpoint** *(dict) --* 

                      Represents the information required for client programs to connect to a cache node.

                      
                      

                      - **Address** *(string) --* 

                        The DNS hostname of the cache node.

                        
                      

                      - **Port** *(integer) --* 

                        The port number that the cache engine is listening on.

                        
                  
                    

                    - **PreferredAvailabilityZone** *(string) --* 

                      The name of the Availability Zone in which the node is located.

                      
                    

                    - **CurrentRole** *(string) --* 

                      The role that is currently assigned to the node - ``primary`` or ``replica`` .

                      
                
              
            
          
            

            - **SnapshottingClusterId** *(string) --* 

              The cluster ID that is used as the daily snapshot source for the replication group.

              
            

            - **AutomaticFailover** *(string) --* 

              Indicates the status of Multi-AZ with automatic failover for this Redis replication group.

               

              Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

               

               
              * Redis versions earlier than 2.8.6. 
               
              * Redis (cluster mode disabled): T1 and T2 cache node types. 
               
              * Redis (cluster mode enabled): T1 node types. 
               

              
            

            - **ConfigurationEndpoint** *(dict) --* 

              The configuration endpoint for this replication group. Use the configuration endpoint to connect to this replication group.

              
              

              - **Address** *(string) --* 

                The DNS hostname of the cache node.

                
              

              - **Port** *(integer) --* 

                The port number that the cache engine is listening on.

                
          
            

            - **SnapshotRetentionLimit** *(integer) --* 

              The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set ``SnapshotRetentionLimit`` to 5, a snapshot that was taken today is retained for 5 days before being deleted.

               

              .. warning::

                 

                If the value of ``SnapshotRetentionLimit`` is set to zero (0), backups are turned off.

                 

              
            

            - **SnapshotWindow** *(string) --* 

              The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).

               

              Example: ``05:00-09:00``  

               

              If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.

               

              .. note::

                 

                This parameter is only valid if the ``Engine`` parameter is ``redis`` .

                 

              
            

            - **ClusterEnabled** *(boolean) --* 

              A flag indicating whether or not this replication group is cluster enabled; i.e., whether its data can be partitioned across multiple shards (API/CLI: node groups).

               

              Valid values: ``true`` | ``false``  

              
            

            - **CacheNodeType** *(string) --* 

              The name of the compute and memory capacity node type for each node in the replication group.

              
            

            - **AuthTokenEnabled** *(boolean) --* 

              A flag that enables using an ``AuthToken`` (password) when issuing Redis commands.

               

              Default: ``false``  

              
            

            - **TransitEncryptionEnabled** *(boolean) --* 

              A flag that enables in-transit encryption when set to ``true`` .

               

              You cannot modify the value of ``TransitEncryptionEnabled`` after the cluster is created. To enable in-transit encryption on a cluster you must set ``TransitEncryptionEnabled`` to ``true`` when you create a cluster.

               

              Default: ``false``  

              
            

            - **AtRestEncryptionEnabled** *(boolean) --* 

              A flag that enables encryption at-rest when set to ``true`` .

               

              You cannot modify the value of ``AtRestEncryptionEnabled`` after the cluster is created. To enable encryption at-rest on a cluster you must set ``AtRestEncryptionEnabled`` to ``true`` when you create a cluster.

               

              Default: ``false``  

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: ElastiCache.Paginator.DescribeReservedCacheNodes

  ::

    
    paginator = client.get_paginator('describe_reserved_cache_nodes')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ElastiCache.Client.describe_reserved_cache_nodes`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeReservedCacheNodes>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          ReservedCacheNodeId='string',
          ReservedCacheNodesOfferingId='string',
          CacheNodeType='string',
          Duration='string',
          ProductDescription='string',
          OfferingType='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type ReservedCacheNodeId: string
    :param ReservedCacheNodeId: 

      The reserved cache node identifier filter value. Use this parameter to show only the reservation that matches the specified reservation ID.

      

    
    :type ReservedCacheNodesOfferingId: string
    :param ReservedCacheNodesOfferingId: 

      The offering identifier filter value. Use this parameter to show only purchased reservations matching the specified offering identifier.

      

    
    :type CacheNodeType: string
    :param CacheNodeType: 

      The cache node type filter value. Use this parameter to show only those reservations matching the specified cache node type.

       

      The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

       

       
      * General purpose: 

         
        * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
         
        * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
         

       
       
      * Compute optimized: 

         
        * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
         

       
       
      * Memory optimized: 

         
        * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
         
        * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
         

       
       

       

       **Notes:**  

       

       
      * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
       
      * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
       
      * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
       
      * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
       

       

      For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

      

    
    :type Duration: string
    :param Duration: 

      The duration filter value, specified in years or seconds. Use this parameter to show only reservations for this duration.

       

      Valid Values: ``1 | 3 | 31536000 | 94608000``  

      

    
    :type ProductDescription: string
    :param ProductDescription: 

      The product description filter value. Use this parameter to show only those reservations matching the specified product description.

      

    
    :type OfferingType: string
    :param OfferingType: 

      The offering type filter value. Use this parameter to show only the available offerings matching the specified offering type.

       

      Valid values: ``"Light Utilization"|"Medium Utilization"|"Heavy Utilization"``  

      

    
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
            'ReservedCacheNodes': [
                {
                    'ReservedCacheNodeId': 'string',
                    'ReservedCacheNodesOfferingId': 'string',
                    'CacheNodeType': 'string',
                    'StartTime': datetime(2015, 1, 1),
                    'Duration': 123,
                    'FixedPrice': 123.0,
                    'UsagePrice': 123.0,
                    'CacheNodeCount': 123,
                    'ProductDescription': 'string',
                    'OfferingType': 'string',
                    'State': 'string',
                    'RecurringCharges': [
                        {
                            'RecurringChargeAmount': 123.0,
                            'RecurringChargeFrequency': 'string'
                        },
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DescribeReservedCacheNodes`` operation.

        
        

        - **ReservedCacheNodes** *(list) --* 

          A list of reserved cache nodes. Each element in the list contains detailed information about one node.

          
          

          - *(dict) --* 

            Represents the output of a ``PurchaseReservedCacheNodesOffering`` operation.

            
            

            - **ReservedCacheNodeId** *(string) --* 

              The unique identifier for the reservation.

              
            

            - **ReservedCacheNodesOfferingId** *(string) --* 

              The offering identifier.

              
            

            - **CacheNodeType** *(string) --* 

              The cache node type for the reserved cache nodes.

               

              The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

               

               
              * General purpose: 

                 
                * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
                 
                * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
                 

               
               
              * Compute optimized: 

                 
                * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
                 

               
               
              * Memory optimized: 

                 
                * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
                 
                * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
                 

               
               

               

               **Notes:**  

               

               
              * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
               
              * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
               
              * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
               
              * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
               

               

              For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

              
            

            - **StartTime** *(datetime) --* 

              The time the reservation started.

              
            

            - **Duration** *(integer) --* 

              The duration of the reservation in seconds.

              
            

            - **FixedPrice** *(float) --* 

              The fixed price charged for this reserved cache node.

              
            

            - **UsagePrice** *(float) --* 

              The hourly price charged for this reserved cache node.

              
            

            - **CacheNodeCount** *(integer) --* 

              The number of cache nodes that have been reserved.

              
            

            - **ProductDescription** *(string) --* 

              The description of the reserved cache node.

              
            

            - **OfferingType** *(string) --* 

              The offering type of this reserved cache node.

              
            

            - **State** *(string) --* 

              The state of the reserved cache node.

              
            

            - **RecurringCharges** *(list) --* 

              The recurring price charged to run this reserved cache node.

              
              

              - *(dict) --* 

                Contains the specific price and frequency of a recurring charges for a reserved cache node, or for a reserved cache node offering.

                
                

                - **RecurringChargeAmount** *(float) --* 

                  The monetary amount of the recurring charge.

                  
                

                - **RecurringChargeFrequency** *(string) --* 

                  The frequency of the recurring charge.

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: ElastiCache.Paginator.DescribeReservedCacheNodesOfferings

  ::

    
    paginator = client.get_paginator('describe_reserved_cache_nodes_offerings')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ElastiCache.Client.describe_reserved_cache_nodes_offerings`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeReservedCacheNodesOfferings>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          ReservedCacheNodesOfferingId='string',
          CacheNodeType='string',
          Duration='string',
          ProductDescription='string',
          OfferingType='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type ReservedCacheNodesOfferingId: string
    :param ReservedCacheNodesOfferingId: 

      The offering identifier filter value. Use this parameter to show only the available offering that matches the specified reservation identifier.

       

      Example: ``438012d3-4052-4cc7-b2e3-8d3372e0e706``  

      

    
    :type CacheNodeType: string
    :param CacheNodeType: 

      The cache node type filter value. Use this parameter to show only the available offerings matching the specified cache node type.

       

      The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

       

       
      * General purpose: 

         
        * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
         
        * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
         

       
       
      * Compute optimized: 

         
        * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
         

       
       
      * Memory optimized: 

         
        * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
         
        * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
         

       
       

       

       **Notes:**  

       

       
      * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
       
      * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
       
      * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
       
      * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
       

       

      For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

      

    
    :type Duration: string
    :param Duration: 

      Duration filter value, specified in years or seconds. Use this parameter to show only reservations for a given duration.

       

      Valid Values: ``1 | 3 | 31536000 | 94608000``  

      

    
    :type ProductDescription: string
    :param ProductDescription: 

      The product description filter value. Use this parameter to show only the available offerings matching the specified product description.

      

    
    :type OfferingType: string
    :param OfferingType: 

      The offering type filter value. Use this parameter to show only the available offerings matching the specified offering type.

       

      Valid Values: ``"Light Utilization"|"Medium Utilization"|"Heavy Utilization"``  

      

    
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
            'ReservedCacheNodesOfferings': [
                {
                    'ReservedCacheNodesOfferingId': 'string',
                    'CacheNodeType': 'string',
                    'Duration': 123,
                    'FixedPrice': 123.0,
                    'UsagePrice': 123.0,
                    'ProductDescription': 'string',
                    'OfferingType': 'string',
                    'RecurringCharges': [
                        {
                            'RecurringChargeAmount': 123.0,
                            'RecurringChargeFrequency': 'string'
                        },
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DescribeReservedCacheNodesOfferings`` operation.

        
        

        - **ReservedCacheNodesOfferings** *(list) --* 

          A list of reserved cache node offerings. Each element in the list contains detailed information about one offering.

          
          

          - *(dict) --* 

            Describes all of the attributes of a reserved cache node offering.

            
            

            - **ReservedCacheNodesOfferingId** *(string) --* 

              A unique identifier for the reserved cache node offering.

              
            

            - **CacheNodeType** *(string) --* 

              The cache node type for the reserved cache node.

               

              The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

               

               
              * General purpose: 

                 
                * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
                 
                * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
                 

               
               
              * Compute optimized: 

                 
                * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
                 

               
               
              * Memory optimized: 

                 
                * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
                 
                * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
                 

               
               

               

               **Notes:**  

               

               
              * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
               
              * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
               
              * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
               
              * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
               

               

              For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

              
            

            - **Duration** *(integer) --* 

              The duration of the offering. in seconds.

              
            

            - **FixedPrice** *(float) --* 

              The fixed price charged for this offering.

              
            

            - **UsagePrice** *(float) --* 

              The hourly price charged for this offering.

              
            

            - **ProductDescription** *(string) --* 

              The cache engine used by the offering.

              
            

            - **OfferingType** *(string) --* 

              The offering type.

              
            

            - **RecurringCharges** *(list) --* 

              The recurring price charged to run this reserved cache node.

              
              

              - *(dict) --* 

                Contains the specific price and frequency of a recurring charges for a reserved cache node, or for a reserved cache node offering.

                
                

                - **RecurringChargeAmount** *(float) --* 

                  The monetary amount of the recurring charge.

                  
                

                - **RecurringChargeFrequency** *(string) --* 

                  The frequency of the recurring charge.

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: ElastiCache.Paginator.DescribeSnapshots

  ::

    
    paginator = client.get_paginator('describe_snapshots')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ElastiCache.Client.describe_snapshots`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeSnapshots>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          ReplicationGroupId='string',
          CacheClusterId='string',
          SnapshotName='string',
          SnapshotSource='string',
          ShowNodeGroupConfig=True|False,
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type ReplicationGroupId: string
    :param ReplicationGroupId: 

      A user-supplied replication group identifier. If this parameter is specified, only snapshots associated with that specific replication group are described.

      

    
    :type CacheClusterId: string
    :param CacheClusterId: 

      A user-supplied cluster identifier. If this parameter is specified, only snapshots associated with that specific cluster are described.

      

    
    :type SnapshotName: string
    :param SnapshotName: 

      A user-supplied name of the snapshot. If this parameter is specified, only this snapshot are described.

      

    
    :type SnapshotSource: string
    :param SnapshotSource: 

      If set to ``system`` , the output shows snapshots that were automatically created by ElastiCache. If set to ``user`` the output shows snapshots that were manually created. If omitted, the output shows both automatically and manually created snapshots.

      

    
    :type ShowNodeGroupConfig: boolean
    :param ShowNodeGroupConfig: 

      A Boolean value which if true, the node group (shard) configuration is included in the snapshot description.

      

    
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
            'Snapshots': [
                {
                    'SnapshotName': 'string',
                    'ReplicationGroupId': 'string',
                    'ReplicationGroupDescription': 'string',
                    'CacheClusterId': 'string',
                    'SnapshotStatus': 'string',
                    'SnapshotSource': 'string',
                    'CacheNodeType': 'string',
                    'Engine': 'string',
                    'EngineVersion': 'string',
                    'NumCacheNodes': 123,
                    'PreferredAvailabilityZone': 'string',
                    'CacheClusterCreateTime': datetime(2015, 1, 1),
                    'PreferredMaintenanceWindow': 'string',
                    'TopicArn': 'string',
                    'Port': 123,
                    'CacheParameterGroupName': 'string',
                    'CacheSubnetGroupName': 'string',
                    'VpcId': 'string',
                    'AutoMinorVersionUpgrade': True|False,
                    'SnapshotRetentionLimit': 123,
                    'SnapshotWindow': 'string',
                    'NumNodeGroups': 123,
                    'AutomaticFailover': 'enabled'|'disabled'|'enabling'|'disabling',
                    'NodeSnapshots': [
                        {
                            'CacheClusterId': 'string',
                            'NodeGroupId': 'string',
                            'CacheNodeId': 'string',
                            'NodeGroupConfiguration': {
                                'Slots': 'string',
                                'ReplicaCount': 123,
                                'PrimaryAvailabilityZone': 'string',
                                'ReplicaAvailabilityZones': [
                                    'string',
                                ]
                            },
                            'CacheSize': 'string',
                            'CacheNodeCreateTime': datetime(2015, 1, 1),
                            'SnapshotCreateTime': datetime(2015, 1, 1)
                        },
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the output of a ``DescribeSnapshots`` operation.

        
        

        - **Snapshots** *(list) --* 

          A list of snapshots. Each item in the list contains detailed information about one snapshot.

          
          

          - *(dict) --* 

            Represents a copy of an entire Redis cluster as of the time when the snapshot was taken.

            
            

            - **SnapshotName** *(string) --* 

              The name of a snapshot. For an automatic snapshot, the name is system-generated. For a manual snapshot, this is the user-provided name.

              
            

            - **ReplicationGroupId** *(string) --* 

              The unique identifier of the source replication group.

              
            

            - **ReplicationGroupDescription** *(string) --* 

              A description of the source replication group.

              
            

            - **CacheClusterId** *(string) --* 

              The user-supplied identifier of the source cluster.

              
            

            - **SnapshotStatus** *(string) --* 

              The status of the snapshot. Valid values: ``creating`` | ``available`` | ``restoring`` | ``copying`` | ``deleting`` .

              
            

            - **SnapshotSource** *(string) --* 

              Indicates whether the snapshot is from an automatic backup (``automated`` ) or was created manually (``manual`` ).

              
            

            - **CacheNodeType** *(string) --* 

              The name of the compute and memory capacity node type for the source cluster.

               

              The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

               

               
              * General purpose: 

                 
                * Current generation:   **T2 node types:**  ``cache.t2.micro`` , ``cache.t2.small`` , ``cache.t2.medium``    **M3 node types:**  ``cache.m3.medium`` , ``cache.m3.large`` , ``cache.m3.xlarge`` , ``cache.m3.2xlarge``    **M4 node types:**  ``cache.m4.large`` , ``cache.m4.xlarge`` , ``cache.m4.2xlarge`` , ``cache.m4.4xlarge`` , ``cache.m4.10xlarge``   
                 
                * Previous generation: (not recommended)  **T1 node types:**  ``cache.t1.micro``    **M1 node types:**  ``cache.m1.small`` , ``cache.m1.medium`` , ``cache.m1.large`` , ``cache.m1.xlarge``   
                 

               
               
              * Compute optimized: 

                 
                * Previous generation: (not recommended)  **C1 node types:**  ``cache.c1.xlarge``   
                 

               
               
              * Memory optimized: 

                 
                * Current generation:   **R3 node types:**  ``cache.r3.large`` , ``cache.r3.xlarge`` , ``cache.r3.2xlarge`` , ``cache.r3.4xlarge`` , ``cache.r3.8xlarge``   
                 
                * Previous generation: (not recommended)  **M2 node types:**  ``cache.m2.xlarge`` , ``cache.m2.2xlarge`` , ``cache.m2.4xlarge``   
                 

               
               

               

               **Notes:**  

               

               
              * All T2 instances are created in an Amazon Virtual Private Cloud (Amazon VPC). 
               
              * Redis (cluster mode disabled): Redis backup/restore is not supported on T1 and T2 instances.  
               
              * Redis (cluster mode enabled): Backup/restore is not supported on T1 instances. 
               
              * Redis Append-only files (AOF) functionality is not supported for T1 or T2 instances. 
               

               

              For a complete listing of node types and specifications, see `Amazon ElastiCache Product Features and Details <http://aws.amazon.com/elasticache/details>`__ and either `Cache Node Type-Specific Parameters for Memcached <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Memcached.html#ParameterGroups.Memcached.NodeSpecific>`__ or `Cache Node Type-Specific Parameters for Redis <http://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/CacheParameterGroups.Redis.html#ParameterGroups.Redis.NodeSpecific>`__ .

              
            

            - **Engine** *(string) --* 

              The name of the cache engine (``memcached`` or ``redis`` ) used by the source cluster.

              
            

            - **EngineVersion** *(string) --* 

              The version of the cache engine version that is used by the source cluster.

              
            

            - **NumCacheNodes** *(integer) --* 

              The number of cache nodes in the source cluster.

               

              For clusters running Redis, this value must be 1. For clusters running Memcached, this value must be between 1 and 20.

              
            

            - **PreferredAvailabilityZone** *(string) --* 

              The name of the Availability Zone in which the source cluster is located.

              
            

            - **CacheClusterCreateTime** *(datetime) --* 

              The date and time when the source cluster was created.

              
            

            - **PreferredMaintenanceWindow** *(string) --* 

              Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.

               

              Valid values for ``ddd`` are:

               

               
              * ``sun``   
               
              * ``mon``   
               
              * ``tue``   
               
              * ``wed``   
               
              * ``thu``   
               
              * ``fri``   
               
              * ``sat``   
               

               

              Example: ``sun:23:00-mon:01:30``  

              
            

            - **TopicArn** *(string) --* 

              The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing notifications.

              
            

            - **Port** *(integer) --* 

              The port number used by each cache nodes in the source cluster.

              
            

            - **CacheParameterGroupName** *(string) --* 

              The cache parameter group that is associated with the source cluster.

              
            

            - **CacheSubnetGroupName** *(string) --* 

              The name of the cache subnet group associated with the source cluster.

              
            

            - **VpcId** *(string) --* 

              The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the source cluster.

              
            

            - **AutoMinorVersionUpgrade** *(boolean) --* 

              This parameter is currently disabled.

              
            

            - **SnapshotRetentionLimit** *(integer) --* 

              For an automatic snapshot, the number of days for which ElastiCache retains the snapshot before deleting it.

               

              For manual snapshots, this field reflects the ``SnapshotRetentionLimit`` for the source cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots do not expire, and can only be deleted using the ``DeleteSnapshot`` operation. 

               

               **Important** If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

              
            

            - **SnapshotWindow** *(string) --* 

              The daily time range during which ElastiCache takes daily snapshots of the source cluster.

              
            

            - **NumNodeGroups** *(integer) --* 

              The number of node groups (shards) in this snapshot. When restoring from a snapshot, the number of node groups (shards) in the snapshot and in the restored replication group must be the same.

              
            

            - **AutomaticFailover** *(string) --* 

              Indicates the status of Multi-AZ with automatic failover for the source Redis replication group.

               

              Amazon ElastiCache for Redis does not support Multi-AZ with automatic failover on:

               

               
              * Redis versions earlier than 2.8.6. 
               
              * Redis (cluster mode disabled): T1 and T2 cache node types. 
               
              * Redis (cluster mode enabled): T1 node types. 
               

              
            

            - **NodeSnapshots** *(list) --* 

              A list of the cache nodes in the source cluster.

              
              

              - *(dict) --* 

                Represents an individual cache node in a snapshot of a cluster.

                
                

                - **CacheClusterId** *(string) --* 

                  A unique identifier for the source cluster.

                  
                

                - **NodeGroupId** *(string) --* 

                  A unique identifier for the source node group (shard).

                  
                

                - **CacheNodeId** *(string) --* 

                  The cache node identifier for the node in the source cluster.

                  
                

                - **NodeGroupConfiguration** *(dict) --* 

                  The configuration for the source node group (shard).

                  
                  

                  - **Slots** *(string) --* 

                    A string that specifies the keyspace for a particular node group. Keyspaces range from 0 to 16,383. The string is in the format ``startkey-endkey`` .

                     

                    Example: ``"0-3999"``  

                    
                  

                  - **ReplicaCount** *(integer) --* 

                    The number of read replica nodes in this node group (shard).

                    
                  

                  - **PrimaryAvailabilityZone** *(string) --* 

                    The Availability Zone where the primary node of this node group (shard) is launched.

                    
                  

                  - **ReplicaAvailabilityZones** *(list) --* 

                    A list of Availability Zones to be used for the read replicas. The number of Availability Zones in this list must match the value of ``ReplicaCount`` or ``ReplicasPerNodeGroup`` if not specified.

                    
                    

                    - *(string) --* 
                
              
                

                - **CacheSize** *(string) --* 

                  The size of the cache on the source cache node.

                  
                

                - **CacheNodeCreateTime** *(datetime) --* 

                  The date and time when the cache node was created in the source cluster.

                  
                

                - **SnapshotCreateTime** *(datetime) --* 

                  The date and time when the source node's metadata and cache data set was obtained for the snapshot.

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

=======
Waiters
=======


The available waiters are:

* :py:class:`ElastiCache.Waiter.CacheClusterAvailable`


* :py:class:`ElastiCache.Waiter.CacheClusterDeleted`


* :py:class:`ElastiCache.Waiter.ReplicationGroupAvailable`


* :py:class:`ElastiCache.Waiter.ReplicationGroupDeleted`



.. py:class:: ElastiCache.Waiter.CacheClusterAvailable

  ::

    
    waiter = client.get_waiter('cache_cluster_available')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`ElastiCache.Client.describe_cache_clusters` every 30 seconds until a successful state is reached. An error is returned after 60 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheClusters>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          CacheClusterId='string',
          MaxRecords=123,
          Marker='string',
          ShowCacheNodeInfo=True|False,
          ShowCacheClustersNotInReplicationGroups=True|False,
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type CacheClusterId: string
    :param CacheClusterId: 

      The user-supplied cluster identifier. If this parameter is specified, only information about that specific cluster is returned. This parameter isn't case sensitive.

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a marker is included in the response so that the remaining results can be retrieved.

       

      Default: 100

       

      Constraints: minimum 20; maximum 100.

      

    
    :type Marker: string
    :param Marker: 

      An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

      

    
    :type ShowCacheNodeInfo: boolean
    :param ShowCacheNodeInfo: 

      An optional flag that can be included in the ``DescribeCacheCluster`` request to retrieve information about the individual cache nodes.

      

    
    :type ShowCacheClustersNotInReplicationGroups: boolean
    :param ShowCacheClustersNotInReplicationGroups: 

      An optional flag that can be included in the ``DescribeCacheCluster`` request to show only nodes (API/CLI: clusters) that are not members of a replication group. In practice, this mean Memcached and single node Redis clusters.

      

    
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 30

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 60

        

      
    
    
    :returns: None

.. py:class:: ElastiCache.Waiter.CacheClusterDeleted

  ::

    
    waiter = client.get_waiter('cache_cluster_deleted')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`ElastiCache.Client.describe_cache_clusters` every 30 seconds until a successful state is reached. An error is returned after 60 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheClusters>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          CacheClusterId='string',
          MaxRecords=123,
          Marker='string',
          ShowCacheNodeInfo=True|False,
          ShowCacheClustersNotInReplicationGroups=True|False,
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type CacheClusterId: string
    :param CacheClusterId: 

      The user-supplied cluster identifier. If this parameter is specified, only information about that specific cluster is returned. This parameter isn't case sensitive.

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a marker is included in the response so that the remaining results can be retrieved.

       

      Default: 100

       

      Constraints: minimum 20; maximum 100.

      

    
    :type Marker: string
    :param Marker: 

      An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

      

    
    :type ShowCacheNodeInfo: boolean
    :param ShowCacheNodeInfo: 

      An optional flag that can be included in the ``DescribeCacheCluster`` request to retrieve information about the individual cache nodes.

      

    
    :type ShowCacheClustersNotInReplicationGroups: boolean
    :param ShowCacheClustersNotInReplicationGroups: 

      An optional flag that can be included in the ``DescribeCacheCluster`` request to show only nodes (API/CLI: clusters) that are not members of a replication group. In practice, this mean Memcached and single node Redis clusters.

      

    
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 30

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 60

        

      
    
    
    :returns: None

.. py:class:: ElastiCache.Waiter.ReplicationGroupAvailable

  ::

    
    waiter = client.get_waiter('replication_group_available')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`ElastiCache.Client.describe_replication_groups` every 30 seconds until a successful state is reached. An error is returned after 60 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeReplicationGroups>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          ReplicationGroupId='string',
          MaxRecords=123,
          Marker='string',
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type ReplicationGroupId: string
    :param ReplicationGroupId: 

      The identifier for the replication group to be described. This parameter is not case sensitive.

       

      If you do not specify this parameter, information about all replication groups is returned.

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a marker is included in the response so that the remaining results can be retrieved.

       

      Default: 100

       

      Constraints: minimum 20; maximum 100.

      

    
    :type Marker: string
    :param Marker: 

      An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

      

    
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 30

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 60

        

      
    
    
    :returns: None

.. py:class:: ElastiCache.Waiter.ReplicationGroupDeleted

  ::

    
    waiter = client.get_waiter('replication_group_deleted')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`ElastiCache.Client.describe_replication_groups` every 30 seconds until a successful state is reached. An error is returned after 60 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeReplicationGroups>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          ReplicationGroupId='string',
          MaxRecords=123,
          Marker='string',
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type ReplicationGroupId: string
    :param ReplicationGroupId: 

      The identifier for the replication group to be described. This parameter is not case sensitive.

       

      If you do not specify this parameter, information about all replication groups is returned.

      

    
    :type MaxRecords: integer
    :param MaxRecords: 

      The maximum number of records to include in the response. If more records exist than the specified ``MaxRecords`` value, a marker is included in the response so that the remaining results can be retrieved.

       

      Default: 100

       

      Constraints: minimum 20; maximum 100.

      

    
    :type Marker: string
    :param Marker: 

      An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by ``MaxRecords`` .

      

    
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 30

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 60

        

      
    
    
    :returns: None