

***
IoT
***

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: IoT.Client

  A low-level client representing AWS IoT::

    
    import boto3
    
    client = boto3.client('iot')

  
  These are the available methods:
  
  *   :py:meth:`~IoT.Client.accept_certificate_transfer`

  
  *   :py:meth:`~IoT.Client.add_thing_to_thing_group`

  
  *   :py:meth:`~IoT.Client.associate_targets_with_job`

  
  *   :py:meth:`~IoT.Client.attach_policy`

  
  *   :py:meth:`~IoT.Client.attach_principal_policy`

  
  *   :py:meth:`~IoT.Client.attach_thing_principal`

  
  *   :py:meth:`~IoT.Client.can_paginate`

  
  *   :py:meth:`~IoT.Client.cancel_certificate_transfer`

  
  *   :py:meth:`~IoT.Client.cancel_job`

  
  *   :py:meth:`~IoT.Client.clear_default_authorizer`

  
  *   :py:meth:`~IoT.Client.create_authorizer`

  
  *   :py:meth:`~IoT.Client.create_certificate_from_csr`

  
  *   :py:meth:`~IoT.Client.create_job`

  
  *   :py:meth:`~IoT.Client.create_keys_and_certificate`

  
  *   :py:meth:`~IoT.Client.create_policy`

  
  *   :py:meth:`~IoT.Client.create_policy_version`

  
  *   :py:meth:`~IoT.Client.create_role_alias`

  
  *   :py:meth:`~IoT.Client.create_thing`

  
  *   :py:meth:`~IoT.Client.create_thing_group`

  
  *   :py:meth:`~IoT.Client.create_thing_type`

  
  *   :py:meth:`~IoT.Client.create_topic_rule`

  
  *   :py:meth:`~IoT.Client.delete_authorizer`

  
  *   :py:meth:`~IoT.Client.delete_ca_certificate`

  
  *   :py:meth:`~IoT.Client.delete_certificate`

  
  *   :py:meth:`~IoT.Client.delete_policy`

  
  *   :py:meth:`~IoT.Client.delete_policy_version`

  
  *   :py:meth:`~IoT.Client.delete_registration_code`

  
  *   :py:meth:`~IoT.Client.delete_role_alias`

  
  *   :py:meth:`~IoT.Client.delete_thing`

  
  *   :py:meth:`~IoT.Client.delete_thing_group`

  
  *   :py:meth:`~IoT.Client.delete_thing_type`

  
  *   :py:meth:`~IoT.Client.delete_topic_rule`

  
  *   :py:meth:`~IoT.Client.delete_v2_logging_level`

  
  *   :py:meth:`~IoT.Client.deprecate_thing_type`

  
  *   :py:meth:`~IoT.Client.describe_authorizer`

  
  *   :py:meth:`~IoT.Client.describe_ca_certificate`

  
  *   :py:meth:`~IoT.Client.describe_certificate`

  
  *   :py:meth:`~IoT.Client.describe_default_authorizer`

  
  *   :py:meth:`~IoT.Client.describe_endpoint`

  
  *   :py:meth:`~IoT.Client.describe_event_configurations`

  
  *   :py:meth:`~IoT.Client.describe_index`

  
  *   :py:meth:`~IoT.Client.describe_job`

  
  *   :py:meth:`~IoT.Client.describe_job_execution`

  
  *   :py:meth:`~IoT.Client.describe_role_alias`

  
  *   :py:meth:`~IoT.Client.describe_thing`

  
  *   :py:meth:`~IoT.Client.describe_thing_group`

  
  *   :py:meth:`~IoT.Client.describe_thing_registration_task`

  
  *   :py:meth:`~IoT.Client.describe_thing_type`

  
  *   :py:meth:`~IoT.Client.detach_policy`

  
  *   :py:meth:`~IoT.Client.detach_principal_policy`

  
  *   :py:meth:`~IoT.Client.detach_thing_principal`

  
  *   :py:meth:`~IoT.Client.disable_topic_rule`

  
  *   :py:meth:`~IoT.Client.enable_topic_rule`

  
  *   :py:meth:`~IoT.Client.generate_presigned_url`

  
  *   :py:meth:`~IoT.Client.get_effective_policies`

  
  *   :py:meth:`~IoT.Client.get_indexing_configuration`

  
  *   :py:meth:`~IoT.Client.get_job_document`

  
  *   :py:meth:`~IoT.Client.get_logging_options`

  
  *   :py:meth:`~IoT.Client.get_paginator`

  
  *   :py:meth:`~IoT.Client.get_policy`

  
  *   :py:meth:`~IoT.Client.get_policy_version`

  
  *   :py:meth:`~IoT.Client.get_registration_code`

  
  *   :py:meth:`~IoT.Client.get_topic_rule`

  
  *   :py:meth:`~IoT.Client.get_v2_logging_options`

  
  *   :py:meth:`~IoT.Client.get_waiter`

  
  *   :py:meth:`~IoT.Client.list_attached_policies`

  
  *   :py:meth:`~IoT.Client.list_authorizers`

  
  *   :py:meth:`~IoT.Client.list_ca_certificates`

  
  *   :py:meth:`~IoT.Client.list_certificates`

  
  *   :py:meth:`~IoT.Client.list_certificates_by_ca`

  
  *   :py:meth:`~IoT.Client.list_indices`

  
  *   :py:meth:`~IoT.Client.list_job_executions_for_job`

  
  *   :py:meth:`~IoT.Client.list_job_executions_for_thing`

  
  *   :py:meth:`~IoT.Client.list_jobs`

  
  *   :py:meth:`~IoT.Client.list_outgoing_certificates`

  
  *   :py:meth:`~IoT.Client.list_policies`

  
  *   :py:meth:`~IoT.Client.list_policy_principals`

  
  *   :py:meth:`~IoT.Client.list_policy_versions`

  
  *   :py:meth:`~IoT.Client.list_principal_policies`

  
  *   :py:meth:`~IoT.Client.list_principal_things`

  
  *   :py:meth:`~IoT.Client.list_role_aliases`

  
  *   :py:meth:`~IoT.Client.list_targets_for_policy`

  
  *   :py:meth:`~IoT.Client.list_thing_groups`

  
  *   :py:meth:`~IoT.Client.list_thing_groups_for_thing`

  
  *   :py:meth:`~IoT.Client.list_thing_principals`

  
  *   :py:meth:`~IoT.Client.list_thing_registration_task_reports`

  
  *   :py:meth:`~IoT.Client.list_thing_registration_tasks`

  
  *   :py:meth:`~IoT.Client.list_thing_types`

  
  *   :py:meth:`~IoT.Client.list_things`

  
  *   :py:meth:`~IoT.Client.list_things_in_thing_group`

  
  *   :py:meth:`~IoT.Client.list_topic_rules`

  
  *   :py:meth:`~IoT.Client.list_v2_logging_levels`

  
  *   :py:meth:`~IoT.Client.register_ca_certificate`

  
  *   :py:meth:`~IoT.Client.register_certificate`

  
  *   :py:meth:`~IoT.Client.register_thing`

  
  *   :py:meth:`~IoT.Client.reject_certificate_transfer`

  
  *   :py:meth:`~IoT.Client.remove_thing_from_thing_group`

  
  *   :py:meth:`~IoT.Client.replace_topic_rule`

  
  *   :py:meth:`~IoT.Client.search_index`

  
  *   :py:meth:`~IoT.Client.set_default_authorizer`

  
  *   :py:meth:`~IoT.Client.set_default_policy_version`

  
  *   :py:meth:`~IoT.Client.set_logging_options`

  
  *   :py:meth:`~IoT.Client.set_v2_logging_level`

  
  *   :py:meth:`~IoT.Client.set_v2_logging_options`

  
  *   :py:meth:`~IoT.Client.start_thing_registration_task`

  
  *   :py:meth:`~IoT.Client.stop_thing_registration_task`

  
  *   :py:meth:`~IoT.Client.test_authorization`

  
  *   :py:meth:`~IoT.Client.test_invoke_authorizer`

  
  *   :py:meth:`~IoT.Client.transfer_certificate`

  
  *   :py:meth:`~IoT.Client.update_authorizer`

  
  *   :py:meth:`~IoT.Client.update_ca_certificate`

  
  *   :py:meth:`~IoT.Client.update_certificate`

  
  *   :py:meth:`~IoT.Client.update_event_configurations`

  
  *   :py:meth:`~IoT.Client.update_indexing_configuration`

  
  *   :py:meth:`~IoT.Client.update_role_alias`

  
  *   :py:meth:`~IoT.Client.update_thing`

  
  *   :py:meth:`~IoT.Client.update_thing_group`

  
  *   :py:meth:`~IoT.Client.update_thing_groups_for_thing`

  

  .. py:method:: accept_certificate_transfer(**kwargs)

    

    Accepts a pending certificate transfer. The default state of the certificate is INACTIVE.

     

    To check for pending certificate transfers, call  ListCertificates to enumerate your certificates.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/AcceptCertificateTransfer>`_    


    **Request Syntax** 
    ::

      response = client.accept_certificate_transfer(
          certificateId='string',
          setAsActive=True|False
      )
    :type certificateId: string
    :param certificateId: **[REQUIRED]** 

      The ID of the certificate.

      

    
    :type setAsActive: boolean
    :param setAsActive: 

      Specifies whether the certificate is active.

      

    
    
    :returns: None

  .. py:method:: add_thing_to_thing_group(**kwargs)

    

    Adds a thing to a thing group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/AddThingToThingGroup>`_    


    **Request Syntax** 
    ::

      response = client.add_thing_to_thing_group(
          thingGroupName='string',
          thingGroupArn='string',
          thingName='string',
          thingArn='string'
      )
    :type thingGroupName: string
    :param thingGroupName: 

      The name of the group to which you are adding a thing.

      

    
    :type thingGroupArn: string
    :param thingGroupArn: 

      The ARN of the group to which you are adding a thing.

      

    
    :type thingName: string
    :param thingName: 

      The name of the thing to add to a group.

      

    
    :type thingArn: string
    :param thingArn: 

      The ARN of the thing to add to a group.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: associate_targets_with_job(**kwargs)

    

    Associates a group with a continuous job. The following criteria must be met: 

     

     
    * The job must have been created with the ``targetSelection`` field set to "CONTINUOUS". 
     
    * The job status must currently be "IN_PROGRESS". 
     
    * The total number of targets associated with a job must not exceed 100. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/AssociateTargetsWithJob>`_    


    **Request Syntax** 
    ::

      response = client.associate_targets_with_job(
          targets=[
              'string',
          ],
          jobId='string',
          comment='string'
      )
    :type targets: list
    :param targets: **[REQUIRED]** 

      A list of thing group ARNs that define the targets of the job.

      

    
      - *(string) --* 

      
  
    :type jobId: string
    :param jobId: **[REQUIRED]** 

      The unique identifier you assigned to this job when it was created.

      

    
    :type comment: string
    :param comment: 

      An optional comment string describing why the job was associated with the targets.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'jobArn': 'string',
            'jobId': 'string',
            'description': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **jobArn** *(string) --* 

          An ARN identifying the job.

          
        

        - **jobId** *(string) --* 

          The unique identifier you assigned to this job when it was created.

          
        

        - **description** *(string) --* 

          A short text description of the job.

          
    

  .. py:method:: attach_policy(**kwargs)

    

    Attaches a policy to the specified target.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/AttachPolicy>`_    


    **Request Syntax** 
    ::

      response = client.attach_policy(
          policyName='string',
          target='string'
      )
    :type policyName: string
    :param policyName: **[REQUIRED]** 

      The name of the policy to attach.

      

    
    :type target: string
    :param target: **[REQUIRED]** 

      The identity to which the policy is attached.

      

    
    
    :returns: None

  .. py:method:: attach_principal_policy(**kwargs)

    

    Attaches the specified policy to the specified principal (certificate or other credential).

     

     **Note:** This API is deprecated. Please use  AttachPolicy instead.

    

    .. danger::

            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.


    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/AttachPrincipalPolicy>`_    


    **Request Syntax** 
    ::

      response = client.attach_principal_policy(
          policyName='string',
          principal='string'
      )
    :type policyName: string
    :param policyName: **[REQUIRED]** 

      The policy name.

      

    
    :type principal: string
    :param principal: **[REQUIRED]** 

      The principal, which can be a certificate ARN (as returned from the CreateCertificate operation) or an Amazon Cognito ID.

      

    
    
    :returns: None

  .. py:method:: attach_thing_principal(**kwargs)

    

    Attaches the specified principal to the specified thing.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/AttachThingPrincipal>`_    


    **Request Syntax** 
    ::

      response = client.attach_thing_principal(
          thingName='string',
          principal='string'
      )
    :type thingName: string
    :param thingName: **[REQUIRED]** 

      The name of the thing.

      

    
    :type principal: string
    :param principal: **[REQUIRED]** 

      The principal, such as a certificate or other credential.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        The output from the AttachThingPrincipal operation.

        
    

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


  .. py:method:: cancel_certificate_transfer(**kwargs)

    

    Cancels a pending transfer for the specified certificate.

     

     **Note** Only the transfer source account can use this operation to cancel a transfer. (Transfer destinations can use  RejectCertificateTransfer instead.) After transfer, AWS IoT returns the certificate to the source account in the INACTIVE state. After the destination account has accepted the transfer, the transfer cannot be cancelled.

     

    After a certificate transfer is cancelled, the status of the certificate changes from PENDING_TRANSFER to INACTIVE.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CancelCertificateTransfer>`_    


    **Request Syntax** 
    ::

      response = client.cancel_certificate_transfer(
          certificateId='string'
      )
    :type certificateId: string
    :param certificateId: **[REQUIRED]** 

      The ID of the certificate.

      

    
    
    :returns: None

  .. py:method:: cancel_job(**kwargs)

    

    Cancels a job.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CancelJob>`_    


    **Request Syntax** 
    ::

      response = client.cancel_job(
          jobId='string',
          comment='string'
      )
    :type jobId: string
    :param jobId: **[REQUIRED]** 

      The unique identifier you assigned to this job when it was created.

      

    
    :type comment: string
    :param comment: 

      An optional comment string describing why the job was canceled.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'jobArn': 'string',
            'jobId': 'string',
            'description': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **jobArn** *(string) --* 

          The job ARN.

          
        

        - **jobId** *(string) --* 

          The unique identifier you assigned to this job when it was created.

          
        

        - **description** *(string) --* 

          A short text description of the job.

          
    

  .. py:method:: clear_default_authorizer()

    

    Clears the default authorizer.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ClearDefaultAuthorizer>`_    


    **Request Syntax** 
    ::

      response = client.clear_default_authorizer()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: create_authorizer(**kwargs)

    

    Creates an authorizer.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateAuthorizer>`_    


    **Request Syntax** 
    ::

      response = client.create_authorizer(
          authorizerName='string',
          authorizerFunctionArn='string',
          tokenKeyName='string',
          tokenSigningPublicKeys={
              'string': 'string'
          },
          status='ACTIVE'|'INACTIVE'
      )
    :type authorizerName: string
    :param authorizerName: **[REQUIRED]** 

      The authorizer name.

      

    
    :type authorizerFunctionArn: string
    :param authorizerFunctionArn: **[REQUIRED]** 

      The ARN of the authorizer's Lambda function.

      

    
    :type tokenKeyName: string
    :param tokenKeyName: **[REQUIRED]** 

      The name of the token key used to extract the token from the HTTP headers.

      

    
    :type tokenSigningPublicKeys: dict
    :param tokenSigningPublicKeys: **[REQUIRED]** 

      The public keys used to verify the digital signature returned by your custom authentication service.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type status: string
    :param status: 

      The status of the create authorizer request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'authorizerName': 'string',
            'authorizerArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **authorizerName** *(string) --* 

          The authorizer's name.

          
        

        - **authorizerArn** *(string) --* 

          The authorizer ARN.

          
    

  .. py:method:: create_certificate_from_csr(**kwargs)

    

    Creates an X.509 certificate using the specified certificate signing request.

     

     **Note:** The CSR must include a public key that is either an RSA key with a length of at least 2048 bits or an ECC key from NIST P-256 or NIST P-384 curves. 

     

     **Note:** Reusing the same certificate signing request (CSR) results in a distinct certificate.

     

    You can create multiple certificates in a batch by creating a directory, copying multiple .csr files into that directory, and then specifying that directory on the command line. The following commands show how to create a batch of certificates given a batch of CSRs.

     

    Assuming a set of CSRs are located inside of the directory my-csr-directory:

     

    On Linux and OS X, the command is:

     

    $ ls my-csr-directory/ | xargs -I {} aws iot create-certificate-from-csr --certificate-signing-request file://my-csr-directory/{}

     

    This command lists all of the CSRs in my-csr-directory and pipes each CSR file name to the aws iot create-certificate-from-csr AWS CLI command to create a certificate for the corresponding CSR.

     

    The aws iot create-certificate-from-csr part of the command can also be run in parallel to speed up the certificate creation process:

     

    $ ls my-csr-directory/ | xargs -P 10 -I {} aws iot create-certificate-from-csr --certificate-signing-request file://my-csr-directory/{}

     

    On Windows PowerShell, the command to create certificates for all CSRs in my-csr-directory is:

     

    > ls -Name my-csr-directory | %{aws iot create-certificate-from-csr --certificate-signing-request file://my-csr-directory/$_}

     

    On a Windows command prompt, the command to create certificates for all CSRs in my-csr-directory is:

     

    > forfiles /p my-csr-directory /c "cmd /c aws iot create-certificate-from-csr --certificate-signing-request file://@path"

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateCertificateFromCsr>`_    


    **Request Syntax** 
    ::

      response = client.create_certificate_from_csr(
          certificateSigningRequest='string',
          setAsActive=True|False
      )
    :type certificateSigningRequest: string
    :param certificateSigningRequest: **[REQUIRED]** 

      The certificate signing request (CSR).

      

    
    :type setAsActive: boolean
    :param setAsActive: 

      Specifies whether the certificate is active.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'certificateArn': 'string',
            'certificateId': 'string',
            'certificatePem': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the CreateCertificateFromCsr operation.

        
        

        - **certificateArn** *(string) --* 

          The Amazon Resource Name (ARN) of the certificate. You can use the ARN as a principal for policy operations.

          
        

        - **certificateId** *(string) --* 

          The ID of the certificate. Certificate management operations only take a certificateId.

          
        

        - **certificatePem** *(string) --* 

          The certificate data, in PEM format.

          
    

  .. py:method:: create_job(**kwargs)

    

    Creates a job.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateJob>`_    


    **Request Syntax** 
    ::

      response = client.create_job(
          jobId='string',
          targets=[
              'string',
          ],
          documentSource='string',
          document='string',
          description='string',
          presignedUrlConfig={
              'roleArn': 'string',
              'expiresInSec': 123
          },
          targetSelection='CONTINUOUS'|'SNAPSHOT',
          jobExecutionsRolloutConfig={
              'maximumPerMinute': 123
          },
          documentParameters={
              'string': 'string'
          }
      )
    :type jobId: string
    :param jobId: **[REQUIRED]** 

      A job identifier which must be unique for your AWS account. We recommend using a UUID. Alpha-numeric characters, "-" and "_" are valid for use here.

      

    
    :type targets: list
    :param targets: **[REQUIRED]** 

      A list of things and thing groups to which the job should be sent.

      

    
      - *(string) --* 

      
  
    :type documentSource: string
    :param documentSource: 

      An S3 link to the job document.

      

    
    :type document: string
    :param document: 

      The job document.

      

    
    :type description: string
    :param description: 

      A short text description of the job.

      

    
    :type presignedUrlConfig: dict
    :param presignedUrlConfig: 

      Configuration information for pre-signed S3 URLs.

      

    
      - **roleArn** *(string) --* 

        The ARN of an IAM role that grants grants permission to download files from the S3 bucket where the job data/updates are stored. The role must also grant permission for IoT to download the files.

        

      
      - **expiresInSec** *(integer) --* 

        How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default value is 3600 seconds. Pre-signed URLs are generated when Jobs receives an MQTT request for the job document.

        

      
    
    :type targetSelection: string
    :param targetSelection: 

      Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a thing when the thing is added to a target group, even after the job was completed by all things originally in the group.

      

    
    :type jobExecutionsRolloutConfig: dict
    :param jobExecutionsRolloutConfig: 

      Allows you to create a staged rollout of the job.

      

    
      - **maximumPerMinute** *(integer) --* 

        The maximum number of things that will be notified of a pending job, per minute. This parameter allows you to create a staged rollout.

        

      
    
    :type documentParameters: dict
    :param documentParameters: 

      Parameters for the job document.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'jobArn': 'string',
            'jobId': 'string',
            'description': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **jobArn** *(string) --* 

          The job ARN.

          
        

        - **jobId** *(string) --* 

          The unique identifier you assigned to this job.

          
        

        - **description** *(string) --* 

          The job description.

          
    

  .. py:method:: create_keys_and_certificate(**kwargs)

    

    Creates a 2048-bit RSA key pair and issues an X.509 certificate using the issued public key.

     

     **Note** This is the only time AWS IoT issues the private key for this certificate, so it is important to keep it in a secure location.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateKeysAndCertificate>`_    


    **Request Syntax** 
    ::

      response = client.create_keys_and_certificate(
          setAsActive=True|False
      )
    :type setAsActive: boolean
    :param setAsActive: 

      Specifies whether the certificate is active.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'certificateArn': 'string',
            'certificateId': 'string',
            'certificatePem': 'string',
            'keyPair': {
                'PublicKey': 'string',
                'PrivateKey': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output of the CreateKeysAndCertificate operation.

        
        

        - **certificateArn** *(string) --* 

          The ARN of the certificate.

          
        

        - **certificateId** *(string) --* 

          The ID of the certificate. AWS IoT issues a default subject name for the certificate (for example, AWS IoT Certificate).

          
        

        - **certificatePem** *(string) --* 

          The certificate data, in PEM format.

          
        

        - **keyPair** *(dict) --* 

          The generated key pair.

          
          

          - **PublicKey** *(string) --* 

            The public key.

            
          

          - **PrivateKey** *(string) --* 

            The private key.

            
      
    

  .. py:method:: create_policy(**kwargs)

    

    Creates an AWS IoT policy.

     

    The created policy is the default version for the policy. This operation creates a policy version with a version identifier of **1** and sets **1** as the policy's default version.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreatePolicy>`_    


    **Request Syntax** 
    ::

      response = client.create_policy(
          policyName='string',
          policyDocument='string'
      )
    :type policyName: string
    :param policyName: **[REQUIRED]** 

      The policy name.

      

    
    :type policyDocument: string
    :param policyDocument: **[REQUIRED]** 

      The JSON document that describes the policy. **policyDocument** must have a minimum length of 1, with a maximum length of 2048, excluding whitespace.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'policyName': 'string',
            'policyArn': 'string',
            'policyDocument': 'string',
            'policyVersionId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the CreatePolicy operation.

        
        

        - **policyName** *(string) --* 

          The policy name.

          
        

        - **policyArn** *(string) --* 

          The policy ARN.

          
        

        - **policyDocument** *(string) --* 

          The JSON document that describes the policy.

          
        

        - **policyVersionId** *(string) --* 

          The policy version ID.

          
    

  .. py:method:: create_policy_version(**kwargs)

    

    Creates a new version of the specified AWS IoT policy. To update a policy, create a new policy version. A managed policy can have up to five versions. If the policy has five versions, you must use  DeletePolicyVersion to delete an existing version before you create a new one.

     

    Optionally, you can set the new version as the policy's default version. The default version is the operative version (that is, the version that is in effect for the certificates to which the policy is attached).

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreatePolicyVersion>`_    


    **Request Syntax** 
    ::

      response = client.create_policy_version(
          policyName='string',
          policyDocument='string',
          setAsDefault=True|False
      )
    :type policyName: string
    :param policyName: **[REQUIRED]** 

      The policy name.

      

    
    :type policyDocument: string
    :param policyDocument: **[REQUIRED]** 

      The JSON document that describes the policy. Minimum length of 1. Maximum length of 2048, excluding whitespace.

      

    
    :type setAsDefault: boolean
    :param setAsDefault: 

      Specifies whether the policy version is set as the default. When this parameter is true, the new policy version becomes the operative version (that is, the version that is in effect for the certificates to which the policy is attached).

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'policyArn': 'string',
            'policyDocument': 'string',
            'policyVersionId': 'string',
            'isDefaultVersion': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output of the CreatePolicyVersion operation.

        
        

        - **policyArn** *(string) --* 

          The policy ARN.

          
        

        - **policyDocument** *(string) --* 

          The JSON document that describes the policy.

          
        

        - **policyVersionId** *(string) --* 

          The policy version ID.

          
        

        - **isDefaultVersion** *(boolean) --* 

          Specifies whether the policy version is the default.

          
    

  .. py:method:: create_role_alias(**kwargs)

    

    Creates a role alias.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateRoleAlias>`_    


    **Request Syntax** 
    ::

      response = client.create_role_alias(
          roleAlias='string',
          roleArn='string',
          credentialDurationSeconds=123
      )
    :type roleAlias: string
    :param roleAlias: **[REQUIRED]** 

      The role alias that points to a role ARN. This allows you to change the role without having to update the device.

      

    
    :type roleArn: string
    :param roleArn: **[REQUIRED]** 

      The role ARN.

      

    
    :type credentialDurationSeconds: integer
    :param credentialDurationSeconds: 

      How long (in seconds) the credentials will be valid.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'roleAlias': 'string',
            'roleAliasArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **roleAlias** *(string) --* 

          The role alias.

          
        

        - **roleAliasArn** *(string) --* 

          The role alias ARN.

          
    

  .. py:method:: create_thing(**kwargs)

    

    Creates a thing record in the thing registry.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateThing>`_    


    **Request Syntax** 
    ::

      response = client.create_thing(
          thingName='string',
          thingTypeName='string',
          attributePayload={
              'attributes': {
                  'string': 'string'
              },
              'merge': True|False
          }
      )
    :type thingName: string
    :param thingName: **[REQUIRED]** 

      The name of the thing to create.

      

    
    :type thingTypeName: string
    :param thingTypeName: 

      The name of the thing type associated with the new thing.

      

    
    :type attributePayload: dict
    :param attributePayload: 

      The attribute payload, which consists of up to three name/value pairs in a JSON document. For example:

       

       ``{\"attributes\":{\"string1\":\"string2\"}}``  

      

    
      - **attributes** *(dict) --* 

        A JSON string containing up to three key-value pair in JSON format. For example:

         

         ``{\"attributes\":{\"string1\":\"string2\"}}``  

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
      - **merge** *(boolean) --* 

        Specifies whether the list of attributes provided in the ``AttributePayload`` is merged with the attributes stored in the registry, instead of overwriting them.

         

        To remove an attribute, call ``UpdateThing`` with an empty attribute value.

         

        .. note::

           

          The ``merge`` attribute is only valid when calling ``UpdateThing`` .

           

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'thingName': 'string',
            'thingArn': 'string',
            'thingId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output of the CreateThing operation.

        
        

        - **thingName** *(string) --* 

          The name of the new thing.

          
        

        - **thingArn** *(string) --* 

          The ARN of the new thing.

          
        

        - **thingId** *(string) --* 

          The thing ID.

          
    

  .. py:method:: create_thing_group(**kwargs)

    

    Create a thing group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateThingGroup>`_    


    **Request Syntax** 
    ::

      response = client.create_thing_group(
          thingGroupName='string',
          parentGroupName='string',
          thingGroupProperties={
              'thingGroupDescription': 'string',
              'attributePayload': {
                  'attributes': {
                      'string': 'string'
                  },
                  'merge': True|False
              }
          }
      )
    :type thingGroupName: string
    :param thingGroupName: **[REQUIRED]** 

      The thing group name to create.

      

    
    :type parentGroupName: string
    :param parentGroupName: 

      The name of the parent thing group.

      

    
    :type thingGroupProperties: dict
    :param thingGroupProperties: 

      The thing group properties.

      

    
      - **thingGroupDescription** *(string) --* 

        The thing group description.

        

      
      - **attributePayload** *(dict) --* 

        The thing group attributes in JSON format.

        

      
        - **attributes** *(dict) --* 

          A JSON string containing up to three key-value pair in JSON format. For example:

           

           ``{\"attributes\":{\"string1\":\"string2\"}}``  

          

        
          - *(string) --* 

          
            - *(string) --* 

            
      
    
        - **merge** *(boolean) --* 

          Specifies whether the list of attributes provided in the ``AttributePayload`` is merged with the attributes stored in the registry, instead of overwriting them.

           

          To remove an attribute, call ``UpdateThing`` with an empty attribute value.

           

          .. note::

             

            The ``merge`` attribute is only valid when calling ``UpdateThing`` .

             

          

        
      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'thingGroupName': 'string',
            'thingGroupArn': 'string',
            'thingGroupId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **thingGroupName** *(string) --* 

          The thing group name.

          
        

        - **thingGroupArn** *(string) --* 

          The thing group ARN.

          
        

        - **thingGroupId** *(string) --* 

          The thing group ID.

          
    

  .. py:method:: create_thing_type(**kwargs)

    

    Creates a new thing type.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateThingType>`_    


    **Request Syntax** 
    ::

      response = client.create_thing_type(
          thingTypeName='string',
          thingTypeProperties={
              'thingTypeDescription': 'string',
              'searchableAttributes': [
                  'string',
              ]
          }
      )
    :type thingTypeName: string
    :param thingTypeName: **[REQUIRED]** 

      The name of the thing type.

      

    
    :type thingTypeProperties: dict
    :param thingTypeProperties: 

      The ThingTypeProperties for the thing type to create. It contains information about the new thing type including a description, and a list of searchable thing attribute names.

      

    
      - **thingTypeDescription** *(string) --* 

        The description of the thing type.

        

      
      - **searchableAttributes** *(list) --* 

        A list of searchable thing attribute names.

        

      
        - *(string) --* 

        
    
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'thingTypeName': 'string',
            'thingTypeArn': 'string',
            'thingTypeId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output of the CreateThingType operation.

        
        

        - **thingTypeName** *(string) --* 

          The name of the thing type.

          
        

        - **thingTypeArn** *(string) --* 

          The Amazon Resource Name (ARN) of the thing type.

          
        

        - **thingTypeId** *(string) --* 

          The thing type ID.

          
    

  .. py:method:: create_topic_rule(**kwargs)

    

    Creates a rule. Creating rules is an administrator-level action. Any user who has permission to create rules will be able to access data processed by the rule.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateTopicRule>`_    


    **Request Syntax** 
    ::

      response = client.create_topic_rule(
          ruleName='string',
          topicRulePayload={
              'sql': 'string',
              'description': 'string',
              'actions': [
                  {
                      'dynamoDB': {
                          'tableName': 'string',
                          'roleArn': 'string',
                          'operation': 'string',
                          'hashKeyField': 'string',
                          'hashKeyValue': 'string',
                          'hashKeyType': 'STRING'|'NUMBER',
                          'rangeKeyField': 'string',
                          'rangeKeyValue': 'string',
                          'rangeKeyType': 'STRING'|'NUMBER',
                          'payloadField': 'string'
                      },
                      'dynamoDBv2': {
                          'roleArn': 'string',
                          'putItem': {
                              'tableName': 'string'
                          }
                      },
                      'lambda': {
                          'functionArn': 'string'
                      },
                      'sns': {
                          'targetArn': 'string',
                          'roleArn': 'string',
                          'messageFormat': 'RAW'|'JSON'
                      },
                      'sqs': {
                          'roleArn': 'string',
                          'queueUrl': 'string',
                          'useBase64': True|False
                      },
                      'kinesis': {
                          'roleArn': 'string',
                          'streamName': 'string',
                          'partitionKey': 'string'
                      },
                      'republish': {
                          'roleArn': 'string',
                          'topic': 'string'
                      },
                      's3': {
                          'roleArn': 'string',
                          'bucketName': 'string',
                          'key': 'string',
                          'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
                      },
                      'firehose': {
                          'roleArn': 'string',
                          'deliveryStreamName': 'string',
                          'separator': 'string'
                      },
                      'cloudwatchMetric': {
                          'roleArn': 'string',
                          'metricNamespace': 'string',
                          'metricName': 'string',
                          'metricValue': 'string',
                          'metricUnit': 'string',
                          'metricTimestamp': 'string'
                      },
                      'cloudwatchAlarm': {
                          'roleArn': 'string',
                          'alarmName': 'string',
                          'stateReason': 'string',
                          'stateValue': 'string'
                      },
                      'elasticsearch': {
                          'roleArn': 'string',
                          'endpoint': 'string',
                          'index': 'string',
                          'type': 'string',
                          'id': 'string'
                      },
                      'salesforce': {
                          'token': 'string',
                          'url': 'string'
                      }
                  },
              ],
              'ruleDisabled': True|False,
              'awsIotSqlVersion': 'string',
              'errorAction': {
                  'dynamoDB': {
                      'tableName': 'string',
                      'roleArn': 'string',
                      'operation': 'string',
                      'hashKeyField': 'string',
                      'hashKeyValue': 'string',
                      'hashKeyType': 'STRING'|'NUMBER',
                      'rangeKeyField': 'string',
                      'rangeKeyValue': 'string',
                      'rangeKeyType': 'STRING'|'NUMBER',
                      'payloadField': 'string'
                  },
                  'dynamoDBv2': {
                      'roleArn': 'string',
                      'putItem': {
                          'tableName': 'string'
                      }
                  },
                  'lambda': {
                      'functionArn': 'string'
                  },
                  'sns': {
                      'targetArn': 'string',
                      'roleArn': 'string',
                      'messageFormat': 'RAW'|'JSON'
                  },
                  'sqs': {
                      'roleArn': 'string',
                      'queueUrl': 'string',
                      'useBase64': True|False
                  },
                  'kinesis': {
                      'roleArn': 'string',
                      'streamName': 'string',
                      'partitionKey': 'string'
                  },
                  'republish': {
                      'roleArn': 'string',
                      'topic': 'string'
                  },
                  's3': {
                      'roleArn': 'string',
                      'bucketName': 'string',
                      'key': 'string',
                      'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
                  },
                  'firehose': {
                      'roleArn': 'string',
                      'deliveryStreamName': 'string',
                      'separator': 'string'
                  },
                  'cloudwatchMetric': {
                      'roleArn': 'string',
                      'metricNamespace': 'string',
                      'metricName': 'string',
                      'metricValue': 'string',
                      'metricUnit': 'string',
                      'metricTimestamp': 'string'
                  },
                  'cloudwatchAlarm': {
                      'roleArn': 'string',
                      'alarmName': 'string',
                      'stateReason': 'string',
                      'stateValue': 'string'
                  },
                  'elasticsearch': {
                      'roleArn': 'string',
                      'endpoint': 'string',
                      'index': 'string',
                      'type': 'string',
                      'id': 'string'
                  },
                  'salesforce': {
                      'token': 'string',
                      'url': 'string'
                  }
              }
          }
      )
    :type ruleName: string
    :param ruleName: **[REQUIRED]** 

      The name of the rule.

      

    
    :type topicRulePayload: dict
    :param topicRulePayload: **[REQUIRED]** 

      The rule payload.

      

    
      - **sql** *(string) --* **[REQUIRED]** 

        The SQL statement used to query the topic. For more information, see `AWS IoT SQL Reference <http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference>`__ in the *AWS IoT Developer Guide* .

        

      
      - **description** *(string) --* 

        The description of the rule.

        

      
      - **actions** *(list) --* **[REQUIRED]** 

        The actions associated with the rule.

        

      
        - *(dict) --* 

          Describes the actions associated with a rule.

          

        
          - **dynamoDB** *(dict) --* 

            Write to a DynamoDB table.

            

          
            - **tableName** *(string) --* **[REQUIRED]** 

              The name of the DynamoDB table.

              

            
            - **roleArn** *(string) --* **[REQUIRED]** 

              The ARN of the IAM role that grants access to the DynamoDB table.

              

            
            - **operation** *(string) --* 

              The type of operation to be performed. This follows the substitution template, so it can be ``${operation}`` , but the substitution must result in one of the following: ``INSERT`` , ``UPDATE`` , or ``DELETE`` .

              

            
            - **hashKeyField** *(string) --* **[REQUIRED]** 

              The hash key name.

              

            
            - **hashKeyValue** *(string) --* **[REQUIRED]** 

              The hash key value.

              

            
            - **hashKeyType** *(string) --* 

              The hash key type. Valid values are "STRING" or "NUMBER"

              

            
            - **rangeKeyField** *(string) --* 

              The range key name.

              

            
            - **rangeKeyValue** *(string) --* 

              The range key value.

              

            
            - **rangeKeyType** *(string) --* 

              The range key type. Valid values are "STRING" or "NUMBER"

              

            
            - **payloadField** *(string) --* 

              The action payload. This name can be customized.

              

            
          
          - **dynamoDBv2** *(dict) --* 

            Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.

            

          
            - **roleArn** *(string) --* 

              The ARN of the IAM role that grants access to the DynamoDB table.

              

            
            - **putItem** *(dict) --* 

              Specifies the DynamoDB table to which the message data will be written. For example:

               

               ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName": "my-table" } } }``  

               

              Each attribute in the message payload will be written to a separate column in the DynamoDB database.

              

            
              - **tableName** *(string) --* **[REQUIRED]** 

                The table where the message data will be written

                

              
            
          
          - **lambda** *(dict) --* 

            Invoke a Lambda function.

            

          
            - **functionArn** *(string) --* **[REQUIRED]** 

              The ARN of the Lambda function.

              

            
          
          - **sns** *(dict) --* 

            Publish to an Amazon SNS topic.

            

          
            - **targetArn** *(string) --* **[REQUIRED]** 

              The ARN of the SNS topic.

              

            
            - **roleArn** *(string) --* **[REQUIRED]** 

              The ARN of the IAM role that grants access.

              

            
            - **messageFormat** *(string) --* 

              The message format of the message to publish. Optional. Accepted values are "JSON" and "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see `http\://docs.aws.amazon.com/sns/latest/dg/json-formats.html <http://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their official documentation.

              

            
          
          - **sqs** *(dict) --* 

            Publish to an Amazon SQS queue.

            

          
            - **roleArn** *(string) --* **[REQUIRED]** 

              The ARN of the IAM role that grants access.

              

            
            - **queueUrl** *(string) --* **[REQUIRED]** 

              The URL of the Amazon SQS queue.

              

            
            - **useBase64** *(boolean) --* 

              Specifies whether to use Base64 encoding.

              

            
          
          - **kinesis** *(dict) --* 

            Write data to an Amazon Kinesis stream.

            

          
            - **roleArn** *(string) --* **[REQUIRED]** 

              The ARN of the IAM role that grants access to the Amazon Kinesis stream.

              

            
            - **streamName** *(string) --* **[REQUIRED]** 

              The name of the Amazon Kinesis stream.

              

            
            - **partitionKey** *(string) --* 

              The partition key.

              

            
          
          - **republish** *(dict) --* 

            Publish to another MQTT topic.

            

          
            - **roleArn** *(string) --* **[REQUIRED]** 

              The ARN of the IAM role that grants access.

              

            
            - **topic** *(string) --* **[REQUIRED]** 

              The name of the MQTT topic.

              

            
          
          - **s3** *(dict) --* 

            Write to an Amazon S3 bucket.

            

          
            - **roleArn** *(string) --* **[REQUIRED]** 

              The ARN of the IAM role that grants access.

              

            
            - **bucketName** *(string) --* **[REQUIRED]** 

              The Amazon S3 bucket.

              

            
            - **key** *(string) --* **[REQUIRED]** 

              The object key.

              

            
            - **cannedAcl** *(string) --* 

              The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see `S3 canned ACLs <http://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .

              

            
          
          - **firehose** *(dict) --* 

            Write to an Amazon Kinesis Firehose stream.

            

          
            - **roleArn** *(string) --* **[REQUIRED]** 

              The IAM role that grants access to the Amazon Kinesis Firehose stream.

              

            
            - **deliveryStreamName** *(string) --* **[REQUIRED]** 

              The delivery stream name.

              

            
            - **separator** *(string) --* 

              A character separator that will be used to separate records written to the Firehose stream. Valid values are: '\n' (newline), '\t' (tab), '\r\n' (Windows newline), ',' (comma).

              

            
          
          - **cloudwatchMetric** *(dict) --* 

            Capture a CloudWatch metric.

            

          
            - **roleArn** *(string) --* **[REQUIRED]** 

              The IAM role that allows access to the CloudWatch metric.

              

            
            - **metricNamespace** *(string) --* **[REQUIRED]** 

              The CloudWatch metric namespace name.

              

            
            - **metricName** *(string) --* **[REQUIRED]** 

              The CloudWatch metric name.

              

            
            - **metricValue** *(string) --* **[REQUIRED]** 

              The CloudWatch metric value.

              

            
            - **metricUnit** *(string) --* **[REQUIRED]** 

              The `metric unit <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__ supported by CloudWatch.

              

            
            - **metricTimestamp** *(string) --* 

              An optional `Unix timestamp <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__ .

              

            
          
          - **cloudwatchAlarm** *(dict) --* 

            Change the state of a CloudWatch alarm.

            

          
            - **roleArn** *(string) --* **[REQUIRED]** 

              The IAM role that allows access to the CloudWatch alarm.

              

            
            - **alarmName** *(string) --* **[REQUIRED]** 

              The CloudWatch alarm name.

              

            
            - **stateReason** *(string) --* **[REQUIRED]** 

              The reason for the alarm change.

              

            
            - **stateValue** *(string) --* **[REQUIRED]** 

              The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

              

            
          
          - **elasticsearch** *(dict) --* 

            Write data to an Amazon Elasticsearch Service domain.

            

          
            - **roleArn** *(string) --* **[REQUIRED]** 

              The IAM role ARN that has access to Elasticsearch.

              

            
            - **endpoint** *(string) --* **[REQUIRED]** 

              The endpoint of your Elasticsearch domain.

              

            
            - **index** *(string) --* **[REQUIRED]** 

              The Elasticsearch index where you want to store your data.

              

            
            - **type** *(string) --* **[REQUIRED]** 

              The type of document you are storing.

              

            
            - **id** *(string) --* **[REQUIRED]** 

              The unique identifier for the document you are storing.

              

            
          
          - **salesforce** *(dict) --* 

            Send a message to a Salesforce IoT Cloud Input Stream.

            

          
            - **token** *(string) --* **[REQUIRED]** 

              The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

              

            
            - **url** *(string) --* **[REQUIRED]** 

              The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

              

            
          
        
    
      - **ruleDisabled** *(boolean) --* 

        Specifies whether the rule is disabled.

        

      
      - **awsIotSqlVersion** *(string) --* 

        The version of the SQL rules engine to use when evaluating the rule.

        

      
      - **errorAction** *(dict) --* 

        The action to take when an error occurs.

        

      
        - **dynamoDB** *(dict) --* 

          Write to a DynamoDB table.

          

        
          - **tableName** *(string) --* **[REQUIRED]** 

            The name of the DynamoDB table.

            

          
          - **roleArn** *(string) --* **[REQUIRED]** 

            The ARN of the IAM role that grants access to the DynamoDB table.

            

          
          - **operation** *(string) --* 

            The type of operation to be performed. This follows the substitution template, so it can be ``${operation}`` , but the substitution must result in one of the following: ``INSERT`` , ``UPDATE`` , or ``DELETE`` .

            

          
          - **hashKeyField** *(string) --* **[REQUIRED]** 

            The hash key name.

            

          
          - **hashKeyValue** *(string) --* **[REQUIRED]** 

            The hash key value.

            

          
          - **hashKeyType** *(string) --* 

            The hash key type. Valid values are "STRING" or "NUMBER"

            

          
          - **rangeKeyField** *(string) --* 

            The range key name.

            

          
          - **rangeKeyValue** *(string) --* 

            The range key value.

            

          
          - **rangeKeyType** *(string) --* 

            The range key type. Valid values are "STRING" or "NUMBER"

            

          
          - **payloadField** *(string) --* 

            The action payload. This name can be customized.

            

          
        
        - **dynamoDBv2** *(dict) --* 

          Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.

          

        
          - **roleArn** *(string) --* 

            The ARN of the IAM role that grants access to the DynamoDB table.

            

          
          - **putItem** *(dict) --* 

            Specifies the DynamoDB table to which the message data will be written. For example:

             

             ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName": "my-table" } } }``  

             

            Each attribute in the message payload will be written to a separate column in the DynamoDB database.

            

          
            - **tableName** *(string) --* **[REQUIRED]** 

              The table where the message data will be written

              

            
          
        
        - **lambda** *(dict) --* 

          Invoke a Lambda function.

          

        
          - **functionArn** *(string) --* **[REQUIRED]** 

            The ARN of the Lambda function.

            

          
        
        - **sns** *(dict) --* 

          Publish to an Amazon SNS topic.

          

        
          - **targetArn** *(string) --* **[REQUIRED]** 

            The ARN of the SNS topic.

            

          
          - **roleArn** *(string) --* **[REQUIRED]** 

            The ARN of the IAM role that grants access.

            

          
          - **messageFormat** *(string) --* 

            The message format of the message to publish. Optional. Accepted values are "JSON" and "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see `http\://docs.aws.amazon.com/sns/latest/dg/json-formats.html <http://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their official documentation.

            

          
        
        - **sqs** *(dict) --* 

          Publish to an Amazon SQS queue.

          

        
          - **roleArn** *(string) --* **[REQUIRED]** 

            The ARN of the IAM role that grants access.

            

          
          - **queueUrl** *(string) --* **[REQUIRED]** 

            The URL of the Amazon SQS queue.

            

          
          - **useBase64** *(boolean) --* 

            Specifies whether to use Base64 encoding.

            

          
        
        - **kinesis** *(dict) --* 

          Write data to an Amazon Kinesis stream.

          

        
          - **roleArn** *(string) --* **[REQUIRED]** 

            The ARN of the IAM role that grants access to the Amazon Kinesis stream.

            

          
          - **streamName** *(string) --* **[REQUIRED]** 

            The name of the Amazon Kinesis stream.

            

          
          - **partitionKey** *(string) --* 

            The partition key.

            

          
        
        - **republish** *(dict) --* 

          Publish to another MQTT topic.

          

        
          - **roleArn** *(string) --* **[REQUIRED]** 

            The ARN of the IAM role that grants access.

            

          
          - **topic** *(string) --* **[REQUIRED]** 

            The name of the MQTT topic.

            

          
        
        - **s3** *(dict) --* 

          Write to an Amazon S3 bucket.

          

        
          - **roleArn** *(string) --* **[REQUIRED]** 

            The ARN of the IAM role that grants access.

            

          
          - **bucketName** *(string) --* **[REQUIRED]** 

            The Amazon S3 bucket.

            

          
          - **key** *(string) --* **[REQUIRED]** 

            The object key.

            

          
          - **cannedAcl** *(string) --* 

            The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see `S3 canned ACLs <http://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .

            

          
        
        - **firehose** *(dict) --* 

          Write to an Amazon Kinesis Firehose stream.

          

        
          - **roleArn** *(string) --* **[REQUIRED]** 

            The IAM role that grants access to the Amazon Kinesis Firehose stream.

            

          
          - **deliveryStreamName** *(string) --* **[REQUIRED]** 

            The delivery stream name.

            

          
          - **separator** *(string) --* 

            A character separator that will be used to separate records written to the Firehose stream. Valid values are: '\n' (newline), '\t' (tab), '\r\n' (Windows newline), ',' (comma).

            

          
        
        - **cloudwatchMetric** *(dict) --* 

          Capture a CloudWatch metric.

          

        
          - **roleArn** *(string) --* **[REQUIRED]** 

            The IAM role that allows access to the CloudWatch metric.

            

          
          - **metricNamespace** *(string) --* **[REQUIRED]** 

            The CloudWatch metric namespace name.

            

          
          - **metricName** *(string) --* **[REQUIRED]** 

            The CloudWatch metric name.

            

          
          - **metricValue** *(string) --* **[REQUIRED]** 

            The CloudWatch metric value.

            

          
          - **metricUnit** *(string) --* **[REQUIRED]** 

            The `metric unit <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__ supported by CloudWatch.

            

          
          - **metricTimestamp** *(string) --* 

            An optional `Unix timestamp <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__ .

            

          
        
        - **cloudwatchAlarm** *(dict) --* 

          Change the state of a CloudWatch alarm.

          

        
          - **roleArn** *(string) --* **[REQUIRED]** 

            The IAM role that allows access to the CloudWatch alarm.

            

          
          - **alarmName** *(string) --* **[REQUIRED]** 

            The CloudWatch alarm name.

            

          
          - **stateReason** *(string) --* **[REQUIRED]** 

            The reason for the alarm change.

            

          
          - **stateValue** *(string) --* **[REQUIRED]** 

            The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

            

          
        
        - **elasticsearch** *(dict) --* 

          Write data to an Amazon Elasticsearch Service domain.

          

        
          - **roleArn** *(string) --* **[REQUIRED]** 

            The IAM role ARN that has access to Elasticsearch.

            

          
          - **endpoint** *(string) --* **[REQUIRED]** 

            The endpoint of your Elasticsearch domain.

            

          
          - **index** *(string) --* **[REQUIRED]** 

            The Elasticsearch index where you want to store your data.

            

          
          - **type** *(string) --* **[REQUIRED]** 

            The type of document you are storing.

            

          
          - **id** *(string) --* **[REQUIRED]** 

            The unique identifier for the document you are storing.

            

          
        
        - **salesforce** *(dict) --* 

          Send a message to a Salesforce IoT Cloud Input Stream.

          

        
          - **token** *(string) --* **[REQUIRED]** 

            The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

            

          
          - **url** *(string) --* **[REQUIRED]** 

            The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

            

          
        
      
    
    
    :returns: None

  .. py:method:: delete_authorizer(**kwargs)

    

    Deletes an authorizer.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteAuthorizer>`_    


    **Request Syntax** 
    ::

      response = client.delete_authorizer(
          authorizerName='string'
      )
    :type authorizerName: string
    :param authorizerName: **[REQUIRED]** 

      The name of the authorizer to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_ca_certificate(**kwargs)

    

    Deletes a registered CA certificate.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteCACertificate>`_    


    **Request Syntax** 
    ::

      response = client.delete_ca_certificate(
          certificateId='string'
      )
    :type certificateId: string
    :param certificateId: **[REQUIRED]** 

      The ID of the certificate to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        The output for the DeleteCACertificate operation.

        
    

  .. py:method:: delete_certificate(**kwargs)

    

    Deletes the specified certificate.

     

    A certificate cannot be deleted if it has a policy attached to it or if its status is set to ACTIVE. To delete a certificate, first use the  DetachPrincipalPolicy API to detach all policies. Next, use the  UpdateCertificate API to set the certificate to the INACTIVE status.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteCertificate>`_    


    **Request Syntax** 
    ::

      response = client.delete_certificate(
          certificateId='string',
          forceDelete=True|False
      )
    :type certificateId: string
    :param certificateId: **[REQUIRED]** 

      The ID of the certificate.

      

    
    :type forceDelete: boolean
    :param forceDelete: 

      Forces a certificate request to be deleted.

      

    
    
    :returns: None

  .. py:method:: delete_policy(**kwargs)

    

    Deletes the specified policy.

     

    A policy cannot be deleted if it has non-default versions or it is attached to any certificate.

     

    To delete a policy, use the DeletePolicyVersion API to delete all non-default versions of the policy; use the DetachPrincipalPolicy API to detach the policy from any certificate; and then use the DeletePolicy API to delete the policy.

     

    When a policy is deleted using DeletePolicy, its default version is deleted with it.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeletePolicy>`_    


    **Request Syntax** 
    ::

      response = client.delete_policy(
          policyName='string'
      )
    :type policyName: string
    :param policyName: **[REQUIRED]** 

      The name of the policy to delete.

      

    
    
    :returns: None

  .. py:method:: delete_policy_version(**kwargs)

    

    Deletes the specified version of the specified policy. You cannot delete the default version of a policy using this API. To delete the default version of a policy, use  DeletePolicy . To find out which version of a policy is marked as the default version, use ListPolicyVersions.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeletePolicyVersion>`_    


    **Request Syntax** 
    ::

      response = client.delete_policy_version(
          policyName='string',
          policyVersionId='string'
      )
    :type policyName: string
    :param policyName: **[REQUIRED]** 

      The name of the policy.

      

    
    :type policyVersionId: string
    :param policyVersionId: **[REQUIRED]** 

      The policy version ID.

      

    
    
    :returns: None

  .. py:method:: delete_registration_code()

    

    Deletes a CA certificate registration code.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteRegistrationCode>`_    


    **Request Syntax** 
    ::

      response = client.delete_registration_code()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        The output for the DeleteRegistrationCode operation.

        
    

  .. py:method:: delete_role_alias(**kwargs)

    

    Deletes a role alias

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteRoleAlias>`_    


    **Request Syntax** 
    ::

      response = client.delete_role_alias(
          roleAlias='string'
      )
    :type roleAlias: string
    :param roleAlias: **[REQUIRED]** 

      The role alias to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_thing(**kwargs)

    

    Deletes the specified thing.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteThing>`_    


    **Request Syntax** 
    ::

      response = client.delete_thing(
          thingName='string',
          expectedVersion=123
      )
    :type thingName: string
    :param thingName: **[REQUIRED]** 

      The name of the thing to delete.

      

    
    :type expectedVersion: integer
    :param expectedVersion: 

      The expected version of the thing record in the registry. If the version of the record in the registry does not match the expected version specified in the request, the ``DeleteThing`` request is rejected with a ``VersionConflictException`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        The output of the DeleteThing operation.

        
    

  .. py:method:: delete_thing_group(**kwargs)

    

    Deletes a thing group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteThingGroup>`_    


    **Request Syntax** 
    ::

      response = client.delete_thing_group(
          thingGroupName='string',
          expectedVersion=123
      )
    :type thingGroupName: string
    :param thingGroupName: **[REQUIRED]** 

      The name of the thing group to delete.

      

    
    :type expectedVersion: integer
    :param expectedVersion: 

      The expected version of the thing group to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_thing_type(**kwargs)

    

    Deletes the specified thing type . You cannot delete a thing type if it has things associated with it. To delete a thing type, first mark it as deprecated by calling  DeprecateThingType , then remove any associated things by calling  UpdateThing to change the thing type on any associated thing, and finally use  DeleteThingType to delete the thing type.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteThingType>`_    


    **Request Syntax** 
    ::

      response = client.delete_thing_type(
          thingTypeName='string'
      )
    :type thingTypeName: string
    :param thingTypeName: **[REQUIRED]** 

      The name of the thing type.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        The output for the DeleteThingType operation.

        
    

  .. py:method:: delete_topic_rule(**kwargs)

    

    Deletes the rule.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteTopicRule>`_    


    **Request Syntax** 
    ::

      response = client.delete_topic_rule(
          ruleName='string'
      )
    :type ruleName: string
    :param ruleName: **[REQUIRED]** 

      The name of the rule.

      

    
    
    :returns: None

  .. py:method:: delete_v2_logging_level(**kwargs)

    

    Deletes a logging level.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteV2LoggingLevel>`_    


    **Request Syntax** 
    ::

      response = client.delete_v2_logging_level(
          targetType='DEFAULT'|'THING_GROUP',
          targetName='string'
      )
    :type targetType: string
    :param targetType: **[REQUIRED]** 

      The type of resource for which you are configuring logging. Must be ``THING_Group`` .

      

    
    :type targetName: string
    :param targetName: **[REQUIRED]** 

      The name of the resource for which you are configuring logging.

      

    
    
    :returns: None

  .. py:method:: deprecate_thing_type(**kwargs)

    

    Deprecates a thing type. You can not associate new things with deprecated thing type.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeprecateThingType>`_    


    **Request Syntax** 
    ::

      response = client.deprecate_thing_type(
          thingTypeName='string',
          undoDeprecate=True|False
      )
    :type thingTypeName: string
    :param thingTypeName: **[REQUIRED]** 

      The name of the thing type to deprecate.

      

    
    :type undoDeprecate: boolean
    :param undoDeprecate: 

      Whether to undeprecate a deprecated thing type. If **true** , the thing type will not be deprecated anymore and you can associate it with things.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        The output for the DeprecateThingType operation.

        
    

  .. py:method:: describe_authorizer(**kwargs)

    

    Describes an authorizer.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeAuthorizer>`_    


    **Request Syntax** 
    ::

      response = client.describe_authorizer(
          authorizerName='string'
      )
    :type authorizerName: string
    :param authorizerName: **[REQUIRED]** 

      The name of the authorizer to describe.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'authorizerDescription': {
                'authorizerName': 'string',
                'authorizerArn': 'string',
                'authorizerFunctionArn': 'string',
                'tokenKeyName': 'string',
                'tokenSigningPublicKeys': {
                    'string': 'string'
                },
                'status': 'ACTIVE'|'INACTIVE',
                'creationDate': datetime(2015, 1, 1),
                'lastModifiedDate': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **authorizerDescription** *(dict) --* 

          The authorizer description.

          
          

          - **authorizerName** *(string) --* 

            The authorizer name.

            
          

          - **authorizerArn** *(string) --* 

            The authorizer ARN.

            
          

          - **authorizerFunctionArn** *(string) --* 

            The authorizer's Lambda function ARN.

            
          

          - **tokenKeyName** *(string) --* 

            The key used to extract the token from the HTTP headers.

            
          

          - **tokenSigningPublicKeys** *(dict) --* 

            The public keys used to validate the token signature returned by your custom authentication service.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **status** *(string) --* 

            The status of the authorizer.

            
          

          - **creationDate** *(datetime) --* 

            The UNIX timestamp of when the authorizer was created.

            
          

          - **lastModifiedDate** *(datetime) --* 

            The UNIX timestamp of when the authorizer was last updated.

            
      
    

  .. py:method:: describe_ca_certificate(**kwargs)

    

    Describes a registered CA certificate.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeCACertificate>`_    


    **Request Syntax** 
    ::

      response = client.describe_ca_certificate(
          certificateId='string'
      )
    :type certificateId: string
    :param certificateId: **[REQUIRED]** 

      The CA certificate identifier.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'certificateDescription': {
                'certificateArn': 'string',
                'certificateId': 'string',
                'status': 'ACTIVE'|'INACTIVE',
                'certificatePem': 'string',
                'ownedBy': 'string',
                'creationDate': datetime(2015, 1, 1),
                'autoRegistrationStatus': 'ENABLE'|'DISABLE'
            },
            'registrationConfig': {
                'templateBody': 'string',
                'roleArn': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the DescribeCACertificate operation.

        
        

        - **certificateDescription** *(dict) --* 

          The CA certificate description.

          
          

          - **certificateArn** *(string) --* 

            The CA certificate ARN.

            
          

          - **certificateId** *(string) --* 

            The CA certificate ID.

            
          

          - **status** *(string) --* 

            The status of a CA certificate.

            
          

          - **certificatePem** *(string) --* 

            The CA certificate data, in PEM format.

            
          

          - **ownedBy** *(string) --* 

            The owner of the CA certificate.

            
          

          - **creationDate** *(datetime) --* 

            The date the CA certificate was created.

            
          

          - **autoRegistrationStatus** *(string) --* 

            Whether the CA certificate configured for auto registration of device certificates. Valid values are "ENABLE" and "DISABLE"

            
      
        

        - **registrationConfig** *(dict) --* 

          Information about the registration configuration.

          
          

          - **templateBody** *(string) --* 

            The template body.

            
          

          - **roleArn** *(string) --* 

            The ARN of the role.

            
      
    

  .. py:method:: describe_certificate(**kwargs)

    

    Gets information about the specified certificate.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeCertificate>`_    


    **Request Syntax** 
    ::

      response = client.describe_certificate(
          certificateId='string'
      )
    :type certificateId: string
    :param certificateId: **[REQUIRED]** 

      The ID of the certificate.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'certificateDescription': {
                'certificateArn': 'string',
                'certificateId': 'string',
                'caCertificateId': 'string',
                'status': 'ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION',
                'certificatePem': 'string',
                'ownedBy': 'string',
                'previousOwnedBy': 'string',
                'creationDate': datetime(2015, 1, 1),
                'lastModifiedDate': datetime(2015, 1, 1),
                'transferData': {
                    'transferMessage': 'string',
                    'rejectReason': 'string',
                    'transferDate': datetime(2015, 1, 1),
                    'acceptDate': datetime(2015, 1, 1),
                    'rejectDate': datetime(2015, 1, 1)
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output of the DescribeCertificate operation.

        
        

        - **certificateDescription** *(dict) --* 

          The description of the certificate.

          
          

          - **certificateArn** *(string) --* 

            The ARN of the certificate.

            
          

          - **certificateId** *(string) --* 

            The ID of the certificate.

            
          

          - **caCertificateId** *(string) --* 

            The certificate ID of the CA certificate used to sign this certificate.

            
          

          - **status** *(string) --* 

            The status of the certificate.

            
          

          - **certificatePem** *(string) --* 

            The certificate data, in PEM format.

            
          

          - **ownedBy** *(string) --* 

            The ID of the AWS account that owns the certificate.

            
          

          - **previousOwnedBy** *(string) --* 

            The ID of the AWS account of the previous owner of the certificate.

            
          

          - **creationDate** *(datetime) --* 

            The date and time the certificate was created.

            
          

          - **lastModifiedDate** *(datetime) --* 

            The date and time the certificate was last modified.

            
          

          - **transferData** *(dict) --* 

            The transfer data.

            
            

            - **transferMessage** *(string) --* 

              The transfer message.

              
            

            - **rejectReason** *(string) --* 

              The reason why the transfer was rejected.

              
            

            - **transferDate** *(datetime) --* 

              The date the transfer took place.

              
            

            - **acceptDate** *(datetime) --* 

              The date the transfer was accepted.

              
            

            - **rejectDate** *(datetime) --* 

              The date the transfer was rejected.

              
        
      
    

  .. py:method:: describe_default_authorizer()

    

    Describes the default authorizer.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeDefaultAuthorizer>`_    


    **Request Syntax** 
    ::

      response = client.describe_default_authorizer()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'authorizerDescription': {
                'authorizerName': 'string',
                'authorizerArn': 'string',
                'authorizerFunctionArn': 'string',
                'tokenKeyName': 'string',
                'tokenSigningPublicKeys': {
                    'string': 'string'
                },
                'status': 'ACTIVE'|'INACTIVE',
                'creationDate': datetime(2015, 1, 1),
                'lastModifiedDate': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **authorizerDescription** *(dict) --* 

          The default authorizer's description.

          
          

          - **authorizerName** *(string) --* 

            The authorizer name.

            
          

          - **authorizerArn** *(string) --* 

            The authorizer ARN.

            
          

          - **authorizerFunctionArn** *(string) --* 

            The authorizer's Lambda function ARN.

            
          

          - **tokenKeyName** *(string) --* 

            The key used to extract the token from the HTTP headers.

            
          

          - **tokenSigningPublicKeys** *(dict) --* 

            The public keys used to validate the token signature returned by your custom authentication service.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
          

          - **status** *(string) --* 

            The status of the authorizer.

            
          

          - **creationDate** *(datetime) --* 

            The UNIX timestamp of when the authorizer was created.

            
          

          - **lastModifiedDate** *(datetime) --* 

            The UNIX timestamp of when the authorizer was last updated.

            
      
    

  .. py:method:: describe_endpoint(**kwargs)

    

    Returns a unique endpoint specific to the AWS account making the call.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeEndpoint>`_    


    **Request Syntax** 
    ::

      response = client.describe_endpoint(
          endpointType='string'
      )
    :type endpointType: string
    :param endpointType: 

      The endpoint type.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'endpointAddress': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the DescribeEndpoint operation.

        
        

        - **endpointAddress** *(string) --* 

          The endpoint. The format of the endpoint is as follows: *identifier* .iot.*region* .amazonaws.com.

          
    

  .. py:method:: describe_event_configurations()

    

    Describes event configurations.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeEventConfigurations>`_    


    **Request Syntax** 
    ::

      response = client.describe_event_configurations()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'eventConfigurations': {
                'string': {
                    'Enabled': True|False
                }
            },
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedDate': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **eventConfigurations** *(dict) --* 

          The event configurations.

          
          

          - *(string) --* 
            

            - *(dict) --* 

              Configuration.

              
              

              - **Enabled** *(boolean) --* 

                True to enable the configuration.

                
          
      
    
        

        - **creationDate** *(datetime) --* 

          The creation date of the event configuration.

          
        

        - **lastModifiedDate** *(datetime) --* 

          The date the event configurations were last modified.

          
    

  .. py:method:: describe_index(**kwargs)

    

    Describes a search index.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeIndex>`_    


    **Request Syntax** 
    ::

      response = client.describe_index(
          indexName='string'
      )
    :type indexName: string
    :param indexName: **[REQUIRED]** 

      The index name.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'indexName': 'string',
            'indexStatus': 'ACTIVE'|'BUILDING'|'REBUILDING',
            'schema': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **indexName** *(string) --* 

          The index name.

          
        

        - **indexStatus** *(string) --* 

          The index status.

          
        

        - **schema** *(string) --* 

          Contains a value that specifies the type of indexing performed. Valid values are:

           

           
          * REGISTRY – Your thing index will contain only registry data. 
           
          * REGISTRY_AND_SHADOW - Your thing index will contain registry and shadow data. 
           

          
    

  .. py:method:: describe_job(**kwargs)

    

    Describes a job.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeJob>`_    


    **Request Syntax** 
    ::

      response = client.describe_job(
          jobId='string'
      )
    :type jobId: string
    :param jobId: **[REQUIRED]** 

      The unique identifier you assigned to this job when it was created.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'documentSource': 'string',
            'job': {
                'jobArn': 'string',
                'jobId': 'string',
                'targetSelection': 'CONTINUOUS'|'SNAPSHOT',
                'status': 'IN_PROGRESS'|'CANCELED'|'COMPLETED',
                'comment': 'string',
                'targets': [
                    'string',
                ],
                'description': 'string',
                'presignedUrlConfig': {
                    'roleArn': 'string',
                    'expiresInSec': 123
                },
                'jobExecutionsRolloutConfig': {
                    'maximumPerMinute': 123
                },
                'createdAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'completedAt': datetime(2015, 1, 1),
                'jobProcessDetails': {
                    'processingTargets': [
                        'string',
                    ],
                    'numberOfCanceledThings': 123,
                    'numberOfSucceededThings': 123,
                    'numberOfFailedThings': 123,
                    'numberOfRejectedThings': 123,
                    'numberOfQueuedThings': 123,
                    'numberOfInProgressThings': 123,
                    'numberOfRemovedThings': 123
                },
                'documentParameters': {
                    'string': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **documentSource** *(string) --* 

          An S3 link to the job document.

          
        

        - **job** *(dict) --* 

          Information about the job.

          
          

          - **jobArn** *(string) --* 

            An ARN identifying the job with format "arn:aws:iot:region:account:job/jobId".

            
          

          - **jobId** *(string) --* 

            The unique identifier you assigned to this job when it was created.

            
          

          - **targetSelection** *(string) --* 

            Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a device when the thing representing the device is added to a target group, even after the job was completed by all things originally in the group. 

            
          

          - **status** *(string) --* 

            The status of the job, one of ``IN_PROGRESS`` , ``CANCELED`` , or ``COMPLETED`` . 

            
          

          - **comment** *(string) --* 

            If the job was updated, describes the reason for the update.

            
          

          - **targets** *(list) --* 

            A list of IoT things and thing groups to which the job should be sent.

            
            

            - *(string) --* 
        
          

          - **description** *(string) --* 

            A short text description of the job.

            
          

          - **presignedUrlConfig** *(dict) --* 

            Configuration for pre-signed S3 URLs.

            
            

            - **roleArn** *(string) --* 

              The ARN of an IAM role that grants grants permission to download files from the S3 bucket where the job data/updates are stored. The role must also grant permission for IoT to download the files.

              
            

            - **expiresInSec** *(integer) --* 

              How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default value is 3600 seconds. Pre-signed URLs are generated when Jobs receives an MQTT request for the job document.

              
        
          

          - **jobExecutionsRolloutConfig** *(dict) --* 

            Allows you to create a staged rollout of a job.

            
            

            - **maximumPerMinute** *(integer) --* 

              The maximum number of things that will be notified of a pending job, per minute. This parameter allows you to create a staged rollout.

              
        
          

          - **createdAt** *(datetime) --* 

            The time, in milliseconds since the epoch, when the job was created.

            
          

          - **lastUpdatedAt** *(datetime) --* 

            The time, in milliseconds since the epoch, when the job was last updated.

            
          

          - **completedAt** *(datetime) --* 

            The time, in milliseconds since the epoch, when the job was completed.

            
          

          - **jobProcessDetails** *(dict) --* 

            Details about the job process.

            
            

            - **processingTargets** *(list) --* 

              The devices on which the job is executing.

              
              

              - *(string) --* 
          
            

            - **numberOfCanceledThings** *(integer) --* 

              The number of things that cancelled the job.

              
            

            - **numberOfSucceededThings** *(integer) --* 

              The number of things which successfully completed the job.

              
            

            - **numberOfFailedThings** *(integer) --* 

              The number of things that failed executing the job.

              
            

            - **numberOfRejectedThings** *(integer) --* 

              The number of things that rejected the job.

              
            

            - **numberOfQueuedThings** *(integer) --* 

              The number of things that are awaiting execution of the job.

              
            

            - **numberOfInProgressThings** *(integer) --* 

              The number of things currently executing the job.

              
            

            - **numberOfRemovedThings** *(integer) --* 

              The number of things that are no longer scheduled to execute the job because they have been deleted or have been removed from the group that was a target of the job.

              
        
          

          - **documentParameters** *(dict) --* 

            The parameters specified for the job document.

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
      
    

  .. py:method:: describe_job_execution(**kwargs)

    

    Describes a job execution.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeJobExecution>`_    


    **Request Syntax** 
    ::

      response = client.describe_job_execution(
          jobId='string',
          thingName='string',
          executionNumber=123
      )
    :type jobId: string
    :param jobId: **[REQUIRED]** 

      The unique identifier you assigned to this job when it was created.

      

    
    :type thingName: string
    :param thingName: **[REQUIRED]** 

      The name of the thing on which the job execution is running.

      

    
    :type executionNumber: integer
    :param executionNumber: 

      A string (consisting of the digits "0" through "9" which is used to specify a particular job execution on a particular device.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'execution': {
                'jobId': 'string',
                'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'REJECTED'|'REMOVED'|'CANCELED',
                'statusDetails': {
                    'detailsMap': {
                        'string': 'string'
                    }
                },
                'thingArn': 'string',
                'queuedAt': datetime(2015, 1, 1),
                'startedAt': datetime(2015, 1, 1),
                'lastUpdatedAt': datetime(2015, 1, 1),
                'executionNumber': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **execution** *(dict) --* 

          Information about the job execution.

          
          

          - **jobId** *(string) --* 

            The unique identifier you assigned to the job when it was created.

            
          

          - **status** *(string) --* 

            The status of the job execution (IN_PROGRESS, QUEUED, FAILED, SUCCESS, CANCELED, or REJECTED).

            
          

          - **statusDetails** *(dict) --* 

            A collection of name/value pairs that describe the status of the job execution.

            
            

            - **detailsMap** *(dict) --* 

              The job execution status.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
        
          

          - **thingArn** *(string) --* 

            The ARN of the thing on which the job execution is running.

            
          

          - **queuedAt** *(datetime) --* 

            The time, in milliseconds since the epoch, when the job execution was queued.

            
          

          - **startedAt** *(datetime) --* 

            The time, in milliseconds since the epoch, when the job execution started.

            
          

          - **lastUpdatedAt** *(datetime) --* 

            The time, in milliseconds since the epoch, when the job execution was last updated.

            
          

          - **executionNumber** *(integer) --* 

            A string (consisting of the digits "0" through "9") which identifies this particular job execution on this particular device. It can be used in commands which return or update job execution information. 

            
      
    

  .. py:method:: describe_role_alias(**kwargs)

    

    Describes a role alias.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeRoleAlias>`_    


    **Request Syntax** 
    ::

      response = client.describe_role_alias(
          roleAlias='string'
      )
    :type roleAlias: string
    :param roleAlias: **[REQUIRED]** 

      The role alias to describe.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'roleAliasDescription': {
                'roleAlias': 'string',
                'roleArn': 'string',
                'owner': 'string',
                'credentialDurationSeconds': 123,
                'creationDate': datetime(2015, 1, 1),
                'lastModifiedDate': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **roleAliasDescription** *(dict) --* 

          The role alias description.

          
          

          - **roleAlias** *(string) --* 

            The role alias.

            
          

          - **roleArn** *(string) --* 

            The role ARN.

            
          

          - **owner** *(string) --* 

            The role alias owner.

            
          

          - **credentialDurationSeconds** *(integer) --* 

            The number of seconds for which the credential is valid.

            
          

          - **creationDate** *(datetime) --* 

            The UNIX timestamp of when the role alias was created.

            
          

          - **lastModifiedDate** *(datetime) --* 

            The UNIX timestamp of when the role alias was last modified.

            
      
    

  .. py:method:: describe_thing(**kwargs)

    

    Gets information about the specified thing.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeThing>`_    


    **Request Syntax** 
    ::

      response = client.describe_thing(
          thingName='string'
      )
    :type thingName: string
    :param thingName: **[REQUIRED]** 

      The name of the thing.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'defaultClientId': 'string',
            'thingName': 'string',
            'thingId': 'string',
            'thingArn': 'string',
            'thingTypeName': 'string',
            'attributes': {
                'string': 'string'
            },
            'version': 123
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the DescribeThing operation.

        
        

        - **defaultClientId** *(string) --* 

          The default client ID.

          
        

        - **thingName** *(string) --* 

          The name of the thing.

          
        

        - **thingId** *(string) --* 

          The ID of the thing to describe.

          
        

        - **thingArn** *(string) --* 

          The ARN of the thing to describe.

          
        

        - **thingTypeName** *(string) --* 

          The thing type name.

          
        

        - **attributes** *(dict) --* 

          The thing attributes.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **version** *(integer) --* 

          The current version of the thing record in the registry.

           

          .. note::

             

            To avoid unintentional changes to the information in the registry, you can pass the version information in the ``expectedVersion`` parameter of the ``UpdateThing`` and ``DeleteThing`` calls.

             

          
    

  .. py:method:: describe_thing_group(**kwargs)

    

    Describe a thing group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeThingGroup>`_    


    **Request Syntax** 
    ::

      response = client.describe_thing_group(
          thingGroupName='string'
      )
    :type thingGroupName: string
    :param thingGroupName: **[REQUIRED]** 

      The name of the thing group.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'thingGroupName': 'string',
            'thingGroupId': 'string',
            'thingGroupArn': 'string',
            'version': 123,
            'thingGroupProperties': {
                'thingGroupDescription': 'string',
                'attributePayload': {
                    'attributes': {
                        'string': 'string'
                    },
                    'merge': True|False
                }
            },
            'thingGroupMetadata': {
                'parentGroupName': 'string',
                'rootToParentThingGroups': [
                    {
                        'groupName': 'string',
                        'groupArn': 'string'
                    },
                ],
                'creationDate': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **thingGroupName** *(string) --* 

          The name of the thing group.

          
        

        - **thingGroupId** *(string) --* 

          The thing group ID.

          
        

        - **thingGroupArn** *(string) --* 

          The thing group ARN.

          
        

        - **version** *(integer) --* 

          The version of the thing group.

          
        

        - **thingGroupProperties** *(dict) --* 

          The thing group properties.

          
          

          - **thingGroupDescription** *(string) --* 

            The thing group description.

            
          

          - **attributePayload** *(dict) --* 

            The thing group attributes in JSON format.

            
            

            - **attributes** *(dict) --* 

              A JSON string containing up to three key-value pair in JSON format. For example:

               

               ``{\"attributes\":{\"string1\":\"string2\"}}``  

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **merge** *(boolean) --* 

              Specifies whether the list of attributes provided in the ``AttributePayload`` is merged with the attributes stored in the registry, instead of overwriting them.

               

              To remove an attribute, call ``UpdateThing`` with an empty attribute value.

               

              .. note::

                 

                The ``merge`` attribute is only valid when calling ``UpdateThing`` .

                 

              
        
      
        

        - **thingGroupMetadata** *(dict) --* 

          Thing group metadata.

          
          

          - **parentGroupName** *(string) --* 

            The parent thing group name.

            
          

          - **rootToParentThingGroups** *(list) --* 

            The root parent thing group.

            
            

            - *(dict) --* 

              The name and ARN of a group.

              
              

              - **groupName** *(string) --* 

                The group name.

                
              

              - **groupArn** *(string) --* 

                The group ARN.

                
          
        
          

          - **creationDate** *(datetime) --* 

            The UNIX timestamp of when the thing group was created.

            
      
    

  .. py:method:: describe_thing_registration_task(**kwargs)

    

    Describes a bulk thing provisioning task.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeThingRegistrationTask>`_    


    **Request Syntax** 
    ::

      response = client.describe_thing_registration_task(
          taskId='string'
      )
    :type taskId: string
    :param taskId: **[REQUIRED]** 

      The task ID.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'taskId': 'string',
            'creationDate': datetime(2015, 1, 1),
            'lastModifiedDate': datetime(2015, 1, 1),
            'templateBody': 'string',
            'inputFileBucket': 'string',
            'inputFileKey': 'string',
            'roleArn': 'string',
            'status': 'InProgress'|'Completed'|'Failed'|'Cancelled'|'Cancelling',
            'message': 'string',
            'successCount': 123,
            'failureCount': 123,
            'percentageProgress': 123
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **taskId** *(string) --* 

          The task ID.

          
        

        - **creationDate** *(datetime) --* 

          The task creation date.

          
        

        - **lastModifiedDate** *(datetime) --* 

          The date when the task was last modified.

          
        

        - **templateBody** *(string) --* 

          The task's template.

          
        

        - **inputFileBucket** *(string) --* 

          The S3 bucket that contains the input file.

          
        

        - **inputFileKey** *(string) --* 

          The input file key.

          
        

        - **roleArn** *(string) --* 

          The role ARN that grants access to the input file bucket.

          
        

        - **status** *(string) --* 

          The status of the bulk thing provisioning task.

          
        

        - **message** *(string) --* 

          The message.

          
        

        - **successCount** *(integer) --* 

          The number of things successfully provisioned.

          
        

        - **failureCount** *(integer) --* 

          The number of things that failed to be provisioned.

          
        

        - **percentageProgress** *(integer) --* 

          The progress of the bulk provisioning task expressed as a percentage.

          
    

  .. py:method:: describe_thing_type(**kwargs)

    

    Gets information about the specified thing type.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DescribeThingType>`_    


    **Request Syntax** 
    ::

      response = client.describe_thing_type(
          thingTypeName='string'
      )
    :type thingTypeName: string
    :param thingTypeName: **[REQUIRED]** 

      The name of the thing type.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'thingTypeName': 'string',
            'thingTypeId': 'string',
            'thingTypeArn': 'string',
            'thingTypeProperties': {
                'thingTypeDescription': 'string',
                'searchableAttributes': [
                    'string',
                ]
            },
            'thingTypeMetadata': {
                'deprecated': True|False,
                'deprecationDate': datetime(2015, 1, 1),
                'creationDate': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output for the DescribeThingType operation.

        
        

        - **thingTypeName** *(string) --* 

          The name of the thing type.

          
        

        - **thingTypeId** *(string) --* 

          The thing type ID.

          
        

        - **thingTypeArn** *(string) --* 

          The thing type ARN.

          
        

        - **thingTypeProperties** *(dict) --* 

          The ThingTypeProperties contains information about the thing type including description, and a list of searchable thing attribute names.

          
          

          - **thingTypeDescription** *(string) --* 

            The description of the thing type.

            
          

          - **searchableAttributes** *(list) --* 

            A list of searchable thing attribute names.

            
            

            - *(string) --* 
        
      
        

        - **thingTypeMetadata** *(dict) --* 

          The ThingTypeMetadata contains additional information about the thing type including: creation date and time, a value indicating whether the thing type is deprecated, and a date and time when it was deprecated.

          
          

          - **deprecated** *(boolean) --* 

            Whether the thing type is deprecated. If **true** , no new things could be associated with this type.

            
          

          - **deprecationDate** *(datetime) --* 

            The date and time when the thing type was deprecated.

            
          

          - **creationDate** *(datetime) --* 

            The date and time when the thing type was created.

            
      
    

  .. py:method:: detach_policy(**kwargs)

    

    Detaches a policy from the specified target.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DetachPolicy>`_    


    **Request Syntax** 
    ::

      response = client.detach_policy(
          policyName='string',
          target='string'
      )
    :type policyName: string
    :param policyName: **[REQUIRED]** 

      The policy to detach.

      

    
    :type target: string
    :param target: **[REQUIRED]** 

      The target from which the policy will be detached.

      

    
    
    :returns: None

  .. py:method:: detach_principal_policy(**kwargs)

    

    Removes the specified policy from the specified certificate.

     

     **Note:** This API is deprecated. Please use  DetachPolicy instead.

    

    .. danger::

            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.


    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DetachPrincipalPolicy>`_    


    **Request Syntax** 
    ::

      response = client.detach_principal_policy(
          policyName='string',
          principal='string'
      )
    :type policyName: string
    :param policyName: **[REQUIRED]** 

      The name of the policy to detach.

      

    
    :type principal: string
    :param principal: **[REQUIRED]** 

      The principal.

       

      If the principal is a certificate, specify the certificate ARN. If the principal is an Amazon Cognito identity, specify the identity ID.

      

    
    
    :returns: None

  .. py:method:: detach_thing_principal(**kwargs)

    

    Detaches the specified principal from the specified thing.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DetachThingPrincipal>`_    


    **Request Syntax** 
    ::

      response = client.detach_thing_principal(
          thingName='string',
          principal='string'
      )
    :type thingName: string
    :param thingName: **[REQUIRED]** 

      The name of the thing.

      

    
    :type principal: string
    :param principal: **[REQUIRED]** 

      If the principal is a certificate, this value must be ARN of the certificate. If the principal is an Amazon Cognito identity, this value must be the ID of the Amazon Cognito identity.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        The output from the DetachThingPrincipal operation.

        
    

  .. py:method:: disable_topic_rule(**kwargs)

    

    Disables the rule.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DisableTopicRule>`_    


    **Request Syntax** 
    ::

      response = client.disable_topic_rule(
          ruleName='string'
      )
    :type ruleName: string
    :param ruleName: **[REQUIRED]** 

      The name of the rule to disable.

      

    
    
    :returns: None

  .. py:method:: enable_topic_rule(**kwargs)

    

    Enables the rule.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/EnableTopicRule>`_    


    **Request Syntax** 
    ::

      response = client.enable_topic_rule(
          ruleName='string'
      )
    :type ruleName: string
    :param ruleName: **[REQUIRED]** 

      The name of the topic rule to enable.

      

    
    
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


  .. py:method:: get_effective_policies(**kwargs)

    

    Gets effective policies.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/GetEffectivePolicies>`_    


    **Request Syntax** 
    ::

      response = client.get_effective_policies(
          principal='string',
          cognitoIdentityPoolId='string',
          thingName='string'
      )
    :type principal: string
    :param principal: 

      The principal.

      

    
    :type cognitoIdentityPoolId: string
    :param cognitoIdentityPoolId: 

      The Cognito identity pool ID.

      

    
    :type thingName: string
    :param thingName: 

      The thing name.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'effectivePolicies': [
                {
                    'policyName': 'string',
                    'policyArn': 'string',
                    'policyDocument': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **effectivePolicies** *(list) --* 

          The effective policies.

          
          

          - *(dict) --* 

            The policy that has the effect on the authorization results.

            
            

            - **policyName** *(string) --* 

              The policy name.

              
            

            - **policyArn** *(string) --* 

              The policy ARN.

              
            

            - **policyDocument** *(string) --* 

              The IAM policy document.

              
        
      
    

  .. py:method:: get_indexing_configuration()

    

    Gets the search configuration.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/GetIndexingConfiguration>`_    


    **Request Syntax** 
    ::

      response = client.get_indexing_configuration()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'thingIndexingConfiguration': {
                'thingIndexingMode': 'OFF'|'REGISTRY'|'REGISTRY_AND_SHADOW'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **thingIndexingConfiguration** *(dict) --* 

          Thing indexing configuration.

          
          

          - **thingIndexingMode** *(string) --* 

            Thing indexing mode. Valid values are: 

             

             
            * REGISTRY – Your thing index will contain only registry data. 
             
            * REGISTRY_AND_SHADOW - Your thing index will contain registry and shadow data. 
             
            * OFF - Thing indexing is disabled. 
             

            
      
    

  .. py:method:: get_job_document(**kwargs)

    

    Gets a job document.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/GetJobDocument>`_    


    **Request Syntax** 
    ::

      response = client.get_job_document(
          jobId='string'
      )
    :type jobId: string
    :param jobId: **[REQUIRED]** 

      The unique identifier you assigned to this job when it was created.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'document': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **document** *(string) --* 

          The job document content.

          
    

  .. py:method:: get_logging_options()

    

    Gets the logging options.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/GetLoggingOptions>`_    


    **Request Syntax** 
    ::

      response = client.get_logging_options()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'roleArn': 'string',
            'logLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the GetLoggingOptions operation.

        
        

        - **roleArn** *(string) --* 

          The ARN of the IAM role that grants access.

          
        

        - **logLevel** *(string) --* 

          The logging level.

          
    

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


  .. py:method:: get_policy(**kwargs)

    

    Gets information about the specified policy with the policy document of the default version.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/GetPolicy>`_    


    **Request Syntax** 
    ::

      response = client.get_policy(
          policyName='string'
      )
    :type policyName: string
    :param policyName: **[REQUIRED]** 

      The name of the policy.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'policyName': 'string',
            'policyArn': 'string',
            'policyDocument': 'string',
            'defaultVersionId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the GetPolicy operation.

        
        

        - **policyName** *(string) --* 

          The policy name.

          
        

        - **policyArn** *(string) --* 

          The policy ARN.

          
        

        - **policyDocument** *(string) --* 

          The JSON document that describes the policy.

          
        

        - **defaultVersionId** *(string) --* 

          The default policy version ID.

          
    

  .. py:method:: get_policy_version(**kwargs)

    

    Gets information about the specified policy version.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/GetPolicyVersion>`_    


    **Request Syntax** 
    ::

      response = client.get_policy_version(
          policyName='string',
          policyVersionId='string'
      )
    :type policyName: string
    :param policyName: **[REQUIRED]** 

      The name of the policy.

      

    
    :type policyVersionId: string
    :param policyVersionId: **[REQUIRED]** 

      The policy version ID.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'policyArn': 'string',
            'policyName': 'string',
            'policyDocument': 'string',
            'policyVersionId': 'string',
            'isDefaultVersion': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the GetPolicyVersion operation.

        
        

        - **policyArn** *(string) --* 

          The policy ARN.

          
        

        - **policyName** *(string) --* 

          The policy name.

          
        

        - **policyDocument** *(string) --* 

          The JSON document that describes the policy.

          
        

        - **policyVersionId** *(string) --* 

          The policy version ID.

          
        

        - **isDefaultVersion** *(boolean) --* 

          Specifies whether the policy version is the default.

          
    

  .. py:method:: get_registration_code()

    

    Gets a registration code used to register a CA certificate with AWS IoT.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/GetRegistrationCode>`_    


    **Request Syntax** 
    ::

      response = client.get_registration_code()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'registrationCode': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the GetRegistrationCode operation.

        
        

        - **registrationCode** *(string) --* 

          The CA certificate registration code.

          
    

  .. py:method:: get_topic_rule(**kwargs)

    

    Gets information about the rule.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/GetTopicRule>`_    


    **Request Syntax** 
    ::

      response = client.get_topic_rule(
          ruleName='string'
      )
    :type ruleName: string
    :param ruleName: **[REQUIRED]** 

      The name of the rule.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ruleArn': 'string',
            'rule': {
                'ruleName': 'string',
                'sql': 'string',
                'description': 'string',
                'createdAt': datetime(2015, 1, 1),
                'actions': [
                    {
                        'dynamoDB': {
                            'tableName': 'string',
                            'roleArn': 'string',
                            'operation': 'string',
                            'hashKeyField': 'string',
                            'hashKeyValue': 'string',
                            'hashKeyType': 'STRING'|'NUMBER',
                            'rangeKeyField': 'string',
                            'rangeKeyValue': 'string',
                            'rangeKeyType': 'STRING'|'NUMBER',
                            'payloadField': 'string'
                        },
                        'dynamoDBv2': {
                            'roleArn': 'string',
                            'putItem': {
                                'tableName': 'string'
                            }
                        },
                        'lambda': {
                            'functionArn': 'string'
                        },
                        'sns': {
                            'targetArn': 'string',
                            'roleArn': 'string',
                            'messageFormat': 'RAW'|'JSON'
                        },
                        'sqs': {
                            'roleArn': 'string',
                            'queueUrl': 'string',
                            'useBase64': True|False
                        },
                        'kinesis': {
                            'roleArn': 'string',
                            'streamName': 'string',
                            'partitionKey': 'string'
                        },
                        'republish': {
                            'roleArn': 'string',
                            'topic': 'string'
                        },
                        's3': {
                            'roleArn': 'string',
                            'bucketName': 'string',
                            'key': 'string',
                            'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
                        },
                        'firehose': {
                            'roleArn': 'string',
                            'deliveryStreamName': 'string',
                            'separator': 'string'
                        },
                        'cloudwatchMetric': {
                            'roleArn': 'string',
                            'metricNamespace': 'string',
                            'metricName': 'string',
                            'metricValue': 'string',
                            'metricUnit': 'string',
                            'metricTimestamp': 'string'
                        },
                        'cloudwatchAlarm': {
                            'roleArn': 'string',
                            'alarmName': 'string',
                            'stateReason': 'string',
                            'stateValue': 'string'
                        },
                        'elasticsearch': {
                            'roleArn': 'string',
                            'endpoint': 'string',
                            'index': 'string',
                            'type': 'string',
                            'id': 'string'
                        },
                        'salesforce': {
                            'token': 'string',
                            'url': 'string'
                        }
                    },
                ],
                'ruleDisabled': True|False,
                'awsIotSqlVersion': 'string',
                'errorAction': {
                    'dynamoDB': {
                        'tableName': 'string',
                        'roleArn': 'string',
                        'operation': 'string',
                        'hashKeyField': 'string',
                        'hashKeyValue': 'string',
                        'hashKeyType': 'STRING'|'NUMBER',
                        'rangeKeyField': 'string',
                        'rangeKeyValue': 'string',
                        'rangeKeyType': 'STRING'|'NUMBER',
                        'payloadField': 'string'
                    },
                    'dynamoDBv2': {
                        'roleArn': 'string',
                        'putItem': {
                            'tableName': 'string'
                        }
                    },
                    'lambda': {
                        'functionArn': 'string'
                    },
                    'sns': {
                        'targetArn': 'string',
                        'roleArn': 'string',
                        'messageFormat': 'RAW'|'JSON'
                    },
                    'sqs': {
                        'roleArn': 'string',
                        'queueUrl': 'string',
                        'useBase64': True|False
                    },
                    'kinesis': {
                        'roleArn': 'string',
                        'streamName': 'string',
                        'partitionKey': 'string'
                    },
                    'republish': {
                        'roleArn': 'string',
                        'topic': 'string'
                    },
                    's3': {
                        'roleArn': 'string',
                        'bucketName': 'string',
                        'key': 'string',
                        'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
                    },
                    'firehose': {
                        'roleArn': 'string',
                        'deliveryStreamName': 'string',
                        'separator': 'string'
                    },
                    'cloudwatchMetric': {
                        'roleArn': 'string',
                        'metricNamespace': 'string',
                        'metricName': 'string',
                        'metricValue': 'string',
                        'metricUnit': 'string',
                        'metricTimestamp': 'string'
                    },
                    'cloudwatchAlarm': {
                        'roleArn': 'string',
                        'alarmName': 'string',
                        'stateReason': 'string',
                        'stateValue': 'string'
                    },
                    'elasticsearch': {
                        'roleArn': 'string',
                        'endpoint': 'string',
                        'index': 'string',
                        'type': 'string',
                        'id': 'string'
                    },
                    'salesforce': {
                        'token': 'string',
                        'url': 'string'
                    }
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the GetTopicRule operation.

        
        

        - **ruleArn** *(string) --* 

          The rule ARN.

          
        

        - **rule** *(dict) --* 

          The rule.

          
          

          - **ruleName** *(string) --* 

            The name of the rule.

            
          

          - **sql** *(string) --* 

            The SQL statement used to query the topic. When using a SQL query with multiple lines, be sure to escape the newline characters.

            
          

          - **description** *(string) --* 

            The description of the rule.

            
          

          - **createdAt** *(datetime) --* 

            The date and time the rule was created.

            
          

          - **actions** *(list) --* 

            The actions associated with the rule.

            
            

            - *(dict) --* 

              Describes the actions associated with a rule.

              
              

              - **dynamoDB** *(dict) --* 

                Write to a DynamoDB table.

                
                

                - **tableName** *(string) --* 

                  The name of the DynamoDB table.

                  
                

                - **roleArn** *(string) --* 

                  The ARN of the IAM role that grants access to the DynamoDB table.

                  
                

                - **operation** *(string) --* 

                  The type of operation to be performed. This follows the substitution template, so it can be ``${operation}`` , but the substitution must result in one of the following: ``INSERT`` , ``UPDATE`` , or ``DELETE`` .

                  
                

                - **hashKeyField** *(string) --* 

                  The hash key name.

                  
                

                - **hashKeyValue** *(string) --* 

                  The hash key value.

                  
                

                - **hashKeyType** *(string) --* 

                  The hash key type. Valid values are "STRING" or "NUMBER"

                  
                

                - **rangeKeyField** *(string) --* 

                  The range key name.

                  
                

                - **rangeKeyValue** *(string) --* 

                  The range key value.

                  
                

                - **rangeKeyType** *(string) --* 

                  The range key type. Valid values are "STRING" or "NUMBER"

                  
                

                - **payloadField** *(string) --* 

                  The action payload. This name can be customized.

                  
            
              

              - **dynamoDBv2** *(dict) --* 

                Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.

                
                

                - **roleArn** *(string) --* 

                  The ARN of the IAM role that grants access to the DynamoDB table.

                  
                

                - **putItem** *(dict) --* 

                  Specifies the DynamoDB table to which the message data will be written. For example:

                   

                   ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName": "my-table" } } }``  

                   

                  Each attribute in the message payload will be written to a separate column in the DynamoDB database.

                  
                  

                  - **tableName** *(string) --* 

                    The table where the message data will be written

                    
              
            
              

              - **lambda** *(dict) --* 

                Invoke a Lambda function.

                
                

                - **functionArn** *(string) --* 

                  The ARN of the Lambda function.

                  
            
              

              - **sns** *(dict) --* 

                Publish to an Amazon SNS topic.

                
                

                - **targetArn** *(string) --* 

                  The ARN of the SNS topic.

                  
                

                - **roleArn** *(string) --* 

                  The ARN of the IAM role that grants access.

                  
                

                - **messageFormat** *(string) --* 

                  The message format of the message to publish. Optional. Accepted values are "JSON" and "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see `http\://docs.aws.amazon.com/sns/latest/dg/json-formats.html <http://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their official documentation.

                  
            
              

              - **sqs** *(dict) --* 

                Publish to an Amazon SQS queue.

                
                

                - **roleArn** *(string) --* 

                  The ARN of the IAM role that grants access.

                  
                

                - **queueUrl** *(string) --* 

                  The URL of the Amazon SQS queue.

                  
                

                - **useBase64** *(boolean) --* 

                  Specifies whether to use Base64 encoding.

                  
            
              

              - **kinesis** *(dict) --* 

                Write data to an Amazon Kinesis stream.

                
                

                - **roleArn** *(string) --* 

                  The ARN of the IAM role that grants access to the Amazon Kinesis stream.

                  
                

                - **streamName** *(string) --* 

                  The name of the Amazon Kinesis stream.

                  
                

                - **partitionKey** *(string) --* 

                  The partition key.

                  
            
              

              - **republish** *(dict) --* 

                Publish to another MQTT topic.

                
                

                - **roleArn** *(string) --* 

                  The ARN of the IAM role that grants access.

                  
                

                - **topic** *(string) --* 

                  The name of the MQTT topic.

                  
            
              

              - **s3** *(dict) --* 

                Write to an Amazon S3 bucket.

                
                

                - **roleArn** *(string) --* 

                  The ARN of the IAM role that grants access.

                  
                

                - **bucketName** *(string) --* 

                  The Amazon S3 bucket.

                  
                

                - **key** *(string) --* 

                  The object key.

                  
                

                - **cannedAcl** *(string) --* 

                  The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see `S3 canned ACLs <http://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .

                  
            
              

              - **firehose** *(dict) --* 

                Write to an Amazon Kinesis Firehose stream.

                
                

                - **roleArn** *(string) --* 

                  The IAM role that grants access to the Amazon Kinesis Firehose stream.

                  
                

                - **deliveryStreamName** *(string) --* 

                  The delivery stream name.

                  
                

                - **separator** *(string) --* 

                  A character separator that will be used to separate records written to the Firehose stream. Valid values are: '\n' (newline), '\t' (tab), '\r\n' (Windows newline), ',' (comma).

                  
            
              

              - **cloudwatchMetric** *(dict) --* 

                Capture a CloudWatch metric.

                
                

                - **roleArn** *(string) --* 

                  The IAM role that allows access to the CloudWatch metric.

                  
                

                - **metricNamespace** *(string) --* 

                  The CloudWatch metric namespace name.

                  
                

                - **metricName** *(string) --* 

                  The CloudWatch metric name.

                  
                

                - **metricValue** *(string) --* 

                  The CloudWatch metric value.

                  
                

                - **metricUnit** *(string) --* 

                  The `metric unit <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__ supported by CloudWatch.

                  
                

                - **metricTimestamp** *(string) --* 

                  An optional `Unix timestamp <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__ .

                  
            
              

              - **cloudwatchAlarm** *(dict) --* 

                Change the state of a CloudWatch alarm.

                
                

                - **roleArn** *(string) --* 

                  The IAM role that allows access to the CloudWatch alarm.

                  
                

                - **alarmName** *(string) --* 

                  The CloudWatch alarm name.

                  
                

                - **stateReason** *(string) --* 

                  The reason for the alarm change.

                  
                

                - **stateValue** *(string) --* 

                  The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

                  
            
              

              - **elasticsearch** *(dict) --* 

                Write data to an Amazon Elasticsearch Service domain.

                
                

                - **roleArn** *(string) --* 

                  The IAM role ARN that has access to Elasticsearch.

                  
                

                - **endpoint** *(string) --* 

                  The endpoint of your Elasticsearch domain.

                  
                

                - **index** *(string) --* 

                  The Elasticsearch index where you want to store your data.

                  
                

                - **type** *(string) --* 

                  The type of document you are storing.

                  
                

                - **id** *(string) --* 

                  The unique identifier for the document you are storing.

                  
            
              

              - **salesforce** *(dict) --* 

                Send a message to a Salesforce IoT Cloud Input Stream.

                
                

                - **token** *(string) --* 

                  The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

                  
                

                - **url** *(string) --* 

                  The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

                  
            
          
        
          

          - **ruleDisabled** *(boolean) --* 

            Specifies whether the rule is disabled.

            
          

          - **awsIotSqlVersion** *(string) --* 

            The version of the SQL rules engine to use when evaluating the rule.

            
          

          - **errorAction** *(dict) --* 

            The action to perform when an error occurs.

            
            

            - **dynamoDB** *(dict) --* 

              Write to a DynamoDB table.

              
              

              - **tableName** *(string) --* 

                The name of the DynamoDB table.

                
              

              - **roleArn** *(string) --* 

                The ARN of the IAM role that grants access to the DynamoDB table.

                
              

              - **operation** *(string) --* 

                The type of operation to be performed. This follows the substitution template, so it can be ``${operation}`` , but the substitution must result in one of the following: ``INSERT`` , ``UPDATE`` , or ``DELETE`` .

                
              

              - **hashKeyField** *(string) --* 

                The hash key name.

                
              

              - **hashKeyValue** *(string) --* 

                The hash key value.

                
              

              - **hashKeyType** *(string) --* 

                The hash key type. Valid values are "STRING" or "NUMBER"

                
              

              - **rangeKeyField** *(string) --* 

                The range key name.

                
              

              - **rangeKeyValue** *(string) --* 

                The range key value.

                
              

              - **rangeKeyType** *(string) --* 

                The range key type. Valid values are "STRING" or "NUMBER"

                
              

              - **payloadField** *(string) --* 

                The action payload. This name can be customized.

                
          
            

            - **dynamoDBv2** *(dict) --* 

              Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.

              
              

              - **roleArn** *(string) --* 

                The ARN of the IAM role that grants access to the DynamoDB table.

                
              

              - **putItem** *(dict) --* 

                Specifies the DynamoDB table to which the message data will be written. For example:

                 

                 ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName": "my-table" } } }``  

                 

                Each attribute in the message payload will be written to a separate column in the DynamoDB database.

                
                

                - **tableName** *(string) --* 

                  The table where the message data will be written

                  
            
          
            

            - **lambda** *(dict) --* 

              Invoke a Lambda function.

              
              

              - **functionArn** *(string) --* 

                The ARN of the Lambda function.

                
          
            

            - **sns** *(dict) --* 

              Publish to an Amazon SNS topic.

              
              

              - **targetArn** *(string) --* 

                The ARN of the SNS topic.

                
              

              - **roleArn** *(string) --* 

                The ARN of the IAM role that grants access.

                
              

              - **messageFormat** *(string) --* 

                The message format of the message to publish. Optional. Accepted values are "JSON" and "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see `http\://docs.aws.amazon.com/sns/latest/dg/json-formats.html <http://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their official documentation.

                
          
            

            - **sqs** *(dict) --* 

              Publish to an Amazon SQS queue.

              
              

              - **roleArn** *(string) --* 

                The ARN of the IAM role that grants access.

                
              

              - **queueUrl** *(string) --* 

                The URL of the Amazon SQS queue.

                
              

              - **useBase64** *(boolean) --* 

                Specifies whether to use Base64 encoding.

                
          
            

            - **kinesis** *(dict) --* 

              Write data to an Amazon Kinesis stream.

              
              

              - **roleArn** *(string) --* 

                The ARN of the IAM role that grants access to the Amazon Kinesis stream.

                
              

              - **streamName** *(string) --* 

                The name of the Amazon Kinesis stream.

                
              

              - **partitionKey** *(string) --* 

                The partition key.

                
          
            

            - **republish** *(dict) --* 

              Publish to another MQTT topic.

              
              

              - **roleArn** *(string) --* 

                The ARN of the IAM role that grants access.

                
              

              - **topic** *(string) --* 

                The name of the MQTT topic.

                
          
            

            - **s3** *(dict) --* 

              Write to an Amazon S3 bucket.

              
              

              - **roleArn** *(string) --* 

                The ARN of the IAM role that grants access.

                
              

              - **bucketName** *(string) --* 

                The Amazon S3 bucket.

                
              

              - **key** *(string) --* 

                The object key.

                
              

              - **cannedAcl** *(string) --* 

                The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see `S3 canned ACLs <http://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .

                
          
            

            - **firehose** *(dict) --* 

              Write to an Amazon Kinesis Firehose stream.

              
              

              - **roleArn** *(string) --* 

                The IAM role that grants access to the Amazon Kinesis Firehose stream.

                
              

              - **deliveryStreamName** *(string) --* 

                The delivery stream name.

                
              

              - **separator** *(string) --* 

                A character separator that will be used to separate records written to the Firehose stream. Valid values are: '\n' (newline), '\t' (tab), '\r\n' (Windows newline), ',' (comma).

                
          
            

            - **cloudwatchMetric** *(dict) --* 

              Capture a CloudWatch metric.

              
              

              - **roleArn** *(string) --* 

                The IAM role that allows access to the CloudWatch metric.

                
              

              - **metricNamespace** *(string) --* 

                The CloudWatch metric namespace name.

                
              

              - **metricName** *(string) --* 

                The CloudWatch metric name.

                
              

              - **metricValue** *(string) --* 

                The CloudWatch metric value.

                
              

              - **metricUnit** *(string) --* 

                The `metric unit <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__ supported by CloudWatch.

                
              

              - **metricTimestamp** *(string) --* 

                An optional `Unix timestamp <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__ .

                
          
            

            - **cloudwatchAlarm** *(dict) --* 

              Change the state of a CloudWatch alarm.

              
              

              - **roleArn** *(string) --* 

                The IAM role that allows access to the CloudWatch alarm.

                
              

              - **alarmName** *(string) --* 

                The CloudWatch alarm name.

                
              

              - **stateReason** *(string) --* 

                The reason for the alarm change.

                
              

              - **stateValue** *(string) --* 

                The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

                
          
            

            - **elasticsearch** *(dict) --* 

              Write data to an Amazon Elasticsearch Service domain.

              
              

              - **roleArn** *(string) --* 

                The IAM role ARN that has access to Elasticsearch.

                
              

              - **endpoint** *(string) --* 

                The endpoint of your Elasticsearch domain.

                
              

              - **index** *(string) --* 

                The Elasticsearch index where you want to store your data.

                
              

              - **type** *(string) --* 

                The type of document you are storing.

                
              

              - **id** *(string) --* 

                The unique identifier for the document you are storing.

                
          
            

            - **salesforce** *(dict) --* 

              Send a message to a Salesforce IoT Cloud Input Stream.

              
              

              - **token** *(string) --* 

                The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

                
              

              - **url** *(string) --* 

                The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

                
          
        
      
    

  .. py:method:: get_v2_logging_options()

    

    Gets the fine grained logging options.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/GetV2LoggingOptions>`_    


    **Request Syntax** 
    ::

      response = client.get_v2_logging_options()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'roleArn': 'string',
            'defaultLogLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED',
            'disableAllLogs': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **roleArn** *(string) --* 

          The IAM role ARN AWS IoT uses to write to your CloudWatch logs.

          
        

        - **defaultLogLevel** *(string) --* 

          The default log level.

          
        

        - **disableAllLogs** *(boolean) --* 

          Disables all logs.

          
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: list_attached_policies(**kwargs)

    

    Lists the policies attached to the specified thing group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListAttachedPolicies>`_    


    **Request Syntax** 
    ::

      response = client.list_attached_policies(
          target='string',
          recursive=True|False,
          marker='string',
          pageSize=123
      )
    :type target: string
    :param target: **[REQUIRED]** 

      The group for which the policies will be listed.

      

    
    :type recursive: boolean
    :param recursive: 

      When true, recursively list attached policies.

      

    
    :type marker: string
    :param marker: 

      The token to retrieve the next set of results.

      

    
    :type pageSize: integer
    :param pageSize: 

      The maximum number of results to be returned per request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'policies': [
                {
                    'policyName': 'string',
                    'policyArn': 'string'
                },
            ],
            'nextMarker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **policies** *(list) --* 

          The policies.

          
          

          - *(dict) --* 

            Describes an AWS IoT policy.

            
            

            - **policyName** *(string) --* 

              The policy name.

              
            

            - **policyArn** *(string) --* 

              The policy ARN.

              
        
      
        

        - **nextMarker** *(string) --* 

          The token to retrieve the next set of results, or ``null`` if there are no more results.

          
    

  .. py:method:: list_authorizers(**kwargs)

    

    Lists the authorizers registered in your account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListAuthorizers>`_    


    **Request Syntax** 
    ::

      response = client.list_authorizers(
          pageSize=123,
          marker='string',
          ascendingOrder=True|False,
          status='ACTIVE'|'INACTIVE'
      )
    :type pageSize: integer
    :param pageSize: 

      The maximum number of results to return at one time.

      

    
    :type marker: string
    :param marker: 

      A marker used to get the next set of results.

      

    
    :type ascendingOrder: boolean
    :param ascendingOrder: 

      Return the list of authorizers in ascending alphabetical order.

      

    
    :type status: string
    :param status: 

      The status of the list authorizers request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'authorizers': [
                {
                    'authorizerName': 'string',
                    'authorizerArn': 'string'
                },
            ],
            'nextMarker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **authorizers** *(list) --* 

          The authorizers.

          
          

          - *(dict) --* 

            The authorizer summary.

            
            

            - **authorizerName** *(string) --* 

              The authorizer name.

              
            

            - **authorizerArn** *(string) --* 

              The authorizer ARN.

              
        
      
        

        - **nextMarker** *(string) --* 

          A marker used to get the next set of results.

          
    

  .. py:method:: list_ca_certificates(**kwargs)

    

    Lists the CA certificates registered for your AWS account.

     

    The results are paginated with a default page size of 25. You can use the returned marker to retrieve additional results.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListCACertificates>`_    


    **Request Syntax** 
    ::

      response = client.list_ca_certificates(
          pageSize=123,
          marker='string',
          ascendingOrder=True|False
      )
    :type pageSize: integer
    :param pageSize: 

      The result page size.

      

    
    :type marker: string
    :param marker: 

      The marker for the next set of results.

      

    
    :type ascendingOrder: boolean
    :param ascendingOrder: 

      Determines the order of the results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'certificates': [
                {
                    'certificateArn': 'string',
                    'certificateId': 'string',
                    'status': 'ACTIVE'|'INACTIVE',
                    'creationDate': datetime(2015, 1, 1)
                },
            ],
            'nextMarker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the ListCACertificates operation.

        
        

        - **certificates** *(list) --* 

          The CA certificates registered in your AWS account.

          
          

          - *(dict) --* 

            A CA certificate.

            
            

            - **certificateArn** *(string) --* 

              The ARN of the CA certificate.

              
            

            - **certificateId** *(string) --* 

              The ID of the CA certificate.

              
            

            - **status** *(string) --* 

              The status of the CA certificate.

               

              The status value REGISTER_INACTIVE is deprecated and should not be used.

              
            

            - **creationDate** *(datetime) --* 

              The date the CA certificate was created.

              
        
      
        

        - **nextMarker** *(string) --* 

          The current position within the list of CA certificates.

          
    

  .. py:method:: list_certificates(**kwargs)

    

    Lists the certificates registered in your AWS account.

     

    The results are paginated with a default page size of 25. You can use the returned marker to retrieve additional results.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListCertificates>`_    


    **Request Syntax** 
    ::

      response = client.list_certificates(
          pageSize=123,
          marker='string',
          ascendingOrder=True|False
      )
    :type pageSize: integer
    :param pageSize: 

      The result page size.

      

    
    :type marker: string
    :param marker: 

      The marker for the next set of results.

      

    
    :type ascendingOrder: boolean
    :param ascendingOrder: 

      Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'certificates': [
                {
                    'certificateArn': 'string',
                    'certificateId': 'string',
                    'status': 'ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION',
                    'creationDate': datetime(2015, 1, 1)
                },
            ],
            'nextMarker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output of the ListCertificates operation.

        
        

        - **certificates** *(list) --* 

          The descriptions of the certificates.

          
          

          - *(dict) --* 

            Information about a certificate.

            
            

            - **certificateArn** *(string) --* 

              The ARN of the certificate.

              
            

            - **certificateId** *(string) --* 

              The ID of the certificate.

              
            

            - **status** *(string) --* 

              The status of the certificate.

               

              The status value REGISTER_INACTIVE is deprecated and should not be used.

              
            

            - **creationDate** *(datetime) --* 

              The date and time the certificate was created.

              
        
      
        

        - **nextMarker** *(string) --* 

          The marker for the next set of results, or null if there are no additional results.

          
    

  .. py:method:: list_certificates_by_ca(**kwargs)

    

    List the device certificates signed by the specified CA certificate.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListCertificatesByCA>`_    


    **Request Syntax** 
    ::

      response = client.list_certificates_by_ca(
          caCertificateId='string',
          pageSize=123,
          marker='string',
          ascendingOrder=True|False
      )
    :type caCertificateId: string
    :param caCertificateId: **[REQUIRED]** 

      The ID of the CA certificate. This operation will list all registered device certificate that were signed by this CA certificate.

      

    
    :type pageSize: integer
    :param pageSize: 

      The result page size.

      

    
    :type marker: string
    :param marker: 

      The marker for the next set of results.

      

    
    :type ascendingOrder: boolean
    :param ascendingOrder: 

      Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'certificates': [
                {
                    'certificateArn': 'string',
                    'certificateId': 'string',
                    'status': 'ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION',
                    'creationDate': datetime(2015, 1, 1)
                },
            ],
            'nextMarker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output of the ListCertificatesByCA operation.

        
        

        - **certificates** *(list) --* 

          The device certificates signed by the specified CA certificate.

          
          

          - *(dict) --* 

            Information about a certificate.

            
            

            - **certificateArn** *(string) --* 

              The ARN of the certificate.

              
            

            - **certificateId** *(string) --* 

              The ID of the certificate.

              
            

            - **status** *(string) --* 

              The status of the certificate.

               

              The status value REGISTER_INACTIVE is deprecated and should not be used.

              
            

            - **creationDate** *(datetime) --* 

              The date and time the certificate was created.

              
        
      
        

        - **nextMarker** *(string) --* 

          The marker for the next set of results, or null if there are no additional results.

          
    

  .. py:method:: list_indices(**kwargs)

    

    Lists the search indices.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListIndices>`_    


    **Request Syntax** 
    ::

      response = client.list_indices(
          nextToken='string',
          maxResults=123
      )
    :type nextToken: string
    :param nextToken: 

      The token used to get the next set of results, or **null** if there are no additional results.

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of results to return at one time.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'indexNames': [
                'string',
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **indexNames** *(list) --* 

          The index names.

          
          

          - *(string) --* 
      
        

        - **nextToken** *(string) --* 

          The token used to get the next set of results, or **null** if there are no additional results.

          
    

  .. py:method:: list_job_executions_for_job(**kwargs)

    

    Lists the job executions for a job.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListJobExecutionsForJob>`_    


    **Request Syntax** 
    ::

      response = client.list_job_executions_for_job(
          jobId='string',
          status='QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'REJECTED'|'REMOVED'|'CANCELED',
          maxResults=123,
          nextToken='string'
      )
    :type jobId: string
    :param jobId: **[REQUIRED]** 

      The unique identifier you assigned to this job when it was created.

      

    
    :type status: string
    :param status: 

      The status of the job.

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of results to be returned per request.

      

    
    :type nextToken: string
    :param nextToken: 

      The token to retrieve the next set of results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'executionSummaries': [
                {
                    'thingArn': 'string',
                    'jobExecutionSummary': {
                        'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'REJECTED'|'REMOVED'|'CANCELED',
                        'queuedAt': datetime(2015, 1, 1),
                        'startedAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'executionNumber': 123
                    }
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **executionSummaries** *(list) --* 

          A list of job execution summaries.

          
          

          - *(dict) --* 

            Contains a summary of information about job executions for a specific job.

            
            

            - **thingArn** *(string) --* 

              The ARN of the thing on which the job execution is running.

              
            

            - **jobExecutionSummary** *(dict) --* 

              Contains a subset of information about a job execution.

              
              

              - **status** *(string) --* 

                The status of the job execution.

                
              

              - **queuedAt** *(datetime) --* 

                The time, in milliseconds since the epoch, when the job execution was queued.

                
              

              - **startedAt** *(datetime) --* 

                The time, in milliseconds since the epoch, when the job execution started.

                
              

              - **lastUpdatedAt** *(datetime) --* 

                The time, in milliseconds since the epoch, when the job execution was last updated.

                
              

              - **executionNumber** *(integer) --* 

                A string (consisting of the digits "0" through "9") which identifies this particular job execution on this particular device. It can be used later in commands which return or update job execution information.

                
          
        
      
        

        - **nextToken** *(string) --* 

          The token for the next set of results, or **null** if there are no additional results.

          
    

  .. py:method:: list_job_executions_for_thing(**kwargs)

    

    Lists the job executions for the specified thing.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListJobExecutionsForThing>`_    


    **Request Syntax** 
    ::

      response = client.list_job_executions_for_thing(
          thingName='string',
          status='QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'REJECTED'|'REMOVED'|'CANCELED',
          maxResults=123,
          nextToken='string'
      )
    :type thingName: string
    :param thingName: **[REQUIRED]** 

      The thing name.

      

    
    :type status: string
    :param status: 

      An optional filter that lets you search for jobs that have the specified status.

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of results to be returned per request.

      

    
    :type nextToken: string
    :param nextToken: 

      The token to retrieve the next set of results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'executionSummaries': [
                {
                    'jobId': 'string',
                    'jobExecutionSummary': {
                        'status': 'QUEUED'|'IN_PROGRESS'|'SUCCEEDED'|'FAILED'|'REJECTED'|'REMOVED'|'CANCELED',
                        'queuedAt': datetime(2015, 1, 1),
                        'startedAt': datetime(2015, 1, 1),
                        'lastUpdatedAt': datetime(2015, 1, 1),
                        'executionNumber': 123
                    }
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **executionSummaries** *(list) --* 

          A list of job execution summaries.

          
          

          - *(dict) --* 

            The job execution summary for a thing.

            
            

            - **jobId** *(string) --* 

              The unique identifier you assigned to this job when it was created.

              
            

            - **jobExecutionSummary** *(dict) --* 

              Contains a subset of information about a job execution.

              
              

              - **status** *(string) --* 

                The status of the job execution.

                
              

              - **queuedAt** *(datetime) --* 

                The time, in milliseconds since the epoch, when the job execution was queued.

                
              

              - **startedAt** *(datetime) --* 

                The time, in milliseconds since the epoch, when the job execution started.

                
              

              - **lastUpdatedAt** *(datetime) --* 

                The time, in milliseconds since the epoch, when the job execution was last updated.

                
              

              - **executionNumber** *(integer) --* 

                A string (consisting of the digits "0" through "9") which identifies this particular job execution on this particular device. It can be used later in commands which return or update job execution information.

                
          
        
      
        

        - **nextToken** *(string) --* 

          The token for the next set of results, or **null** if there are no additional results.

          
    

  .. py:method:: list_jobs(**kwargs)

    

    Lists jobs.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListJobs>`_    


    **Request Syntax** 
    ::

      response = client.list_jobs(
          status='IN_PROGRESS'|'CANCELED'|'COMPLETED',
          targetSelection='CONTINUOUS'|'SNAPSHOT',
          maxResults=123,
          nextToken='string',
          thingGroupName='string',
          thingGroupId='string'
      )
    :type status: string
    :param status: 

      An optional filter that lets you search for jobs that have the specified status.

      

    
    :type targetSelection: string
    :param targetSelection: 

      Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a thing when the thing is added to a target group, even after the job was completed by all things originally in the group. 

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of results to return per request.

      

    
    :type nextToken: string
    :param nextToken: 

      The token to retrieve the next set of results.

      

    
    :type thingGroupName: string
    :param thingGroupName: 

      A filter that limits the returned jobs to those for the specified group.

      

    
    :type thingGroupId: string
    :param thingGroupId: 

      A filter that limits the returned jobs to those for the specified group.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'jobs': [
                {
                    'jobArn': 'string',
                    'jobId': 'string',
                    'thingGroupId': 'string',
                    'targetSelection': 'CONTINUOUS'|'SNAPSHOT',
                    'status': 'IN_PROGRESS'|'CANCELED'|'COMPLETED',
                    'createdAt': datetime(2015, 1, 1),
                    'lastUpdatedAt': datetime(2015, 1, 1),
                    'completedAt': datetime(2015, 1, 1)
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **jobs** *(list) --* 

          A list of jobs.

          
          

          - *(dict) --* 

            The job summary.

            
            

            - **jobArn** *(string) --* 

              The job ARN.

              
            

            - **jobId** *(string) --* 

              The unique identifier you assigned to this job when it was created.

              
            

            - **thingGroupId** *(string) --* 

              The ID of the thing group.

              
            

            - **targetSelection** *(string) --* 

              Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a thing when the thing is added to a target group, even after the job was completed by all things originally in the group.

              
            

            - **status** *(string) --* 

              The job summary status.

              
            

            - **createdAt** *(datetime) --* 

              The time, in milliseconds since the epoch, when the job was created.

              
            

            - **lastUpdatedAt** *(datetime) --* 

              The time, in milliseconds since the epoch, when the job was last updated.

              
            

            - **completedAt** *(datetime) --* 

              The time, in milliseconds since the epoch, when the job completed.

              
        
      
        

        - **nextToken** *(string) --* 

          The token for the next set of results, or **null** if there are no additional results.

          
    

  .. py:method:: list_outgoing_certificates(**kwargs)

    

    Lists certificates that are being transferred but not yet accepted.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListOutgoingCertificates>`_    


    **Request Syntax** 
    ::

      response = client.list_outgoing_certificates(
          pageSize=123,
          marker='string',
          ascendingOrder=True|False
      )
    :type pageSize: integer
    :param pageSize: 

      The result page size.

      

    
    :type marker: string
    :param marker: 

      The marker for the next set of results.

      

    
    :type ascendingOrder: boolean
    :param ascendingOrder: 

      Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'outgoingCertificates': [
                {
                    'certificateArn': 'string',
                    'certificateId': 'string',
                    'transferredTo': 'string',
                    'transferDate': datetime(2015, 1, 1),
                    'transferMessage': 'string',
                    'creationDate': datetime(2015, 1, 1)
                },
            ],
            'nextMarker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the ListOutgoingCertificates operation.

        
        

        - **outgoingCertificates** *(list) --* 

          The certificates that are being transferred but not yet accepted.

          
          

          - *(dict) --* 

            A certificate that has been transferred but not yet accepted.

            
            

            - **certificateArn** *(string) --* 

              The certificate ARN.

              
            

            - **certificateId** *(string) --* 

              The certificate ID.

              
            

            - **transferredTo** *(string) --* 

              The AWS account to which the transfer was made.

              
            

            - **transferDate** *(datetime) --* 

              The date the transfer was initiated.

              
            

            - **transferMessage** *(string) --* 

              The transfer message.

              
            

            - **creationDate** *(datetime) --* 

              The certificate creation date.

              
        
      
        

        - **nextMarker** *(string) --* 

          The marker for the next set of results.

          
    

  .. py:method:: list_policies(**kwargs)

    

    Lists your policies.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListPolicies>`_    


    **Request Syntax** 
    ::

      response = client.list_policies(
          marker='string',
          pageSize=123,
          ascendingOrder=True|False
      )
    :type marker: string
    :param marker: 

      The marker for the next set of results.

      

    
    :type pageSize: integer
    :param pageSize: 

      The result page size.

      

    
    :type ascendingOrder: boolean
    :param ascendingOrder: 

      Specifies the order for results. If true, the results are returned in ascending creation order.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'policies': [
                {
                    'policyName': 'string',
                    'policyArn': 'string'
                },
            ],
            'nextMarker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the ListPolicies operation.

        
        

        - **policies** *(list) --* 

          The descriptions of the policies.

          
          

          - *(dict) --* 

            Describes an AWS IoT policy.

            
            

            - **policyName** *(string) --* 

              The policy name.

              
            

            - **policyArn** *(string) --* 

              The policy ARN.

              
        
      
        

        - **nextMarker** *(string) --* 

          The marker for the next set of results, or null if there are no additional results.

          
    

  .. py:method:: list_policy_principals(**kwargs)

    

    Lists the principals associated with the specified policy.

     

     **Note:** This API is deprecated. Please use  ListTargetsForPolicy instead.

    

    .. danger::

            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.


    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListPolicyPrincipals>`_    


    **Request Syntax** 
    ::

      response = client.list_policy_principals(
          policyName='string',
          marker='string',
          pageSize=123,
          ascendingOrder=True|False
      )
    :type policyName: string
    :param policyName: **[REQUIRED]** 

      The policy name.

      

    
    :type marker: string
    :param marker: 

      The marker for the next set of results.

      

    
    :type pageSize: integer
    :param pageSize: 

      The result page size.

      

    
    :type ascendingOrder: boolean
    :param ascendingOrder: 

      Specifies the order for results. If true, the results are returned in ascending creation order.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'principals': [
                'string',
            ],
            'nextMarker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the ListPolicyPrincipals operation.

        
        

        - **principals** *(list) --* 

          The descriptions of the principals.

          
          

          - *(string) --* 
      
        

        - **nextMarker** *(string) --* 

          The marker for the next set of results, or null if there are no additional results.

          
    

  .. py:method:: list_policy_versions(**kwargs)

    

    Lists the versions of the specified policy and identifies the default version.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListPolicyVersions>`_    


    **Request Syntax** 
    ::

      response = client.list_policy_versions(
          policyName='string'
      )
    :type policyName: string
    :param policyName: **[REQUIRED]** 

      The policy name.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'policyVersions': [
                {
                    'versionId': 'string',
                    'isDefaultVersion': True|False,
                    'createDate': datetime(2015, 1, 1)
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the ListPolicyVersions operation.

        
        

        - **policyVersions** *(list) --* 

          The policy versions.

          
          

          - *(dict) --* 

            Describes a policy version.

            
            

            - **versionId** *(string) --* 

              The policy version ID.

              
            

            - **isDefaultVersion** *(boolean) --* 

              Specifies whether the policy version is the default.

              
            

            - **createDate** *(datetime) --* 

              The date and time the policy was created.

              
        
      
    

  .. py:method:: list_principal_policies(**kwargs)

    

    Lists the policies attached to the specified principal. If you use an Cognito identity, the ID must be in `AmazonCognito Identity format <http://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetCredentialsForIdentity.html#API_GetCredentialsForIdentity_RequestSyntax>`__ .

     

     **Note:** This API is deprecated. Please use  ListAttachedPolicies instead.

    

    .. danger::

            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.


    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListPrincipalPolicies>`_    


    **Request Syntax** 
    ::

      response = client.list_principal_policies(
          principal='string',
          marker='string',
          pageSize=123,
          ascendingOrder=True|False
      )
    :type principal: string
    :param principal: **[REQUIRED]** 

      The principal.

      

    
    :type marker: string
    :param marker: 

      The marker for the next set of results.

      

    
    :type pageSize: integer
    :param pageSize: 

      The result page size.

      

    
    :type ascendingOrder: boolean
    :param ascendingOrder: 

      Specifies the order for results. If true, results are returned in ascending creation order.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'policies': [
                {
                    'policyName': 'string',
                    'policyArn': 'string'
                },
            ],
            'nextMarker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the ListPrincipalPolicies operation.

        
        

        - **policies** *(list) --* 

          The policies.

          
          

          - *(dict) --* 

            Describes an AWS IoT policy.

            
            

            - **policyName** *(string) --* 

              The policy name.

              
            

            - **policyArn** *(string) --* 

              The policy ARN.

              
        
      
        

        - **nextMarker** *(string) --* 

          The marker for the next set of results, or null if there are no additional results.

          
    

  .. py:method:: list_principal_things(**kwargs)

    

    Lists the things associated with the specified principal.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListPrincipalThings>`_    


    **Request Syntax** 
    ::

      response = client.list_principal_things(
          nextToken='string',
          maxResults=123,
          principal='string'
      )
    :type nextToken: string
    :param nextToken: 

      The token used to get the next set of results, or **null** if there are no additional results.

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of results to return in this operation.

      

    
    :type principal: string
    :param principal: **[REQUIRED]** 

      The principal.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'things': [
                'string',
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the ListPrincipalThings operation.

        
        

        - **things** *(list) --* 

          The things.

          
          

          - *(string) --* 
      
        

        - **nextToken** *(string) --* 

          The token used to get the next set of results, or **null** if there are no additional results.

          
    

  .. py:method:: list_role_aliases(**kwargs)

    

    Lists the role aliases registered in your account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListRoleAliases>`_    


    **Request Syntax** 
    ::

      response = client.list_role_aliases(
          pageSize=123,
          marker='string',
          ascendingOrder=True|False
      )
    :type pageSize: integer
    :param pageSize: 

      The maximum number of results to return at one time.

      

    
    :type marker: string
    :param marker: 

      A marker used to get the next set of results.

      

    
    :type ascendingOrder: boolean
    :param ascendingOrder: 

      Return the list of role aliases in ascending alphabetical order.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'roleAliases': [
                'string',
            ],
            'nextMarker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **roleAliases** *(list) --* 

          The role aliases.

          
          

          - *(string) --* 
      
        

        - **nextMarker** *(string) --* 

          A marker used to get the next set of results.

          
    

  .. py:method:: list_targets_for_policy(**kwargs)

    

    List targets for the specified policy.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListTargetsForPolicy>`_    


    **Request Syntax** 
    ::

      response = client.list_targets_for_policy(
          policyName='string',
          marker='string',
          pageSize=123
      )
    :type policyName: string
    :param policyName: **[REQUIRED]** 

      The policy name.

      

    
    :type marker: string
    :param marker: 

      A marker used to get the next set of results.

      

    
    :type pageSize: integer
    :param pageSize: 

      The maximum number of results to return at one time.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'targets': [
                'string',
            ],
            'nextMarker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **targets** *(list) --* 

          The policy targets.

          
          

          - *(string) --* 
      
        

        - **nextMarker** *(string) --* 

          A marker used to get the next set of results.

          
    

  .. py:method:: list_thing_groups(**kwargs)

    

    List the thing groups in your account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThingGroups>`_    


    **Request Syntax** 
    ::

      response = client.list_thing_groups(
          nextToken='string',
          maxResults=123,
          parentGroup='string',
          namePrefixFilter='string',
          recursive=True|False
      )
    :type nextToken: string
    :param nextToken: 

      The token used to get the next set of results, or **null** if there are no additional results.

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of results to return at one time.

      

    
    :type parentGroup: string
    :param parentGroup: 

      A filter that limits the results to those with the specified parent group.

      

    
    :type namePrefixFilter: string
    :param namePrefixFilter: 

      A filter that limits the results to those with the specified name prefix.

      

    
    :type recursive: boolean
    :param recursive: 

      If true, return child groups as well.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'thingGroups': [
                {
                    'groupName': 'string',
                    'groupArn': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **thingGroups** *(list) --* 

          The thing groups.

          
          

          - *(dict) --* 

            The name and ARN of a group.

            
            

            - **groupName** *(string) --* 

              The group name.

              
            

            - **groupArn** *(string) --* 

              The group ARN.

              
        
      
        

        - **nextToken** *(string) --* 

          The token used to get the next set of results, or **null** if there are no additional results.

          
    

  .. py:method:: list_thing_groups_for_thing(**kwargs)

    

    List the thing groups to which the specified thing belongs.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThingGroupsForThing>`_    


    **Request Syntax** 
    ::

      response = client.list_thing_groups_for_thing(
          thingName='string',
          nextToken='string',
          maxResults=123
      )
    :type thingName: string
    :param thingName: **[REQUIRED]** 

      The thing name.

      

    
    :type nextToken: string
    :param nextToken: 

      The token used to get the next set of results, or **null** if there are no additional results.

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of results to return at one time.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'thingGroups': [
                {
                    'groupName': 'string',
                    'groupArn': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **thingGroups** *(list) --* 

          The thing groups.

          
          

          - *(dict) --* 

            The name and ARN of a group.

            
            

            - **groupName** *(string) --* 

              The group name.

              
            

            - **groupArn** *(string) --* 

              The group ARN.

              
        
      
        

        - **nextToken** *(string) --* 

          The token used to get the next set of results, or **null** if there are no additional results.

          
    

  .. py:method:: list_thing_principals(**kwargs)

    

    Lists the principals associated with the specified thing.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThingPrincipals>`_    


    **Request Syntax** 
    ::

      response = client.list_thing_principals(
          thingName='string'
      )
    :type thingName: string
    :param thingName: **[REQUIRED]** 

      The name of the thing.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'principals': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the ListThingPrincipals operation.

        
        

        - **principals** *(list) --* 

          The principals associated with the thing.

          
          

          - *(string) --* 
      
    

  .. py:method:: list_thing_registration_task_reports(**kwargs)

    

    Information about the thing registration tasks.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThingRegistrationTaskReports>`_    


    **Request Syntax** 
    ::

      response = client.list_thing_registration_task_reports(
          taskId='string',
          reportType='ERRORS'|'RESULTS',
          nextToken='string',
          maxResults=123
      )
    :type taskId: string
    :param taskId: **[REQUIRED]** 

      The id of the task.

      

    
    :type reportType: string
    :param reportType: **[REQUIRED]** 

      The type of task report.

      

    
    :type nextToken: string
    :param nextToken: 

      The token to retrieve the next set of results.

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of results to return per request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'resourceLinks': [
                'string',
            ],
            'reportType': 'ERRORS'|'RESULTS',
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **resourceLinks** *(list) --* 

          Links to the task resources.

          
          

          - *(string) --* 
      
        

        - **reportType** *(string) --* 

          The type of task report.

          
        

        - **nextToken** *(string) --* 

          The token to retrieve the next set of results.

          
    

  .. py:method:: list_thing_registration_tasks(**kwargs)

    

    List bulk thing provisioning tasks.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThingRegistrationTasks>`_    


    **Request Syntax** 
    ::

      response = client.list_thing_registration_tasks(
          nextToken='string',
          maxResults=123,
          status='InProgress'|'Completed'|'Failed'|'Cancelled'|'Cancelling'
      )
    :type nextToken: string
    :param nextToken: 

      The token used to get the next set of results, or **null** if there are no additional results.

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of results to return at one time.

      

    
    :type status: string
    :param status: 

      The status of the bulk thing provisioning task.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'taskIds': [
                'string',
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **taskIds** *(list) --* 

          A list of bulk thing provisioning task IDs.

          
          

          - *(string) --* 
      
        

        - **nextToken** *(string) --* 

          The token used to get the next set of results, or **null** if there are no additional results.

          
    

  .. py:method:: list_thing_types(**kwargs)

    

    Lists the existing thing types.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThingTypes>`_    


    **Request Syntax** 
    ::

      response = client.list_thing_types(
          nextToken='string',
          maxResults=123,
          thingTypeName='string'
      )
    :type nextToken: string
    :param nextToken: 

      The token for the next set of results, or **null** if there are no additional results.

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of results to return in this operation.

      

    
    :type thingTypeName: string
    :param thingTypeName: 

      The name of the thing type.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'thingTypes': [
                {
                    'thingTypeName': 'string',
                    'thingTypeArn': 'string',
                    'thingTypeProperties': {
                        'thingTypeDescription': 'string',
                        'searchableAttributes': [
                            'string',
                        ]
                    },
                    'thingTypeMetadata': {
                        'deprecated': True|False,
                        'deprecationDate': datetime(2015, 1, 1),
                        'creationDate': datetime(2015, 1, 1)
                    }
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output for the ListThingTypes operation.

        
        

        - **thingTypes** *(list) --* 

          The thing types.

          
          

          - *(dict) --* 

            The definition of the thing type, including thing type name and description.

            
            

            - **thingTypeName** *(string) --* 

              The name of the thing type.

              
            

            - **thingTypeArn** *(string) --* 

              The thing type ARN.

              
            

            - **thingTypeProperties** *(dict) --* 

              The ThingTypeProperties for the thing type.

              
              

              - **thingTypeDescription** *(string) --* 

                The description of the thing type.

                
              

              - **searchableAttributes** *(list) --* 

                A list of searchable thing attribute names.

                
                

                - *(string) --* 
            
          
            

            - **thingTypeMetadata** *(dict) --* 

              The ThingTypeMetadata contains additional information about the thing type including: creation date and time, a value indicating whether the thing type is deprecated, and a date and time when it was deprecated.

              
              

              - **deprecated** *(boolean) --* 

                Whether the thing type is deprecated. If **true** , no new things could be associated with this type.

                
              

              - **deprecationDate** *(datetime) --* 

                The date and time when the thing type was deprecated.

                
              

              - **creationDate** *(datetime) --* 

                The date and time when the thing type was created.

                
          
        
      
        

        - **nextToken** *(string) --* 

          The token for the next set of results, or **null** if there are no additional results.

          
    

  .. py:method:: list_things(**kwargs)

    

    Lists your things. Use the **attributeName** and **attributeValue** parameters to filter your things. For example, calling ``ListThings`` with attributeName=Color and attributeValue=Red retrieves all things in the registry that contain an attribute **Color** with the value **Red** . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThings>`_    


    **Request Syntax** 
    ::

      response = client.list_things(
          nextToken='string',
          maxResults=123,
          attributeName='string',
          attributeValue='string',
          thingTypeName='string'
      )
    :type nextToken: string
    :param nextToken: 

      The token used to get the next set of results, or **null** if there are no additional results.

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of results to return in this operation.

      

    
    :type attributeName: string
    :param attributeName: 

      The attribute name used to search for things.

      

    
    :type attributeValue: string
    :param attributeValue: 

      The attribute value used to search for things.

      

    
    :type thingTypeName: string
    :param thingTypeName: 

      The name of the thing type used to search for things.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'things': [
                {
                    'thingName': 'string',
                    'thingTypeName': 'string',
                    'thingArn': 'string',
                    'attributes': {
                        'string': 'string'
                    },
                    'version': 123
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the ListThings operation.

        
        

        - **things** *(list) --* 

          The things.

          
          

          - *(dict) --* 

            The properties of the thing, including thing name, thing type name, and a list of thing attributes.

            
            

            - **thingName** *(string) --* 

              The name of the thing.

              
            

            - **thingTypeName** *(string) --* 

              The name of the thing type, if the thing has been associated with a type.

              
            

            - **thingArn** *(string) --* 

              The thing ARN.

              
            

            - **attributes** *(dict) --* 

              A list of thing attributes which are name-value pairs.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **version** *(integer) --* 

              The version of the thing record in the registry.

              
        
      
        

        - **nextToken** *(string) --* 

          The token used to get the next set of results, or **null** if there are no additional results.

          
    

  .. py:method:: list_things_in_thing_group(**kwargs)

    

    Lists the things in the specified group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThingsInThingGroup>`_    


    **Request Syntax** 
    ::

      response = client.list_things_in_thing_group(
          thingGroupName='string',
          recursive=True|False,
          nextToken='string',
          maxResults=123
      )
    :type thingGroupName: string
    :param thingGroupName: **[REQUIRED]** 

      The thing group name.

      

    
    :type recursive: boolean
    :param recursive: 

      When true, list things in this thing group and in all child groups as well.

      

    
    :type nextToken: string
    :param nextToken: 

      The token used to get the next set of results, or **null** if there are no additional results.

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of results to return at one time.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'things': [
                'string',
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **things** *(list) --* 

          The things in the specified thing group.

          
          

          - *(string) --* 
      
        

        - **nextToken** *(string) --* 

          The token used to get the next set of results, or **null** if there are no additional results.

          
    

  .. py:method:: list_topic_rules(**kwargs)

    

    Lists the rules for the specific topic.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListTopicRules>`_    


    **Request Syntax** 
    ::

      response = client.list_topic_rules(
          topic='string',
          maxResults=123,
          nextToken='string',
          ruleDisabled=True|False
      )
    :type topic: string
    :param topic: 

      The topic.

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of results to return.

      

    
    :type nextToken: string
    :param nextToken: 

      A token used to retrieve the next value.

      

    
    :type ruleDisabled: boolean
    :param ruleDisabled: 

      Specifies whether the rule is disabled.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'rules': [
                {
                    'ruleArn': 'string',
                    'ruleName': 'string',
                    'topicPattern': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'ruleDisabled': True|False
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the ListTopicRules operation.

        
        

        - **rules** *(list) --* 

          The rules.

          
          

          - *(dict) --* 

            Describes a rule.

            
            

            - **ruleArn** *(string) --* 

              The rule ARN.

              
            

            - **ruleName** *(string) --* 

              The name of the rule.

              
            

            - **topicPattern** *(string) --* 

              The pattern for the topic names that apply.

              
            

            - **createdAt** *(datetime) --* 

              The date and time the rule was created.

              
            

            - **ruleDisabled** *(boolean) --* 

              Specifies whether the rule is disabled.

              
        
      
        

        - **nextToken** *(string) --* 

          A token used to retrieve the next value.

          
    

  .. py:method:: list_v2_logging_levels(**kwargs)

    

    Lists logging levels.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListV2LoggingLevels>`_    


    **Request Syntax** 
    ::

      response = client.list_v2_logging_levels(
          targetType='DEFAULT'|'THING_GROUP',
          nextToken='string',
          maxResults=123
      )
    :type targetType: string
    :param targetType: 

      The type of resource for which you are configuring logging. Must be ``THING_Group`` .

      

    
    :type nextToken: string
    :param nextToken: 

      The token used to get the next set of results, or **null** if there are no additional results.

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of results to return at one time.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'logTargetConfigurations': [
                {
                    'logTarget': {
                        'targetType': 'DEFAULT'|'THING_GROUP',
                        'targetName': 'string'
                    },
                    'logLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **logTargetConfigurations** *(list) --* 

          The logging configuration for a target.

          
          

          - *(dict) --* 

            The target configuration.

            
            

            - **logTarget** *(dict) --* 

              A log target

              
              

              - **targetType** *(string) --* 

                The target type.

                
              

              - **targetName** *(string) --* 

                The target name.

                
          
            

            - **logLevel** *(string) --* 

              The logging level.

              
        
      
        

        - **nextToken** *(string) --* 

          The token used to get the next set of results, or **null** if there are no additional results.

          
    

  .. py:method:: register_ca_certificate(**kwargs)

    

    Registers a CA certificate with AWS IoT. This CA certificate can then be used to sign device certificates, which can be then registered with AWS IoT. You can register up to 10 CA certificates per AWS account that have the same subject field. This enables you to have up to 10 certificate authorities sign your device certificates. If you have more than one CA certificate registered, make sure you pass the CA certificate when you register your device certificates with the RegisterCertificate API.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/RegisterCACertificate>`_    


    **Request Syntax** 
    ::

      response = client.register_ca_certificate(
          caCertificate='string',
          verificationCertificate='string',
          setAsActive=True|False,
          allowAutoRegistration=True|False,
          registrationConfig={
              'templateBody': 'string',
              'roleArn': 'string'
          }
      )
    :type caCertificate: string
    :param caCertificate: **[REQUIRED]** 

      The CA certificate.

      

    
    :type verificationCertificate: string
    :param verificationCertificate: **[REQUIRED]** 

      The private key verification certificate.

      

    
    :type setAsActive: boolean
    :param setAsActive: 

      A boolean value that specifies if the CA certificate is set to active.

      

    
    :type allowAutoRegistration: boolean
    :param allowAutoRegistration: 

      Allows this CA certificate to be used for auto registration of device certificates.

      

    
    :type registrationConfig: dict
    :param registrationConfig: 

      Information about the registration configuration.

      

    
      - **templateBody** *(string) --* 

        The template body.

        

      
      - **roleArn** *(string) --* 

        The ARN of the role.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'certificateArn': 'string',
            'certificateId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the RegisterCACertificateResponse operation.

        
        

        - **certificateArn** *(string) --* 

          The CA certificate ARN.

          
        

        - **certificateId** *(string) --* 

          The CA certificate identifier.

          
    

  .. py:method:: register_certificate(**kwargs)

    

    Registers a device certificate with AWS IoT. If you have more than one CA certificate that has the same subject field, you must specify the CA certificate that was used to sign the device certificate being registered.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/RegisterCertificate>`_    


    **Request Syntax** 
    ::

      response = client.register_certificate(
          certificatePem='string',
          caCertificatePem='string',
          setAsActive=True|False,
          status='ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION'
      )
    :type certificatePem: string
    :param certificatePem: **[REQUIRED]** 

      The certificate data, in PEM format.

      

    
    :type caCertificatePem: string
    :param caCertificatePem: 

      The CA certificate used to sign the device certificate being registered.

      

    
    :type setAsActive: boolean
    :param setAsActive: 

      A boolean value that specifies if the CA certificate is set to active.

      

    
    :type status: string
    :param status: 

      The status of the register certificate request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'certificateArn': 'string',
            'certificateId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the RegisterCertificate operation.

        
        

        - **certificateArn** *(string) --* 

          The certificate ARN.

          
        

        - **certificateId** *(string) --* 

          The certificate identifier.

          
    

  .. py:method:: register_thing(**kwargs)

    

    Provisions a thing.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/RegisterThing>`_    


    **Request Syntax** 
    ::

      response = client.register_thing(
          templateBody='string',
          parameters={
              'string': 'string'
          }
      )
    :type templateBody: string
    :param templateBody: **[REQUIRED]** 

      The provisioning template. 

      

    
    :type parameters: dict
    :param parameters: 

      The parameters for provisioning a thing.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'certificatePem': 'string',
            'resourceArns': {
                'string': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **certificatePem** *(string) --* 

          The PEM of a certificate.

          
        

        - **resourceArns** *(dict) --* 

          ARNs for the generated resources.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
    

  .. py:method:: reject_certificate_transfer(**kwargs)

    

    Rejects a pending certificate transfer. After AWS IoT rejects a certificate transfer, the certificate status changes from **PENDING_TRANSFER** to **INACTIVE** .

     

    To check for pending certificate transfers, call  ListCertificates to enumerate your certificates.

     

    This operation can only be called by the transfer destination. After it is called, the certificate will be returned to the source's account in the INACTIVE state.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/RejectCertificateTransfer>`_    


    **Request Syntax** 
    ::

      response = client.reject_certificate_transfer(
          certificateId='string',
          rejectReason='string'
      )
    :type certificateId: string
    :param certificateId: **[REQUIRED]** 

      The ID of the certificate.

      

    
    :type rejectReason: string
    :param rejectReason: 

      The reason the certificate transfer was rejected.

      

    
    
    :returns: None

  .. py:method:: remove_thing_from_thing_group(**kwargs)

    

    Remove the specified thing from the specified group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/RemoveThingFromThingGroup>`_    


    **Request Syntax** 
    ::

      response = client.remove_thing_from_thing_group(
          thingGroupName='string',
          thingGroupArn='string',
          thingName='string',
          thingArn='string'
      )
    :type thingGroupName: string
    :param thingGroupName: 

      The group name.

      

    
    :type thingGroupArn: string
    :param thingGroupArn: 

      The group ARN.

      

    
    :type thingName: string
    :param thingName: 

      The name of the thing to remove from the group.

      

    
    :type thingArn: string
    :param thingArn: 

      The ARN of the thing to remove from the group.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: replace_topic_rule(**kwargs)

    

    Replaces the rule. You must specify all parameters for the new rule. Creating rules is an administrator-level action. Any user who has permission to create rules will be able to access data processed by the rule.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ReplaceTopicRule>`_    


    **Request Syntax** 
    ::

      response = client.replace_topic_rule(
          ruleName='string',
          topicRulePayload={
              'sql': 'string',
              'description': 'string',
              'actions': [
                  {
                      'dynamoDB': {
                          'tableName': 'string',
                          'roleArn': 'string',
                          'operation': 'string',
                          'hashKeyField': 'string',
                          'hashKeyValue': 'string',
                          'hashKeyType': 'STRING'|'NUMBER',
                          'rangeKeyField': 'string',
                          'rangeKeyValue': 'string',
                          'rangeKeyType': 'STRING'|'NUMBER',
                          'payloadField': 'string'
                      },
                      'dynamoDBv2': {
                          'roleArn': 'string',
                          'putItem': {
                              'tableName': 'string'
                          }
                      },
                      'lambda': {
                          'functionArn': 'string'
                      },
                      'sns': {
                          'targetArn': 'string',
                          'roleArn': 'string',
                          'messageFormat': 'RAW'|'JSON'
                      },
                      'sqs': {
                          'roleArn': 'string',
                          'queueUrl': 'string',
                          'useBase64': True|False
                      },
                      'kinesis': {
                          'roleArn': 'string',
                          'streamName': 'string',
                          'partitionKey': 'string'
                      },
                      'republish': {
                          'roleArn': 'string',
                          'topic': 'string'
                      },
                      's3': {
                          'roleArn': 'string',
                          'bucketName': 'string',
                          'key': 'string',
                          'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
                      },
                      'firehose': {
                          'roleArn': 'string',
                          'deliveryStreamName': 'string',
                          'separator': 'string'
                      },
                      'cloudwatchMetric': {
                          'roleArn': 'string',
                          'metricNamespace': 'string',
                          'metricName': 'string',
                          'metricValue': 'string',
                          'metricUnit': 'string',
                          'metricTimestamp': 'string'
                      },
                      'cloudwatchAlarm': {
                          'roleArn': 'string',
                          'alarmName': 'string',
                          'stateReason': 'string',
                          'stateValue': 'string'
                      },
                      'elasticsearch': {
                          'roleArn': 'string',
                          'endpoint': 'string',
                          'index': 'string',
                          'type': 'string',
                          'id': 'string'
                      },
                      'salesforce': {
                          'token': 'string',
                          'url': 'string'
                      }
                  },
              ],
              'ruleDisabled': True|False,
              'awsIotSqlVersion': 'string',
              'errorAction': {
                  'dynamoDB': {
                      'tableName': 'string',
                      'roleArn': 'string',
                      'operation': 'string',
                      'hashKeyField': 'string',
                      'hashKeyValue': 'string',
                      'hashKeyType': 'STRING'|'NUMBER',
                      'rangeKeyField': 'string',
                      'rangeKeyValue': 'string',
                      'rangeKeyType': 'STRING'|'NUMBER',
                      'payloadField': 'string'
                  },
                  'dynamoDBv2': {
                      'roleArn': 'string',
                      'putItem': {
                          'tableName': 'string'
                      }
                  },
                  'lambda': {
                      'functionArn': 'string'
                  },
                  'sns': {
                      'targetArn': 'string',
                      'roleArn': 'string',
                      'messageFormat': 'RAW'|'JSON'
                  },
                  'sqs': {
                      'roleArn': 'string',
                      'queueUrl': 'string',
                      'useBase64': True|False
                  },
                  'kinesis': {
                      'roleArn': 'string',
                      'streamName': 'string',
                      'partitionKey': 'string'
                  },
                  'republish': {
                      'roleArn': 'string',
                      'topic': 'string'
                  },
                  's3': {
                      'roleArn': 'string',
                      'bucketName': 'string',
                      'key': 'string',
                      'cannedAcl': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control'|'log-delivery-write'
                  },
                  'firehose': {
                      'roleArn': 'string',
                      'deliveryStreamName': 'string',
                      'separator': 'string'
                  },
                  'cloudwatchMetric': {
                      'roleArn': 'string',
                      'metricNamespace': 'string',
                      'metricName': 'string',
                      'metricValue': 'string',
                      'metricUnit': 'string',
                      'metricTimestamp': 'string'
                  },
                  'cloudwatchAlarm': {
                      'roleArn': 'string',
                      'alarmName': 'string',
                      'stateReason': 'string',
                      'stateValue': 'string'
                  },
                  'elasticsearch': {
                      'roleArn': 'string',
                      'endpoint': 'string',
                      'index': 'string',
                      'type': 'string',
                      'id': 'string'
                  },
                  'salesforce': {
                      'token': 'string',
                      'url': 'string'
                  }
              }
          }
      )
    :type ruleName: string
    :param ruleName: **[REQUIRED]** 

      The name of the rule.

      

    
    :type topicRulePayload: dict
    :param topicRulePayload: **[REQUIRED]** 

      The rule payload.

      

    
      - **sql** *(string) --* **[REQUIRED]** 

        The SQL statement used to query the topic. For more information, see `AWS IoT SQL Reference <http://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html#aws-iot-sql-reference>`__ in the *AWS IoT Developer Guide* .

        

      
      - **description** *(string) --* 

        The description of the rule.

        

      
      - **actions** *(list) --* **[REQUIRED]** 

        The actions associated with the rule.

        

      
        - *(dict) --* 

          Describes the actions associated with a rule.

          

        
          - **dynamoDB** *(dict) --* 

            Write to a DynamoDB table.

            

          
            - **tableName** *(string) --* **[REQUIRED]** 

              The name of the DynamoDB table.

              

            
            - **roleArn** *(string) --* **[REQUIRED]** 

              The ARN of the IAM role that grants access to the DynamoDB table.

              

            
            - **operation** *(string) --* 

              The type of operation to be performed. This follows the substitution template, so it can be ``${operation}`` , but the substitution must result in one of the following: ``INSERT`` , ``UPDATE`` , or ``DELETE`` .

              

            
            - **hashKeyField** *(string) --* **[REQUIRED]** 

              The hash key name.

              

            
            - **hashKeyValue** *(string) --* **[REQUIRED]** 

              The hash key value.

              

            
            - **hashKeyType** *(string) --* 

              The hash key type. Valid values are "STRING" or "NUMBER"

              

            
            - **rangeKeyField** *(string) --* 

              The range key name.

              

            
            - **rangeKeyValue** *(string) --* 

              The range key value.

              

            
            - **rangeKeyType** *(string) --* 

              The range key type. Valid values are "STRING" or "NUMBER"

              

            
            - **payloadField** *(string) --* 

              The action payload. This name can be customized.

              

            
          
          - **dynamoDBv2** *(dict) --* 

            Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.

            

          
            - **roleArn** *(string) --* 

              The ARN of the IAM role that grants access to the DynamoDB table.

              

            
            - **putItem** *(dict) --* 

              Specifies the DynamoDB table to which the message data will be written. For example:

               

               ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName": "my-table" } } }``  

               

              Each attribute in the message payload will be written to a separate column in the DynamoDB database.

              

            
              - **tableName** *(string) --* **[REQUIRED]** 

                The table where the message data will be written

                

              
            
          
          - **lambda** *(dict) --* 

            Invoke a Lambda function.

            

          
            - **functionArn** *(string) --* **[REQUIRED]** 

              The ARN of the Lambda function.

              

            
          
          - **sns** *(dict) --* 

            Publish to an Amazon SNS topic.

            

          
            - **targetArn** *(string) --* **[REQUIRED]** 

              The ARN of the SNS topic.

              

            
            - **roleArn** *(string) --* **[REQUIRED]** 

              The ARN of the IAM role that grants access.

              

            
            - **messageFormat** *(string) --* 

              The message format of the message to publish. Optional. Accepted values are "JSON" and "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see `http\://docs.aws.amazon.com/sns/latest/dg/json-formats.html <http://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their official documentation.

              

            
          
          - **sqs** *(dict) --* 

            Publish to an Amazon SQS queue.

            

          
            - **roleArn** *(string) --* **[REQUIRED]** 

              The ARN of the IAM role that grants access.

              

            
            - **queueUrl** *(string) --* **[REQUIRED]** 

              The URL of the Amazon SQS queue.

              

            
            - **useBase64** *(boolean) --* 

              Specifies whether to use Base64 encoding.

              

            
          
          - **kinesis** *(dict) --* 

            Write data to an Amazon Kinesis stream.

            

          
            - **roleArn** *(string) --* **[REQUIRED]** 

              The ARN of the IAM role that grants access to the Amazon Kinesis stream.

              

            
            - **streamName** *(string) --* **[REQUIRED]** 

              The name of the Amazon Kinesis stream.

              

            
            - **partitionKey** *(string) --* 

              The partition key.

              

            
          
          - **republish** *(dict) --* 

            Publish to another MQTT topic.

            

          
            - **roleArn** *(string) --* **[REQUIRED]** 

              The ARN of the IAM role that grants access.

              

            
            - **topic** *(string) --* **[REQUIRED]** 

              The name of the MQTT topic.

              

            
          
          - **s3** *(dict) --* 

            Write to an Amazon S3 bucket.

            

          
            - **roleArn** *(string) --* **[REQUIRED]** 

              The ARN of the IAM role that grants access.

              

            
            - **bucketName** *(string) --* **[REQUIRED]** 

              The Amazon S3 bucket.

              

            
            - **key** *(string) --* **[REQUIRED]** 

              The object key.

              

            
            - **cannedAcl** *(string) --* 

              The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see `S3 canned ACLs <http://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .

              

            
          
          - **firehose** *(dict) --* 

            Write to an Amazon Kinesis Firehose stream.

            

          
            - **roleArn** *(string) --* **[REQUIRED]** 

              The IAM role that grants access to the Amazon Kinesis Firehose stream.

              

            
            - **deliveryStreamName** *(string) --* **[REQUIRED]** 

              The delivery stream name.

              

            
            - **separator** *(string) --* 

              A character separator that will be used to separate records written to the Firehose stream. Valid values are: '\n' (newline), '\t' (tab), '\r\n' (Windows newline), ',' (comma).

              

            
          
          - **cloudwatchMetric** *(dict) --* 

            Capture a CloudWatch metric.

            

          
            - **roleArn** *(string) --* **[REQUIRED]** 

              The IAM role that allows access to the CloudWatch metric.

              

            
            - **metricNamespace** *(string) --* **[REQUIRED]** 

              The CloudWatch metric namespace name.

              

            
            - **metricName** *(string) --* **[REQUIRED]** 

              The CloudWatch metric name.

              

            
            - **metricValue** *(string) --* **[REQUIRED]** 

              The CloudWatch metric value.

              

            
            - **metricUnit** *(string) --* **[REQUIRED]** 

              The `metric unit <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__ supported by CloudWatch.

              

            
            - **metricTimestamp** *(string) --* 

              An optional `Unix timestamp <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__ .

              

            
          
          - **cloudwatchAlarm** *(dict) --* 

            Change the state of a CloudWatch alarm.

            

          
            - **roleArn** *(string) --* **[REQUIRED]** 

              The IAM role that allows access to the CloudWatch alarm.

              

            
            - **alarmName** *(string) --* **[REQUIRED]** 

              The CloudWatch alarm name.

              

            
            - **stateReason** *(string) --* **[REQUIRED]** 

              The reason for the alarm change.

              

            
            - **stateValue** *(string) --* **[REQUIRED]** 

              The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

              

            
          
          - **elasticsearch** *(dict) --* 

            Write data to an Amazon Elasticsearch Service domain.

            

          
            - **roleArn** *(string) --* **[REQUIRED]** 

              The IAM role ARN that has access to Elasticsearch.

              

            
            - **endpoint** *(string) --* **[REQUIRED]** 

              The endpoint of your Elasticsearch domain.

              

            
            - **index** *(string) --* **[REQUIRED]** 

              The Elasticsearch index where you want to store your data.

              

            
            - **type** *(string) --* **[REQUIRED]** 

              The type of document you are storing.

              

            
            - **id** *(string) --* **[REQUIRED]** 

              The unique identifier for the document you are storing.

              

            
          
          - **salesforce** *(dict) --* 

            Send a message to a Salesforce IoT Cloud Input Stream.

            

          
            - **token** *(string) --* **[REQUIRED]** 

              The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

              

            
            - **url** *(string) --* **[REQUIRED]** 

              The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

              

            
          
        
    
      - **ruleDisabled** *(boolean) --* 

        Specifies whether the rule is disabled.

        

      
      - **awsIotSqlVersion** *(string) --* 

        The version of the SQL rules engine to use when evaluating the rule.

        

      
      - **errorAction** *(dict) --* 

        The action to take when an error occurs.

        

      
        - **dynamoDB** *(dict) --* 

          Write to a DynamoDB table.

          

        
          - **tableName** *(string) --* **[REQUIRED]** 

            The name of the DynamoDB table.

            

          
          - **roleArn** *(string) --* **[REQUIRED]** 

            The ARN of the IAM role that grants access to the DynamoDB table.

            

          
          - **operation** *(string) --* 

            The type of operation to be performed. This follows the substitution template, so it can be ``${operation}`` , but the substitution must result in one of the following: ``INSERT`` , ``UPDATE`` , or ``DELETE`` .

            

          
          - **hashKeyField** *(string) --* **[REQUIRED]** 

            The hash key name.

            

          
          - **hashKeyValue** *(string) --* **[REQUIRED]** 

            The hash key value.

            

          
          - **hashKeyType** *(string) --* 

            The hash key type. Valid values are "STRING" or "NUMBER"

            

          
          - **rangeKeyField** *(string) --* 

            The range key name.

            

          
          - **rangeKeyValue** *(string) --* 

            The range key value.

            

          
          - **rangeKeyType** *(string) --* 

            The range key type. Valid values are "STRING" or "NUMBER"

            

          
          - **payloadField** *(string) --* 

            The action payload. This name can be customized.

            

          
        
        - **dynamoDBv2** *(dict) --* 

          Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.

          

        
          - **roleArn** *(string) --* 

            The ARN of the IAM role that grants access to the DynamoDB table.

            

          
          - **putItem** *(dict) --* 

            Specifies the DynamoDB table to which the message data will be written. For example:

             

             ``{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName": "my-table" } } }``  

             

            Each attribute in the message payload will be written to a separate column in the DynamoDB database.

            

          
            - **tableName** *(string) --* **[REQUIRED]** 

              The table where the message data will be written

              

            
          
        
        - **lambda** *(dict) --* 

          Invoke a Lambda function.

          

        
          - **functionArn** *(string) --* **[REQUIRED]** 

            The ARN of the Lambda function.

            

          
        
        - **sns** *(dict) --* 

          Publish to an Amazon SNS topic.

          

        
          - **targetArn** *(string) --* **[REQUIRED]** 

            The ARN of the SNS topic.

            

          
          - **roleArn** *(string) --* **[REQUIRED]** 

            The ARN of the IAM role that grants access.

            

          
          - **messageFormat** *(string) --* 

            The message format of the message to publish. Optional. Accepted values are "JSON" and "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see `http\://docs.aws.amazon.com/sns/latest/dg/json-formats.html <http://docs.aws.amazon.com/sns/latest/dg/json-formats.html>`__ refer to their official documentation.

            

          
        
        - **sqs** *(dict) --* 

          Publish to an Amazon SQS queue.

          

        
          - **roleArn** *(string) --* **[REQUIRED]** 

            The ARN of the IAM role that grants access.

            

          
          - **queueUrl** *(string) --* **[REQUIRED]** 

            The URL of the Amazon SQS queue.

            

          
          - **useBase64** *(boolean) --* 

            Specifies whether to use Base64 encoding.

            

          
        
        - **kinesis** *(dict) --* 

          Write data to an Amazon Kinesis stream.

          

        
          - **roleArn** *(string) --* **[REQUIRED]** 

            The ARN of the IAM role that grants access to the Amazon Kinesis stream.

            

          
          - **streamName** *(string) --* **[REQUIRED]** 

            The name of the Amazon Kinesis stream.

            

          
          - **partitionKey** *(string) --* 

            The partition key.

            

          
        
        - **republish** *(dict) --* 

          Publish to another MQTT topic.

          

        
          - **roleArn** *(string) --* **[REQUIRED]** 

            The ARN of the IAM role that grants access.

            

          
          - **topic** *(string) --* **[REQUIRED]** 

            The name of the MQTT topic.

            

          
        
        - **s3** *(dict) --* 

          Write to an Amazon S3 bucket.

          

        
          - **roleArn** *(string) --* **[REQUIRED]** 

            The ARN of the IAM role that grants access.

            

          
          - **bucketName** *(string) --* **[REQUIRED]** 

            The Amazon S3 bucket.

            

          
          - **key** *(string) --* **[REQUIRED]** 

            The object key.

            

          
          - **cannedAcl** *(string) --* 

            The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see `S3 canned ACLs <http://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`__ .

            

          
        
        - **firehose** *(dict) --* 

          Write to an Amazon Kinesis Firehose stream.

          

        
          - **roleArn** *(string) --* **[REQUIRED]** 

            The IAM role that grants access to the Amazon Kinesis Firehose stream.

            

          
          - **deliveryStreamName** *(string) --* **[REQUIRED]** 

            The delivery stream name.

            

          
          - **separator** *(string) --* 

            A character separator that will be used to separate records written to the Firehose stream. Valid values are: '\n' (newline), '\t' (tab), '\r\n' (Windows newline), ',' (comma).

            

          
        
        - **cloudwatchMetric** *(dict) --* 

          Capture a CloudWatch metric.

          

        
          - **roleArn** *(string) --* **[REQUIRED]** 

            The IAM role that allows access to the CloudWatch metric.

            

          
          - **metricNamespace** *(string) --* **[REQUIRED]** 

            The CloudWatch metric namespace name.

            

          
          - **metricName** *(string) --* **[REQUIRED]** 

            The CloudWatch metric name.

            

          
          - **metricValue** *(string) --* **[REQUIRED]** 

            The CloudWatch metric value.

            

          
          - **metricUnit** *(string) --* **[REQUIRED]** 

            The `metric unit <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit>`__ supported by CloudWatch.

            

          
          - **metricTimestamp** *(string) --* 

            An optional `Unix timestamp <http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp>`__ .

            

          
        
        - **cloudwatchAlarm** *(dict) --* 

          Change the state of a CloudWatch alarm.

          

        
          - **roleArn** *(string) --* **[REQUIRED]** 

            The IAM role that allows access to the CloudWatch alarm.

            

          
          - **alarmName** *(string) --* **[REQUIRED]** 

            The CloudWatch alarm name.

            

          
          - **stateReason** *(string) --* **[REQUIRED]** 

            The reason for the alarm change.

            

          
          - **stateValue** *(string) --* **[REQUIRED]** 

            The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

            

          
        
        - **elasticsearch** *(dict) --* 

          Write data to an Amazon Elasticsearch Service domain.

          

        
          - **roleArn** *(string) --* **[REQUIRED]** 

            The IAM role ARN that has access to Elasticsearch.

            

          
          - **endpoint** *(string) --* **[REQUIRED]** 

            The endpoint of your Elasticsearch domain.

            

          
          - **index** *(string) --* **[REQUIRED]** 

            The Elasticsearch index where you want to store your data.

            

          
          - **type** *(string) --* **[REQUIRED]** 

            The type of document you are storing.

            

          
          - **id** *(string) --* **[REQUIRED]** 

            The unique identifier for the document you are storing.

            

          
        
        - **salesforce** *(dict) --* 

          Send a message to a Salesforce IoT Cloud Input Stream.

          

        
          - **token** *(string) --* **[REQUIRED]** 

            The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

            

          
          - **url** *(string) --* **[REQUIRED]** 

            The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

            

          
        
      
    
    
    :returns: None

  .. py:method:: search_index(**kwargs)

    

    The query search index.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/SearchIndex>`_    


    **Request Syntax** 
    ::

      response = client.search_index(
          indexName='string',
          queryString='string',
          nextToken='string',
          maxResults=123,
          queryVersion='string'
      )
    :type indexName: string
    :param indexName: 

      The search index name.

      

    
    :type queryString: string
    :param queryString: **[REQUIRED]** 

      The search query string.

      

    
    :type nextToken: string
    :param nextToken: 

      The token used to get the next set of results, or **null** if there are no additional results.

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of results to return at one time.

      

    
    :type queryVersion: string
    :param queryVersion: 

      The query version.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'nextToken': 'string',
            'things': [
                {
                    'thingName': 'string',
                    'thingId': 'string',
                    'thingTypeName': 'string',
                    'thingGroupNames': [
                        'string',
                    ],
                    'attributes': {
                        'string': 'string'
                    },
                    'shadow': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **nextToken** *(string) --* 

          The token used to get the next set of results, or **null** if there are no additional results.

          
        

        - **things** *(list) --* 

          The things that match the search query.

          
          

          - *(dict) --* 

            The thing search index document.

            
            

            - **thingName** *(string) --* 

              The thing name.

              
            

            - **thingId** *(string) --* 

              The thing ID.

              
            

            - **thingTypeName** *(string) --* 

              The thing type name.

              
            

            - **thingGroupNames** *(list) --* 

              Thing group names.

              
              

              - *(string) --* 
          
            

            - **attributes** *(dict) --* 

              The attributes.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **shadow** *(string) --* 

              The thing shadow.

              
        
      
    

  .. py:method:: set_default_authorizer(**kwargs)

    

    Sets the default authorizer. This will be used if a websocket connection is made without specifying an authorizer.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/SetDefaultAuthorizer>`_    


    **Request Syntax** 
    ::

      response = client.set_default_authorizer(
          authorizerName='string'
      )
    :type authorizerName: string
    :param authorizerName: **[REQUIRED]** 

      The authorizer name.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'authorizerName': 'string',
            'authorizerArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **authorizerName** *(string) --* 

          The authorizer name.

          
        

        - **authorizerArn** *(string) --* 

          The authorizer ARN.

          
    

  .. py:method:: set_default_policy_version(**kwargs)

    

    Sets the specified version of the specified policy as the policy's default (operative) version. This action affects all certificates to which the policy is attached. To list the principals the policy is attached to, use the ListPrincipalPolicy API.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/SetDefaultPolicyVersion>`_    


    **Request Syntax** 
    ::

      response = client.set_default_policy_version(
          policyName='string',
          policyVersionId='string'
      )
    :type policyName: string
    :param policyName: **[REQUIRED]** 

      The policy name.

      

    
    :type policyVersionId: string
    :param policyVersionId: **[REQUIRED]** 

      The policy version ID.

      

    
    
    :returns: None

  .. py:method:: set_logging_options(**kwargs)

    

    Sets the logging options.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/SetLoggingOptions>`_    


    **Request Syntax** 
    ::

      response = client.set_logging_options(
          loggingOptionsPayload={
              'roleArn': 'string',
              'logLevel': 'DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
          }
      )
    :type loggingOptionsPayload: dict
    :param loggingOptionsPayload: **[REQUIRED]** 

      The logging options payload.

      

    
      - **roleArn** *(string) --* **[REQUIRED]** 

        The ARN of the IAM role that grants access.

        

      
      - **logLevel** *(string) --* 

        The log level.

        

      
    
    
    :returns: None

  .. py:method:: set_v2_logging_level(**kwargs)

    

    Sets the logging level.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/SetV2LoggingLevel>`_    


    **Request Syntax** 
    ::

      response = client.set_v2_logging_level(
          logTarget={
              'targetType': 'DEFAULT'|'THING_GROUP',
              'targetName': 'string'
          },
          logLevel='DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED'
      )
    :type logTarget: dict
    :param logTarget: **[REQUIRED]** 

      The log target.

      

    
      - **targetType** *(string) --* **[REQUIRED]** 

        The target type.

        

      
      - **targetName** *(string) --* 

        The target name.

        

      
    
    :type logLevel: string
    :param logLevel: **[REQUIRED]** 

      The log level.

      

    
    
    :returns: None

  .. py:method:: set_v2_logging_options(**kwargs)

    

    Sets the logging options for the V2 logging service.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/SetV2LoggingOptions>`_    


    **Request Syntax** 
    ::

      response = client.set_v2_logging_options(
          roleArn='string',
          defaultLogLevel='DEBUG'|'INFO'|'ERROR'|'WARN'|'DISABLED',
          disableAllLogs=True|False
      )
    :type roleArn: string
    :param roleArn: 

      The role ARN that allows IoT to write to Cloudwatch logs.

      

    
    :type defaultLogLevel: string
    :param defaultLogLevel: 

      The default logging level.

      

    
    :type disableAllLogs: boolean
    :param disableAllLogs: 

      Set to true to disable all logs, otherwise set to false.

      

    
    
    :returns: None

  .. py:method:: start_thing_registration_task(**kwargs)

    

    Creates a bulk thing provisioning task.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/StartThingRegistrationTask>`_    


    **Request Syntax** 
    ::

      response = client.start_thing_registration_task(
          templateBody='string',
          inputFileBucket='string',
          inputFileKey='string',
          roleArn='string'
      )
    :type templateBody: string
    :param templateBody: **[REQUIRED]** 

      The provisioning template.

      

    
    :type inputFileBucket: string
    :param inputFileBucket: **[REQUIRED]** 

      The S3 bucket that contains the input file.

      

    
    :type inputFileKey: string
    :param inputFileKey: **[REQUIRED]** 

      The name of input file within the S3 bucket. This file contains a newline delimited JSON file. Each line contains the parameter values to provision one device (thing).

      

    
    :type roleArn: string
    :param roleArn: **[REQUIRED]** 

      The IAM role ARN that grants permission the input file.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'taskId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **taskId** *(string) --* 

          The bulk thing provisioning task ID.

          
    

  .. py:method:: stop_thing_registration_task(**kwargs)

    

    Cancels a bulk thing provisioning task.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/StopThingRegistrationTask>`_    


    **Request Syntax** 
    ::

      response = client.stop_thing_registration_task(
          taskId='string'
      )
    :type taskId: string
    :param taskId: **[REQUIRED]** 

      The bulk thing provisioning task ID.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: test_authorization(**kwargs)

    

    Test custom authorization.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/TestAuthorization>`_    


    **Request Syntax** 
    ::

      response = client.test_authorization(
          principal='string',
          cognitoIdentityPoolId='string',
          authInfos=[
              {
                  'actionType': 'PUBLISH'|'SUBSCRIBE'|'RECEIVE'|'CONNECT',
                  'resources': [
                      'string',
                  ]
              },
          ],
          clientId='string',
          policyNamesToAdd=[
              'string',
          ],
          policyNamesToSkip=[
              'string',
          ]
      )
    :type principal: string
    :param principal: 

      The principal.

      

    
    :type cognitoIdentityPoolId: string
    :param cognitoIdentityPoolId: 

      The Cognito identity pool ID.

      

    
    :type authInfos: list
    :param authInfos: **[REQUIRED]** 

      A list of authorization info objects. Simulating authorization will create a response for each ``authInfo`` object in the list.

      

    
      - *(dict) --* 

        A collection of authorization information.

        

      
        - **actionType** *(string) --* 

          The type of action for which the principal is being authorized.

          

        
        - **resources** *(list) --* 

          The resources for which the principal is being authorized to perform the specified action.

          

        
          - *(string) --* 

          
      
      
  
    :type clientId: string
    :param clientId: 

      The MQTT client ID.

      

    
    :type policyNamesToAdd: list
    :param policyNamesToAdd: 

      When testing custom authorization, the policies specified here are treated as if they are attached to the principal being authorized.

      

    
      - *(string) --* 

      
  
    :type policyNamesToSkip: list
    :param policyNamesToSkip: 

      When testing custom authorization, the policies specified here are treated as if they are not attached to the principal being authorized.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'authResults': [
                {
                    'authInfo': {
                        'actionType': 'PUBLISH'|'SUBSCRIBE'|'RECEIVE'|'CONNECT',
                        'resources': [
                            'string',
                        ]
                    },
                    'allowed': {
                        'policies': [
                            {
                                'policyName': 'string',
                                'policyArn': 'string'
                            },
                        ]
                    },
                    'denied': {
                        'implicitDeny': {
                            'policies': [
                                {
                                    'policyName': 'string',
                                    'policyArn': 'string'
                                },
                            ]
                        },
                        'explicitDeny': {
                            'policies': [
                                {
                                    'policyName': 'string',
                                    'policyArn': 'string'
                                },
                            ]
                        }
                    },
                    'authDecision': 'ALLOWED'|'EXPLICIT_DENY'|'IMPLICIT_DENY',
                    'missingContextValues': [
                        'string',
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **authResults** *(list) --* 

          The authentication results.

          
          

          - *(dict) --* 

            The authorizer result.

            
            

            - **authInfo** *(dict) --* 

              Authorization information.

              
              

              - **actionType** *(string) --* 

                The type of action for which the principal is being authorized.

                
              

              - **resources** *(list) --* 

                The resources for which the principal is being authorized to perform the specified action.

                
                

                - *(string) --* 
            
          
            

            - **allowed** *(dict) --* 

              The policies and statements that allowed the specified action.

              
              

              - **policies** *(list) --* 

                A list of policies that allowed the authentication.

                
                

                - *(dict) --* 

                  Describes an AWS IoT policy.

                  
                  

                  - **policyName** *(string) --* 

                    The policy name.

                    
                  

                  - **policyArn** *(string) --* 

                    The policy ARN.

                    
              
            
          
            

            - **denied** *(dict) --* 

              The policies and statements that denied the specified action.

              
              

              - **implicitDeny** *(dict) --* 

                Information that implicitly denies the authorization. When a policy doesn't explicitly deny or allow an action on a resource it is considered an implicit deny.

                
                

                - **policies** *(list) --* 

                  Policies that don't contain a matching allow or deny statement for the specified action on the specified resource. 

                  
                  

                  - *(dict) --* 

                    Describes an AWS IoT policy.

                    
                    

                    - **policyName** *(string) --* 

                      The policy name.

                      
                    

                    - **policyArn** *(string) --* 

                      The policy ARN.

                      
                
              
            
              

              - **explicitDeny** *(dict) --* 

                Information that explicitly denies the authorization. 

                
                

                - **policies** *(list) --* 

                  The policies that denied the authorization.

                  
                  

                  - *(dict) --* 

                    Describes an AWS IoT policy.

                    
                    

                    - **policyName** *(string) --* 

                      The policy name.

                      
                    

                    - **policyArn** *(string) --* 

                      The policy ARN.

                      
                
              
            
          
            

            - **authDecision** *(string) --* 

              The final authorization decision of this scenario. Multiple statements are taken into account when determining the authorization decision. An explicit deny statement can override multiple allow statements.

              
            

            - **missingContextValues** *(list) --* 

              Contains any missing context values found while evaluating policy.

              
              

              - *(string) --* 
          
        
      
    

  .. py:method:: test_invoke_authorizer(**kwargs)

    

    Invoke the specified custom authorizer for testing purposes.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/TestInvokeAuthorizer>`_    


    **Request Syntax** 
    ::

      response = client.test_invoke_authorizer(
          authorizerName='string',
          token='string',
          tokenSignature='string'
      )
    :type authorizerName: string
    :param authorizerName: **[REQUIRED]** 

      The custom authorizer name.

      

    
    :type token: string
    :param token: **[REQUIRED]** 

      The token returned by your custom authentication service.

      

    
    :type tokenSignature: string
    :param tokenSignature: **[REQUIRED]** 

      The signature made with the token and your custom authentication service's private key.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'isAuthenticated': True|False,
            'principalId': 'string',
            'policyDocuments': [
                'string',
            ],
            'refreshAfterInSeconds': 123,
            'disconnectAfterInSeconds': 123
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **isAuthenticated** *(boolean) --* 

          True if the token is authenticated, otherwise false.

          
        

        - **principalId** *(string) --* 

          The principal ID.

          
        

        - **policyDocuments** *(list) --* 

          IAM policy documents.

          
          

          - *(string) --* 
      
        

        - **refreshAfterInSeconds** *(integer) --* 

          The number of seconds after which the temporary credentials are refreshed.

          
        

        - **disconnectAfterInSeconds** *(integer) --* 

          The number of seconds after which the connection is terminated.

          
    

  .. py:method:: transfer_certificate(**kwargs)

    

    Transfers the specified certificate to the specified AWS account.

     

    You can cancel the transfer until it is acknowledged by the recipient.

     

    No notification is sent to the transfer destination's account. It is up to the caller to notify the transfer target.

     

    The certificate being transferred must not be in the ACTIVE state. You can use the UpdateCertificate API to deactivate it.

     

    The certificate must not have any policies attached to it. You can use the DetachPrincipalPolicy API to detach them.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/TransferCertificate>`_    


    **Request Syntax** 
    ::

      response = client.transfer_certificate(
          certificateId='string',
          targetAwsAccount='string',
          transferMessage='string'
      )
    :type certificateId: string
    :param certificateId: **[REQUIRED]** 

      The ID of the certificate.

      

    
    :type targetAwsAccount: string
    :param targetAwsAccount: **[REQUIRED]** 

      The AWS account.

      

    
    :type transferMessage: string
    :param transferMessage: 

      The transfer message.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'transferredCertificateArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the TransferCertificate operation.

        
        

        - **transferredCertificateArn** *(string) --* 

          The ARN of the certificate.

          
    

  .. py:method:: update_authorizer(**kwargs)

    

    Updates an authorizer.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateAuthorizer>`_    


    **Request Syntax** 
    ::

      response = client.update_authorizer(
          authorizerName='string',
          authorizerFunctionArn='string',
          tokenKeyName='string',
          tokenSigningPublicKeys={
              'string': 'string'
          },
          status='ACTIVE'|'INACTIVE'
      )
    :type authorizerName: string
    :param authorizerName: **[REQUIRED]** 

      The authorizer name.

      

    
    :type authorizerFunctionArn: string
    :param authorizerFunctionArn: 

      The ARN of the authorizer's Lambda function.

      

    
    :type tokenKeyName: string
    :param tokenKeyName: 

      The key used to extract the token from the HTTP headers. 

      

    
    :type tokenSigningPublicKeys: dict
    :param tokenSigningPublicKeys: 

      The public keys used to verify the token signature.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type status: string
    :param status: 

      The status of the update authorizer request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'authorizerName': 'string',
            'authorizerArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **authorizerName** *(string) --* 

          The authorizer name.

          
        

        - **authorizerArn** *(string) --* 

          The authorizer ARN.

          
    

  .. py:method:: update_ca_certificate(**kwargs)

    

    Updates a registered CA certificate.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateCACertificate>`_    


    **Request Syntax** 
    ::

      response = client.update_ca_certificate(
          certificateId='string',
          newStatus='ACTIVE'|'INACTIVE',
          newAutoRegistrationStatus='ENABLE'|'DISABLE',
          registrationConfig={
              'templateBody': 'string',
              'roleArn': 'string'
          },
          removeAutoRegistration=True|False
      )
    :type certificateId: string
    :param certificateId: **[REQUIRED]** 

      The CA certificate identifier.

      

    
    :type newStatus: string
    :param newStatus: 

      The updated status of the CA certificate.

       

       **Note:** The status value REGISTER_INACTIVE is deprecated and should not be used.

      

    
    :type newAutoRegistrationStatus: string
    :param newAutoRegistrationStatus: 

      The new value for the auto registration status. Valid values are: "ENABLE" or "DISABLE".

      

    
    :type registrationConfig: dict
    :param registrationConfig: 

      Information about the registration configuration.

      

    
      - **templateBody** *(string) --* 

        The template body.

        

      
      - **roleArn** *(string) --* 

        The ARN of the role.

        

      
    
    :type removeAutoRegistration: boolean
    :param removeAutoRegistration: 

      If true, remove auto registration.

      

    
    
    :returns: None

  .. py:method:: update_certificate(**kwargs)

    

    Updates the status of the specified certificate. This operation is idempotent.

     

    Moving a certificate from the ACTIVE state (including REVOKED) will not disconnect currently connected devices, but these devices will be unable to reconnect.

     

    The ACTIVE state is required to authenticate devices connecting to AWS IoT using a certificate.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateCertificate>`_    


    **Request Syntax** 
    ::

      response = client.update_certificate(
          certificateId='string',
          newStatus='ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION'
      )
    :type certificateId: string
    :param certificateId: **[REQUIRED]** 

      The ID of the certificate.

      

    
    :type newStatus: string
    :param newStatus: **[REQUIRED]** 

      The new status.

       

       **Note:** Setting the status to PENDING_TRANSFER will result in an exception being thrown. PENDING_TRANSFER is a status used internally by AWS IoT. It is not intended for developer use.

       

       **Note:** The status value REGISTER_INACTIVE is deprecated and should not be used.

      

    
    
    :returns: None

  .. py:method:: update_event_configurations(**kwargs)

    

    Updates the event configurations.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateEventConfigurations>`_    


    **Request Syntax** 
    ::

      response = client.update_event_configurations(
          eventConfigurations={
              'string': {
                  'Enabled': True|False
              }
          }
      )
    :type eventConfigurations: dict
    :param eventConfigurations: 

      The new event configuration values.

      

    
      - *(string) --* 

      
        - *(dict) --* 

          Configuration.

          

        
          - **Enabled** *(boolean) --* 

            True to enable the configuration.

            

          
        
  

    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: update_indexing_configuration(**kwargs)

    

    Updates the search configuration.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateIndexingConfiguration>`_    


    **Request Syntax** 
    ::

      response = client.update_indexing_configuration(
          thingIndexingConfiguration={
              'thingIndexingMode': 'OFF'|'REGISTRY'|'REGISTRY_AND_SHADOW'
          }
      )
    :type thingIndexingConfiguration: dict
    :param thingIndexingConfiguration: 

      Thing indexing configuration.

      

    
      - **thingIndexingMode** *(string) --* 

        Thing indexing mode. Valid values are: 

         

         
        * REGISTRY – Your thing index will contain only registry data. 
         
        * REGISTRY_AND_SHADOW - Your thing index will contain registry and shadow data. 
         
        * OFF - Thing indexing is disabled. 
         

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: update_role_alias(**kwargs)

    

    Updates a role alias.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateRoleAlias>`_    


    **Request Syntax** 
    ::

      response = client.update_role_alias(
          roleAlias='string',
          roleArn='string',
          credentialDurationSeconds=123
      )
    :type roleAlias: string
    :param roleAlias: **[REQUIRED]** 

      The role alias to update.

      

    
    :type roleArn: string
    :param roleArn: 

      The role ARN.

      

    
    :type credentialDurationSeconds: integer
    :param credentialDurationSeconds: 

      The number of seconds the credential will be valid.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'roleAlias': 'string',
            'roleAliasArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **roleAlias** *(string) --* 

          The role alias.

          
        

        - **roleAliasArn** *(string) --* 

          The role alias ARN.

          
    

  .. py:method:: update_thing(**kwargs)

    

    Updates the data for a thing.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateThing>`_    


    **Request Syntax** 
    ::

      response = client.update_thing(
          thingName='string',
          thingTypeName='string',
          attributePayload={
              'attributes': {
                  'string': 'string'
              },
              'merge': True|False
          },
          expectedVersion=123,
          removeThingType=True|False
      )
    :type thingName: string
    :param thingName: **[REQUIRED]** 

      The name of the thing to update.

      

    
    :type thingTypeName: string
    :param thingTypeName: 

      The name of the thing type.

      

    
    :type attributePayload: dict
    :param attributePayload: 

      A list of thing attributes, a JSON string containing name-value pairs. For example:

       

       ``{\"attributes\":{\"name1\":\"value2\"}}``  

       

      This data is used to add new attributes or update existing attributes.

      

    
      - **attributes** *(dict) --* 

        A JSON string containing up to three key-value pair in JSON format. For example:

         

         ``{\"attributes\":{\"string1\":\"string2\"}}``  

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
      - **merge** *(boolean) --* 

        Specifies whether the list of attributes provided in the ``AttributePayload`` is merged with the attributes stored in the registry, instead of overwriting them.

         

        To remove an attribute, call ``UpdateThing`` with an empty attribute value.

         

        .. note::

           

          The ``merge`` attribute is only valid when calling ``UpdateThing`` .

           

        

      
    
    :type expectedVersion: integer
    :param expectedVersion: 

      The expected version of the thing record in the registry. If the version of the record in the registry does not match the expected version specified in the request, the ``UpdateThing`` request is rejected with a ``VersionConflictException`` .

      

    
    :type removeThingType: boolean
    :param removeThingType: 

      Remove a thing type association. If **true** , the association is removed.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        The output from the UpdateThing operation.

        
    

  .. py:method:: update_thing_group(**kwargs)

    

    Update a thing group.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateThingGroup>`_    


    **Request Syntax** 
    ::

      response = client.update_thing_group(
          thingGroupName='string',
          thingGroupProperties={
              'thingGroupDescription': 'string',
              'attributePayload': {
                  'attributes': {
                      'string': 'string'
                  },
                  'merge': True|False
              }
          },
          expectedVersion=123
      )
    :type thingGroupName: string
    :param thingGroupName: **[REQUIRED]** 

      The thing group to update.

      

    
    :type thingGroupProperties: dict
    :param thingGroupProperties: **[REQUIRED]** 

      The thing group properties.

      

    
      - **thingGroupDescription** *(string) --* 

        The thing group description.

        

      
      - **attributePayload** *(dict) --* 

        The thing group attributes in JSON format.

        

      
        - **attributes** *(dict) --* 

          A JSON string containing up to three key-value pair in JSON format. For example:

           

           ``{\"attributes\":{\"string1\":\"string2\"}}``  

          

        
          - *(string) --* 

          
            - *(string) --* 

            
      
    
        - **merge** *(boolean) --* 

          Specifies whether the list of attributes provided in the ``AttributePayload`` is merged with the attributes stored in the registry, instead of overwriting them.

           

          To remove an attribute, call ``UpdateThing`` with an empty attribute value.

           

          .. note::

             

            The ``merge`` attribute is only valid when calling ``UpdateThing`` .

             

          

        
      
    
    :type expectedVersion: integer
    :param expectedVersion: 

      The expected version of the thing group. If this does not match the version of the thing group being updated, the update will fail.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'version': 123
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **version** *(integer) --* 

          The version of the updated thing group.

          
    

  .. py:method:: update_thing_groups_for_thing(**kwargs)

    

    Updates the groups to which the thing belongs.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/UpdateThingGroupsForThing>`_    


    **Request Syntax** 
    ::

      response = client.update_thing_groups_for_thing(
          thingName='string',
          thingGroupsToAdd=[
              'string',
          ],
          thingGroupsToRemove=[
              'string',
          ]
      )
    :type thingName: string
    :param thingName: 

      The thing whose group memberships will be updated.

      

    
    :type thingGroupsToAdd: list
    :param thingGroupsToAdd: 

      The groups to which the thing will be added.

      

    
      - *(string) --* 

      
  
    :type thingGroupsToRemove: list
    :param thingGroupsToRemove: 

      The groups from which the thing will be removed.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

==========
Paginators
==========


The available paginators are:

* :py:class:`IoT.Paginator.ListCACertificates`


* :py:class:`IoT.Paginator.ListCertificates`


* :py:class:`IoT.Paginator.ListCertificatesByCA`


* :py:class:`IoT.Paginator.ListOutgoingCertificates`


* :py:class:`IoT.Paginator.ListPolicies`


* :py:class:`IoT.Paginator.ListPolicyPrincipals`


* :py:class:`IoT.Paginator.ListPrincipalPolicies`


* :py:class:`IoT.Paginator.ListPrincipalThings`


* :py:class:`IoT.Paginator.ListThingTypes`


* :py:class:`IoT.Paginator.ListThings`


* :py:class:`IoT.Paginator.ListTopicRules`



.. py:class:: IoT.Paginator.ListCACertificates

  ::

    
    paginator = client.get_paginator('list_ca_certificates')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_ca_certificates`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListCACertificates>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          ascendingOrder=True|False,
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type ascendingOrder: boolean
    :param ascendingOrder: 

      Determines the order of the results.

      

    
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
            'certificates': [
                {
                    'certificateArn': 'string',
                    'certificateId': 'string',
                    'status': 'ACTIVE'|'INACTIVE',
                    'creationDate': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the ListCACertificates operation.

        
        

        - **certificates** *(list) --* 

          The CA certificates registered in your AWS account.

          
          

          - *(dict) --* 

            A CA certificate.

            
            

            - **certificateArn** *(string) --* 

              The ARN of the CA certificate.

              
            

            - **certificateId** *(string) --* 

              The ID of the CA certificate.

              
            

            - **status** *(string) --* 

              The status of the CA certificate.

               

              The status value REGISTER_INACTIVE is deprecated and should not be used.

              
            

            - **creationDate** *(datetime) --* 

              The date the CA certificate was created.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: IoT.Paginator.ListCertificates

  ::

    
    paginator = client.get_paginator('list_certificates')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_certificates`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListCertificates>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          ascendingOrder=True|False,
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type ascendingOrder: boolean
    :param ascendingOrder: 

      Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.

      

    
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
            'certificates': [
                {
                    'certificateArn': 'string',
                    'certificateId': 'string',
                    'status': 'ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION',
                    'creationDate': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output of the ListCertificates operation.

        
        

        - **certificates** *(list) --* 

          The descriptions of the certificates.

          
          

          - *(dict) --* 

            Information about a certificate.

            
            

            - **certificateArn** *(string) --* 

              The ARN of the certificate.

              
            

            - **certificateId** *(string) --* 

              The ID of the certificate.

              
            

            - **status** *(string) --* 

              The status of the certificate.

               

              The status value REGISTER_INACTIVE is deprecated and should not be used.

              
            

            - **creationDate** *(datetime) --* 

              The date and time the certificate was created.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: IoT.Paginator.ListCertificatesByCA

  ::

    
    paginator = client.get_paginator('list_certificates_by_ca')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_certificates_by_ca`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListCertificatesByCA>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          caCertificateId='string',
          ascendingOrder=True|False,
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type caCertificateId: string
    :param caCertificateId: **[REQUIRED]** 

      The ID of the CA certificate. This operation will list all registered device certificate that were signed by this CA certificate.

      

    
    :type ascendingOrder: boolean
    :param ascendingOrder: 

      Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.

      

    
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
            'certificates': [
                {
                    'certificateArn': 'string',
                    'certificateId': 'string',
                    'status': 'ACTIVE'|'INACTIVE'|'REVOKED'|'PENDING_TRANSFER'|'REGISTER_INACTIVE'|'PENDING_ACTIVATION',
                    'creationDate': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output of the ListCertificatesByCA operation.

        
        

        - **certificates** *(list) --* 

          The device certificates signed by the specified CA certificate.

          
          

          - *(dict) --* 

            Information about a certificate.

            
            

            - **certificateArn** *(string) --* 

              The ARN of the certificate.

              
            

            - **certificateId** *(string) --* 

              The ID of the certificate.

              
            

            - **status** *(string) --* 

              The status of the certificate.

               

              The status value REGISTER_INACTIVE is deprecated and should not be used.

              
            

            - **creationDate** *(datetime) --* 

              The date and time the certificate was created.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: IoT.Paginator.ListOutgoingCertificates

  ::

    
    paginator = client.get_paginator('list_outgoing_certificates')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_outgoing_certificates`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListOutgoingCertificates>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          ascendingOrder=True|False,
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type ascendingOrder: boolean
    :param ascendingOrder: 

      Specifies the order for results. If True, the results are returned in ascending order, based on the creation date.

      

    
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
            'outgoingCertificates': [
                {
                    'certificateArn': 'string',
                    'certificateId': 'string',
                    'transferredTo': 'string',
                    'transferDate': datetime(2015, 1, 1),
                    'transferMessage': 'string',
                    'creationDate': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the ListOutgoingCertificates operation.

        
        

        - **outgoingCertificates** *(list) --* 

          The certificates that are being transferred but not yet accepted.

          
          

          - *(dict) --* 

            A certificate that has been transferred but not yet accepted.

            
            

            - **certificateArn** *(string) --* 

              The certificate ARN.

              
            

            - **certificateId** *(string) --* 

              The certificate ID.

              
            

            - **transferredTo** *(string) --* 

              The AWS account to which the transfer was made.

              
            

            - **transferDate** *(datetime) --* 

              The date the transfer was initiated.

              
            

            - **transferMessage** *(string) --* 

              The transfer message.

              
            

            - **creationDate** *(datetime) --* 

              The certificate creation date.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: IoT.Paginator.ListPolicies

  ::

    
    paginator = client.get_paginator('list_policies')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_policies`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListPolicies>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          ascendingOrder=True|False,
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type ascendingOrder: boolean
    :param ascendingOrder: 

      Specifies the order for results. If true, the results are returned in ascending creation order.

      

    
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
            'policies': [
                {
                    'policyName': 'string',
                    'policyArn': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the ListPolicies operation.

        
        

        - **policies** *(list) --* 

          The descriptions of the policies.

          
          

          - *(dict) --* 

            Describes an AWS IoT policy.

            
            

            - **policyName** *(string) --* 

              The policy name.

              
            

            - **policyArn** *(string) --* 

              The policy ARN.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: IoT.Paginator.ListPolicyPrincipals

  ::

    
    paginator = client.get_paginator('list_policy_principals')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_policy_principals`.

    .. danger::

            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.


    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListPolicyPrincipals>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          policyName='string',
          ascendingOrder=True|False,
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type policyName: string
    :param policyName: **[REQUIRED]** 

      The policy name.

      

    
    :type ascendingOrder: boolean
    :param ascendingOrder: 

      Specifies the order for results. If true, the results are returned in ascending creation order.

      

    
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
            'principals': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the ListPolicyPrincipals operation.

        
        

        - **principals** *(list) --* 

          The descriptions of the principals.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: IoT.Paginator.ListPrincipalPolicies

  ::

    
    paginator = client.get_paginator('list_principal_policies')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_principal_policies`.

    .. danger::

            This operation is deprecated and may not function as expected. This operation should not be used going forward and is only kept for the purpose of backwards compatiblity.


    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListPrincipalPolicies>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          principal='string',
          ascendingOrder=True|False,
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type principal: string
    :param principal: **[REQUIRED]** 

      The principal.

      

    
    :type ascendingOrder: boolean
    :param ascendingOrder: 

      Specifies the order for results. If true, results are returned in ascending creation order.

      

    
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
            'policies': [
                {
                    'policyName': 'string',
                    'policyArn': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the ListPrincipalPolicies operation.

        
        

        - **policies** *(list) --* 

          The policies.

          
          

          - *(dict) --* 

            Describes an AWS IoT policy.

            
            

            - **policyName** *(string) --* 

              The policy name.

              
            

            - **policyArn** *(string) --* 

              The policy ARN.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: IoT.Paginator.ListPrincipalThings

  ::

    
    paginator = client.get_paginator('list_principal_things')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_principal_things`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListPrincipalThings>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          principal='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type principal: string
    :param principal: **[REQUIRED]** 

      The principal.

      

    
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
            'things': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the ListPrincipalThings operation.

        
        

        - **things** *(list) --* 

          The things.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: IoT.Paginator.ListThingTypes

  ::

    
    paginator = client.get_paginator('list_thing_types')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_thing_types`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThingTypes>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          thingTypeName='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type thingTypeName: string
    :param thingTypeName: 

      The name of the thing type.

      

    
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
            'thingTypes': [
                {
                    'thingTypeName': 'string',
                    'thingTypeArn': 'string',
                    'thingTypeProperties': {
                        'thingTypeDescription': 'string',
                        'searchableAttributes': [
                            'string',
                        ]
                    },
                    'thingTypeMetadata': {
                        'deprecated': True|False,
                        'deprecationDate': datetime(2015, 1, 1),
                        'creationDate': datetime(2015, 1, 1)
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output for the ListThingTypes operation.

        
        

        - **thingTypes** *(list) --* 

          The thing types.

          
          

          - *(dict) --* 

            The definition of the thing type, including thing type name and description.

            
            

            - **thingTypeName** *(string) --* 

              The name of the thing type.

              
            

            - **thingTypeArn** *(string) --* 

              The thing type ARN.

              
            

            - **thingTypeProperties** *(dict) --* 

              The ThingTypeProperties for the thing type.

              
              

              - **thingTypeDescription** *(string) --* 

                The description of the thing type.

                
              

              - **searchableAttributes** *(list) --* 

                A list of searchable thing attribute names.

                
                

                - *(string) --* 
            
          
            

            - **thingTypeMetadata** *(dict) --* 

              The ThingTypeMetadata contains additional information about the thing type including: creation date and time, a value indicating whether the thing type is deprecated, and a date and time when it was deprecated.

              
              

              - **deprecated** *(boolean) --* 

                Whether the thing type is deprecated. If **true** , no new things could be associated with this type.

                
              

              - **deprecationDate** *(datetime) --* 

                The date and time when the thing type was deprecated.

                
              

              - **creationDate** *(datetime) --* 

                The date and time when the thing type was created.

                
          
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: IoT.Paginator.ListThings

  ::

    
    paginator = client.get_paginator('list_things')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_things`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListThings>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          attributeName='string',
          attributeValue='string',
          thingTypeName='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type attributeName: string
    :param attributeName: 

      The attribute name used to search for things.

      

    
    :type attributeValue: string
    :param attributeValue: 

      The attribute value used to search for things.

      

    
    :type thingTypeName: string
    :param thingTypeName: 

      The name of the thing type used to search for things.

      

    
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
            'things': [
                {
                    'thingName': 'string',
                    'thingTypeName': 'string',
                    'thingArn': 'string',
                    'attributes': {
                        'string': 'string'
                    },
                    'version': 123
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the ListThings operation.

        
        

        - **things** *(list) --* 

          The things.

          
          

          - *(dict) --* 

            The properties of the thing, including thing name, thing type name, and a list of thing attributes.

            
            

            - **thingName** *(string) --* 

              The name of the thing.

              
            

            - **thingTypeName** *(string) --* 

              The name of the thing type, if the thing has been associated with a type.

              
            

            - **thingArn** *(string) --* 

              The thing ARN.

              
            

            - **attributes** *(dict) --* 

              A list of thing attributes which are name-value pairs.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **version** *(integer) --* 

              The version of the thing record in the registry.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: IoT.Paginator.ListTopicRules

  ::

    
    paginator = client.get_paginator('list_topic_rules')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`IoT.Client.list_topic_rules`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListTopicRules>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          topic='string',
          ruleDisabled=True|False,
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type topic: string
    :param topic: 

      The topic.

      

    
    :type ruleDisabled: boolean
    :param ruleDisabled: 

      Specifies whether the rule is disabled.

      

    
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
            'rules': [
                {
                    'ruleArn': 'string',
                    'ruleName': 'string',
                    'topicPattern': 'string',
                    'createdAt': datetime(2015, 1, 1),
                    'ruleDisabled': True|False
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the ListTopicRules operation.

        
        

        - **rules** *(list) --* 

          The rules.

          
          

          - *(dict) --* 

            Describes a rule.

            
            

            - **ruleArn** *(string) --* 

              The rule ARN.

              
            

            - **ruleName** *(string) --* 

              The name of the rule.

              
            

            - **topicPattern** *(string) --* 

              The pattern for the topic names that apply.

              
            

            - **createdAt** *(datetime) --* 

              The date and time the rule was created.

              
            

            - **ruleDisabled** *(boolean) --* 

              Specifies whether the rule is disabled.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    