

********
OpsWorks
********

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: OpsWorks.Client

  A low-level client representing AWS OpsWorks::

    
    import boto3
    
    client = boto3.client('opsworks')

  
  These are the available methods:
  
  *   :py:meth:`~OpsWorks.Client.assign_instance`

  
  *   :py:meth:`~OpsWorks.Client.assign_volume`

  
  *   :py:meth:`~OpsWorks.Client.associate_elastic_ip`

  
  *   :py:meth:`~OpsWorks.Client.attach_elastic_load_balancer`

  
  *   :py:meth:`~OpsWorks.Client.can_paginate`

  
  *   :py:meth:`~OpsWorks.Client.clone_stack`

  
  *   :py:meth:`~OpsWorks.Client.create_app`

  
  *   :py:meth:`~OpsWorks.Client.create_deployment`

  
  *   :py:meth:`~OpsWorks.Client.create_instance`

  
  *   :py:meth:`~OpsWorks.Client.create_layer`

  
  *   :py:meth:`~OpsWorks.Client.create_stack`

  
  *   :py:meth:`~OpsWorks.Client.create_user_profile`

  
  *   :py:meth:`~OpsWorks.Client.delete_app`

  
  *   :py:meth:`~OpsWorks.Client.delete_instance`

  
  *   :py:meth:`~OpsWorks.Client.delete_layer`

  
  *   :py:meth:`~OpsWorks.Client.delete_stack`

  
  *   :py:meth:`~OpsWorks.Client.delete_user_profile`

  
  *   :py:meth:`~OpsWorks.Client.deregister_ecs_cluster`

  
  *   :py:meth:`~OpsWorks.Client.deregister_elastic_ip`

  
  *   :py:meth:`~OpsWorks.Client.deregister_instance`

  
  *   :py:meth:`~OpsWorks.Client.deregister_rds_db_instance`

  
  *   :py:meth:`~OpsWorks.Client.deregister_volume`

  
  *   :py:meth:`~OpsWorks.Client.describe_agent_versions`

  
  *   :py:meth:`~OpsWorks.Client.describe_apps`

  
  *   :py:meth:`~OpsWorks.Client.describe_commands`

  
  *   :py:meth:`~OpsWorks.Client.describe_deployments`

  
  *   :py:meth:`~OpsWorks.Client.describe_ecs_clusters`

  
  *   :py:meth:`~OpsWorks.Client.describe_elastic_ips`

  
  *   :py:meth:`~OpsWorks.Client.describe_elastic_load_balancers`

  
  *   :py:meth:`~OpsWorks.Client.describe_instances`

  
  *   :py:meth:`~OpsWorks.Client.describe_layers`

  
  *   :py:meth:`~OpsWorks.Client.describe_load_based_auto_scaling`

  
  *   :py:meth:`~OpsWorks.Client.describe_my_user_profile`

  
  *   :py:meth:`~OpsWorks.Client.describe_permissions`

  
  *   :py:meth:`~OpsWorks.Client.describe_raid_arrays`

  
  *   :py:meth:`~OpsWorks.Client.describe_rds_db_instances`

  
  *   :py:meth:`~OpsWorks.Client.describe_service_errors`

  
  *   :py:meth:`~OpsWorks.Client.describe_stack_provisioning_parameters`

  
  *   :py:meth:`~OpsWorks.Client.describe_stack_summary`

  
  *   :py:meth:`~OpsWorks.Client.describe_stacks`

  
  *   :py:meth:`~OpsWorks.Client.describe_time_based_auto_scaling`

  
  *   :py:meth:`~OpsWorks.Client.describe_user_profiles`

  
  *   :py:meth:`~OpsWorks.Client.describe_volumes`

  
  *   :py:meth:`~OpsWorks.Client.detach_elastic_load_balancer`

  
  *   :py:meth:`~OpsWorks.Client.disassociate_elastic_ip`

  
  *   :py:meth:`~OpsWorks.Client.generate_presigned_url`

  
  *   :py:meth:`~OpsWorks.Client.get_hostname_suggestion`

  
  *   :py:meth:`~OpsWorks.Client.get_paginator`

  
  *   :py:meth:`~OpsWorks.Client.get_waiter`

  
  *   :py:meth:`~OpsWorks.Client.grant_access`

  
  *   :py:meth:`~OpsWorks.Client.list_tags`

  
  *   :py:meth:`~OpsWorks.Client.reboot_instance`

  
  *   :py:meth:`~OpsWorks.Client.register_ecs_cluster`

  
  *   :py:meth:`~OpsWorks.Client.register_elastic_ip`

  
  *   :py:meth:`~OpsWorks.Client.register_instance`

  
  *   :py:meth:`~OpsWorks.Client.register_rds_db_instance`

  
  *   :py:meth:`~OpsWorks.Client.register_volume`

  
  *   :py:meth:`~OpsWorks.Client.set_load_based_auto_scaling`

  
  *   :py:meth:`~OpsWorks.Client.set_permission`

  
  *   :py:meth:`~OpsWorks.Client.set_time_based_auto_scaling`

  
  *   :py:meth:`~OpsWorks.Client.start_instance`

  
  *   :py:meth:`~OpsWorks.Client.start_stack`

  
  *   :py:meth:`~OpsWorks.Client.stop_instance`

  
  *   :py:meth:`~OpsWorks.Client.stop_stack`

  
  *   :py:meth:`~OpsWorks.Client.tag_resource`

  
  *   :py:meth:`~OpsWorks.Client.unassign_instance`

  
  *   :py:meth:`~OpsWorks.Client.unassign_volume`

  
  *   :py:meth:`~OpsWorks.Client.untag_resource`

  
  *   :py:meth:`~OpsWorks.Client.update_app`

  
  *   :py:meth:`~OpsWorks.Client.update_elastic_ip`

  
  *   :py:meth:`~OpsWorks.Client.update_instance`

  
  *   :py:meth:`~OpsWorks.Client.update_layer`

  
  *   :py:meth:`~OpsWorks.Client.update_my_user_profile`

  
  *   :py:meth:`~OpsWorks.Client.update_rds_db_instance`

  
  *   :py:meth:`~OpsWorks.Client.update_stack`

  
  *   :py:meth:`~OpsWorks.Client.update_user_profile`

  
  *   :py:meth:`~OpsWorks.Client.update_volume`

  

  .. py:method:: assign_instance(**kwargs)

    

    Assign a registered instance to a layer.

     

     
    * You can assign registered on-premises instances to any layer type. 
     
    * You can assign registered Amazon EC2 instances only to custom layers. 
     
    * You cannot use this action with instances that were created with AWS OpsWorks Stacks. 
     

     

     **Required Permissions** : To use this action, an AWS Identity and Access Management (IAM) user must have a Manage permissions level for the stack or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/AssignInstance>`_    


    **Request Syntax** 
    ::

      response = client.assign_instance(
          InstanceId='string',
          LayerIds=[
              'string',
          ]
      )
    :type InstanceId: string
    :param InstanceId: **[REQUIRED]** 

      The instance ID.

      

    
    :type LayerIds: list
    :param LayerIds: **[REQUIRED]** 

      The layer ID, which must correspond to a custom layer. You cannot assign a registered instance to a built-in layer.

      

    
      - *(string) --* 

      
  
    
    :returns: None

  .. py:method:: assign_volume(**kwargs)

    

    Assigns one of the stack's registered Amazon EBS volumes to a specified instance. The volume must first be registered with the stack by calling  RegisterVolume . After you register the volume, you must call  UpdateVolume to specify a mount point before calling ``AssignVolume`` . For more information, see `Resource Management <http://docs.aws.amazon.com/opsworks/latest/userguide/resources.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/AssignVolume>`_    


    **Request Syntax** 
    ::

      response = client.assign_volume(
          VolumeId='string',
          InstanceId='string'
      )
    :type VolumeId: string
    :param VolumeId: **[REQUIRED]** 

      The volume ID.

      

    
    :type InstanceId: string
    :param InstanceId: 

      The instance ID.

      

    
    
    :returns: None

  .. py:method:: associate_elastic_ip(**kwargs)

    

    Associates one of the stack's registered Elastic IP addresses with a specified instance. The address must first be registered with the stack by calling  RegisterElasticIp . For more information, see `Resource Management <http://docs.aws.amazon.com/opsworks/latest/userguide/resources.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/AssociateElasticIp>`_    


    **Request Syntax** 
    ::

      response = client.associate_elastic_ip(
          ElasticIp='string',
          InstanceId='string'
      )
    :type ElasticIp: string
    :param ElasticIp: **[REQUIRED]** 

      The Elastic IP address.

      

    
    :type InstanceId: string
    :param InstanceId: 

      The instance ID.

      

    
    
    :returns: None

  .. py:method:: attach_elastic_load_balancer(**kwargs)

    

    Attaches an Elastic Load Balancing load balancer to a specified layer. AWS OpsWorks Stacks does not support Application Load Balancer. You can only use Classic Load Balancer with AWS OpsWorks Stacks. For more information, see `Elastic Load Balancing <http://docs.aws.amazon.com/opsworks/latest/userguide/layers-elb.html>`__ .

     

    .. note::

       

      You must create the Elastic Load Balancing instance separately, by using the Elastic Load Balancing console, API, or CLI. For more information, see `Elastic Load Balancing Developer Guide <http://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/Welcome.html>`__ .

       

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/AttachElasticLoadBalancer>`_    


    **Request Syntax** 
    ::

      response = client.attach_elastic_load_balancer(
          ElasticLoadBalancerName='string',
          LayerId='string'
      )
    :type ElasticLoadBalancerName: string
    :param ElasticLoadBalancerName: **[REQUIRED]** 

      The Elastic Load Balancing instance's name.

      

    
    :type LayerId: string
    :param LayerId: **[REQUIRED]** 

      The ID of the layer that the Elastic Load Balancing instance is to be attached to.

      

    
    
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


  .. py:method:: clone_stack(**kwargs)

    

    Creates a clone of a specified stack. For more information, see `Clone a Stack <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-cloning.html>`__ . By default, all parameters are set to the values used by the parent stack.

     

     **Required Permissions** : To use this action, an IAM user must have an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/CloneStack>`_    


    **Request Syntax** 
    ::

      response = client.clone_stack(
          SourceStackId='string',
          Name='string',
          Region='string',
          VpcId='string',
          Attributes={
              'string': 'string'
          },
          ServiceRoleArn='string',
          DefaultInstanceProfileArn='string',
          DefaultOs='string',
          HostnameTheme='string',
          DefaultAvailabilityZone='string',
          DefaultSubnetId='string',
          CustomJson='string',
          ConfigurationManager={
              'Name': 'string',
              'Version': 'string'
          },
          ChefConfiguration={
              'ManageBerkshelf': True|False,
              'BerkshelfVersion': 'string'
          },
          UseCustomCookbooks=True|False,
          UseOpsworksSecurityGroups=True|False,
          CustomCookbooksSource={
              'Type': 'git'|'svn'|'archive'|'s3',
              'Url': 'string',
              'Username': 'string',
              'Password': 'string',
              'SshKey': 'string',
              'Revision': 'string'
          },
          DefaultSshKeyName='string',
          ClonePermissions=True|False,
          CloneAppIds=[
              'string',
          ],
          DefaultRootDeviceType='ebs'|'instance-store',
          AgentVersion='string'
      )
    :type SourceStackId: string
    :param SourceStackId: **[REQUIRED]** 

      The source stack ID.

      

    
    :type Name: string
    :param Name: 

      The cloned stack name.

      

    
    :type Region: string
    :param Region: 

      The cloned stack AWS region, such as "ap-northeast-2". For more information about AWS regions, see `Regions and Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html>`__ .

      

    
    :type VpcId: string
    :param VpcId: 

      The ID of the VPC that the cloned stack is to be launched into. It must be in the specified region. All instances are launched into this VPC, and you cannot change the ID later.

       

       
      * If your account supports EC2 Classic, the default value is no VPC. 
       
      * If your account does not support EC2 Classic, the default value is the default VPC for the specified region. 
       

       

      If the VPC ID corresponds to a default VPC and you have specified either the ``DefaultAvailabilityZone`` or the ``DefaultSubnetId`` parameter only, AWS OpsWorks Stacks infers the value of the other parameter. If you specify neither parameter, AWS OpsWorks Stacks sets these parameters to the first valid Availability Zone for the specified region and the corresponding default VPC subnet ID, respectively. 

       

      If you specify a nondefault VPC ID, note the following:

       

       
      * It must belong to a VPC in your account that is in the specified region. 
       
      * You must specify a value for ``DefaultSubnetId`` . 
       

       

      For more information on how to use AWS OpsWorks Stacks with a VPC, see `Running a Stack in a VPC <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-vpc.html>`__ . For more information on default VPC and EC2 Classic, see `Supported Platforms <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-platforms.html>`__ . 

      

    
    :type Attributes: dict
    :param Attributes: 

      A list of stack attributes and values as key/value pairs to be added to the cloned stack.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type ServiceRoleArn: string
    :param ServiceRoleArn: **[REQUIRED]** 

      The stack AWS Identity and Access Management (IAM) role, which allows AWS OpsWorks Stacks to work with AWS resources on your behalf. You must set this parameter to the Amazon Resource Name (ARN) for an existing IAM role. If you create a stack by using the AWS OpsWorks Stacks console, it creates the role for you. You can obtain an existing stack's IAM ARN programmatically by calling  DescribePermissions . For more information about IAM ARNs, see `Using Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ .

       

      .. note::

         

        You must set this parameter to a valid service role ARN or the action will fail; there is no default value. You can specify the source stack's service role ARN, if you prefer, but you must do so explicitly.

         

      

    
    :type DefaultInstanceProfileArn: string
    :param DefaultInstanceProfileArn: 

      The Amazon Resource Name (ARN) of an IAM profile that is the default profile for all of the stack's EC2 instances. For more information about IAM ARNs, see `Using Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ .

      

    
    :type DefaultOs: string
    :param DefaultOs: 

      The stack's operating system, which must be set to one of the following.

       

       
      * A supported Linux operating system: An Amazon Linux version, such as ``Amazon Linux 2017.03`` , ``Amazon Linux 2016.09`` , ``Amazon Linux 2016.03`` , ``Amazon Linux 2015.09`` , or ``Amazon Linux 2015.03`` . 
       
      * A supported Ubuntu operating system, such as ``Ubuntu 16.04 LTS`` , ``Ubuntu 14.04 LTS`` , or ``Ubuntu 12.04 LTS`` . 
       
      * ``CentOS Linux 7``   
       
      * ``Red Hat Enterprise Linux 7``   
       
      * ``Microsoft Windows Server 2012 R2 Base`` , ``Microsoft Windows Server 2012 R2 with SQL Server Express`` , ``Microsoft Windows Server 2012 R2 with SQL Server Standard`` , or ``Microsoft Windows Server 2012 R2 with SQL Server Web`` . 
       
      * A custom AMI: ``Custom`` . You specify the custom AMI you want to use when you create instances. For more information on how to use custom AMIs with OpsWorks, see `Using Custom AMIs <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-custom-ami.html>`__ . 
       

       

      The default option is the parent stack's operating system. For more information on the supported operating systems, see `AWS OpsWorks Stacks Operating Systems <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-os.html>`__ .

       

      .. note::

         

        You can specify a different Linux operating system for the cloned stack, but you cannot change from Linux to Windows or Windows to Linux.

         

      

    
    :type HostnameTheme: string
    :param HostnameTheme: 

      The stack's host name theme, with spaces are replaced by underscores. The theme is used to generate host names for the stack's instances. By default, ``HostnameTheme`` is set to ``Layer_Dependent`` , which creates host names by appending integers to the layer's short name. The other themes are:

       

       
      * ``Baked_Goods``   
       
      * ``Clouds``   
       
      * ``Europe_Cities``   
       
      * ``Fruits``   
       
      * ``Greek_Deities``   
       
      * ``Legendary_creatures_from_Japan``   
       
      * ``Planets_and_Moons``   
       
      * ``Roman_Deities``   
       
      * ``Scottish_Islands``   
       
      * ``US_Cities``   
       
      * ``Wild_Cats``   
       

       

      To obtain a generated host name, call ``GetHostNameSuggestion`` , which returns a host name based on the current theme.

      

    
    :type DefaultAvailabilityZone: string
    :param DefaultAvailabilityZone: 

      The cloned stack's default Availability Zone, which must be in the specified region. For more information, see `Regions and Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html>`__ . If you also specify a value for ``DefaultSubnetId`` , the subnet must be in the same zone. For more information, see the ``VpcId`` parameter description. 

      

    
    :type DefaultSubnetId: string
    :param DefaultSubnetId: 

      The stack's default VPC subnet ID. This parameter is required if you specify a value for the ``VpcId`` parameter. All instances are launched into this subnet unless you specify otherwise when you create the instance. If you also specify a value for ``DefaultAvailabilityZone`` , the subnet must be in that zone. For information on default values and when this parameter is required, see the ``VpcId`` parameter description. 

      

    
    :type CustomJson: string
    :param CustomJson: 

      A string that contains user-defined, custom JSON. It is used to override the corresponding default stack configuration JSON values. The string should be in the following format:

       

       ``"{\"key1\": \"value1\", \"key2\": \"value2\",...}"``  

       

      For more information on custom JSON, see `Use Custom JSON to Modify the Stack Configuration Attributes <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-json.html>`__  

      

    
    :type ConfigurationManager: dict
    :param ConfigurationManager: 

      The configuration manager. When you clone a stack we recommend that you use the configuration manager to specify the Chef version: 12, 11.10, or 11.4 for Linux stacks, or 12.2 for Windows stacks. The default value for Linux stacks is currently 12.

      

    
      - **Name** *(string) --* 

        The name. This parameter must be set to "Chef".

        

      
      - **Version** *(string) --* 

        The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to 12.2 for Windows stacks. The default value for Linux stacks is 11.4.

        

      
    
    :type ChefConfiguration: dict
    :param ChefConfiguration: 

      A ``ChefConfiguration`` object that specifies whether to enable Berkshelf and the Berkshelf version on Chef 11.10 stacks. For more information, see `Create a New Stack <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`__ .

      

    
      - **ManageBerkshelf** *(boolean) --* 

        Whether to enable Berkshelf.

        

      
      - **BerkshelfVersion** *(string) --* 

        The Berkshelf version.

        

      
    
    :type UseCustomCookbooks: boolean
    :param UseCustomCookbooks: 

      Whether to use custom cookbooks.

      

    
    :type UseOpsworksSecurityGroups: boolean
    :param UseOpsworksSecurityGroups: 

      Whether to associate the AWS OpsWorks Stacks built-in security groups with the stack's layers.

       

      AWS OpsWorks Stacks provides a standard set of built-in security groups, one for each layer, which are associated with layers by default. With ``UseOpsworksSecurityGroups`` you can instead provide your own custom security groups. ``UseOpsworksSecurityGroups`` has the following settings: 

       

       
      * True - AWS OpsWorks Stacks automatically associates the appropriate built-in security group with each layer (default setting). You can associate additional security groups with a layer after you create it but you cannot delete the built-in security group. 
       
      * False - AWS OpsWorks Stacks does not associate built-in security groups with layers. You must create appropriate Amazon Elastic Compute Cloud (Amazon EC2) security groups and associate a security group with each layer that you create. However, you can still manually associate a built-in security group with a layer on creation; custom security groups are required only for those layers that need custom settings. 
       

       

      For more information, see `Create a New Stack <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`__ .

      

    
    :type CustomCookbooksSource: dict
    :param CustomCookbooksSource: 

      Contains the information required to retrieve an app or cookbook from a repository. For more information, see `Creating Apps <http://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html>`__ or `Custom Recipes and Cookbooks <http://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html>`__ .

      

    
      - **Type** *(string) --* 

        The repository type.

        

      
      - **Url** *(string) --* 

        The source URL. The following is an example of an Amazon S3 source URL: ``https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz`` .

        

      
      - **Username** *(string) --* 

        This parameter depends on the repository type.

         

         
        * For Amazon S3 bundles, set ``Username`` to the appropriate IAM access key ID. 
         
        * For HTTP bundles, Git repositories, and Subversion repositories, set ``Username`` to the user name. 
         

        

      
      - **Password** *(string) --* 

        When included in a request, the parameter depends on the repository type.

         

         
        * For Amazon S3 bundles, set ``Password`` to the appropriate IAM secret access key. 
         
        * For HTTP bundles and Subversion repositories, set ``Password`` to the password. 
         

         

        For more information on how to safely handle IAM credentials, see `http\://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html <http://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html>`__ .

         

        In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

        

      
      - **SshKey** *(string) --* 

        In requests, the repository's SSH key.

         

        In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

        

      
      - **Revision** *(string) --* 

        The application's version. AWS OpsWorks Stacks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.

        

      
    
    :type DefaultSshKeyName: string
    :param DefaultSshKeyName: 

      A default Amazon EC2 key pair name. The default value is none. If you specify a key pair name, AWS OpsWorks installs the public key on the instance and you can use the private key with an SSH client to log in to the instance. For more information, see `Using SSH to Communicate with an Instance <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-ssh.html>`__ and `Managing SSH Access <http://docs.aws.amazon.com/opsworks/latest/userguide/security-ssh-access.html>`__ . You can override this setting by specifying a different key pair, or no key pair, when you `create an instance <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-add.html>`__ . 

      

    
    :type ClonePermissions: boolean
    :param ClonePermissions: 

      Whether to clone the source stack's permissions.

      

    
    :type CloneAppIds: list
    :param CloneAppIds: 

      A list of source stack app IDs to be included in the cloned stack.

      

    
      - *(string) --* 

      
  
    :type DefaultRootDeviceType: string
    :param DefaultRootDeviceType: 

      The default root device type. This value is used by default for all instances in the cloned stack, but you can override it when you create an instance. For more information, see `Storage for the Root Device <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-for-the-root-device>`__ .

      

    
    :type AgentVersion: string
    :param AgentVersion: 

      The default AWS OpsWorks Stacks agent version. You have the following options:

       

       
      * Auto-update - Set this parameter to ``LATEST`` . AWS OpsWorks Stacks automatically installs new agent versions on the stack's instances as soon as they are available. 
       
      * Fixed version - Set this parameter to your preferred agent version. To update the agent version, you must edit the stack configuration and specify a new version. AWS OpsWorks Stacks then automatically installs that version on the stack's instances. 
       

       

      The default setting is ``LATEST`` . To specify an agent version, you must use the complete version number, not the abbreviated number shown on the console. For a list of available agent version numbers, call  DescribeAgentVersions . AgentVersion cannot be set to Chef 12.2.

       

      .. note::

         

        You can also specify an agent version when you create or update an instance, which overrides the stack's default setting.

         

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'StackId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``CloneStack`` request.

        
        

        - **StackId** *(string) --* 

          The cloned stack ID.

          
    

  .. py:method:: create_app(**kwargs)

    

    Creates an app for a specified stack. For more information, see `Creating Apps <http://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/CreateApp>`_    


    **Request Syntax** 
    ::

      response = client.create_app(
          StackId='string',
          Shortname='string',
          Name='string',
          Description='string',
          DataSources=[
              {
                  'Type': 'string',
                  'Arn': 'string',
                  'DatabaseName': 'string'
              },
          ],
          Type='aws-flow-ruby'|'java'|'rails'|'php'|'nodejs'|'static'|'other',
          AppSource={
              'Type': 'git'|'svn'|'archive'|'s3',
              'Url': 'string',
              'Username': 'string',
              'Password': 'string',
              'SshKey': 'string',
              'Revision': 'string'
          },
          Domains=[
              'string',
          ],
          EnableSsl=True|False,
          SslConfiguration={
              'Certificate': 'string',
              'PrivateKey': 'string',
              'Chain': 'string'
          },
          Attributes={
              'string': 'string'
          },
          Environment=[
              {
                  'Key': 'string',
                  'Value': 'string',
                  'Secure': True|False
              },
          ]
      )
    :type StackId: string
    :param StackId: **[REQUIRED]** 

      The stack ID.

      

    
    :type Shortname: string
    :param Shortname: 

      The app's short name.

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      The app name.

      

    
    :type Description: string
    :param Description: 

      A description of the app.

      

    
    :type DataSources: list
    :param DataSources: 

      The app's data source.

      

    
      - *(dict) --* 

        Describes an app's data source.

        

      
        - **Type** *(string) --* 

          The data source's type, ``AutoSelectOpsworksMysqlInstance`` , ``OpsworksMysqlInstance`` , or ``RdsDbInstance`` .

          

        
        - **Arn** *(string) --* 

          The data source's ARN.

          

        
        - **DatabaseName** *(string) --* 

          The database name.

          

        
      
  
    :type Type: string
    :param Type: **[REQUIRED]** 

      The app type. Each supported type is associated with a particular layer. For example, PHP applications are associated with a PHP layer. AWS OpsWorks Stacks deploys an application to those instances that are members of the corresponding layer. If your app isn't one of the standard types, or you prefer to implement your own Deploy recipes, specify ``other`` .

      

    
    :type AppSource: dict
    :param AppSource: 

      A ``Source`` object that specifies the app repository.

      

    
      - **Type** *(string) --* 

        The repository type.

        

      
      - **Url** *(string) --* 

        The source URL. The following is an example of an Amazon S3 source URL: ``https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz`` .

        

      
      - **Username** *(string) --* 

        This parameter depends on the repository type.

         

         
        * For Amazon S3 bundles, set ``Username`` to the appropriate IAM access key ID. 
         
        * For HTTP bundles, Git repositories, and Subversion repositories, set ``Username`` to the user name. 
         

        

      
      - **Password** *(string) --* 

        When included in a request, the parameter depends on the repository type.

         

         
        * For Amazon S3 bundles, set ``Password`` to the appropriate IAM secret access key. 
         
        * For HTTP bundles and Subversion repositories, set ``Password`` to the password. 
         

         

        For more information on how to safely handle IAM credentials, see `http\://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html <http://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html>`__ .

         

        In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

        

      
      - **SshKey** *(string) --* 

        In requests, the repository's SSH key.

         

        In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

        

      
      - **Revision** *(string) --* 

        The application's version. AWS OpsWorks Stacks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.

        

      
    
    :type Domains: list
    :param Domains: 

      The app virtual host settings, with multiple domains separated by commas. For example: ``'www.example.com, example.com'``  

      

    
      - *(string) --* 

      
  
    :type EnableSsl: boolean
    :param EnableSsl: 

      Whether to enable SSL for the app.

      

    
    :type SslConfiguration: dict
    :param SslConfiguration: 

      An ``SslConfiguration`` object with the SSL configuration.

      

    
      - **Certificate** *(string) --* **[REQUIRED]** 

        The contents of the certificate's domain.crt file.

        

      
      - **PrivateKey** *(string) --* **[REQUIRED]** 

        The private key; the contents of the certificate's domain.kex file.

        

      
      - **Chain** *(string) --* 

        Optional. Can be used to specify an intermediate certificate authority key or client authentication.

        

      
    
    :type Attributes: dict
    :param Attributes: 

      One or more user-defined key/value pairs to be added to the stack attributes.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type Environment: list
    :param Environment: 

      An array of ``EnvironmentVariable`` objects that specify environment variables to be associated with the app. After you deploy the app, these variables are defined on the associated app server instance. For more information, see `Environment Variables <http://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html#workingapps-creating-environment>`__ .

       

      There is no specific limit on the number of environment variables. However, the size of the associated data structure - which includes the variables' names, values, and protected flag values - cannot exceed 10 KB (10240 Bytes). This limit should accommodate most if not all use cases. Exceeding it will cause an exception with the message, "Environment: is too large (maximum is 10KB)."

       

      .. note::

         

        This parameter is supported only by Chef 11.10 stacks. If you have specified one or more environment variables, you cannot modify the stack's Chef version.

         

      

    
      - *(dict) --* 

        Represents an app's environment variable.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          (Required) The environment variable's name, which can consist of up to 64 characters and must be specified. The name can contain upper- and lowercase letters, numbers, and underscores (_), but it must start with a letter or underscore.

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          (Optional) The environment variable's value, which can be left empty. If you specify a value, it can contain up to 256 characters, which must all be printable.

          

        
        - **Secure** *(boolean) --* 

          (Optional) Whether the variable's value will be returned by the  DescribeApps action. To conceal an environment variable's value, set ``Secure`` to ``true`` . ``DescribeApps`` then returns ``*****FILTERED*****`` instead of the actual value. The default value for ``Secure`` is ``false`` . 

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AppId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``CreateApp`` request.

        
        

        - **AppId** *(string) --* 

          The app ID.

          
    

  .. py:method:: create_deployment(**kwargs)

    

    Runs deployment or stack commands. For more information, see `Deploying Apps <http://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-deploying.html>`__ and `Run Stack Commands <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-commands.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have a Deploy or Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/CreateDeployment>`_    


    **Request Syntax** 
    ::

      response = client.create_deployment(
          StackId='string',
          AppId='string',
          InstanceIds=[
              'string',
          ],
          LayerIds=[
              'string',
          ],
          Command={
              'Name': 'install_dependencies'|'update_dependencies'|'update_custom_cookbooks'|'execute_recipes'|'configure'|'setup'|'deploy'|'rollback'|'start'|'stop'|'restart'|'undeploy',
              'Args': {
                  'string': [
                      'string',
                  ]
              }
          },
          Comment='string',
          CustomJson='string'
      )
    :type StackId: string
    :param StackId: **[REQUIRED]** 

      The stack ID.

      

    
    :type AppId: string
    :param AppId: 

      The app ID. This parameter is required for app deployments, but not for other deployment commands.

      

    
    :type InstanceIds: list
    :param InstanceIds: 

      The instance IDs for the deployment targets.

      

    
      - *(string) --* 

      
  
    :type LayerIds: list
    :param LayerIds: 

      The layer IDs for the deployment targets.

      

    
      - *(string) --* 

      
  
    :type Command: dict
    :param Command: **[REQUIRED]** 

      A ``DeploymentCommand`` object that specifies the deployment command and any associated arguments.

      

    
      - **Name** *(string) --* **[REQUIRED]** 

        Specifies the operation. You can specify only one command.

         

        For stacks, the following commands are available:

         

         
        * ``execute_recipes`` : Execute one or more recipes. To specify the recipes, set an ``Args`` parameter named ``recipes`` to the list of recipes to be executed. For example, to execute ``phpapp::appsetup`` , set ``Args`` to ``{"recipes":["phpapp::appsetup"]}`` . 
         
        * ``install_dependencies`` : Install the stack's dependencies. 
         
        * ``update_custom_cookbooks`` : Update the stack's custom cookbooks. 
         
        * ``update_dependencies`` : Update the stack's dependencies. 
         

         

        .. note::

           

          The update_dependencies and install_dependencies commands are supported only for Linux instances. You can run the commands successfully on Windows instances, but they do nothing.

           

         

        For apps, the following commands are available:

         

         
        * ``deploy`` : Deploy an app. Ruby on Rails apps have an optional ``Args`` parameter named ``migrate`` . Set ``Args`` to {"migrate":["true"]} to migrate the database. The default setting is {"migrate":["false"]}. 
         
        * ``rollback`` Roll the app back to the previous version. When you update an app, AWS OpsWorks Stacks stores the previous version, up to a maximum of five versions. You can use this command to roll an app back as many as four versions. 
         
        * ``start`` : Start the app's web or application server. 
         
        * ``stop`` : Stop the app's web or application server. 
         
        * ``restart`` : Restart the app's web or application server. 
         
        * ``undeploy`` : Undeploy the app. 
         

        

      
      - **Args** *(dict) --* 

        The arguments of those commands that take arguments. It should be set to a JSON object with the following format:

         

         ``{"arg_name1" : ["value1", "value2", ...], "arg_name2" : ["value1", "value2", ...], ...}``  

         

        The ``update_dependencies`` command takes two arguments:

         

         
        * ``upgrade_os_to`` - Specifies the desired Amazon Linux version for instances whose OS you want to upgrade, such as ``Amazon Linux 2016.09`` . You must also set the ``allow_reboot`` argument to true. 
         
        * ``allow_reboot`` - Specifies whether to allow AWS OpsWorks Stacks to reboot the instances if necessary, after installing the updates. This argument can be set to either ``true`` or ``false`` . The default value is ``false`` . 
         

         

        For example, to upgrade an instance to Amazon Linux 2016.09, set ``Args`` to the following.

         

         ``{ "upgrade_os_to":["Amazon Linux 2016.09"], "allow_reboot":["true"] }``  

        

      
        - *(string) --* 

        
          - *(list) --* 

          
            - *(string) --* 

            
        
    
  
    
    :type Comment: string
    :param Comment: 

      A user-defined comment.

      

    
    :type CustomJson: string
    :param CustomJson: 

      A string that contains user-defined, custom JSON. It is used to override the corresponding default stack configuration JSON values. The string should be in the following format:

       

       ``"{\"key1\": \"value1\", \"key2\": \"value2\",...}"``  

       

      For more information on custom JSON, see `Use Custom JSON to Modify the Stack Configuration Attributes <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-json.html>`__ .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DeploymentId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``CreateDeployment`` request.

        
        

        - **DeploymentId** *(string) --* 

          The deployment ID, which can be used with other requests to identify the deployment.

          
    

  .. py:method:: create_instance(**kwargs)

    

    Creates an instance in a specified stack. For more information, see `Adding an Instance to a Layer <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-add.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/CreateInstance>`_    


    **Request Syntax** 
    ::

      response = client.create_instance(
          StackId='string',
          LayerIds=[
              'string',
          ],
          InstanceType='string',
          AutoScalingType='load'|'timer',
          Hostname='string',
          Os='string',
          AmiId='string',
          SshKeyName='string',
          AvailabilityZone='string',
          VirtualizationType='string',
          SubnetId='string',
          Architecture='x86_64'|'i386',
          RootDeviceType='ebs'|'instance-store',
          BlockDeviceMappings=[
              {
                  'DeviceName': 'string',
                  'NoDevice': 'string',
                  'VirtualName': 'string',
                  'Ebs': {
                      'SnapshotId': 'string',
                      'Iops': 123,
                      'VolumeSize': 123,
                      'VolumeType': 'gp2'|'io1'|'standard',
                      'DeleteOnTermination': True|False
                  }
              },
          ],
          InstallUpdatesOnBoot=True|False,
          EbsOptimized=True|False,
          AgentVersion='string',
          Tenancy='string'
      )
    :type StackId: string
    :param StackId: **[REQUIRED]** 

      The stack ID.

      

    
    :type LayerIds: list
    :param LayerIds: **[REQUIRED]** 

      An array that contains the instance's layer IDs.

      

    
      - *(string) --* 

      
  
    :type InstanceType: string
    :param InstanceType: **[REQUIRED]** 

      The instance type, such as ``t2.micro`` . For a list of supported instance types, open the stack in the console, choose **Instances** , and choose **+ Instance** . The **Size** list contains the currently supported types. For more information, see `Instance Families and Types <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html>`__ . The parameter values that you use to specify the various types are in the **API Name** column of the **Available Instance Types** table.

      

    
    :type AutoScalingType: string
    :param AutoScalingType: 

      For load-based or time-based instances, the type. Windows stacks can use only time-based instances.

      

    
    :type Hostname: string
    :param Hostname: 

      The instance host name.

      

    
    :type Os: string
    :param Os: 

      The instance's operating system, which must be set to one of the following.

       

       
      * A supported Linux operating system: An Amazon Linux version, such as ``Amazon Linux 2017.03`` , ``Amazon Linux 2016.09`` , ``Amazon Linux 2016.03`` , ``Amazon Linux 2015.09`` , or ``Amazon Linux 2015.03`` . 
       
      * A supported Ubuntu operating system, such as ``Ubuntu 16.04 LTS`` , ``Ubuntu 14.04 LTS`` , or ``Ubuntu 12.04 LTS`` . 
       
      * ``CentOS Linux 7``   
       
      * ``Red Hat Enterprise Linux 7``   
       
      * A supported Windows operating system, such as ``Microsoft Windows Server 2012 R2 Base`` , ``Microsoft Windows Server 2012 R2 with SQL Server Express`` , ``Microsoft Windows Server 2012 R2 with SQL Server Standard`` , or ``Microsoft Windows Server 2012 R2 with SQL Server Web`` . 
       
      * A custom AMI: ``Custom`` . 
       

       

      For more information on the supported operating systems, see `AWS OpsWorks Stacks Operating Systems <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-os.html>`__ .

       

      The default option is the current Amazon Linux version. If you set this parameter to ``Custom`` , you must use the  CreateInstance action's AmiId parameter to specify the custom AMI that you want to use. Block device mappings are not supported if the value is ``Custom`` . For more information on the supported operating systems, see `Operating Systems <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-os.html>`__ For more information on how to use custom AMIs with AWS OpsWorks Stacks, see `Using Custom AMIs <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-custom-ami.html>`__ .

      

    
    :type AmiId: string
    :param AmiId: 

      A custom AMI ID to be used to create the instance. The AMI should be based on one of the supported operating systems. For more information, see `Using Custom AMIs <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-custom-ami.html>`__ .

       

      .. note::

         

        If you specify a custom AMI, you must set ``Os`` to ``Custom`` .

         

      

    
    :type SshKeyName: string
    :param SshKeyName: 

      The instance's Amazon EC2 key-pair name.

      

    
    :type AvailabilityZone: string
    :param AvailabilityZone: 

      The instance Availability Zone. For more information, see `Regions and Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html>`__ .

      

    
    :type VirtualizationType: string
    :param VirtualizationType: 

      The instance's virtualization type, ``paravirtual`` or ``hvm`` .

      

    
    :type SubnetId: string
    :param SubnetId: 

      The ID of the instance's subnet. If the stack is running in a VPC, you can use this parameter to override the stack's default subnet ID value and direct AWS OpsWorks Stacks to launch the instance in a different subnet.

      

    
    :type Architecture: string
    :param Architecture: 

      The instance architecture. The default option is ``x86_64`` . Instance types do not necessarily support both architectures. For a list of the architectures that are supported by the different instance types, see `Instance Families and Types <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html>`__ .

      

    
    :type RootDeviceType: string
    :param RootDeviceType: 

      The instance root device type. For more information, see `Storage for the Root Device <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-for-the-root-device>`__ .

      

    
    :type BlockDeviceMappings: list
    :param BlockDeviceMappings: 

      An array of ``BlockDeviceMapping`` objects that specify the instance's block devices. For more information, see `Block Device Mapping <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html>`__ . Note that block device mappings are not supported for custom AMIs.

      

    
      - *(dict) --* 

        Describes a block device mapping. This data type maps directly to the Amazon EC2 `BlockDeviceMapping <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BlockDeviceMapping.html>`__ data type. 

        

      
        - **DeviceName** *(string) --* 

          The device name that is exposed to the instance, such as ``/dev/sdh`` . For the root device, you can use the explicit device name or you can set this parameter to ``ROOT_DEVICE`` and AWS OpsWorks Stacks will provide the correct device name.

          

        
        - **NoDevice** *(string) --* 

          Suppresses the specified device included in the AMI's block device mapping.

          

        
        - **VirtualName** *(string) --* 

          The virtual device name. For more information, see `BlockDeviceMapping <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BlockDeviceMapping.html>`__ .

          

        
        - **Ebs** *(dict) --* 

          An ``EBSBlockDevice`` that defines how to configure an Amazon EBS volume when the instance is launched.

          

        
          - **SnapshotId** *(string) --* 

            The snapshot ID.

            

          
          - **Iops** *(integer) --* 

            The number of I/O operations per second (IOPS) that the volume supports. For more information, see `EbsBlockDevice <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EbsBlockDevice.html>`__ .

            

          
          - **VolumeSize** *(integer) --* 

            The volume size, in GiB. For more information, see `EbsBlockDevice <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EbsBlockDevice.html>`__ .

            

          
          - **VolumeType** *(string) --* 

            The volume type. ``gp2`` for General Purpose (SSD) volumes, ``io1`` for Provisioned IOPS (SSD) volumes, and ``standard`` for Magnetic volumes.

            

          
          - **DeleteOnTermination** *(boolean) --* 

            Whether the volume is deleted on instance termination.

            

          
        
      
  
    :type InstallUpdatesOnBoot: boolean
    :param InstallUpdatesOnBoot: 

      Whether to install operating system and package updates when the instance boots. The default value is ``true`` . To control when updates are installed, set this value to ``false`` . You must then update your instances manually by using  CreateDeployment to run the ``update_dependencies`` stack command or by manually running ``yum`` (Amazon Linux) or ``apt-get`` (Ubuntu) on the instances. 

       

      .. note::

         

        We strongly recommend using the default value of ``true`` to ensure that your instances have the latest security updates.

         

      

    
    :type EbsOptimized: boolean
    :param EbsOptimized: 

      Whether to create an Amazon EBS-optimized instance.

      

    
    :type AgentVersion: string
    :param AgentVersion: 

      The default AWS OpsWorks Stacks agent version. You have the following options:

       

       
      * ``INHERIT`` - Use the stack's default agent version setting. 
       
      * *version_number* - Use the specified agent version. This value overrides the stack's default setting. To update the agent version, edit the instance configuration and specify a new version. AWS OpsWorks Stacks then automatically installs that version on the instance. 
       

       

      The default setting is ``INHERIT`` . To specify an agent version, you must use the complete version number, not the abbreviated number shown on the console. For a list of available agent version numbers, call  DescribeAgentVersions . AgentVersion cannot be set to Chef 12.2.

      

    
    :type Tenancy: string
    :param Tenancy: 

      The instance's tenancy option. The default option is no tenancy, or if the instance is running in a VPC, inherit tenancy settings from the VPC. The following are valid values for this parameter: ``dedicated`` , ``default`` , or ``host`` . Because there are costs associated with changes in tenancy options, we recommend that you research tenancy options before choosing them for your instances. For more information about dedicated hosts, see `Dedicated Hosts Overview <http://aws.amazon.com/ec2/dedicated-hosts/>`__ and `Amazon EC2 Dedicated Hosts <http://aws.amazon.com/ec2/dedicated-hosts/>`__ . For more information about dedicated instances, see `Dedicated Instances <http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/dedicated-instance.html>`__ and `Amazon EC2 Dedicated Instances <http://aws.amazon.com/ec2/purchasing-options/dedicated-instances/>`__ .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'InstanceId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``CreateInstance`` request.

        
        

        - **InstanceId** *(string) --* 

          The instance ID.

          
    

  .. py:method:: create_layer(**kwargs)

    

    Creates a layer. For more information, see `How to Create a Layer <http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-create.html>`__ .

     

    .. note::

       

      You should use **CreateLayer** for noncustom layer types such as PHP App Server only if the stack does not have an existing layer of that type. A stack can have at most one instance of each noncustom layer; if you attempt to create a second instance, **CreateLayer** fails. A stack can have an arbitrary number of custom layers, so you can call **CreateLayer** as many times as you like for that layer type.

       

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/CreateLayer>`_    


    **Request Syntax** 
    ::

      response = client.create_layer(
          StackId='string',
          Type='aws-flow-ruby'|'ecs-cluster'|'java-app'|'lb'|'web'|'php-app'|'rails-app'|'nodejs-app'|'memcached'|'db-master'|'monitoring-master'|'custom',
          Name='string',
          Shortname='string',
          Attributes={
              'string': 'string'
          },
          CloudWatchLogsConfiguration={
              'Enabled': True|False,
              'LogStreams': [
                  {
                      'LogGroupName': 'string',
                      'DatetimeFormat': 'string',
                      'TimeZone': 'LOCAL'|'UTC',
                      'File': 'string',
                      'FileFingerprintLines': 'string',
                      'MultiLineStartPattern': 'string',
                      'InitialPosition': 'start_of_file'|'end_of_file',
                      'Encoding': 'ascii'|'big5'|'big5hkscs'|'cp037'|'cp424'|'cp437'|'cp500'|'cp720'|'cp737'|'cp775'|'cp850'|'cp852'|'cp855'|'cp856'|'cp857'|'cp858'|'cp860'|'cp861'|'cp862'|'cp863'|'cp864'|'cp865'|'cp866'|'cp869'|'cp874'|'cp875'|'cp932'|'cp949'|'cp950'|'cp1006'|'cp1026'|'cp1140'|'cp1250'|'cp1251'|'cp1252'|'cp1253'|'cp1254'|'cp1255'|'cp1256'|'cp1257'|'cp1258'|'euc_jp'|'euc_jis_2004'|'euc_jisx0213'|'euc_kr'|'gb2312'|'gbk'|'gb18030'|'hz'|'iso2022_jp'|'iso2022_jp_1'|'iso2022_jp_2'|'iso2022_jp_2004'|'iso2022_jp_3'|'iso2022_jp_ext'|'iso2022_kr'|'latin_1'|'iso8859_2'|'iso8859_3'|'iso8859_4'|'iso8859_5'|'iso8859_6'|'iso8859_7'|'iso8859_8'|'iso8859_9'|'iso8859_10'|'iso8859_13'|'iso8859_14'|'iso8859_15'|'iso8859_16'|'johab'|'koi8_r'|'koi8_u'|'mac_cyrillic'|'mac_greek'|'mac_iceland'|'mac_latin2'|'mac_roman'|'mac_turkish'|'ptcp154'|'shift_jis'|'shift_jis_2004'|'shift_jisx0213'|'utf_32'|'utf_32_be'|'utf_32_le'|'utf_16'|'utf_16_be'|'utf_16_le'|'utf_7'|'utf_8'|'utf_8_sig',
                      'BufferDuration': 123,
                      'BatchCount': 123,
                      'BatchSize': 123
                  },
              ]
          },
          CustomInstanceProfileArn='string',
          CustomJson='string',
          CustomSecurityGroupIds=[
              'string',
          ],
          Packages=[
              'string',
          ],
          VolumeConfigurations=[
              {
                  'MountPoint': 'string',
                  'RaidLevel': 123,
                  'NumberOfDisks': 123,
                  'Size': 123,
                  'VolumeType': 'string',
                  'Iops': 123
              },
          ],
          EnableAutoHealing=True|False,
          AutoAssignElasticIps=True|False,
          AutoAssignPublicIps=True|False,
          CustomRecipes={
              'Setup': [
                  'string',
              ],
              'Configure': [
                  'string',
              ],
              'Deploy': [
                  'string',
              ],
              'Undeploy': [
                  'string',
              ],
              'Shutdown': [
                  'string',
              ]
          },
          InstallUpdatesOnBoot=True|False,
          UseEbsOptimizedInstances=True|False,
          LifecycleEventConfiguration={
              'Shutdown': {
                  'ExecutionTimeout': 123,
                  'DelayUntilElbConnectionsDrained': True|False
              }
          }
      )
    :type StackId: string
    :param StackId: **[REQUIRED]** 

      The layer stack ID.

      

    
    :type Type: string
    :param Type: **[REQUIRED]** 

      The layer type. A stack cannot have more than one built-in layer of the same type. It can have any number of custom layers. Built-in layers are not available in Chef 12 stacks.

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      The layer name, which is used by the console.

      

    
    :type Shortname: string
    :param Shortname: **[REQUIRED]** 

      For custom layers only, use this parameter to specify the layer's short name, which is used internally by AWS OpsWorks Stacks and by Chef recipes. The short name is also used as the name for the directory where your app files are installed. It can have a maximum of 200 characters, which are limited to the alphanumeric characters, '-', '_', and '.'.

       

      The built-in layers' short names are defined by AWS OpsWorks Stacks. For more information, see the `Layer Reference <http://docs.aws.amazon.com/opsworks/latest/userguide/layers.html>`__ .

      

    
    :type Attributes: dict
    :param Attributes: 

      One or more user-defined key-value pairs to be added to the stack attributes.

       

      To create a cluster layer, set the ``EcsClusterArn`` attribute to the cluster's ARN.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type CloudWatchLogsConfiguration: dict
    :param CloudWatchLogsConfiguration: 

      Specifies CloudWatch Logs configuration options for the layer. For more information, see  CloudWatchLogsLogStream .

      

    
      - **Enabled** *(boolean) --* 

        Whether CloudWatch Logs is enabled for a layer.

        

      
      - **LogStreams** *(list) --* 

        A list of configuration options for CloudWatch Logs.

        

      
        - *(dict) --* 

          Describes the Amazon CloudWatch logs configuration for a layer. For detailed information about members of this data type, see the `CloudWatch Logs Agent Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html>`__ .

          

        
          - **LogGroupName** *(string) --* 

            Specifies the destination log group. A log group is created automatically if it doesn't already exist. Log group names can be between 1 and 512 characters long. Allowed characters include a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), '/' (forward slash), and '.' (period).

            

          
          - **DatetimeFormat** *(string) --* 

            Specifies how the time stamp is extracted from logs. For more information, see the `CloudWatch Logs Agent Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html>`__ .

            

          
          - **TimeZone** *(string) --* 

            Specifies the time zone of log event time stamps.

            

          
          - **File** *(string) --* 

            Specifies log files that you want to push to CloudWatch Logs.

             

             ``File`` can point to a specific file or multiple files (by using wild card characters such as ``/var/log/system.log*`` ). Only the latest file is pushed to CloudWatch Logs, based on file modification time. We recommend that you use wild card characters to specify a series of files of the same type, such as ``access_log.2014-06-01-01`` , ``access_log.2014-06-01-02`` , and so on by using a pattern like ``access_log.*`` . Don't use a wildcard to match multiple file types, such as ``access_log_80`` and ``access_log_443`` . To specify multiple, different file types, add another log stream entry to the configuration file, so that each log file type is stored in a different log group.

             

            Zipped files are not supported.

            

          
          - **FileFingerprintLines** *(string) --* 

            Specifies the range of lines for identifying a file. The valid values are one number, or two dash-delimited numbers, such as '1', '2-5'. The default value is '1', meaning the first line is used to calculate the fingerprint. Fingerprint lines are not sent to CloudWatch Logs unless all specified lines are available.

            

          
          - **MultiLineStartPattern** *(string) --* 

            Specifies the pattern for identifying the start of a log message.

            

          
          - **InitialPosition** *(string) --* 

            Specifies where to start to read data (start_of_file or end_of_file). The default is start_of_file. This setting is only used if there is no state persisted for that log stream.

            

          
          - **Encoding** *(string) --* 

            Specifies the encoding of the log file so that the file can be read correctly. The default is ``utf_8`` . Encodings supported by Python ``codecs.decode()`` can be used here.

            

          
          - **BufferDuration** *(integer) --* 

            Specifies the time duration for the batching of log events. The minimum value is 5000ms and default value is 5000ms.

            

          
          - **BatchCount** *(integer) --* 

            Specifies the max number of log events in a batch, up to 10000. The default value is 1000.

            

          
          - **BatchSize** *(integer) --* 

            Specifies the maximum size of log events in a batch, in bytes, up to 1048576 bytes. The default value is 32768 bytes. This size is calculated as the sum of all event messages in UTF-8, plus 26 bytes for each log event.

            

          
        
    
    
    :type CustomInstanceProfileArn: string
    :param CustomInstanceProfileArn: 

      The ARN of an IAM profile to be used for the layer's EC2 instances. For more information about IAM ARNs, see `Using Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ .

      

    
    :type CustomJson: string
    :param CustomJson: 

      A JSON-formatted string containing custom stack configuration and deployment attributes to be installed on the layer's instances. For more information, see `Using Custom JSON <http://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook-json-override.html>`__ . This feature is supported as of version 1.7.42 of the AWS CLI. 

      

    
    :type CustomSecurityGroupIds: list
    :param CustomSecurityGroupIds: 

      An array containing the layer custom security group IDs.

      

    
      - *(string) --* 

      
  
    :type Packages: list
    :param Packages: 

      An array of ``Package`` objects that describes the layer packages.

      

    
      - *(string) --* 

      
  
    :type VolumeConfigurations: list
    :param VolumeConfigurations: 

      A ``VolumeConfigurations`` object that describes the layer's Amazon EBS volumes.

      

    
      - *(dict) --* 

        Describes an Amazon EBS volume configuration.

        

      
        - **MountPoint** *(string) --* **[REQUIRED]** 

          The volume mount point. For example "/dev/sdh".

          

        
        - **RaidLevel** *(integer) --* 

          The volume `RAID level <http://en.wikipedia.org/wiki/Standard_RAID_levels>`__ .

          

        
        - **NumberOfDisks** *(integer) --* **[REQUIRED]** 

          The number of disks in the volume.

          

        
        - **Size** *(integer) --* **[REQUIRED]** 

          The volume size.

          

        
        - **VolumeType** *(string) --* 

          The volume type:

           

           
          * ``standard`` - Magnetic 
           
          * ``io1`` - Provisioned IOPS (SSD) 
           
          * ``gp2`` - General Purpose (SSD) 
           

          

        
        - **Iops** *(integer) --* 

          For PIOPS volumes, the IOPS per disk.

          

        
      
  
    :type EnableAutoHealing: boolean
    :param EnableAutoHealing: 

      Whether to disable auto healing for the layer.

      

    
    :type AutoAssignElasticIps: boolean
    :param AutoAssignElasticIps: 

      Whether to automatically assign an `Elastic IP address <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html>`__ to the layer's instances. For more information, see `How to Edit a Layer <http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-edit.html>`__ .

      

    
    :type AutoAssignPublicIps: boolean
    :param AutoAssignPublicIps: 

      For stacks that are running in a VPC, whether to automatically assign a public IP address to the layer's instances. For more information, see `How to Edit a Layer <http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-edit.html>`__ .

      

    
    :type CustomRecipes: dict
    :param CustomRecipes: 

      A ``LayerCustomRecipes`` object that specifies the layer custom recipes.

      

    
      - **Setup** *(list) --* 

        An array of custom recipe names to be run following a ``setup`` event.

        

      
        - *(string) --* 

        
    
      - **Configure** *(list) --* 

        An array of custom recipe names to be run following a ``configure`` event.

        

      
        - *(string) --* 

        
    
      - **Deploy** *(list) --* 

        An array of custom recipe names to be run following a ``deploy`` event.

        

      
        - *(string) --* 

        
    
      - **Undeploy** *(list) --* 

        An array of custom recipe names to be run following a ``undeploy`` event.

        

      
        - *(string) --* 

        
    
      - **Shutdown** *(list) --* 

        An array of custom recipe names to be run following a ``shutdown`` event.

        

      
        - *(string) --* 

        
    
    
    :type InstallUpdatesOnBoot: boolean
    :param InstallUpdatesOnBoot: 

      Whether to install operating system and package updates when the instance boots. The default value is ``true`` . To control when updates are installed, set this value to ``false`` . You must then update your instances manually by using  CreateDeployment to run the ``update_dependencies`` stack command or by manually running ``yum`` (Amazon Linux) or ``apt-get`` (Ubuntu) on the instances. 

       

      .. note::

         

        To ensure that your instances have the latest security updates, we strongly recommend using the default value of ``true`` .

         

      

    
    :type UseEbsOptimizedInstances: boolean
    :param UseEbsOptimizedInstances: 

      Whether to use Amazon EBS-optimized instances.

      

    
    :type LifecycleEventConfiguration: dict
    :param LifecycleEventConfiguration: 

      A ``LifeCycleEventConfiguration`` object that you can use to configure the Shutdown event to specify an execution timeout and enable or disable Elastic Load Balancer connection draining.

      

    
      - **Shutdown** *(dict) --* 

        A ``ShutdownEventConfiguration`` object that specifies the Shutdown event configuration.

        

      
        - **ExecutionTimeout** *(integer) --* 

          The time, in seconds, that AWS OpsWorks Stacks will wait after triggering a Shutdown event before shutting down an instance.

          

        
        - **DelayUntilElbConnectionsDrained** *(boolean) --* 

          Whether to enable Elastic Load Balancing connection draining. For more information, see `Connection Draining <http://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/TerminologyandKeyConcepts.html#conn-drain>`__  

          

        
      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'LayerId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``CreateLayer`` request.

        
        

        - **LayerId** *(string) --* 

          The layer ID.

          
    

  .. py:method:: create_stack(**kwargs)

    

    Creates a new stack. For more information, see `Create a New Stack <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-edit.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/CreateStack>`_    


    **Request Syntax** 
    ::

      response = client.create_stack(
          Name='string',
          Region='string',
          VpcId='string',
          Attributes={
              'string': 'string'
          },
          ServiceRoleArn='string',
          DefaultInstanceProfileArn='string',
          DefaultOs='string',
          HostnameTheme='string',
          DefaultAvailabilityZone='string',
          DefaultSubnetId='string',
          CustomJson='string',
          ConfigurationManager={
              'Name': 'string',
              'Version': 'string'
          },
          ChefConfiguration={
              'ManageBerkshelf': True|False,
              'BerkshelfVersion': 'string'
          },
          UseCustomCookbooks=True|False,
          UseOpsworksSecurityGroups=True|False,
          CustomCookbooksSource={
              'Type': 'git'|'svn'|'archive'|'s3',
              'Url': 'string',
              'Username': 'string',
              'Password': 'string',
              'SshKey': 'string',
              'Revision': 'string'
          },
          DefaultSshKeyName='string',
          DefaultRootDeviceType='ebs'|'instance-store',
          AgentVersion='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The stack name.

      

    
    :type Region: string
    :param Region: **[REQUIRED]** 

      The stack's AWS region, such as "ap-south-1". For more information about Amazon regions, see `Regions and Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html>`__ .

      

    
    :type VpcId: string
    :param VpcId: 

      The ID of the VPC that the stack is to be launched into. The VPC must be in the stack's region. All instances are launched into this VPC. You cannot change the ID later.

       

       
      * If your account supports EC2-Classic, the default value is ``no VPC`` . 
       
      * If your account does not support EC2-Classic, the default value is the default VPC for the specified region. 
       

       

      If the VPC ID corresponds to a default VPC and you have specified either the ``DefaultAvailabilityZone`` or the ``DefaultSubnetId`` parameter only, AWS OpsWorks Stacks infers the value of the other parameter. If you specify neither parameter, AWS OpsWorks Stacks sets these parameters to the first valid Availability Zone for the specified region and the corresponding default VPC subnet ID, respectively.

       

      If you specify a nondefault VPC ID, note the following:

       

       
      * It must belong to a VPC in your account that is in the specified region. 
       
      * You must specify a value for ``DefaultSubnetId`` . 
       

       

      For more information on how to use AWS OpsWorks Stacks with a VPC, see `Running a Stack in a VPC <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-vpc.html>`__ . For more information on default VPC and EC2-Classic, see `Supported Platforms <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-platforms.html>`__ . 

      

    
    :type Attributes: dict
    :param Attributes: 

      One or more user-defined key-value pairs to be added to the stack attributes.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type ServiceRoleArn: string
    :param ServiceRoleArn: **[REQUIRED]** 

      The stack's AWS Identity and Access Management (IAM) role, which allows AWS OpsWorks Stacks to work with AWS resources on your behalf. You must set this parameter to the Amazon Resource Name (ARN) for an existing IAM role. For more information about IAM ARNs, see `Using Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ .

      

    
    :type DefaultInstanceProfileArn: string
    :param DefaultInstanceProfileArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of an IAM profile that is the default profile for all of the stack's EC2 instances. For more information about IAM ARNs, see `Using Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ .

      

    
    :type DefaultOs: string
    :param DefaultOs: 

      The stack's default operating system, which is installed on every instance unless you specify a different operating system when you create the instance. You can specify one of the following.

       

       
      * A supported Linux operating system: An Amazon Linux version, such as ``Amazon Linux 2017.03`` , ``Amazon Linux 2016.09`` , ``Amazon Linux 2016.03`` , ``Amazon Linux 2015.09`` , or ``Amazon Linux 2015.03`` . 
       
      * A supported Ubuntu operating system, such as ``Ubuntu 16.04 LTS`` , ``Ubuntu 14.04 LTS`` , or ``Ubuntu 12.04 LTS`` . 
       
      * ``CentOS Linux 7``   
       
      * ``Red Hat Enterprise Linux 7``   
       
      * A supported Windows operating system, such as ``Microsoft Windows Server 2012 R2 Base`` , ``Microsoft Windows Server 2012 R2 with SQL Server Express`` , ``Microsoft Windows Server 2012 R2 with SQL Server Standard`` , or ``Microsoft Windows Server 2012 R2 with SQL Server Web`` . 
       
      * A custom AMI: ``Custom`` . You specify the custom AMI you want to use when you create instances. For more information, see `Using Custom AMIs <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-custom-ami.html>`__ . 
       

       

      The default option is the current Amazon Linux version. For more information on the supported operating systems, see `AWS OpsWorks Stacks Operating Systems <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-os.html>`__ .

      

    
    :type HostnameTheme: string
    :param HostnameTheme: 

      The stack's host name theme, with spaces replaced by underscores. The theme is used to generate host names for the stack's instances. By default, ``HostnameTheme`` is set to ``Layer_Dependent`` , which creates host names by appending integers to the layer's short name. The other themes are:

       

       
      * ``Baked_Goods``   
       
      * ``Clouds``   
       
      * ``Europe_Cities``   
       
      * ``Fruits``   
       
      * ``Greek_Deities``   
       
      * ``Legendary_creatures_from_Japan``   
       
      * ``Planets_and_Moons``   
       
      * ``Roman_Deities``   
       
      * ``Scottish_Islands``   
       
      * ``US_Cities``   
       
      * ``Wild_Cats``   
       

       

      To obtain a generated host name, call ``GetHostNameSuggestion`` , which returns a host name based on the current theme.

      

    
    :type DefaultAvailabilityZone: string
    :param DefaultAvailabilityZone: 

      The stack's default Availability Zone, which must be in the specified region. For more information, see `Regions and Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html>`__ . If you also specify a value for ``DefaultSubnetId`` , the subnet must be in the same zone. For more information, see the ``VpcId`` parameter description. 

      

    
    :type DefaultSubnetId: string
    :param DefaultSubnetId: 

      The stack's default VPC subnet ID. This parameter is required if you specify a value for the ``VpcId`` parameter. All instances are launched into this subnet unless you specify otherwise when you create the instance. If you also specify a value for ``DefaultAvailabilityZone`` , the subnet must be in that zone. For information on default values and when this parameter is required, see the ``VpcId`` parameter description. 

      

    
    :type CustomJson: string
    :param CustomJson: 

      A string that contains user-defined, custom JSON. It can be used to override the corresponding default stack configuration attribute values or to pass data to recipes. The string should be in the following format:

       

       ``"{\"key1\": \"value1\", \"key2\": \"value2\",...}"``  

       

      For more information on custom JSON, see `Use Custom JSON to Modify the Stack Configuration Attributes <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-json.html>`__ .

      

    
    :type ConfigurationManager: dict
    :param ConfigurationManager: 

      The configuration manager. When you create a stack we recommend that you use the configuration manager to specify the Chef version: 12, 11.10, or 11.4 for Linux stacks, or 12.2 for Windows stacks. The default value for Linux stacks is currently 11.4.

      

    
      - **Name** *(string) --* 

        The name. This parameter must be set to "Chef".

        

      
      - **Version** *(string) --* 

        The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to 12.2 for Windows stacks. The default value for Linux stacks is 11.4.

        

      
    
    :type ChefConfiguration: dict
    :param ChefConfiguration: 

      A ``ChefConfiguration`` object that specifies whether to enable Berkshelf and the Berkshelf version on Chef 11.10 stacks. For more information, see `Create a New Stack <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`__ .

      

    
      - **ManageBerkshelf** *(boolean) --* 

        Whether to enable Berkshelf.

        

      
      - **BerkshelfVersion** *(string) --* 

        The Berkshelf version.

        

      
    
    :type UseCustomCookbooks: boolean
    :param UseCustomCookbooks: 

      Whether the stack uses custom cookbooks.

      

    
    :type UseOpsworksSecurityGroups: boolean
    :param UseOpsworksSecurityGroups: 

      Whether to associate the AWS OpsWorks Stacks built-in security groups with the stack's layers.

       

      AWS OpsWorks Stacks provides a standard set of built-in security groups, one for each layer, which are associated with layers by default. With ``UseOpsworksSecurityGroups`` you can instead provide your own custom security groups. ``UseOpsworksSecurityGroups`` has the following settings: 

       

       
      * True - AWS OpsWorks Stacks automatically associates the appropriate built-in security group with each layer (default setting). You can associate additional security groups with a layer after you create it, but you cannot delete the built-in security group. 
       
      * False - AWS OpsWorks Stacks does not associate built-in security groups with layers. You must create appropriate EC2 security groups and associate a security group with each layer that you create. However, you can still manually associate a built-in security group with a layer on creation; custom security groups are required only for those layers that need custom settings. 
       

       

      For more information, see `Create a New Stack <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`__ .

      

    
    :type CustomCookbooksSource: dict
    :param CustomCookbooksSource: 

      Contains the information required to retrieve an app or cookbook from a repository. For more information, see `Creating Apps <http://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html>`__ or `Custom Recipes and Cookbooks <http://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html>`__ .

      

    
      - **Type** *(string) --* 

        The repository type.

        

      
      - **Url** *(string) --* 

        The source URL. The following is an example of an Amazon S3 source URL: ``https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz`` .

        

      
      - **Username** *(string) --* 

        This parameter depends on the repository type.

         

         
        * For Amazon S3 bundles, set ``Username`` to the appropriate IAM access key ID. 
         
        * For HTTP bundles, Git repositories, and Subversion repositories, set ``Username`` to the user name. 
         

        

      
      - **Password** *(string) --* 

        When included in a request, the parameter depends on the repository type.

         

         
        * For Amazon S3 bundles, set ``Password`` to the appropriate IAM secret access key. 
         
        * For HTTP bundles and Subversion repositories, set ``Password`` to the password. 
         

         

        For more information on how to safely handle IAM credentials, see `http\://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html <http://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html>`__ .

         

        In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

        

      
      - **SshKey** *(string) --* 

        In requests, the repository's SSH key.

         

        In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

        

      
      - **Revision** *(string) --* 

        The application's version. AWS OpsWorks Stacks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.

        

      
    
    :type DefaultSshKeyName: string
    :param DefaultSshKeyName: 

      A default Amazon EC2 key pair name. The default value is none. If you specify a key pair name, AWS OpsWorks installs the public key on the instance and you can use the private key with an SSH client to log in to the instance. For more information, see `Using SSH to Communicate with an Instance <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-ssh.html>`__ and `Managing SSH Access <http://docs.aws.amazon.com/opsworks/latest/userguide/security-ssh-access.html>`__ . You can override this setting by specifying a different key pair, or no key pair, when you `create an instance <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-add.html>`__ . 

      

    
    :type DefaultRootDeviceType: string
    :param DefaultRootDeviceType: 

      The default root device type. This value is the default for all instances in the stack, but you can override it when you create an instance. The default option is ``instance-store`` . For more information, see `Storage for the Root Device <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-for-the-root-device>`__ .

      

    
    :type AgentVersion: string
    :param AgentVersion: 

      The default AWS OpsWorks Stacks agent version. You have the following options:

       

       
      * Auto-update - Set this parameter to ``LATEST`` . AWS OpsWorks Stacks automatically installs new agent versions on the stack's instances as soon as they are available. 
       
      * Fixed version - Set this parameter to your preferred agent version. To update the agent version, you must edit the stack configuration and specify a new version. AWS OpsWorks Stacks then automatically installs that version on the stack's instances. 
       

       

      The default setting is the most recent release of the agent. To specify an agent version, you must use the complete version number, not the abbreviated number shown on the console. For a list of available agent version numbers, call  DescribeAgentVersions . AgentVersion cannot be set to Chef 12.2.

       

      .. note::

         

        You can also specify an agent version when you create or update an instance, which overrides the stack's default setting.

         

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'StackId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``CreateStack`` request.

        
        

        - **StackId** *(string) --* 

          The stack ID, which is an opaque string that you use to identify the stack when performing actions such as ``DescribeStacks`` .

          
    

  .. py:method:: create_user_profile(**kwargs)

    

    Creates a new user profile.

     

     **Required Permissions** : To use this action, an IAM user must have an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/CreateUserProfile>`_    


    **Request Syntax** 
    ::

      response = client.create_user_profile(
          IamUserArn='string',
          SshUsername='string',
          SshPublicKey='string',
          AllowSelfManagement=True|False
      )
    :type IamUserArn: string
    :param IamUserArn: **[REQUIRED]** 

      The user's IAM ARN; this can also be a federated user's ARN.

      

    
    :type SshUsername: string
    :param SshUsername: 

      The user's SSH user name. The allowable characters are [a-z], [A-Z], [0-9], '-', and '_'. If the specified name includes other punctuation marks, AWS OpsWorks Stacks removes them. For example, ``my.name`` will be changed to ``myname`` . If you do not specify an SSH user name, AWS OpsWorks Stacks generates one from the IAM user name. 

      

    
    :type SshPublicKey: string
    :param SshPublicKey: 

      The user's public SSH key.

      

    
    :type AllowSelfManagement: boolean
    :param AllowSelfManagement: 

      Whether users can specify their own SSH public key through the My Settings page. For more information, see `Setting an IAM User's Public SSH Key <http://docs.aws.amazon.com/opsworks/latest/userguide/security-settingsshkey.html>`__ .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'IamUserArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``CreateUserProfile`` request.

        
        

        - **IamUserArn** *(string) --* 

          The user's IAM ARN.

          
    

  .. py:method:: delete_app(**kwargs)

    

    Deletes a specified app.

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DeleteApp>`_    


    **Request Syntax** 
    ::

      response = client.delete_app(
          AppId='string'
      )
    :type AppId: string
    :param AppId: **[REQUIRED]** 

      The app ID.

      

    
    
    :returns: None

  .. py:method:: delete_instance(**kwargs)

    

    Deletes a specified instance, which terminates the associated Amazon EC2 instance. You must stop an instance before you can delete it.

     

    For more information, see `Deleting Instances <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-delete.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DeleteInstance>`_    


    **Request Syntax** 
    ::

      response = client.delete_instance(
          InstanceId='string',
          DeleteElasticIp=True|False,
          DeleteVolumes=True|False
      )
    :type InstanceId: string
    :param InstanceId: **[REQUIRED]** 

      The instance ID.

      

    
    :type DeleteElasticIp: boolean
    :param DeleteElasticIp: 

      Whether to delete the instance Elastic IP address.

      

    
    :type DeleteVolumes: boolean
    :param DeleteVolumes: 

      Whether to delete the instance's Amazon EBS volumes.

      

    
    
    :returns: None

  .. py:method:: delete_layer(**kwargs)

    

    Deletes a specified layer. You must first stop and then delete all associated instances or unassign registered instances. For more information, see `How to Delete a Layer <http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-delete.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DeleteLayer>`_    


    **Request Syntax** 
    ::

      response = client.delete_layer(
          LayerId='string'
      )
    :type LayerId: string
    :param LayerId: **[REQUIRED]** 

      The layer ID.

      

    
    
    :returns: None

  .. py:method:: delete_stack(**kwargs)

    

    Deletes a specified stack. You must first delete all instances, layers, and apps or deregister registered instances. For more information, see `Shut Down a Stack <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-shutting.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DeleteStack>`_    


    **Request Syntax** 
    ::

      response = client.delete_stack(
          StackId='string'
      )
    :type StackId: string
    :param StackId: **[REQUIRED]** 

      The stack ID.

      

    
    
    :returns: None

  .. py:method:: delete_user_profile(**kwargs)

    

    Deletes a user profile.

     

     **Required Permissions** : To use this action, an IAM user must have an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DeleteUserProfile>`_    


    **Request Syntax** 
    ::

      response = client.delete_user_profile(
          IamUserArn='string'
      )
    :type IamUserArn: string
    :param IamUserArn: **[REQUIRED]** 

      The user's IAM ARN. This can also be a federated user's ARN.

      

    
    
    :returns: None

  .. py:method:: deregister_ecs_cluster(**kwargs)

    

    Deregisters a specified Amazon ECS cluster from a stack. For more information, see `Resource Management <http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-ecscluster.html#workinglayers-ecscluster-delete>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack or an attached policy that explicitly grants permissions. For more information on user permissions, see `http\://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DeregisterEcsCluster>`_    


    **Request Syntax** 
    ::

      response = client.deregister_ecs_cluster(
          EcsClusterArn='string'
      )
    :type EcsClusterArn: string
    :param EcsClusterArn: **[REQUIRED]** 

      The cluster's ARN.

      

    
    
    :returns: None

  .. py:method:: deregister_elastic_ip(**kwargs)

    

    Deregisters a specified Elastic IP address. The address can then be registered by another stack. For more information, see `Resource Management <http://docs.aws.amazon.com/opsworks/latest/userguide/resources.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DeregisterElasticIp>`_    


    **Request Syntax** 
    ::

      response = client.deregister_elastic_ip(
          ElasticIp='string'
      )
    :type ElasticIp: string
    :param ElasticIp: **[REQUIRED]** 

      The Elastic IP address.

      

    
    
    :returns: None

  .. py:method:: deregister_instance(**kwargs)

    

    Deregister a registered Amazon EC2 or on-premises instance. This action removes the instance from the stack and returns it to your control. This action can not be used with instances that were created with AWS OpsWorks Stacks.

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DeregisterInstance>`_    


    **Request Syntax** 
    ::

      response = client.deregister_instance(
          InstanceId='string'
      )
    :type InstanceId: string
    :param InstanceId: **[REQUIRED]** 

      The instance ID.

      

    
    
    :returns: None

  .. py:method:: deregister_rds_db_instance(**kwargs)

    

    Deregisters an Amazon RDS instance.

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DeregisterRdsDbInstance>`_    


    **Request Syntax** 
    ::

      response = client.deregister_rds_db_instance(
          RdsDbInstanceArn='string'
      )
    :type RdsDbInstanceArn: string
    :param RdsDbInstanceArn: **[REQUIRED]** 

      The Amazon RDS instance's ARN.

      

    
    
    :returns: None

  .. py:method:: deregister_volume(**kwargs)

    

    Deregisters an Amazon EBS volume. The volume can then be registered by another stack. For more information, see `Resource Management <http://docs.aws.amazon.com/opsworks/latest/userguide/resources.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DeregisterVolume>`_    


    **Request Syntax** 
    ::

      response = client.deregister_volume(
          VolumeId='string'
      )
    :type VolumeId: string
    :param VolumeId: **[REQUIRED]** 

      The AWS OpsWorks Stacks volume ID, which is the GUID that AWS OpsWorks Stacks assigned to the instance when you registered the volume with the stack, not the Amazon EC2 volume ID.

      

    
    
    :returns: None

  .. py:method:: describe_agent_versions(**kwargs)

    

    Describes the available AWS OpsWorks Stacks agent versions. You must specify a stack ID or a configuration manager. ``DescribeAgentVersions`` returns a list of available agent versions for the specified stack or configuration manager.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeAgentVersions>`_    


    **Request Syntax** 
    ::

      response = client.describe_agent_versions(
          StackId='string',
          ConfigurationManager={
              'Name': 'string',
              'Version': 'string'
          }
      )
    :type StackId: string
    :param StackId: 

      The stack ID.

      

    
    :type ConfigurationManager: dict
    :param ConfigurationManager: 

      The configuration manager.

      

    
      - **Name** *(string) --* 

        The name. This parameter must be set to "Chef".

        

      
      - **Version** *(string) --* 

        The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to 12.2 for Windows stacks. The default value for Linux stacks is 11.4.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AgentVersions': [
                {
                    'Version': 'string',
                    'ConfigurationManager': {
                        'Name': 'string',
                        'Version': 'string'
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``DescribeAgentVersions`` request.

        
        

        - **AgentVersions** *(list) --* 

          The agent versions for the specified stack or configuration manager. Note that this value is the complete version number, not the abbreviated number used by the console.

          
          

          - *(dict) --* 

            Describes an agent version.

            
            

            - **Version** *(string) --* 

              The agent version.

              
            

            - **ConfigurationManager** *(dict) --* 

              The configuration manager.

              
              

              - **Name** *(string) --* 

                The name. This parameter must be set to "Chef".

                
              

              - **Version** *(string) --* 

                The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to 12.2 for Windows stacks. The default value for Linux stacks is 11.4.

                
          
        
      
    

  .. py:method:: describe_apps(**kwargs)

    

    Requests a description of a specified set of apps.

     

    .. note::

       

      This call accepts only one resource-identifying parameter.

       

     

     **Required Permissions** : To use this action, an IAM user must have a Show, Deploy, or Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeApps>`_    


    **Request Syntax** 
    ::

      response = client.describe_apps(
          StackId='string',
          AppIds=[
              'string',
          ]
      )
    :type StackId: string
    :param StackId: 

      The app stack ID. If you use this parameter, ``DescribeApps`` returns a description of the apps in the specified stack.

      

    
    :type AppIds: list
    :param AppIds: 

      An array of app IDs for the apps to be described. If you use this parameter, ``DescribeApps`` returns a description of the specified apps. Otherwise, it returns a description of every app.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Apps': [
                {
                    'AppId': 'string',
                    'StackId': 'string',
                    'Shortname': 'string',
                    'Name': 'string',
                    'Description': 'string',
                    'DataSources': [
                        {
                            'Type': 'string',
                            'Arn': 'string',
                            'DatabaseName': 'string'
                        },
                    ],
                    'Type': 'aws-flow-ruby'|'java'|'rails'|'php'|'nodejs'|'static'|'other',
                    'AppSource': {
                        'Type': 'git'|'svn'|'archive'|'s3',
                        'Url': 'string',
                        'Username': 'string',
                        'Password': 'string',
                        'SshKey': 'string',
                        'Revision': 'string'
                    },
                    'Domains': [
                        'string',
                    ],
                    'EnableSsl': True|False,
                    'SslConfiguration': {
                        'Certificate': 'string',
                        'PrivateKey': 'string',
                        'Chain': 'string'
                    },
                    'Attributes': {
                        'string': 'string'
                    },
                    'CreatedAt': 'string',
                    'Environment': [
                        {
                            'Key': 'string',
                            'Value': 'string',
                            'Secure': True|False
                        },
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``DescribeApps`` request.

        
        

        - **Apps** *(list) --* 

          An array of ``App`` objects that describe the specified apps. 

          
          

          - *(dict) --* 

            A description of the app.

            
            

            - **AppId** *(string) --* 

              The app ID.

              
            

            - **StackId** *(string) --* 

              The app stack ID.

              
            

            - **Shortname** *(string) --* 

              The app's short name.

              
            

            - **Name** *(string) --* 

              The app name.

              
            

            - **Description** *(string) --* 

              A description of the app.

              
            

            - **DataSources** *(list) --* 

              The app's data sources.

              
              

              - *(dict) --* 

                Describes an app's data source.

                
                

                - **Type** *(string) --* 

                  The data source's type, ``AutoSelectOpsworksMysqlInstance`` , ``OpsworksMysqlInstance`` , or ``RdsDbInstance`` .

                  
                

                - **Arn** *(string) --* 

                  The data source's ARN.

                  
                

                - **DatabaseName** *(string) --* 

                  The database name.

                  
            
          
            

            - **Type** *(string) --* 

              The app type.

              
            

            - **AppSource** *(dict) --* 

              A ``Source`` object that describes the app repository.

              
              

              - **Type** *(string) --* 

                The repository type.

                
              

              - **Url** *(string) --* 

                The source URL. The following is an example of an Amazon S3 source URL: ``https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz`` .

                
              

              - **Username** *(string) --* 

                This parameter depends on the repository type.

                 

                 
                * For Amazon S3 bundles, set ``Username`` to the appropriate IAM access key ID. 
                 
                * For HTTP bundles, Git repositories, and Subversion repositories, set ``Username`` to the user name. 
                 

                
              

              - **Password** *(string) --* 

                When included in a request, the parameter depends on the repository type.

                 

                 
                * For Amazon S3 bundles, set ``Password`` to the appropriate IAM secret access key. 
                 
                * For HTTP bundles and Subversion repositories, set ``Password`` to the password. 
                 

                 

                For more information on how to safely handle IAM credentials, see `http\://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html <http://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html>`__ .

                 

                In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

                
              

              - **SshKey** *(string) --* 

                In requests, the repository's SSH key.

                 

                In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

                
              

              - **Revision** *(string) --* 

                The application's version. AWS OpsWorks Stacks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.

                
          
            

            - **Domains** *(list) --* 

              The app vhost settings with multiple domains separated by commas. For example: ``'www.example.com, example.com'``  

              
              

              - *(string) --* 
          
            

            - **EnableSsl** *(boolean) --* 

              Whether to enable SSL for the app.

              
            

            - **SslConfiguration** *(dict) --* 

              An ``SslConfiguration`` object with the SSL configuration.

              
              

              - **Certificate** *(string) --* 

                The contents of the certificate's domain.crt file.

                
              

              - **PrivateKey** *(string) --* 

                The private key; the contents of the certificate's domain.kex file.

                
              

              - **Chain** *(string) --* 

                Optional. Can be used to specify an intermediate certificate authority key or client authentication.

                
          
            

            - **Attributes** *(dict) --* 

              The stack attributes.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **CreatedAt** *(string) --* 

              When the app was created.

              
            

            - **Environment** *(list) --* 

              An array of ``EnvironmentVariable`` objects that specify environment variables to be associated with the app. After you deploy the app, these variables are defined on the associated app server instances. For more information, see `Environment Variables <http://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html#workingapps-creating-environment>`__ . 

               

              .. note::

                 

                There is no specific limit on the number of environment variables. However, the size of the associated data structure - which includes the variable names, values, and protected flag values - cannot exceed 10 KB (10240 Bytes). This limit should accommodate most if not all use cases, but if you do exceed it, you will cause an exception (API) with an "Environment: is too large (maximum is 10KB)" message.

                 

              
              

              - *(dict) --* 

                Represents an app's environment variable.

                
                

                - **Key** *(string) --* 

                  (Required) The environment variable's name, which can consist of up to 64 characters and must be specified. The name can contain upper- and lowercase letters, numbers, and underscores (_), but it must start with a letter or underscore.

                  
                

                - **Value** *(string) --* 

                  (Optional) The environment variable's value, which can be left empty. If you specify a value, it can contain up to 256 characters, which must all be printable.

                  
                

                - **Secure** *(boolean) --* 

                  (Optional) Whether the variable's value will be returned by the  DescribeApps action. To conceal an environment variable's value, set ``Secure`` to ``true`` . ``DescribeApps`` then returns ``*****FILTERED*****`` instead of the actual value. The default value for ``Secure`` is ``false`` . 

                  
            
          
        
      
    

  .. py:method:: describe_commands(**kwargs)

    

    Describes the results of specified commands.

     

    .. note::

       

      This call accepts only one resource-identifying parameter.

       

     

     **Required Permissions** : To use this action, an IAM user must have a Show, Deploy, or Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeCommands>`_    


    **Request Syntax** 
    ::

      response = client.describe_commands(
          DeploymentId='string',
          InstanceId='string',
          CommandIds=[
              'string',
          ]
      )
    :type DeploymentId: string
    :param DeploymentId: 

      The deployment ID. If you include this parameter, ``DescribeCommands`` returns a description of the commands associated with the specified deployment.

      

    
    :type InstanceId: string
    :param InstanceId: 

      The instance ID. If you include this parameter, ``DescribeCommands`` returns a description of the commands associated with the specified instance.

      

    
    :type CommandIds: list
    :param CommandIds: 

      An array of command IDs. If you include this parameter, ``DescribeCommands`` returns a description of the specified commands. Otherwise, it returns a description of every command.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Commands': [
                {
                    'CommandId': 'string',
                    'InstanceId': 'string',
                    'DeploymentId': 'string',
                    'CreatedAt': 'string',
                    'AcknowledgedAt': 'string',
                    'CompletedAt': 'string',
                    'Status': 'string',
                    'ExitCode': 123,
                    'LogUrl': 'string',
                    'Type': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``DescribeCommands`` request.

        
        

        - **Commands** *(list) --* 

          An array of ``Command`` objects that describe each of the specified commands.

          
          

          - *(dict) --* 

            Describes a command.

            
            

            - **CommandId** *(string) --* 

              The command ID.

              
            

            - **InstanceId** *(string) --* 

              The ID of the instance where the command was executed.

              
            

            - **DeploymentId** *(string) --* 

              The command deployment ID.

              
            

            - **CreatedAt** *(string) --* 

              Date and time when the command was run.

              
            

            - **AcknowledgedAt** *(string) --* 

              Date and time when the command was acknowledged.

              
            

            - **CompletedAt** *(string) --* 

              Date when the command completed.

              
            

            - **Status** *(string) --* 

              The command status:

               

               
              * failed 
               
              * successful 
               
              * skipped 
               
              * pending 
               

              
            

            - **ExitCode** *(integer) --* 

              The command exit code.

              
            

            - **LogUrl** *(string) --* 

              The URL of the command log.

              
            

            - **Type** *(string) --* 

              The command type:

               

               
              * ``configure``   
               
              * ``deploy``   
               
              * ``execute_recipes``   
               
              * ``install_dependencies``   
               
              * ``restart``   
               
              * ``rollback``   
               
              * ``setup``   
               
              * ``start``   
               
              * ``stop``   
               
              * ``undeploy``   
               
              * ``update_custom_cookbooks``   
               
              * ``update_dependencies``   
               

              
        
      
    

  .. py:method:: describe_deployments(**kwargs)

    

    Requests a description of a specified set of deployments.

     

    .. note::

       

      This call accepts only one resource-identifying parameter.

       

     

     **Required Permissions** : To use this action, an IAM user must have a Show, Deploy, or Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeDeployments>`_    


    **Request Syntax** 
    ::

      response = client.describe_deployments(
          StackId='string',
          AppId='string',
          DeploymentIds=[
              'string',
          ]
      )
    :type StackId: string
    :param StackId: 

      The stack ID. If you include this parameter, ``DescribeDeployments`` returns a description of the commands associated with the specified stack.

      

    
    :type AppId: string
    :param AppId: 

      The app ID. If you include this parameter, ``DescribeDeployments`` returns a description of the commands associated with the specified app.

      

    
    :type DeploymentIds: list
    :param DeploymentIds: 

      An array of deployment IDs to be described. If you include this parameter, ``DescribeDeployments`` returns a description of the specified deployments. Otherwise, it returns a description of every deployment.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Deployments': [
                {
                    'DeploymentId': 'string',
                    'StackId': 'string',
                    'AppId': 'string',
                    'CreatedAt': 'string',
                    'CompletedAt': 'string',
                    'Duration': 123,
                    'IamUserArn': 'string',
                    'Comment': 'string',
                    'Command': {
                        'Name': 'install_dependencies'|'update_dependencies'|'update_custom_cookbooks'|'execute_recipes'|'configure'|'setup'|'deploy'|'rollback'|'start'|'stop'|'restart'|'undeploy',
                        'Args': {
                            'string': [
                                'string',
                            ]
                        }
                    },
                    'Status': 'string',
                    'CustomJson': 'string',
                    'InstanceIds': [
                        'string',
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``DescribeDeployments`` request.

        
        

        - **Deployments** *(list) --* 

          An array of ``Deployment`` objects that describe the deployments.

          
          

          - *(dict) --* 

            Describes a deployment of a stack or app.

            
            

            - **DeploymentId** *(string) --* 

              The deployment ID.

              
            

            - **StackId** *(string) --* 

              The stack ID.

              
            

            - **AppId** *(string) --* 

              The app ID.

              
            

            - **CreatedAt** *(string) --* 

              Date when the deployment was created.

              
            

            - **CompletedAt** *(string) --* 

              Date when the deployment completed.

              
            

            - **Duration** *(integer) --* 

              The deployment duration.

              
            

            - **IamUserArn** *(string) --* 

              The user's IAM ARN.

              
            

            - **Comment** *(string) --* 

              A user-defined comment.

              
            

            - **Command** *(dict) --* 

              Used to specify a stack or deployment command.

              
              

              - **Name** *(string) --* 

                Specifies the operation. You can specify only one command.

                 

                For stacks, the following commands are available:

                 

                 
                * ``execute_recipes`` : Execute one or more recipes. To specify the recipes, set an ``Args`` parameter named ``recipes`` to the list of recipes to be executed. For example, to execute ``phpapp::appsetup`` , set ``Args`` to ``{"recipes":["phpapp::appsetup"]}`` . 
                 
                * ``install_dependencies`` : Install the stack's dependencies. 
                 
                * ``update_custom_cookbooks`` : Update the stack's custom cookbooks. 
                 
                * ``update_dependencies`` : Update the stack's dependencies. 
                 

                 

                .. note::

                   

                  The update_dependencies and install_dependencies commands are supported only for Linux instances. You can run the commands successfully on Windows instances, but they do nothing.

                   

                 

                For apps, the following commands are available:

                 

                 
                * ``deploy`` : Deploy an app. Ruby on Rails apps have an optional ``Args`` parameter named ``migrate`` . Set ``Args`` to {"migrate":["true"]} to migrate the database. The default setting is {"migrate":["false"]}. 
                 
                * ``rollback`` Roll the app back to the previous version. When you update an app, AWS OpsWorks Stacks stores the previous version, up to a maximum of five versions. You can use this command to roll an app back as many as four versions. 
                 
                * ``start`` : Start the app's web or application server. 
                 
                * ``stop`` : Stop the app's web or application server. 
                 
                * ``restart`` : Restart the app's web or application server. 
                 
                * ``undeploy`` : Undeploy the app. 
                 

                
              

              - **Args** *(dict) --* 

                The arguments of those commands that take arguments. It should be set to a JSON object with the following format:

                 

                 ``{"arg_name1" : ["value1", "value2", ...], "arg_name2" : ["value1", "value2", ...], ...}``  

                 

                The ``update_dependencies`` command takes two arguments:

                 

                 
                * ``upgrade_os_to`` - Specifies the desired Amazon Linux version for instances whose OS you want to upgrade, such as ``Amazon Linux 2016.09`` . You must also set the ``allow_reboot`` argument to true. 
                 
                * ``allow_reboot`` - Specifies whether to allow AWS OpsWorks Stacks to reboot the instances if necessary, after installing the updates. This argument can be set to either ``true`` or ``false`` . The default value is ``false`` . 
                 

                 

                For example, to upgrade an instance to Amazon Linux 2016.09, set ``Args`` to the following.

                 

                 ``{ "upgrade_os_to":["Amazon Linux 2016.09"], "allow_reboot":["true"] }``  

                
                

                - *(string) --* 
                  

                  - *(list) --* 
                    

                    - *(string) --* 
                
            
          
          
            

            - **Status** *(string) --* 

              The deployment status:

               

               
              * running 
               
              * successful 
               
              * failed 
               

              
            

            - **CustomJson** *(string) --* 

              A string that contains user-defined custom JSON. It can be used to override the corresponding default stack configuration attribute values for stack or to pass data to recipes. The string should be in the following format:

               

               ``"{\"key1\": \"value1\", \"key2\": \"value2\",...}"``  

               

              For more information on custom JSON, see `Use Custom JSON to Modify the Stack Configuration Attributes <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-json.html>`__ .

              
            

            - **InstanceIds** *(list) --* 

              The IDs of the target instances.

              
              

              - *(string) --* 
          
        
      
    

  .. py:method:: describe_ecs_clusters(**kwargs)

    

    Describes Amazon ECS clusters that are registered with a stack. If you specify only a stack ID, you can use the ``MaxResults`` and ``NextToken`` parameters to paginate the response. However, AWS OpsWorks Stacks currently supports only one cluster per layer, so the result set has a maximum of one element.

     

     **Required Permissions** : To use this action, an IAM user must have a Show, Deploy, or Manage permissions level for the stack or an attached policy that explicitly grants permission. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

     

    This call accepts only one resource-identifying parameter.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeEcsClusters>`_    


    **Request Syntax** 
    ::

      response = client.describe_ecs_clusters(
          EcsClusterArns=[
              'string',
          ],
          StackId='string',
          NextToken='string',
          MaxResults=123
      )
    :type EcsClusterArns: list
    :param EcsClusterArns: 

      A list of ARNs, one for each cluster to be described.

      

    
      - *(string) --* 

      
  
    :type StackId: string
    :param StackId: 

      A stack ID. ``DescribeEcsClusters`` returns a description of the cluster that is registered with the stack.

      

    
    :type NextToken: string
    :param NextToken: 

      If the previous paginated request did not return all of the remaining results, the response object's``NextToken`` parameter value is set to a token. To retrieve the next set of results, call ``DescribeEcsClusters`` again and assign that token to the request object's ``NextToken`` parameter. If there are no remaining results, the previous response object's ``NextToken`` parameter is set to ``null`` .

      

    
    :type MaxResults: integer
    :param MaxResults: 

      To receive a paginated response, use this parameter to specify the maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a ``NextToken`` value that you can assign to the ``NextToken`` request parameter to get the next set of results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'EcsClusters': [
                {
                    'EcsClusterArn': 'string',
                    'EcsClusterName': 'string',
                    'StackId': 'string',
                    'RegisteredAt': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``DescribeEcsClusters`` request.

        
        

        - **EcsClusters** *(list) --* 

          A list of ``EcsCluster`` objects containing the cluster descriptions.

          
          

          - *(dict) --* 

            Describes a registered Amazon ECS cluster.

            
            

            - **EcsClusterArn** *(string) --* 

              The cluster's ARN.

              
            

            - **EcsClusterName** *(string) --* 

              The cluster name.

              
            

            - **StackId** *(string) --* 

              The stack ID.

              
            

            - **RegisteredAt** *(string) --* 

              The time and date that the cluster was registered with the stack.

              
        
      
        

        - **NextToken** *(string) --* 

          If a paginated request does not return all of the remaining results, this parameter is set to a token that you can assign to the request object's ``NextToken`` parameter to retrieve the next set of results. If the previous paginated request returned all of the remaining results, this parameter is set to ``null`` .

          
    

  .. py:method:: describe_elastic_ips(**kwargs)

    

    Describes `Elastic IP addresses <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html>`__ .

     

    .. note::

       

      This call accepts only one resource-identifying parameter.

       

     

     **Required Permissions** : To use this action, an IAM user must have a Show, Deploy, or Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeElasticIps>`_    


    **Request Syntax** 
    ::

      response = client.describe_elastic_ips(
          InstanceId='string',
          StackId='string',
          Ips=[
              'string',
          ]
      )
    :type InstanceId: string
    :param InstanceId: 

      The instance ID. If you include this parameter, ``DescribeElasticIps`` returns a description of the Elastic IP addresses associated with the specified instance.

      

    
    :type StackId: string
    :param StackId: 

      A stack ID. If you include this parameter, ``DescribeElasticIps`` returns a description of the Elastic IP addresses that are registered with the specified stack.

      

    
    :type Ips: list
    :param Ips: 

      An array of Elastic IP addresses to be described. If you include this parameter, ``DescribeElasticIps`` returns a description of the specified Elastic IP addresses. Otherwise, it returns a description of every Elastic IP address.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ElasticIps': [
                {
                    'Ip': 'string',
                    'Name': 'string',
                    'Domain': 'string',
                    'Region': 'string',
                    'InstanceId': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``DescribeElasticIps`` request.

        
        

        - **ElasticIps** *(list) --* 

          An ``ElasticIps`` object that describes the specified Elastic IP addresses.

          
          

          - *(dict) --* 

            Describes an Elastic IP address.

            
            

            - **Ip** *(string) --* 

              The IP address.

              
            

            - **Name** *(string) --* 

              The name.

              
            

            - **Domain** *(string) --* 

              The domain.

              
            

            - **Region** *(string) --* 

              The AWS region. For more information, see `Regions and Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html>`__ .

              
            

            - **InstanceId** *(string) --* 

              The ID of the instance that the address is attached to.

              
        
      
    

  .. py:method:: describe_elastic_load_balancers(**kwargs)

    

    Describes a stack's Elastic Load Balancing instances.

     

    .. note::

       

      This call accepts only one resource-identifying parameter.

       

     

     **Required Permissions** : To use this action, an IAM user must have a Show, Deploy, or Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeElasticLoadBalancers>`_    


    **Request Syntax** 
    ::

      response = client.describe_elastic_load_balancers(
          StackId='string',
          LayerIds=[
              'string',
          ]
      )
    :type StackId: string
    :param StackId: 

      A stack ID. The action describes the stack's Elastic Load Balancing instances.

      

    
    :type LayerIds: list
    :param LayerIds: 

      A list of layer IDs. The action describes the Elastic Load Balancing instances for the specified layers.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ElasticLoadBalancers': [
                {
                    'ElasticLoadBalancerName': 'string',
                    'Region': 'string',
                    'DnsName': 'string',
                    'StackId': 'string',
                    'LayerId': 'string',
                    'VpcId': 'string',
                    'AvailabilityZones': [
                        'string',
                    ],
                    'SubnetIds': [
                        'string',
                    ],
                    'Ec2InstanceIds': [
                        'string',
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``DescribeElasticLoadBalancers`` request.

        
        

        - **ElasticLoadBalancers** *(list) --* 

          A list of ``ElasticLoadBalancer`` objects that describe the specified Elastic Load Balancing instances.

          
          

          - *(dict) --* 

            Describes an Elastic Load Balancing instance.

            
            

            - **ElasticLoadBalancerName** *(string) --* 

              The Elastic Load Balancing instance's name.

              
            

            - **Region** *(string) --* 

              The instance's AWS region.

              
            

            - **DnsName** *(string) --* 

              The instance's public DNS name.

              
            

            - **StackId** *(string) --* 

              The ID of the stack that the instance is associated with.

              
            

            - **LayerId** *(string) --* 

              The ID of the layer that the instance is attached to.

              
            

            - **VpcId** *(string) --* 

              The VPC ID.

              
            

            - **AvailabilityZones** *(list) --* 

              A list of Availability Zones.

              
              

              - *(string) --* 
          
            

            - **SubnetIds** *(list) --* 

              A list of subnet IDs, if the stack is running in a VPC.

              
              

              - *(string) --* 
          
            

            - **Ec2InstanceIds** *(list) --* 

              A list of the EC2 instances that the Elastic Load Balancing instance is managing traffic for.

              
              

              - *(string) --* 
          
        
      
    

  .. py:method:: describe_instances(**kwargs)

    

    Requests a description of a set of instances.

     

    .. note::

       

      This call accepts only one resource-identifying parameter.

       

     

     **Required Permissions** : To use this action, an IAM user must have a Show, Deploy, or Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeInstances>`_    


    **Request Syntax** 
    ::

      response = client.describe_instances(
          StackId='string',
          LayerId='string',
          InstanceIds=[
              'string',
          ]
      )
    :type StackId: string
    :param StackId: 

      A stack ID. If you use this parameter, ``DescribeInstances`` returns descriptions of the instances associated with the specified stack.

      

    
    :type LayerId: string
    :param LayerId: 

      A layer ID. If you use this parameter, ``DescribeInstances`` returns descriptions of the instances associated with the specified layer.

      

    
    :type InstanceIds: list
    :param InstanceIds: 

      An array of instance IDs to be described. If you use this parameter, ``DescribeInstances`` returns a description of the specified instances. Otherwise, it returns a description of every instance.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Instances': [
                {
                    'AgentVersion': 'string',
                    'AmiId': 'string',
                    'Architecture': 'x86_64'|'i386',
                    'Arn': 'string',
                    'AutoScalingType': 'load'|'timer',
                    'AvailabilityZone': 'string',
                    'BlockDeviceMappings': [
                        {
                            'DeviceName': 'string',
                            'NoDevice': 'string',
                            'VirtualName': 'string',
                            'Ebs': {
                                'SnapshotId': 'string',
                                'Iops': 123,
                                'VolumeSize': 123,
                                'VolumeType': 'gp2'|'io1'|'standard',
                                'DeleteOnTermination': True|False
                            }
                        },
                    ],
                    'CreatedAt': 'string',
                    'EbsOptimized': True|False,
                    'Ec2InstanceId': 'string',
                    'EcsClusterArn': 'string',
                    'EcsContainerInstanceArn': 'string',
                    'ElasticIp': 'string',
                    'Hostname': 'string',
                    'InfrastructureClass': 'string',
                    'InstallUpdatesOnBoot': True|False,
                    'InstanceId': 'string',
                    'InstanceProfileArn': 'string',
                    'InstanceType': 'string',
                    'LastServiceErrorId': 'string',
                    'LayerIds': [
                        'string',
                    ],
                    'Os': 'string',
                    'Platform': 'string',
                    'PrivateDns': 'string',
                    'PrivateIp': 'string',
                    'PublicDns': 'string',
                    'PublicIp': 'string',
                    'RegisteredBy': 'string',
                    'ReportedAgentVersion': 'string',
                    'ReportedOs': {
                        'Family': 'string',
                        'Name': 'string',
                        'Version': 'string'
                    },
                    'RootDeviceType': 'ebs'|'instance-store',
                    'RootDeviceVolumeId': 'string',
                    'SecurityGroupIds': [
                        'string',
                    ],
                    'SshHostDsaKeyFingerprint': 'string',
                    'SshHostRsaKeyFingerprint': 'string',
                    'SshKeyName': 'string',
                    'StackId': 'string',
                    'Status': 'string',
                    'SubnetId': 'string',
                    'Tenancy': 'string',
                    'VirtualizationType': 'paravirtual'|'hvm'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``DescribeInstances`` request.

        
        

        - **Instances** *(list) --* 

          An array of ``Instance`` objects that describe the instances.

          
          

          - *(dict) --* 

            Describes an instance.

            
            

            - **AgentVersion** *(string) --* 

              The agent version. This parameter is set to ``INHERIT`` if the instance inherits the default stack setting or to a a version number for a fixed agent version.

              
            

            - **AmiId** *(string) --* 

              A custom AMI ID to be used to create the instance. For more information, see `Instances <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-custom-ami.html>`__  

              
            

            - **Architecture** *(string) --* 

              The instance architecture: "i386" or "x86_64".

              
            

            - **Arn** *(string) --* 
            

            - **AutoScalingType** *(string) --* 

              For load-based or time-based instances, the type.

              
            

            - **AvailabilityZone** *(string) --* 

              The instance Availability Zone. For more information, see `Regions and Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html>`__ .

              
            

            - **BlockDeviceMappings** *(list) --* 

              An array of ``BlockDeviceMapping`` objects that specify the instance's block device mappings.

              
              

              - *(dict) --* 

                Describes a block device mapping. This data type maps directly to the Amazon EC2 `BlockDeviceMapping <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BlockDeviceMapping.html>`__ data type. 

                
                

                - **DeviceName** *(string) --* 

                  The device name that is exposed to the instance, such as ``/dev/sdh`` . For the root device, you can use the explicit device name or you can set this parameter to ``ROOT_DEVICE`` and AWS OpsWorks Stacks will provide the correct device name.

                  
                

                - **NoDevice** *(string) --* 

                  Suppresses the specified device included in the AMI's block device mapping.

                  
                

                - **VirtualName** *(string) --* 

                  The virtual device name. For more information, see `BlockDeviceMapping <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BlockDeviceMapping.html>`__ .

                  
                

                - **Ebs** *(dict) --* 

                  An ``EBSBlockDevice`` that defines how to configure an Amazon EBS volume when the instance is launched.

                  
                  

                  - **SnapshotId** *(string) --* 

                    The snapshot ID.

                    
                  

                  - **Iops** *(integer) --* 

                    The number of I/O operations per second (IOPS) that the volume supports. For more information, see `EbsBlockDevice <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EbsBlockDevice.html>`__ .

                    
                  

                  - **VolumeSize** *(integer) --* 

                    The volume size, in GiB. For more information, see `EbsBlockDevice <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EbsBlockDevice.html>`__ .

                    
                  

                  - **VolumeType** *(string) --* 

                    The volume type. ``gp2`` for General Purpose (SSD) volumes, ``io1`` for Provisioned IOPS (SSD) volumes, and ``standard`` for Magnetic volumes.

                    
                  

                  - **DeleteOnTermination** *(boolean) --* 

                    Whether the volume is deleted on instance termination.

                    
              
            
          
            

            - **CreatedAt** *(string) --* 

              The time that the instance was created.

              
            

            - **EbsOptimized** *(boolean) --* 

              Whether this is an Amazon EBS-optimized instance.

              
            

            - **Ec2InstanceId** *(string) --* 

              The ID of the associated Amazon EC2 instance.

              
            

            - **EcsClusterArn** *(string) --* 

              For container instances, the Amazon ECS cluster's ARN.

              
            

            - **EcsContainerInstanceArn** *(string) --* 

              For container instances, the instance's ARN.

              
            

            - **ElasticIp** *(string) --* 

              The instance `Elastic IP address <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html>`__ .

              
            

            - **Hostname** *(string) --* 

              The instance host name.

              
            

            - **InfrastructureClass** *(string) --* 

              For registered instances, the infrastructure class: ``ec2`` or ``on-premises`` .

              
            

            - **InstallUpdatesOnBoot** *(boolean) --* 

              Whether to install operating system and package updates when the instance boots. The default value is ``true`` . If this value is set to ``false`` , you must then update your instances manually by using  CreateDeployment to run the ``update_dependencies`` stack command or by manually running ``yum`` (Amazon Linux) or ``apt-get`` (Ubuntu) on the instances. 

               

              .. note::

                 

                We strongly recommend using the default value of ``true`` , to ensure that your instances have the latest security updates.

                 

              
            

            - **InstanceId** *(string) --* 

              The instance ID.

              
            

            - **InstanceProfileArn** *(string) --* 

              The ARN of the instance's IAM profile. For more information about IAM ARNs, see `Using Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ .

              
            

            - **InstanceType** *(string) --* 

              The instance type, such as ``t2.micro`` .

              
            

            - **LastServiceErrorId** *(string) --* 

              The ID of the last service error. For more information, call  DescribeServiceErrors .

              
            

            - **LayerIds** *(list) --* 

              An array containing the instance layer IDs.

              
              

              - *(string) --* 
          
            

            - **Os** *(string) --* 

              The instance's operating system.

              
            

            - **Platform** *(string) --* 

              The instance's platform.

              
            

            - **PrivateDns** *(string) --* 

              The instance's private DNS name.

              
            

            - **PrivateIp** *(string) --* 

              The instance's private IP address.

              
            

            - **PublicDns** *(string) --* 

              The instance public DNS name.

              
            

            - **PublicIp** *(string) --* 

              The instance public IP address.

              
            

            - **RegisteredBy** *(string) --* 

              For registered instances, who performed the registration.

              
            

            - **ReportedAgentVersion** *(string) --* 

              The instance's reported AWS OpsWorks Stacks agent version.

              
            

            - **ReportedOs** *(dict) --* 

              For registered instances, the reported operating system.

              
              

              - **Family** *(string) --* 

                The operating system family.

                
              

              - **Name** *(string) --* 

                The operating system name.

                
              

              - **Version** *(string) --* 

                The operating system version.

                
          
            

            - **RootDeviceType** *(string) --* 

              The instance's root device type. For more information, see `Storage for the Root Device <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-for-the-root-device>`__ .

              
            

            - **RootDeviceVolumeId** *(string) --* 

              The root device volume ID.

              
            

            - **SecurityGroupIds** *(list) --* 

              An array containing the instance security group IDs.

              
              

              - *(string) --* 
          
            

            - **SshHostDsaKeyFingerprint** *(string) --* 

              The SSH key's Deep Security Agent (DSA) fingerprint.

              
            

            - **SshHostRsaKeyFingerprint** *(string) --* 

              The SSH key's RSA fingerprint.

              
            

            - **SshKeyName** *(string) --* 

              The instance's Amazon EC2 key-pair name.

              
            

            - **StackId** *(string) --* 

              The stack ID.

              
            

            - **Status** *(string) --* 

              The instance status:

               

               
              * ``booting``   
               
              * ``connection_lost``   
               
              * ``online``   
               
              * ``pending``   
               
              * ``rebooting``   
               
              * ``requested``   
               
              * ``running_setup``   
               
              * ``setup_failed``   
               
              * ``shutting_down``   
               
              * ``start_failed``   
               
              * ``stop_failed``   
               
              * ``stopped``   
               
              * ``stopping``   
               
              * ``terminated``   
               
              * ``terminating``   
               

              
            

            - **SubnetId** *(string) --* 

              The instance's subnet ID; applicable only if the stack is running in a VPC.

              
            

            - **Tenancy** *(string) --* 

              The instance's tenancy option, such as ``dedicated`` or ``host`` .

              
            

            - **VirtualizationType** *(string) --* 

              The instance's virtualization type: ``paravirtual`` or ``hvm`` .

              
        
      
    

  .. py:method:: describe_layers(**kwargs)

    

    Requests a description of one or more layers in a specified stack.

     

    .. note::

       

      This call accepts only one resource-identifying parameter.

       

     

     **Required Permissions** : To use this action, an IAM user must have a Show, Deploy, or Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeLayers>`_    


    **Request Syntax** 
    ::

      response = client.describe_layers(
          StackId='string',
          LayerIds=[
              'string',
          ]
      )
    :type StackId: string
    :param StackId: 

      The stack ID.

      

    
    :type LayerIds: list
    :param LayerIds: 

      An array of layer IDs that specify the layers to be described. If you omit this parameter, ``DescribeLayers`` returns a description of every layer in the specified stack.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Layers': [
                {
                    'Arn': 'string',
                    'StackId': 'string',
                    'LayerId': 'string',
                    'Type': 'aws-flow-ruby'|'ecs-cluster'|'java-app'|'lb'|'web'|'php-app'|'rails-app'|'nodejs-app'|'memcached'|'db-master'|'monitoring-master'|'custom',
                    'Name': 'string',
                    'Shortname': 'string',
                    'Attributes': {
                        'string': 'string'
                    },
                    'CloudWatchLogsConfiguration': {
                        'Enabled': True|False,
                        'LogStreams': [
                            {
                                'LogGroupName': 'string',
                                'DatetimeFormat': 'string',
                                'TimeZone': 'LOCAL'|'UTC',
                                'File': 'string',
                                'FileFingerprintLines': 'string',
                                'MultiLineStartPattern': 'string',
                                'InitialPosition': 'start_of_file'|'end_of_file',
                                'Encoding': 'ascii'|'big5'|'big5hkscs'|'cp037'|'cp424'|'cp437'|'cp500'|'cp720'|'cp737'|'cp775'|'cp850'|'cp852'|'cp855'|'cp856'|'cp857'|'cp858'|'cp860'|'cp861'|'cp862'|'cp863'|'cp864'|'cp865'|'cp866'|'cp869'|'cp874'|'cp875'|'cp932'|'cp949'|'cp950'|'cp1006'|'cp1026'|'cp1140'|'cp1250'|'cp1251'|'cp1252'|'cp1253'|'cp1254'|'cp1255'|'cp1256'|'cp1257'|'cp1258'|'euc_jp'|'euc_jis_2004'|'euc_jisx0213'|'euc_kr'|'gb2312'|'gbk'|'gb18030'|'hz'|'iso2022_jp'|'iso2022_jp_1'|'iso2022_jp_2'|'iso2022_jp_2004'|'iso2022_jp_3'|'iso2022_jp_ext'|'iso2022_kr'|'latin_1'|'iso8859_2'|'iso8859_3'|'iso8859_4'|'iso8859_5'|'iso8859_6'|'iso8859_7'|'iso8859_8'|'iso8859_9'|'iso8859_10'|'iso8859_13'|'iso8859_14'|'iso8859_15'|'iso8859_16'|'johab'|'koi8_r'|'koi8_u'|'mac_cyrillic'|'mac_greek'|'mac_iceland'|'mac_latin2'|'mac_roman'|'mac_turkish'|'ptcp154'|'shift_jis'|'shift_jis_2004'|'shift_jisx0213'|'utf_32'|'utf_32_be'|'utf_32_le'|'utf_16'|'utf_16_be'|'utf_16_le'|'utf_7'|'utf_8'|'utf_8_sig',
                                'BufferDuration': 123,
                                'BatchCount': 123,
                                'BatchSize': 123
                            },
                        ]
                    },
                    'CustomInstanceProfileArn': 'string',
                    'CustomJson': 'string',
                    'CustomSecurityGroupIds': [
                        'string',
                    ],
                    'DefaultSecurityGroupNames': [
                        'string',
                    ],
                    'Packages': [
                        'string',
                    ],
                    'VolumeConfigurations': [
                        {
                            'MountPoint': 'string',
                            'RaidLevel': 123,
                            'NumberOfDisks': 123,
                            'Size': 123,
                            'VolumeType': 'string',
                            'Iops': 123
                        },
                    ],
                    'EnableAutoHealing': True|False,
                    'AutoAssignElasticIps': True|False,
                    'AutoAssignPublicIps': True|False,
                    'DefaultRecipes': {
                        'Setup': [
                            'string',
                        ],
                        'Configure': [
                            'string',
                        ],
                        'Deploy': [
                            'string',
                        ],
                        'Undeploy': [
                            'string',
                        ],
                        'Shutdown': [
                            'string',
                        ]
                    },
                    'CustomRecipes': {
                        'Setup': [
                            'string',
                        ],
                        'Configure': [
                            'string',
                        ],
                        'Deploy': [
                            'string',
                        ],
                        'Undeploy': [
                            'string',
                        ],
                        'Shutdown': [
                            'string',
                        ]
                    },
                    'CreatedAt': 'string',
                    'InstallUpdatesOnBoot': True|False,
                    'UseEbsOptimizedInstances': True|False,
                    'LifecycleEventConfiguration': {
                        'Shutdown': {
                            'ExecutionTimeout': 123,
                            'DelayUntilElbConnectionsDrained': True|False
                        }
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``DescribeLayers`` request.

        
        

        - **Layers** *(list) --* 

          An array of ``Layer`` objects that describe the layers.

          
          

          - *(dict) --* 

            Describes a layer.

            
            

            - **Arn** *(string) --* 
            

            - **StackId** *(string) --* 

              The layer stack ID.

              
            

            - **LayerId** *(string) --* 

              The layer ID.

              
            

            - **Type** *(string) --* 

              The layer type.

              
            

            - **Name** *(string) --* 

              The layer name.

              
            

            - **Shortname** *(string) --* 

              The layer short name.

              
            

            - **Attributes** *(dict) --* 

              The layer attributes.

               

              For the ``HaproxyStatsPassword`` , ``MysqlRootPassword`` , and ``GangliaPassword`` attributes, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value

               

              For an ECS Cluster layer, AWS OpsWorks Stacks the ``EcsClusterArn`` attribute is set to the cluster's ARN.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **CloudWatchLogsConfiguration** *(dict) --* 

              The Amazon CloudWatch Logs configuration settings for the layer.

              
              

              - **Enabled** *(boolean) --* 

                Whether CloudWatch Logs is enabled for a layer.

                
              

              - **LogStreams** *(list) --* 

                A list of configuration options for CloudWatch Logs.

                
                

                - *(dict) --* 

                  Describes the Amazon CloudWatch logs configuration for a layer. For detailed information about members of this data type, see the `CloudWatch Logs Agent Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html>`__ .

                  
                  

                  - **LogGroupName** *(string) --* 

                    Specifies the destination log group. A log group is created automatically if it doesn't already exist. Log group names can be between 1 and 512 characters long. Allowed characters include a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), '/' (forward slash), and '.' (period).

                    
                  

                  - **DatetimeFormat** *(string) --* 

                    Specifies how the time stamp is extracted from logs. For more information, see the `CloudWatch Logs Agent Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html>`__ .

                    
                  

                  - **TimeZone** *(string) --* 

                    Specifies the time zone of log event time stamps.

                    
                  

                  - **File** *(string) --* 

                    Specifies log files that you want to push to CloudWatch Logs.

                     

                     ``File`` can point to a specific file or multiple files (by using wild card characters such as ``/var/log/system.log*`` ). Only the latest file is pushed to CloudWatch Logs, based on file modification time. We recommend that you use wild card characters to specify a series of files of the same type, such as ``access_log.2014-06-01-01`` , ``access_log.2014-06-01-02`` , and so on by using a pattern like ``access_log.*`` . Don't use a wildcard to match multiple file types, such as ``access_log_80`` and ``access_log_443`` . To specify multiple, different file types, add another log stream entry to the configuration file, so that each log file type is stored in a different log group.

                     

                    Zipped files are not supported.

                    
                  

                  - **FileFingerprintLines** *(string) --* 

                    Specifies the range of lines for identifying a file. The valid values are one number, or two dash-delimited numbers, such as '1', '2-5'. The default value is '1', meaning the first line is used to calculate the fingerprint. Fingerprint lines are not sent to CloudWatch Logs unless all specified lines are available.

                    
                  

                  - **MultiLineStartPattern** *(string) --* 

                    Specifies the pattern for identifying the start of a log message.

                    
                  

                  - **InitialPosition** *(string) --* 

                    Specifies where to start to read data (start_of_file or end_of_file). The default is start_of_file. This setting is only used if there is no state persisted for that log stream.

                    
                  

                  - **Encoding** *(string) --* 

                    Specifies the encoding of the log file so that the file can be read correctly. The default is ``utf_8`` . Encodings supported by Python ``codecs.decode()`` can be used here.

                    
                  

                  - **BufferDuration** *(integer) --* 

                    Specifies the time duration for the batching of log events. The minimum value is 5000ms and default value is 5000ms.

                    
                  

                  - **BatchCount** *(integer) --* 

                    Specifies the max number of log events in a batch, up to 10000. The default value is 1000.

                    
                  

                  - **BatchSize** *(integer) --* 

                    Specifies the maximum size of log events in a batch, in bytes, up to 1048576 bytes. The default value is 32768 bytes. This size is calculated as the sum of all event messages in UTF-8, plus 26 bytes for each log event.

                    
              
            
          
            

            - **CustomInstanceProfileArn** *(string) --* 

              The ARN of the default IAM profile to be used for the layer's EC2 instances. For more information about IAM ARNs, see `Using Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ .

              
            

            - **CustomJson** *(string) --* 

              A JSON formatted string containing the layer's custom stack configuration and deployment attributes.

              
            

            - **CustomSecurityGroupIds** *(list) --* 

              An array containing the layer's custom security group IDs.

              
              

              - *(string) --* 
          
            

            - **DefaultSecurityGroupNames** *(list) --* 

              An array containing the layer's security group names.

              
              

              - *(string) --* 
          
            

            - **Packages** *(list) --* 

              An array of ``Package`` objects that describe the layer's packages.

              
              

              - *(string) --* 
          
            

            - **VolumeConfigurations** *(list) --* 

              A ``VolumeConfigurations`` object that describes the layer's Amazon EBS volumes.

              
              

              - *(dict) --* 

                Describes an Amazon EBS volume configuration.

                
                

                - **MountPoint** *(string) --* 

                  The volume mount point. For example "/dev/sdh".

                  
                

                - **RaidLevel** *(integer) --* 

                  The volume `RAID level <http://en.wikipedia.org/wiki/Standard_RAID_levels>`__ .

                  
                

                - **NumberOfDisks** *(integer) --* 

                  The number of disks in the volume.

                  
                

                - **Size** *(integer) --* 

                  The volume size.

                  
                

                - **VolumeType** *(string) --* 

                  The volume type:

                   

                   
                  * ``standard`` - Magnetic 
                   
                  * ``io1`` - Provisioned IOPS (SSD) 
                   
                  * ``gp2`` - General Purpose (SSD) 
                   

                  
                

                - **Iops** *(integer) --* 

                  For PIOPS volumes, the IOPS per disk.

                  
            
          
            

            - **EnableAutoHealing** *(boolean) --* 

              Whether auto healing is disabled for the layer.

              
            

            - **AutoAssignElasticIps** *(boolean) --* 

              Whether to automatically assign an `Elastic IP address <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html>`__ to the layer's instances. For more information, see `How to Edit a Layer <http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-edit.html>`__ .

              
            

            - **AutoAssignPublicIps** *(boolean) --* 

              For stacks that are running in a VPC, whether to automatically assign a public IP address to the layer's instances. For more information, see `How to Edit a Layer <http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-edit.html>`__ .

              
            

            - **DefaultRecipes** *(dict) --* 

              AWS OpsWorks Stacks supports five lifecycle events: **setup** , **configuration** , **deploy** , **undeploy** , and **shutdown** . For each layer, AWS OpsWorks Stacks runs a set of standard recipes for each event. In addition, you can provide custom recipes for any or all layers and events. AWS OpsWorks Stacks runs custom event recipes after the standard recipes. ``LayerCustomRecipes`` specifies the custom recipes for a particular layer to be run in response to each of the five events. 

               

              To specify a recipe, use the cookbook's directory name in the repository followed by two colons and the recipe name, which is the recipe's file name without the .rb extension. For example: phpapp2::dbsetup specifies the dbsetup.rb recipe in the repository's phpapp2 folder.

              
              

              - **Setup** *(list) --* 

                An array of custom recipe names to be run following a ``setup`` event.

                
                

                - *(string) --* 
            
              

              - **Configure** *(list) --* 

                An array of custom recipe names to be run following a ``configure`` event.

                
                

                - *(string) --* 
            
              

              - **Deploy** *(list) --* 

                An array of custom recipe names to be run following a ``deploy`` event.

                
                

                - *(string) --* 
            
              

              - **Undeploy** *(list) --* 

                An array of custom recipe names to be run following a ``undeploy`` event.

                
                

                - *(string) --* 
            
              

              - **Shutdown** *(list) --* 

                An array of custom recipe names to be run following a ``shutdown`` event.

                
                

                - *(string) --* 
            
          
            

            - **CustomRecipes** *(dict) --* 

              A ``LayerCustomRecipes`` object that specifies the layer's custom recipes.

              
              

              - **Setup** *(list) --* 

                An array of custom recipe names to be run following a ``setup`` event.

                
                

                - *(string) --* 
            
              

              - **Configure** *(list) --* 

                An array of custom recipe names to be run following a ``configure`` event.

                
                

                - *(string) --* 
            
              

              - **Deploy** *(list) --* 

                An array of custom recipe names to be run following a ``deploy`` event.

                
                

                - *(string) --* 
            
              

              - **Undeploy** *(list) --* 

                An array of custom recipe names to be run following a ``undeploy`` event.

                
                

                - *(string) --* 
            
              

              - **Shutdown** *(list) --* 

                An array of custom recipe names to be run following a ``shutdown`` event.

                
                

                - *(string) --* 
            
          
            

            - **CreatedAt** *(string) --* 

              Date when the layer was created.

              
            

            - **InstallUpdatesOnBoot** *(boolean) --* 

              Whether to install operating system and package updates when the instance boots. The default value is ``true`` . If this value is set to ``false`` , you must then update your instances manually by using  CreateDeployment to run the ``update_dependencies`` stack command or manually running ``yum`` (Amazon Linux) or ``apt-get`` (Ubuntu) on the instances. 

               

              .. note::

                 

                We strongly recommend using the default value of ``true`` , to ensure that your instances have the latest security updates.

                 

              
            

            - **UseEbsOptimizedInstances** *(boolean) --* 

              Whether the layer uses Amazon EBS-optimized instances.

              
            

            - **LifecycleEventConfiguration** *(dict) --* 

              A ``LifeCycleEventConfiguration`` object that specifies the Shutdown event configuration.

              
              

              - **Shutdown** *(dict) --* 

                A ``ShutdownEventConfiguration`` object that specifies the Shutdown event configuration.

                
                

                - **ExecutionTimeout** *(integer) --* 

                  The time, in seconds, that AWS OpsWorks Stacks will wait after triggering a Shutdown event before shutting down an instance.

                  
                

                - **DelayUntilElbConnectionsDrained** *(boolean) --* 

                  Whether to enable Elastic Load Balancing connection draining. For more information, see `Connection Draining <http://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/TerminologyandKeyConcepts.html#conn-drain>`__  

                  
            
          
        
      
    

  .. py:method:: describe_load_based_auto_scaling(**kwargs)

    

    Describes load-based auto scaling configurations for specified layers.

     

    .. note::

       

      You must specify at least one of the parameters.

       

     

     **Required Permissions** : To use this action, an IAM user must have a Show, Deploy, or Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeLoadBasedAutoScaling>`_    


    **Request Syntax** 
    ::

      response = client.describe_load_based_auto_scaling(
          LayerIds=[
              'string',
          ]
      )
    :type LayerIds: list
    :param LayerIds: **[REQUIRED]** 

      An array of layer IDs.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'LoadBasedAutoScalingConfigurations': [
                {
                    'LayerId': 'string',
                    'Enable': True|False,
                    'UpScaling': {
                        'InstanceCount': 123,
                        'ThresholdsWaitTime': 123,
                        'IgnoreMetricsTime': 123,
                        'CpuThreshold': 123.0,
                        'MemoryThreshold': 123.0,
                        'LoadThreshold': 123.0,
                        'Alarms': [
                            'string',
                        ]
                    },
                    'DownScaling': {
                        'InstanceCount': 123,
                        'ThresholdsWaitTime': 123,
                        'IgnoreMetricsTime': 123,
                        'CpuThreshold': 123.0,
                        'MemoryThreshold': 123.0,
                        'LoadThreshold': 123.0,
                        'Alarms': [
                            'string',
                        ]
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``DescribeLoadBasedAutoScaling`` request.

        
        

        - **LoadBasedAutoScalingConfigurations** *(list) --* 

          An array of ``LoadBasedAutoScalingConfiguration`` objects that describe each layer's configuration.

          
          

          - *(dict) --* 

            Describes a layer's load-based auto scaling configuration.

            
            

            - **LayerId** *(string) --* 

              The layer ID.

              
            

            - **Enable** *(boolean) --* 

              Whether load-based auto scaling is enabled for the layer.

              
            

            - **UpScaling** *(dict) --* 

              An ``AutoScalingThresholds`` object that describes the upscaling configuration, which defines how and when AWS OpsWorks Stacks increases the number of instances.

              
              

              - **InstanceCount** *(integer) --* 

                The number of instances to add or remove when the load exceeds a threshold.

                
              

              - **ThresholdsWaitTime** *(integer) --* 

                The amount of time, in minutes, that the load must exceed a threshold before more instances are added or removed.

                
              

              - **IgnoreMetricsTime** *(integer) --* 

                The amount of time (in minutes) after a scaling event occurs that AWS OpsWorks Stacks should ignore metrics and suppress additional scaling events. For example, AWS OpsWorks Stacks adds new instances following an upscaling event but the instances won't start reducing the load until they have been booted and configured. There is no point in raising additional scaling events during that operation, which typically takes several minutes. ``IgnoreMetricsTime`` allows you to direct AWS OpsWorks Stacks to suppress scaling events long enough to get the new instances online.

                
              

              - **CpuThreshold** *(float) --* 

                The CPU utilization threshold, as a percent of the available CPU. A value of -1 disables the threshold.

                
              

              - **MemoryThreshold** *(float) --* 

                The memory utilization threshold, as a percent of the available memory. A value of -1 disables the threshold.

                
              

              - **LoadThreshold** *(float) --* 

                The load threshold. A value of -1 disables the threshold. For more information about how load is computed, see `Load (computing) <http://en.wikipedia.org/wiki/Load_%28computing%29>`__ .

                
              

              - **Alarms** *(list) --* 

                Custom Cloudwatch auto scaling alarms, to be used as thresholds. This parameter takes a list of up to five alarm names, which are case sensitive and must be in the same region as the stack.

                 

                .. note::

                   

                  To use custom alarms, you must update your service role to allow ``cloudwatch:DescribeAlarms`` . You can either have AWS OpsWorks Stacks update the role for you when you first use this feature or you can edit the role manually. For more information, see `Allowing AWS OpsWorks Stacks to Act on Your Behalf <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-servicerole.html>`__ .

                   

                
                

                - *(string) --* 
            
          
            

            - **DownScaling** *(dict) --* 

              An ``AutoScalingThresholds`` object that describes the downscaling configuration, which defines how and when AWS OpsWorks Stacks reduces the number of instances.

              
              

              - **InstanceCount** *(integer) --* 

                The number of instances to add or remove when the load exceeds a threshold.

                
              

              - **ThresholdsWaitTime** *(integer) --* 

                The amount of time, in minutes, that the load must exceed a threshold before more instances are added or removed.

                
              

              - **IgnoreMetricsTime** *(integer) --* 

                The amount of time (in minutes) after a scaling event occurs that AWS OpsWorks Stacks should ignore metrics and suppress additional scaling events. For example, AWS OpsWorks Stacks adds new instances following an upscaling event but the instances won't start reducing the load until they have been booted and configured. There is no point in raising additional scaling events during that operation, which typically takes several minutes. ``IgnoreMetricsTime`` allows you to direct AWS OpsWorks Stacks to suppress scaling events long enough to get the new instances online.

                
              

              - **CpuThreshold** *(float) --* 

                The CPU utilization threshold, as a percent of the available CPU. A value of -1 disables the threshold.

                
              

              - **MemoryThreshold** *(float) --* 

                The memory utilization threshold, as a percent of the available memory. A value of -1 disables the threshold.

                
              

              - **LoadThreshold** *(float) --* 

                The load threshold. A value of -1 disables the threshold. For more information about how load is computed, see `Load (computing) <http://en.wikipedia.org/wiki/Load_%28computing%29>`__ .

                
              

              - **Alarms** *(list) --* 

                Custom Cloudwatch auto scaling alarms, to be used as thresholds. This parameter takes a list of up to five alarm names, which are case sensitive and must be in the same region as the stack.

                 

                .. note::

                   

                  To use custom alarms, you must update your service role to allow ``cloudwatch:DescribeAlarms`` . You can either have AWS OpsWorks Stacks update the role for you when you first use this feature or you can edit the role manually. For more information, see `Allowing AWS OpsWorks Stacks to Act on Your Behalf <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-servicerole.html>`__ .

                   

                
                

                - *(string) --* 
            
          
        
      
    

  .. py:method:: describe_my_user_profile()

    

    Describes a user's SSH information.

     

     **Required Permissions** : To use this action, an IAM user must have self-management enabled or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeMyUserProfile>`_    


    **Request Syntax** 

    ::

      response = client.describe_my_user_profile()
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UserProfile': {
                'IamUserArn': 'string',
                'Name': 'string',
                'SshUsername': 'string',
                'SshPublicKey': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``DescribeMyUserProfile`` request.

        
        

        - **UserProfile** *(dict) --* 

          A ``UserProfile`` object that describes the user's SSH information.

          
          

          - **IamUserArn** *(string) --* 

            The user's IAM ARN.

            
          

          - **Name** *(string) --* 

            The user's name.

            
          

          - **SshUsername** *(string) --* 

            The user's SSH user name.

            
          

          - **SshPublicKey** *(string) --* 

            The user's SSH public key.

            
      
    

  .. py:method:: describe_permissions(**kwargs)

    

    Describes the permissions for a specified stack.

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribePermissions>`_    


    **Request Syntax** 
    ::

      response = client.describe_permissions(
          IamUserArn='string',
          StackId='string'
      )
    :type IamUserArn: string
    :param IamUserArn: 

      The user's IAM ARN. This can also be a federated user's ARN. For more information about IAM ARNs, see `Using Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ .

      

    
    :type StackId: string
    :param StackId: 

      The stack ID.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Permissions': [
                {
                    'StackId': 'string',
                    'IamUserArn': 'string',
                    'AllowSsh': True|False,
                    'AllowSudo': True|False,
                    'Level': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``DescribePermissions`` request.

        
        

        - **Permissions** *(list) --* 

          An array of ``Permission`` objects that describe the stack permissions.

           

           
          * If the request object contains only a stack ID, the array contains a ``Permission`` object with permissions for each of the stack IAM ARNs. 
           
          * If the request object contains only an IAM ARN, the array contains a ``Permission`` object with permissions for each of the user's stack IDs. 
           
          * If the request contains a stack ID and an IAM ARN, the array contains a single ``Permission`` object with permissions for the specified stack and IAM ARN. 
           

          
          

          - *(dict) --* 

            Describes stack or user permissions.

            
            

            - **StackId** *(string) --* 

              A stack ID.

              
            

            - **IamUserArn** *(string) --* 

              The Amazon Resource Name (ARN) for an AWS Identity and Access Management (IAM) role. For more information about IAM ARNs, see `Using Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ .

              
            

            - **AllowSsh** *(boolean) --* 

              Whether the user can use SSH.

              
            

            - **AllowSudo** *(boolean) --* 

              Whether the user can use **sudo** .

              
            

            - **Level** *(string) --* 

              The user's permission level, which must be the following:

               

               
              * ``deny``   
               
              * ``show``   
               
              * ``deploy``   
               
              * ``manage``   
               
              * ``iam_only``   
               

               

              For more information on the permissions associated with these levels, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__  

              
        
      
    

  .. py:method:: describe_raid_arrays(**kwargs)

    

    Describe an instance's RAID arrays.

     

    .. note::

       

      This call accepts only one resource-identifying parameter.

       

     

     **Required Permissions** : To use this action, an IAM user must have a Show, Deploy, or Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeRaidArrays>`_    


    **Request Syntax** 
    ::

      response = client.describe_raid_arrays(
          InstanceId='string',
          StackId='string',
          RaidArrayIds=[
              'string',
          ]
      )
    :type InstanceId: string
    :param InstanceId: 

      The instance ID. If you use this parameter, ``DescribeRaidArrays`` returns descriptions of the RAID arrays associated with the specified instance. 

      

    
    :type StackId: string
    :param StackId: 

      The stack ID.

      

    
    :type RaidArrayIds: list
    :param RaidArrayIds: 

      An array of RAID array IDs. If you use this parameter, ``DescribeRaidArrays`` returns descriptions of the specified arrays. Otherwise, it returns a description of every array.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'RaidArrays': [
                {
                    'RaidArrayId': 'string',
                    'InstanceId': 'string',
                    'Name': 'string',
                    'RaidLevel': 123,
                    'NumberOfDisks': 123,
                    'Size': 123,
                    'Device': 'string',
                    'MountPoint': 'string',
                    'AvailabilityZone': 'string',
                    'CreatedAt': 'string',
                    'StackId': 'string',
                    'VolumeType': 'string',
                    'Iops': 123
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``DescribeRaidArrays`` request.

        
        

        - **RaidArrays** *(list) --* 

          A ``RaidArrays`` object that describes the specified RAID arrays.

          
          

          - *(dict) --* 

            Describes an instance's RAID array.

            
            

            - **RaidArrayId** *(string) --* 

              The array ID.

              
            

            - **InstanceId** *(string) --* 

              The instance ID.

              
            

            - **Name** *(string) --* 

              The array name.

              
            

            - **RaidLevel** *(integer) --* 

              The `RAID level <http://en.wikipedia.org/wiki/Standard_RAID_levels>`__ .

              
            

            - **NumberOfDisks** *(integer) --* 

              The number of disks in the array.

              
            

            - **Size** *(integer) --* 

              The array's size.

              
            

            - **Device** *(string) --* 

              The array's Linux device. For example /dev/mdadm0.

              
            

            - **MountPoint** *(string) --* 

              The array's mount point.

              
            

            - **AvailabilityZone** *(string) --* 

              The array's Availability Zone. For more information, see `Regions and Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html>`__ .

              
            

            - **CreatedAt** *(string) --* 

              When the RAID array was created.

              
            

            - **StackId** *(string) --* 

              The stack ID.

              
            

            - **VolumeType** *(string) --* 

              The volume type, standard or PIOPS.

              
            

            - **Iops** *(integer) --* 

              For PIOPS volumes, the IOPS per disk.

              
        
      
    

  .. py:method:: describe_rds_db_instances(**kwargs)

    

    Describes Amazon RDS instances.

     

     **Required Permissions** : To use this action, an IAM user must have a Show, Deploy, or Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

     

    This call accepts only one resource-identifying parameter.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeRdsDbInstances>`_    


    **Request Syntax** 
    ::

      response = client.describe_rds_db_instances(
          StackId='string',
          RdsDbInstanceArns=[
              'string',
          ]
      )
    :type StackId: string
    :param StackId: **[REQUIRED]** 

      The stack ID that the instances are registered with. The operation returns descriptions of all registered Amazon RDS instances.

      

    
    :type RdsDbInstanceArns: list
    :param RdsDbInstanceArns: 

      An array containing the ARNs of the instances to be described.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'RdsDbInstances': [
                {
                    'RdsDbInstanceArn': 'string',
                    'DbInstanceIdentifier': 'string',
                    'DbUser': 'string',
                    'DbPassword': 'string',
                    'Region': 'string',
                    'Address': 'string',
                    'Engine': 'string',
                    'StackId': 'string',
                    'MissingOnRds': True|False
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``DescribeRdsDbInstances`` request.

        
        

        - **RdsDbInstances** *(list) --* 

          An a array of ``RdsDbInstance`` objects that describe the instances.

          
          

          - *(dict) --* 

            Describes an Amazon RDS instance.

            
            

            - **RdsDbInstanceArn** *(string) --* 

              The instance's ARN.

              
            

            - **DbInstanceIdentifier** *(string) --* 

              The DB instance identifier.

              
            

            - **DbUser** *(string) --* 

              The master user name.

              
            

            - **DbPassword** *(string) --* 

              AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

              
            

            - **Region** *(string) --* 

              The instance's AWS region.

              
            

            - **Address** *(string) --* 

              The instance's address.

              
            

            - **Engine** *(string) --* 

              The instance's database engine.

              
            

            - **StackId** *(string) --* 

              The ID of the stack with which the instance is registered.

              
            

            - **MissingOnRds** *(boolean) --* 

              Set to ``true`` if AWS OpsWorks Stacks is unable to discover the Amazon RDS instance. AWS OpsWorks Stacks attempts to discover the instance only once. If this value is set to ``true`` , you must deregister the instance, and then register it again.

              
        
      
    

  .. py:method:: describe_service_errors(**kwargs)

    

    Describes AWS OpsWorks Stacks service errors.

     

     **Required Permissions** : To use this action, an IAM user must have a Show, Deploy, or Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

     

    This call accepts only one resource-identifying parameter.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeServiceErrors>`_    


    **Request Syntax** 
    ::

      response = client.describe_service_errors(
          StackId='string',
          InstanceId='string',
          ServiceErrorIds=[
              'string',
          ]
      )
    :type StackId: string
    :param StackId: 

      The stack ID. If you use this parameter, ``DescribeServiceErrors`` returns descriptions of the errors associated with the specified stack.

      

    
    :type InstanceId: string
    :param InstanceId: 

      The instance ID. If you use this parameter, ``DescribeServiceErrors`` returns descriptions of the errors associated with the specified instance.

      

    
    :type ServiceErrorIds: list
    :param ServiceErrorIds: 

      An array of service error IDs. If you use this parameter, ``DescribeServiceErrors`` returns descriptions of the specified errors. Otherwise, it returns a description of every error.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ServiceErrors': [
                {
                    'ServiceErrorId': 'string',
                    'StackId': 'string',
                    'InstanceId': 'string',
                    'Type': 'string',
                    'Message': 'string',
                    'CreatedAt': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``DescribeServiceErrors`` request.

        
        

        - **ServiceErrors** *(list) --* 

          An array of ``ServiceError`` objects that describe the specified service errors.

          
          

          - *(dict) --* 

            Describes an AWS OpsWorks Stacks service error.

            
            

            - **ServiceErrorId** *(string) --* 

              The error ID.

              
            

            - **StackId** *(string) --* 

              The stack ID.

              
            

            - **InstanceId** *(string) --* 

              The instance ID.

              
            

            - **Type** *(string) --* 

              The error type.

              
            

            - **Message** *(string) --* 

              A message that describes the error.

              
            

            - **CreatedAt** *(string) --* 

              When the error occurred.

              
        
      
    

  .. py:method:: describe_stack_provisioning_parameters(**kwargs)

    

    Requests a description of a stack's provisioning parameters.

     

     **Required Permissions** : To use this action, an IAM user must have a Show, Deploy, or Manage permissions level for the stack or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeStackProvisioningParameters>`_    


    **Request Syntax** 
    ::

      response = client.describe_stack_provisioning_parameters(
          StackId='string'
      )
    :type StackId: string
    :param StackId: **[REQUIRED]** 

      The stack ID

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AgentInstallerUrl': 'string',
            'Parameters': {
                'string': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``DescribeStackProvisioningParameters`` request.

        
        

        - **AgentInstallerUrl** *(string) --* 

          The AWS OpsWorks Stacks agent installer's URL.

          
        

        - **Parameters** *(dict) --* 

          An embedded object that contains the provisioning parameters.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
    

  .. py:method:: describe_stack_summary(**kwargs)

    

    Describes the number of layers and apps in a specified stack, and the number of instances in each state, such as ``running_setup`` or ``online`` .

     

     **Required Permissions** : To use this action, an IAM user must have a Show, Deploy, or Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeStackSummary>`_    


    **Request Syntax** 
    ::

      response = client.describe_stack_summary(
          StackId='string'
      )
    :type StackId: string
    :param StackId: **[REQUIRED]** 

      The stack ID.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'StackSummary': {
                'StackId': 'string',
                'Name': 'string',
                'Arn': 'string',
                'LayersCount': 123,
                'AppsCount': 123,
                'InstancesCount': {
                    'Assigning': 123,
                    'Booting': 123,
                    'ConnectionLost': 123,
                    'Deregistering': 123,
                    'Online': 123,
                    'Pending': 123,
                    'Rebooting': 123,
                    'Registered': 123,
                    'Registering': 123,
                    'Requested': 123,
                    'RunningSetup': 123,
                    'SetupFailed': 123,
                    'ShuttingDown': 123,
                    'StartFailed': 123,
                    'Stopped': 123,
                    'Stopping': 123,
                    'Terminated': 123,
                    'Terminating': 123,
                    'Unassigning': 123
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``DescribeStackSummary`` request.

        
        

        - **StackSummary** *(dict) --* 

          A ``StackSummary`` object that contains the results.

          
          

          - **StackId** *(string) --* 

            The stack ID.

            
          

          - **Name** *(string) --* 

            The stack name.

            
          

          - **Arn** *(string) --* 

            The stack's ARN.

            
          

          - **LayersCount** *(integer) --* 

            The number of layers.

            
          

          - **AppsCount** *(integer) --* 

            The number of apps.

            
          

          - **InstancesCount** *(dict) --* 

            An ``InstancesCount`` object with the number of instances in each status.

            
            

            - **Assigning** *(integer) --* 

              The number of instances in the Assigning state.

              
            

            - **Booting** *(integer) --* 

              The number of instances with ``booting`` status.

              
            

            - **ConnectionLost** *(integer) --* 

              The number of instances with ``connection_lost`` status.

              
            

            - **Deregistering** *(integer) --* 

              The number of instances in the Deregistering state.

              
            

            - **Online** *(integer) --* 

              The number of instances with ``online`` status.

              
            

            - **Pending** *(integer) --* 

              The number of instances with ``pending`` status.

              
            

            - **Rebooting** *(integer) --* 

              The number of instances with ``rebooting`` status.

              
            

            - **Registered** *(integer) --* 

              The number of instances in the Registered state.

              
            

            - **Registering** *(integer) --* 

              The number of instances in the Registering state.

              
            

            - **Requested** *(integer) --* 

              The number of instances with ``requested`` status.

              
            

            - **RunningSetup** *(integer) --* 

              The number of instances with ``running_setup`` status.

              
            

            - **SetupFailed** *(integer) --* 

              The number of instances with ``setup_failed`` status.

              
            

            - **ShuttingDown** *(integer) --* 

              The number of instances with ``shutting_down`` status.

              
            

            - **StartFailed** *(integer) --* 

              The number of instances with ``start_failed`` status.

              
            

            - **Stopped** *(integer) --* 

              The number of instances with ``stopped`` status.

              
            

            - **Stopping** *(integer) --* 

              The number of instances with ``stopping`` status.

              
            

            - **Terminated** *(integer) --* 

              The number of instances with ``terminated`` status.

              
            

            - **Terminating** *(integer) --* 

              The number of instances with ``terminating`` status.

              
            

            - **Unassigning** *(integer) --* 

              The number of instances in the Unassigning state.

              
        
      
    

  .. py:method:: describe_stacks(**kwargs)

    

    Requests a description of one or more stacks.

     

     **Required Permissions** : To use this action, an IAM user must have a Show, Deploy, or Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeStacks>`_    


    **Request Syntax** 
    ::

      response = client.describe_stacks(
          StackIds=[
              'string',
          ]
      )
    :type StackIds: list
    :param StackIds: 

      An array of stack IDs that specify the stacks to be described. If you omit this parameter, ``DescribeStacks`` returns a description of every stack.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Stacks': [
                {
                    'StackId': 'string',
                    'Name': 'string',
                    'Arn': 'string',
                    'Region': 'string',
                    'VpcId': 'string',
                    'Attributes': {
                        'string': 'string'
                    },
                    'ServiceRoleArn': 'string',
                    'DefaultInstanceProfileArn': 'string',
                    'DefaultOs': 'string',
                    'HostnameTheme': 'string',
                    'DefaultAvailabilityZone': 'string',
                    'DefaultSubnetId': 'string',
                    'CustomJson': 'string',
                    'ConfigurationManager': {
                        'Name': 'string',
                        'Version': 'string'
                    },
                    'ChefConfiguration': {
                        'ManageBerkshelf': True|False,
                        'BerkshelfVersion': 'string'
                    },
                    'UseCustomCookbooks': True|False,
                    'UseOpsworksSecurityGroups': True|False,
                    'CustomCookbooksSource': {
                        'Type': 'git'|'svn'|'archive'|'s3',
                        'Url': 'string',
                        'Username': 'string',
                        'Password': 'string',
                        'SshKey': 'string',
                        'Revision': 'string'
                    },
                    'DefaultSshKeyName': 'string',
                    'CreatedAt': 'string',
                    'DefaultRootDeviceType': 'ebs'|'instance-store',
                    'AgentVersion': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``DescribeStacks`` request.

        
        

        - **Stacks** *(list) --* 

          An array of ``Stack`` objects that describe the stacks.

          
          

          - *(dict) --* 

            Describes a stack.

            
            

            - **StackId** *(string) --* 

              The stack ID.

              
            

            - **Name** *(string) --* 

              The stack name.

              
            

            - **Arn** *(string) --* 

              The stack's ARN.

              
            

            - **Region** *(string) --* 

              The stack AWS region, such as "ap-northeast-2". For more information about AWS regions, see `Regions and Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html>`__ .

              
            

            - **VpcId** *(string) --* 

              The VPC ID; applicable only if the stack is running in a VPC.

              
            

            - **Attributes** *(dict) --* 

              The stack's attributes.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **ServiceRoleArn** *(string) --* 

              The stack AWS Identity and Access Management (IAM) role.

              
            

            - **DefaultInstanceProfileArn** *(string) --* 

              The ARN of an IAM profile that is the default profile for all of the stack's EC2 instances. For more information about IAM ARNs, see `Using Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ .

              
            

            - **DefaultOs** *(string) --* 

              The stack's default operating system.

              
            

            - **HostnameTheme** *(string) --* 

              The stack host name theme, with spaces replaced by underscores.

              
            

            - **DefaultAvailabilityZone** *(string) --* 

              The stack's default Availability Zone. For more information, see `Regions and Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html>`__ .

              
            

            - **DefaultSubnetId** *(string) --* 

              The default subnet ID; applicable only if the stack is running in a VPC.

              
            

            - **CustomJson** *(string) --* 

              A JSON object that contains user-defined attributes to be added to the stack configuration and deployment attributes. You can use custom JSON to override the corresponding default stack configuration attribute values or to pass data to recipes. The string should be in the following format:

               

               ``"{\"key1\": \"value1\", \"key2\": \"value2\",...}"``  

               

              For more information on custom JSON, see `Use Custom JSON to Modify the Stack Configuration Attributes <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-json.html>`__ .

              
            

            - **ConfigurationManager** *(dict) --* 

              The configuration manager.

              
              

              - **Name** *(string) --* 

                The name. This parameter must be set to "Chef".

                
              

              - **Version** *(string) --* 

                The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to 12.2 for Windows stacks. The default value for Linux stacks is 11.4.

                
          
            

            - **ChefConfiguration** *(dict) --* 

              A ``ChefConfiguration`` object that specifies whether to enable Berkshelf and the Berkshelf version. For more information, see `Create a New Stack <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`__ .

              
              

              - **ManageBerkshelf** *(boolean) --* 

                Whether to enable Berkshelf.

                
              

              - **BerkshelfVersion** *(string) --* 

                The Berkshelf version.

                
          
            

            - **UseCustomCookbooks** *(boolean) --* 

              Whether the stack uses custom cookbooks.

              
            

            - **UseOpsworksSecurityGroups** *(boolean) --* 

              Whether the stack automatically associates the AWS OpsWorks Stacks built-in security groups with the stack's layers.

              
            

            - **CustomCookbooksSource** *(dict) --* 

              Contains the information required to retrieve an app or cookbook from a repository. For more information, see `Creating Apps <http://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html>`__ or `Custom Recipes and Cookbooks <http://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html>`__ .

              
              

              - **Type** *(string) --* 

                The repository type.

                
              

              - **Url** *(string) --* 

                The source URL. The following is an example of an Amazon S3 source URL: ``https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz`` .

                
              

              - **Username** *(string) --* 

                This parameter depends on the repository type.

                 

                 
                * For Amazon S3 bundles, set ``Username`` to the appropriate IAM access key ID. 
                 
                * For HTTP bundles, Git repositories, and Subversion repositories, set ``Username`` to the user name. 
                 

                
              

              - **Password** *(string) --* 

                When included in a request, the parameter depends on the repository type.

                 

                 
                * For Amazon S3 bundles, set ``Password`` to the appropriate IAM secret access key. 
                 
                * For HTTP bundles and Subversion repositories, set ``Password`` to the password. 
                 

                 

                For more information on how to safely handle IAM credentials, see `http\://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html <http://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html>`__ .

                 

                In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

                
              

              - **SshKey** *(string) --* 

                In requests, the repository's SSH key.

                 

                In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

                
              

              - **Revision** *(string) --* 

                The application's version. AWS OpsWorks Stacks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.

                
          
            

            - **DefaultSshKeyName** *(string) --* 

              A default Amazon EC2 key pair for the stack's instances. You can override this value when you create or update an instance.

              
            

            - **CreatedAt** *(string) --* 

              The date when the stack was created.

              
            

            - **DefaultRootDeviceType** *(string) --* 

              The default root device type. This value is used by default for all instances in the stack, but you can override it when you create an instance. For more information, see `Storage for the Root Device <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-for-the-root-device>`__ .

              
            

            - **AgentVersion** *(string) --* 

              The agent version. This parameter is set to ``LATEST`` for auto-update. or a version number for a fixed agent version.

              
        
      
    

  .. py:method:: describe_time_based_auto_scaling(**kwargs)

    

    Describes time-based auto scaling configurations for specified instances.

     

    .. note::

       

      You must specify at least one of the parameters.

       

     

     **Required Permissions** : To use this action, an IAM user must have a Show, Deploy, or Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeTimeBasedAutoScaling>`_    


    **Request Syntax** 
    ::

      response = client.describe_time_based_auto_scaling(
          InstanceIds=[
              'string',
          ]
      )
    :type InstanceIds: list
    :param InstanceIds: **[REQUIRED]** 

      An array of instance IDs.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TimeBasedAutoScalingConfigurations': [
                {
                    'InstanceId': 'string',
                    'AutoScalingSchedule': {
                        'Monday': {
                            'string': 'string'
                        },
                        'Tuesday': {
                            'string': 'string'
                        },
                        'Wednesday': {
                            'string': 'string'
                        },
                        'Thursday': {
                            'string': 'string'
                        },
                        'Friday': {
                            'string': 'string'
                        },
                        'Saturday': {
                            'string': 'string'
                        },
                        'Sunday': {
                            'string': 'string'
                        }
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``DescribeTimeBasedAutoScaling`` request.

        
        

        - **TimeBasedAutoScalingConfigurations** *(list) --* 

          An array of ``TimeBasedAutoScalingConfiguration`` objects that describe the configuration for the specified instances.

          
          

          - *(dict) --* 

            Describes an instance's time-based auto scaling configuration.

            
            

            - **InstanceId** *(string) --* 

              The instance ID.

              
            

            - **AutoScalingSchedule** *(dict) --* 

              A ``WeeklyAutoScalingSchedule`` object with the instance schedule.

              
              

              - **Monday** *(dict) --* 

                The schedule for Monday.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **Tuesday** *(dict) --* 

                The schedule for Tuesday.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **Wednesday** *(dict) --* 

                The schedule for Wednesday.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **Thursday** *(dict) --* 

                The schedule for Thursday.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **Friday** *(dict) --* 

                The schedule for Friday.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **Saturday** *(dict) --* 

                The schedule for Saturday.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **Sunday** *(dict) --* 

                The schedule for Sunday.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
          
        
      
    

  .. py:method:: describe_user_profiles(**kwargs)

    

    Describe specified users.

     

     **Required Permissions** : To use this action, an IAM user must have an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeUserProfiles>`_    


    **Request Syntax** 
    ::

      response = client.describe_user_profiles(
          IamUserArns=[
              'string',
          ]
      )
    :type IamUserArns: list
    :param IamUserArns: 

      An array of IAM or federated user ARNs that identify the users to be described.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UserProfiles': [
                {
                    'IamUserArn': 'string',
                    'Name': 'string',
                    'SshUsername': 'string',
                    'SshPublicKey': 'string',
                    'AllowSelfManagement': True|False
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``DescribeUserProfiles`` request.

        
        

        - **UserProfiles** *(list) --* 

          A ``Users`` object that describes the specified users.

          
          

          - *(dict) --* 

            Describes a user's SSH information.

            
            

            - **IamUserArn** *(string) --* 

              The user's IAM ARN.

              
            

            - **Name** *(string) --* 

              The user's name.

              
            

            - **SshUsername** *(string) --* 

              The user's SSH user name.

              
            

            - **SshPublicKey** *(string) --* 

              The user's SSH public key.

              
            

            - **AllowSelfManagement** *(boolean) --* 

              Whether users can specify their own SSH public key through the My Settings page. For more information, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/security-settingsshkey.html>`__ .

              
        
      
    

  .. py:method:: describe_volumes(**kwargs)

    

    Describes an instance's Amazon EBS volumes.

     

    .. note::

       

      This call accepts only one resource-identifying parameter.

       

     

     **Required Permissions** : To use this action, an IAM user must have a Show, Deploy, or Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeVolumes>`_    


    **Request Syntax** 
    ::

      response = client.describe_volumes(
          InstanceId='string',
          StackId='string',
          RaidArrayId='string',
          VolumeIds=[
              'string',
          ]
      )
    :type InstanceId: string
    :param InstanceId: 

      The instance ID. If you use this parameter, ``DescribeVolumes`` returns descriptions of the volumes associated with the specified instance.

      

    
    :type StackId: string
    :param StackId: 

      A stack ID. The action describes the stack's registered Amazon EBS volumes.

      

    
    :type RaidArrayId: string
    :param RaidArrayId: 

      The RAID array ID. If you use this parameter, ``DescribeVolumes`` returns descriptions of the volumes associated with the specified RAID array.

      

    
    :type VolumeIds: list
    :param VolumeIds: 

      Am array of volume IDs. If you use this parameter, ``DescribeVolumes`` returns descriptions of the specified volumes. Otherwise, it returns a description of every volume.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Volumes': [
                {
                    'VolumeId': 'string',
                    'Ec2VolumeId': 'string',
                    'Name': 'string',
                    'RaidArrayId': 'string',
                    'InstanceId': 'string',
                    'Status': 'string',
                    'Size': 123,
                    'Device': 'string',
                    'MountPoint': 'string',
                    'Region': 'string',
                    'AvailabilityZone': 'string',
                    'VolumeType': 'string',
                    'Iops': 123
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``DescribeVolumes`` request.

        
        

        - **Volumes** *(list) --* 

          An array of volume IDs.

          
          

          - *(dict) --* 

            Describes an instance's Amazon EBS volume.

            
            

            - **VolumeId** *(string) --* 

              The volume ID.

              
            

            - **Ec2VolumeId** *(string) --* 

              The Amazon EC2 volume ID.

              
            

            - **Name** *(string) --* 

              The volume name.

              
            

            - **RaidArrayId** *(string) --* 

              The RAID array ID.

              
            

            - **InstanceId** *(string) --* 

              The instance ID.

              
            

            - **Status** *(string) --* 

              The value returned by `DescribeVolumes <http://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-query-DescribeVolumes.html>`__ .

              
            

            - **Size** *(integer) --* 

              The volume size.

              
            

            - **Device** *(string) --* 

              The device name.

              
            

            - **MountPoint** *(string) --* 

              The volume mount point. For example, "/mnt/disk1".

              
            

            - **Region** *(string) --* 

              The AWS region. For more information about AWS regions, see `Regions and Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html>`__ .

              
            

            - **AvailabilityZone** *(string) --* 

              The volume Availability Zone. For more information, see `Regions and Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html>`__ .

              
            

            - **VolumeType** *(string) --* 

              The volume type, standard or PIOPS.

              
            

            - **Iops** *(integer) --* 

              For PIOPS volumes, the IOPS per disk.

              
        
      
    

  .. py:method:: detach_elastic_load_balancer(**kwargs)

    

    Detaches a specified Elastic Load Balancing instance from its layer.

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DetachElasticLoadBalancer>`_    


    **Request Syntax** 
    ::

      response = client.detach_elastic_load_balancer(
          ElasticLoadBalancerName='string',
          LayerId='string'
      )
    :type ElasticLoadBalancerName: string
    :param ElasticLoadBalancerName: **[REQUIRED]** 

      The Elastic Load Balancing instance's name.

      

    
    :type LayerId: string
    :param LayerId: **[REQUIRED]** 

      The ID of the layer that the Elastic Load Balancing instance is attached to.

      

    
    
    :returns: None

  .. py:method:: disassociate_elastic_ip(**kwargs)

    

    Disassociates an Elastic IP address from its instance. The address remains registered with the stack. For more information, see `Resource Management <http://docs.aws.amazon.com/opsworks/latest/userguide/resources.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DisassociateElasticIp>`_    


    **Request Syntax** 
    ::

      response = client.disassociate_elastic_ip(
          ElasticIp='string'
      )
    :type ElasticIp: string
    :param ElasticIp: **[REQUIRED]** 

      The Elastic IP address.

      

    
    
    :returns: None

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


  .. py:method:: get_hostname_suggestion(**kwargs)

    

    Gets a generated host name for the specified layer, based on the current host name theme.

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/GetHostnameSuggestion>`_    


    **Request Syntax** 
    ::

      response = client.get_hostname_suggestion(
          LayerId='string'
      )
    :type LayerId: string
    :param LayerId: **[REQUIRED]** 

      The layer ID.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'LayerId': 'string',
            'Hostname': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``GetHostnameSuggestion`` request.

        
        

        - **LayerId** *(string) --* 

          The layer ID.

          
        

        - **Hostname** *(string) --* 

          The generated host name.

          
    

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

        


  .. py:method:: grant_access(**kwargs)

    

    .. note::

       

      This action can be used only with Windows stacks.

       

     

    Grants RDP access to a Windows instance for a specified time period.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/GrantAccess>`_    


    **Request Syntax** 
    ::

      response = client.grant_access(
          InstanceId='string',
          ValidForInMinutes=123
      )
    :type InstanceId: string
    :param InstanceId: **[REQUIRED]** 

      The instance's AWS OpsWorks Stacks ID.

      

    
    :type ValidForInMinutes: integer
    :param ValidForInMinutes: 

      The length of time (in minutes) that the grant is valid. When the grant expires at the end of this period, the user will no longer be able to use the credentials to log in. If the user is logged in at the time, he or she automatically will be logged out.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TemporaryCredential': {
                'Username': 'string',
                'Password': 'string',
                'ValidForInMinutes': 123,
                'InstanceId': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``GrantAccess`` request.

        
        

        - **TemporaryCredential** *(dict) --* 

          A ``TemporaryCredential`` object that contains the data needed to log in to the instance by RDP clients, such as the Microsoft Remote Desktop Connection.

          
          

          - **Username** *(string) --* 

            The user name.

            
          

          - **Password** *(string) --* 

            The password.

            
          

          - **ValidForInMinutes** *(integer) --* 

            The length of time (in minutes) that the grant is valid. When the grant expires, at the end of this period, the user will no longer be able to use the credentials to log in. If they are logged in at the time, they will be automatically logged out.

            
          

          - **InstanceId** *(string) --* 

            The instance's AWS OpsWorks Stacks ID.

            
      
    

  .. py:method:: list_tags(**kwargs)

    

    Returns a list of tags that are applied to the specified stack or layer.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/ListTags>`_    


    **Request Syntax** 
    ::

      response = client.list_tags(
          ResourceArn='string',
          MaxResults=123,
          NextToken='string'
      )
    :type ResourceArn: string
    :param ResourceArn: **[REQUIRED]** 

      The stack or layer's Amazon Resource Number (ARN).

      

    
    :type MaxResults: integer
    :param MaxResults: 

      Do not use. A validation exception occurs if you add a ``MaxResults`` parameter to a ``ListTagsRequest`` call. 

      

    
    :type NextToken: string
    :param NextToken: 

      Do not use. A validation exception occurs if you add a ``NextToken`` parameter to a ``ListTagsRequest`` call. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Tags': {
                'string': 'string'
            },
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``ListTags`` request.

        
        

        - **Tags** *(dict) --* 

          A set of key-value pairs that contain tag keys and tag values that are attached to a stack or layer.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **NextToken** *(string) --* 

          If a paginated request does not return all of the remaining results, this parameter is set to a token that you can assign to the request object's ``NextToken`` parameter to get the next set of results. If the previous paginated request returned all of the remaining results, this parameter is set to ``null`` . 

          
    

  .. py:method:: reboot_instance(**kwargs)

    

    Reboots a specified instance. For more information, see `Starting, Stopping, and Rebooting Instances <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-starting.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/RebootInstance>`_    


    **Request Syntax** 
    ::

      response = client.reboot_instance(
          InstanceId='string'
      )
    :type InstanceId: string
    :param InstanceId: **[REQUIRED]** 

      The instance ID.

      

    
    
    :returns: None

  .. py:method:: register_ecs_cluster(**kwargs)

    

    Registers a specified Amazon ECS cluster with a stack. You can register only one cluster with a stack. A cluster can be registered with only one stack. For more information, see `Resource Management <http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-ecscluster.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/RegisterEcsCluster>`_    


    **Request Syntax** 
    ::

      response = client.register_ecs_cluster(
          EcsClusterArn='string',
          StackId='string'
      )
    :type EcsClusterArn: string
    :param EcsClusterArn: **[REQUIRED]** 

      The cluster's ARN.

      

    
    :type StackId: string
    :param StackId: **[REQUIRED]** 

      The stack ID.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'EcsClusterArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``RegisterEcsCluster`` request.

        
        

        - **EcsClusterArn** *(string) --* 

          The cluster's ARN.

          
    

  .. py:method:: register_elastic_ip(**kwargs)

    

    Registers an Elastic IP address with a specified stack. An address can be registered with only one stack at a time. If the address is already registered, you must first deregister it by calling  DeregisterElasticIp . For more information, see `Resource Management <http://docs.aws.amazon.com/opsworks/latest/userguide/resources.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/RegisterElasticIp>`_    


    **Request Syntax** 
    ::

      response = client.register_elastic_ip(
          ElasticIp='string',
          StackId='string'
      )
    :type ElasticIp: string
    :param ElasticIp: **[REQUIRED]** 

      The Elastic IP address.

      

    
    :type StackId: string
    :param StackId: **[REQUIRED]** 

      The stack ID.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ElasticIp': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``RegisterElasticIp`` request.

        
        

        - **ElasticIp** *(string) --* 

          The Elastic IP address.

          
    

  .. py:method:: register_instance(**kwargs)

    

    Registers instances that were created outside of AWS OpsWorks Stacks with a specified stack.

     

    .. note::

       

      We do not recommend using this action to register instances. The complete registration operation includes two tasks: installing the AWS OpsWorks Stacks agent on the instance, and registering the instance with the stack. ``RegisterInstance`` handles only the second step. You should instead use the AWS CLI ``register`` command, which performs the entire registration operation. For more information, see `Registering an Instance with an AWS OpsWorks Stacks Stack <http://docs.aws.amazon.com/opsworks/latest/userguide/registered-instances-register.html>`__ .

       

     

    Registered instances have the same requirements as instances that are created by using the  CreateInstance API. For example, registered instances must be running a supported Linux-based operating system, and they must have a supported instance type. For more information about requirements for instances that you want to register, see `Preparing the Instance <http://docs.aws.amazon.com/opsworks/latest/userguide/registered-instances-register-registering-preparer.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/RegisterInstance>`_    


    **Request Syntax** 
    ::

      response = client.register_instance(
          StackId='string',
          Hostname='string',
          PublicIp='string',
          PrivateIp='string',
          RsaPublicKey='string',
          RsaPublicKeyFingerprint='string',
          InstanceIdentity={
              'Document': 'string',
              'Signature': 'string'
          }
      )
    :type StackId: string
    :param StackId: **[REQUIRED]** 

      The ID of the stack that the instance is to be registered with.

      

    
    :type Hostname: string
    :param Hostname: 

      The instance's hostname.

      

    
    :type PublicIp: string
    :param PublicIp: 

      The instance's public IP address.

      

    
    :type PrivateIp: string
    :param PrivateIp: 

      The instance's private IP address.

      

    
    :type RsaPublicKey: string
    :param RsaPublicKey: 

      The instances public RSA key. This key is used to encrypt communication between the instance and the service.

      

    
    :type RsaPublicKeyFingerprint: string
    :param RsaPublicKeyFingerprint: 

      The instances public RSA key fingerprint.

      

    
    :type InstanceIdentity: dict
    :param InstanceIdentity: 

      An InstanceIdentity object that contains the instance's identity.

      

    
      - **Document** *(string) --* 

        A JSON document that contains the metadata.

        

      
      - **Signature** *(string) --* 

        A signature that can be used to verify the document's accuracy and authenticity.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'InstanceId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``RegisterInstanceResult`` request.

        
        

        - **InstanceId** *(string) --* 

          The registered instance's AWS OpsWorks Stacks ID.

          
    

  .. py:method:: register_rds_db_instance(**kwargs)

    

    Registers an Amazon RDS instance with a stack.

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/RegisterRdsDbInstance>`_    


    **Request Syntax** 
    ::

      response = client.register_rds_db_instance(
          StackId='string',
          RdsDbInstanceArn='string',
          DbUser='string',
          DbPassword='string'
      )
    :type StackId: string
    :param StackId: **[REQUIRED]** 

      The stack ID.

      

    
    :type RdsDbInstanceArn: string
    :param RdsDbInstanceArn: **[REQUIRED]** 

      The Amazon RDS instance's ARN.

      

    
    :type DbUser: string
    :param DbUser: **[REQUIRED]** 

      The database's master user name.

      

    
    :type DbPassword: string
    :param DbPassword: **[REQUIRED]** 

      The database password.

      

    
    
    :returns: None

  .. py:method:: register_volume(**kwargs)

    

    Registers an Amazon EBS volume with a specified stack. A volume can be registered with only one stack at a time. If the volume is already registered, you must first deregister it by calling  DeregisterVolume . For more information, see `Resource Management <http://docs.aws.amazon.com/opsworks/latest/userguide/resources.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/RegisterVolume>`_    


    **Request Syntax** 
    ::

      response = client.register_volume(
          Ec2VolumeId='string',
          StackId='string'
      )
    :type Ec2VolumeId: string
    :param Ec2VolumeId: 

      The Amazon EBS volume ID.

      

    
    :type StackId: string
    :param StackId: **[REQUIRED]** 

      The stack ID.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'VolumeId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``RegisterVolume`` request.

        
        

        - **VolumeId** *(string) --* 

          The volume ID.

          
    

  .. py:method:: set_load_based_auto_scaling(**kwargs)

    

    Specify the load-based auto scaling configuration for a specified layer. For more information, see `Managing Load with Time-based and Load-based Instances <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-autoscaling.html>`__ .

     

    .. note::

       

      To use load-based auto scaling, you must create a set of load-based auto scaling instances. Load-based auto scaling operates only on the instances from that set, so you must ensure that you have created enough instances to handle the maximum anticipated load.

       

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/SetLoadBasedAutoScaling>`_    


    **Request Syntax** 
    ::

      response = client.set_load_based_auto_scaling(
          LayerId='string',
          Enable=True|False,
          UpScaling={
              'InstanceCount': 123,
              'ThresholdsWaitTime': 123,
              'IgnoreMetricsTime': 123,
              'CpuThreshold': 123.0,
              'MemoryThreshold': 123.0,
              'LoadThreshold': 123.0,
              'Alarms': [
                  'string',
              ]
          },
          DownScaling={
              'InstanceCount': 123,
              'ThresholdsWaitTime': 123,
              'IgnoreMetricsTime': 123,
              'CpuThreshold': 123.0,
              'MemoryThreshold': 123.0,
              'LoadThreshold': 123.0,
              'Alarms': [
                  'string',
              ]
          }
      )
    :type LayerId: string
    :param LayerId: **[REQUIRED]** 

      The layer ID.

      

    
    :type Enable: boolean
    :param Enable: 

      Enables load-based auto scaling for the layer.

      

    
    :type UpScaling: dict
    :param UpScaling: 

      An ``AutoScalingThresholds`` object with the upscaling threshold configuration. If the load exceeds these thresholds for a specified amount of time, AWS OpsWorks Stacks starts a specified number of instances.

      

    
      - **InstanceCount** *(integer) --* 

        The number of instances to add or remove when the load exceeds a threshold.

        

      
      - **ThresholdsWaitTime** *(integer) --* 

        The amount of time, in minutes, that the load must exceed a threshold before more instances are added or removed.

        

      
      - **IgnoreMetricsTime** *(integer) --* 

        The amount of time (in minutes) after a scaling event occurs that AWS OpsWorks Stacks should ignore metrics and suppress additional scaling events. For example, AWS OpsWorks Stacks adds new instances following an upscaling event but the instances won't start reducing the load until they have been booted and configured. There is no point in raising additional scaling events during that operation, which typically takes several minutes. ``IgnoreMetricsTime`` allows you to direct AWS OpsWorks Stacks to suppress scaling events long enough to get the new instances online.

        

      
      - **CpuThreshold** *(float) --* 

        The CPU utilization threshold, as a percent of the available CPU. A value of -1 disables the threshold.

        

      
      - **MemoryThreshold** *(float) --* 

        The memory utilization threshold, as a percent of the available memory. A value of -1 disables the threshold.

        

      
      - **LoadThreshold** *(float) --* 

        The load threshold. A value of -1 disables the threshold. For more information about how load is computed, see `Load (computing) <http://en.wikipedia.org/wiki/Load_%28computing%29>`__ .

        

      
      - **Alarms** *(list) --* 

        Custom Cloudwatch auto scaling alarms, to be used as thresholds. This parameter takes a list of up to five alarm names, which are case sensitive and must be in the same region as the stack.

         

        .. note::

           

          To use custom alarms, you must update your service role to allow ``cloudwatch:DescribeAlarms`` . You can either have AWS OpsWorks Stacks update the role for you when you first use this feature or you can edit the role manually. For more information, see `Allowing AWS OpsWorks Stacks to Act on Your Behalf <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-servicerole.html>`__ .

           

        

      
        - *(string) --* 

        
    
    
    :type DownScaling: dict
    :param DownScaling: 

      An ``AutoScalingThresholds`` object with the downscaling threshold configuration. If the load falls below these thresholds for a specified amount of time, AWS OpsWorks Stacks stops a specified number of instances.

      

    
      - **InstanceCount** *(integer) --* 

        The number of instances to add or remove when the load exceeds a threshold.

        

      
      - **ThresholdsWaitTime** *(integer) --* 

        The amount of time, in minutes, that the load must exceed a threshold before more instances are added or removed.

        

      
      - **IgnoreMetricsTime** *(integer) --* 

        The amount of time (in minutes) after a scaling event occurs that AWS OpsWorks Stacks should ignore metrics and suppress additional scaling events. For example, AWS OpsWorks Stacks adds new instances following an upscaling event but the instances won't start reducing the load until they have been booted and configured. There is no point in raising additional scaling events during that operation, which typically takes several minutes. ``IgnoreMetricsTime`` allows you to direct AWS OpsWorks Stacks to suppress scaling events long enough to get the new instances online.

        

      
      - **CpuThreshold** *(float) --* 

        The CPU utilization threshold, as a percent of the available CPU. A value of -1 disables the threshold.

        

      
      - **MemoryThreshold** *(float) --* 

        The memory utilization threshold, as a percent of the available memory. A value of -1 disables the threshold.

        

      
      - **LoadThreshold** *(float) --* 

        The load threshold. A value of -1 disables the threshold. For more information about how load is computed, see `Load (computing) <http://en.wikipedia.org/wiki/Load_%28computing%29>`__ .

        

      
      - **Alarms** *(list) --* 

        Custom Cloudwatch auto scaling alarms, to be used as thresholds. This parameter takes a list of up to five alarm names, which are case sensitive and must be in the same region as the stack.

         

        .. note::

           

          To use custom alarms, you must update your service role to allow ``cloudwatch:DescribeAlarms`` . You can either have AWS OpsWorks Stacks update the role for you when you first use this feature or you can edit the role manually. For more information, see `Allowing AWS OpsWorks Stacks to Act on Your Behalf <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-servicerole.html>`__ .

           

        

      
        - *(string) --* 

        
    
    
    
    :returns: None

  .. py:method:: set_permission(**kwargs)

    

    Specifies a user's permissions. For more information, see `Security and Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/workingsecurity.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/SetPermission>`_    


    **Request Syntax** 
    ::

      response = client.set_permission(
          StackId='string',
          IamUserArn='string',
          AllowSsh=True|False,
          AllowSudo=True|False,
          Level='string'
      )
    :type StackId: string
    :param StackId: **[REQUIRED]** 

      The stack ID.

      

    
    :type IamUserArn: string
    :param IamUserArn: **[REQUIRED]** 

      The user's IAM ARN. This can also be a federated user's ARN.

      

    
    :type AllowSsh: boolean
    :param AllowSsh: 

      The user is allowed to use SSH to communicate with the instance.

      

    
    :type AllowSudo: boolean
    :param AllowSudo: 

      The user is allowed to use **sudo** to elevate privileges.

      

    
    :type Level: string
    :param Level: 

      The user's permission level, which must be set to one of the following strings. You cannot set your own permissions level.

       

       
      * ``deny``   
       
      * ``show``   
       
      * ``deploy``   
       
      * ``manage``   
       
      * ``iam_only``   
       

       

      For more information on the permissions associated with these levels, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

      

    
    
    :returns: None

  .. py:method:: set_time_based_auto_scaling(**kwargs)

    

    Specify the time-based auto scaling configuration for a specified instance. For more information, see `Managing Load with Time-based and Load-based Instances <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-autoscaling.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/SetTimeBasedAutoScaling>`_    


    **Request Syntax** 
    ::

      response = client.set_time_based_auto_scaling(
          InstanceId='string',
          AutoScalingSchedule={
              'Monday': {
                  'string': 'string'
              },
              'Tuesday': {
                  'string': 'string'
              },
              'Wednesday': {
                  'string': 'string'
              },
              'Thursday': {
                  'string': 'string'
              },
              'Friday': {
                  'string': 'string'
              },
              'Saturday': {
                  'string': 'string'
              },
              'Sunday': {
                  'string': 'string'
              }
          }
      )
    :type InstanceId: string
    :param InstanceId: **[REQUIRED]** 

      The instance ID.

      

    
    :type AutoScalingSchedule: dict
    :param AutoScalingSchedule: 

      An ``AutoScalingSchedule`` with the instance schedule.

      

    
      - **Monday** *(dict) --* 

        The schedule for Monday.

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
      - **Tuesday** *(dict) --* 

        The schedule for Tuesday.

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
      - **Wednesday** *(dict) --* 

        The schedule for Wednesday.

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
      - **Thursday** *(dict) --* 

        The schedule for Thursday.

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
      - **Friday** *(dict) --* 

        The schedule for Friday.

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
      - **Saturday** *(dict) --* 

        The schedule for Saturday.

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
      - **Sunday** *(dict) --* 

        The schedule for Sunday.

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
    
    
    :returns: None

  .. py:method:: start_instance(**kwargs)

    

    Starts a specified instance. For more information, see `Starting, Stopping, and Rebooting Instances <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-starting.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/StartInstance>`_    


    **Request Syntax** 
    ::

      response = client.start_instance(
          InstanceId='string'
      )
    :type InstanceId: string
    :param InstanceId: **[REQUIRED]** 

      The instance ID.

      

    
    
    :returns: None

  .. py:method:: start_stack(**kwargs)

    

    Starts a stack's instances.

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/StartStack>`_    


    **Request Syntax** 
    ::

      response = client.start_stack(
          StackId='string'
      )
    :type StackId: string
    :param StackId: **[REQUIRED]** 

      The stack ID.

      

    
    
    :returns: None

  .. py:method:: stop_instance(**kwargs)

    

    Stops a specified instance. When you stop a standard instance, the data disappears and must be reinstalled when you restart the instance. You can stop an Amazon EBS-backed instance without losing data. For more information, see `Starting, Stopping, and Rebooting Instances <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-starting.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/StopInstance>`_    


    **Request Syntax** 
    ::

      response = client.stop_instance(
          InstanceId='string'
      )
    :type InstanceId: string
    :param InstanceId: **[REQUIRED]** 

      The instance ID.

      

    
    
    :returns: None

  .. py:method:: stop_stack(**kwargs)

    

    Stops a specified stack.

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/StopStack>`_    


    **Request Syntax** 
    ::

      response = client.stop_stack(
          StackId='string'
      )
    :type StackId: string
    :param StackId: **[REQUIRED]** 

      The stack ID.

      

    
    
    :returns: None

  .. py:method:: tag_resource(**kwargs)

    

    Apply cost-allocation tags to a specified stack or layer in AWS OpsWorks Stacks. For more information about how tagging works, see `Tags <http://docs.aws.amazon.com/opsworks/latest/userguide/tagging.html>`__ in the AWS OpsWorks User Guide.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/TagResource>`_    


    **Request Syntax** 
    ::

      response = client.tag_resource(
          ResourceArn='string',
          Tags={
              'string': 'string'
          }
      )
    :type ResourceArn: string
    :param ResourceArn: **[REQUIRED]** 

      The stack or layer's Amazon Resource Number (ARN).

      

    
    :type Tags: dict
    :param Tags: **[REQUIRED]** 

      A map that contains tag keys and tag values that are attached to a stack or layer.

       

       
      * The key cannot be empty. 
       
      * The key can be a maximum of 127 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: ``+ - = . _ : /``   
       
      * The value can be a maximum 255 characters, and contain only Unicode letters, numbers, or separators, or the following special characters: ``+ - = . _ : /``   
       
      * Leading and trailing white spaces are trimmed from both the key and value. 
       
      * A maximum of 40 tags is allowed for any resource. 
       

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    
    :returns: None

  .. py:method:: unassign_instance(**kwargs)

    

    Unassigns a registered instance from all of it's layers. The instance remains in the stack as an unassigned instance and can be assigned to another layer, as needed. You cannot use this action with instances that were created with AWS OpsWorks Stacks.

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/UnassignInstance>`_    


    **Request Syntax** 
    ::

      response = client.unassign_instance(
          InstanceId='string'
      )
    :type InstanceId: string
    :param InstanceId: **[REQUIRED]** 

      The instance ID.

      

    
    
    :returns: None

  .. py:method:: unassign_volume(**kwargs)

    

    Unassigns an assigned Amazon EBS volume. The volume remains registered with the stack. For more information, see `Resource Management <http://docs.aws.amazon.com/opsworks/latest/userguide/resources.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/UnassignVolume>`_    


    **Request Syntax** 
    ::

      response = client.unassign_volume(
          VolumeId='string'
      )
    :type VolumeId: string
    :param VolumeId: **[REQUIRED]** 

      The volume ID.

      

    
    
    :returns: None

  .. py:method:: untag_resource(**kwargs)

    

    Removes tags from a specified stack or layer.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/UntagResource>`_    


    **Request Syntax** 
    ::

      response = client.untag_resource(
          ResourceArn='string',
          TagKeys=[
              'string',
          ]
      )
    :type ResourceArn: string
    :param ResourceArn: **[REQUIRED]** 

      The stack or layer's Amazon Resource Number (ARN).

      

    
    :type TagKeys: list
    :param TagKeys: **[REQUIRED]** 

      A list of the keys of tags to be removed from a stack or layer.

      

    
      - *(string) --* 

      
  
    
    :returns: None

  .. py:method:: update_app(**kwargs)

    

    Updates a specified app.

     

     **Required Permissions** : To use this action, an IAM user must have a Deploy or Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/UpdateApp>`_    


    **Request Syntax** 
    ::

      response = client.update_app(
          AppId='string',
          Name='string',
          Description='string',
          DataSources=[
              {
                  'Type': 'string',
                  'Arn': 'string',
                  'DatabaseName': 'string'
              },
          ],
          Type='aws-flow-ruby'|'java'|'rails'|'php'|'nodejs'|'static'|'other',
          AppSource={
              'Type': 'git'|'svn'|'archive'|'s3',
              'Url': 'string',
              'Username': 'string',
              'Password': 'string',
              'SshKey': 'string',
              'Revision': 'string'
          },
          Domains=[
              'string',
          ],
          EnableSsl=True|False,
          SslConfiguration={
              'Certificate': 'string',
              'PrivateKey': 'string',
              'Chain': 'string'
          },
          Attributes={
              'string': 'string'
          },
          Environment=[
              {
                  'Key': 'string',
                  'Value': 'string',
                  'Secure': True|False
              },
          ]
      )
    :type AppId: string
    :param AppId: **[REQUIRED]** 

      The app ID.

      

    
    :type Name: string
    :param Name: 

      The app name.

      

    
    :type Description: string
    :param Description: 

      A description of the app.

      

    
    :type DataSources: list
    :param DataSources: 

      The app's data sources.

      

    
      - *(dict) --* 

        Describes an app's data source.

        

      
        - **Type** *(string) --* 

          The data source's type, ``AutoSelectOpsworksMysqlInstance`` , ``OpsworksMysqlInstance`` , or ``RdsDbInstance`` .

          

        
        - **Arn** *(string) --* 

          The data source's ARN.

          

        
        - **DatabaseName** *(string) --* 

          The database name.

          

        
      
  
    :type Type: string
    :param Type: 

      The app type.

      

    
    :type AppSource: dict
    :param AppSource: 

      A ``Source`` object that specifies the app repository.

      

    
      - **Type** *(string) --* 

        The repository type.

        

      
      - **Url** *(string) --* 

        The source URL. The following is an example of an Amazon S3 source URL: ``https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz`` .

        

      
      - **Username** *(string) --* 

        This parameter depends on the repository type.

         

         
        * For Amazon S3 bundles, set ``Username`` to the appropriate IAM access key ID. 
         
        * For HTTP bundles, Git repositories, and Subversion repositories, set ``Username`` to the user name. 
         

        

      
      - **Password** *(string) --* 

        When included in a request, the parameter depends on the repository type.

         

         
        * For Amazon S3 bundles, set ``Password`` to the appropriate IAM secret access key. 
         
        * For HTTP bundles and Subversion repositories, set ``Password`` to the password. 
         

         

        For more information on how to safely handle IAM credentials, see `http\://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html <http://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html>`__ .

         

        In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

        

      
      - **SshKey** *(string) --* 

        In requests, the repository's SSH key.

         

        In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

        

      
      - **Revision** *(string) --* 

        The application's version. AWS OpsWorks Stacks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.

        

      
    
    :type Domains: list
    :param Domains: 

      The app's virtual host settings, with multiple domains separated by commas. For example: ``'www.example.com, example.com'``  

      

    
      - *(string) --* 

      
  
    :type EnableSsl: boolean
    :param EnableSsl: 

      Whether SSL is enabled for the app.

      

    
    :type SslConfiguration: dict
    :param SslConfiguration: 

      An ``SslConfiguration`` object with the SSL configuration.

      

    
      - **Certificate** *(string) --* **[REQUIRED]** 

        The contents of the certificate's domain.crt file.

        

      
      - **PrivateKey** *(string) --* **[REQUIRED]** 

        The private key; the contents of the certificate's domain.kex file.

        

      
      - **Chain** *(string) --* 

        Optional. Can be used to specify an intermediate certificate authority key or client authentication.

        

      
    
    :type Attributes: dict
    :param Attributes: 

      One or more user-defined key/value pairs to be added to the stack attributes.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type Environment: list
    :param Environment: 

      An array of ``EnvironmentVariable`` objects that specify environment variables to be associated with the app. After you deploy the app, these variables are defined on the associated app server instances.For more information, see `Environment Variables <http://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html#workingapps-creating-environment>`__ .

       

      There is no specific limit on the number of environment variables. However, the size of the associated data structure - which includes the variables' names, values, and protected flag values - cannot exceed 10 KB (10240 Bytes). This limit should accommodate most if not all use cases. Exceeding it will cause an exception with the message, "Environment: is too large (maximum is 10KB)."

       

      .. note::

         

        This parameter is supported only by Chef 11.10 stacks. If you have specified one or more environment variables, you cannot modify the stack's Chef version.

         

      

    
      - *(dict) --* 

        Represents an app's environment variable.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          (Required) The environment variable's name, which can consist of up to 64 characters and must be specified. The name can contain upper- and lowercase letters, numbers, and underscores (_), but it must start with a letter or underscore.

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          (Optional) The environment variable's value, which can be left empty. If you specify a value, it can contain up to 256 characters, which must all be printable.

          

        
        - **Secure** *(boolean) --* 

          (Optional) Whether the variable's value will be returned by the  DescribeApps action. To conceal an environment variable's value, set ``Secure`` to ``true`` . ``DescribeApps`` then returns ``*****FILTERED*****`` instead of the actual value. The default value for ``Secure`` is ``false`` . 

          

        
      
  
    
    :returns: None

  .. py:method:: update_elastic_ip(**kwargs)

    

    Updates a registered Elastic IP address's name. For more information, see `Resource Management <http://docs.aws.amazon.com/opsworks/latest/userguide/resources.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/UpdateElasticIp>`_    


    **Request Syntax** 
    ::

      response = client.update_elastic_ip(
          ElasticIp='string',
          Name='string'
      )
    :type ElasticIp: string
    :param ElasticIp: **[REQUIRED]** 

      The address.

      

    
    :type Name: string
    :param Name: 

      The new name.

      

    
    
    :returns: None

  .. py:method:: update_instance(**kwargs)

    

    Updates a specified instance.

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/UpdateInstance>`_    


    **Request Syntax** 
    ::

      response = client.update_instance(
          InstanceId='string',
          LayerIds=[
              'string',
          ],
          InstanceType='string',
          AutoScalingType='load'|'timer',
          Hostname='string',
          Os='string',
          AmiId='string',
          SshKeyName='string',
          Architecture='x86_64'|'i386',
          InstallUpdatesOnBoot=True|False,
          EbsOptimized=True|False,
          AgentVersion='string'
      )
    :type InstanceId: string
    :param InstanceId: **[REQUIRED]** 

      The instance ID.

      

    
    :type LayerIds: list
    :param LayerIds: 

      The instance's layer IDs.

      

    
      - *(string) --* 

      
  
    :type InstanceType: string
    :param InstanceType: 

      The instance type, such as ``t2.micro`` . For a list of supported instance types, open the stack in the console, choose **Instances** , and choose **+ Instance** . The **Size** list contains the currently supported types. For more information, see `Instance Families and Types <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html>`__ . The parameter values that you use to specify the various types are in the **API Name** column of the **Available Instance Types** table.

      

    
    :type AutoScalingType: string
    :param AutoScalingType: 

      For load-based or time-based instances, the type. Windows stacks can use only time-based instances.

      

    
    :type Hostname: string
    :param Hostname: 

      The instance host name.

      

    
    :type Os: string
    :param Os: 

      The instance's operating system, which must be set to one of the following. You cannot update an instance that is using a custom AMI.

       

       
      * A supported Linux operating system: An Amazon Linux version, such as ``Amazon Linux 2017.03`` , ``Amazon Linux 2016.09`` , ``Amazon Linux 2016.03`` , ``Amazon Linux 2015.09`` , or ``Amazon Linux 2015.03`` . 
       
      * A supported Ubuntu operating system, such as ``Ubuntu 16.04 LTS`` , ``Ubuntu 14.04 LTS`` , or ``Ubuntu 12.04 LTS`` . 
       
      * ``CentOS Linux 7``   
       
      * ``Red Hat Enterprise Linux 7``   
       
      * A supported Windows operating system, such as ``Microsoft Windows Server 2012 R2 Base`` , ``Microsoft Windows Server 2012 R2 with SQL Server Express`` , ``Microsoft Windows Server 2012 R2 with SQL Server Standard`` , or ``Microsoft Windows Server 2012 R2 with SQL Server Web`` . 
       

       

      For more information on the supported operating systems, see `AWS OpsWorks Stacks Operating Systems <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-os.html>`__ .

       

      The default option is the current Amazon Linux version. If you set this parameter to ``Custom`` , you must use the AmiId parameter to specify the custom AMI that you want to use. For more information on the supported operating systems, see `Operating Systems <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-os.html>`__ . For more information on how to use custom AMIs with OpsWorks, see `Using Custom AMIs <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-custom-ami.html>`__ .

       

      .. note::

         

        You can specify a different Linux operating system for the updated stack, but you cannot change from Linux to Windows or Windows to Linux.

         

      

    
    :type AmiId: string
    :param AmiId: 

      The ID of the AMI that was used to create the instance. The value of this parameter must be the same AMI ID that the instance is already using. You cannot apply a new AMI to an instance by running UpdateInstance. UpdateInstance does not work on instances that are using custom AMIs. 

      

    
    :type SshKeyName: string
    :param SshKeyName: 

      The instance's Amazon EC2 key name.

      

    
    :type Architecture: string
    :param Architecture: 

      The instance architecture. Instance types do not necessarily support both architectures. For a list of the architectures that are supported by the different instance types, see `Instance Families and Types <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html>`__ .

      

    
    :type InstallUpdatesOnBoot: boolean
    :param InstallUpdatesOnBoot: 

      Whether to install operating system and package updates when the instance boots. The default value is ``true`` . To control when updates are installed, set this value to ``false`` . You must then update your instances manually by using  CreateDeployment to run the ``update_dependencies`` stack command or by manually running ``yum`` (Amazon Linux) or ``apt-get`` (Ubuntu) on the instances. 

       

      .. note::

         

        We strongly recommend using the default value of ``true`` , to ensure that your instances have the latest security updates.

         

      

    
    :type EbsOptimized: boolean
    :param EbsOptimized: 

      This property cannot be updated.

      

    
    :type AgentVersion: string
    :param AgentVersion: 

      The default AWS OpsWorks Stacks agent version. You have the following options:

       

       
      * ``INHERIT`` - Use the stack's default agent version setting. 
       
      * *version_number* - Use the specified agent version. This value overrides the stack's default setting. To update the agent version, you must edit the instance configuration and specify a new version. AWS OpsWorks Stacks then automatically installs that version on the instance. 
       

       

      The default setting is ``INHERIT`` . To specify an agent version, you must use the complete version number, not the abbreviated number shown on the console. For a list of available agent version numbers, call  DescribeAgentVersions .

       

      AgentVersion cannot be set to Chef 12.2.

      

    
    
    :returns: None

  .. py:method:: update_layer(**kwargs)

    

    Updates a specified layer.

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/UpdateLayer>`_    


    **Request Syntax** 
    ::

      response = client.update_layer(
          LayerId='string',
          Name='string',
          Shortname='string',
          Attributes={
              'string': 'string'
          },
          CloudWatchLogsConfiguration={
              'Enabled': True|False,
              'LogStreams': [
                  {
                      'LogGroupName': 'string',
                      'DatetimeFormat': 'string',
                      'TimeZone': 'LOCAL'|'UTC',
                      'File': 'string',
                      'FileFingerprintLines': 'string',
                      'MultiLineStartPattern': 'string',
                      'InitialPosition': 'start_of_file'|'end_of_file',
                      'Encoding': 'ascii'|'big5'|'big5hkscs'|'cp037'|'cp424'|'cp437'|'cp500'|'cp720'|'cp737'|'cp775'|'cp850'|'cp852'|'cp855'|'cp856'|'cp857'|'cp858'|'cp860'|'cp861'|'cp862'|'cp863'|'cp864'|'cp865'|'cp866'|'cp869'|'cp874'|'cp875'|'cp932'|'cp949'|'cp950'|'cp1006'|'cp1026'|'cp1140'|'cp1250'|'cp1251'|'cp1252'|'cp1253'|'cp1254'|'cp1255'|'cp1256'|'cp1257'|'cp1258'|'euc_jp'|'euc_jis_2004'|'euc_jisx0213'|'euc_kr'|'gb2312'|'gbk'|'gb18030'|'hz'|'iso2022_jp'|'iso2022_jp_1'|'iso2022_jp_2'|'iso2022_jp_2004'|'iso2022_jp_3'|'iso2022_jp_ext'|'iso2022_kr'|'latin_1'|'iso8859_2'|'iso8859_3'|'iso8859_4'|'iso8859_5'|'iso8859_6'|'iso8859_7'|'iso8859_8'|'iso8859_9'|'iso8859_10'|'iso8859_13'|'iso8859_14'|'iso8859_15'|'iso8859_16'|'johab'|'koi8_r'|'koi8_u'|'mac_cyrillic'|'mac_greek'|'mac_iceland'|'mac_latin2'|'mac_roman'|'mac_turkish'|'ptcp154'|'shift_jis'|'shift_jis_2004'|'shift_jisx0213'|'utf_32'|'utf_32_be'|'utf_32_le'|'utf_16'|'utf_16_be'|'utf_16_le'|'utf_7'|'utf_8'|'utf_8_sig',
                      'BufferDuration': 123,
                      'BatchCount': 123,
                      'BatchSize': 123
                  },
              ]
          },
          CustomInstanceProfileArn='string',
          CustomJson='string',
          CustomSecurityGroupIds=[
              'string',
          ],
          Packages=[
              'string',
          ],
          VolumeConfigurations=[
              {
                  'MountPoint': 'string',
                  'RaidLevel': 123,
                  'NumberOfDisks': 123,
                  'Size': 123,
                  'VolumeType': 'string',
                  'Iops': 123
              },
          ],
          EnableAutoHealing=True|False,
          AutoAssignElasticIps=True|False,
          AutoAssignPublicIps=True|False,
          CustomRecipes={
              'Setup': [
                  'string',
              ],
              'Configure': [
                  'string',
              ],
              'Deploy': [
                  'string',
              ],
              'Undeploy': [
                  'string',
              ],
              'Shutdown': [
                  'string',
              ]
          },
          InstallUpdatesOnBoot=True|False,
          UseEbsOptimizedInstances=True|False,
          LifecycleEventConfiguration={
              'Shutdown': {
                  'ExecutionTimeout': 123,
                  'DelayUntilElbConnectionsDrained': True|False
              }
          }
      )
    :type LayerId: string
    :param LayerId: **[REQUIRED]** 

      The layer ID.

      

    
    :type Name: string
    :param Name: 

      The layer name, which is used by the console.

      

    
    :type Shortname: string
    :param Shortname: 

      For custom layers only, use this parameter to specify the layer's short name, which is used internally by AWS OpsWorks Stacks and by Chef. The short name is also used as the name for the directory where your app files are installed. It can have a maximum of 200 characters and must be in the following format: /\A[a-z0-9\-\_\.]+\Z/.

       

      The built-in layers' short names are defined by AWS OpsWorks Stacks. For more information, see the `Layer Reference <http://docs.aws.amazon.com/opsworks/latest/userguide/layers.html>`__  

      

    
    :type Attributes: dict
    :param Attributes: 

      One or more user-defined key/value pairs to be added to the stack attributes.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type CloudWatchLogsConfiguration: dict
    :param CloudWatchLogsConfiguration: 

      Specifies CloudWatch Logs configuration options for the layer. For more information, see  CloudWatchLogsLogStream .

      

    
      - **Enabled** *(boolean) --* 

        Whether CloudWatch Logs is enabled for a layer.

        

      
      - **LogStreams** *(list) --* 

        A list of configuration options for CloudWatch Logs.

        

      
        - *(dict) --* 

          Describes the Amazon CloudWatch logs configuration for a layer. For detailed information about members of this data type, see the `CloudWatch Logs Agent Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html>`__ .

          

        
          - **LogGroupName** *(string) --* 

            Specifies the destination log group. A log group is created automatically if it doesn't already exist. Log group names can be between 1 and 512 characters long. Allowed characters include a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), '/' (forward slash), and '.' (period).

            

          
          - **DatetimeFormat** *(string) --* 

            Specifies how the time stamp is extracted from logs. For more information, see the `CloudWatch Logs Agent Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html>`__ .

            

          
          - **TimeZone** *(string) --* 

            Specifies the time zone of log event time stamps.

            

          
          - **File** *(string) --* 

            Specifies log files that you want to push to CloudWatch Logs.

             

             ``File`` can point to a specific file or multiple files (by using wild card characters such as ``/var/log/system.log*`` ). Only the latest file is pushed to CloudWatch Logs, based on file modification time. We recommend that you use wild card characters to specify a series of files of the same type, such as ``access_log.2014-06-01-01`` , ``access_log.2014-06-01-02`` , and so on by using a pattern like ``access_log.*`` . Don't use a wildcard to match multiple file types, such as ``access_log_80`` and ``access_log_443`` . To specify multiple, different file types, add another log stream entry to the configuration file, so that each log file type is stored in a different log group.

             

            Zipped files are not supported.

            

          
          - **FileFingerprintLines** *(string) --* 

            Specifies the range of lines for identifying a file. The valid values are one number, or two dash-delimited numbers, such as '1', '2-5'. The default value is '1', meaning the first line is used to calculate the fingerprint. Fingerprint lines are not sent to CloudWatch Logs unless all specified lines are available.

            

          
          - **MultiLineStartPattern** *(string) --* 

            Specifies the pattern for identifying the start of a log message.

            

          
          - **InitialPosition** *(string) --* 

            Specifies where to start to read data (start_of_file or end_of_file). The default is start_of_file. This setting is only used if there is no state persisted for that log stream.

            

          
          - **Encoding** *(string) --* 

            Specifies the encoding of the log file so that the file can be read correctly. The default is ``utf_8`` . Encodings supported by Python ``codecs.decode()`` can be used here.

            

          
          - **BufferDuration** *(integer) --* 

            Specifies the time duration for the batching of log events. The minimum value is 5000ms and default value is 5000ms.

            

          
          - **BatchCount** *(integer) --* 

            Specifies the max number of log events in a batch, up to 10000. The default value is 1000.

            

          
          - **BatchSize** *(integer) --* 

            Specifies the maximum size of log events in a batch, in bytes, up to 1048576 bytes. The default value is 32768 bytes. This size is calculated as the sum of all event messages in UTF-8, plus 26 bytes for each log event.

            

          
        
    
    
    :type CustomInstanceProfileArn: string
    :param CustomInstanceProfileArn: 

      The ARN of an IAM profile to be used for all of the layer's EC2 instances. For more information about IAM ARNs, see `Using Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ .

      

    
    :type CustomJson: string
    :param CustomJson: 

      A JSON-formatted string containing custom stack configuration and deployment attributes to be installed on the layer's instances. For more information, see `Using Custom JSON <http://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook-json-override.html>`__ . 

      

    
    :type CustomSecurityGroupIds: list
    :param CustomSecurityGroupIds: 

      An array containing the layer's custom security group IDs.

      

    
      - *(string) --* 

      
  
    :type Packages: list
    :param Packages: 

      An array of ``Package`` objects that describe the layer's packages.

      

    
      - *(string) --* 

      
  
    :type VolumeConfigurations: list
    :param VolumeConfigurations: 

      A ``VolumeConfigurations`` object that describes the layer's Amazon EBS volumes.

      

    
      - *(dict) --* 

        Describes an Amazon EBS volume configuration.

        

      
        - **MountPoint** *(string) --* **[REQUIRED]** 

          The volume mount point. For example "/dev/sdh".

          

        
        - **RaidLevel** *(integer) --* 

          The volume `RAID level <http://en.wikipedia.org/wiki/Standard_RAID_levels>`__ .

          

        
        - **NumberOfDisks** *(integer) --* **[REQUIRED]** 

          The number of disks in the volume.

          

        
        - **Size** *(integer) --* **[REQUIRED]** 

          The volume size.

          

        
        - **VolumeType** *(string) --* 

          The volume type:

           

           
          * ``standard`` - Magnetic 
           
          * ``io1`` - Provisioned IOPS (SSD) 
           
          * ``gp2`` - General Purpose (SSD) 
           

          

        
        - **Iops** *(integer) --* 

          For PIOPS volumes, the IOPS per disk.

          

        
      
  
    :type EnableAutoHealing: boolean
    :param EnableAutoHealing: 

      Whether to disable auto healing for the layer.

      

    
    :type AutoAssignElasticIps: boolean
    :param AutoAssignElasticIps: 

      Whether to automatically assign an `Elastic IP address <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html>`__ to the layer's instances. For more information, see `How to Edit a Layer <http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-edit.html>`__ .

      

    
    :type AutoAssignPublicIps: boolean
    :param AutoAssignPublicIps: 

      For stacks that are running in a VPC, whether to automatically assign a public IP address to the layer's instances. For more information, see `How to Edit a Layer <http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-edit.html>`__ .

      

    
    :type CustomRecipes: dict
    :param CustomRecipes: 

      A ``LayerCustomRecipes`` object that specifies the layer's custom recipes.

      

    
      - **Setup** *(list) --* 

        An array of custom recipe names to be run following a ``setup`` event.

        

      
        - *(string) --* 

        
    
      - **Configure** *(list) --* 

        An array of custom recipe names to be run following a ``configure`` event.

        

      
        - *(string) --* 

        
    
      - **Deploy** *(list) --* 

        An array of custom recipe names to be run following a ``deploy`` event.

        

      
        - *(string) --* 

        
    
      - **Undeploy** *(list) --* 

        An array of custom recipe names to be run following a ``undeploy`` event.

        

      
        - *(string) --* 

        
    
      - **Shutdown** *(list) --* 

        An array of custom recipe names to be run following a ``shutdown`` event.

        

      
        - *(string) --* 

        
    
    
    :type InstallUpdatesOnBoot: boolean
    :param InstallUpdatesOnBoot: 

      Whether to install operating system and package updates when the instance boots. The default value is ``true`` . To control when updates are installed, set this value to ``false`` . You must then update your instances manually by using  CreateDeployment to run the ``update_dependencies`` stack command or manually running ``yum`` (Amazon Linux) or ``apt-get`` (Ubuntu) on the instances. 

       

      .. note::

         

        We strongly recommend using the default value of ``true`` , to ensure that your instances have the latest security updates.

         

      

    
    :type UseEbsOptimizedInstances: boolean
    :param UseEbsOptimizedInstances: 

      Whether to use Amazon EBS-optimized instances.

      

    
    :type LifecycleEventConfiguration: dict
    :param LifecycleEventConfiguration: 

      

      

    
      - **Shutdown** *(dict) --* 

        A ``ShutdownEventConfiguration`` object that specifies the Shutdown event configuration.

        

      
        - **ExecutionTimeout** *(integer) --* 

          The time, in seconds, that AWS OpsWorks Stacks will wait after triggering a Shutdown event before shutting down an instance.

          

        
        - **DelayUntilElbConnectionsDrained** *(boolean) --* 

          Whether to enable Elastic Load Balancing connection draining. For more information, see `Connection Draining <http://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/TerminologyandKeyConcepts.html#conn-drain>`__  

          

        
      
    
    
    :returns: None

  .. py:method:: update_my_user_profile(**kwargs)

    

    Updates a user's SSH public key.

     

     **Required Permissions** : To use this action, an IAM user must have self-management enabled or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/UpdateMyUserProfile>`_    


    **Request Syntax** 
    ::

      response = client.update_my_user_profile(
          SshPublicKey='string'
      )
    :type SshPublicKey: string
    :param SshPublicKey: 

      The user's SSH public key.

      

    
    
    :returns: None

  .. py:method:: update_rds_db_instance(**kwargs)

    

    Updates an Amazon RDS instance.

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/UpdateRdsDbInstance>`_    


    **Request Syntax** 
    ::

      response = client.update_rds_db_instance(
          RdsDbInstanceArn='string',
          DbUser='string',
          DbPassword='string'
      )
    :type RdsDbInstanceArn: string
    :param RdsDbInstanceArn: **[REQUIRED]** 

      The Amazon RDS instance's ARN.

      

    
    :type DbUser: string
    :param DbUser: 

      The master user name.

      

    
    :type DbPassword: string
    :param DbPassword: 

      The database password.

      

    
    
    :returns: None

  .. py:method:: update_stack(**kwargs)

    

    Updates a specified stack.

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/UpdateStack>`_    


    **Request Syntax** 
    ::

      response = client.update_stack(
          StackId='string',
          Name='string',
          Attributes={
              'string': 'string'
          },
          ServiceRoleArn='string',
          DefaultInstanceProfileArn='string',
          DefaultOs='string',
          HostnameTheme='string',
          DefaultAvailabilityZone='string',
          DefaultSubnetId='string',
          CustomJson='string',
          ConfigurationManager={
              'Name': 'string',
              'Version': 'string'
          },
          ChefConfiguration={
              'ManageBerkshelf': True|False,
              'BerkshelfVersion': 'string'
          },
          UseCustomCookbooks=True|False,
          CustomCookbooksSource={
              'Type': 'git'|'svn'|'archive'|'s3',
              'Url': 'string',
              'Username': 'string',
              'Password': 'string',
              'SshKey': 'string',
              'Revision': 'string'
          },
          DefaultSshKeyName='string',
          DefaultRootDeviceType='ebs'|'instance-store',
          UseOpsworksSecurityGroups=True|False,
          AgentVersion='string'
      )
    :type StackId: string
    :param StackId: **[REQUIRED]** 

      The stack ID.

      

    
    :type Name: string
    :param Name: 

      The stack's new name.

      

    
    :type Attributes: dict
    :param Attributes: 

      One or more user-defined key-value pairs to be added to the stack attributes.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type ServiceRoleArn: string
    :param ServiceRoleArn: 

      Do not use this parameter. You cannot update a stack's service role.

      

    
    :type DefaultInstanceProfileArn: string
    :param DefaultInstanceProfileArn: 

      The ARN of an IAM profile that is the default profile for all of the stack's EC2 instances. For more information about IAM ARNs, see `Using Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ .

      

    
    :type DefaultOs: string
    :param DefaultOs: 

      The stack's operating system, which must be set to one of the following:

       

       
      * A supported Linux operating system: An Amazon Linux version, such as ``Amazon Linux 2017.03`` , ``Amazon Linux 2016.09`` , ``Amazon Linux 2016.03`` , ``Amazon Linux 2015.09`` , or ``Amazon Linux 2015.03`` . 
       
      * A supported Ubuntu operating system, such as ``Ubuntu 16.04 LTS`` , ``Ubuntu 14.04 LTS`` , or ``Ubuntu 12.04 LTS`` . 
       
      * ``CentOS Linux 7``   
       
      * ``Red Hat Enterprise Linux 7``   
       
      * A supported Windows operating system, such as ``Microsoft Windows Server 2012 R2 Base`` , ``Microsoft Windows Server 2012 R2 with SQL Server Express`` , ``Microsoft Windows Server 2012 R2 with SQL Server Standard`` , or ``Microsoft Windows Server 2012 R2 with SQL Server Web`` . 
       
      * A custom AMI: ``Custom`` . You specify the custom AMI you want to use when you create instances. For more information on how to use custom AMIs with OpsWorks, see `Using Custom AMIs <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-custom-ami.html>`__ . 
       

       

      The default option is the stack's current operating system. For more information on the supported operating systems, see `AWS OpsWorks Stacks Operating Systems <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-os.html>`__ .

      

    
    :type HostnameTheme: string
    :param HostnameTheme: 

      The stack's new host name theme, with spaces replaced by underscores. The theme is used to generate host names for the stack's instances. By default, ``HostnameTheme`` is set to ``Layer_Dependent`` , which creates host names by appending integers to the layer's short name. The other themes are:

       

       
      * ``Baked_Goods``   
       
      * ``Clouds``   
       
      * ``Europe_Cities``   
       
      * ``Fruits``   
       
      * ``Greek_Deities``   
       
      * ``Legendary_creatures_from_Japan``   
       
      * ``Planets_and_Moons``   
       
      * ``Roman_Deities``   
       
      * ``Scottish_Islands``   
       
      * ``US_Cities``   
       
      * ``Wild_Cats``   
       

       

      To obtain a generated host name, call ``GetHostNameSuggestion`` , which returns a host name based on the current theme.

      

    
    :type DefaultAvailabilityZone: string
    :param DefaultAvailabilityZone: 

      The stack's default Availability Zone, which must be in the stack's region. For more information, see `Regions and Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html>`__ . If you also specify a value for ``DefaultSubnetId`` , the subnet must be in the same zone. For more information, see  CreateStack . 

      

    
    :type DefaultSubnetId: string
    :param DefaultSubnetId: 

      The stack's default VPC subnet ID. This parameter is required if you specify a value for the ``VpcId`` parameter. All instances are launched into this subnet unless you specify otherwise when you create the instance. If you also specify a value for ``DefaultAvailabilityZone`` , the subnet must be in that zone. For information on default values and when this parameter is required, see the ``VpcId`` parameter description. 

      

    
    :type CustomJson: string
    :param CustomJson: 

      A string that contains user-defined, custom JSON. It can be used to override the corresponding default stack configuration JSON values or to pass data to recipes. The string should be in the following format:

       

       ``"{\"key1\": \"value1\", \"key2\": \"value2\",...}"``  

       

      For more information on custom JSON, see `Use Custom JSON to Modify the Stack Configuration Attributes <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-json.html>`__ .

      

    
    :type ConfigurationManager: dict
    :param ConfigurationManager: 

      The configuration manager. When you update a stack, we recommend that you use the configuration manager to specify the Chef version: 12, 11.10, or 11.4 for Linux stacks, or 12.2 for Windows stacks. The default value for Linux stacks is currently 11.4.

      

    
      - **Name** *(string) --* 

        The name. This parameter must be set to "Chef".

        

      
      - **Version** *(string) --* 

        The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to 12.2 for Windows stacks. The default value for Linux stacks is 11.4.

        

      
    
    :type ChefConfiguration: dict
    :param ChefConfiguration: 

      A ``ChefConfiguration`` object that specifies whether to enable Berkshelf and the Berkshelf version on Chef 11.10 stacks. For more information, see `Create a New Stack <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`__ .

      

    
      - **ManageBerkshelf** *(boolean) --* 

        Whether to enable Berkshelf.

        

      
      - **BerkshelfVersion** *(string) --* 

        The Berkshelf version.

        

      
    
    :type UseCustomCookbooks: boolean
    :param UseCustomCookbooks: 

      Whether the stack uses custom cookbooks.

      

    
    :type CustomCookbooksSource: dict
    :param CustomCookbooksSource: 

      Contains the information required to retrieve an app or cookbook from a repository. For more information, see `Creating Apps <http://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html>`__ or `Custom Recipes and Cookbooks <http://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html>`__ .

      

    
      - **Type** *(string) --* 

        The repository type.

        

      
      - **Url** *(string) --* 

        The source URL. The following is an example of an Amazon S3 source URL: ``https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz`` .

        

      
      - **Username** *(string) --* 

        This parameter depends on the repository type.

         

         
        * For Amazon S3 bundles, set ``Username`` to the appropriate IAM access key ID. 
         
        * For HTTP bundles, Git repositories, and Subversion repositories, set ``Username`` to the user name. 
         

        

      
      - **Password** *(string) --* 

        When included in a request, the parameter depends on the repository type.

         

         
        * For Amazon S3 bundles, set ``Password`` to the appropriate IAM secret access key. 
         
        * For HTTP bundles and Subversion repositories, set ``Password`` to the password. 
         

         

        For more information on how to safely handle IAM credentials, see `http\://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html <http://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html>`__ .

         

        In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

        

      
      - **SshKey** *(string) --* 

        In requests, the repository's SSH key.

         

        In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

        

      
      - **Revision** *(string) --* 

        The application's version. AWS OpsWorks Stacks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.

        

      
    
    :type DefaultSshKeyName: string
    :param DefaultSshKeyName: 

      A default Amazon EC2 key-pair name. The default value is ``none`` . If you specify a key-pair name, AWS OpsWorks Stacks installs the public key on the instance and you can use the private key with an SSH client to log in to the instance. For more information, see `Using SSH to Communicate with an Instance <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-ssh.html>`__ and `Managing SSH Access <http://docs.aws.amazon.com/opsworks/latest/userguide/security-ssh-access.html>`__ . You can override this setting by specifying a different key pair, or no key pair, when you `create an instance <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-add.html>`__ . 

      

    
    :type DefaultRootDeviceType: string
    :param DefaultRootDeviceType: 

      The default root device type. This value is used by default for all instances in the stack, but you can override it when you create an instance. For more information, see `Storage for the Root Device <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-for-the-root-device>`__ .

      

    
    :type UseOpsworksSecurityGroups: boolean
    :param UseOpsworksSecurityGroups: 

      Whether to associate the AWS OpsWorks Stacks built-in security groups with the stack's layers.

       

      AWS OpsWorks Stacks provides a standard set of built-in security groups, one for each layer, which are associated with layers by default. ``UseOpsworksSecurityGroups`` allows you to provide your own custom security groups instead of using the built-in groups. ``UseOpsworksSecurityGroups`` has the following settings: 

       

       
      * True - AWS OpsWorks Stacks automatically associates the appropriate built-in security group with each layer (default setting). You can associate additional security groups with a layer after you create it, but you cannot delete the built-in security group. 
       
      * False - AWS OpsWorks Stacks does not associate built-in security groups with layers. You must create appropriate EC2 security groups and associate a security group with each layer that you create. However, you can still manually associate a built-in security group with a layer on. Custom security groups are required only for those layers that need custom settings. 
       

       

      For more information, see `Create a New Stack <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`__ .

      

    
    :type AgentVersion: string
    :param AgentVersion: 

      The default AWS OpsWorks Stacks agent version. You have the following options:

       

       
      * Auto-update - Set this parameter to ``LATEST`` . AWS OpsWorks Stacks automatically installs new agent versions on the stack's instances as soon as they are available. 
       
      * Fixed version - Set this parameter to your preferred agent version. To update the agent version, you must edit the stack configuration and specify a new version. AWS OpsWorks Stacks then automatically installs that version on the stack's instances. 
       

       

      The default setting is ``LATEST`` . To specify an agent version, you must use the complete version number, not the abbreviated number shown on the console. For a list of available agent version numbers, call  DescribeAgentVersions . AgentVersion cannot be set to Chef 12.2.

       

      .. note::

         

        You can also specify an agent version when you create or update an instance, which overrides the stack's default setting.

         

      

    
    
    :returns: None

  .. py:method:: update_user_profile(**kwargs)

    

    Updates a specified user profile.

     

     **Required Permissions** : To use this action, an IAM user must have an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/UpdateUserProfile>`_    


    **Request Syntax** 
    ::

      response = client.update_user_profile(
          IamUserArn='string',
          SshUsername='string',
          SshPublicKey='string',
          AllowSelfManagement=True|False
      )
    :type IamUserArn: string
    :param IamUserArn: **[REQUIRED]** 

      The user IAM ARN. This can also be a federated user's ARN.

      

    
    :type SshUsername: string
    :param SshUsername: 

      The user's SSH user name. The allowable characters are [a-z], [A-Z], [0-9], '-', and '_'. If the specified name includes other punctuation marks, AWS OpsWorks Stacks removes them. For example, ``my.name`` will be changed to ``myname`` . If you do not specify an SSH user name, AWS OpsWorks Stacks generates one from the IAM user name. 

      

    
    :type SshPublicKey: string
    :param SshPublicKey: 

      The user's new SSH public key.

      

    
    :type AllowSelfManagement: boolean
    :param AllowSelfManagement: 

      Whether users can specify their own SSH public key through the My Settings page. For more information, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/security-settingsshkey.html>`__ .

      

    
    
    :returns: None

  .. py:method:: update_volume(**kwargs)

    

    Updates an Amazon EBS volume's name or mount point. For more information, see `Resource Management <http://docs.aws.amazon.com/opsworks/latest/userguide/resources.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/UpdateVolume>`_    


    **Request Syntax** 
    ::

      response = client.update_volume(
          VolumeId='string',
          Name='string',
          MountPoint='string'
      )
    :type VolumeId: string
    :param VolumeId: **[REQUIRED]** 

      The volume ID.

      

    
    :type Name: string
    :param Name: 

      The new name.

      

    
    :type MountPoint: string
    :param MountPoint: 

      The new mount point.

      

    
    
    :returns: None

==========
Paginators
==========


The available paginators are:

* :py:class:`OpsWorks.Paginator.DescribeEcsClusters`



.. py:class:: OpsWorks.Paginator.DescribeEcsClusters

  ::

    
    paginator = client.get_paginator('describe_ecs_clusters')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`OpsWorks.Client.describe_ecs_clusters`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeEcsClusters>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          EcsClusterArns=[
              'string',
          ],
          StackId='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type EcsClusterArns: list
    :param EcsClusterArns: 

      A list of ARNs, one for each cluster to be described.

      

    
      - *(string) --* 

      
  
    :type StackId: string
    :param StackId: 

      A stack ID. ``DescribeEcsClusters`` returns a description of the cluster that is registered with the stack.

      

    
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
            'EcsClusters': [
                {
                    'EcsClusterArn': 'string',
                    'EcsClusterName': 'string',
                    'StackId': 'string',
                    'RegisteredAt': 'string'
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the response to a ``DescribeEcsClusters`` request.

        
        

        - **EcsClusters** *(list) --* 

          A list of ``EcsCluster`` objects containing the cluster descriptions.

          
          

          - *(dict) --* 

            Describes a registered Amazon ECS cluster.

            
            

            - **EcsClusterArn** *(string) --* 

              The cluster's ARN.

              
            

            - **EcsClusterName** *(string) --* 

              The cluster name.

              
            

            - **StackId** *(string) --* 

              The stack ID.

              
            

            - **RegisteredAt** *(string) --* 

              The time and date that the cluster was registered with the stack.

              
        
      
    

=======
Waiters
=======


The available waiters are:

* :py:class:`OpsWorks.Waiter.AppExists`


* :py:class:`OpsWorks.Waiter.DeploymentSuccessful`


* :py:class:`OpsWorks.Waiter.InstanceOnline`


* :py:class:`OpsWorks.Waiter.InstanceRegistered`


* :py:class:`OpsWorks.Waiter.InstanceStopped`


* :py:class:`OpsWorks.Waiter.InstanceTerminated`



.. py:class:: OpsWorks.Waiter.AppExists

  ::

    
    waiter = client.get_waiter('app_exists')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`OpsWorks.Client.describe_apps` every 1 seconds until a successful state is reached. An error is returned after 40 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeApps>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          StackId='string',
          AppIds=[
              'string',
          ],
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type StackId: string
    :param StackId: 

      The app stack ID. If you use this parameter, ``DescribeApps`` returns a description of the apps in the specified stack.

      

    
    :type AppIds: list
    :param AppIds: 

      An array of app IDs for the apps to be described. If you use this parameter, ``DescribeApps`` returns a description of the specified apps. Otherwise, it returns a description of every app.

      

    
      - *(string) --* 

      
  
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 1

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 40

        

      
    
    
    :returns: None

.. py:class:: OpsWorks.Waiter.DeploymentSuccessful

  ::

    
    waiter = client.get_waiter('deployment_successful')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`OpsWorks.Client.describe_deployments` every 15 seconds until a successful state is reached. An error is returned after 40 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeDeployments>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          StackId='string',
          AppId='string',
          DeploymentIds=[
              'string',
          ],
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type StackId: string
    :param StackId: 

      The stack ID. If you include this parameter, ``DescribeDeployments`` returns a description of the commands associated with the specified stack.

      

    
    :type AppId: string
    :param AppId: 

      The app ID. If you include this parameter, ``DescribeDeployments`` returns a description of the commands associated with the specified app.

      

    
    :type DeploymentIds: list
    :param DeploymentIds: 

      An array of deployment IDs to be described. If you include this parameter, ``DescribeDeployments`` returns a description of the specified deployments. Otherwise, it returns a description of every deployment.

      

    
      - *(string) --* 

      
  
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 15

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 40

        

      
    
    
    :returns: None

.. py:class:: OpsWorks.Waiter.InstanceOnline

  ::

    
    waiter = client.get_waiter('instance_online')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`OpsWorks.Client.describe_instances` every 15 seconds until a successful state is reached. An error is returned after 40 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeInstances>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          StackId='string',
          LayerId='string',
          InstanceIds=[
              'string',
          ],
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type StackId: string
    :param StackId: 

      A stack ID. If you use this parameter, ``DescribeInstances`` returns descriptions of the instances associated with the specified stack.

      

    
    :type LayerId: string
    :param LayerId: 

      A layer ID. If you use this parameter, ``DescribeInstances`` returns descriptions of the instances associated with the specified layer.

      

    
    :type InstanceIds: list
    :param InstanceIds: 

      An array of instance IDs to be described. If you use this parameter, ``DescribeInstances`` returns a description of the specified instances. Otherwise, it returns a description of every instance.

      

    
      - *(string) --* 

      
  
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 15

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 40

        

      
    
    
    :returns: None

.. py:class:: OpsWorks.Waiter.InstanceRegistered

  ::

    
    waiter = client.get_waiter('instance_registered')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`OpsWorks.Client.describe_instances` every 15 seconds until a successful state is reached. An error is returned after 40 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeInstances>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          StackId='string',
          LayerId='string',
          InstanceIds=[
              'string',
          ],
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type StackId: string
    :param StackId: 

      A stack ID. If you use this parameter, ``DescribeInstances`` returns descriptions of the instances associated with the specified stack.

      

    
    :type LayerId: string
    :param LayerId: 

      A layer ID. If you use this parameter, ``DescribeInstances`` returns descriptions of the instances associated with the specified layer.

      

    
    :type InstanceIds: list
    :param InstanceIds: 

      An array of instance IDs to be described. If you use this parameter, ``DescribeInstances`` returns a description of the specified instances. Otherwise, it returns a description of every instance.

      

    
      - *(string) --* 

      
  
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 15

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 40

        

      
    
    
    :returns: None

.. py:class:: OpsWorks.Waiter.InstanceStopped

  ::

    
    waiter = client.get_waiter('instance_stopped')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`OpsWorks.Client.describe_instances` every 15 seconds until a successful state is reached. An error is returned after 40 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeInstances>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          StackId='string',
          LayerId='string',
          InstanceIds=[
              'string',
          ],
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type StackId: string
    :param StackId: 

      A stack ID. If you use this parameter, ``DescribeInstances`` returns descriptions of the instances associated with the specified stack.

      

    
    :type LayerId: string
    :param LayerId: 

      A layer ID. If you use this parameter, ``DescribeInstances`` returns descriptions of the instances associated with the specified layer.

      

    
    :type InstanceIds: list
    :param InstanceIds: 

      An array of instance IDs to be described. If you use this parameter, ``DescribeInstances`` returns a description of the specified instances. Otherwise, it returns a description of every instance.

      

    
      - *(string) --* 

      
  
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 15

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 40

        

      
    
    
    :returns: None

.. py:class:: OpsWorks.Waiter.InstanceTerminated

  ::

    
    waiter = client.get_waiter('instance_terminated')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`OpsWorks.Client.describe_instances` every 15 seconds until a successful state is reached. An error is returned after 40 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeInstances>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          StackId='string',
          LayerId='string',
          InstanceIds=[
              'string',
          ],
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type StackId: string
    :param StackId: 

      A stack ID. If you use this parameter, ``DescribeInstances`` returns descriptions of the instances associated with the specified stack.

      

    
    :type LayerId: string
    :param LayerId: 

      A layer ID. If you use this parameter, ``DescribeInstances`` returns descriptions of the instances associated with the specified layer.

      

    
    :type InstanceIds: list
    :param InstanceIds: 

      An array of instance IDs to be described. If you use this parameter, ``DescribeInstances`` returns a description of the specified instances. Otherwise, it returns a description of every instance.

      

    
      - *(string) --* 

      
  
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 15

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 40

        

      
    
    
    :returns: None

================
Service Resource
================



.. py:class:: OpsWorks.ServiceResource()

  A resource representing AWS OpsWorks::

    
    import boto3
    
    opsworks = boto3.resource('opsworks')

  
  These are the resource's available actions:
  
  *   :py:meth:`create_stack()`

  
  *   :py:meth:`get_available_subresources()`

  
  These are the resource's available sub-resources:
  
  *   :py:meth:`Layer()`

  
  *   :py:meth:`Stack()`

  
  *   :py:meth:`StackSummary()`

  
  These are the resource's available collections:
  
  *   :py:attr:`stacks`

  
  .. rst-class:: admonition-title
  
  Actions
  
  Actions call operations on resources.  They may automatically handle the passing in of arguments set from identifiers and some attributes.
  For more information about actions refer to the :ref:`Resources Introduction Guide<actions_intro>`.
  

  .. py:method:: create_stack(**kwargs)

    

    Creates a new stack. For more information, see `Create a New Stack <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-edit.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/CreateStack>`_    


    **Request Syntax** 
    ::

      stack = opsworks.create_stack(
          Name='string',
          Region='string',
          VpcId='string',
          Attributes={
              'string': 'string'
          },
          ServiceRoleArn='string',
          DefaultInstanceProfileArn='string',
          DefaultOs='string',
          HostnameTheme='string',
          DefaultAvailabilityZone='string',
          DefaultSubnetId='string',
          CustomJson='string',
          ConfigurationManager={
              'Name': 'string',
              'Version': 'string'
          },
          ChefConfiguration={
              'ManageBerkshelf': True|False,
              'BerkshelfVersion': 'string'
          },
          UseCustomCookbooks=True|False,
          UseOpsworksSecurityGroups=True|False,
          CustomCookbooksSource={
              'Type': 'git'|'svn'|'archive'|'s3',
              'Url': 'string',
              'Username': 'string',
              'Password': 'string',
              'SshKey': 'string',
              'Revision': 'string'
          },
          DefaultSshKeyName='string',
          DefaultRootDeviceType='ebs'|'instance-store',
          AgentVersion='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The stack name.

      

    
    :type Region: string
    :param Region: **[REQUIRED]** 

      The stack's AWS region, such as "ap-south-1". For more information about Amazon regions, see `Regions and Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html>`__ .

      

    
    :type VpcId: string
    :param VpcId: 

      The ID of the VPC that the stack is to be launched into. The VPC must be in the stack's region. All instances are launched into this VPC. You cannot change the ID later.

       

       
      * If your account supports EC2-Classic, the default value is ``no VPC`` . 
       
      * If your account does not support EC2-Classic, the default value is the default VPC for the specified region. 
       

       

      If the VPC ID corresponds to a default VPC and you have specified either the ``DefaultAvailabilityZone`` or the ``DefaultSubnetId`` parameter only, AWS OpsWorks Stacks infers the value of the other parameter. If you specify neither parameter, AWS OpsWorks Stacks sets these parameters to the first valid Availability Zone for the specified region and the corresponding default VPC subnet ID, respectively.

       

      If you specify a nondefault VPC ID, note the following:

       

       
      * It must belong to a VPC in your account that is in the specified region. 
       
      * You must specify a value for ``DefaultSubnetId`` . 
       

       

      For more information on how to use AWS OpsWorks Stacks with a VPC, see `Running a Stack in a VPC <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-vpc.html>`__ . For more information on default VPC and EC2-Classic, see `Supported Platforms <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-platforms.html>`__ . 

      

    
    :type Attributes: dict
    :param Attributes: 

      One or more user-defined key-value pairs to be added to the stack attributes.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type ServiceRoleArn: string
    :param ServiceRoleArn: **[REQUIRED]** 

      The stack's AWS Identity and Access Management (IAM) role, which allows AWS OpsWorks Stacks to work with AWS resources on your behalf. You must set this parameter to the Amazon Resource Name (ARN) for an existing IAM role. For more information about IAM ARNs, see `Using Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ .

      

    
    :type DefaultInstanceProfileArn: string
    :param DefaultInstanceProfileArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of an IAM profile that is the default profile for all of the stack's EC2 instances. For more information about IAM ARNs, see `Using Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ .

      

    
    :type DefaultOs: string
    :param DefaultOs: 

      The stack's default operating system, which is installed on every instance unless you specify a different operating system when you create the instance. You can specify one of the following.

       

       
      * A supported Linux operating system: An Amazon Linux version, such as ``Amazon Linux 2017.03`` , ``Amazon Linux 2016.09`` , ``Amazon Linux 2016.03`` , ``Amazon Linux 2015.09`` , or ``Amazon Linux 2015.03`` . 
       
      * A supported Ubuntu operating system, such as ``Ubuntu 16.04 LTS`` , ``Ubuntu 14.04 LTS`` , or ``Ubuntu 12.04 LTS`` . 
       
      * ``CentOS Linux 7``   
       
      * ``Red Hat Enterprise Linux 7``   
       
      * A supported Windows operating system, such as ``Microsoft Windows Server 2012 R2 Base`` , ``Microsoft Windows Server 2012 R2 with SQL Server Express`` , ``Microsoft Windows Server 2012 R2 with SQL Server Standard`` , or ``Microsoft Windows Server 2012 R2 with SQL Server Web`` . 
       
      * A custom AMI: ``Custom`` . You specify the custom AMI you want to use when you create instances. For more information, see `Using Custom AMIs <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-custom-ami.html>`__ . 
       

       

      The default option is the current Amazon Linux version. For more information on the supported operating systems, see `AWS OpsWorks Stacks Operating Systems <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-os.html>`__ .

      

    
    :type HostnameTheme: string
    :param HostnameTheme: 

      The stack's host name theme, with spaces replaced by underscores. The theme is used to generate host names for the stack's instances. By default, ``HostnameTheme`` is set to ``Layer_Dependent`` , which creates host names by appending integers to the layer's short name. The other themes are:

       

       
      * ``Baked_Goods``   
       
      * ``Clouds``   
       
      * ``Europe_Cities``   
       
      * ``Fruits``   
       
      * ``Greek_Deities``   
       
      * ``Legendary_creatures_from_Japan``   
       
      * ``Planets_and_Moons``   
       
      * ``Roman_Deities``   
       
      * ``Scottish_Islands``   
       
      * ``US_Cities``   
       
      * ``Wild_Cats``   
       

       

      To obtain a generated host name, call ``GetHostNameSuggestion`` , which returns a host name based on the current theme.

      

    
    :type DefaultAvailabilityZone: string
    :param DefaultAvailabilityZone: 

      The stack's default Availability Zone, which must be in the specified region. For more information, see `Regions and Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html>`__ . If you also specify a value for ``DefaultSubnetId`` , the subnet must be in the same zone. For more information, see the ``VpcId`` parameter description. 

      

    
    :type DefaultSubnetId: string
    :param DefaultSubnetId: 

      The stack's default VPC subnet ID. This parameter is required if you specify a value for the ``VpcId`` parameter. All instances are launched into this subnet unless you specify otherwise when you create the instance. If you also specify a value for ``DefaultAvailabilityZone`` , the subnet must be in that zone. For information on default values and when this parameter is required, see the ``VpcId`` parameter description. 

      

    
    :type CustomJson: string
    :param CustomJson: 

      A string that contains user-defined, custom JSON. It can be used to override the corresponding default stack configuration attribute values or to pass data to recipes. The string should be in the following format:

       

       ``"{\"key1\": \"value1\", \"key2\": \"value2\",...}"``  

       

      For more information on custom JSON, see `Use Custom JSON to Modify the Stack Configuration Attributes <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-json.html>`__ .

      

    
    :type ConfigurationManager: dict
    :param ConfigurationManager: 

      The configuration manager. When you create a stack we recommend that you use the configuration manager to specify the Chef version: 12, 11.10, or 11.4 for Linux stacks, or 12.2 for Windows stacks. The default value for Linux stacks is currently 11.4.

      

    
      - **Name** *(string) --* 

        The name. This parameter must be set to "Chef".

        

      
      - **Version** *(string) --* 

        The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to 12.2 for Windows stacks. The default value for Linux stacks is 11.4.

        

      
    
    :type ChefConfiguration: dict
    :param ChefConfiguration: 

      A ``ChefConfiguration`` object that specifies whether to enable Berkshelf and the Berkshelf version on Chef 11.10 stacks. For more information, see `Create a New Stack <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`__ .

      

    
      - **ManageBerkshelf** *(boolean) --* 

        Whether to enable Berkshelf.

        

      
      - **BerkshelfVersion** *(string) --* 

        The Berkshelf version.

        

      
    
    :type UseCustomCookbooks: boolean
    :param UseCustomCookbooks: 

      Whether the stack uses custom cookbooks.

      

    
    :type UseOpsworksSecurityGroups: boolean
    :param UseOpsworksSecurityGroups: 

      Whether to associate the AWS OpsWorks Stacks built-in security groups with the stack's layers.

       

      AWS OpsWorks Stacks provides a standard set of built-in security groups, one for each layer, which are associated with layers by default. With ``UseOpsworksSecurityGroups`` you can instead provide your own custom security groups. ``UseOpsworksSecurityGroups`` has the following settings: 

       

       
      * True - AWS OpsWorks Stacks automatically associates the appropriate built-in security group with each layer (default setting). You can associate additional security groups with a layer after you create it, but you cannot delete the built-in security group. 
       
      * False - AWS OpsWorks Stacks does not associate built-in security groups with layers. You must create appropriate EC2 security groups and associate a security group with each layer that you create. However, you can still manually associate a built-in security group with a layer on creation; custom security groups are required only for those layers that need custom settings. 
       

       

      For more information, see `Create a New Stack <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`__ .

      

    
    :type CustomCookbooksSource: dict
    :param CustomCookbooksSource: 

      Contains the information required to retrieve an app or cookbook from a repository. For more information, see `Creating Apps <http://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html>`__ or `Custom Recipes and Cookbooks <http://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html>`__ .

      

    
      - **Type** *(string) --* 

        The repository type.

        

      
      - **Url** *(string) --* 

        The source URL. The following is an example of an Amazon S3 source URL: ``https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz`` .

        

      
      - **Username** *(string) --* 

        This parameter depends on the repository type.

         

         
        * For Amazon S3 bundles, set ``Username`` to the appropriate IAM access key ID. 
         
        * For HTTP bundles, Git repositories, and Subversion repositories, set ``Username`` to the user name. 
         

        

      
      - **Password** *(string) --* 

        When included in a request, the parameter depends on the repository type.

         

         
        * For Amazon S3 bundles, set ``Password`` to the appropriate IAM secret access key. 
         
        * For HTTP bundles and Subversion repositories, set ``Password`` to the password. 
         

         

        For more information on how to safely handle IAM credentials, see `http\://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html <http://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html>`__ .

         

        In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

        

      
      - **SshKey** *(string) --* 

        In requests, the repository's SSH key.

         

        In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

        

      
      - **Revision** *(string) --* 

        The application's version. AWS OpsWorks Stacks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.

        

      
    
    :type DefaultSshKeyName: string
    :param DefaultSshKeyName: 

      A default Amazon EC2 key pair name. The default value is none. If you specify a key pair name, AWS OpsWorks installs the public key on the instance and you can use the private key with an SSH client to log in to the instance. For more information, see `Using SSH to Communicate with an Instance <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-ssh.html>`__ and `Managing SSH Access <http://docs.aws.amazon.com/opsworks/latest/userguide/security-ssh-access.html>`__ . You can override this setting by specifying a different key pair, or no key pair, when you `create an instance <http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-add.html>`__ . 

      

    
    :type DefaultRootDeviceType: string
    :param DefaultRootDeviceType: 

      The default root device type. This value is the default for all instances in the stack, but you can override it when you create an instance. The default option is ``instance-store`` . For more information, see `Storage for the Root Device <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-for-the-root-device>`__ .

      

    
    :type AgentVersion: string
    :param AgentVersion: 

      The default AWS OpsWorks Stacks agent version. You have the following options:

       

       
      * Auto-update - Set this parameter to ``LATEST`` . AWS OpsWorks Stacks automatically installs new agent versions on the stack's instances as soon as they are available. 
       
      * Fixed version - Set this parameter to your preferred agent version. To update the agent version, you must edit the stack configuration and specify a new version. AWS OpsWorks Stacks then automatically installs that version on the stack's instances. 
       

       

      The default setting is the most recent release of the agent. To specify an agent version, you must use the complete version number, not the abbreviated number shown on the console. For a list of available agent version numbers, call  DescribeAgentVersions . AgentVersion cannot be set to Chef 12.2.

       

      .. note::

         

        You can also specify an agent version when you create or update an instance, which overrides the stack's default setting.

         

      

    
    
    :rtype: :py:class:`opsworks.Stack`
    :returns: Stack resource
    

  .. py:method:: get_available_subresources()

        
    Returns a list of all the available sub-resources for this
    Resource.
    
    :returns: A list containing the name of each sub-resource for this
        resource
    :rtype: list of str

  .. rst-class:: admonition-title
  
  Sub-resources
  
  Sub-resources are methods that create a new instance of a child resource. This resource's identifiers get passed along to the child.
  For more information about sub-resources refer to the :ref:`Resources Introduction Guide<subresources_intro>`.
  

  .. py:method:: Layer(id)

    Creates a Layer resource.::

      layer = opsworks.Layer('id')

    :type id: string
    :param id: The Layer's id identifier. This **must** be set.
    
    :rtype: :py:class:`OpsWorks.Layer`
    :returns: A Layer resource
    

  .. py:method:: Stack(id)

    Creates a Stack resource.::

      stack = opsworks.Stack('id')

    :type id: string
    :param id: The Stack's id identifier. This **must** be set.
    
    :rtype: :py:class:`OpsWorks.Stack`
    :returns: A Stack resource
    

  .. py:method:: StackSummary(stack_id)

    Creates a StackSummary resource.::

      stack_summary = opsworks.StackSummary('stack_id')

    :type stack_id: string
    :param stack_id: The StackSummary's stack_id identifier. This **must** be set.
    
    :rtype: :py:class:`OpsWorks.StackSummary`
    :returns: A StackSummary resource
    
  .. rst-class:: admonition-title
  
  Collections
  
  Collections provide an interface to iterate over and manipulate groups of resources. 
  For more information about collections refer to the :ref:`Resources Introduction Guide<guide_collections>`.
  

  .. py:attribute:: stacks

    A collection of Stack resources

    .. py:method:: all()

      Creates an iterable of all Stack resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeStacks>`_      


      **Request Syntax** 
      ::

        stack_iterator = opsworks.stacks.all()
        
      
      :rtype: list(:py:class:`opsworks.Stack`)
      :returns: A list of Stack resources
      

    .. py:method:: filter(**kwargs)

      Creates an iterable of all Stack resources in the collection filtered by kwargs passed to method.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeStacks>`_      


      **Request Syntax** 
      ::

        stack_iterator = opsworks.stacks.filter(
            StackIds=[
                'string',
            ]
        )
      :type StackIds: list
      :param StackIds: 

        An array of stack IDs that specify the stacks to be described. If you omit this parameter, ``DescribeStacks`` returns a description of every stack.

        

      
        - *(string) --* 

        
    
      
      :rtype: list(:py:class:`opsworks.Stack`)
      :returns: A list of Stack resources
      

    .. py:method:: limit(**kwargs)

      Creates an iterable up to a specified amount of Stack resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeStacks>`_      


      **Request Syntax** 
      ::

        stack_iterator = opsworks.stacks.limit(
            count=123
        )
      :type count: integer
      :param count: The limit to the number of resources in the iterable.

      
      
      :rtype: list(:py:class:`opsworks.Stack`)
      :returns: A list of Stack resources
      

    .. py:method:: page_size(**kwargs)

      Creates an iterable of all Stack resources in the collection, but limits the number of items returned by each service call by the specified amount.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeStacks>`_      


      **Request Syntax** 
      ::

        stack_iterator = opsworks.stacks.page_size(
            count=123
        )
      :type count: integer
      :param count: The number of items returned by each service call

      
      
      :rtype: list(:py:class:`opsworks.Stack`)
      :returns: A list of Stack resources
      

=====
Layer
=====



.. py:class:: OpsWorks.Layer(id)

  A resource representing an AWS OpsWorks Layer::

    
    import boto3
    
    opsworks = boto3.resource('opsworks')
    layer = opsworks.Layer('id')

  :type id: string
  :param id: The Layer's id identifier. This **must** be set.
  
  These are the resource's available identifiers:
  
  *   :py:attr:`id`

  
  These are the resource's available attributes:
  
  *   :py:attr:`arn`

  
  *   :py:attr:`attributes`

  
  *   :py:attr:`auto_assign_elastic_ips`

  
  *   :py:attr:`auto_assign_public_ips`

  
  *   :py:attr:`cloud_watch_logs_configuration`

  
  *   :py:attr:`created_at`

  
  *   :py:attr:`custom_instance_profile_arn`

  
  *   :py:attr:`custom_json`

  
  *   :py:attr:`custom_recipes`

  
  *   :py:attr:`custom_security_group_ids`

  
  *   :py:attr:`default_recipes`

  
  *   :py:attr:`default_security_group_names`

  
  *   :py:attr:`enable_auto_healing`

  
  *   :py:attr:`install_updates_on_boot`

  
  *   :py:attr:`layer_id`

  
  *   :py:attr:`lifecycle_event_configuration`

  
  *   :py:attr:`name`

  
  *   :py:attr:`packages`

  
  *   :py:attr:`shortname`

  
  *   :py:attr:`stack_id`

  
  *   :py:attr:`type`

  
  *   :py:attr:`use_ebs_optimized_instances`

  
  *   :py:attr:`volume_configurations`

  
  These are the resource's available references:
  
  *   :py:attr:`stack`

  
  These are the resource's available actions:
  
  *   :py:meth:`delete()`

  
  *   :py:meth:`get_available_subresources()`

  
  *   :py:meth:`load()`

  
  *   :py:meth:`reload()`

  
  .. rst-class:: admonition-title
  
  Identifiers
  
  Identifiers are properties of a resource that are set upon instantation of the resource.
  For more information about identifiers refer to the :ref:`Resources Introduction Guide<identifiers_attributes_intro>`.
  

  .. py:attribute:: id

    *(string)* The Layer's id identifier. This **must** be set.
  .. rst-class:: admonition-title
  
  Attributes
  
  Attributes provide access to the properties of a resource. Attributes are lazy-loaded the first time one is accessed via the :py:meth:`load` method.
  For more information about attributes refer to the :ref:`Resources Introduction Guide<identifiers_attributes_intro>`.
  

  .. py:attribute:: arn

    

    - *(string) --* 

  .. py:attribute:: attributes

    

    - *(dict) --* 

      The layer attributes.

       

      For the ``HaproxyStatsPassword`` , ``MysqlRootPassword`` , and ``GangliaPassword`` attributes, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value

       

      For an ECS Cluster layer, AWS OpsWorks Stacks the ``EcsClusterArn`` attribute is set to the cluster's ARN.

      
      

      - *(string) --* 
        

        - *(string) --* 
  


  .. py:attribute:: auto_assign_elastic_ips

    

    - *(boolean) --* 

      Whether to automatically assign an `Elastic IP address <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html>`__ to the layer's instances. For more information, see `How to Edit a Layer <http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-edit.html>`__ .

      

  .. py:attribute:: auto_assign_public_ips

    

    - *(boolean) --* 

      For stacks that are running in a VPC, whether to automatically assign a public IP address to the layer's instances. For more information, see `How to Edit a Layer <http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-edit.html>`__ .

      

  .. py:attribute:: cloud_watch_logs_configuration

    

    - *(dict) --* 

      The Amazon CloudWatch Logs configuration settings for the layer.

      
      

      - **Enabled** *(boolean) --* 

        Whether CloudWatch Logs is enabled for a layer.

        
      

      - **LogStreams** *(list) --* 

        A list of configuration options for CloudWatch Logs.

        
        

        - *(dict) --* 

          Describes the Amazon CloudWatch logs configuration for a layer. For detailed information about members of this data type, see the `CloudWatch Logs Agent Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html>`__ .

          
          

          - **LogGroupName** *(string) --* 

            Specifies the destination log group. A log group is created automatically if it doesn't already exist. Log group names can be between 1 and 512 characters long. Allowed characters include a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), '/' (forward slash), and '.' (period).

            
          

          - **DatetimeFormat** *(string) --* 

            Specifies how the time stamp is extracted from logs. For more information, see the `CloudWatch Logs Agent Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html>`__ .

            
          

          - **TimeZone** *(string) --* 

            Specifies the time zone of log event time stamps.

            
          

          - **File** *(string) --* 

            Specifies log files that you want to push to CloudWatch Logs.

             

             ``File`` can point to a specific file or multiple files (by using wild card characters such as ``/var/log/system.log*`` ). Only the latest file is pushed to CloudWatch Logs, based on file modification time. We recommend that you use wild card characters to specify a series of files of the same type, such as ``access_log.2014-06-01-01`` , ``access_log.2014-06-01-02`` , and so on by using a pattern like ``access_log.*`` . Don't use a wildcard to match multiple file types, such as ``access_log_80`` and ``access_log_443`` . To specify multiple, different file types, add another log stream entry to the configuration file, so that each log file type is stored in a different log group.

             

            Zipped files are not supported.

            
          

          - **FileFingerprintLines** *(string) --* 

            Specifies the range of lines for identifying a file. The valid values are one number, or two dash-delimited numbers, such as '1', '2-5'. The default value is '1', meaning the first line is used to calculate the fingerprint. Fingerprint lines are not sent to CloudWatch Logs unless all specified lines are available.

            
          

          - **MultiLineStartPattern** *(string) --* 

            Specifies the pattern for identifying the start of a log message.

            
          

          - **InitialPosition** *(string) --* 

            Specifies where to start to read data (start_of_file or end_of_file). The default is start_of_file. This setting is only used if there is no state persisted for that log stream.

            
          

          - **Encoding** *(string) --* 

            Specifies the encoding of the log file so that the file can be read correctly. The default is ``utf_8`` . Encodings supported by Python ``codecs.decode()`` can be used here.

            
          

          - **BufferDuration** *(integer) --* 

            Specifies the time duration for the batching of log events. The minimum value is 5000ms and default value is 5000ms.

            
          

          - **BatchCount** *(integer) --* 

            Specifies the max number of log events in a batch, up to 10000. The default value is 1000.

            
          

          - **BatchSize** *(integer) --* 

            Specifies the maximum size of log events in a batch, in bytes, up to 1048576 bytes. The default value is 32768 bytes. This size is calculated as the sum of all event messages in UTF-8, plus 26 bytes for each log event.

            
      
    
  

  .. py:attribute:: created_at

    

    - *(string) --* 

      Date when the layer was created.

      

  .. py:attribute:: custom_instance_profile_arn

    

    - *(string) --* 

      The ARN of the default IAM profile to be used for the layer's EC2 instances. For more information about IAM ARNs, see `Using Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ .

      

  .. py:attribute:: custom_json

    

    - *(string) --* 

      A JSON formatted string containing the layer's custom stack configuration and deployment attributes.

      

  .. py:attribute:: custom_recipes

    

    - *(dict) --* 

      A ``LayerCustomRecipes`` object that specifies the layer's custom recipes.

      
      

      - **Setup** *(list) --* 

        An array of custom recipe names to be run following a ``setup`` event.

        
        

        - *(string) --* 
    
      

      - **Configure** *(list) --* 

        An array of custom recipe names to be run following a ``configure`` event.

        
        

        - *(string) --* 
    
      

      - **Deploy** *(list) --* 

        An array of custom recipe names to be run following a ``deploy`` event.

        
        

        - *(string) --* 
    
      

      - **Undeploy** *(list) --* 

        An array of custom recipe names to be run following a ``undeploy`` event.

        
        

        - *(string) --* 
    
      

      - **Shutdown** *(list) --* 

        An array of custom recipe names to be run following a ``shutdown`` event.

        
        

        - *(string) --* 
    
  

  .. py:attribute:: custom_security_group_ids

    

    - *(list) --* 

      An array containing the layer's custom security group IDs.

      
      

      - *(string) --* 
  

  .. py:attribute:: default_recipes

    

    - *(dict) --* 

      AWS OpsWorks Stacks supports five lifecycle events: **setup** , **configuration** , **deploy** , **undeploy** , and **shutdown** . For each layer, AWS OpsWorks Stacks runs a set of standard recipes for each event. In addition, you can provide custom recipes for any or all layers and events. AWS OpsWorks Stacks runs custom event recipes after the standard recipes. ``LayerCustomRecipes`` specifies the custom recipes for a particular layer to be run in response to each of the five events. 

       

      To specify a recipe, use the cookbook's directory name in the repository followed by two colons and the recipe name, which is the recipe's file name without the .rb extension. For example: phpapp2::dbsetup specifies the dbsetup.rb recipe in the repository's phpapp2 folder.

      
      

      - **Setup** *(list) --* 

        An array of custom recipe names to be run following a ``setup`` event.

        
        

        - *(string) --* 
    
      

      - **Configure** *(list) --* 

        An array of custom recipe names to be run following a ``configure`` event.

        
        

        - *(string) --* 
    
      

      - **Deploy** *(list) --* 

        An array of custom recipe names to be run following a ``deploy`` event.

        
        

        - *(string) --* 
    
      

      - **Undeploy** *(list) --* 

        An array of custom recipe names to be run following a ``undeploy`` event.

        
        

        - *(string) --* 
    
      

      - **Shutdown** *(list) --* 

        An array of custom recipe names to be run following a ``shutdown`` event.

        
        

        - *(string) --* 
    
  

  .. py:attribute:: default_security_group_names

    

    - *(list) --* 

      An array containing the layer's security group names.

      
      

      - *(string) --* 
  

  .. py:attribute:: enable_auto_healing

    

    - *(boolean) --* 

      Whether auto healing is disabled for the layer.

      

  .. py:attribute:: install_updates_on_boot

    

    - *(boolean) --* 

      Whether to install operating system and package updates when the instance boots. The default value is ``true`` . If this value is set to ``false`` , you must then update your instances manually by using  CreateDeployment to run the ``update_dependencies`` stack command or manually running ``yum`` (Amazon Linux) or ``apt-get`` (Ubuntu) on the instances. 

       

      .. note::

         

        We strongly recommend using the default value of ``true`` , to ensure that your instances have the latest security updates.

         

      

  .. py:attribute:: layer_id

    

    - *(string) --* 

      The layer ID.

      

  .. py:attribute:: lifecycle_event_configuration

    

    - *(dict) --* 

      A ``LifeCycleEventConfiguration`` object that specifies the Shutdown event configuration.

      
      

      - **Shutdown** *(dict) --* 

        A ``ShutdownEventConfiguration`` object that specifies the Shutdown event configuration.

        
        

        - **ExecutionTimeout** *(integer) --* 

          The time, in seconds, that AWS OpsWorks Stacks will wait after triggering a Shutdown event before shutting down an instance.

          
        

        - **DelayUntilElbConnectionsDrained** *(boolean) --* 

          Whether to enable Elastic Load Balancing connection draining. For more information, see `Connection Draining <http://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/TerminologyandKeyConcepts.html#conn-drain>`__  

          
    
  

  .. py:attribute:: name

    

    - *(string) --* 

      The layer name.

      

  .. py:attribute:: packages

    

    - *(list) --* 

      An array of ``Package`` objects that describe the layer's packages.

      
      

      - *(string) --* 
  

  .. py:attribute:: shortname

    

    - *(string) --* 

      The layer short name.

      

  .. py:attribute:: stack_id

    

    - *(string) --* 

      The layer stack ID.

      

  .. py:attribute:: type

    

    - *(string) --* 

      The layer type.

      

  .. py:attribute:: use_ebs_optimized_instances

    

    - *(boolean) --* 

      Whether the layer uses Amazon EBS-optimized instances.

      

  .. py:attribute:: volume_configurations

    

    - *(list) --* 

      A ``VolumeConfigurations`` object that describes the layer's Amazon EBS volumes.

      
      

      - *(dict) --* 

        Describes an Amazon EBS volume configuration.

        
        

        - **MountPoint** *(string) --* 

          The volume mount point. For example "/dev/sdh".

          
        

        - **RaidLevel** *(integer) --* 

          The volume `RAID level <http://en.wikipedia.org/wiki/Standard_RAID_levels>`__ .

          
        

        - **NumberOfDisks** *(integer) --* 

          The number of disks in the volume.

          
        

        - **Size** *(integer) --* 

          The volume size.

          
        

        - **VolumeType** *(string) --* 

          The volume type:

           

           
          * ``standard`` - Magnetic 
           
          * ``io1`` - Provisioned IOPS (SSD) 
           
          * ``gp2`` - General Purpose (SSD) 
           

          
        

        - **Iops** *(integer) --* 

          For PIOPS volumes, the IOPS per disk.

          
    
  
  .. rst-class:: admonition-title
  
  References
  
  References are related resource instances that have a belongs-to relationship.
  For more information about references refer to the :ref:`Resources Introduction Guide<references_intro>`.
  

  .. py:attribute:: stack

    (:py:class:`Stack`) The related stack if set, otherwise ``None``.
  .. rst-class:: admonition-title
  
  Actions
  
  Actions call operations on resources.  They may automatically handle the passing in of arguments set from identifiers and some attributes.
  For more information about actions refer to the :ref:`Resources Introduction Guide<actions_intro>`.
  

  .. py:method:: delete()

    

    Deletes a specified layer. You must first stop and then delete all associated instances or unassign registered instances. For more information, see `How to Delete a Layer <http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-delete.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DeleteLayer>`_    


    **Request Syntax** 
    ::

      response = layer.delete()
      
    
    :returns: None

  .. py:method:: get_available_subresources()

        
    Returns a list of all the available sub-resources for this
    Resource.
    
    :returns: A list containing the name of each sub-resource for this
        resource
    :rtype: list of str


  .. py:method:: load()

    Calls :py:meth:`OpsWorks.Client.describe_layers` to update the attributes of the Layer resource. Note that the load and reload methods are the same method and can be used interchangeably.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/None>`_    


    **Request Syntax** 

    ::

      layer.load()
    :returns: None

  .. py:method:: reload()

    Calls :py:meth:`OpsWorks.Client.describe_layers` to update the attributes of the Layer resource. Note that the load and reload methods are the same method and can be used interchangeably.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/None>`_    


    **Request Syntax** 

    ::

      layer.reload()
    :returns: None

=====
Stack
=====



.. py:class:: OpsWorks.Stack(id)

  A resource representing an AWS OpsWorks Stack::

    
    import boto3
    
    opsworks = boto3.resource('opsworks')
    stack = opsworks.Stack('id')

  :type id: string
  :param id: The Stack's id identifier. This **must** be set.
  
  These are the resource's available identifiers:
  
  *   :py:attr:`id`

  
  These are the resource's available attributes:
  
  *   :py:attr:`agent_version`

  
  *   :py:attr:`arn`

  
  *   :py:attr:`attributes`

  
  *   :py:attr:`chef_configuration`

  
  *   :py:attr:`configuration_manager`

  
  *   :py:attr:`created_at`

  
  *   :py:attr:`custom_cookbooks_source`

  
  *   :py:attr:`custom_json`

  
  *   :py:attr:`default_availability_zone`

  
  *   :py:attr:`default_instance_profile_arn`

  
  *   :py:attr:`default_os`

  
  *   :py:attr:`default_root_device_type`

  
  *   :py:attr:`default_ssh_key_name`

  
  *   :py:attr:`default_subnet_id`

  
  *   :py:attr:`hostname_theme`

  
  *   :py:attr:`name`

  
  *   :py:attr:`region`

  
  *   :py:attr:`service_role_arn`

  
  *   :py:attr:`stack_id`

  
  *   :py:attr:`use_custom_cookbooks`

  
  *   :py:attr:`use_opsworks_security_groups`

  
  *   :py:attr:`vpc_id`

  
  These are the resource's available actions:
  
  *   :py:meth:`create_layer()`

  
  *   :py:meth:`delete()`

  
  *   :py:meth:`get_available_subresources()`

  
  *   :py:meth:`load()`

  
  *   :py:meth:`reload()`

  
  These are the resource's available sub-resources:
  
  *   :py:meth:`Summary()`

  
  These are the resource's available collections:
  
  *   :py:attr:`layers`

  
  .. rst-class:: admonition-title
  
  Identifiers
  
  Identifiers are properties of a resource that are set upon instantation of the resource.
  For more information about identifiers refer to the :ref:`Resources Introduction Guide<identifiers_attributes_intro>`.
  

  .. py:attribute:: id

    *(string)* The Stack's id identifier. This **must** be set.
  .. rst-class:: admonition-title
  
  Attributes
  
  Attributes provide access to the properties of a resource. Attributes are lazy-loaded the first time one is accessed via the :py:meth:`load` method.
  For more information about attributes refer to the :ref:`Resources Introduction Guide<identifiers_attributes_intro>`.
  

  .. py:attribute:: agent_version

    

    - *(string) --* 

      The agent version. This parameter is set to ``LATEST`` for auto-update. or a version number for a fixed agent version.

      

  .. py:attribute:: arn

    

    - *(string) --* 

      The stack's ARN.

      

  .. py:attribute:: attributes

    

    - *(dict) --* 

      The stack's attributes.

      
      

      - *(string) --* 
        

        - *(string) --* 
  


  .. py:attribute:: chef_configuration

    

    - *(dict) --* 

      A ``ChefConfiguration`` object that specifies whether to enable Berkshelf and the Berkshelf version. For more information, see `Create a New Stack <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-creating.html>`__ .

      
      

      - **ManageBerkshelf** *(boolean) --* 

        Whether to enable Berkshelf.

        
      

      - **BerkshelfVersion** *(string) --* 

        The Berkshelf version.

        
  

  .. py:attribute:: configuration_manager

    

    - *(dict) --* 

      The configuration manager.

      
      

      - **Name** *(string) --* 

        The name. This parameter must be set to "Chef".

        
      

      - **Version** *(string) --* 

        The Chef version. This parameter must be set to 12, 11.10, or 11.4 for Linux stacks, and to 12.2 for Windows stacks. The default value for Linux stacks is 11.4.

        
  

  .. py:attribute:: created_at

    

    - *(string) --* 

      The date when the stack was created.

      

  .. py:attribute:: custom_cookbooks_source

    

    - *(dict) --* 

      Contains the information required to retrieve an app or cookbook from a repository. For more information, see `Creating Apps <http://docs.aws.amazon.com/opsworks/latest/userguide/workingapps-creating.html>`__ or `Custom Recipes and Cookbooks <http://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook.html>`__ .

      
      

      - **Type** *(string) --* 

        The repository type.

        
      

      - **Url** *(string) --* 

        The source URL. The following is an example of an Amazon S3 source URL: ``https://s3.amazonaws.com/opsworks-demo-bucket/opsworks_cookbook_demo.tar.gz`` .

        
      

      - **Username** *(string) --* 

        This parameter depends on the repository type.

         

         
        * For Amazon S3 bundles, set ``Username`` to the appropriate IAM access key ID. 
         
        * For HTTP bundles, Git repositories, and Subversion repositories, set ``Username`` to the user name. 
         

        
      

      - **Password** *(string) --* 

        When included in a request, the parameter depends on the repository type.

         

         
        * For Amazon S3 bundles, set ``Password`` to the appropriate IAM secret access key. 
         
        * For HTTP bundles and Subversion repositories, set ``Password`` to the password. 
         

         

        For more information on how to safely handle IAM credentials, see `http\://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html <http://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html>`__ .

         

        In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

        
      

      - **SshKey** *(string) --* 

        In requests, the repository's SSH key.

         

        In responses, AWS OpsWorks Stacks returns ``*****FILTERED*****`` instead of the actual value.

        
      

      - **Revision** *(string) --* 

        The application's version. AWS OpsWorks Stacks enables you to easily deploy new versions of an application. One of the simplest approaches is to have branches or revisions in your repository that represent different versions that can potentially be deployed.

        
  

  .. py:attribute:: custom_json

    

    - *(string) --* 

      A JSON object that contains user-defined attributes to be added to the stack configuration and deployment attributes. You can use custom JSON to override the corresponding default stack configuration attribute values or to pass data to recipes. The string should be in the following format:

       

       ``"{\"key1\": \"value1\", \"key2\": \"value2\",...}"``  

       

      For more information on custom JSON, see `Use Custom JSON to Modify the Stack Configuration Attributes <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-json.html>`__ .

      

  .. py:attribute:: default_availability_zone

    

    - *(string) --* 

      The stack's default Availability Zone. For more information, see `Regions and Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html>`__ .

      

  .. py:attribute:: default_instance_profile_arn

    

    - *(string) --* 

      The ARN of an IAM profile that is the default profile for all of the stack's EC2 instances. For more information about IAM ARNs, see `Using Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ .

      

  .. py:attribute:: default_os

    

    - *(string) --* 

      The stack's default operating system.

      

  .. py:attribute:: default_root_device_type

    

    - *(string) --* 

      The default root device type. This value is used by default for all instances in the stack, but you can override it when you create an instance. For more information, see `Storage for the Root Device <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-for-the-root-device>`__ .

      

  .. py:attribute:: default_ssh_key_name

    

    - *(string) --* 

      A default Amazon EC2 key pair for the stack's instances. You can override this value when you create or update an instance.

      

  .. py:attribute:: default_subnet_id

    

    - *(string) --* 

      The default subnet ID; applicable only if the stack is running in a VPC.

      

  .. py:attribute:: hostname_theme

    

    - *(string) --* 

      The stack host name theme, with spaces replaced by underscores.

      

  .. py:attribute:: name

    

    - *(string) --* 

      The stack name.

      

  .. py:attribute:: region

    

    - *(string) --* 

      The stack AWS region, such as "ap-northeast-2". For more information about AWS regions, see `Regions and Endpoints <http://docs.aws.amazon.com/general/latest/gr/rande.html>`__ .

      

  .. py:attribute:: service_role_arn

    

    - *(string) --* 

      The stack AWS Identity and Access Management (IAM) role.

      

  .. py:attribute:: stack_id

    

    - *(string) --* 

      The stack ID.

      

  .. py:attribute:: use_custom_cookbooks

    

    - *(boolean) --* 

      Whether the stack uses custom cookbooks.

      

  .. py:attribute:: use_opsworks_security_groups

    

    - *(boolean) --* 

      Whether the stack automatically associates the AWS OpsWorks Stacks built-in security groups with the stack's layers.

      

  .. py:attribute:: vpc_id

    

    - *(string) --* 

      The VPC ID; applicable only if the stack is running in a VPC.

      
  .. rst-class:: admonition-title
  
  Actions
  
  Actions call operations on resources.  They may automatically handle the passing in of arguments set from identifiers and some attributes.
  For more information about actions refer to the :ref:`Resources Introduction Guide<actions_intro>`.
  

  .. py:method:: create_layer(**kwargs)

    

    Creates a layer. For more information, see `How to Create a Layer <http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-create.html>`__ .

     

    .. note::

       

      You should use **CreateLayer** for noncustom layer types such as PHP App Server only if the stack does not have an existing layer of that type. A stack can have at most one instance of each noncustom layer; if you attempt to create a second instance, **CreateLayer** fails. A stack can have an arbitrary number of custom layers, so you can call **CreateLayer** as many times as you like for that layer type.

       

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/CreateLayer>`_    


    **Request Syntax** 
    ::

      layer = stack.create_layer(
          Type='aws-flow-ruby'|'ecs-cluster'|'java-app'|'lb'|'web'|'php-app'|'rails-app'|'nodejs-app'|'memcached'|'db-master'|'monitoring-master'|'custom',
          Name='string',
          Shortname='string',
          Attributes={
              'string': 'string'
          },
          CloudWatchLogsConfiguration={
              'Enabled': True|False,
              'LogStreams': [
                  {
                      'LogGroupName': 'string',
                      'DatetimeFormat': 'string',
                      'TimeZone': 'LOCAL'|'UTC',
                      'File': 'string',
                      'FileFingerprintLines': 'string',
                      'MultiLineStartPattern': 'string',
                      'InitialPosition': 'start_of_file'|'end_of_file',
                      'Encoding': 'ascii'|'big5'|'big5hkscs'|'cp037'|'cp424'|'cp437'|'cp500'|'cp720'|'cp737'|'cp775'|'cp850'|'cp852'|'cp855'|'cp856'|'cp857'|'cp858'|'cp860'|'cp861'|'cp862'|'cp863'|'cp864'|'cp865'|'cp866'|'cp869'|'cp874'|'cp875'|'cp932'|'cp949'|'cp950'|'cp1006'|'cp1026'|'cp1140'|'cp1250'|'cp1251'|'cp1252'|'cp1253'|'cp1254'|'cp1255'|'cp1256'|'cp1257'|'cp1258'|'euc_jp'|'euc_jis_2004'|'euc_jisx0213'|'euc_kr'|'gb2312'|'gbk'|'gb18030'|'hz'|'iso2022_jp'|'iso2022_jp_1'|'iso2022_jp_2'|'iso2022_jp_2004'|'iso2022_jp_3'|'iso2022_jp_ext'|'iso2022_kr'|'latin_1'|'iso8859_2'|'iso8859_3'|'iso8859_4'|'iso8859_5'|'iso8859_6'|'iso8859_7'|'iso8859_8'|'iso8859_9'|'iso8859_10'|'iso8859_13'|'iso8859_14'|'iso8859_15'|'iso8859_16'|'johab'|'koi8_r'|'koi8_u'|'mac_cyrillic'|'mac_greek'|'mac_iceland'|'mac_latin2'|'mac_roman'|'mac_turkish'|'ptcp154'|'shift_jis'|'shift_jis_2004'|'shift_jisx0213'|'utf_32'|'utf_32_be'|'utf_32_le'|'utf_16'|'utf_16_be'|'utf_16_le'|'utf_7'|'utf_8'|'utf_8_sig',
                      'BufferDuration': 123,
                      'BatchCount': 123,
                      'BatchSize': 123
                  },
              ]
          },
          CustomInstanceProfileArn='string',
          CustomJson='string',
          CustomSecurityGroupIds=[
              'string',
          ],
          Packages=[
              'string',
          ],
          VolumeConfigurations=[
              {
                  'MountPoint': 'string',
                  'RaidLevel': 123,
                  'NumberOfDisks': 123,
                  'Size': 123,
                  'VolumeType': 'string',
                  'Iops': 123
              },
          ],
          EnableAutoHealing=True|False,
          AutoAssignElasticIps=True|False,
          AutoAssignPublicIps=True|False,
          CustomRecipes={
              'Setup': [
                  'string',
              ],
              'Configure': [
                  'string',
              ],
              'Deploy': [
                  'string',
              ],
              'Undeploy': [
                  'string',
              ],
              'Shutdown': [
                  'string',
              ]
          },
          InstallUpdatesOnBoot=True|False,
          UseEbsOptimizedInstances=True|False,
          LifecycleEventConfiguration={
              'Shutdown': {
                  'ExecutionTimeout': 123,
                  'DelayUntilElbConnectionsDrained': True|False
              }
          }
      )
    :type Type: string
    :param Type: **[REQUIRED]** 

      The layer type. A stack cannot have more than one built-in layer of the same type. It can have any number of custom layers. Built-in layers are not available in Chef 12 stacks.

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      The layer name, which is used by the console.

      

    
    :type Shortname: string
    :param Shortname: **[REQUIRED]** 

      For custom layers only, use this parameter to specify the layer's short name, which is used internally by AWS OpsWorks Stacks and by Chef recipes. The short name is also used as the name for the directory where your app files are installed. It can have a maximum of 200 characters, which are limited to the alphanumeric characters, '-', '_', and '.'.

       

      The built-in layers' short names are defined by AWS OpsWorks Stacks. For more information, see the `Layer Reference <http://docs.aws.amazon.com/opsworks/latest/userguide/layers.html>`__ .

      

    
    :type Attributes: dict
    :param Attributes: 

      One or more user-defined key-value pairs to be added to the stack attributes.

       

      To create a cluster layer, set the ``EcsClusterArn`` attribute to the cluster's ARN.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type CloudWatchLogsConfiguration: dict
    :param CloudWatchLogsConfiguration: 

      Specifies CloudWatch Logs configuration options for the layer. For more information, see  CloudWatchLogsLogStream .

      

    
      - **Enabled** *(boolean) --* 

        Whether CloudWatch Logs is enabled for a layer.

        

      
      - **LogStreams** *(list) --* 

        A list of configuration options for CloudWatch Logs.

        

      
        - *(dict) --* 

          Describes the Amazon CloudWatch logs configuration for a layer. For detailed information about members of this data type, see the `CloudWatch Logs Agent Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html>`__ .

          

        
          - **LogGroupName** *(string) --* 

            Specifies the destination log group. A log group is created automatically if it doesn't already exist. Log group names can be between 1 and 512 characters long. Allowed characters include a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), '/' (forward slash), and '.' (period).

            

          
          - **DatetimeFormat** *(string) --* 

            Specifies how the time stamp is extracted from logs. For more information, see the `CloudWatch Logs Agent Reference <http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html>`__ .

            

          
          - **TimeZone** *(string) --* 

            Specifies the time zone of log event time stamps.

            

          
          - **File** *(string) --* 

            Specifies log files that you want to push to CloudWatch Logs.

             

             ``File`` can point to a specific file or multiple files (by using wild card characters such as ``/var/log/system.log*`` ). Only the latest file is pushed to CloudWatch Logs, based on file modification time. We recommend that you use wild card characters to specify a series of files of the same type, such as ``access_log.2014-06-01-01`` , ``access_log.2014-06-01-02`` , and so on by using a pattern like ``access_log.*`` . Don't use a wildcard to match multiple file types, such as ``access_log_80`` and ``access_log_443`` . To specify multiple, different file types, add another log stream entry to the configuration file, so that each log file type is stored in a different log group.

             

            Zipped files are not supported.

            

          
          - **FileFingerprintLines** *(string) --* 

            Specifies the range of lines for identifying a file. The valid values are one number, or two dash-delimited numbers, such as '1', '2-5'. The default value is '1', meaning the first line is used to calculate the fingerprint. Fingerprint lines are not sent to CloudWatch Logs unless all specified lines are available.

            

          
          - **MultiLineStartPattern** *(string) --* 

            Specifies the pattern for identifying the start of a log message.

            

          
          - **InitialPosition** *(string) --* 

            Specifies where to start to read data (start_of_file or end_of_file). The default is start_of_file. This setting is only used if there is no state persisted for that log stream.

            

          
          - **Encoding** *(string) --* 

            Specifies the encoding of the log file so that the file can be read correctly. The default is ``utf_8`` . Encodings supported by Python ``codecs.decode()`` can be used here.

            

          
          - **BufferDuration** *(integer) --* 

            Specifies the time duration for the batching of log events. The minimum value is 5000ms and default value is 5000ms.

            

          
          - **BatchCount** *(integer) --* 

            Specifies the max number of log events in a batch, up to 10000. The default value is 1000.

            

          
          - **BatchSize** *(integer) --* 

            Specifies the maximum size of log events in a batch, in bytes, up to 1048576 bytes. The default value is 32768 bytes. This size is calculated as the sum of all event messages in UTF-8, plus 26 bytes for each log event.

            

          
        
    
    
    :type CustomInstanceProfileArn: string
    :param CustomInstanceProfileArn: 

      The ARN of an IAM profile to be used for the layer's EC2 instances. For more information about IAM ARNs, see `Using Identifiers <http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ .

      

    
    :type CustomJson: string
    :param CustomJson: 

      A JSON-formatted string containing custom stack configuration and deployment attributes to be installed on the layer's instances. For more information, see `Using Custom JSON <http://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook-json-override.html>`__ . This feature is supported as of version 1.7.42 of the AWS CLI. 

      

    
    :type CustomSecurityGroupIds: list
    :param CustomSecurityGroupIds: 

      An array containing the layer custom security group IDs.

      

    
      - *(string) --* 

      
  
    :type Packages: list
    :param Packages: 

      An array of ``Package`` objects that describes the layer packages.

      

    
      - *(string) --* 

      
  
    :type VolumeConfigurations: list
    :param VolumeConfigurations: 

      A ``VolumeConfigurations`` object that describes the layer's Amazon EBS volumes.

      

    
      - *(dict) --* 

        Describes an Amazon EBS volume configuration.

        

      
        - **MountPoint** *(string) --* **[REQUIRED]** 

          The volume mount point. For example "/dev/sdh".

          

        
        - **RaidLevel** *(integer) --* 

          The volume `RAID level <http://en.wikipedia.org/wiki/Standard_RAID_levels>`__ .

          

        
        - **NumberOfDisks** *(integer) --* **[REQUIRED]** 

          The number of disks in the volume.

          

        
        - **Size** *(integer) --* **[REQUIRED]** 

          The volume size.

          

        
        - **VolumeType** *(string) --* 

          The volume type:

           

           
          * ``standard`` - Magnetic 
           
          * ``io1`` - Provisioned IOPS (SSD) 
           
          * ``gp2`` - General Purpose (SSD) 
           

          

        
        - **Iops** *(integer) --* 

          For PIOPS volumes, the IOPS per disk.

          

        
      
  
    :type EnableAutoHealing: boolean
    :param EnableAutoHealing: 

      Whether to disable auto healing for the layer.

      

    
    :type AutoAssignElasticIps: boolean
    :param AutoAssignElasticIps: 

      Whether to automatically assign an `Elastic IP address <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html>`__ to the layer's instances. For more information, see `How to Edit a Layer <http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-edit.html>`__ .

      

    
    :type AutoAssignPublicIps: boolean
    :param AutoAssignPublicIps: 

      For stacks that are running in a VPC, whether to automatically assign a public IP address to the layer's instances. For more information, see `How to Edit a Layer <http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-basics-edit.html>`__ .

      

    
    :type CustomRecipes: dict
    :param CustomRecipes: 

      A ``LayerCustomRecipes`` object that specifies the layer custom recipes.

      

    
      - **Setup** *(list) --* 

        An array of custom recipe names to be run following a ``setup`` event.

        

      
        - *(string) --* 

        
    
      - **Configure** *(list) --* 

        An array of custom recipe names to be run following a ``configure`` event.

        

      
        - *(string) --* 

        
    
      - **Deploy** *(list) --* 

        An array of custom recipe names to be run following a ``deploy`` event.

        

      
        - *(string) --* 

        
    
      - **Undeploy** *(list) --* 

        An array of custom recipe names to be run following a ``undeploy`` event.

        

      
        - *(string) --* 

        
    
      - **Shutdown** *(list) --* 

        An array of custom recipe names to be run following a ``shutdown`` event.

        

      
        - *(string) --* 

        
    
    
    :type InstallUpdatesOnBoot: boolean
    :param InstallUpdatesOnBoot: 

      Whether to install operating system and package updates when the instance boots. The default value is ``true`` . To control when updates are installed, set this value to ``false`` . You must then update your instances manually by using  CreateDeployment to run the ``update_dependencies`` stack command or by manually running ``yum`` (Amazon Linux) or ``apt-get`` (Ubuntu) on the instances. 

       

      .. note::

         

        To ensure that your instances have the latest security updates, we strongly recommend using the default value of ``true`` .

         

      

    
    :type UseEbsOptimizedInstances: boolean
    :param UseEbsOptimizedInstances: 

      Whether to use Amazon EBS-optimized instances.

      

    
    :type LifecycleEventConfiguration: dict
    :param LifecycleEventConfiguration: 

      A ``LifeCycleEventConfiguration`` object that you can use to configure the Shutdown event to specify an execution timeout and enable or disable Elastic Load Balancer connection draining.

      

    
      - **Shutdown** *(dict) --* 

        A ``ShutdownEventConfiguration`` object that specifies the Shutdown event configuration.

        

      
        - **ExecutionTimeout** *(integer) --* 

          The time, in seconds, that AWS OpsWorks Stacks will wait after triggering a Shutdown event before shutting down an instance.

          

        
        - **DelayUntilElbConnectionsDrained** *(boolean) --* 

          Whether to enable Elastic Load Balancing connection draining. For more information, see `Connection Draining <http://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/TerminologyandKeyConcepts.html#conn-drain>`__  

          

        
      
    
    
    :rtype: :py:class:`opsworks.Layer`
    :returns: Layer resource
    

  .. py:method:: delete()

    

    Deletes a specified stack. You must first delete all instances, layers, and apps or deregister registered instances. For more information, see `Shut Down a Stack <http://docs.aws.amazon.com/opsworks/latest/userguide/workingstacks-shutting.html>`__ .

     

     **Required Permissions** : To use this action, an IAM user must have a Manage permissions level for the stack, or an attached policy that explicitly grants permissions. For more information on user permissions, see `Managing User Permissions <http://docs.aws.amazon.com/opsworks/latest/userguide/opsworks-security-users.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DeleteStack>`_    


    **Request Syntax** 
    ::

      response = stack.delete()
      
    
    :returns: None

  .. py:method:: get_available_subresources()

        
    Returns a list of all the available sub-resources for this
    Resource.
    
    :returns: A list containing the name of each sub-resource for this
        resource
    :rtype: list of str


  .. py:method:: load()

    Calls :py:meth:`OpsWorks.Client.describe_stacks` to update the attributes of the Stack resource. Note that the load and reload methods are the same method and can be used interchangeably.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/None>`_    


    **Request Syntax** 

    ::

      stack.load()
    :returns: None

  .. py:method:: reload()

    Calls :py:meth:`OpsWorks.Client.describe_stacks` to update the attributes of the Stack resource. Note that the load and reload methods are the same method and can be used interchangeably.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/None>`_    


    **Request Syntax** 

    ::

      stack.reload()
    :returns: None
  .. rst-class:: admonition-title
  
  Sub-resources
  
  Sub-resources are methods that create a new instance of a child resource. This resource's identifiers get passed along to the child.
  For more information about sub-resources refer to the :ref:`Resources Introduction Guide<subresources_intro>`.
  

  .. py:method:: Summary()

    Creates a StackSummary resource.::

      stack_summary = stack.Summary()

    
    :rtype: :py:class:`OpsWorks.StackSummary`
    :returns: A StackSummary resource
    
  .. rst-class:: admonition-title
  
  Collections
  
  Collections provide an interface to iterate over and manipulate groups of resources. 
  For more information about collections refer to the :ref:`Resources Introduction Guide<guide_collections>`.
  

  .. py:attribute:: layers

    A collection of Layer resources

    .. py:method:: all()

      Creates an iterable of all Layer resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeLayers>`_      


      **Request Syntax** 
      ::

        layer_iterator = stack.layers.all()
        
      
      :rtype: list(:py:class:`opsworks.Layer`)
      :returns: A list of Layer resources
      

    .. py:method:: filter(**kwargs)

      Creates an iterable of all Layer resources in the collection filtered by kwargs passed to method.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeLayers>`_      


      **Request Syntax** 
      ::

        layer_iterator = stack.layers.filter(
            LayerIds=[
                'string',
            ]
        )
      :type LayerIds: list
      :param LayerIds: 

        An array of layer IDs that specify the layers to be described. If you omit this parameter, ``DescribeLayers`` returns a description of every layer in the specified stack.

        

      
        - *(string) --* 

        
    
      
      :rtype: list(:py:class:`opsworks.Layer`)
      :returns: A list of Layer resources
      

    .. py:method:: limit(**kwargs)

      Creates an iterable up to a specified amount of Layer resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeLayers>`_      


      **Request Syntax** 
      ::

        layer_iterator = stack.layers.limit(
            count=123
        )
      :type count: integer
      :param count: The limit to the number of resources in the iterable.

      
      
      :rtype: list(:py:class:`opsworks.Layer`)
      :returns: A list of Layer resources
      

    .. py:method:: page_size(**kwargs)

      Creates an iterable of all Layer resources in the collection, but limits the number of items returned by each service call by the specified amount.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeLayers>`_      


      **Request Syntax** 
      ::

        layer_iterator = stack.layers.page_size(
            count=123
        )
      :type count: integer
      :param count: The number of items returned by each service call

      
      
      :rtype: list(:py:class:`opsworks.Layer`)
      :returns: A list of Layer resources
      

============
StackSummary
============



.. py:class:: OpsWorks.StackSummary(stack_id)

  A resource representing an AWS OpsWorks StackSummary::

    
    import boto3
    
    opsworks = boto3.resource('opsworks')
    stack_summary = opsworks.StackSummary('stack_id')

  :type stack_id: string
  :param stack_id: The StackSummary's stack_id identifier. This **must** be set.
  
  These are the resource's available identifiers:
  
  *   :py:attr:`stack_id`

  
  These are the resource's available attributes:
  
  *   :py:attr:`apps_count`

  
  *   :py:attr:`arn`

  
  *   :py:attr:`instances_count`

  
  *   :py:attr:`layers_count`

  
  *   :py:attr:`name`

  
  These are the resource's available sub-resources:
  
  *   :py:meth:`Stack()`

  
  .. rst-class:: admonition-title
  
  Identifiers
  
  Identifiers are properties of a resource that are set upon instantation of the resource.
  For more information about identifiers refer to the :ref:`Resources Introduction Guide<identifiers_attributes_intro>`.
  

  .. py:attribute:: stack_id

    *(string)* The StackSummary's stack_id identifier. This **must** be set.
  .. rst-class:: admonition-title
  
  Attributes
  
  Attributes provide access to the properties of a resource. Attributes are lazy-loaded the first time one is accessed via the :py:meth:`load` method.
  For more information about attributes refer to the :ref:`Resources Introduction Guide<identifiers_attributes_intro>`.
  

  .. py:attribute:: apps_count

    

    - *(integer) --* 

      The number of apps.

      

  .. py:attribute:: arn

    

    - *(string) --* 

      The stack's ARN.

      

  .. py:attribute:: instances_count

    

    - *(dict) --* 

      An ``InstancesCount`` object with the number of instances in each status.

      
      

      - **Assigning** *(integer) --* 

        The number of instances in the Assigning state.

        
      

      - **Booting** *(integer) --* 

        The number of instances with ``booting`` status.

        
      

      - **ConnectionLost** *(integer) --* 

        The number of instances with ``connection_lost`` status.

        
      

      - **Deregistering** *(integer) --* 

        The number of instances in the Deregistering state.

        
      

      - **Online** *(integer) --* 

        The number of instances with ``online`` status.

        
      

      - **Pending** *(integer) --* 

        The number of instances with ``pending`` status.

        
      

      - **Rebooting** *(integer) --* 

        The number of instances with ``rebooting`` status.

        
      

      - **Registered** *(integer) --* 

        The number of instances in the Registered state.

        
      

      - **Registering** *(integer) --* 

        The number of instances in the Registering state.

        
      

      - **Requested** *(integer) --* 

        The number of instances with ``requested`` status.

        
      

      - **RunningSetup** *(integer) --* 

        The number of instances with ``running_setup`` status.

        
      

      - **SetupFailed** *(integer) --* 

        The number of instances with ``setup_failed`` status.

        
      

      - **ShuttingDown** *(integer) --* 

        The number of instances with ``shutting_down`` status.

        
      

      - **StartFailed** *(integer) --* 

        The number of instances with ``start_failed`` status.

        
      

      - **Stopped** *(integer) --* 

        The number of instances with ``stopped`` status.

        
      

      - **Stopping** *(integer) --* 

        The number of instances with ``stopping`` status.

        
      

      - **Terminated** *(integer) --* 

        The number of instances with ``terminated`` status.

        
      

      - **Terminating** *(integer) --* 

        The number of instances with ``terminating`` status.

        
      

      - **Unassigning** *(integer) --* 

        The number of instances in the Unassigning state.

        
  

  .. py:attribute:: layers_count

    

    - *(integer) --* 

      The number of layers.

      

  .. py:attribute:: name

    

    - *(string) --* 

      The stack name.

      
  .. rst-class:: admonition-title
  
  Sub-resources
  
  Sub-resources are methods that create a new instance of a child resource. This resource's identifiers get passed along to the child.
  For more information about sub-resources refer to the :ref:`Resources Introduction Guide<subresources_intro>`.
  

  .. py:method:: Stack()

    Creates a Stack resource.::

      stack = stack_summary.Stack()

    
    :rtype: :py:class:`OpsWorks.Stack`
    :returns: A Stack resource
    