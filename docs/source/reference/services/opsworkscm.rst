

**********
OpsWorksCM
**********

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: OpsWorksCM.Client

  A low-level client representing AWS OpsWorks for Chef Automate (OpsWorksCM)::

    
    import boto3
    
    client = boto3.client('opsworkscm')

  
  These are the available methods:
  
  *   :py:meth:`~OpsWorksCM.Client.associate_node`

  
  *   :py:meth:`~OpsWorksCM.Client.can_paginate`

  
  *   :py:meth:`~OpsWorksCM.Client.create_backup`

  
  *   :py:meth:`~OpsWorksCM.Client.create_server`

  
  *   :py:meth:`~OpsWorksCM.Client.delete_backup`

  
  *   :py:meth:`~OpsWorksCM.Client.delete_server`

  
  *   :py:meth:`~OpsWorksCM.Client.describe_account_attributes`

  
  *   :py:meth:`~OpsWorksCM.Client.describe_backups`

  
  *   :py:meth:`~OpsWorksCM.Client.describe_events`

  
  *   :py:meth:`~OpsWorksCM.Client.describe_node_association_status`

  
  *   :py:meth:`~OpsWorksCM.Client.describe_servers`

  
  *   :py:meth:`~OpsWorksCM.Client.disassociate_node`

  
  *   :py:meth:`~OpsWorksCM.Client.generate_presigned_url`

  
  *   :py:meth:`~OpsWorksCM.Client.get_paginator`

  
  *   :py:meth:`~OpsWorksCM.Client.get_waiter`

  
  *   :py:meth:`~OpsWorksCM.Client.restore_server`

  
  *   :py:meth:`~OpsWorksCM.Client.start_maintenance`

  
  *   :py:meth:`~OpsWorksCM.Client.update_server`

  
  *   :py:meth:`~OpsWorksCM.Client.update_server_engine_attributes`

  

  .. py:method:: associate_node(**kwargs)

    

    Associates a new node with the server. For more information about how to disassociate a node, see  DisassociateNode .

     

    On a Chef server: This command is an alternative to ``knife bootstrap`` .

     

    Example (Chef): ``aws opsworks-cm associate-node --server-name *MyServer* --node-name *MyManagedNode* --engine-attributes "Name=*CHEF_ORGANIZATION* ,Value=default" "Name=*CHEF_NODE_PUBLIC_KEY* ,Value=*public-key-pem* "``  

     

    On a Puppet server, this command is an alternative to the ``puppet cert sign`` command that signs a Puppet node CSR. 

     

    Example (Chef): ``aws opsworks-cm associate-node --server-name *MyServer* --node-name *MyManagedNode* --engine-attributes "Name=*PUPPET_NODE_CSR* ,Value=*csr-pem* "``  

     

    A node can can only be associated with servers that are in a ``HEALTHY`` state. Otherwise, an ``InvalidStateException`` is thrown. A ``ResourceNotFoundException`` is thrown when the server does not exist. A ``ValidationException`` is raised when parameters of the request are not valid. The AssociateNode API call can be integrated into Auto Scaling configurations, AWS Cloudformation templates, or the user data of a server's instance. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworkscm-2016-11-01/AssociateNode>`_    


    **Request Syntax** 
    ::

      response = client.associate_node(
          ServerName='string',
          NodeName='string',
          EngineAttributes=[
              {
                  'Name': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type ServerName: string
    :param ServerName: **[REQUIRED]** 

      The name of the server with which to associate the node. 

      

    
    :type NodeName: string
    :param NodeName: **[REQUIRED]** 

      The name of the node. 

      

    
    :type EngineAttributes: list
    :param EngineAttributes: **[REQUIRED]** 

      Engine attributes used for associating the node. 

       

       **Attributes accepted in a AssociateNode request for Chef**  

       

       
      * ``CHEF_ORGANIZATION`` : The Chef organization with which the node is associated. By default only one organization named ``default`` can exist.  
       
      * ``CHEF_NODE_PUBLIC_KEY`` : A PEM-formatted public key. This key is required for the ``chef-client`` agent to access the Chef API.  
       

       

       **Attributes accepted in a AssociateNode request for Puppet**  

       

       
      * ``PUPPET_NODE_CSR`` : A PEM-formatted certificate-signing request (CSR) that is created by the node.  
       

      

    
      - *(dict) --* 

        A name and value pair that is specific to the engine of the server. 

        

      
        - **Name** *(string) --* 

          The name of the engine attribute. 

          

        
        - **Value** *(string) --* 

          The value of the engine attribute. 

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NodeAssociationStatusToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NodeAssociationStatusToken** *(string) --* 

          Contains a token which can be passed to the ``DescribeNodeAssociationStatus`` API call to get the status of the association request. 

          
    

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


  .. py:method:: create_backup(**kwargs)

    

    Creates an application-level backup of a server. While the server is in the ``BACKING_UP`` state, the server cannot be changed, and no additional backup can be created. 

     

    Backups can be created for servers in ``RUNNING`` , ``HEALTHY`` , and ``UNHEALTHY`` states. By default, you can create a maximum of 50 manual backups. 

     

    This operation is asynchronous. 

     

    A ``LimitExceededException`` is thrown when the maximum number of manual backups is reached. An ``InvalidStateException`` is thrown when the server is not in any of the following states: RUNNING, HEALTHY, or UNHEALTHY. A ``ResourceNotFoundException`` is thrown when the server is not found. A ``ValidationException`` is thrown when parameters of the request are not valid. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworkscm-2016-11-01/CreateBackup>`_    


    **Request Syntax** 
    ::

      response = client.create_backup(
          ServerName='string',
          Description='string'
      )
    :type ServerName: string
    :param ServerName: **[REQUIRED]** 

      The name of the server that you want to back up. 

      

    
    :type Description: string
    :param Description: 

      A user-defined description of the backup. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Backup': {
                'BackupArn': 'string',
                'BackupId': 'string',
                'BackupType': 'AUTOMATED'|'MANUAL',
                'CreatedAt': datetime(2015, 1, 1),
                'Description': 'string',
                'Engine': 'string',
                'EngineModel': 'string',
                'EngineVersion': 'string',
                'InstanceProfileArn': 'string',
                'InstanceType': 'string',
                'KeyPair': 'string',
                'PreferredBackupWindow': 'string',
                'PreferredMaintenanceWindow': 'string',
                'S3DataSize': 123,
                'S3DataUrl': 'string',
                'S3LogUrl': 'string',
                'SecurityGroupIds': [
                    'string',
                ],
                'ServerName': 'string',
                'ServiceRoleArn': 'string',
                'Status': 'IN_PROGRESS'|'OK'|'FAILED'|'DELETING',
                'StatusDescription': 'string',
                'SubnetIds': [
                    'string',
                ],
                'ToolsVersion': 'string',
                'UserArn': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Backup** *(dict) --* 

          Backup created by request.

          
          

          - **BackupArn** *(string) --* 

            The ARN of the backup. 

            
          

          - **BackupId** *(string) --* 

            The generated ID of the backup. Example: ``myServerName-yyyyMMddHHmmssSSS``  

            
          

          - **BackupType** *(string) --* 

            The backup type. Valid values are ``automated`` or ``manual`` . 

            
          

          - **CreatedAt** *(datetime) --* 

            The time stamp when the backup was created in the database. Example: ``2016-07-29T13:38:47.520Z``  

            
          

          - **Description** *(string) --* 

            A user-provided description for a manual backup. This field is empty for automated backups. 

            
          

          - **Engine** *(string) --* 

            The engine type that is obtained from the server when the backup is created. 

            
          

          - **EngineModel** *(string) --* 

            The engine model that is obtained from the server when the backup is created. 

            
          

          - **EngineVersion** *(string) --* 

            The engine version that is obtained from the server when the backup is created. 

            
          

          - **InstanceProfileArn** *(string) --* 

            The EC2 instance profile ARN that is obtained from the server when the backup is created. Because this value is stored, you are not required to provide the InstanceProfileArn again if you restore a backup. 

            
          

          - **InstanceType** *(string) --* 

            The instance type that is obtained from the server when the backup is created. 

            
          

          - **KeyPair** *(string) --* 

            The key pair that is obtained from the server when the backup is created. 

            
          

          - **PreferredBackupWindow** *(string) --* 

            The preferred backup period that is obtained from the server when the backup is created. 

            
          

          - **PreferredMaintenanceWindow** *(string) --* 

            The preferred maintenance period that is obtained from the server when the backup is created. 

            
          

          - **S3DataSize** *(integer) --* 

            This field is deprecated and is no longer used. 

            
          

          - **S3DataUrl** *(string) --* 

            This field is deprecated and is no longer used. 

            
          

          - **S3LogUrl** *(string) --* 

            The Amazon S3 URL of the backup's log file. 

            
          

          - **SecurityGroupIds** *(list) --* 

            The security group IDs that are obtained from the server when the backup is created. 

            
            

            - *(string) --* 
        
          

          - **ServerName** *(string) --* 

            The name of the server from which the backup was made. 

            
          

          - **ServiceRoleArn** *(string) --* 

            The service role ARN that is obtained from the server when the backup is created. 

            
          

          - **Status** *(string) --* 

            The status of a backup while in progress. 

            
          

          - **StatusDescription** *(string) --* 

            An informational message about backup status. 

            
          

          - **SubnetIds** *(list) --* 

            The subnet IDs that are obtained from the server when the backup is created. 

            
            

            - *(string) --* 
        
          

          - **ToolsVersion** *(string) --* 

            The version of AWS OpsWorks CM-specific tools that is obtained from the server when the backup is created. 

            
          

          - **UserArn** *(string) --* 

            The IAM user ARN of the requester for manual backups. This field is empty for automated backups. 

            
      
    

  .. py:method:: create_server(**kwargs)

    

    Creates and immedately starts a new server. The server is ready to use when it is in the ``HEALTHY`` state. By default, you can create a maximum of 10 servers. 

     

    This operation is asynchronous. 

     

    A ``LimitExceededException`` is thrown when you have created the maximum number of servers (10). A ``ResourceAlreadyExistsException`` is thrown when a server with the same name already exists in the account. A ``ResourceNotFoundException`` is thrown when you specify a backup ID that is not valid or is for a backup that does not exist. A ``ValidationException`` is thrown when parameters of the request are not valid. 

     

    If you do not specify a security group by adding the ``SecurityGroupIds`` parameter, AWS OpsWorks creates a new security group. 

     

     *Chef Automate:* The default security group opens the Chef server to the world on TCP port 443. If a KeyName is present, AWS OpsWorks enables SSH access. SSH is also open to the world on TCP port 22. 

     

     *Puppet Enterprise:* The default security group opens TCP ports 22, 443, 4433, 8140, 8142, 8143, and 8170. If a KeyName is present, AWS OpsWorks enables SSH access. SSH is also open to the world on TCP port 22. 

     

    By default, your server is accessible from any IP address. We recommend that you update your security group rules to allow access from known IP addresses and address ranges only. To edit security group rules, open Security Groups in the navigation pane of the EC2 management console. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworkscm-2016-11-01/CreateServer>`_    


    **Request Syntax** 
    ::

      response = client.create_server(
          AssociatePublicIpAddress=True|False,
          DisableAutomatedBackup=True|False,
          Engine='string',
          EngineModel='string',
          EngineVersion='string',
          EngineAttributes=[
              {
                  'Name': 'string',
                  'Value': 'string'
              },
          ],
          BackupRetentionCount=123,
          ServerName='string',
          InstanceProfileArn='string',
          InstanceType='string',
          KeyPair='string',
          PreferredMaintenanceWindow='string',
          PreferredBackupWindow='string',
          SecurityGroupIds=[
              'string',
          ],
          ServiceRoleArn='string',
          SubnetIds=[
              'string',
          ],
          BackupId='string'
      )
    :type AssociatePublicIpAddress: boolean
    :param AssociatePublicIpAddress: 

      Associate a public IP address with a server that you are launching. Valid values are ``true`` or ``false`` . The default value is ``true`` . 

      

    
    :type DisableAutomatedBackup: boolean
    :param DisableAutomatedBackup: 

      Enable or disable scheduled backups. Valid values are ``true`` or ``false`` . The default value is ``true`` . 

      

    
    :type Engine: string
    :param Engine: 

      The configuration management engine to use. Valid values include ``Chef`` and ``Puppet`` . 

      

    
    :type EngineModel: string
    :param EngineModel: 

      The engine model of the server. Valid values in this release include ``Monolithic`` for Puppet and ``Single`` for Chef. 

      

    
    :type EngineVersion: string
    :param EngineVersion: 

      The major release version of the engine that you want to use. For a Chef server, the valid value for EngineVersion is currently ``12`` . For a Puppet server, the valid value is ``2017`` . 

      

    
    :type EngineAttributes: list
    :param EngineAttributes: 

      Optional engine attributes on a specified server. 

       

       **Attributes accepted in a Chef createServer request:**  

       

       
      * ``CHEF_PIVOTAL_KEY`` : A base64-encoded RSA private key that is not stored by AWS OpsWorks for Chef Automate. This private key is required to access the Chef API. When no CHEF_PIVOTAL_KEY is set, one is generated and returned in the response.  
       
      * ``CHEF_DELIVERY_ADMIN_PASSWORD`` : The password for the administrative user in the Chef Automate GUI. The password length is a minimum of eight characters, and a maximum of 32. The password can contain letters, numbers, and special characters (!/@#$%^&+=_). The password must contain at least one lower case letter, one upper case letter, one number, and one special character. When no CHEF_DELIVERY_ADMIN_PASSWORD is set, one is generated and returned in the response. 
       

       

       **Attributes accepted in a Puppet createServer request:**  

       

       
      * ``PUPPET_ADMIN_PASSWORD`` : To work with the Puppet Enterprise console, a password must use ASCII characters. 
       

      

    
      - *(dict) --* 

        A name and value pair that is specific to the engine of the server. 

        

      
        - **Name** *(string) --* 

          The name of the engine attribute. 

          

        
        - **Value** *(string) --* 

          The value of the engine attribute. 

          

        
      
  
    :type BackupRetentionCount: integer
    :param BackupRetentionCount: 

      The number of automated backups that you want to keep. Whenever a new backup is created, AWS OpsWorks CM deletes the oldest backups if this number is exceeded. The default value is ``1`` . 

      

    
    :type ServerName: string
    :param ServerName: **[REQUIRED]** 

      The name of the server. The server name must be unique within your AWS account, within each region. Server names must start with a letter; then letters, numbers, or hyphens (-) are allowed, up to a maximum of 40 characters. 

      

    
    :type InstanceProfileArn: string
    :param InstanceProfileArn: **[REQUIRED]** 

      The ARN of the instance profile that your Amazon EC2 instances use. Although the AWS OpsWorks console typically creates the instance profile for you, if you are using API commands instead, run the service-role-creation.yaml AWS CloudFormation template, located at https://s3.amazonaws.com/opsworks-cm-us-east-1-prod-default-assets/misc/opsworks-cm-roles.yaml. This template creates a CloudFormation stack that includes the instance profile you need. 

      

    
    :type InstanceType: string
    :param InstanceType: **[REQUIRED]** 

      The Amazon EC2 instance type to use. For example, ``m4.large`` . Recommended instance types include ``t2.medium`` and greater, ``m4.*`` , or ``c4.xlarge`` and greater. 

      

    
    :type KeyPair: string
    :param KeyPair: 

      The Amazon EC2 key pair to set for the instance. This parameter is optional; if desired, you may specify this parameter to connect to your instances by using SSH. 

      

    
    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: 

      The start time for a one-hour period each week during which AWS OpsWorks CM performs maintenance on the instance. Valid values must be specified in the following format: ``DDD:HH:MM`` . The specified time is in coordinated universal time (UTC). The default value is a random one-hour period on Tuesday, Wednesday, or Friday. See ``TimeWindowDefinition`` for more information. 

       

       **Example:**  ``Mon:08:00`` , which represents a start time of every Monday at 08:00 UTC. (8:00 a.m.) 

      

    
    :type PreferredBackupWindow: string
    :param PreferredBackupWindow: 

      The start time for a one-hour period during which AWS OpsWorks CM backs up application-level data on your server if automated backups are enabled. Valid values must be specified in one of the following formats: 

       

       
      * ``HH:MM`` for daily backups 
       
      * ``DDD:HH:MM`` for weekly backups 
       

       

      The specified time is in coordinated universal time (UTC). The default value is a random, daily start time.

       

       **Example:**  ``08:00`` , which represents a daily start time of 08:00 UTC.

       

       **Example:**  ``Mon:08:00`` , which represents a start time of every Monday at 08:00 UTC. (8:00 a.m.)

      

    
    :type SecurityGroupIds: list
    :param SecurityGroupIds: 

      A list of security group IDs to attach to the Amazon EC2 instance. If you add this parameter, the specified security groups must be within the VPC that is specified by ``SubnetIds`` . 

       

      If you do not specify this parameter, AWS OpsWorks CM creates one new security group that uses TCP ports 22 and 443, open to 0.0.0.0/0 (everyone). 

      

    
      - *(string) --* 

      
  
    :type ServiceRoleArn: string
    :param ServiceRoleArn: **[REQUIRED]** 

      The service role that the AWS OpsWorks CM service backend uses to work with your account. Although the AWS OpsWorks management console typically creates the service role for you, if you are using the AWS CLI or API commands, run the service-role-creation.yaml AWS CloudFormation template, located at https://s3.amazonaws.com/opsworks-cm-us-east-1-prod-default-assets/misc/opsworks-cm-roles.yaml. This template creates a CloudFormation stack that includes the service role and instance profile that you need. 

      

    
    :type SubnetIds: list
    :param SubnetIds: 

      The IDs of subnets in which to launch the server EC2 instance. 

       

      Amazon EC2-Classic customers: This field is required. All servers must run within a VPC. The VPC must have "Auto Assign Public IP" enabled. 

       

      EC2-VPC customers: This field is optional. If you do not specify subnet IDs, your EC2 instances are created in a default subnet that is selected by Amazon EC2. If you specify subnet IDs, the VPC must have "Auto Assign Public IP" enabled. 

       

      For more information about supported Amazon EC2 platforms, see `Supported Platforms <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-platforms.html>`__ .

      

    
      - *(string) --* 

      
  
    :type BackupId: string
    :param BackupId: 

      If you specify this field, AWS OpsWorks CM creates the server by using the backup represented by BackupId. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Server': {
                'AssociatePublicIpAddress': True|False,
                'BackupRetentionCount': 123,
                'ServerName': 'string',
                'CreatedAt': datetime(2015, 1, 1),
                'CloudFormationStackArn': 'string',
                'DisableAutomatedBackup': True|False,
                'Endpoint': 'string',
                'Engine': 'string',
                'EngineModel': 'string',
                'EngineAttributes': [
                    {
                        'Name': 'string',
                        'Value': 'string'
                    },
                ],
                'EngineVersion': 'string',
                'InstanceProfileArn': 'string',
                'InstanceType': 'string',
                'KeyPair': 'string',
                'MaintenanceStatus': 'SUCCESS'|'FAILED',
                'PreferredMaintenanceWindow': 'string',
                'PreferredBackupWindow': 'string',
                'SecurityGroupIds': [
                    'string',
                ],
                'ServiceRoleArn': 'string',
                'Status': 'BACKING_UP'|'CONNECTION_LOST'|'CREATING'|'DELETING'|'MODIFYING'|'FAILED'|'HEALTHY'|'RUNNING'|'RESTORING'|'SETUP'|'UNDER_MAINTENANCE'|'UNHEALTHY'|'TERMINATED',
                'StatusReason': 'string',
                'SubnetIds': [
                    'string',
                ],
                'ServerArn': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Server** *(dict) --* 

          The server that is created by the request. 

          
          

          - **AssociatePublicIpAddress** *(boolean) --* 

            Associate a public IP address with a server that you are launching. 

            
          

          - **BackupRetentionCount** *(integer) --* 

            The number of automated backups to keep. 

            
          

          - **ServerName** *(string) --* 

            The name of the server. 

            
          

          - **CreatedAt** *(datetime) --* 

            Time stamp of server creation. Example ``2016-07-29T13:38:47.520Z``  

            
          

          - **CloudFormationStackArn** *(string) --* 

            The ARN of the CloudFormation stack that was used to create the server. 

            
          

          - **DisableAutomatedBackup** *(boolean) --* 

            Disables automated backups. The number of stored backups is dependent on the value of PreferredBackupCount. 

            
          

          - **Endpoint** *(string) --* 

            A DNS name that can be used to access the engine. Example: ``myserver-asdfghjkl.us-east-1.opsworks.io``  

            
          

          - **Engine** *(string) --* 

            The engine type of the server. Valid values in this release include ``Chef`` and ``Puppet`` . 

            
          

          - **EngineModel** *(string) --* 

            The engine model of the server. Valid values in this release include ``Monolithic`` for Puppet and ``Single`` for Chef. 

            
          

          - **EngineAttributes** *(list) --* 

            The response of a createServer() request returns the master credential to access the server in EngineAttributes. These credentials are not stored by AWS OpsWorks CM; they are returned only as part of the result of createServer(). 

             

             **Attributes returned in a createServer response for Chef**  

             

             
            * ``CHEF_PIVOTAL_KEY`` : A base64-encoded RSA private key that is generated by AWS OpsWorks for Chef Automate. This private key is required to access the Chef API. 
             
            * ``CHEF_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Chef starter kit, which includes a README, a configuration file, and the required RSA private key. Save this file, unzip it, and then change to the directory where you've unzipped the file contents. From this directory, you can run Knife commands. 
             

             

             **Attributes returned in a createServer response for Puppet**  

             

             
            * ``PUPPET_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Puppet starter kit, including a README and a required private key. Save this file, unzip it, and then change to the directory where you've unzipped the file contents. 
             
            * ``PUPPET_ADMIN_PASSWORD`` : An administrator password that you can use to sign in to the Puppet Enterprise console after the server is online. 
             

            
            

            - *(dict) --* 

              A name and value pair that is specific to the engine of the server. 

              
              

              - **Name** *(string) --* 

                The name of the engine attribute. 

                
              

              - **Value** *(string) --* 

                The value of the engine attribute. 

                
          
        
          

          - **EngineVersion** *(string) --* 

            The engine version of the server. For a Chef server, the valid value for EngineVersion is currently ``12`` . For a Puppet server, the valid value is ``2017`` . 

            
          

          - **InstanceProfileArn** *(string) --* 

            The instance profile ARN of the server. 

            
          

          - **InstanceType** *(string) --* 

            The instance type for the server, as specified in the CloudFormation stack. This might not be the same instance type that is shown in the EC2 console. 

            
          

          - **KeyPair** *(string) --* 

            The key pair associated with the server. 

            
          

          - **MaintenanceStatus** *(string) --* 

            The status of the most recent server maintenance run. Shows ``SUCCESS`` or ``FAILED`` . 

            
          

          - **PreferredMaintenanceWindow** *(string) --* 

            The preferred maintenance period specified for the server. 

            
          

          - **PreferredBackupWindow** *(string) --* 

            The preferred backup period specified for the server. 

            
          

          - **SecurityGroupIds** *(list) --* 

            The security group IDs for the server, as specified in the CloudFormation stack. These might not be the same security groups that are shown in the EC2 console. 

            
            

            - *(string) --* 
        
          

          - **ServiceRoleArn** *(string) --* 

            The service role ARN used to create the server. 

            
          

          - **Status** *(string) --* 

            The server's status. This field displays the states of actions in progress, such as creating, running, or backing up the server, as well as the server's health state. 

            
          

          - **StatusReason** *(string) --* 

            Depending on the server status, this field has either a human-readable message (such as a create or backup error), or an escaped block of JSON (used for health check results). 

            
          

          - **SubnetIds** *(list) --* 

            The subnet IDs specified in a CreateServer request. 

            
            

            - *(string) --* 
        
          

          - **ServerArn** *(string) --* 

            The ARN of the server. 

            
      
    

  .. py:method:: delete_backup(**kwargs)

    

    Deletes a backup. You can delete both manual and automated backups. This operation is asynchronous. 

     

    An ``InvalidStateException`` is thrown when a backup deletion is already in progress. A ``ResourceNotFoundException`` is thrown when the backup does not exist. A ``ValidationException`` is thrown when parameters of the request are not valid. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworkscm-2016-11-01/DeleteBackup>`_    


    **Request Syntax** 
    ::

      response = client.delete_backup(
          BackupId='string'
      )
    :type BackupId: string
    :param BackupId: **[REQUIRED]** 

      The ID of the backup to delete. Run the DescribeBackups command to get a list of backup IDs. Backup IDs are in the format ``ServerName-yyyyMMddHHmmssSSS`` . 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_server(**kwargs)

    

    Deletes the server and the underlying AWS CloudFormation stacks (including the server's EC2 instance). When you run this command, the server state is updated to ``DELETING`` . After the server is deleted, it is no longer returned by ``DescribeServer`` requests. If the AWS CloudFormation stack cannot be deleted, the server cannot be deleted. 

     

    This operation is asynchronous. 

     

    An ``InvalidStateException`` is thrown when a server deletion is already in progress. A ``ResourceNotFoundException`` is thrown when the server does not exist. A ``ValidationException`` is raised when parameters of the request are not valid. 

     

     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworkscm-2016-11-01/DeleteServer>`_    


    **Request Syntax** 
    ::

      response = client.delete_server(
          ServerName='string'
      )
    :type ServerName: string
    :param ServerName: **[REQUIRED]** 

      The ID of the server to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: describe_account_attributes()

    

    Describes your account attributes, and creates requests to increase limits before they are reached or exceeded. 

     

    This operation is synchronous. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworkscm-2016-11-01/DescribeAccountAttributes>`_    


    **Request Syntax** 
    ::

      response = client.describe_account_attributes()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Attributes': [
                {
                    'Name': 'string',
                    'Maximum': 123,
                    'Used': 123
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Attributes** *(list) --* 

          The attributes that are currently set for the account. 

          
          

          - *(dict) --* 

            Stores account attributes. 

            
            

            - **Name** *(string) --* 

              The attribute name. The following are supported attribute names. 

               

               
              * *ServerLimit:* The number of current servers/maximum number of servers allowed. By default, you can have a maximum of 10 servers.  
               
              * *ManualBackupLimit:* The number of current manual backups/maximum number of backups allowed. By default, you can have a maximum of 50 manual backups saved.  
               

              
            

            - **Maximum** *(integer) --* 

              The maximum allowed value. 

              
            

            - **Used** *(integer) --* 

              The current usage, such as the current number of servers that are associated with the account. 

              
        
      
    

  .. py:method:: describe_backups(**kwargs)

    

    Describes backups. The results are ordered by time, with newest backups first. If you do not specify a BackupId or ServerName, the command returns all backups. 

     

    This operation is synchronous. 

     

    A ``ResourceNotFoundException`` is thrown when the backup does not exist. A ``ValidationException`` is raised when parameters of the request are not valid. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworkscm-2016-11-01/DescribeBackups>`_    


    **Request Syntax** 
    ::

      response = client.describe_backups(
          BackupId='string',
          ServerName='string',
          NextToken='string',
          MaxResults=123
      )
    :type BackupId: string
    :param BackupId: 

      Describes a single backup. 

      

    
    :type ServerName: string
    :param ServerName: 

      Returns backups for the server with the specified ServerName. 

      

    
    :type NextToken: string
    :param NextToken: 

      NextToken is a string that is returned in some command responses. It indicates that not all entries have been returned, and that you must run at least one more request to get remaining items. To get remaining results, call ``DescribeBackups`` again, and assign the token from the previous results as the value of the ``nextToken`` parameter. If there are no more results, the response object's ``nextToken`` parameter value is ``null`` . Setting a ``nextToken`` value that was not returned in your previous results causes an ``InvalidNextTokenException`` to occur.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      To receive a paginated response, use this parameter to specify the maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a ``NextToken`` value that you can assign to the ``NextToken`` request parameter to get the next set of results. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Backups': [
                {
                    'BackupArn': 'string',
                    'BackupId': 'string',
                    'BackupType': 'AUTOMATED'|'MANUAL',
                    'CreatedAt': datetime(2015, 1, 1),
                    'Description': 'string',
                    'Engine': 'string',
                    'EngineModel': 'string',
                    'EngineVersion': 'string',
                    'InstanceProfileArn': 'string',
                    'InstanceType': 'string',
                    'KeyPair': 'string',
                    'PreferredBackupWindow': 'string',
                    'PreferredMaintenanceWindow': 'string',
                    'S3DataSize': 123,
                    'S3DataUrl': 'string',
                    'S3LogUrl': 'string',
                    'SecurityGroupIds': [
                        'string',
                    ],
                    'ServerName': 'string',
                    'ServiceRoleArn': 'string',
                    'Status': 'IN_PROGRESS'|'OK'|'FAILED'|'DELETING',
                    'StatusDescription': 'string',
                    'SubnetIds': [
                        'string',
                    ],
                    'ToolsVersion': 'string',
                    'UserArn': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Backups** *(list) --* 

          Contains the response to a ``DescribeBackups`` request. 

          
          

          - *(dict) --* 

            Describes a single backup. 

            
            

            - **BackupArn** *(string) --* 

              The ARN of the backup. 

              
            

            - **BackupId** *(string) --* 

              The generated ID of the backup. Example: ``myServerName-yyyyMMddHHmmssSSS``  

              
            

            - **BackupType** *(string) --* 

              The backup type. Valid values are ``automated`` or ``manual`` . 

              
            

            - **CreatedAt** *(datetime) --* 

              The time stamp when the backup was created in the database. Example: ``2016-07-29T13:38:47.520Z``  

              
            

            - **Description** *(string) --* 

              A user-provided description for a manual backup. This field is empty for automated backups. 

              
            

            - **Engine** *(string) --* 

              The engine type that is obtained from the server when the backup is created. 

              
            

            - **EngineModel** *(string) --* 

              The engine model that is obtained from the server when the backup is created. 

              
            

            - **EngineVersion** *(string) --* 

              The engine version that is obtained from the server when the backup is created. 

              
            

            - **InstanceProfileArn** *(string) --* 

              The EC2 instance profile ARN that is obtained from the server when the backup is created. Because this value is stored, you are not required to provide the InstanceProfileArn again if you restore a backup. 

              
            

            - **InstanceType** *(string) --* 

              The instance type that is obtained from the server when the backup is created. 

              
            

            - **KeyPair** *(string) --* 

              The key pair that is obtained from the server when the backup is created. 

              
            

            - **PreferredBackupWindow** *(string) --* 

              The preferred backup period that is obtained from the server when the backup is created. 

              
            

            - **PreferredMaintenanceWindow** *(string) --* 

              The preferred maintenance period that is obtained from the server when the backup is created. 

              
            

            - **S3DataSize** *(integer) --* 

              This field is deprecated and is no longer used. 

              
            

            - **S3DataUrl** *(string) --* 

              This field is deprecated and is no longer used. 

              
            

            - **S3LogUrl** *(string) --* 

              The Amazon S3 URL of the backup's log file. 

              
            

            - **SecurityGroupIds** *(list) --* 

              The security group IDs that are obtained from the server when the backup is created. 

              
              

              - *(string) --* 
          
            

            - **ServerName** *(string) --* 

              The name of the server from which the backup was made. 

              
            

            - **ServiceRoleArn** *(string) --* 

              The service role ARN that is obtained from the server when the backup is created. 

              
            

            - **Status** *(string) --* 

              The status of a backup while in progress. 

              
            

            - **StatusDescription** *(string) --* 

              An informational message about backup status. 

              
            

            - **SubnetIds** *(list) --* 

              The subnet IDs that are obtained from the server when the backup is created. 

              
              

              - *(string) --* 
          
            

            - **ToolsVersion** *(string) --* 

              The version of AWS OpsWorks CM-specific tools that is obtained from the server when the backup is created. 

              
            

            - **UserArn** *(string) --* 

              The IAM user ARN of the requester for manual backups. This field is empty for automated backups. 

              
        
      
        

        - **NextToken** *(string) --* 

          NextToken is a string that is returned in some command responses. It indicates that not all entries have been returned, and that you must run at least one more request to get remaining items. To get remaining results, call ``DescribeBackups`` again, and assign the token from the previous results as the value of the ``nextToken`` parameter. If there are no more results, the response object's ``nextToken`` parameter value is ``null`` . Setting a ``nextToken`` value that was not returned in your previous results causes an ``InvalidNextTokenException`` to occur. 

          
    

  .. py:method:: describe_events(**kwargs)

    

    Describes events for a specified server. Results are ordered by time, with newest events first. 

     

    This operation is synchronous. 

     

    A ``ResourceNotFoundException`` is thrown when the server does not exist. A ``ValidationException`` is raised when parameters of the request are not valid. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworkscm-2016-11-01/DescribeEvents>`_    


    **Request Syntax** 
    ::

      response = client.describe_events(
          ServerName='string',
          NextToken='string',
          MaxResults=123
      )
    :type ServerName: string
    :param ServerName: **[REQUIRED]** 

      The name of the server for which you want to view events.

      

    
    :type NextToken: string
    :param NextToken: 

      NextToken is a string that is returned in some command responses. It indicates that not all entries have been returned, and that you must run at least one more request to get remaining items. To get remaining results, call ``DescribeEvents`` again, and assign the token from the previous results as the value of the ``nextToken`` parameter. If there are no more results, the response object's ``nextToken`` parameter value is ``null`` . Setting a ``nextToken`` value that was not returned in your previous results causes an ``InvalidNextTokenException`` to occur. 

      

    
    :type MaxResults: integer
    :param MaxResults: 

      To receive a paginated response, use this parameter to specify the maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a ``NextToken`` value that you can assign to the ``NextToken`` request parameter to get the next set of results. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ServerEvents': [
                {
                    'CreatedAt': datetime(2015, 1, 1),
                    'ServerName': 'string',
                    'Message': 'string',
                    'LogUrl': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ServerEvents** *(list) --* 

          Contains the response to a ``DescribeEvents`` request. 

          
          

          - *(dict) --* 

            An event that is related to the server, such as the start of maintenance or backup. 

            
            

            - **CreatedAt** *(datetime) --* 

              The time when the event occurred. 

              
            

            - **ServerName** *(string) --* 

              The name of the server on or for which the event occurred. 

              
            

            - **Message** *(string) --* 

              A human-readable informational or status message.

              
            

            - **LogUrl** *(string) --* 

              The Amazon S3 URL of the event's log file.

              
        
      
        

        - **NextToken** *(string) --* 

          NextToken is a string that is returned in some command responses. It indicates that not all entries have been returned, and that you must run at least one more request to get remaining items. To get remaining results, call ``DescribeEvents`` again, and assign the token from the previous results as the value of the ``nextToken`` parameter. If there are no more results, the response object's ``nextToken`` parameter value is ``null`` . Setting a ``nextToken`` value that was not returned in your previous results causes an ``InvalidNextTokenException`` to occur. 

          
    

  .. py:method:: describe_node_association_status(**kwargs)

    

    Returns the current status of an existing association or disassociation request. 

     

    A ``ResourceNotFoundException`` is thrown when no recent association or disassociation request with the specified token is found, or when the server does not exist. A ``ValidationException`` is raised when parameters of the request are not valid. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworkscm-2016-11-01/DescribeNodeAssociationStatus>`_    


    **Request Syntax** 
    ::

      response = client.describe_node_association_status(
          NodeAssociationStatusToken='string',
          ServerName='string'
      )
    :type NodeAssociationStatusToken: string
    :param NodeAssociationStatusToken: **[REQUIRED]** 

      The token returned in either the AssociateNodeResponse or the DisassociateNodeResponse. 

      

    
    :type ServerName: string
    :param ServerName: **[REQUIRED]** 

      The name of the server from which to disassociate the node. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NodeAssociationStatus': 'SUCCESS'|'FAILED'|'IN_PROGRESS',
            'EngineAttributes': [
                {
                    'Name': 'string',
                    'Value': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NodeAssociationStatus** *(string) --* 

          The status of the association or disassociation request. 

           

           **Possible values:**  

           

           
          * ``SUCCESS`` : The association or disassociation succeeded.  
           
          * ``FAILED`` : The association or disassociation failed.  
           
          * ``IN_PROGRESS`` : The association or disassociation is still in progress.  
           

          
        

        - **EngineAttributes** *(list) --* 

          Attributes specific to the node association. In Puppet, the attibute PUPPET_NODE_CERT contains the signed certificate (the result of the CSR). 

          
          

          - *(dict) --* 

            A name and value pair that is specific to the engine of the server. 

            
            

            - **Name** *(string) --* 

              The name of the engine attribute. 

              
            

            - **Value** *(string) --* 

              The value of the engine attribute. 

              
        
      
    

  .. py:method:: describe_servers(**kwargs)

    

    Lists all configuration management servers that are identified with your account. Only the stored results from Amazon DynamoDB are returned. AWS OpsWorks CM does not query other services. 

     

    This operation is synchronous. 

     

    A ``ResourceNotFoundException`` is thrown when the server does not exist. A ``ValidationException`` is raised when parameters of the request are not valid. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworkscm-2016-11-01/DescribeServers>`_    


    **Request Syntax** 
    ::

      response = client.describe_servers(
          ServerName='string',
          NextToken='string',
          MaxResults=123
      )
    :type ServerName: string
    :param ServerName: 

      Describes the server with the specified ServerName.

      

    
    :type NextToken: string
    :param NextToken: 

      NextToken is a string that is returned in some command responses. It indicates that not all entries have been returned, and that you must run at least one more request to get remaining items. To get remaining results, call ``DescribeServers`` again, and assign the token from the previous results as the value of the ``nextToken`` parameter. If there are no more results, the response object's ``nextToken`` parameter value is ``null`` . Setting a ``nextToken`` value that was not returned in your previous results causes an ``InvalidNextTokenException`` to occur. 

      

    
    :type MaxResults: integer
    :param MaxResults: 

      To receive a paginated response, use this parameter to specify the maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a ``NextToken`` value that you can assign to the ``NextToken`` request parameter to get the next set of results. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Servers': [
                {
                    'AssociatePublicIpAddress': True|False,
                    'BackupRetentionCount': 123,
                    'ServerName': 'string',
                    'CreatedAt': datetime(2015, 1, 1),
                    'CloudFormationStackArn': 'string',
                    'DisableAutomatedBackup': True|False,
                    'Endpoint': 'string',
                    'Engine': 'string',
                    'EngineModel': 'string',
                    'EngineAttributes': [
                        {
                            'Name': 'string',
                            'Value': 'string'
                        },
                    ],
                    'EngineVersion': 'string',
                    'InstanceProfileArn': 'string',
                    'InstanceType': 'string',
                    'KeyPair': 'string',
                    'MaintenanceStatus': 'SUCCESS'|'FAILED',
                    'PreferredMaintenanceWindow': 'string',
                    'PreferredBackupWindow': 'string',
                    'SecurityGroupIds': [
                        'string',
                    ],
                    'ServiceRoleArn': 'string',
                    'Status': 'BACKING_UP'|'CONNECTION_LOST'|'CREATING'|'DELETING'|'MODIFYING'|'FAILED'|'HEALTHY'|'RUNNING'|'RESTORING'|'SETUP'|'UNDER_MAINTENANCE'|'UNHEALTHY'|'TERMINATED',
                    'StatusReason': 'string',
                    'SubnetIds': [
                        'string',
                    ],
                    'ServerArn': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Servers** *(list) --* 

          Contains the response to a ``DescribeServers`` request.

           

           *For Puppet Server:*  ``DescribeServersResponse$Servers$EngineAttributes`` contains PUPPET_API_CA_CERT. This is the PEM-encoded CA certificate that is used by the Puppet API over TCP port number 8140. The CA certificate is also used to sign node certificates.

          
          

          - *(dict) --* 

            Describes a configuration management server. 

            
            

            - **AssociatePublicIpAddress** *(boolean) --* 

              Associate a public IP address with a server that you are launching. 

              
            

            - **BackupRetentionCount** *(integer) --* 

              The number of automated backups to keep. 

              
            

            - **ServerName** *(string) --* 

              The name of the server. 

              
            

            - **CreatedAt** *(datetime) --* 

              Time stamp of server creation. Example ``2016-07-29T13:38:47.520Z``  

              
            

            - **CloudFormationStackArn** *(string) --* 

              The ARN of the CloudFormation stack that was used to create the server. 

              
            

            - **DisableAutomatedBackup** *(boolean) --* 

              Disables automated backups. The number of stored backups is dependent on the value of PreferredBackupCount. 

              
            

            - **Endpoint** *(string) --* 

              A DNS name that can be used to access the engine. Example: ``myserver-asdfghjkl.us-east-1.opsworks.io``  

              
            

            - **Engine** *(string) --* 

              The engine type of the server. Valid values in this release include ``Chef`` and ``Puppet`` . 

              
            

            - **EngineModel** *(string) --* 

              The engine model of the server. Valid values in this release include ``Monolithic`` for Puppet and ``Single`` for Chef. 

              
            

            - **EngineAttributes** *(list) --* 

              The response of a createServer() request returns the master credential to access the server in EngineAttributes. These credentials are not stored by AWS OpsWorks CM; they are returned only as part of the result of createServer(). 

               

               **Attributes returned in a createServer response for Chef**  

               

               
              * ``CHEF_PIVOTAL_KEY`` : A base64-encoded RSA private key that is generated by AWS OpsWorks for Chef Automate. This private key is required to access the Chef API. 
               
              * ``CHEF_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Chef starter kit, which includes a README, a configuration file, and the required RSA private key. Save this file, unzip it, and then change to the directory where you've unzipped the file contents. From this directory, you can run Knife commands. 
               

               

               **Attributes returned in a createServer response for Puppet**  

               

               
              * ``PUPPET_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Puppet starter kit, including a README and a required private key. Save this file, unzip it, and then change to the directory where you've unzipped the file contents. 
               
              * ``PUPPET_ADMIN_PASSWORD`` : An administrator password that you can use to sign in to the Puppet Enterprise console after the server is online. 
               

              
              

              - *(dict) --* 

                A name and value pair that is specific to the engine of the server. 

                
                

                - **Name** *(string) --* 

                  The name of the engine attribute. 

                  
                

                - **Value** *(string) --* 

                  The value of the engine attribute. 

                  
            
          
            

            - **EngineVersion** *(string) --* 

              The engine version of the server. For a Chef server, the valid value for EngineVersion is currently ``12`` . For a Puppet server, the valid value is ``2017`` . 

              
            

            - **InstanceProfileArn** *(string) --* 

              The instance profile ARN of the server. 

              
            

            - **InstanceType** *(string) --* 

              The instance type for the server, as specified in the CloudFormation stack. This might not be the same instance type that is shown in the EC2 console. 

              
            

            - **KeyPair** *(string) --* 

              The key pair associated with the server. 

              
            

            - **MaintenanceStatus** *(string) --* 

              The status of the most recent server maintenance run. Shows ``SUCCESS`` or ``FAILED`` . 

              
            

            - **PreferredMaintenanceWindow** *(string) --* 

              The preferred maintenance period specified for the server. 

              
            

            - **PreferredBackupWindow** *(string) --* 

              The preferred backup period specified for the server. 

              
            

            - **SecurityGroupIds** *(list) --* 

              The security group IDs for the server, as specified in the CloudFormation stack. These might not be the same security groups that are shown in the EC2 console. 

              
              

              - *(string) --* 
          
            

            - **ServiceRoleArn** *(string) --* 

              The service role ARN used to create the server. 

              
            

            - **Status** *(string) --* 

              The server's status. This field displays the states of actions in progress, such as creating, running, or backing up the server, as well as the server's health state. 

              
            

            - **StatusReason** *(string) --* 

              Depending on the server status, this field has either a human-readable message (such as a create or backup error), or an escaped block of JSON (used for health check results). 

              
            

            - **SubnetIds** *(list) --* 

              The subnet IDs specified in a CreateServer request. 

              
              

              - *(string) --* 
          
            

            - **ServerArn** *(string) --* 

              The ARN of the server. 

              
        
      
        

        - **NextToken** *(string) --* 

          NextToken is a string that is returned in some command responses. It indicates that not all entries have been returned, and that you must run at least one more request to get remaining items. To get remaining results, call ``DescribeServers`` again, and assign the token from the previous results as the value of the ``nextToken`` parameter. If there are no more results, the response object's ``nextToken`` parameter value is ``null`` . Setting a ``nextToken`` value that was not returned in your previous results causes an ``InvalidNextTokenException`` to occur. 

          
    

  .. py:method:: disassociate_node(**kwargs)

    

    Disassociates a node from an AWS OpsWorks CM server, and removes the node from the server's managed nodes. After a node is disassociated, the node key pair is no longer valid for accessing the configuration manager's API. For more information about how to associate a node, see  AssociateNode . 

     

    A node can can only be disassociated from a server that is in a ``HEALTHY`` state. Otherwise, an ``InvalidStateException`` is thrown. A ``ResourceNotFoundException`` is thrown when the server does not exist. A ``ValidationException`` is raised when parameters of the request are not valid. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworkscm-2016-11-01/DisassociateNode>`_    


    **Request Syntax** 
    ::

      response = client.disassociate_node(
          ServerName='string',
          NodeName='string',
          EngineAttributes=[
              {
                  'Name': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type ServerName: string
    :param ServerName: **[REQUIRED]** 

      The name of the server from which to disassociate the node. 

      

    
    :type NodeName: string
    :param NodeName: **[REQUIRED]** 

      The name of the client node. 

      

    
    :type EngineAttributes: list
    :param EngineAttributes: 

      Engine attributes that are used for disassociating the node. No attributes are required for Puppet. 

       

       **Attributes required in a DisassociateNode request for Chef**  

       

       
      * ``CHEF_ORGANIZATION`` : The Chef organization with which the node was associated. By default only one organization named ``default`` can exist.  
       

      

    
      - *(dict) --* 

        A name and value pair that is specific to the engine of the server. 

        

      
        - **Name** *(string) --* 

          The name of the engine attribute. 

          

        
        - **Value** *(string) --* 

          The value of the engine attribute. 

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NodeAssociationStatusToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NodeAssociationStatusToken** *(string) --* 

          Contains a token which can be passed to the ``DescribeNodeAssociationStatus`` API call to get the status of the disassociation request. 

          
    

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

        


  .. py:method:: restore_server(**kwargs)

    

    Restores a backup to a server that is in a ``CONNECTION_LOST`` , ``HEALTHY`` , ``RUNNING`` , ``UNHEALTHY`` , or ``TERMINATED`` state. When you run RestoreServer, the server's EC2 instance is deleted, and a new EC2 instance is configured. RestoreServer maintains the existing server endpoint, so configuration management of the server's client devices (nodes) should continue to work. 

     

    This operation is asynchronous. 

     

    An ``InvalidStateException`` is thrown when the server is not in a valid state. A ``ResourceNotFoundException`` is thrown when the server does not exist. A ``ValidationException`` is raised when parameters of the request are not valid. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworkscm-2016-11-01/RestoreServer>`_    


    **Request Syntax** 
    ::

      response = client.restore_server(
          BackupId='string',
          ServerName='string',
          InstanceType='string',
          KeyPair='string'
      )
    :type BackupId: string
    :param BackupId: **[REQUIRED]** 

      The ID of the backup that you want to use to restore a server. 

      

    
    :type ServerName: string
    :param ServerName: **[REQUIRED]** 

      The name of the server that you want to restore. 

      

    
    :type InstanceType: string
    :param InstanceType: 

      The type of the instance to create. Valid values must be specified in the following format: ``^([cm][34]|t2).*`` For example, ``m4.large`` . Valid values are ``t2.medium`` , ``m4.large`` , and ``m4.2xlarge`` . If you do not specify this parameter, RestoreServer uses the instance type from the specified backup. 

      

    
    :type KeyPair: string
    :param KeyPair: 

      The name of the key pair to set on the new EC2 instance. This can be helpful if the administrator no longer has the SSH key. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: start_maintenance(**kwargs)

    

    Manually starts server maintenance. This command can be useful if an earlier maintenance attempt failed, and the underlying cause of maintenance failure has been resolved. The server is in an ``UNDER_MAINTENANCE`` state while maintenance is in progress. 

     

    Maintenance can only be started on servers in ``HEALTHY`` and ``UNHEALTHY`` states. Otherwise, an ``InvalidStateException`` is thrown. A ``ResourceNotFoundException`` is thrown when the server does not exist. A ``ValidationException`` is raised when parameters of the request are not valid. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworkscm-2016-11-01/StartMaintenance>`_    


    **Request Syntax** 
    ::

      response = client.start_maintenance(
          ServerName='string',
          EngineAttributes=[
              {
                  'Name': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type ServerName: string
    :param ServerName: **[REQUIRED]** 

      The name of the server on which to run maintenance. 

      

    
    :type EngineAttributes: list
    :param EngineAttributes: 

      Engine attributes that are specific to the server on which you want to run maintenance. 

      

    
      - *(dict) --* 

        A name and value pair that is specific to the engine of the server. 

        

      
        - **Name** *(string) --* 

          The name of the engine attribute. 

          

        
        - **Value** *(string) --* 

          The value of the engine attribute. 

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Server': {
                'AssociatePublicIpAddress': True|False,
                'BackupRetentionCount': 123,
                'ServerName': 'string',
                'CreatedAt': datetime(2015, 1, 1),
                'CloudFormationStackArn': 'string',
                'DisableAutomatedBackup': True|False,
                'Endpoint': 'string',
                'Engine': 'string',
                'EngineModel': 'string',
                'EngineAttributes': [
                    {
                        'Name': 'string',
                        'Value': 'string'
                    },
                ],
                'EngineVersion': 'string',
                'InstanceProfileArn': 'string',
                'InstanceType': 'string',
                'KeyPair': 'string',
                'MaintenanceStatus': 'SUCCESS'|'FAILED',
                'PreferredMaintenanceWindow': 'string',
                'PreferredBackupWindow': 'string',
                'SecurityGroupIds': [
                    'string',
                ],
                'ServiceRoleArn': 'string',
                'Status': 'BACKING_UP'|'CONNECTION_LOST'|'CREATING'|'DELETING'|'MODIFYING'|'FAILED'|'HEALTHY'|'RUNNING'|'RESTORING'|'SETUP'|'UNDER_MAINTENANCE'|'UNHEALTHY'|'TERMINATED',
                'StatusReason': 'string',
                'SubnetIds': [
                    'string',
                ],
                'ServerArn': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Server** *(dict) --* 

          Contains the response to a ``StartMaintenance`` request. 

          
          

          - **AssociatePublicIpAddress** *(boolean) --* 

            Associate a public IP address with a server that you are launching. 

            
          

          - **BackupRetentionCount** *(integer) --* 

            The number of automated backups to keep. 

            
          

          - **ServerName** *(string) --* 

            The name of the server. 

            
          

          - **CreatedAt** *(datetime) --* 

            Time stamp of server creation. Example ``2016-07-29T13:38:47.520Z``  

            
          

          - **CloudFormationStackArn** *(string) --* 

            The ARN of the CloudFormation stack that was used to create the server. 

            
          

          - **DisableAutomatedBackup** *(boolean) --* 

            Disables automated backups. The number of stored backups is dependent on the value of PreferredBackupCount. 

            
          

          - **Endpoint** *(string) --* 

            A DNS name that can be used to access the engine. Example: ``myserver-asdfghjkl.us-east-1.opsworks.io``  

            
          

          - **Engine** *(string) --* 

            The engine type of the server. Valid values in this release include ``Chef`` and ``Puppet`` . 

            
          

          - **EngineModel** *(string) --* 

            The engine model of the server. Valid values in this release include ``Monolithic`` for Puppet and ``Single`` for Chef. 

            
          

          - **EngineAttributes** *(list) --* 

            The response of a createServer() request returns the master credential to access the server in EngineAttributes. These credentials are not stored by AWS OpsWorks CM; they are returned only as part of the result of createServer(). 

             

             **Attributes returned in a createServer response for Chef**  

             

             
            * ``CHEF_PIVOTAL_KEY`` : A base64-encoded RSA private key that is generated by AWS OpsWorks for Chef Automate. This private key is required to access the Chef API. 
             
            * ``CHEF_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Chef starter kit, which includes a README, a configuration file, and the required RSA private key. Save this file, unzip it, and then change to the directory where you've unzipped the file contents. From this directory, you can run Knife commands. 
             

             

             **Attributes returned in a createServer response for Puppet**  

             

             
            * ``PUPPET_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Puppet starter kit, including a README and a required private key. Save this file, unzip it, and then change to the directory where you've unzipped the file contents. 
             
            * ``PUPPET_ADMIN_PASSWORD`` : An administrator password that you can use to sign in to the Puppet Enterprise console after the server is online. 
             

            
            

            - *(dict) --* 

              A name and value pair that is specific to the engine of the server. 

              
              

              - **Name** *(string) --* 

                The name of the engine attribute. 

                
              

              - **Value** *(string) --* 

                The value of the engine attribute. 

                
          
        
          

          - **EngineVersion** *(string) --* 

            The engine version of the server. For a Chef server, the valid value for EngineVersion is currently ``12`` . For a Puppet server, the valid value is ``2017`` . 

            
          

          - **InstanceProfileArn** *(string) --* 

            The instance profile ARN of the server. 

            
          

          - **InstanceType** *(string) --* 

            The instance type for the server, as specified in the CloudFormation stack. This might not be the same instance type that is shown in the EC2 console. 

            
          

          - **KeyPair** *(string) --* 

            The key pair associated with the server. 

            
          

          - **MaintenanceStatus** *(string) --* 

            The status of the most recent server maintenance run. Shows ``SUCCESS`` or ``FAILED`` . 

            
          

          - **PreferredMaintenanceWindow** *(string) --* 

            The preferred maintenance period specified for the server. 

            
          

          - **PreferredBackupWindow** *(string) --* 

            The preferred backup period specified for the server. 

            
          

          - **SecurityGroupIds** *(list) --* 

            The security group IDs for the server, as specified in the CloudFormation stack. These might not be the same security groups that are shown in the EC2 console. 

            
            

            - *(string) --* 
        
          

          - **ServiceRoleArn** *(string) --* 

            The service role ARN used to create the server. 

            
          

          - **Status** *(string) --* 

            The server's status. This field displays the states of actions in progress, such as creating, running, or backing up the server, as well as the server's health state. 

            
          

          - **StatusReason** *(string) --* 

            Depending on the server status, this field has either a human-readable message (such as a create or backup error), or an escaped block of JSON (used for health check results). 

            
          

          - **SubnetIds** *(list) --* 

            The subnet IDs specified in a CreateServer request. 

            
            

            - *(string) --* 
        
          

          - **ServerArn** *(string) --* 

            The ARN of the server. 

            
      
    

  .. py:method:: update_server(**kwargs)

    

    Updates settings for a server. 

     

    This operation is synchronous. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworkscm-2016-11-01/UpdateServer>`_    


    **Request Syntax** 
    ::

      response = client.update_server(
          DisableAutomatedBackup=True|False,
          BackupRetentionCount=123,
          ServerName='string',
          PreferredMaintenanceWindow='string',
          PreferredBackupWindow='string'
      )
    :type DisableAutomatedBackup: boolean
    :param DisableAutomatedBackup: 

      Setting DisableAutomatedBackup to ``true`` disables automated or scheduled backups. Automated backups are enabled by default. 

      

    
    :type BackupRetentionCount: integer
    :param BackupRetentionCount: 

      Sets the number of automated backups that you want to keep. 

      

    
    :type ServerName: string
    :param ServerName: **[REQUIRED]** 

      The name of the server to update. 

      

    
    :type PreferredMaintenanceWindow: string
    :param PreferredMaintenanceWindow: 

       ``DDD:HH:MM`` (weekly start time) or ``HH:MM`` (daily start time). 

       

      Time windows always use coordinated universal time (UTC). Valid strings for day of week (``DDD`` ) are: ``Mon`` , ``Tue`` , ``Wed`` , ``Thr`` , ``Fri`` , ``Sat`` , or ``Sun`` .

      

    
    :type PreferredBackupWindow: string
    :param PreferredBackupWindow: 

       ``DDD:HH:MM`` (weekly start time) or ``HH:MM`` (daily start time). 

       

      Time windows always use coordinated universal time (UTC). Valid strings for day of week (``DDD`` ) are: ``Mon`` , ``Tue`` , ``Wed`` , ``Thr`` , ``Fri`` , ``Sat`` , or ``Sun`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Server': {
                'AssociatePublicIpAddress': True|False,
                'BackupRetentionCount': 123,
                'ServerName': 'string',
                'CreatedAt': datetime(2015, 1, 1),
                'CloudFormationStackArn': 'string',
                'DisableAutomatedBackup': True|False,
                'Endpoint': 'string',
                'Engine': 'string',
                'EngineModel': 'string',
                'EngineAttributes': [
                    {
                        'Name': 'string',
                        'Value': 'string'
                    },
                ],
                'EngineVersion': 'string',
                'InstanceProfileArn': 'string',
                'InstanceType': 'string',
                'KeyPair': 'string',
                'MaintenanceStatus': 'SUCCESS'|'FAILED',
                'PreferredMaintenanceWindow': 'string',
                'PreferredBackupWindow': 'string',
                'SecurityGroupIds': [
                    'string',
                ],
                'ServiceRoleArn': 'string',
                'Status': 'BACKING_UP'|'CONNECTION_LOST'|'CREATING'|'DELETING'|'MODIFYING'|'FAILED'|'HEALTHY'|'RUNNING'|'RESTORING'|'SETUP'|'UNDER_MAINTENANCE'|'UNHEALTHY'|'TERMINATED',
                'StatusReason': 'string',
                'SubnetIds': [
                    'string',
                ],
                'ServerArn': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Server** *(dict) --* 

          Contains the response to a ``UpdateServer`` request. 

          
          

          - **AssociatePublicIpAddress** *(boolean) --* 

            Associate a public IP address with a server that you are launching. 

            
          

          - **BackupRetentionCount** *(integer) --* 

            The number of automated backups to keep. 

            
          

          - **ServerName** *(string) --* 

            The name of the server. 

            
          

          - **CreatedAt** *(datetime) --* 

            Time stamp of server creation. Example ``2016-07-29T13:38:47.520Z``  

            
          

          - **CloudFormationStackArn** *(string) --* 

            The ARN of the CloudFormation stack that was used to create the server. 

            
          

          - **DisableAutomatedBackup** *(boolean) --* 

            Disables automated backups. The number of stored backups is dependent on the value of PreferredBackupCount. 

            
          

          - **Endpoint** *(string) --* 

            A DNS name that can be used to access the engine. Example: ``myserver-asdfghjkl.us-east-1.opsworks.io``  

            
          

          - **Engine** *(string) --* 

            The engine type of the server. Valid values in this release include ``Chef`` and ``Puppet`` . 

            
          

          - **EngineModel** *(string) --* 

            The engine model of the server. Valid values in this release include ``Monolithic`` for Puppet and ``Single`` for Chef. 

            
          

          - **EngineAttributes** *(list) --* 

            The response of a createServer() request returns the master credential to access the server in EngineAttributes. These credentials are not stored by AWS OpsWorks CM; they are returned only as part of the result of createServer(). 

             

             **Attributes returned in a createServer response for Chef**  

             

             
            * ``CHEF_PIVOTAL_KEY`` : A base64-encoded RSA private key that is generated by AWS OpsWorks for Chef Automate. This private key is required to access the Chef API. 
             
            * ``CHEF_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Chef starter kit, which includes a README, a configuration file, and the required RSA private key. Save this file, unzip it, and then change to the directory where you've unzipped the file contents. From this directory, you can run Knife commands. 
             

             

             **Attributes returned in a createServer response for Puppet**  

             

             
            * ``PUPPET_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Puppet starter kit, including a README and a required private key. Save this file, unzip it, and then change to the directory where you've unzipped the file contents. 
             
            * ``PUPPET_ADMIN_PASSWORD`` : An administrator password that you can use to sign in to the Puppet Enterprise console after the server is online. 
             

            
            

            - *(dict) --* 

              A name and value pair that is specific to the engine of the server. 

              
              

              - **Name** *(string) --* 

                The name of the engine attribute. 

                
              

              - **Value** *(string) --* 

                The value of the engine attribute. 

                
          
        
          

          - **EngineVersion** *(string) --* 

            The engine version of the server. For a Chef server, the valid value for EngineVersion is currently ``12`` . For a Puppet server, the valid value is ``2017`` . 

            
          

          - **InstanceProfileArn** *(string) --* 

            The instance profile ARN of the server. 

            
          

          - **InstanceType** *(string) --* 

            The instance type for the server, as specified in the CloudFormation stack. This might not be the same instance type that is shown in the EC2 console. 

            
          

          - **KeyPair** *(string) --* 

            The key pair associated with the server. 

            
          

          - **MaintenanceStatus** *(string) --* 

            The status of the most recent server maintenance run. Shows ``SUCCESS`` or ``FAILED`` . 

            
          

          - **PreferredMaintenanceWindow** *(string) --* 

            The preferred maintenance period specified for the server. 

            
          

          - **PreferredBackupWindow** *(string) --* 

            The preferred backup period specified for the server. 

            
          

          - **SecurityGroupIds** *(list) --* 

            The security group IDs for the server, as specified in the CloudFormation stack. These might not be the same security groups that are shown in the EC2 console. 

            
            

            - *(string) --* 
        
          

          - **ServiceRoleArn** *(string) --* 

            The service role ARN used to create the server. 

            
          

          - **Status** *(string) --* 

            The server's status. This field displays the states of actions in progress, such as creating, running, or backing up the server, as well as the server's health state. 

            
          

          - **StatusReason** *(string) --* 

            Depending on the server status, this field has either a human-readable message (such as a create or backup error), or an escaped block of JSON (used for health check results). 

            
          

          - **SubnetIds** *(list) --* 

            The subnet IDs specified in a CreateServer request. 

            
            

            - *(string) --* 
        
          

          - **ServerArn** *(string) --* 

            The ARN of the server. 

            
      
    

  .. py:method:: update_server_engine_attributes(**kwargs)

    

    Updates engine-specific attributes on a specified server. The server enters the ``MODIFYING`` state when this operation is in progress. Only one update can occur at a time. You can use this command to reset a Chef server's private key (``CHEF_PIVOTAL_KEY`` ), a Chef server's admin password (``CHEF_DELIVERY_ADMIN_PASSWORD`` ), or a Puppet server's admin password (``PUPPET_ADMIN_PASSWORD`` ). 

     

    This operation is asynchronous. 

     

    This operation can only be called for servers in ``HEALTHY`` or ``UNHEALTHY`` states. Otherwise, an ``InvalidStateException`` is raised. A ``ResourceNotFoundException`` is thrown when the server does not exist. A ``ValidationException`` is raised when parameters of the request are not valid. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworkscm-2016-11-01/UpdateServerEngineAttributes>`_    


    **Request Syntax** 
    ::

      response = client.update_server_engine_attributes(
          ServerName='string',
          AttributeName='string',
          AttributeValue='string'
      )
    :type ServerName: string
    :param ServerName: **[REQUIRED]** 

      The name of the server to update. 

      

    
    :type AttributeName: string
    :param AttributeName: **[REQUIRED]** 

      The name of the engine attribute to update. 

      

    
    :type AttributeValue: string
    :param AttributeValue: 

      The value to set for the attribute. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Server': {
                'AssociatePublicIpAddress': True|False,
                'BackupRetentionCount': 123,
                'ServerName': 'string',
                'CreatedAt': datetime(2015, 1, 1),
                'CloudFormationStackArn': 'string',
                'DisableAutomatedBackup': True|False,
                'Endpoint': 'string',
                'Engine': 'string',
                'EngineModel': 'string',
                'EngineAttributes': [
                    {
                        'Name': 'string',
                        'Value': 'string'
                    },
                ],
                'EngineVersion': 'string',
                'InstanceProfileArn': 'string',
                'InstanceType': 'string',
                'KeyPair': 'string',
                'MaintenanceStatus': 'SUCCESS'|'FAILED',
                'PreferredMaintenanceWindow': 'string',
                'PreferredBackupWindow': 'string',
                'SecurityGroupIds': [
                    'string',
                ],
                'ServiceRoleArn': 'string',
                'Status': 'BACKING_UP'|'CONNECTION_LOST'|'CREATING'|'DELETING'|'MODIFYING'|'FAILED'|'HEALTHY'|'RUNNING'|'RESTORING'|'SETUP'|'UNDER_MAINTENANCE'|'UNHEALTHY'|'TERMINATED',
                'StatusReason': 'string',
                'SubnetIds': [
                    'string',
                ],
                'ServerArn': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Server** *(dict) --* 

          Contains the response to an ``UpdateServerEngineAttributes`` request. 

          
          

          - **AssociatePublicIpAddress** *(boolean) --* 

            Associate a public IP address with a server that you are launching. 

            
          

          - **BackupRetentionCount** *(integer) --* 

            The number of automated backups to keep. 

            
          

          - **ServerName** *(string) --* 

            The name of the server. 

            
          

          - **CreatedAt** *(datetime) --* 

            Time stamp of server creation. Example ``2016-07-29T13:38:47.520Z``  

            
          

          - **CloudFormationStackArn** *(string) --* 

            The ARN of the CloudFormation stack that was used to create the server. 

            
          

          - **DisableAutomatedBackup** *(boolean) --* 

            Disables automated backups. The number of stored backups is dependent on the value of PreferredBackupCount. 

            
          

          - **Endpoint** *(string) --* 

            A DNS name that can be used to access the engine. Example: ``myserver-asdfghjkl.us-east-1.opsworks.io``  

            
          

          - **Engine** *(string) --* 

            The engine type of the server. Valid values in this release include ``Chef`` and ``Puppet`` . 

            
          

          - **EngineModel** *(string) --* 

            The engine model of the server. Valid values in this release include ``Monolithic`` for Puppet and ``Single`` for Chef. 

            
          

          - **EngineAttributes** *(list) --* 

            The response of a createServer() request returns the master credential to access the server in EngineAttributes. These credentials are not stored by AWS OpsWorks CM; they are returned only as part of the result of createServer(). 

             

             **Attributes returned in a createServer response for Chef**  

             

             
            * ``CHEF_PIVOTAL_KEY`` : A base64-encoded RSA private key that is generated by AWS OpsWorks for Chef Automate. This private key is required to access the Chef API. 
             
            * ``CHEF_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Chef starter kit, which includes a README, a configuration file, and the required RSA private key. Save this file, unzip it, and then change to the directory where you've unzipped the file contents. From this directory, you can run Knife commands. 
             

             

             **Attributes returned in a createServer response for Puppet**  

             

             
            * ``PUPPET_STARTER_KIT`` : A base64-encoded ZIP file. The ZIP file contains a Puppet starter kit, including a README and a required private key. Save this file, unzip it, and then change to the directory where you've unzipped the file contents. 
             
            * ``PUPPET_ADMIN_PASSWORD`` : An administrator password that you can use to sign in to the Puppet Enterprise console after the server is online. 
             

            
            

            - *(dict) --* 

              A name and value pair that is specific to the engine of the server. 

              
              

              - **Name** *(string) --* 

                The name of the engine attribute. 

                
              

              - **Value** *(string) --* 

                The value of the engine attribute. 

                
          
        
          

          - **EngineVersion** *(string) --* 

            The engine version of the server. For a Chef server, the valid value for EngineVersion is currently ``12`` . For a Puppet server, the valid value is ``2017`` . 

            
          

          - **InstanceProfileArn** *(string) --* 

            The instance profile ARN of the server. 

            
          

          - **InstanceType** *(string) --* 

            The instance type for the server, as specified in the CloudFormation stack. This might not be the same instance type that is shown in the EC2 console. 

            
          

          - **KeyPair** *(string) --* 

            The key pair associated with the server. 

            
          

          - **MaintenanceStatus** *(string) --* 

            The status of the most recent server maintenance run. Shows ``SUCCESS`` or ``FAILED`` . 

            
          

          - **PreferredMaintenanceWindow** *(string) --* 

            The preferred maintenance period specified for the server. 

            
          

          - **PreferredBackupWindow** *(string) --* 

            The preferred backup period specified for the server. 

            
          

          - **SecurityGroupIds** *(list) --* 

            The security group IDs for the server, as specified in the CloudFormation stack. These might not be the same security groups that are shown in the EC2 console. 

            
            

            - *(string) --* 
        
          

          - **ServiceRoleArn** *(string) --* 

            The service role ARN used to create the server. 

            
          

          - **Status** *(string) --* 

            The server's status. This field displays the states of actions in progress, such as creating, running, or backing up the server, as well as the server's health state. 

            
          

          - **StatusReason** *(string) --* 

            Depending on the server status, this field has either a human-readable message (such as a create or backup error), or an escaped block of JSON (used for health check results). 

            
          

          - **SubnetIds** *(list) --* 

            The subnet IDs specified in a CreateServer request. 

            
            

            - *(string) --* 
        
          

          - **ServerArn** *(string) --* 

            The ARN of the server. 

            
      
    

==========
Paginators
==========


The available paginators are:


=======
Waiters
=======


The available waiters are:

* :py:class:`OpsWorksCM.Waiter.NodeAssociated`



.. py:class:: OpsWorksCM.Waiter.NodeAssociated

  ::

    
    waiter = client.get_waiter('node_associated')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`OpsWorksCM.Client.describe_node_association_status` every 15 seconds until a successful state is reached. An error is returned after 15 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/opsworkscm-2016-11-01/DescribeNodeAssociationStatus>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          NodeAssociationStatusToken='string',
          ServerName='string',
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type NodeAssociationStatusToken: string
    :param NodeAssociationStatusToken: **[REQUIRED]** 

      The token returned in either the AssociateNodeResponse or the DisassociateNodeResponse. 

      

    
    :type ServerName: string
    :param ServerName: **[REQUIRED]** 

      The name of the server from which to disassociate the node. 

      

    
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 15

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 15

        

      
    
    
    :returns: None