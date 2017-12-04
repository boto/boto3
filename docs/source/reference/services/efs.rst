

***
EFS
***

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: EFS.Client

  A low-level client representing Amazon Elastic File System (EFS)::

    
    import boto3
    
    client = boto3.client('efs')

  
  These are the available methods:
  
  *   :py:meth:`~EFS.Client.can_paginate`

  
  *   :py:meth:`~EFS.Client.create_file_system`

  
  *   :py:meth:`~EFS.Client.create_mount_target`

  
  *   :py:meth:`~EFS.Client.create_tags`

  
  *   :py:meth:`~EFS.Client.delete_file_system`

  
  *   :py:meth:`~EFS.Client.delete_mount_target`

  
  *   :py:meth:`~EFS.Client.delete_tags`

  
  *   :py:meth:`~EFS.Client.describe_file_systems`

  
  *   :py:meth:`~EFS.Client.describe_mount_target_security_groups`

  
  *   :py:meth:`~EFS.Client.describe_mount_targets`

  
  *   :py:meth:`~EFS.Client.describe_tags`

  
  *   :py:meth:`~EFS.Client.generate_presigned_url`

  
  *   :py:meth:`~EFS.Client.get_paginator`

  
  *   :py:meth:`~EFS.Client.get_waiter`

  
  *   :py:meth:`~EFS.Client.modify_mount_target_security_groups`

  

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


  .. py:method:: create_file_system(**kwargs)

    

    Creates a new, empty file system. The operation requires a creation token in the request that Amazon EFS uses to ensure idempotent creation (calling the operation with same creation token has no effect). If a file system does not currently exist that is owned by the caller's AWS account with the specified creation token, this operation does the following:

     

     
    * Creates a new, empty file system. The file system will have an Amazon EFS assigned ID, and an initial lifecycle state ``creating`` . 
     
    * Returns with the description of the created file system. 
     

     

    Otherwise, this operation returns a ``FileSystemAlreadyExists`` error with the ID of the existing file system.

     

    .. note::

       

      For basic use cases, you can use a randomly generated UUID for the creation token.

       

     

    The idempotent operation allows you to retry a ``CreateFileSystem`` call without risk of creating an extra file system. This can happen when an initial call fails in a way that leaves it uncertain whether or not a file system was actually created. An example might be that a transport level timeout occurred or your connection was reset. As long as you use the same creation token, if the initial call had succeeded in creating a file system, the client can learn of its existence from the ``FileSystemAlreadyExists`` error.

     

    .. note::

       

      The ``CreateFileSystem`` call returns while the file system's lifecycle state is still ``creating`` . You can check the file system creation status by calling the  DescribeFileSystems operation, which among other things returns the file system state.

       

     

    This operation also takes an optional ``PerformanceMode`` parameter that you choose for your file system. We recommend ``generalPurpose`` performance mode for most file systems. File systems using the ``maxIO`` performance mode can scale to higher levels of aggregate throughput and operations per second with a tradeoff of slightly higher latencies for most file operations. The performance mode can't be changed after the file system has been created. For more information, see `Amazon EFS\: Performance Modes <http://docs.aws.amazon.com/efs/latest/ug/performance.html#performancemodes.html>`__ .

     

    After the file system is fully created, Amazon EFS sets its lifecycle state to ``available`` , at which point you can create one or more mount targets for the file system in your VPC. For more information, see  CreateMountTarget . You mount your Amazon EFS file system on an EC2 instances in your VPC via the mount target. For more information, see `Amazon EFS\: How it Works <http://docs.aws.amazon.com/efs/latest/ug/how-it-works.html>`__ . 

     

    This operation requires permissions for the ``elasticfilesystem:CreateFileSystem`` action. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/CreateFileSystem>`_    


    **Request Syntax** 
    ::

      response = client.create_file_system(
          CreationToken='string',
          PerformanceMode='generalPurpose'|'maxIO',
          Encrypted=True|False,
          KmsKeyId='string'
      )
    :type CreationToken: string
    :param CreationToken: **[REQUIRED]** 

      String of up to 64 ASCII characters. Amazon EFS uses this to ensure idempotent creation.

      

    
    :type PerformanceMode: string
    :param PerformanceMode: 

      The ``PerformanceMode`` of the file system. We recommend ``generalPurpose`` performance mode for most file systems. File systems using the ``maxIO`` performance mode can scale to higher levels of aggregate throughput and operations per second with a tradeoff of slightly higher latencies for most file operations. This can't be changed after the file system has been created.

      

    
    :type Encrypted: boolean
    :param Encrypted: 

      A boolean value that, if true, creates an encrypted file system. When creating an encrypted file system, you have the option of specifying a  CreateFileSystemRequest$KmsKeyId for an existing AWS Key Management Service (AWS KMS) customer master key (CMK). If you don't specify a CMK, then the default CMK for Amazon EFS, ``/aws/elasticfilesystem`` , is used to protect the encrypted file system. 

      

    
    :type KmsKeyId: string
    :param KmsKeyId: 

      The id of the AWS KMS CMK that will be used to protect the encrypted file system. This parameter is only required if you want to use a non-default CMK. If this parameter is not specified, the default CMK for Amazon EFS is used. This id can be in one of the following formats:

       

       
      * Key ID - A unique identifier of the key. For example, ``1234abcd-12ab-34cd-56ef-1234567890ab`` . 
       
      * ARN - An Amazon Resource Name for the key. For example, ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` . 
       
      * Key alias - A previously created display name for a key. For example, ``alias/projectKey1`` . 
       
      * Key alias ARN - An Amazon Resource Name for a key alias. For example, ``arn:aws:kms:us-west-2:444455556666:alias/projectKey1`` . 
       

       

      Note that if the KmsKeyId is specified, the  CreateFileSystemRequest$Encrypted parameter must be set to true.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'OwnerId': 'string',
            'CreationToken': 'string',
            'FileSystemId': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'LifeCycleState': 'creating'|'available'|'deleting'|'deleted',
            'Name': 'string',
            'NumberOfMountTargets': 123,
            'SizeInBytes': {
                'Value': 123,
                'Timestamp': datetime(2015, 1, 1)
            },
            'PerformanceMode': 'generalPurpose'|'maxIO',
            'Encrypted': True|False,
            'KmsKeyId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Description of the file system.

        
        

        - **OwnerId** *(string) --* 

          AWS account that created the file system. If the file system was created by an IAM user, the parent account to which the user belongs is the owner.

          
        

        - **CreationToken** *(string) --* 

          Opaque string specified in the request.

          
        

        - **FileSystemId** *(string) --* 

          ID of the file system, assigned by Amazon EFS.

          
        

        - **CreationTime** *(datetime) --* 

          Time that the file system was created, in seconds (since 1970-01-01T00:00:00Z).

          
        

        - **LifeCycleState** *(string) --* 

          Lifecycle phase of the file system.

          
        

        - **Name** *(string) --* 

          You can add tags to a file system, including a ``Name`` tag. For more information, see  CreateTags . If the file system has a ``Name`` tag, Amazon EFS returns the value in this field. 

          
        

        - **NumberOfMountTargets** *(integer) --* 

          Current number of mount targets that the file system has. For more information, see  CreateMountTarget .

          
        

        - **SizeInBytes** *(dict) --* 

          Latest known metered size (in bytes) of data stored in the file system, in bytes, in its ``Value`` field, and the time at which that size was determined in its ``Timestamp`` field. The ``Timestamp`` value is the integer number of seconds since 1970-01-01T00:00:00Z. Note that the value does not represent the size of a consistent snapshot of the file system, but it is eventually consistent when there are no writes to the file system. That is, the value will represent actual size only if the file system is not modified for a period longer than a couple of hours. Otherwise, the value is not the exact size the file system was at any instant in time. 

          
          

          - **Value** *(integer) --* 

            Latest known metered size (in bytes) of data stored in the file system.

            
          

          - **Timestamp** *(datetime) --* 

            Time at which the size of data, returned in the ``Value`` field, was determined. The value is the integer number of seconds since 1970-01-01T00:00:00Z.

            
      
        

        - **PerformanceMode** *(string) --* 

          The ``PerformanceMode`` of the file system.

          
        

        - **Encrypted** *(boolean) --* 

          A boolean value that, if true, indicates that the file system is encrypted.

          
        

        - **KmsKeyId** *(string) --* 

          The id of an AWS Key Management Service (AWS KMS) customer master key (CMK) that was used to protect the encrypted file system.

          
    

    **Examples** 

    This operation creates a new file system with the default generalpurpose performance mode.
    ::

      response = client.create_file_system(
          CreationToken='tokenstring',
          PerformanceMode='generalPurpose',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'CreationTime': datetime(2016, 12, 15, 14, 38, 44, 3, 350, 0),
          'CreationToken': 'tokenstring',
          'FileSystemId': 'fs-01234567',
          'LifeCycleState': 'creating',
          'NumberOfMountTargets': 0,
          'OwnerId': '012345678912',
          'PerformanceMode': 'generalPurpose',
          'SizeInBytes': {
              'Value': 0,
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_mount_target(**kwargs)

    

    Creates a mount target for a file system. You can then mount the file system on EC2 instances via the mount target.

     

    You can create one mount target in each Availability Zone in your VPC. All EC2 instances in a VPC within a given Availability Zone share a single mount target for a given file system. If you have multiple subnets in an Availability Zone, you create a mount target in one of the subnets. EC2 instances do not need to be in the same subnet as the mount target in order to access their file system. For more information, see `Amazon EFS\: How it Works <http://docs.aws.amazon.com/efs/latest/ug/how-it-works.html>`__ . 

     

    In the request, you also specify a file system ID for which you are creating the mount target and the file system's lifecycle state must be ``available`` . For more information, see  DescribeFileSystems .

     

    In the request, you also provide a subnet ID, which determines the following:

     

     
    * VPC in which Amazon EFS creates the mount target 
     
    * Availability Zone in which Amazon EFS creates the mount target 
     
    * IP address range from which Amazon EFS selects the IP address of the mount target (if you don't specify an IP address in the request) 
     

     

    After creating the mount target, Amazon EFS returns a response that includes, a ``MountTargetId`` and an ``IpAddress`` . You use this IP address when mounting the file system in an EC2 instance. You can also use the mount target's DNS name when mounting the file system. The EC2 instance on which you mount the file system via the mount target can resolve the mount target's DNS name to its IP address. For more information, see `How it Works\: Implementation Overview <http://docs.aws.amazon.com/efs/latest/ug/how-it-works.html#how-it-works-implementation>`__ . 

     

    Note that you can create mount targets for a file system in only one VPC, and there can be only one mount target per Availability Zone. That is, if the file system already has one or more mount targets created for it, the subnet specified in the request to add another mount target must meet the following requirements:

     

     
    * Must belong to the same VPC as the subnets of the existing mount targets 
     
    * Must not be in the same Availability Zone as any of the subnets of the existing mount targets 
     

     

    If the request satisfies the requirements, Amazon EFS does the following:

     

     
    * Creates a new mount target in the specified subnet. 
     
    * Also creates a new network interface in the subnet as follows: 

       
      * If the request provides an ``IpAddress`` , Amazon EFS assigns that IP address to the network interface. Otherwise, Amazon EFS assigns a free address in the subnet (in the same way that the Amazon EC2 ``CreateNetworkInterface`` call does when a request does not specify a primary private IP address). 
       
      * If the request provides ``SecurityGroups`` , this network interface is associated with those security groups. Otherwise, it belongs to the default security group for the subnet's VPC. 
       
      * Assigns the description ``Mount target *fsmt-id* for file system *fs-id* `` where `` *fsmt-id* `` is the mount target ID, and `` *fs-id* `` is the ``FileSystemId`` . 
       
      * Sets the ``requesterManaged`` property of the network interface to ``true`` , and the ``requesterId`` value to ``EFS`` . 
       

     

    Each Amazon EFS mount target has one corresponding requester-managed EC2 network interface. After the network interface is created, Amazon EFS sets the ``NetworkInterfaceId`` field in the mount target's description to the network interface ID, and the ``IpAddress`` field to its address. If network interface creation fails, the entire ``CreateMountTarget`` operation fails.

     
     

     

    .. note::

       

      The ``CreateMountTarget`` call returns only after creating the network interface, but while the mount target state is still ``creating`` , you can check the mount target creation status by calling the  DescribeMountTargets operation, which among other things returns the mount target state.

       

     

    We recommend you create a mount target in each of the Availability Zones. There are cost considerations for using a file system in an Availability Zone through a mount target created in another Availability Zone. For more information, see `Amazon EFS <http://aws.amazon.com/efs/>`__ . In addition, by always using a mount target local to the instance's Availability Zone, you eliminate a partial failure scenario. If the Availability Zone in which your mount target is created goes down, then you won't be able to access your file system through that mount target. 

     

    This operation requires permissions for the following action on the file system:

     

     
    * ``elasticfilesystem:CreateMountTarget``   
     

     

    This operation also requires permissions for the following Amazon EC2 actions:

     

     
    * ``ec2:DescribeSubnets``   
     
    * ``ec2:DescribeNetworkInterfaces``   
     
    * ``ec2:CreateNetworkInterface``   
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/CreateMountTarget>`_    


    **Request Syntax** 
    ::

      response = client.create_mount_target(
          FileSystemId='string',
          SubnetId='string',
          IpAddress='string',
          SecurityGroups=[
              'string',
          ]
      )
    :type FileSystemId: string
    :param FileSystemId: **[REQUIRED]** 

      ID of the file system for which to create the mount target.

      

    
    :type SubnetId: string
    :param SubnetId: **[REQUIRED]** 

      ID of the subnet to add the mount target in.

      

    
    :type IpAddress: string
    :param IpAddress: 

      Valid IPv4 address within the address range of the specified subnet.

      

    
    :type SecurityGroups: list
    :param SecurityGroups: 

      Up to five VPC security group IDs, of the form ``sg-xxxxxxxx`` . These must be for the same VPC as subnet specified.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'OwnerId': 'string',
            'MountTargetId': 'string',
            'FileSystemId': 'string',
            'SubnetId': 'string',
            'LifeCycleState': 'creating'|'available'|'deleting'|'deleted',
            'IpAddress': 'string',
            'NetworkInterfaceId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Provides a description of a mount target.

        
        

        - **OwnerId** *(string) --* 

          AWS account ID that owns the resource.

          
        

        - **MountTargetId** *(string) --* 

          System-assigned mount target ID.

          
        

        - **FileSystemId** *(string) --* 

          ID of the file system for which the mount target is intended.

          
        

        - **SubnetId** *(string) --* 

          ID of the mount target's subnet.

          
        

        - **LifeCycleState** *(string) --* 

          Lifecycle state of the mount target.

          
        

        - **IpAddress** *(string) --* 

          Address at which the file system may be mounted via the mount target.

          
        

        - **NetworkInterfaceId** *(string) --* 

          ID of the network interface that Amazon EFS created when it created the mount target.

          
    

    **Examples** 

    This operation creates a new mount target for an EFS file system.
    ::

      response = client.create_mount_target(
          FileSystemId='fs-01234567',
          SubnetId='subnet-1234abcd',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'FileSystemId': 'fs-01234567',
          'IpAddress': '192.0.0.2',
          'LifeCycleState': 'creating',
          'MountTargetId': 'fsmt-12340abc',
          'NetworkInterfaceId': 'eni-cedf6789',
          'OwnerId': '012345678912',
          'SubnetId': 'subnet-1234abcd',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_tags(**kwargs)

    

    Creates or overwrites tags associated with a file system. Each tag is a key-value pair. If a tag key specified in the request already exists on the file system, this operation overwrites its value with the value provided in the request. If you add the ``Name`` tag to your file system, Amazon EFS returns it in the response to the  DescribeFileSystems operation. 

     

    This operation requires permission for the ``elasticfilesystem:CreateTags`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/CreateTags>`_    


    **Request Syntax** 
    ::

      response = client.create_tags(
          FileSystemId='string',
          Tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type FileSystemId: string
    :param FileSystemId: **[REQUIRED]** 

      ID of the file system whose tags you want to modify (String). This operation modifies the tags only, not the file system.

      

    
    :type Tags: list
    :param Tags: **[REQUIRED]** 

      Array of ``Tag`` objects to add. Each ``Tag`` object is a key-value pair. 

      

    
      - *(dict) --* 

        A tag is a key-value pair. Allowed characters: letters, whitespace, and numbers, representable in UTF-8, and the following characters:``+ - = . _ : /``  

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          Tag key (String). The key can't start with ``aws:`` .

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          Value of the tag key.

          

        
      
  
    
    :returns: None

    **Examples** 

    This operation creates a new tag for an EFS file system.
    ::

      response = client.create_tags(
          FileSystemId='fs-01234567',
          Tags=[
              {
                  'Key': 'Name',
                  'Value': 'MyFileSystem',
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

    

  .. py:method:: delete_file_system(**kwargs)

    

    Deletes a file system, permanently severing access to its contents. Upon return, the file system no longer exists and you can't access any contents of the deleted file system.

     

    You can't delete a file system that is in use. That is, if the file system has any mount targets, you must first delete them. For more information, see  DescribeMountTargets and  DeleteMountTarget . 

     

    .. note::

       

      The ``DeleteFileSystem`` call returns while the file system state is still ``deleting`` . You can check the file system deletion status by calling the  DescribeFileSystems operation, which returns a list of file systems in your account. If you pass file system ID or creation token for the deleted file system, the  DescribeFileSystems returns a ``404 FileSystemNotFound`` error.

       

     

    This operation requires permissions for the ``elasticfilesystem:DeleteFileSystem`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/DeleteFileSystem>`_    


    **Request Syntax** 
    ::

      response = client.delete_file_system(
          FileSystemId='string'
      )
    :type FileSystemId: string
    :param FileSystemId: **[REQUIRED]** 

      ID of the file system you want to delete.

      

    
    
    :returns: None

    **Examples** 

    This operation deletes an EFS file system.
    ::

      response = client.delete_file_system(
          FileSystemId='fs-01234567',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_mount_target(**kwargs)

    

    Deletes the specified mount target.

     

    This operation forcibly breaks any mounts of the file system via the mount target that is being deleted, which might disrupt instances or applications using those mounts. To avoid applications getting cut off abruptly, you might consider unmounting any mounts of the mount target, if feasible. The operation also deletes the associated network interface. Uncommitted writes may be lost, but breaking a mount target using this operation does not corrupt the file system itself. The file system you created remains. You can mount an EC2 instance in your VPC via another mount target.

     

    This operation requires permissions for the following action on the file system:

     

     
    * ``elasticfilesystem:DeleteMountTarget``   
     

     

    .. note::

       

      The ``DeleteMountTarget`` call returns while the mount target state is still ``deleting`` . You can check the mount target deletion by calling the  DescribeMountTargets operation, which returns a list of mount target descriptions for the given file system. 

       

     

    The operation also requires permissions for the following Amazon EC2 action on the mount target's network interface:

     

     
    * ``ec2:DeleteNetworkInterface``   
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/DeleteMountTarget>`_    


    **Request Syntax** 
    ::

      response = client.delete_mount_target(
          MountTargetId='string'
      )
    :type MountTargetId: string
    :param MountTargetId: **[REQUIRED]** 

      ID of the mount target to delete (String).

      

    
    
    :returns: None

    **Examples** 

    This operation deletes a mount target.
    ::

      response = client.delete_mount_target(
          MountTargetId='fsmt-12340abc',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_tags(**kwargs)

    

    Deletes the specified tags from a file system. If the ``DeleteTags`` request includes a tag key that does not exist, Amazon EFS ignores it and doesn't cause an error. For more information about tags and related restrictions, see `Tag Restrictions <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`__ in the *AWS Billing and Cost Management User Guide* .

     

    This operation requires permissions for the ``elasticfilesystem:DeleteTags`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/DeleteTags>`_    


    **Request Syntax** 
    ::

      response = client.delete_tags(
          FileSystemId='string',
          TagKeys=[
              'string',
          ]
      )
    :type FileSystemId: string
    :param FileSystemId: **[REQUIRED]** 

      ID of the file system whose tags you want to delete (String).

      

    
    :type TagKeys: list
    :param TagKeys: **[REQUIRED]** 

      List of tag keys to delete.

      

    
      - *(string) --* 

      
  
    
    :returns: None

    **Examples** 

    This operation deletes tags for an EFS file system.
    ::

      response = client.delete_tags(
          FileSystemId='fs-01234567',
          TagKeys=[
              'Name',
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

    

  .. py:method:: describe_file_systems(**kwargs)

    

    Returns the description of a specific Amazon EFS file system if either the file system ``CreationToken`` or the ``FileSystemId`` is provided. Otherwise, it returns descriptions of all file systems owned by the caller's AWS account in the AWS Region of the endpoint that you're calling.

     

    When retrieving all file system descriptions, you can optionally specify the ``MaxItems`` parameter to limit the number of descriptions in a response. If more file system descriptions remain, Amazon EFS returns a ``NextMarker`` , an opaque token, in the response. In this case, you should send a subsequent request with the ``Marker`` request parameter set to the value of ``NextMarker`` . 

     

    To retrieve a list of your file system descriptions, this operation is used in an iterative process, where ``DescribeFileSystems`` is called first without the ``Marker`` and then the operation continues to call it with the ``Marker`` parameter set to the value of the ``NextMarker`` from the previous response until the response has no ``NextMarker`` . 

     

    The implementation may return fewer than ``MaxItems`` file system descriptions while still including a ``NextMarker`` value. 

     

    The order of file systems returned in the response of one ``DescribeFileSystems`` call and the order of file systems returned across the responses of a multi-call iteration is unspecified. 

     

    This operation requires permissions for the ``elasticfilesystem:DescribeFileSystems`` action. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/DescribeFileSystems>`_    


    **Request Syntax** 
    ::

      response = client.describe_file_systems(
          MaxItems=123,
          Marker='string',
          CreationToken='string',
          FileSystemId='string'
      )
    :type MaxItems: integer
    :param MaxItems: 

      (Optional) Specifies the maximum number of file systems to return in the response (integer). This parameter value must be greater than 0. The number of items that Amazon EFS returns is the minimum of the ``MaxItems`` parameter specified in the request and the service's internal maximum number of items per page. 

      

    
    :type Marker: string
    :param Marker: 

      (Optional) Opaque pagination token returned from a previous ``DescribeFileSystems`` operation (String). If present, specifies to continue the list from where the returning call had left off. 

      

    
    :type CreationToken: string
    :param CreationToken: 

      (Optional) Restricts the list to the file system with this creation token (String). You specify a creation token when you create an Amazon EFS file system.

      

    
    :type FileSystemId: string
    :param FileSystemId: 

      (Optional) ID of the file system whose description you want to retrieve (String).

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Marker': 'string',
            'FileSystems': [
                {
                    'OwnerId': 'string',
                    'CreationToken': 'string',
                    'FileSystemId': 'string',
                    'CreationTime': datetime(2015, 1, 1),
                    'LifeCycleState': 'creating'|'available'|'deleting'|'deleted',
                    'Name': 'string',
                    'NumberOfMountTargets': 123,
                    'SizeInBytes': {
                        'Value': 123,
                        'Timestamp': datetime(2015, 1, 1)
                    },
                    'PerformanceMode': 'generalPurpose'|'maxIO',
                    'Encrypted': True|False,
                    'KmsKeyId': 'string'
                },
            ],
            'NextMarker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Marker** *(string) --* 

          Present if provided by caller in the request (String).

          
        

        - **FileSystems** *(list) --* 

          Array of file system descriptions.

          
          

          - *(dict) --* 

            Description of the file system.

            
            

            - **OwnerId** *(string) --* 

              AWS account that created the file system. If the file system was created by an IAM user, the parent account to which the user belongs is the owner.

              
            

            - **CreationToken** *(string) --* 

              Opaque string specified in the request.

              
            

            - **FileSystemId** *(string) --* 

              ID of the file system, assigned by Amazon EFS.

              
            

            - **CreationTime** *(datetime) --* 

              Time that the file system was created, in seconds (since 1970-01-01T00:00:00Z).

              
            

            - **LifeCycleState** *(string) --* 

              Lifecycle phase of the file system.

              
            

            - **Name** *(string) --* 

              You can add tags to a file system, including a ``Name`` tag. For more information, see  CreateTags . If the file system has a ``Name`` tag, Amazon EFS returns the value in this field. 

              
            

            - **NumberOfMountTargets** *(integer) --* 

              Current number of mount targets that the file system has. For more information, see  CreateMountTarget .

              
            

            - **SizeInBytes** *(dict) --* 

              Latest known metered size (in bytes) of data stored in the file system, in bytes, in its ``Value`` field, and the time at which that size was determined in its ``Timestamp`` field. The ``Timestamp`` value is the integer number of seconds since 1970-01-01T00:00:00Z. Note that the value does not represent the size of a consistent snapshot of the file system, but it is eventually consistent when there are no writes to the file system. That is, the value will represent actual size only if the file system is not modified for a period longer than a couple of hours. Otherwise, the value is not the exact size the file system was at any instant in time. 

              
              

              - **Value** *(integer) --* 

                Latest known metered size (in bytes) of data stored in the file system.

                
              

              - **Timestamp** *(datetime) --* 

                Time at which the size of data, returned in the ``Value`` field, was determined. The value is the integer number of seconds since 1970-01-01T00:00:00Z.

                
          
            

            - **PerformanceMode** *(string) --* 

              The ``PerformanceMode`` of the file system.

              
            

            - **Encrypted** *(boolean) --* 

              A boolean value that, if true, indicates that the file system is encrypted.

              
            

            - **KmsKeyId** *(string) --* 

              The id of an AWS Key Management Service (AWS KMS) customer master key (CMK) that was used to protect the encrypted file system.

              
        
      
        

        - **NextMarker** *(string) --* 

          Present if there are more file systems than returned in the response (String). You can use the ``NextMarker`` in the subsequent request to fetch the descriptions.

          
    

    **Examples** 

    This operation describes all of the EFS file systems in an account.
    ::

      response = client.describe_file_systems(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'FileSystems': [
              {
                  'CreationTime': datetime(2016, 12, 15, 14, 38, 44, 3, 350, 0),
                  'CreationToken': 'tokenstring',
                  'FileSystemId': 'fs-01234567',
                  'LifeCycleState': 'available',
                  'Name': 'MyFileSystem',
                  'NumberOfMountTargets': 1,
                  'OwnerId': '012345678912',
                  'PerformanceMode': 'generalPurpose',
                  'SizeInBytes': {
                      'Value': 6144,
                  },
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_mount_target_security_groups(**kwargs)

    

    Returns the security groups currently in effect for a mount target. This operation requires that the network interface of the mount target has been created and the lifecycle state of the mount target is not ``deleted`` .

     

    This operation requires permissions for the following actions:

     

     
    * ``elasticfilesystem:DescribeMountTargetSecurityGroups`` action on the mount target's file system.  
     
    * ``ec2:DescribeNetworkInterfaceAttribute`` action on the mount target's network interface.  
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/DescribeMountTargetSecurityGroups>`_    


    **Request Syntax** 
    ::

      response = client.describe_mount_target_security_groups(
          MountTargetId='string'
      )
    :type MountTargetId: string
    :param MountTargetId: **[REQUIRED]** 

      ID of the mount target whose security groups you want to retrieve.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'SecurityGroups': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **SecurityGroups** *(list) --* 

          Array of security groups.

          
          

          - *(string) --* 
      
    

    **Examples** 

    This operation describes all of the security groups for a file system's mount target.
    ::

      response = client.describe_mount_target_security_groups(
          MountTargetId='fsmt-12340abc',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'SecurityGroups': [
              'sg-fghi4567',
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_mount_targets(**kwargs)

    

    Returns the descriptions of all the current mount targets, or a specific mount target, for a file system. When requesting all of the current mount targets, the order of mount targets returned in the response is unspecified.

     

    This operation requires permissions for the ``elasticfilesystem:DescribeMountTargets`` action, on either the file system ID that you specify in ``FileSystemId`` , or on the file system of the mount target that you specify in ``MountTargetId`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/DescribeMountTargets>`_    


    **Request Syntax** 
    ::

      response = client.describe_mount_targets(
          MaxItems=123,
          Marker='string',
          FileSystemId='string',
          MountTargetId='string'
      )
    :type MaxItems: integer
    :param MaxItems: 

      (Optional) Maximum number of mount targets to return in the response. It must be an integer with a value greater than zero.

      

    
    :type Marker: string
    :param Marker: 

      (Optional) Opaque pagination token returned from a previous ``DescribeMountTargets`` operation (String). If present, it specifies to continue the list from where the previous returning call left off.

      

    
    :type FileSystemId: string
    :param FileSystemId: 

      (Optional) ID of the file system whose mount targets you want to list (String). It must be included in your request if ``MountTargetId`` is not included.

      

    
    :type MountTargetId: string
    :param MountTargetId: 

      (Optional) ID of the mount target that you want to have described (String). It must be included in your request if ``FileSystemId`` is not included.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Marker': 'string',
            'MountTargets': [
                {
                    'OwnerId': 'string',
                    'MountTargetId': 'string',
                    'FileSystemId': 'string',
                    'SubnetId': 'string',
                    'LifeCycleState': 'creating'|'available'|'deleting'|'deleted',
                    'IpAddress': 'string',
                    'NetworkInterfaceId': 'string'
                },
            ],
            'NextMarker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        

        
        

        - **Marker** *(string) --* 

          If the request included the ``Marker`` , the response returns that value in this field.

          
        

        - **MountTargets** *(list) --* 

          Returns the file system's mount targets as an array of ``MountTargetDescription`` objects.

          
          

          - *(dict) --* 

            Provides a description of a mount target.

            
            

            - **OwnerId** *(string) --* 

              AWS account ID that owns the resource.

              
            

            - **MountTargetId** *(string) --* 

              System-assigned mount target ID.

              
            

            - **FileSystemId** *(string) --* 

              ID of the file system for which the mount target is intended.

              
            

            - **SubnetId** *(string) --* 

              ID of the mount target's subnet.

              
            

            - **LifeCycleState** *(string) --* 

              Lifecycle state of the mount target.

              
            

            - **IpAddress** *(string) --* 

              Address at which the file system may be mounted via the mount target.

              
            

            - **NetworkInterfaceId** *(string) --* 

              ID of the network interface that Amazon EFS created when it created the mount target.

              
        
      
        

        - **NextMarker** *(string) --* 

          If a value is present, there are more mount targets to return. In a subsequent request, you can provide ``Marker`` in your request with this value to retrieve the next set of mount targets.

          
    

    **Examples** 

    This operation describes all of a file system's mount targets.
    ::

      response = client.describe_mount_targets(
          FileSystemId='fs-01234567',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'MountTargets': [
              {
                  'FileSystemId': 'fs-01234567',
                  'IpAddress': '192.0.0.2',
                  'LifeCycleState': 'available',
                  'MountTargetId': 'fsmt-12340abc',
                  'NetworkInterfaceId': 'eni-cedf6789',
                  'OwnerId': '012345678912',
                  'SubnetId': 'subnet-1234abcd',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_tags(**kwargs)

    

    Returns the tags associated with a file system. The order of tags returned in the response of one ``DescribeTags`` call and the order of tags returned across the responses of a multi-call iteration (when using pagination) is unspecified. 

     

    This operation requires permissions for the ``elasticfilesystem:DescribeTags`` action. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/DescribeTags>`_    


    **Request Syntax** 
    ::

      response = client.describe_tags(
          MaxItems=123,
          Marker='string',
          FileSystemId='string'
      )
    :type MaxItems: integer
    :param MaxItems: 

      (Optional) Maximum number of file system tags to return in the response. It must be an integer with a value greater than zero.

      

    
    :type Marker: string
    :param Marker: 

      (Optional) Opaque pagination token returned from a previous ``DescribeTags`` operation (String). If present, it specifies to continue the list from where the previous call left off.

      

    
    :type FileSystemId: string
    :param FileSystemId: **[REQUIRED]** 

      ID of the file system whose tag set you want to retrieve.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Marker': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'NextMarker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        

        
        

        - **Marker** *(string) --* 

          If the request included a ``Marker`` , the response returns that value in this field.

          
        

        - **Tags** *(list) --* 

          Returns tags associated with the file system as an array of ``Tag`` objects. 

          
          

          - *(dict) --* 

            A tag is a key-value pair. Allowed characters: letters, whitespace, and numbers, representable in UTF-8, and the following characters:``+ - = . _ : /``  

            
            

            - **Key** *(string) --* 

              Tag key (String). The key can't start with ``aws:`` .

              
            

            - **Value** *(string) --* 

              Value of the tag key.

              
        
      
        

        - **NextMarker** *(string) --* 

          If a value is present, there are more tags to return. In a subsequent request, you can provide the value of ``NextMarker`` as the value of the ``Marker`` parameter in your next request to retrieve the next set of tags.

          
    

    **Examples** 

    This operation describes all of a file system's tags.
    ::

      response = client.describe_tags(
          FileSystemId='fs-01234567',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Tags': [
              {
                  'Key': 'Name',
                  'Value': 'MyFileSystem',
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

        


  .. py:method:: modify_mount_target_security_groups(**kwargs)

    

    Modifies the set of security groups in effect for a mount target.

     

    When you create a mount target, Amazon EFS also creates a new network interface. For more information, see  CreateMountTarget . This operation replaces the security groups in effect for the network interface associated with a mount target, with the ``SecurityGroups`` provided in the request. This operation requires that the network interface of the mount target has been created and the lifecycle state of the mount target is not ``deleted`` . 

     

    The operation requires permissions for the following actions:

     

     
    * ``elasticfilesystem:ModifyMountTargetSecurityGroups`` action on the mount target's file system.  
     
    * ``ec2:ModifyNetworkInterfaceAttribute`` action on the mount target's network interface.  
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/ModifyMountTargetSecurityGroups>`_    


    **Request Syntax** 
    ::

      response = client.modify_mount_target_security_groups(
          MountTargetId='string',
          SecurityGroups=[
              'string',
          ]
      )
    :type MountTargetId: string
    :param MountTargetId: **[REQUIRED]** 

      ID of the mount target whose security groups you want to modify.

      

    
    :type SecurityGroups: list
    :param SecurityGroups: 

      Array of up to five VPC security group IDs.

      

    
      - *(string) --* 

      
  
    
    :returns: None

    **Examples** 

    This operation modifies the security groups associated with a mount target for a file system.
    ::

      response = client.modify_mount_target_security_groups(
          MountTargetId='fsmt-12340abc',
          SecurityGroups=[
              'sg-abcd1234',
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

    

==========
Paginators
==========


The available paginators are:

* :py:class:`EFS.Paginator.DescribeFileSystems`


* :py:class:`EFS.Paginator.DescribeMountTargets`


* :py:class:`EFS.Paginator.DescribeTags`



.. py:class:: EFS.Paginator.DescribeFileSystems

  ::

    
    paginator = client.get_paginator('describe_file_systems')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`EFS.Client.describe_file_systems`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/DescribeFileSystems>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          CreationToken='string',
          FileSystemId='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type CreationToken: string
    :param CreationToken: 

      (Optional) Restricts the list to the file system with this creation token (String). You specify a creation token when you create an Amazon EFS file system.

      

    
    :type FileSystemId: string
    :param FileSystemId: 

      (Optional) ID of the file system whose description you want to retrieve (String).

      

    
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
            'Marker': 'string',
            'FileSystems': [
                {
                    'OwnerId': 'string',
                    'CreationToken': 'string',
                    'FileSystemId': 'string',
                    'CreationTime': datetime(2015, 1, 1),
                    'LifeCycleState': 'creating'|'available'|'deleting'|'deleted',
                    'Name': 'string',
                    'NumberOfMountTargets': 123,
                    'SizeInBytes': {
                        'Value': 123,
                        'Timestamp': datetime(2015, 1, 1)
                    },
                    'PerformanceMode': 'generalPurpose'|'maxIO',
                    'Encrypted': True|False,
                    'KmsKeyId': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Marker** *(string) --* 

          Present if provided by caller in the request (String).

          
        

        - **FileSystems** *(list) --* 

          Array of file system descriptions.

          
          

          - *(dict) --* 

            Description of the file system.

            
            

            - **OwnerId** *(string) --* 

              AWS account that created the file system. If the file system was created by an IAM user, the parent account to which the user belongs is the owner.

              
            

            - **CreationToken** *(string) --* 

              Opaque string specified in the request.

              
            

            - **FileSystemId** *(string) --* 

              ID of the file system, assigned by Amazon EFS.

              
            

            - **CreationTime** *(datetime) --* 

              Time that the file system was created, in seconds (since 1970-01-01T00:00:00Z).

              
            

            - **LifeCycleState** *(string) --* 

              Lifecycle phase of the file system.

              
            

            - **Name** *(string) --* 

              You can add tags to a file system, including a ``Name`` tag. For more information, see  CreateTags . If the file system has a ``Name`` tag, Amazon EFS returns the value in this field. 

              
            

            - **NumberOfMountTargets** *(integer) --* 

              Current number of mount targets that the file system has. For more information, see  CreateMountTarget .

              
            

            - **SizeInBytes** *(dict) --* 

              Latest known metered size (in bytes) of data stored in the file system, in bytes, in its ``Value`` field, and the time at which that size was determined in its ``Timestamp`` field. The ``Timestamp`` value is the integer number of seconds since 1970-01-01T00:00:00Z. Note that the value does not represent the size of a consistent snapshot of the file system, but it is eventually consistent when there are no writes to the file system. That is, the value will represent actual size only if the file system is not modified for a period longer than a couple of hours. Otherwise, the value is not the exact size the file system was at any instant in time. 

              
              

              - **Value** *(integer) --* 

                Latest known metered size (in bytes) of data stored in the file system.

                
              

              - **Timestamp** *(datetime) --* 

                Time at which the size of data, returned in the ``Value`` field, was determined. The value is the integer number of seconds since 1970-01-01T00:00:00Z.

                
          
            

            - **PerformanceMode** *(string) --* 

              The ``PerformanceMode`` of the file system.

              
            

            - **Encrypted** *(boolean) --* 

              A boolean value that, if true, indicates that the file system is encrypted.

              
            

            - **KmsKeyId** *(string) --* 

              The id of an AWS Key Management Service (AWS KMS) customer master key (CMK) that was used to protect the encrypted file system.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: EFS.Paginator.DescribeMountTargets

  ::

    
    paginator = client.get_paginator('describe_mount_targets')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`EFS.Client.describe_mount_targets`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/DescribeMountTargets>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          FileSystemId='string',
          MountTargetId='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type FileSystemId: string
    :param FileSystemId: 

      (Optional) ID of the file system whose mount targets you want to list (String). It must be included in your request if ``MountTargetId`` is not included.

      

    
    :type MountTargetId: string
    :param MountTargetId: 

      (Optional) ID of the mount target that you want to have described (String). It must be included in your request if ``FileSystemId`` is not included.

      

    
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
            'Marker': 'string',
            'MountTargets': [
                {
                    'OwnerId': 'string',
                    'MountTargetId': 'string',
                    'FileSystemId': 'string',
                    'SubnetId': 'string',
                    'LifeCycleState': 'creating'|'available'|'deleting'|'deleted',
                    'IpAddress': 'string',
                    'NetworkInterfaceId': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        

        
        

        - **Marker** *(string) --* 

          If the request included the ``Marker`` , the response returns that value in this field.

          
        

        - **MountTargets** *(list) --* 

          Returns the file system's mount targets as an array of ``MountTargetDescription`` objects.

          
          

          - *(dict) --* 

            Provides a description of a mount target.

            
            

            - **OwnerId** *(string) --* 

              AWS account ID that owns the resource.

              
            

            - **MountTargetId** *(string) --* 

              System-assigned mount target ID.

              
            

            - **FileSystemId** *(string) --* 

              ID of the file system for which the mount target is intended.

              
            

            - **SubnetId** *(string) --* 

              ID of the mount target's subnet.

              
            

            - **LifeCycleState** *(string) --* 

              Lifecycle state of the mount target.

              
            

            - **IpAddress** *(string) --* 

              Address at which the file system may be mounted via the mount target.

              
            

            - **NetworkInterfaceId** *(string) --* 

              ID of the network interface that Amazon EFS created when it created the mount target.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: EFS.Paginator.DescribeTags

  ::

    
    paginator = client.get_paginator('describe_tags')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`EFS.Client.describe_tags`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/DescribeTags>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          FileSystemId='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type FileSystemId: string
    :param FileSystemId: **[REQUIRED]** 

      ID of the file system whose tag set you want to retrieve.

      

    
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
            'Marker': 'string',
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        

        
        

        - **Marker** *(string) --* 

          If the request included a ``Marker`` , the response returns that value in this field.

          
        

        - **Tags** *(list) --* 

          Returns tags associated with the file system as an array of ``Tag`` objects. 

          
          

          - *(dict) --* 

            A tag is a key-value pair. Allowed characters: letters, whitespace, and numbers, representable in UTF-8, and the following characters:``+ - = . _ : /``  

            
            

            - **Key** *(string) --* 

              Tag key (String). The key can't start with ``aws:`` .

              
            

            - **Value** *(string) --* 

              Value of the tag key.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    