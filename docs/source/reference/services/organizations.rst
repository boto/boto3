

*************
Organizations
*************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: Organizations.Client

  A low-level client representing AWS Organizations::

    
    import boto3
    
    client = boto3.client('organizations')

  
  These are the available methods:
  
  *   :py:meth:`~Organizations.Client.accept_handshake`

  
  *   :py:meth:`~Organizations.Client.attach_policy`

  
  *   :py:meth:`~Organizations.Client.can_paginate`

  
  *   :py:meth:`~Organizations.Client.cancel_handshake`

  
  *   :py:meth:`~Organizations.Client.create_account`

  
  *   :py:meth:`~Organizations.Client.create_organization`

  
  *   :py:meth:`~Organizations.Client.create_organizational_unit`

  
  *   :py:meth:`~Organizations.Client.create_policy`

  
  *   :py:meth:`~Organizations.Client.decline_handshake`

  
  *   :py:meth:`~Organizations.Client.delete_organization`

  
  *   :py:meth:`~Organizations.Client.delete_organizational_unit`

  
  *   :py:meth:`~Organizations.Client.delete_policy`

  
  *   :py:meth:`~Organizations.Client.describe_account`

  
  *   :py:meth:`~Organizations.Client.describe_create_account_status`

  
  *   :py:meth:`~Organizations.Client.describe_handshake`

  
  *   :py:meth:`~Organizations.Client.describe_organization`

  
  *   :py:meth:`~Organizations.Client.describe_organizational_unit`

  
  *   :py:meth:`~Organizations.Client.describe_policy`

  
  *   :py:meth:`~Organizations.Client.detach_policy`

  
  *   :py:meth:`~Organizations.Client.disable_aws_service_access`

  
  *   :py:meth:`~Organizations.Client.disable_policy_type`

  
  *   :py:meth:`~Organizations.Client.enable_all_features`

  
  *   :py:meth:`~Organizations.Client.enable_aws_service_access`

  
  *   :py:meth:`~Organizations.Client.enable_policy_type`

  
  *   :py:meth:`~Organizations.Client.generate_presigned_url`

  
  *   :py:meth:`~Organizations.Client.get_paginator`

  
  *   :py:meth:`~Organizations.Client.get_waiter`

  
  *   :py:meth:`~Organizations.Client.invite_account_to_organization`

  
  *   :py:meth:`~Organizations.Client.leave_organization`

  
  *   :py:meth:`~Organizations.Client.list_accounts`

  
  *   :py:meth:`~Organizations.Client.list_accounts_for_parent`

  
  *   :py:meth:`~Organizations.Client.list_aws_service_access_for_organization`

  
  *   :py:meth:`~Organizations.Client.list_children`

  
  *   :py:meth:`~Organizations.Client.list_create_account_status`

  
  *   :py:meth:`~Organizations.Client.list_handshakes_for_account`

  
  *   :py:meth:`~Organizations.Client.list_handshakes_for_organization`

  
  *   :py:meth:`~Organizations.Client.list_organizational_units_for_parent`

  
  *   :py:meth:`~Organizations.Client.list_parents`

  
  *   :py:meth:`~Organizations.Client.list_policies`

  
  *   :py:meth:`~Organizations.Client.list_policies_for_target`

  
  *   :py:meth:`~Organizations.Client.list_roots`

  
  *   :py:meth:`~Organizations.Client.list_targets_for_policy`

  
  *   :py:meth:`~Organizations.Client.move_account`

  
  *   :py:meth:`~Organizations.Client.remove_account_from_organization`

  
  *   :py:meth:`~Organizations.Client.update_organizational_unit`

  
  *   :py:meth:`~Organizations.Client.update_policy`

  

  .. py:method:: accept_handshake(**kwargs)

    

    Sends a response to the originator of a handshake agreeing to the action proposed by the handshake request. 

     

    This operation can be called only by the following principals when they also have the relevant IAM permissions:

     

     
    * **Invitation to join** or **Approve all features request** handshakes: only a principal from the member account.  The user who calls the API for an invitation to join must have the ``organizations:AcceptHandshake`` permission. If you enabled all features in the organization, then the user must also have the ``iam:CreateServiceLinkedRole`` permission so that Organizations can create the required service-linked role named *OrgsServiceLinkedRoleName* . For more information, see `AWS Organizations and Service-Linked Roles <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_integration_services.html#orgs_integration_service-linked-roles>`__ in the *AWS Organizations User Guide* . 
     
    * **Enable all features final confirmation** handshake: only a principal from the master account. For more information about invitations, see `Inviting an AWS Account to Join Your Organization <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html>`__ in the *AWS Organizations User Guide* . For more information about requests to enable all features in the organization, see `Enabling All Features in Your Organization <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html>`__ in the *AWS Organizations User Guide* . 
     

     

    After you accept a handshake, it continues to appear in the results of relevant APIs for only 30 days. After that it is deleted.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/AcceptHandshake>`_    


    **Request Syntax** 
    ::

      response = client.accept_handshake(
          HandshakeId='string'
      )
    :type HandshakeId: string
    :param HandshakeId: **[REQUIRED]** 

      The unique identifier (ID) of the handshake that you want to accept.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Handshake': {
                'Id': 'string',
                'Arn': 'string',
                'Parties': [
                    {
                        'Id': 'string',
                        'Type': 'ACCOUNT'|'ORGANIZATION'|'EMAIL'
                    },
                ],
                'State': 'REQUESTED'|'OPEN'|'CANCELED'|'ACCEPTED'|'DECLINED'|'EXPIRED',
                'RequestedTimestamp': datetime(2015, 1, 1),
                'ExpirationTimestamp': datetime(2015, 1, 1),
                'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
                'Resources': [
                    {
                        'Value': 'string',
                        'Type': 'ACCOUNT'|'ORGANIZATION'|'ORGANIZATION_FEATURE_SET'|'EMAIL'|'MASTER_EMAIL'|'MASTER_NAME'|'NOTES'|'PARENT_HANDSHAKE',
                        'Resources': {'... recursive ...'}
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Handshake** *(dict) --* 

          A structure that contains details about the accepted handshake.

          
          

          - **Id** *(string) --* 

            The unique identifier (ID) of a handshake. The originating account creates the ID when it initiates the handshake.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

            
          

          - **Arn** *(string) --* 

            The Amazon Resource Name (ARN) of a handshake.

             

            For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

            
          

          - **Parties** *(list) --* 

            Information about the two accounts that are participating in the handshake.

            
            

            - *(dict) --* 

              Identifies a participant in a handshake.

              
              

              - **Id** *(string) --* 

                The unique identifier (ID) for the party.

                 

                The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

                
              

              - **Type** *(string) --* 

                The type of party.

                
          
        
          

          - **State** *(string) --* 

            The current state of the handshake. Use the state to trace the flow of the handshake through the process from its creation to its acceptance. The meaning of each of the valid values is as follows:

             

             
            * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some handshake types) and not all recipients have responded yet. The request stays in this state until all recipients respond. 
             
            * **OPEN** : This handshake was sent to multiple recipients (applicable to only some policy types) and all recipients have responded, allowing the originator to complete the handshake action. 
             
            * **CANCELED** : This handshake is no longer active because it was canceled by the originating account. 
             
            * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient. 
             
            * **DECLINED** : This handshake is no longer active because it was declined by the recipient account. 
             
            * **EXPIRED** : This handshake is no longer active because the originator did not receive a response of any kind from the recipient before the expiration time (15 days). 
             

            
          

          - **RequestedTimestamp** *(datetime) --* 

            The date and time that the handshake request was made.

            
          

          - **ExpirationTimestamp** *(datetime) --* 

            The date and time that the handshake expires. If the recipient of the handshake request fails to respond before the specified date and time, the handshake becomes inactive and is no longer valid.

            
          

          - **Action** *(string) --* 

            The type of handshake, indicating what action occurs when the recipient accepts the handshake. The following handshake types are supported:

             

             
            * **INVITE** : This type of handshake represents a request to join an organization. It is always sent from the master account to only non-member accounts. 
             
            * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all features in an organization. It is always sent from the master account to only *invited* member accounts. Created accounts do not receive this because those accounts were created by the organization's master account and approval is inferred. 
             
            * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations service when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It is sent only to the master account and signals the master that it can finalize the process to enable all features. 
             

            
          

          - **Resources** *(list) --* 

            Additional information that is needed to process the handshake.

            
            

            - *(dict) --* 

              Contains additional data that is needed to process a handshake.

              
              

              - **Value** *(string) --* 

                The information that is passed to the other party in the handshake. The format of the value string must match the requirements of the specified type.

                
              

              - **Type** *(string) --* 

                The type of information being passed, specifying how the value is to be interpreted by the other party:

                 

                 
                * ``ACCOUNT`` - Specifies an AWS account ID number. 
                 
                * ``ORGANIZATION`` - Specifies an organization ID number. 
                 
                * ``EMAIL`` - Specifies the email address that is associated with the account that receives the handshake.  
                 
                * ``OWNER_EMAIL`` - Specifies the email address associated with the master account. Included as information about an organization.  
                 
                * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as information about an organization.  
                 
                * ``NOTES`` - Additional text provided by the handshake initiator and intended for the recipient to read. 
                 

                
              

              - **Resources** *(list) --* 

                When needed, contains an additional array of ``HandshakeResource`` objects.

                
          
        
      
    

  .. py:method:: attach_policy(**kwargs)

    

    Attaches a policy to a root, an organizational unit, or an individual account. How the policy affects accounts depends on the type of policy:

     

     
    * **Service control policy (SCP)** - An SCP specifies what permissions can be delegated to users in affected member accounts. The scope of influence for a policy depends on what you attach the policy to: 

       
      * If you attach an SCP to a root, it affects all accounts in the organization. 
       
      * If you attach an SCP to an OU, it affects all accounts in that OU and in any child OUs. 
       
      * If you attach the policy directly to an account, then it affects only that account. 
       

     

    SCPs essentially are permission "filters". When you attach one SCP to a higher level root or OU, and you also attach a different SCP to a child OU or to an account, the child policy can further restrict only the permissions that pass through the parent filter and are available to the child. An SCP that is attached to a child cannot grant a permission that is not already granted by the parent. For example, imagine that the parent SCP allows permissions A, B, C, D, and E. The child SCP allows C, D, E, F, and G. The result is that the accounts affected by the child SCP are allowed to use only C, D, and E. They cannot use A or B because they were filtered out by the child OU. They also cannot use F and G because they were filtered out by the parent OU. They cannot be granted back by the child SCP; child SCPs can only filter the permissions they receive from the parent SCP.

     

    AWS Organizations attaches a default SCP named ``"FullAWSAccess`` to every root, OU, and account. This default SCP allows all services and actions, enabling any new child OU or account to inherit the permissions of the parent root or OU. If you detach the default policy, you must replace it with a policy that specifies the permissions that you want to allow in that OU or account.

     

    For more information about how Organizations policies permissions work, see `Using Service Control Policies <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html>`__ in the *AWS Organizations User Guide* .

     
     

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/AttachPolicy>`_    


    **Request Syntax** 
    ::

      response = client.attach_policy(
          PolicyId='string',
          TargetId='string'
      )
    :type PolicyId: string
    :param PolicyId: **[REQUIRED]** 

      The unique identifier (ID) of the policy that you want to attach to the target. You can get the ID for the policy by calling the  ListPolicies operation.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires "p-" followed by from 8 to 128 lower-case letters or digits.

      

    
    :type TargetId: string
    :param TargetId: **[REQUIRED]** 

      The unique identifier (ID) of the root, OU, or account that you want to attach the policy to. You can get the ID by calling the  ListRoots ,  ListOrganizationalUnitsForParent , or  ListAccounts operations.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a target ID string requires one of the following:

       

       
      * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits. 
       
      * Account: a string that consists of exactly 12 digits. 
       
      * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits. 
       

      

    
    
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


  .. py:method:: cancel_handshake(**kwargs)

    

    Cancels a handshake. Canceling a handshake sets the handshake state to ``CANCELED`` . 

     

    This operation can be called only from the account that originated the handshake. The recipient of the handshake can't cancel it, but can use  DeclineHandshake instead. After a handshake is canceled, the recipient can no longer respond to that handshake.

     

    After you cancel a handshake, it continues to appear in the results of relevant APIs for only 30 days. After that it is deleted.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/CancelHandshake>`_    


    **Request Syntax** 
    ::

      response = client.cancel_handshake(
          HandshakeId='string'
      )
    :type HandshakeId: string
    :param HandshakeId: **[REQUIRED]** 

      The unique identifier (ID) of the handshake that you want to cancel. You can get the ID from the  ListHandshakesForOrganization operation.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Handshake': {
                'Id': 'string',
                'Arn': 'string',
                'Parties': [
                    {
                        'Id': 'string',
                        'Type': 'ACCOUNT'|'ORGANIZATION'|'EMAIL'
                    },
                ],
                'State': 'REQUESTED'|'OPEN'|'CANCELED'|'ACCEPTED'|'DECLINED'|'EXPIRED',
                'RequestedTimestamp': datetime(2015, 1, 1),
                'ExpirationTimestamp': datetime(2015, 1, 1),
                'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
                'Resources': [
                    {
                        'Value': 'string',
                        'Type': 'ACCOUNT'|'ORGANIZATION'|'ORGANIZATION_FEATURE_SET'|'EMAIL'|'MASTER_EMAIL'|'MASTER_NAME'|'NOTES'|'PARENT_HANDSHAKE',
                        'Resources': {'... recursive ...'}
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Handshake** *(dict) --* 

          A structure that contains details about the handshake that you canceled.

          
          

          - **Id** *(string) --* 

            The unique identifier (ID) of a handshake. The originating account creates the ID when it initiates the handshake.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

            
          

          - **Arn** *(string) --* 

            The Amazon Resource Name (ARN) of a handshake.

             

            For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

            
          

          - **Parties** *(list) --* 

            Information about the two accounts that are participating in the handshake.

            
            

            - *(dict) --* 

              Identifies a participant in a handshake.

              
              

              - **Id** *(string) --* 

                The unique identifier (ID) for the party.

                 

                The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

                
              

              - **Type** *(string) --* 

                The type of party.

                
          
        
          

          - **State** *(string) --* 

            The current state of the handshake. Use the state to trace the flow of the handshake through the process from its creation to its acceptance. The meaning of each of the valid values is as follows:

             

             
            * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some handshake types) and not all recipients have responded yet. The request stays in this state until all recipients respond. 
             
            * **OPEN** : This handshake was sent to multiple recipients (applicable to only some policy types) and all recipients have responded, allowing the originator to complete the handshake action. 
             
            * **CANCELED** : This handshake is no longer active because it was canceled by the originating account. 
             
            * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient. 
             
            * **DECLINED** : This handshake is no longer active because it was declined by the recipient account. 
             
            * **EXPIRED** : This handshake is no longer active because the originator did not receive a response of any kind from the recipient before the expiration time (15 days). 
             

            
          

          - **RequestedTimestamp** *(datetime) --* 

            The date and time that the handshake request was made.

            
          

          - **ExpirationTimestamp** *(datetime) --* 

            The date and time that the handshake expires. If the recipient of the handshake request fails to respond before the specified date and time, the handshake becomes inactive and is no longer valid.

            
          

          - **Action** *(string) --* 

            The type of handshake, indicating what action occurs when the recipient accepts the handshake. The following handshake types are supported:

             

             
            * **INVITE** : This type of handshake represents a request to join an organization. It is always sent from the master account to only non-member accounts. 
             
            * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all features in an organization. It is always sent from the master account to only *invited* member accounts. Created accounts do not receive this because those accounts were created by the organization's master account and approval is inferred. 
             
            * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations service when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It is sent only to the master account and signals the master that it can finalize the process to enable all features. 
             

            
          

          - **Resources** *(list) --* 

            Additional information that is needed to process the handshake.

            
            

            - *(dict) --* 

              Contains additional data that is needed to process a handshake.

              
              

              - **Value** *(string) --* 

                The information that is passed to the other party in the handshake. The format of the value string must match the requirements of the specified type.

                
              

              - **Type** *(string) --* 

                The type of information being passed, specifying how the value is to be interpreted by the other party:

                 

                 
                * ``ACCOUNT`` - Specifies an AWS account ID number. 
                 
                * ``ORGANIZATION`` - Specifies an organization ID number. 
                 
                * ``EMAIL`` - Specifies the email address that is associated with the account that receives the handshake.  
                 
                * ``OWNER_EMAIL`` - Specifies the email address associated with the master account. Included as information about an organization.  
                 
                * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as information about an organization.  
                 
                * ``NOTES`` - Additional text provided by the handshake initiator and intended for the recipient to read. 
                 

                
              

              - **Resources** *(list) --* 

                When needed, contains an additional array of ``HandshakeResource`` objects.

                
          
        
      
    

  .. py:method:: create_account(**kwargs)

    

    Creates an AWS account that is automatically a member of the organization whose credentials made the request. This is an asynchronous request that AWS performs in the background. If you want to check the status of the request later, you need the ``OperationId`` response element from this operation to provide as a parameter to the  DescribeCreateAccountStatus operation.

     

    The user who calls the API for an invitation to join must have the ``organizations:CreateAccount`` permission. If you enabled all features in the organization, then the user must also have the ``iam:CreateServiceLinkedRole`` permission so that Organizations can create the required service-linked role named *OrgsServiceLinkedRoleName* . For more information, see `AWS Organizations and Service-Linked Roles <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_integration_services.html#orgs_integration_service-linked-roles>`__ in the *AWS Organizations User Guide* .

     

    The user in the master account who calls this API must also have the ``iam:CreateRole`` permission because AWS Organizations preconfigures the new member account with a role (named ``OrganizationAccountAccessRole`` by default) that grants users in the master account administrator permissions in the new member account. Principals in the master account can assume the role. AWS Organizations clones the company name and address information for the new account from the organization's master account.

     

    This operation can be called only from the organization's master account.

     

    For more information about creating accounts, see `Creating an AWS Account in Your Organization <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html>`__ in the *AWS Organizations User Guide* .

     

    .. warning::

       

      When you create an account in an organization using the AWS Organizations console, API, or CLI commands, the information required for the account to operate as a standalone account, such as a payment method and signing the End User Licence Agreement (EULA) is *not* automatically collected. If you must remove an account from your organization later, you can do so only after you provide the missing information. Follow the steps at `To leave an organization when all required account information has not yet been provided <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html#leave-without-all-info>`__ in the *AWS Organizations User Guide* .

       

     

    .. note::

       

      When you create a member account with this operation, you can choose whether to create the account with the **IAM User and Role Access to Billing Information** switch enabled. If you enable it, IAM users and roles that have appropriate permissions can view billing information for the account. If you disable this, then only the account root user can access billing information. For information about how to disable this for an account, see `Granting Access to Your Billing Information and Tools <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/grantaccess.html>`__ .

       

     

    This operation can be called only from the organization's master account.

     

    .. warning::

       

      If you get an exception that indicates that you exceeded your account limits for the organization or that you can"t add an account because your organization is still initializing, please contact `AWS Customer Support <https://console.aws.amazon.com/support/home#/>`__ .

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/CreateAccount>`_    


    **Request Syntax** 
    ::

      response = client.create_account(
          Email='string',
          AccountName='string',
          RoleName='string',
          IamUserAccessToBilling='ALLOW'|'DENY'
      )
    :type Email: string
    :param Email: **[REQUIRED]** 

      The email address of the owner to assign to the new member account. This email address must not already be associated with another AWS account. You must use a valid email address to complete account creation. You cannot access the root user of the account or remove an account that was created with an invalid email address.

      

    
    :type AccountName: string
    :param AccountName: **[REQUIRED]** 

      The friendly name of the member account.

      

    
    :type RoleName: string
    :param RoleName: 

      (Optional)

       

      The name of an IAM role that Organizations automatically preconfigures in the new member account. This role trusts the master account, allowing users in the master account to assume the role, as permitted by the master account administrator. The role has administrator permissions in the new member account.

       

      If you do not specify this parameter, the role name defaults to ``OrganizationAccountAccessRole`` .

       

      For more information about how to use this role to access the member account, see `Accessing and Administering the Member Accounts in Your Organization <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_access.html#orgs_manage_accounts_create-cross-account-role>`__ in the *AWS Organizations User Guide* , and steps 2 and 3 in `Tutorial\: Delegate Access Across AWS Accounts Using IAM Roles <http://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html>`__ in the *IAM User Guide* .

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of characters that can consist of uppercase letters, lowercase letters, digits with no spaces, and any of the following characters: =,.@-

      

    
    :type IamUserAccessToBilling: string
    :param IamUserAccessToBilling: 

      If set to ``ALLOW`` , the new account enables IAM users to access account billing information *if* they have the required permissions. If set to ``DENY`` , then only the root user of the new account can access account billing information. For more information, see `Activating Access to the Billing and Cost Management Console <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/grantaccess.html#ControllingAccessWebsite-Activate>`__ in the *AWS Billing and Cost Management User Guide* .

       

      If you do not specify this parameter, the value defaults to ALLOW, and IAM users and roles with the required permissions can access billing information for the new account.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CreateAccountStatus': {
                'Id': 'string',
                'AccountName': 'string',
                'State': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
                'RequestedTimestamp': datetime(2015, 1, 1),
                'CompletedTimestamp': datetime(2015, 1, 1),
                'AccountId': 'string',
                'FailureReason': 'ACCOUNT_LIMIT_EXCEEDED'|'EMAIL_ALREADY_EXISTS'|'INVALID_ADDRESS'|'INVALID_EMAIL'|'CONCURRENT_ACCOUNT_MODIFICATION'|'INTERNAL_FAILURE'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CreateAccountStatus** *(dict) --* 

          A structure that contains details about the request to create an account. This response structure might not be fully populated when you first receive it because account creation is an asynchronous process. You can pass the returned CreateAccountStatus ID as a parameter to ``  DescribeCreateAccountStatus `` to get status about the progress of the request at later times. 

          
          

          - **Id** *(string) --* 

            The unique identifier (ID) that references this request. You get this value from the response of the initial  CreateAccount request to create the account.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an create account request ID string requires "car-" followed by from 8 to 32 lower-case letters or digits.

            
          

          - **AccountName** *(string) --* 

            The account name given to the account when it was created.

            
          

          - **State** *(string) --* 

            The status of the request.

            
          

          - **RequestedTimestamp** *(datetime) --* 

            The date and time that the request was made for the account creation.

            
          

          - **CompletedTimestamp** *(datetime) --* 

            The date and time that the account was created and the request completed.

            
          

          - **AccountId** *(string) --* 

            If the account was created successfully, the unique identifier (ID) of the new account.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires exactly 12 digits.

            
          

          - **FailureReason** *(string) --* 

            If the request failed, a description of the reason for the failure.

             

             
            * ACCOUNT_LIMIT_EXCEEDED: The account could not be created because you have reached the limit on the number of accounts in your organization. 
             
            * EMAIL_ALREADY_EXISTS: The account could not be created because another AWS account with that email address already exists. 
             
            * INVALID_ADDRESS: The account could not be created because the address you provided is not valid. 
             
            * INVALID_EMAIL: The account could not be created because the email address you provided is not valid. 
             
            * INTERNAL_FAILURE: The account could not be created because of an internal failure. Try again later. If the problem persists, contact Customer Support. 
             

            
      
    

  .. py:method:: create_organization(**kwargs)

    

    Creates an AWS organization. The account whose user is calling the CreateOrganization operation automatically becomes the `master account <http://docs.aws.amazon.com/IAM/latest/UserGuide/orgs_getting-started_concepts.html#account>`__ of the new organization.

     

    This operation must be called using credentials from the account that is to become the new organization's master account. The principal must also have the relevant IAM permissions.

     

    By default (or if you set the ``FeatureSet`` parameter to ``ALL`` ), the new organization is created with all features enabled and service control policies automatically enabled in the root. If you instead choose to create the organization supporting only the consolidated billing features by setting the ``FeatureSet`` parameter to ``CONSOLIDATED_BILLING"`` , then no policy types are enabled by default and you cannot use organization policies.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/CreateOrganization>`_    


    **Request Syntax** 
    ::

      response = client.create_organization(
          FeatureSet='ALL'|'CONSOLIDATED_BILLING'
      )
    :type FeatureSet: string
    :param FeatureSet: 

      Specifies the feature set supported by the new organization. Each feature set supports different levels of functionality.

       

       
      * *CONSOLIDATED_BILLING* : All member accounts have their bills consolidated to and paid by the master account. For more information, see `Consolidated Billing <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#feature-set-cb-only>`__ in the *AWS Organizations User Guide* . 
       
      * *ALL* : In addition to all the features supported by the consolidated billing feature set, the master account can also apply any type of policy to any member account in the organization. For more information, see `All features <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#feature-set-all>`__ in the *AWS Organizations User Guide* . 
       

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Organization': {
                'Id': 'string',
                'Arn': 'string',
                'FeatureSet': 'ALL'|'CONSOLIDATED_BILLING',
                'MasterAccountArn': 'string',
                'MasterAccountId': 'string',
                'MasterAccountEmail': 'string',
                'AvailablePolicyTypes': [
                    {
                        'Type': 'SERVICE_CONTROL_POLICY',
                        'Status': 'ENABLED'|'PENDING_ENABLE'|'PENDING_DISABLE'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Organization** *(dict) --* 

          A structure that contains details about the newly created organization.

          
          

          - **Id** *(string) --* 

            The unique identifier (ID) of an organization.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organization ID string requires "o-" followed by from 10 to 32 lower-case letters or digits.

            
          

          - **Arn** *(string) --* 

            The Amazon Resource Name (ARN) of an organization.

             

            For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

            
          

          - **FeatureSet** *(string) --* 

            Specifies the functionality that currently is available to the organization. If set to "ALL", then all features are enabled and policies can be applied to accounts in the organization. If set to "CONSOLIDATED_BILLING", then only consolidated billing functionality is available. For more information, see `Enabling All Features in Your Organization <http://docs.aws.amazon.com/IAM/latest/UserGuide/orgs_manage_org_support-all-features.html>`__ in the *AWS Organizations User Guide* .

            
          

          - **MasterAccountArn** *(string) --* 

            The Amazon Resource Name (ARN) of the account that is designated as the master account for the organization.

             

            For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

            
          

          - **MasterAccountId** *(string) --* 

            The unique identifier (ID) of the master account of an organization.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires exactly 12 digits.

            
          

          - **MasterAccountEmail** *(string) --* 

            The email address that is associated with the AWS account that is designated as the master account for the organization.

            
          

          - **AvailablePolicyTypes** *(list) --* 

            A list of policy types that are enabled for this organization. For example, if your organization has all features enabled, then service control policies (SCPs) are included in the list.

            
            

            - *(dict) --* 

              Contains information about a policy type and its status in the associated root.

              
              

              - **Type** *(string) --* 

                The name of the policy type.

                
              

              - **Status** *(string) --* 

                The status of the policy type as it relates to the associated root. To attach a policy of the specified type to a root or to an OU or account in that root, it must be available in the organization and enabled for that root.

                
          
        
      
    

  .. py:method:: create_organizational_unit(**kwargs)

    

    Creates an organizational unit (OU) within a root or parent OU. An OU is a container for accounts that enables you to organize your accounts to apply policies according to your business requirements. The number of levels deep that you can nest OUs is dependent upon the policy types enabled for that root. For service control policies, the limit is five. 

     

    For more information about OUs, see `Managing Organizational Units <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html>`__ in the *AWS Organizations User Guide* .

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/CreateOrganizationalUnit>`_    


    **Request Syntax** 
    ::

      response = client.create_organizational_unit(
          ParentId='string',
          Name='string'
      )
    :type ParentId: string
    :param ParentId: **[REQUIRED]** 

      The unique identifier (ID) of the parent root or OU in which you want to create the new OU.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a parent ID string requires one of the following:

       

       
      * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits. 
       
      * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits. 
       

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      The friendly name to assign to the new OU.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'OrganizationalUnit': {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **OrganizationalUnit** *(dict) --* 

          A structure that contains details about the newly created OU.

          
          

          - **Id** *(string) --* 

            The unique identifier (ID) associated with this OU.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.

            
          

          - **Arn** *(string) --* 

            The Amazon Resource Name (ARN) of this OU.

             

            For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

            
          

          - **Name** *(string) --* 

            The friendly name of this OU.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

            
      
    

  .. py:method:: create_policy(**kwargs)

    

    Creates a policy of a specified type that you can attach to a root, an organizational unit (OU), or an individual AWS account.

     

    For more information about policies and their use, see `Managing Organization Policies <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html>`__ .

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/CreatePolicy>`_    


    **Request Syntax** 
    ::

      response = client.create_policy(
          Content='string',
          Description='string',
          Name='string',
          Type='SERVICE_CONTROL_POLICY'
      )
    :type Content: string
    :param Content: **[REQUIRED]** 

      The policy content to add to the new policy. For example, if you create a `service control policy <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp.html>`__ (SCP), this string must be JSON text that specifies the permissions that admins in attached accounts can delegate to their users, groups, and roles. For more information about the SCP syntax, see `Service Control Policy Syntax <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_scp-syntax.html>`__ in the *AWS Organizations User Guide* .

      

    
    :type Description: string
    :param Description: **[REQUIRED]** 

      An optional description to assign to the policy.

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      The friendly name to assign to the policy.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

      

    
    :type Type: string
    :param Type: **[REQUIRED]** 

      The type of policy to create.

       

      .. note::

         

        In the current release, the only type of policy that you can create is a service control policy (SCP).

         

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Policy': {
                'PolicySummary': {
                    'Id': 'string',
                    'Arn': 'string',
                    'Name': 'string',
                    'Description': 'string',
                    'Type': 'SERVICE_CONTROL_POLICY',
                    'AwsManaged': True|False
                },
                'Content': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Policy** *(dict) --* 

          A structure that contains details about the newly created policy.

          
          

          - **PolicySummary** *(dict) --* 

            A structure that contains additional details about the policy.

            
            

            - **Id** *(string) --* 

              The unique identifier (ID) of the policy.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires "p-" followed by from 8 to 128 lower-case letters or digits.

              
            

            - **Arn** *(string) --* 

              The Amazon Resource Name (ARN) of the policy.

               

              For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

              
            

            - **Name** *(string) --* 

              The friendly name of the policy.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

              
            

            - **Description** *(string) --* 

              The description of the policy.

              
            

            - **Type** *(string) --* 

              The type of policy.

              
            

            - **AwsManaged** *(boolean) --* 

              A boolean value that indicates whether the specified policy is an AWS managed policy. If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.

              
        
          

          - **Content** *(string) --* 

            The text content of the policy.

            
      
    

  .. py:method:: decline_handshake(**kwargs)

    

    Declines a handshake request. This sets the handshake state to ``DECLINED`` and effectively deactivates the request.

     

    This operation can be called only from the account that received the handshake. The originator of the handshake can use  CancelHandshake instead. The originator can't reactivate a declined request, but can re-initiate the process with a new handshake request.

     

    After you decline a handshake, it continues to appear in the results of relevant APIs for only 30 days. After that it is deleted.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/DeclineHandshake>`_    


    **Request Syntax** 
    ::

      response = client.decline_handshake(
          HandshakeId='string'
      )
    :type HandshakeId: string
    :param HandshakeId: **[REQUIRED]** 

      The unique identifier (ID) of the handshake that you want to decline. You can get the ID from the  ListHandshakesForAccount operation.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Handshake': {
                'Id': 'string',
                'Arn': 'string',
                'Parties': [
                    {
                        'Id': 'string',
                        'Type': 'ACCOUNT'|'ORGANIZATION'|'EMAIL'
                    },
                ],
                'State': 'REQUESTED'|'OPEN'|'CANCELED'|'ACCEPTED'|'DECLINED'|'EXPIRED',
                'RequestedTimestamp': datetime(2015, 1, 1),
                'ExpirationTimestamp': datetime(2015, 1, 1),
                'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
                'Resources': [
                    {
                        'Value': 'string',
                        'Type': 'ACCOUNT'|'ORGANIZATION'|'ORGANIZATION_FEATURE_SET'|'EMAIL'|'MASTER_EMAIL'|'MASTER_NAME'|'NOTES'|'PARENT_HANDSHAKE',
                        'Resources': {'... recursive ...'}
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Handshake** *(dict) --* 

          A structure that contains details about the declined handshake. The state is updated to show the value ``DECLINED`` .

          
          

          - **Id** *(string) --* 

            The unique identifier (ID) of a handshake. The originating account creates the ID when it initiates the handshake.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

            
          

          - **Arn** *(string) --* 

            The Amazon Resource Name (ARN) of a handshake.

             

            For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

            
          

          - **Parties** *(list) --* 

            Information about the two accounts that are participating in the handshake.

            
            

            - *(dict) --* 

              Identifies a participant in a handshake.

              
              

              - **Id** *(string) --* 

                The unique identifier (ID) for the party.

                 

                The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

                
              

              - **Type** *(string) --* 

                The type of party.

                
          
        
          

          - **State** *(string) --* 

            The current state of the handshake. Use the state to trace the flow of the handshake through the process from its creation to its acceptance. The meaning of each of the valid values is as follows:

             

             
            * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some handshake types) and not all recipients have responded yet. The request stays in this state until all recipients respond. 
             
            * **OPEN** : This handshake was sent to multiple recipients (applicable to only some policy types) and all recipients have responded, allowing the originator to complete the handshake action. 
             
            * **CANCELED** : This handshake is no longer active because it was canceled by the originating account. 
             
            * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient. 
             
            * **DECLINED** : This handshake is no longer active because it was declined by the recipient account. 
             
            * **EXPIRED** : This handshake is no longer active because the originator did not receive a response of any kind from the recipient before the expiration time (15 days). 
             

            
          

          - **RequestedTimestamp** *(datetime) --* 

            The date and time that the handshake request was made.

            
          

          - **ExpirationTimestamp** *(datetime) --* 

            The date and time that the handshake expires. If the recipient of the handshake request fails to respond before the specified date and time, the handshake becomes inactive and is no longer valid.

            
          

          - **Action** *(string) --* 

            The type of handshake, indicating what action occurs when the recipient accepts the handshake. The following handshake types are supported:

             

             
            * **INVITE** : This type of handshake represents a request to join an organization. It is always sent from the master account to only non-member accounts. 
             
            * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all features in an organization. It is always sent from the master account to only *invited* member accounts. Created accounts do not receive this because those accounts were created by the organization's master account and approval is inferred. 
             
            * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations service when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It is sent only to the master account and signals the master that it can finalize the process to enable all features. 
             

            
          

          - **Resources** *(list) --* 

            Additional information that is needed to process the handshake.

            
            

            - *(dict) --* 

              Contains additional data that is needed to process a handshake.

              
              

              - **Value** *(string) --* 

                The information that is passed to the other party in the handshake. The format of the value string must match the requirements of the specified type.

                
              

              - **Type** *(string) --* 

                The type of information being passed, specifying how the value is to be interpreted by the other party:

                 

                 
                * ``ACCOUNT`` - Specifies an AWS account ID number. 
                 
                * ``ORGANIZATION`` - Specifies an organization ID number. 
                 
                * ``EMAIL`` - Specifies the email address that is associated with the account that receives the handshake.  
                 
                * ``OWNER_EMAIL`` - Specifies the email address associated with the master account. Included as information about an organization.  
                 
                * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as information about an organization.  
                 
                * ``NOTES`` - Additional text provided by the handshake initiator and intended for the recipient to read. 
                 

                
              

              - **Resources** *(list) --* 

                When needed, contains an additional array of ``HandshakeResource`` objects.

                
          
        
      
    

  .. py:method:: delete_organization()

    

    Deletes the organization. You can delete an organization only by using credentials from the master account. The organization must be empty of member accounts, OUs, and policies.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/DeleteOrganization>`_    


    **Request Syntax** 

    ::

      response = client.delete_organization()
    :returns: None

  .. py:method:: delete_organizational_unit(**kwargs)

    

    Deletes an organizational unit from a root or another OU. You must first remove all accounts and child OUs from the OU that you want to delete.

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/DeleteOrganizationalUnit>`_    


    **Request Syntax** 
    ::

      response = client.delete_organizational_unit(
          OrganizationalUnitId='string'
      )
    :type OrganizationalUnitId: string
    :param OrganizationalUnitId: **[REQUIRED]** 

      The unique identifier (ID) of the organizational unit that you want to delete. You can get the ID from the  ListOrganizationalUnitsForParent operation.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.

      

    
    
    :returns: None

  .. py:method:: delete_policy(**kwargs)

    

    Deletes the specified policy from your organization. Before you perform this operation, you must first detach the policy from all OUs, roots, and accounts.

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/DeletePolicy>`_    


    **Request Syntax** 
    ::

      response = client.delete_policy(
          PolicyId='string'
      )
    :type PolicyId: string
    :param PolicyId: **[REQUIRED]** 

      The unique identifier (ID) of the policy that you want to delete. You can get the ID from the  ListPolicies or  ListPoliciesForTarget operations.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires "p-" followed by from 8 to 128 lower-case letters or digits.

      

    
    
    :returns: None

  .. py:method:: describe_account(**kwargs)

    

    Retrieves Organizations-related information about the specified account.

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/DescribeAccount>`_    


    **Request Syntax** 
    ::

      response = client.describe_account(
          AccountId='string'
      )
    :type AccountId: string
    :param AccountId: **[REQUIRED]** 

      The unique identifier (ID) of the AWS account that you want information about. You can get the ID from the  ListAccounts or  ListAccountsForParent operations.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires exactly 12 digits.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Account': {
                'Id': 'string',
                'Arn': 'string',
                'Email': 'string',
                'Name': 'string',
                'Status': 'ACTIVE'|'SUSPENDED',
                'JoinedMethod': 'INVITED'|'CREATED',
                'JoinedTimestamp': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Account** *(dict) --* 

          A structure that contains information about the requested account.

          
          

          - **Id** *(string) --* 

            The unique identifier (ID) of the account.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires exactly 12 digits.

            
          

          - **Arn** *(string) --* 

            The Amazon Resource Name (ARN) of the account.

             

            For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

            
          

          - **Email** *(string) --* 

            The email address associated with the AWS account.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for this parameter is a string of characters that represents a standard Internet email address.

            
          

          - **Name** *(string) --* 

            The friendly name of the account.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

            
          

          - **Status** *(string) --* 

            The status of the account in the organization.

            
          

          - **JoinedMethod** *(string) --* 

            The method by which the account joined the organization.

            
          

          - **JoinedTimestamp** *(datetime) --* 

            The date the account became a part of the organization.

            
      
    

  .. py:method:: describe_create_account_status(**kwargs)

    

    Retrieves the current status of an asynchronous request to create an account.

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/DescribeCreateAccountStatus>`_    


    **Request Syntax** 
    ::

      response = client.describe_create_account_status(
          CreateAccountRequestId='string'
      )
    :type CreateAccountRequestId: string
    :param CreateAccountRequestId: **[REQUIRED]** 

      Specifies the ``operationId`` that uniquely identifies the request. You can get the ID from the response to an earlier  CreateAccount request, or from the  ListCreateAccountStatus operation.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an create account request ID string requires "car-" followed by from 8 to 32 lower-case letters or digits.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CreateAccountStatus': {
                'Id': 'string',
                'AccountName': 'string',
                'State': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
                'RequestedTimestamp': datetime(2015, 1, 1),
                'CompletedTimestamp': datetime(2015, 1, 1),
                'AccountId': 'string',
                'FailureReason': 'ACCOUNT_LIMIT_EXCEEDED'|'EMAIL_ALREADY_EXISTS'|'INVALID_ADDRESS'|'INVALID_EMAIL'|'CONCURRENT_ACCOUNT_MODIFICATION'|'INTERNAL_FAILURE'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CreateAccountStatus** *(dict) --* 

          A structure that contains the current status of an account creation request.

          
          

          - **Id** *(string) --* 

            The unique identifier (ID) that references this request. You get this value from the response of the initial  CreateAccount request to create the account.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an create account request ID string requires "car-" followed by from 8 to 32 lower-case letters or digits.

            
          

          - **AccountName** *(string) --* 

            The account name given to the account when it was created.

            
          

          - **State** *(string) --* 

            The status of the request.

            
          

          - **RequestedTimestamp** *(datetime) --* 

            The date and time that the request was made for the account creation.

            
          

          - **CompletedTimestamp** *(datetime) --* 

            The date and time that the account was created and the request completed.

            
          

          - **AccountId** *(string) --* 

            If the account was created successfully, the unique identifier (ID) of the new account.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires exactly 12 digits.

            
          

          - **FailureReason** *(string) --* 

            If the request failed, a description of the reason for the failure.

             

             
            * ACCOUNT_LIMIT_EXCEEDED: The account could not be created because you have reached the limit on the number of accounts in your organization. 
             
            * EMAIL_ALREADY_EXISTS: The account could not be created because another AWS account with that email address already exists. 
             
            * INVALID_ADDRESS: The account could not be created because the address you provided is not valid. 
             
            * INVALID_EMAIL: The account could not be created because the email address you provided is not valid. 
             
            * INTERNAL_FAILURE: The account could not be created because of an internal failure. Try again later. If the problem persists, contact Customer Support. 
             

            
      
    

  .. py:method:: describe_handshake(**kwargs)

    

    Retrieves information about a previously requested handshake. The handshake ID comes from the response to the original  InviteAccountToOrganization operation that generated the handshake.

     

    You can access handshakes that are ACCEPTED, DECLINED, or CANCELED for only 30 days after they change to that state. They are then deleted and no longer accessible.

     

    This operation can be called from any account in the organization.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/DescribeHandshake>`_    


    **Request Syntax** 
    ::

      response = client.describe_handshake(
          HandshakeId='string'
      )
    :type HandshakeId: string
    :param HandshakeId: **[REQUIRED]** 

      The unique identifier (ID) of the handshake that you want information about. You can get the ID from the original call to  InviteAccountToOrganization , or from a call to  ListHandshakesForAccount or  ListHandshakesForOrganization .

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Handshake': {
                'Id': 'string',
                'Arn': 'string',
                'Parties': [
                    {
                        'Id': 'string',
                        'Type': 'ACCOUNT'|'ORGANIZATION'|'EMAIL'
                    },
                ],
                'State': 'REQUESTED'|'OPEN'|'CANCELED'|'ACCEPTED'|'DECLINED'|'EXPIRED',
                'RequestedTimestamp': datetime(2015, 1, 1),
                'ExpirationTimestamp': datetime(2015, 1, 1),
                'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
                'Resources': [
                    {
                        'Value': 'string',
                        'Type': 'ACCOUNT'|'ORGANIZATION'|'ORGANIZATION_FEATURE_SET'|'EMAIL'|'MASTER_EMAIL'|'MASTER_NAME'|'NOTES'|'PARENT_HANDSHAKE',
                        'Resources': {'... recursive ...'}
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Handshake** *(dict) --* 

          A structure that contains information about the specified handshake.

          
          

          - **Id** *(string) --* 

            The unique identifier (ID) of a handshake. The originating account creates the ID when it initiates the handshake.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

            
          

          - **Arn** *(string) --* 

            The Amazon Resource Name (ARN) of a handshake.

             

            For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

            
          

          - **Parties** *(list) --* 

            Information about the two accounts that are participating in the handshake.

            
            

            - *(dict) --* 

              Identifies a participant in a handshake.

              
              

              - **Id** *(string) --* 

                The unique identifier (ID) for the party.

                 

                The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

                
              

              - **Type** *(string) --* 

                The type of party.

                
          
        
          

          - **State** *(string) --* 

            The current state of the handshake. Use the state to trace the flow of the handshake through the process from its creation to its acceptance. The meaning of each of the valid values is as follows:

             

             
            * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some handshake types) and not all recipients have responded yet. The request stays in this state until all recipients respond. 
             
            * **OPEN** : This handshake was sent to multiple recipients (applicable to only some policy types) and all recipients have responded, allowing the originator to complete the handshake action. 
             
            * **CANCELED** : This handshake is no longer active because it was canceled by the originating account. 
             
            * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient. 
             
            * **DECLINED** : This handshake is no longer active because it was declined by the recipient account. 
             
            * **EXPIRED** : This handshake is no longer active because the originator did not receive a response of any kind from the recipient before the expiration time (15 days). 
             

            
          

          - **RequestedTimestamp** *(datetime) --* 

            The date and time that the handshake request was made.

            
          

          - **ExpirationTimestamp** *(datetime) --* 

            The date and time that the handshake expires. If the recipient of the handshake request fails to respond before the specified date and time, the handshake becomes inactive and is no longer valid.

            
          

          - **Action** *(string) --* 

            The type of handshake, indicating what action occurs when the recipient accepts the handshake. The following handshake types are supported:

             

             
            * **INVITE** : This type of handshake represents a request to join an organization. It is always sent from the master account to only non-member accounts. 
             
            * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all features in an organization. It is always sent from the master account to only *invited* member accounts. Created accounts do not receive this because those accounts were created by the organization's master account and approval is inferred. 
             
            * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations service when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It is sent only to the master account and signals the master that it can finalize the process to enable all features. 
             

            
          

          - **Resources** *(list) --* 

            Additional information that is needed to process the handshake.

            
            

            - *(dict) --* 

              Contains additional data that is needed to process a handshake.

              
              

              - **Value** *(string) --* 

                The information that is passed to the other party in the handshake. The format of the value string must match the requirements of the specified type.

                
              

              - **Type** *(string) --* 

                The type of information being passed, specifying how the value is to be interpreted by the other party:

                 

                 
                * ``ACCOUNT`` - Specifies an AWS account ID number. 
                 
                * ``ORGANIZATION`` - Specifies an organization ID number. 
                 
                * ``EMAIL`` - Specifies the email address that is associated with the account that receives the handshake.  
                 
                * ``OWNER_EMAIL`` - Specifies the email address associated with the master account. Included as information about an organization.  
                 
                * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as information about an organization.  
                 
                * ``NOTES`` - Additional text provided by the handshake initiator and intended for the recipient to read. 
                 

                
              

              - **Resources** *(list) --* 

                When needed, contains an additional array of ``HandshakeResource`` objects.

                
          
        
      
    

  .. py:method:: describe_organization()

    

    Retrieves information about the organization that the user's account belongs to.

     

    This operation can be called from any account in the organization.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/DescribeOrganization>`_    


    **Request Syntax** 

    ::

      response = client.describe_organization()
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Organization': {
                'Id': 'string',
                'Arn': 'string',
                'FeatureSet': 'ALL'|'CONSOLIDATED_BILLING',
                'MasterAccountArn': 'string',
                'MasterAccountId': 'string',
                'MasterAccountEmail': 'string',
                'AvailablePolicyTypes': [
                    {
                        'Type': 'SERVICE_CONTROL_POLICY',
                        'Status': 'ENABLED'|'PENDING_ENABLE'|'PENDING_DISABLE'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Organization** *(dict) --* 

          A structure that contains information about the organization.

          
          

          - **Id** *(string) --* 

            The unique identifier (ID) of an organization.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organization ID string requires "o-" followed by from 10 to 32 lower-case letters or digits.

            
          

          - **Arn** *(string) --* 

            The Amazon Resource Name (ARN) of an organization.

             

            For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

            
          

          - **FeatureSet** *(string) --* 

            Specifies the functionality that currently is available to the organization. If set to "ALL", then all features are enabled and policies can be applied to accounts in the organization. If set to "CONSOLIDATED_BILLING", then only consolidated billing functionality is available. For more information, see `Enabling All Features in Your Organization <http://docs.aws.amazon.com/IAM/latest/UserGuide/orgs_manage_org_support-all-features.html>`__ in the *AWS Organizations User Guide* .

            
          

          - **MasterAccountArn** *(string) --* 

            The Amazon Resource Name (ARN) of the account that is designated as the master account for the organization.

             

            For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

            
          

          - **MasterAccountId** *(string) --* 

            The unique identifier (ID) of the master account of an organization.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires exactly 12 digits.

            
          

          - **MasterAccountEmail** *(string) --* 

            The email address that is associated with the AWS account that is designated as the master account for the organization.

            
          

          - **AvailablePolicyTypes** *(list) --* 

            A list of policy types that are enabled for this organization. For example, if your organization has all features enabled, then service control policies (SCPs) are included in the list.

            
            

            - *(dict) --* 

              Contains information about a policy type and its status in the associated root.

              
              

              - **Type** *(string) --* 

                The name of the policy type.

                
              

              - **Status** *(string) --* 

                The status of the policy type as it relates to the associated root. To attach a policy of the specified type to a root or to an OU or account in that root, it must be available in the organization and enabled for that root.

                
          
        
      
    

  .. py:method:: describe_organizational_unit(**kwargs)

    

    Retrieves information about an organizational unit (OU).

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/DescribeOrganizationalUnit>`_    


    **Request Syntax** 
    ::

      response = client.describe_organizational_unit(
          OrganizationalUnitId='string'
      )
    :type OrganizationalUnitId: string
    :param OrganizationalUnitId: **[REQUIRED]** 

      The unique identifier (ID) of the organizational unit that you want details about. You can get the ID from the  ListOrganizationalUnitsForParent operation.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'OrganizationalUnit': {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **OrganizationalUnit** *(dict) --* 

          A structure that contains details about the specified OU.

          
          

          - **Id** *(string) --* 

            The unique identifier (ID) associated with this OU.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.

            
          

          - **Arn** *(string) --* 

            The Amazon Resource Name (ARN) of this OU.

             

            For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

            
          

          - **Name** *(string) --* 

            The friendly name of this OU.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

            
      
    

  .. py:method:: describe_policy(**kwargs)

    

    Retrieves information about a policy.

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/DescribePolicy>`_    


    **Request Syntax** 
    ::

      response = client.describe_policy(
          PolicyId='string'
      )
    :type PolicyId: string
    :param PolicyId: **[REQUIRED]** 

      The unique identifier (ID) of the policy that you want details about. You can get the ID from the  ListPolicies or  ListPoliciesForTarget operations.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires "p-" followed by from 8 to 128 lower-case letters or digits.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Policy': {
                'PolicySummary': {
                    'Id': 'string',
                    'Arn': 'string',
                    'Name': 'string',
                    'Description': 'string',
                    'Type': 'SERVICE_CONTROL_POLICY',
                    'AwsManaged': True|False
                },
                'Content': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Policy** *(dict) --* 

          A structure that contains details about the specified policy.

          
          

          - **PolicySummary** *(dict) --* 

            A structure that contains additional details about the policy.

            
            

            - **Id** *(string) --* 

              The unique identifier (ID) of the policy.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires "p-" followed by from 8 to 128 lower-case letters or digits.

              
            

            - **Arn** *(string) --* 

              The Amazon Resource Name (ARN) of the policy.

               

              For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

              
            

            - **Name** *(string) --* 

              The friendly name of the policy.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

              
            

            - **Description** *(string) --* 

              The description of the policy.

              
            

            - **Type** *(string) --* 

              The type of policy.

              
            

            - **AwsManaged** *(boolean) --* 

              A boolean value that indicates whether the specified policy is an AWS managed policy. If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.

              
        
          

          - **Content** *(string) --* 

            The text content of the policy.

            
      
    

  .. py:method:: detach_policy(**kwargs)

    

    Detaches a policy from a target root, organizational unit, or account. If the policy being detached is a service control policy (SCP), the changes to permissions for IAM users and roles in affected accounts are immediate.

     

     **Note:** Every root, OU, and account must have at least one SCP attached. If you want to replace the default ``FullAWSAccess`` policy with one that limits the permissions that can be delegated, then you must attach the replacement policy before you can remove the default one. This is the authorization strategy of `whitelisting <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_about-scps.html#orgs_policies_whitelist>`__ . If you instead attach a second SCP and leave the ``FullAWSAccess`` SCP still attached, and specify ``"Effect": "Deny"`` in the second SCP to override the ``"Effect": "Allow"`` in the ``FullAWSAccess`` policy (or any other attached SCP), then you are using the authorization strategy of `blacklisting <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_about-scps.html#orgs_policies_blacklist>`__ . 

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/DetachPolicy>`_    


    **Request Syntax** 
    ::

      response = client.detach_policy(
          PolicyId='string',
          TargetId='string'
      )
    :type PolicyId: string
    :param PolicyId: **[REQUIRED]** 

      The unique identifier (ID) of the policy you want to detach. You can get the ID from the  ListPolicies or  ListPoliciesForTarget operations.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires "p-" followed by from 8 to 128 lower-case letters or digits.

      

    
    :type TargetId: string
    :param TargetId: **[REQUIRED]** 

      The unique identifier (ID) of the root, OU, or account from which you want to detach the policy. You can get the ID from the  ListRoots ,  ListOrganizationalUnitsForParent , or  ListAccounts operations.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a target ID string requires one of the following:

       

       
      * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits. 
       
      * Account: a string that consists of exactly 12 digits. 
       
      * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits. 
       

      

    
    
    :returns: None

  .. py:method:: disable_aws_service_access(**kwargs)

    

    Disables the integration of an AWS service (the service that is specified by ``ServicePrincipal`` ) with AWS Organizations. When you disable integration, the specified service no longer can create a `service-linked role <http://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html>`__ in *new* accounts in your organization. This means the service can't perform operations on your behalf on any new accounts in your organization. The service can still perform operations in older accounts until the service completes its clean-up from AWS Organizations.

     

    

     

    .. warning::

       

      We recommend that you disable integration between AWS Organizations and the specified AWS service by using the console or commands that are provided by the specified service. Doing so ensures that the other service is aware that it can clean up any resources that are required only for the integration. How the service cleans up its resources in the organization's accounts depends on that service. For more information, see the documentation for the other AWS service.

       

     

    After you perform the ``DisableAWSServiceAccess`` operation, the specified service can no longer perform operations in your organization's accounts unless the operations are explicitly permitted by the IAM policies that are attached to your roles. 

     

    For more information about integrating other services with AWS Organizations, including the list of services that work with Organizations, see `Integrating AWS Organizations with Other AWS Services <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html>`__ in the *AWS Organizations User Guide* .

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/DisableAWSServiceAccess>`_    


    **Request Syntax** 
    ::

      response = client.disable_aws_service_access(
          ServicePrincipal='string'
      )
    :type ServicePrincipal: string
    :param ServicePrincipal: **[REQUIRED]** 

      The service principal name of the AWS service for which you want to disable integration with your organization. This is typically in the form of a URL, such as `` *service-abbreviation* .amazonaws.com`` .

      

    
    
    :returns: None

  .. py:method:: disable_policy_type(**kwargs)

    

    Disables an organizational control policy type in a root. A policy of a certain type can be attached to entities in a root only if that type is enabled in the root. After you perform this operation, you no longer can attach policies of the specified type to that root or to any OU or account in that root. You can undo this by using the  EnablePolicyType operation.

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/DisablePolicyType>`_    


    **Request Syntax** 
    ::

      response = client.disable_policy_type(
          RootId='string',
          PolicyType='SERVICE_CONTROL_POLICY'
      )
    :type RootId: string
    :param RootId: **[REQUIRED]** 

      The unique identifier (ID) of the root in which you want to disable a policy type. You can get the ID from the  ListRoots operation.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a root ID string requires "r-" followed by from 4 to 32 lower-case letters or digits.

      

    
    :type PolicyType: string
    :param PolicyType: **[REQUIRED]** 

      The policy type that you want to disable in this root.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Root': {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string',
                'PolicyTypes': [
                    {
                        'Type': 'SERVICE_CONTROL_POLICY',
                        'Status': 'ENABLED'|'PENDING_ENABLE'|'PENDING_DISABLE'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Root** *(dict) --* 

          A structure that shows the root with the updated list of enabled policy types.

          
          

          - **Id** *(string) --* 

            The unique identifier (ID) for the root.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a root ID string requires "r-" followed by from 4 to 32 lower-case letters or digits.

            
          

          - **Arn** *(string) --* 

            The Amazon Resource Name (ARN) of the root.

             

            For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

            
          

          - **Name** *(string) --* 

            The friendly name of the root.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

            
          

          - **PolicyTypes** *(list) --* 

            The types of policies that are currently enabled for the root and therefore can be attached to the root or to its OUs or accounts.

            
            

            - *(dict) --* 

              Contains information about a policy type and its status in the associated root.

              
              

              - **Type** *(string) --* 

                The name of the policy type.

                
              

              - **Status** *(string) --* 

                The status of the policy type as it relates to the associated root. To attach a policy of the specified type to a root or to an OU or account in that root, it must be available in the organization and enabled for that root.

                
          
        
      
    

  .. py:method:: enable_all_features()

    

    Enables all features in an organization. This enables the use of organization policies that can restrict the services and actions that can be called in each account. Until you enable all features, you have access only to consolidated billing, and you can't use any of the advanced account administration features that AWS Organizations supports. For more information, see `Enabling All Features in Your Organization <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html>`__ in the *AWS Organizations User Guide* .

     

    .. warning::

       

      This operation is required only for organizations that were created explicitly with only the consolidated billing features enabled, or that were migrated from a Consolidated Billing account family to Organizations. Calling this operation sends a handshake to every invited account in the organization. The feature set change can be finalized and the additional features enabled only after all administrators in the invited accounts approve the change by accepting the handshake.

       

     

    After all invited member accounts accept the handshake, you finalize the feature set change by accepting the handshake that contains ``"Action": "ENABLE_ALL_FEATURES"`` . This completes the change.

     

    After you enable all features in your organization, the master account in the organization can apply policies on all member accounts. These policies can restrict what users and even administrators in those accounts can do. The master account can apply policies that prevent accounts from leaving the organization. Ensure that your account administrators are aware of this.

     

    This operation can be called only from the organization's master account. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/EnableAllFeatures>`_    


    **Request Syntax** 
    ::

      response = client.enable_all_features()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Handshake': {
                'Id': 'string',
                'Arn': 'string',
                'Parties': [
                    {
                        'Id': 'string',
                        'Type': 'ACCOUNT'|'ORGANIZATION'|'EMAIL'
                    },
                ],
                'State': 'REQUESTED'|'OPEN'|'CANCELED'|'ACCEPTED'|'DECLINED'|'EXPIRED',
                'RequestedTimestamp': datetime(2015, 1, 1),
                'ExpirationTimestamp': datetime(2015, 1, 1),
                'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
                'Resources': [
                    {
                        'Value': 'string',
                        'Type': 'ACCOUNT'|'ORGANIZATION'|'ORGANIZATION_FEATURE_SET'|'EMAIL'|'MASTER_EMAIL'|'MASTER_NAME'|'NOTES'|'PARENT_HANDSHAKE',
                        'Resources': {'... recursive ...'}
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Handshake** *(dict) --* 

          A structure that contains details about the handshake created to support this request to enable all features in the organization.

          
          

          - **Id** *(string) --* 

            The unique identifier (ID) of a handshake. The originating account creates the ID when it initiates the handshake.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

            
          

          - **Arn** *(string) --* 

            The Amazon Resource Name (ARN) of a handshake.

             

            For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

            
          

          - **Parties** *(list) --* 

            Information about the two accounts that are participating in the handshake.

            
            

            - *(dict) --* 

              Identifies a participant in a handshake.

              
              

              - **Id** *(string) --* 

                The unique identifier (ID) for the party.

                 

                The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

                
              

              - **Type** *(string) --* 

                The type of party.

                
          
        
          

          - **State** *(string) --* 

            The current state of the handshake. Use the state to trace the flow of the handshake through the process from its creation to its acceptance. The meaning of each of the valid values is as follows:

             

             
            * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some handshake types) and not all recipients have responded yet. The request stays in this state until all recipients respond. 
             
            * **OPEN** : This handshake was sent to multiple recipients (applicable to only some policy types) and all recipients have responded, allowing the originator to complete the handshake action. 
             
            * **CANCELED** : This handshake is no longer active because it was canceled by the originating account. 
             
            * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient. 
             
            * **DECLINED** : This handshake is no longer active because it was declined by the recipient account. 
             
            * **EXPIRED** : This handshake is no longer active because the originator did not receive a response of any kind from the recipient before the expiration time (15 days). 
             

            
          

          - **RequestedTimestamp** *(datetime) --* 

            The date and time that the handshake request was made.

            
          

          - **ExpirationTimestamp** *(datetime) --* 

            The date and time that the handshake expires. If the recipient of the handshake request fails to respond before the specified date and time, the handshake becomes inactive and is no longer valid.

            
          

          - **Action** *(string) --* 

            The type of handshake, indicating what action occurs when the recipient accepts the handshake. The following handshake types are supported:

             

             
            * **INVITE** : This type of handshake represents a request to join an organization. It is always sent from the master account to only non-member accounts. 
             
            * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all features in an organization. It is always sent from the master account to only *invited* member accounts. Created accounts do not receive this because those accounts were created by the organization's master account and approval is inferred. 
             
            * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations service when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It is sent only to the master account and signals the master that it can finalize the process to enable all features. 
             

            
          

          - **Resources** *(list) --* 

            Additional information that is needed to process the handshake.

            
            

            - *(dict) --* 

              Contains additional data that is needed to process a handshake.

              
              

              - **Value** *(string) --* 

                The information that is passed to the other party in the handshake. The format of the value string must match the requirements of the specified type.

                
              

              - **Type** *(string) --* 

                The type of information being passed, specifying how the value is to be interpreted by the other party:

                 

                 
                * ``ACCOUNT`` - Specifies an AWS account ID number. 
                 
                * ``ORGANIZATION`` - Specifies an organization ID number. 
                 
                * ``EMAIL`` - Specifies the email address that is associated with the account that receives the handshake.  
                 
                * ``OWNER_EMAIL`` - Specifies the email address associated with the master account. Included as information about an organization.  
                 
                * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as information about an organization.  
                 
                * ``NOTES`` - Additional text provided by the handshake initiator and intended for the recipient to read. 
                 

                
              

              - **Resources** *(list) --* 

                When needed, contains an additional array of ``HandshakeResource`` objects.

                
          
        
      
    

  .. py:method:: enable_aws_service_access(**kwargs)

    

    Enables the integration of an AWS service (the service that is specified by ``ServicePrincipal`` ) with AWS Organizations. When you enable integration, you allow the specified service to create a `service-linked role <http://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html>`__ in all the accounts in your organization. This allows the service to perform operations on your behalf in your organization and its accounts.

     

    .. warning::

       

      We recommend that you enable integration between AWS Organizations and the specified AWS service by using the console or commands that are provided by the specified service. Doing so ensures that the service is aware that it can create the resources that are required for the integration. How the service creates those resources in the organization's accounts depends on that service. For more information, see the documentation for the other AWS service.

       

     

    For more information about enabling services to integrate with AWS Organizations, see `Integrating AWS Organizations with Other AWS Services <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html>`__ in the *AWS Organizations User Guide* .

     

    This operation can be called only from the organization's master account and only if the organization has `enabled all features <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/EnableAWSServiceAccess>`_    


    **Request Syntax** 
    ::

      response = client.enable_aws_service_access(
          ServicePrincipal='string'
      )
    :type ServicePrincipal: string
    :param ServicePrincipal: **[REQUIRED]** 

      The service principal name of the AWS service for which you want to enable integration with your organization. This is typically in the form of a URL, such as `` *service-abbreviation* .amazonaws.com`` .

      

    
    
    :returns: None

  .. py:method:: enable_policy_type(**kwargs)

    

    Enables a policy type in a root. After you enable a policy type in a root, you can attach policies of that type to the root, any OU, or account in that root. You can undo this by using the  DisablePolicyType operation.

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/EnablePolicyType>`_    


    **Request Syntax** 
    ::

      response = client.enable_policy_type(
          RootId='string',
          PolicyType='SERVICE_CONTROL_POLICY'
      )
    :type RootId: string
    :param RootId: **[REQUIRED]** 

      The unique identifier (ID) of the root in which you want to enable a policy type. You can get the ID from the  ListRoots operation.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a root ID string requires "r-" followed by from 4 to 32 lower-case letters or digits.

      

    
    :type PolicyType: string
    :param PolicyType: **[REQUIRED]** 

      The policy type that you want to enable.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Root': {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string',
                'PolicyTypes': [
                    {
                        'Type': 'SERVICE_CONTROL_POLICY',
                        'Status': 'ENABLED'|'PENDING_ENABLE'|'PENDING_DISABLE'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Root** *(dict) --* 

          A structure that shows the root with the updated list of enabled policy types.

          
          

          - **Id** *(string) --* 

            The unique identifier (ID) for the root.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a root ID string requires "r-" followed by from 4 to 32 lower-case letters or digits.

            
          

          - **Arn** *(string) --* 

            The Amazon Resource Name (ARN) of the root.

             

            For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

            
          

          - **Name** *(string) --* 

            The friendly name of the root.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

            
          

          - **PolicyTypes** *(list) --* 

            The types of policies that are currently enabled for the root and therefore can be attached to the root or to its OUs or accounts.

            
            

            - *(dict) --* 

              Contains information about a policy type and its status in the associated root.

              
              

              - **Type** *(string) --* 

                The name of the policy type.

                
              

              - **Status** *(string) --* 

                The status of the policy type as it relates to the associated root. To attach a policy of the specified type to a root or to an OU or account in that root, it must be available in the organization and enabled for that root.

                
          
        
      
    

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

        


  .. py:method:: invite_account_to_organization(**kwargs)

    

    Sends an invitation to another account to join your organization as a member account. Organizations sends email on your behalf to the email address that is associated with the other account's owner. The invitation is implemented as a  Handshake whose details are in the response.

     

    .. warning::

       

      You can invite AWS accounts only from the same seller as the master account. For example, if your organization's master account was created by Amazon Internet Services Pvt. Ltd (AISPL), an AWS seller in India, then you can only invite other AISPL accounts to your organization. You can't combine accounts from AISPL and AWS, or any other AWS seller. For more information, see `Consolidated Billing in India <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/useconsolidatedbilliing-India.html>`__ .

       

     

    This operation can be called only from the organization's master account.

     

    .. warning::

       

      If you get an exception that indicates that you exceeded your account limits for the organization or that you can"t add an account because your organization is still initializing, please contact `AWS Customer Support <https://console.aws.amazon.com/support/home#/>`__ .

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/InviteAccountToOrganization>`_    


    **Request Syntax** 
    ::

      response = client.invite_account_to_organization(
          Target={
              'Id': 'string',
              'Type': 'ACCOUNT'|'ORGANIZATION'|'EMAIL'
          },
          Notes='string'
      )
    :type Target: dict
    :param Target: **[REQUIRED]** 

      The identifier (ID) of the AWS account that you want to invite to join your organization. This is a JSON object that contains the following elements: 

       

       ``{ "Type": "ACCOUNT", "Id": "<* **account id number** * >" }``  

       

      If you use the AWS CLI, you can submit this as a single string, similar to the following example:

       

       ``--target Id=123456789012,Type=ACCOUNT``  

       

      If you specify ``"Type": "ACCOUNT"`` , then you must provide the AWS account ID number as the ``Id`` . If you specify ``"Type": "EMAIL"`` , then you must specify the email address that is associated with the account.

       

       ``--target Id=bill@example.com,Type=EMAIL``  

      

    
      - **Id** *(string) --* **[REQUIRED]** 

        The unique identifier (ID) for the party.

         

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

        

      
      - **Type** *(string) --* **[REQUIRED]** 

        The type of party.

        

      
    
    :type Notes: string
    :param Notes: 

      Additional information that you want to include in the generated email to the recipient account owner.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Handshake': {
                'Id': 'string',
                'Arn': 'string',
                'Parties': [
                    {
                        'Id': 'string',
                        'Type': 'ACCOUNT'|'ORGANIZATION'|'EMAIL'
                    },
                ],
                'State': 'REQUESTED'|'OPEN'|'CANCELED'|'ACCEPTED'|'DECLINED'|'EXPIRED',
                'RequestedTimestamp': datetime(2015, 1, 1),
                'ExpirationTimestamp': datetime(2015, 1, 1),
                'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
                'Resources': [
                    {
                        'Value': 'string',
                        'Type': 'ACCOUNT'|'ORGANIZATION'|'ORGANIZATION_FEATURE_SET'|'EMAIL'|'MASTER_EMAIL'|'MASTER_NAME'|'NOTES'|'PARENT_HANDSHAKE',
                        'Resources': {'... recursive ...'}
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Handshake** *(dict) --* 

          A structure that contains details about the handshake that is created to support this invitation request.

          
          

          - **Id** *(string) --* 

            The unique identifier (ID) of a handshake. The originating account creates the ID when it initiates the handshake.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

            
          

          - **Arn** *(string) --* 

            The Amazon Resource Name (ARN) of a handshake.

             

            For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

            
          

          - **Parties** *(list) --* 

            Information about the two accounts that are participating in the handshake.

            
            

            - *(dict) --* 

              Identifies a participant in a handshake.

              
              

              - **Id** *(string) --* 

                The unique identifier (ID) for the party.

                 

                The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

                
              

              - **Type** *(string) --* 

                The type of party.

                
          
        
          

          - **State** *(string) --* 

            The current state of the handshake. Use the state to trace the flow of the handshake through the process from its creation to its acceptance. The meaning of each of the valid values is as follows:

             

             
            * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some handshake types) and not all recipients have responded yet. The request stays in this state until all recipients respond. 
             
            * **OPEN** : This handshake was sent to multiple recipients (applicable to only some policy types) and all recipients have responded, allowing the originator to complete the handshake action. 
             
            * **CANCELED** : This handshake is no longer active because it was canceled by the originating account. 
             
            * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient. 
             
            * **DECLINED** : This handshake is no longer active because it was declined by the recipient account. 
             
            * **EXPIRED** : This handshake is no longer active because the originator did not receive a response of any kind from the recipient before the expiration time (15 days). 
             

            
          

          - **RequestedTimestamp** *(datetime) --* 

            The date and time that the handshake request was made.

            
          

          - **ExpirationTimestamp** *(datetime) --* 

            The date and time that the handshake expires. If the recipient of the handshake request fails to respond before the specified date and time, the handshake becomes inactive and is no longer valid.

            
          

          - **Action** *(string) --* 

            The type of handshake, indicating what action occurs when the recipient accepts the handshake. The following handshake types are supported:

             

             
            * **INVITE** : This type of handshake represents a request to join an organization. It is always sent from the master account to only non-member accounts. 
             
            * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all features in an organization. It is always sent from the master account to only *invited* member accounts. Created accounts do not receive this because those accounts were created by the organization's master account and approval is inferred. 
             
            * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations service when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It is sent only to the master account and signals the master that it can finalize the process to enable all features. 
             

            
          

          - **Resources** *(list) --* 

            Additional information that is needed to process the handshake.

            
            

            - *(dict) --* 

              Contains additional data that is needed to process a handshake.

              
              

              - **Value** *(string) --* 

                The information that is passed to the other party in the handshake. The format of the value string must match the requirements of the specified type.

                
              

              - **Type** *(string) --* 

                The type of information being passed, specifying how the value is to be interpreted by the other party:

                 

                 
                * ``ACCOUNT`` - Specifies an AWS account ID number. 
                 
                * ``ORGANIZATION`` - Specifies an organization ID number. 
                 
                * ``EMAIL`` - Specifies the email address that is associated with the account that receives the handshake.  
                 
                * ``OWNER_EMAIL`` - Specifies the email address associated with the master account. Included as information about an organization.  
                 
                * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as information about an organization.  
                 
                * ``NOTES`` - Additional text provided by the handshake initiator and intended for the recipient to read. 
                 

                
              

              - **Resources** *(list) --* 

                When needed, contains an additional array of ``HandshakeResource`` objects.

                
          
        
      
    

  .. py:method:: leave_organization()

    

    Removes a member account from its parent organization. This version of the operation is performed by the account that wants to leave. To remove a member account as a user in the master account, use  RemoveAccountFromOrganization instead.

     

    This operation can be called only from a member account in the organization.

     

    .. warning::

       

       
      * The master account in an organization with all features enabled can set service control policies (SCPs) that can restrict what administrators of member accounts can do, including preventing them from successfully calling ``LeaveOrganization`` and leaving the organization.  
       
      * You can leave an organization as a member account only if the account is configured with the information required to operate as a standalone account. When you create an account in an organization using the AWS Organizations console, API, or CLI commands, the information required of standalone accounts is *not* automatically collected. For each account that you want to make standalone, you must accept the End User License Agreement (EULA), choose a support plan, provide and verify the required contact information, and provide a current payment method. AWS uses the payment method to charge for any billable (not free tier) AWS activity that occurs while the account is not attached to an organization. Follow the steps at `To leave an organization when all required account information has not yet been provided <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html#leave-without-all-info>`__ in the *AWS Organizations User Guide* . 
       
      * You can leave an organization only after you enable IAM user access to billing in your account. For more information, see `Activating Access to the Billing and Cost Management Console <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/grantaccess.html#ControllingAccessWebsite-Activate>`__ in the *AWS Billing and Cost Management User Guide* . 
       

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/LeaveOrganization>`_    


    **Request Syntax** 

    ::

      response = client.leave_organization()
    :returns: None

  .. py:method:: list_accounts(**kwargs)

    

    Lists all the accounts in the organization. To request only the accounts in a root or OU, use the  ListAccountsForParent operation instead.

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListAccounts>`_    


    **Request Syntax** 
    ::

      response = client.list_accounts(
          NextToken='string',
          MaxResults=123
      )
    :type NextToken: string
    :param NextToken: 

      Use this parameter if you receive a ``NextToken`` response in a previous request that indicates that there is more output available. Set it to the value of the previous call's ``NextToken`` response to indicate where the output should continue from.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      (Optional) Use this to limit the number of results you want included in the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the ``NextToken`` response element is present and has a value (is not null). Include that value as the ``NextToken`` request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check ``NextToken`` after every operation to ensure that you receive all of the results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Accounts': [
                {
                    'Id': 'string',
                    'Arn': 'string',
                    'Email': 'string',
                    'Name': 'string',
                    'Status': 'ACTIVE'|'SUSPENDED',
                    'JoinedMethod': 'INVITED'|'CREATED',
                    'JoinedTimestamp': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Accounts** *(list) --* 

          A list of objects in the organization.

          
          

          - *(dict) --* 

            Contains information about an AWS account that is a member of an organization.

            
            

            - **Id** *(string) --* 

              The unique identifier (ID) of the account.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires exactly 12 digits.

              
            

            - **Arn** *(string) --* 

              The Amazon Resource Name (ARN) of the account.

               

              For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

              
            

            - **Email** *(string) --* 

              The email address associated with the AWS account.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for this parameter is a string of characters that represents a standard Internet email address.

              
            

            - **Name** *(string) --* 

              The friendly name of the account.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

              
            

            - **Status** *(string) --* 

              The status of the account in the organization.

              
            

            - **JoinedMethod** *(string) --* 

              The method by which the account joined the organization.

              
            

            - **JoinedTimestamp** *(datetime) --* 

              The date the account became a part of the organization.

              
        
      
        

        - **NextToken** *(string) --* 

          If present, this value indicates that there is more output available than is included in the current response. Use this value in the ``NextToken`` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the ``NextToken`` response element comes back as ``null`` .

          
    

  .. py:method:: list_accounts_for_parent(**kwargs)

    

    Lists the accounts in an organization that are contained by the specified target root or organizational unit (OU). If you specify the root, you get a list of all the accounts that are not in any OU. If you specify an OU, you get a list of all the accounts in only that OU, and not in any child OUs. To get a list of all accounts in the organization, use the  ListAccounts operation.

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListAccountsForParent>`_    


    **Request Syntax** 
    ::

      response = client.list_accounts_for_parent(
          ParentId='string',
          NextToken='string',
          MaxResults=123
      )
    :type ParentId: string
    :param ParentId: **[REQUIRED]** 

      The unique identifier (ID) for the parent root or organization unit (OU) whose accounts you want to list.

      

    
    :type NextToken: string
    :param NextToken: 

      Use this parameter if you receive a ``NextToken`` response in a previous request that indicates that there is more output available. Set it to the value of the previous call's ``NextToken`` response to indicate where the output should continue from.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      (Optional) Use this to limit the number of results you want included in the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the ``NextToken`` response element is present and has a value (is not null). Include that value as the ``NextToken`` request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check ``NextToken`` after every operation to ensure that you receive all of the results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Accounts': [
                {
                    'Id': 'string',
                    'Arn': 'string',
                    'Email': 'string',
                    'Name': 'string',
                    'Status': 'ACTIVE'|'SUSPENDED',
                    'JoinedMethod': 'INVITED'|'CREATED',
                    'JoinedTimestamp': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Accounts** *(list) --* 

          A list of the accounts in the specified root or OU.

          
          

          - *(dict) --* 

            Contains information about an AWS account that is a member of an organization.

            
            

            - **Id** *(string) --* 

              The unique identifier (ID) of the account.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires exactly 12 digits.

              
            

            - **Arn** *(string) --* 

              The Amazon Resource Name (ARN) of the account.

               

              For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

              
            

            - **Email** *(string) --* 

              The email address associated with the AWS account.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for this parameter is a string of characters that represents a standard Internet email address.

              
            

            - **Name** *(string) --* 

              The friendly name of the account.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

              
            

            - **Status** *(string) --* 

              The status of the account in the organization.

              
            

            - **JoinedMethod** *(string) --* 

              The method by which the account joined the organization.

              
            

            - **JoinedTimestamp** *(datetime) --* 

              The date the account became a part of the organization.

              
        
      
        

        - **NextToken** *(string) --* 

          If present, this value indicates that there is more output available than is included in the current response. Use this value in the ``NextToken`` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the ``NextToken`` response element comes back as ``null`` .

          
    

  .. py:method:: list_aws_service_access_for_organization(**kwargs)

    

    Returns a list of the AWS services that you enabled to integrate with your organization. After a service on this list creates the resources that it requires for the integration, it can perform operations on your organization and its accounts.

     

    For more information about integrating other services with AWS Organizations, including the list of services that currently work with Organizations, see `Integrating AWS Organizations with Other AWS Services <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html>`__ in the *AWS Organizations User Guide* .

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListAWSServiceAccessForOrganization>`_    


    **Request Syntax** 
    ::

      response = client.list_aws_service_access_for_organization(
          NextToken='string',
          MaxResults=123
      )
    :type NextToken: string
    :param NextToken: 

      Use this parameter if you receive a ``NextToken`` response in a previous request that indicates that there is more output available. Set it to the value of the previous call's ``NextToken`` response to indicate where the output should continue from.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      (Optional) Use this to limit the number of results you want included in the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the ``NextToken`` response element is present and has a value (is not null). Include that value as the ``NextToken`` request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check ``NextToken`` after every operation to ensure that you receive all of the results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'EnabledServicePrincipals': [
                {
                    'ServicePrincipal': 'string',
                    'DateEnabled': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **EnabledServicePrincipals** *(list) --* 

          A list of the service principals for the services that are enabled to integrate with your organization. Each principal is a structure that includes the name and the date that it was enabled for integration with AWS Organizations.

          
          

          - *(dict) --* 

            A structure that contains details of a service principal that is enabled to integrate with AWS Organizations.

            
            

            - **ServicePrincipal** *(string) --* 

              The name of the service principal. This is typically in the form of a URL, such as: `` *servicename* .amazonaws.com`` .

              
            

            - **DateEnabled** *(datetime) --* 

              The date that the service principal was enabled for integration with AWS Organizations.

              
        
      
        

        - **NextToken** *(string) --* 

          If present, this value indicates that there is more output available than is included in the current response. Use this value in the ``NextToken`` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the ``NextToken`` response element comes back as ``null`` .

          
    

  .. py:method:: list_children(**kwargs)

    

    Lists all of the OUs or accounts that are contained in the specified parent OU or root. This operation, along with  ListParents enables you to traverse the tree structure that makes up this root.

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListChildren>`_    


    **Request Syntax** 
    ::

      response = client.list_children(
          ParentId='string',
          ChildType='ACCOUNT'|'ORGANIZATIONAL_UNIT',
          NextToken='string',
          MaxResults=123
      )
    :type ParentId: string
    :param ParentId: **[REQUIRED]** 

      The unique identifier (ID) for the parent root or OU whose children you want to list.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a parent ID string requires one of the following:

       

       
      * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits. 
       
      * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits. 
       

      

    
    :type ChildType: string
    :param ChildType: **[REQUIRED]** 

      Filters the output to include only the specified child type.

      

    
    :type NextToken: string
    :param NextToken: 

      Use this parameter if you receive a ``NextToken`` response in a previous request that indicates that there is more output available. Set it to the value of the previous call's ``NextToken`` response to indicate where the output should continue from.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      (Optional) Use this to limit the number of results you want included in the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the ``NextToken`` response element is present and has a value (is not null). Include that value as the ``NextToken`` request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check ``NextToken`` after every operation to ensure that you receive all of the results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Children': [
                {
                    'Id': 'string',
                    'Type': 'ACCOUNT'|'ORGANIZATIONAL_UNIT'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Children** *(list) --* 

          The list of children of the specified parent container.

          
          

          - *(dict) --* 

            Contains a list of child entities, either OUs or accounts.

            
            

            - **Id** *(string) --* 

              The unique identifier (ID) of this child entity.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a child ID string requires one of the following:

               

               
              * Account: a string that consists of exactly 12 digits. 
               
              * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits. 
               

              
            

            - **Type** *(string) --* 

              The type of this child entity.

              
        
      
        

        - **NextToken** *(string) --* 

          If present, this value indicates that there is more output available than is included in the current response. Use this value in the ``NextToken`` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the ``NextToken`` response element comes back as ``null`` .

          
    

  .. py:method:: list_create_account_status(**kwargs)

    

    Lists the account creation requests that match the specified status that is currently being tracked for the organization.

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListCreateAccountStatus>`_    


    **Request Syntax** 
    ::

      response = client.list_create_account_status(
          States=[
              'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
          ],
          NextToken='string',
          MaxResults=123
      )
    :type States: list
    :param States: 

      A list of one or more states that you want included in the response. If this parameter is not present, then all requests are included in the response.

      

    
      - *(string) --* 

      
  
    :type NextToken: string
    :param NextToken: 

      Use this parameter if you receive a ``NextToken`` response in a previous request that indicates that there is more output available. Set it to the value of the previous call's ``NextToken`` response to indicate where the output should continue from.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      (Optional) Use this to limit the number of results you want included in the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the ``NextToken`` response element is present and has a value (is not null). Include that value as the ``NextToken`` request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check ``NextToken`` after every operation to ensure that you receive all of the results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CreateAccountStatuses': [
                {
                    'Id': 'string',
                    'AccountName': 'string',
                    'State': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
                    'RequestedTimestamp': datetime(2015, 1, 1),
                    'CompletedTimestamp': datetime(2015, 1, 1),
                    'AccountId': 'string',
                    'FailureReason': 'ACCOUNT_LIMIT_EXCEEDED'|'EMAIL_ALREADY_EXISTS'|'INVALID_ADDRESS'|'INVALID_EMAIL'|'CONCURRENT_ACCOUNT_MODIFICATION'|'INTERNAL_FAILURE'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CreateAccountStatuses** *(list) --* 

          A list of objects with details about the requests. Certain elements, such as the accountId number, are present in the output only after the account has been successfully created.

          
          

          - *(dict) --* 

            Contains the status about a  CreateAccount request to create an AWS account in an organization.

            
            

            - **Id** *(string) --* 

              The unique identifier (ID) that references this request. You get this value from the response of the initial  CreateAccount request to create the account.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an create account request ID string requires "car-" followed by from 8 to 32 lower-case letters or digits.

              
            

            - **AccountName** *(string) --* 

              The account name given to the account when it was created.

              
            

            - **State** *(string) --* 

              The status of the request.

              
            

            - **RequestedTimestamp** *(datetime) --* 

              The date and time that the request was made for the account creation.

              
            

            - **CompletedTimestamp** *(datetime) --* 

              The date and time that the account was created and the request completed.

              
            

            - **AccountId** *(string) --* 

              If the account was created successfully, the unique identifier (ID) of the new account.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires exactly 12 digits.

              
            

            - **FailureReason** *(string) --* 

              If the request failed, a description of the reason for the failure.

               

               
              * ACCOUNT_LIMIT_EXCEEDED: The account could not be created because you have reached the limit on the number of accounts in your organization. 
               
              * EMAIL_ALREADY_EXISTS: The account could not be created because another AWS account with that email address already exists. 
               
              * INVALID_ADDRESS: The account could not be created because the address you provided is not valid. 
               
              * INVALID_EMAIL: The account could not be created because the email address you provided is not valid. 
               
              * INTERNAL_FAILURE: The account could not be created because of an internal failure. Try again later. If the problem persists, contact Customer Support. 
               

              
        
      
        

        - **NextToken** *(string) --* 

          If present, this value indicates that there is more output available than is included in the current response. Use this value in the ``NextToken`` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the ``NextToken`` response element comes back as ``null`` .

          
    

  .. py:method:: list_handshakes_for_account(**kwargs)

    

    Lists the current handshakes that are associated with the account of the requesting user.

     

    Handshakes that are ACCEPTED, DECLINED, or CANCELED appear in the results of this API for only 30 days after changing to that state. After that they are deleted and no longer accessible.

     

    This operation can be called from any account in the organization.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListHandshakesForAccount>`_    


    **Request Syntax** 
    ::

      response = client.list_handshakes_for_account(
          Filter={
              'ActionType': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
              'ParentHandshakeId': 'string'
          },
          NextToken='string',
          MaxResults=123
      )
    :type Filter: dict
    :param Filter: 

      Filters the handshakes that you want included in the response. The default is all types. Use the ``ActionType`` element to limit the output to only a specified type, such as ``INVITE`` , ``ENABLE-FULL-CONTROL`` , or ``APPROVE-FULL-CONTROL`` . Alternatively, for the ``ENABLE-FULL-CONTROL`` handshake that generates a separate child handshake for each member account, you can specify ``ParentHandshakeId`` to see only the handshakes that were generated by that parent request.

      

    
      - **ActionType** *(string) --* 

        Specifies the type of handshake action.

         

        If you specify ``ActionType`` , you cannot also specify ``ParentHandshakeId`` .

        

      
      - **ParentHandshakeId** *(string) --* 

        Specifies the parent handshake. Only used for handshake types that are a child of another type.

         

        If you specify ``ParentHandshakeId`` , you cannot also specify ``ActionType`` .

         

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

        

      
    
    :type NextToken: string
    :param NextToken: 

      Use this parameter if you receive a ``NextToken`` response in a previous request that indicates that there is more output available. Set it to the value of the previous call's ``NextToken`` response to indicate where the output should continue from.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      (Optional) Use this to limit the number of results you want included in the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the ``NextToken`` response element is present and has a value (is not null). Include that value as the ``NextToken`` request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check ``NextToken`` after every operation to ensure that you receive all of the results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Handshakes': [
                {
                    'Id': 'string',
                    'Arn': 'string',
                    'Parties': [
                        {
                            'Id': 'string',
                            'Type': 'ACCOUNT'|'ORGANIZATION'|'EMAIL'
                        },
                    ],
                    'State': 'REQUESTED'|'OPEN'|'CANCELED'|'ACCEPTED'|'DECLINED'|'EXPIRED',
                    'RequestedTimestamp': datetime(2015, 1, 1),
                    'ExpirationTimestamp': datetime(2015, 1, 1),
                    'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
                    'Resources': [
                        {
                            'Value': 'string',
                            'Type': 'ACCOUNT'|'ORGANIZATION'|'ORGANIZATION_FEATURE_SET'|'EMAIL'|'MASTER_EMAIL'|'MASTER_NAME'|'NOTES'|'PARENT_HANDSHAKE',
                            'Resources': {'... recursive ...'}
                        },
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Handshakes** *(list) --* 

          A list of  Handshake objects with details about each of the handshakes that is associated with the specified account.

          
          

          - *(dict) --* 

            Contains information that must be exchanged to securely establish a relationship between two accounts (an *originator* and a *recipient* ). For example, when a master account (the originator) invites another account (the recipient) to join its organization, the two accounts exchange information as a series of handshake requests and responses.

             

             **Note:** Handshakes that are CANCELED, ACCEPTED, or DECLINED show up in lists for only 30 days after entering that state After that they are deleted.

            
            

            - **Id** *(string) --* 

              The unique identifier (ID) of a handshake. The originating account creates the ID when it initiates the handshake.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

              
            

            - **Arn** *(string) --* 

              The Amazon Resource Name (ARN) of a handshake.

               

              For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

              
            

            - **Parties** *(list) --* 

              Information about the two accounts that are participating in the handshake.

              
              

              - *(dict) --* 

                Identifies a participant in a handshake.

                
                

                - **Id** *(string) --* 

                  The unique identifier (ID) for the party.

                   

                  The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

                  
                

                - **Type** *(string) --* 

                  The type of party.

                  
            
          
            

            - **State** *(string) --* 

              The current state of the handshake. Use the state to trace the flow of the handshake through the process from its creation to its acceptance. The meaning of each of the valid values is as follows:

               

               
              * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some handshake types) and not all recipients have responded yet. The request stays in this state until all recipients respond. 
               
              * **OPEN** : This handshake was sent to multiple recipients (applicable to only some policy types) and all recipients have responded, allowing the originator to complete the handshake action. 
               
              * **CANCELED** : This handshake is no longer active because it was canceled by the originating account. 
               
              * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient. 
               
              * **DECLINED** : This handshake is no longer active because it was declined by the recipient account. 
               
              * **EXPIRED** : This handshake is no longer active because the originator did not receive a response of any kind from the recipient before the expiration time (15 days). 
               

              
            

            - **RequestedTimestamp** *(datetime) --* 

              The date and time that the handshake request was made.

              
            

            - **ExpirationTimestamp** *(datetime) --* 

              The date and time that the handshake expires. If the recipient of the handshake request fails to respond before the specified date and time, the handshake becomes inactive and is no longer valid.

              
            

            - **Action** *(string) --* 

              The type of handshake, indicating what action occurs when the recipient accepts the handshake. The following handshake types are supported:

               

               
              * **INVITE** : This type of handshake represents a request to join an organization. It is always sent from the master account to only non-member accounts. 
               
              * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all features in an organization. It is always sent from the master account to only *invited* member accounts. Created accounts do not receive this because those accounts were created by the organization's master account and approval is inferred. 
               
              * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations service when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It is sent only to the master account and signals the master that it can finalize the process to enable all features. 
               

              
            

            - **Resources** *(list) --* 

              Additional information that is needed to process the handshake.

              
              

              - *(dict) --* 

                Contains additional data that is needed to process a handshake.

                
                

                - **Value** *(string) --* 

                  The information that is passed to the other party in the handshake. The format of the value string must match the requirements of the specified type.

                  
                

                - **Type** *(string) --* 

                  The type of information being passed, specifying how the value is to be interpreted by the other party:

                   

                   
                  * ``ACCOUNT`` - Specifies an AWS account ID number. 
                   
                  * ``ORGANIZATION`` - Specifies an organization ID number. 
                   
                  * ``EMAIL`` - Specifies the email address that is associated with the account that receives the handshake.  
                   
                  * ``OWNER_EMAIL`` - Specifies the email address associated with the master account. Included as information about an organization.  
                   
                  * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as information about an organization.  
                   
                  * ``NOTES`` - Additional text provided by the handshake initiator and intended for the recipient to read. 
                   

                  
                

                - **Resources** *(list) --* 

                  When needed, contains an additional array of ``HandshakeResource`` objects.

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          If present, this value indicates that there is more output available than is included in the current response. Use this value in the ``NextToken`` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the ``NextToken`` response element comes back as ``null`` .

          
    

  .. py:method:: list_handshakes_for_organization(**kwargs)

    

    Lists the handshakes that are associated with the organization that the requesting user is part of. The ``ListHandshakesForOrganization`` operation returns a list of handshake structures. Each structure contains details and status about a handshake.

     

    Handshakes that are ACCEPTED, DECLINED, or CANCELED appear in the results of this API for only 30 days after changing to that state. After that they are deleted and no longer accessible.

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListHandshakesForOrganization>`_    


    **Request Syntax** 
    ::

      response = client.list_handshakes_for_organization(
          Filter={
              'ActionType': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
              'ParentHandshakeId': 'string'
          },
          NextToken='string',
          MaxResults=123
      )
    :type Filter: dict
    :param Filter: 

      A filter of the handshakes that you want included in the response. The default is all types. Use the ``ActionType`` element to limit the output to only a specified type, such as ``INVITE`` , ``ENABLE-ALL-FEATURES`` , or ``APPROVE-ALL-FEATURES`` . Alternatively, for the ``ENABLE-ALL-FEATURES`` handshake that generates a separate child handshake for each member account, you can specify the ``ParentHandshakeId`` to see only the handshakes that were generated by that parent request.

      

    
      - **ActionType** *(string) --* 

        Specifies the type of handshake action.

         

        If you specify ``ActionType`` , you cannot also specify ``ParentHandshakeId`` .

        

      
      - **ParentHandshakeId** *(string) --* 

        Specifies the parent handshake. Only used for handshake types that are a child of another type.

         

        If you specify ``ParentHandshakeId`` , you cannot also specify ``ActionType`` .

         

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

        

      
    
    :type NextToken: string
    :param NextToken: 

      Use this parameter if you receive a ``NextToken`` response in a previous request that indicates that there is more output available. Set it to the value of the previous call's ``NextToken`` response to indicate where the output should continue from.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      (Optional) Use this to limit the number of results you want included in the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the ``NextToken`` response element is present and has a value (is not null). Include that value as the ``NextToken`` request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check ``NextToken`` after every operation to ensure that you receive all of the results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Handshakes': [
                {
                    'Id': 'string',
                    'Arn': 'string',
                    'Parties': [
                        {
                            'Id': 'string',
                            'Type': 'ACCOUNT'|'ORGANIZATION'|'EMAIL'
                        },
                    ],
                    'State': 'REQUESTED'|'OPEN'|'CANCELED'|'ACCEPTED'|'DECLINED'|'EXPIRED',
                    'RequestedTimestamp': datetime(2015, 1, 1),
                    'ExpirationTimestamp': datetime(2015, 1, 1),
                    'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
                    'Resources': [
                        {
                            'Value': 'string',
                            'Type': 'ACCOUNT'|'ORGANIZATION'|'ORGANIZATION_FEATURE_SET'|'EMAIL'|'MASTER_EMAIL'|'MASTER_NAME'|'NOTES'|'PARENT_HANDSHAKE',
                            'Resources': {'... recursive ...'}
                        },
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Handshakes** *(list) --* 

          A list of  Handshake objects with details about each of the handshakes that are associated with an organization.

          
          

          - *(dict) --* 

            Contains information that must be exchanged to securely establish a relationship between two accounts (an *originator* and a *recipient* ). For example, when a master account (the originator) invites another account (the recipient) to join its organization, the two accounts exchange information as a series of handshake requests and responses.

             

             **Note:** Handshakes that are CANCELED, ACCEPTED, or DECLINED show up in lists for only 30 days after entering that state After that they are deleted.

            
            

            - **Id** *(string) --* 

              The unique identifier (ID) of a handshake. The originating account creates the ID when it initiates the handshake.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

              
            

            - **Arn** *(string) --* 

              The Amazon Resource Name (ARN) of a handshake.

               

              For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

              
            

            - **Parties** *(list) --* 

              Information about the two accounts that are participating in the handshake.

              
              

              - *(dict) --* 

                Identifies a participant in a handshake.

                
                

                - **Id** *(string) --* 

                  The unique identifier (ID) for the party.

                   

                  The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

                  
                

                - **Type** *(string) --* 

                  The type of party.

                  
            
          
            

            - **State** *(string) --* 

              The current state of the handshake. Use the state to trace the flow of the handshake through the process from its creation to its acceptance. The meaning of each of the valid values is as follows:

               

               
              * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some handshake types) and not all recipients have responded yet. The request stays in this state until all recipients respond. 
               
              * **OPEN** : This handshake was sent to multiple recipients (applicable to only some policy types) and all recipients have responded, allowing the originator to complete the handshake action. 
               
              * **CANCELED** : This handshake is no longer active because it was canceled by the originating account. 
               
              * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient. 
               
              * **DECLINED** : This handshake is no longer active because it was declined by the recipient account. 
               
              * **EXPIRED** : This handshake is no longer active because the originator did not receive a response of any kind from the recipient before the expiration time (15 days). 
               

              
            

            - **RequestedTimestamp** *(datetime) --* 

              The date and time that the handshake request was made.

              
            

            - **ExpirationTimestamp** *(datetime) --* 

              The date and time that the handshake expires. If the recipient of the handshake request fails to respond before the specified date and time, the handshake becomes inactive and is no longer valid.

              
            

            - **Action** *(string) --* 

              The type of handshake, indicating what action occurs when the recipient accepts the handshake. The following handshake types are supported:

               

               
              * **INVITE** : This type of handshake represents a request to join an organization. It is always sent from the master account to only non-member accounts. 
               
              * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all features in an organization. It is always sent from the master account to only *invited* member accounts. Created accounts do not receive this because those accounts were created by the organization's master account and approval is inferred. 
               
              * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations service when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It is sent only to the master account and signals the master that it can finalize the process to enable all features. 
               

              
            

            - **Resources** *(list) --* 

              Additional information that is needed to process the handshake.

              
              

              - *(dict) --* 

                Contains additional data that is needed to process a handshake.

                
                

                - **Value** *(string) --* 

                  The information that is passed to the other party in the handshake. The format of the value string must match the requirements of the specified type.

                  
                

                - **Type** *(string) --* 

                  The type of information being passed, specifying how the value is to be interpreted by the other party:

                   

                   
                  * ``ACCOUNT`` - Specifies an AWS account ID number. 
                   
                  * ``ORGANIZATION`` - Specifies an organization ID number. 
                   
                  * ``EMAIL`` - Specifies the email address that is associated with the account that receives the handshake.  
                   
                  * ``OWNER_EMAIL`` - Specifies the email address associated with the master account. Included as information about an organization.  
                   
                  * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as information about an organization.  
                   
                  * ``NOTES`` - Additional text provided by the handshake initiator and intended for the recipient to read. 
                   

                  
                

                - **Resources** *(list) --* 

                  When needed, contains an additional array of ``HandshakeResource`` objects.

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          If present, this value indicates that there is more output available than is included in the current response. Use this value in the ``NextToken`` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the ``NextToken`` response element comes back as ``null`` .

          
    

  .. py:method:: list_organizational_units_for_parent(**kwargs)

    

    Lists the organizational units (OUs) in a parent organizational unit or root.

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListOrganizationalUnitsForParent>`_    


    **Request Syntax** 
    ::

      response = client.list_organizational_units_for_parent(
          ParentId='string',
          NextToken='string',
          MaxResults=123
      )
    :type ParentId: string
    :param ParentId: **[REQUIRED]** 

      The unique identifier (ID) of the root or OU whose child OUs you want to list.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a parent ID string requires one of the following:

       

       
      * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits. 
       
      * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits. 
       

      

    
    :type NextToken: string
    :param NextToken: 

      Use this parameter if you receive a ``NextToken`` response in a previous request that indicates that there is more output available. Set it to the value of the previous call's ``NextToken`` response to indicate where the output should continue from.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      (Optional) Use this to limit the number of results you want included in the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the ``NextToken`` response element is present and has a value (is not null). Include that value as the ``NextToken`` request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check ``NextToken`` after every operation to ensure that you receive all of the results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'OrganizationalUnits': [
                {
                    'Id': 'string',
                    'Arn': 'string',
                    'Name': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **OrganizationalUnits** *(list) --* 

          A list of the OUs in the specified root or parent OU.

          
          

          - *(dict) --* 

            Contains details about an organizational unit (OU). An OU is a container of AWS accounts within a root of an organization. Policies that are attached to an OU apply to all accounts contained in that OU and in any child OUs.

            
            

            - **Id** *(string) --* 

              The unique identifier (ID) associated with this OU.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.

              
            

            - **Arn** *(string) --* 

              The Amazon Resource Name (ARN) of this OU.

               

              For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

              
            

            - **Name** *(string) --* 

              The friendly name of this OU.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

              
        
      
        

        - **NextToken** *(string) --* 

          If present, this value indicates that there is more output available than is included in the current response. Use this value in the ``NextToken`` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the ``NextToken`` response element comes back as ``null`` .

          
    

  .. py:method:: list_parents(**kwargs)

    

    Lists the root or organizational units (OUs) that serve as the immediate parent of the specified child OU or account. This operation, along with  ListChildren enables you to traverse the tree structure that makes up this root.

     

    This operation can be called only from the organization's master account.

     

    .. note::

       

      In the current release, a child can have only a single parent. 

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListParents>`_    


    **Request Syntax** 
    ::

      response = client.list_parents(
          ChildId='string',
          NextToken='string',
          MaxResults=123
      )
    :type ChildId: string
    :param ChildId: **[REQUIRED]** 

      The unique identifier (ID) of the OU or account whose parent containers you want to list. Do not specify a root.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a child ID string requires one of the following:

       

       
      * Account: a string that consists of exactly 12 digits. 
       
      * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits. 
       

      

    
    :type NextToken: string
    :param NextToken: 

      Use this parameter if you receive a ``NextToken`` response in a previous request that indicates that there is more output available. Set it to the value of the previous call's ``NextToken`` response to indicate where the output should continue from.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      (Optional) Use this to limit the number of results you want included in the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the ``NextToken`` response element is present and has a value (is not null). Include that value as the ``NextToken`` request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check ``NextToken`` after every operation to ensure that you receive all of the results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Parents': [
                {
                    'Id': 'string',
                    'Type': 'ROOT'|'ORGANIZATIONAL_UNIT'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Parents** *(list) --* 

          A list of parents for the specified child account or OU.

          
          

          - *(dict) --* 

            Contains information about either a root or an organizational unit (OU) that can contain OUs or accounts in an organization.

            
            

            - **Id** *(string) --* 

              The unique identifier (ID) of the parent entity.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a parent ID string requires one of the following:

               

               
              * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits. 
               
              * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits. 
               

              
            

            - **Type** *(string) --* 

              The type of the parent entity.

              
        
      
        

        - **NextToken** *(string) --* 

          If present, this value indicates that there is more output available than is included in the current response. Use this value in the ``NextToken`` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the ``NextToken`` response element comes back as ``null`` .

          
    

  .. py:method:: list_policies(**kwargs)

    

    Retrieves the list of all policies in an organization of a specified type.

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListPolicies>`_    


    **Request Syntax** 
    ::

      response = client.list_policies(
          Filter='SERVICE_CONTROL_POLICY',
          NextToken='string',
          MaxResults=123
      )
    :type Filter: string
    :param Filter: **[REQUIRED]** 

      Specifies the type of policy that you want to include in the response.

      

    
    :type NextToken: string
    :param NextToken: 

      Use this parameter if you receive a ``NextToken`` response in a previous request that indicates that there is more output available. Set it to the value of the previous call's ``NextToken`` response to indicate where the output should continue from.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      (Optional) Use this to limit the number of results you want included in the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the ``NextToken`` response element is present and has a value (is not null). Include that value as the ``NextToken`` request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check ``NextToken`` after every operation to ensure that you receive all of the results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Policies': [
                {
                    'Id': 'string',
                    'Arn': 'string',
                    'Name': 'string',
                    'Description': 'string',
                    'Type': 'SERVICE_CONTROL_POLICY',
                    'AwsManaged': True|False
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Policies** *(list) --* 

          A list of policies that match the filter criteria in the request. The output list does not include the policy contents. To see the content for a policy, see  DescribePolicy .

          
          

          - *(dict) --* 

            Contains information about a policy, but does not include the content. To see the content of a policy, see  DescribePolicy .

            
            

            - **Id** *(string) --* 

              The unique identifier (ID) of the policy.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires "p-" followed by from 8 to 128 lower-case letters or digits.

              
            

            - **Arn** *(string) --* 

              The Amazon Resource Name (ARN) of the policy.

               

              For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

              
            

            - **Name** *(string) --* 

              The friendly name of the policy.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

              
            

            - **Description** *(string) --* 

              The description of the policy.

              
            

            - **Type** *(string) --* 

              The type of policy.

              
            

            - **AwsManaged** *(boolean) --* 

              A boolean value that indicates whether the specified policy is an AWS managed policy. If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.

              
        
      
        

        - **NextToken** *(string) --* 

          If present, this value indicates that there is more output available than is included in the current response. Use this value in the ``NextToken`` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the ``NextToken`` response element comes back as ``null`` .

          
    

  .. py:method:: list_policies_for_target(**kwargs)

    

    Lists the policies that are directly attached to the specified target root, organizational unit (OU), or account. You must specify the policy type that you want included in the returned list.

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListPoliciesForTarget>`_    


    **Request Syntax** 
    ::

      response = client.list_policies_for_target(
          TargetId='string',
          Filter='SERVICE_CONTROL_POLICY',
          NextToken='string',
          MaxResults=123
      )
    :type TargetId: string
    :param TargetId: **[REQUIRED]** 

      The unique identifier (ID) of the root, organizational unit, or account whose policies you want to list.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a target ID string requires one of the following:

       

       
      * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits. 
       
      * Account: a string that consists of exactly 12 digits. 
       
      * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits. 
       

      

    
    :type Filter: string
    :param Filter: **[REQUIRED]** 

      The type of policy that you want to include in the returned list.

      

    
    :type NextToken: string
    :param NextToken: 

      Use this parameter if you receive a ``NextToken`` response in a previous request that indicates that there is more output available. Set it to the value of the previous call's ``NextToken`` response to indicate where the output should continue from.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      (Optional) Use this to limit the number of results you want included in the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the ``NextToken`` response element is present and has a value (is not null). Include that value as the ``NextToken`` request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check ``NextToken`` after every operation to ensure that you receive all of the results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Policies': [
                {
                    'Id': 'string',
                    'Arn': 'string',
                    'Name': 'string',
                    'Description': 'string',
                    'Type': 'SERVICE_CONTROL_POLICY',
                    'AwsManaged': True|False
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Policies** *(list) --* 

          The list of policies that match the criteria in the request.

          
          

          - *(dict) --* 

            Contains information about a policy, but does not include the content. To see the content of a policy, see  DescribePolicy .

            
            

            - **Id** *(string) --* 

              The unique identifier (ID) of the policy.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires "p-" followed by from 8 to 128 lower-case letters or digits.

              
            

            - **Arn** *(string) --* 

              The Amazon Resource Name (ARN) of the policy.

               

              For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

              
            

            - **Name** *(string) --* 

              The friendly name of the policy.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

              
            

            - **Description** *(string) --* 

              The description of the policy.

              
            

            - **Type** *(string) --* 

              The type of policy.

              
            

            - **AwsManaged** *(boolean) --* 

              A boolean value that indicates whether the specified policy is an AWS managed policy. If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.

              
        
      
        

        - **NextToken** *(string) --* 

          If present, this value indicates that there is more output available than is included in the current response. Use this value in the ``NextToken`` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the ``NextToken`` response element comes back as ``null`` .

          
    

  .. py:method:: list_roots(**kwargs)

    

    Lists the roots that are defined in the current organization.

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListRoots>`_    


    **Request Syntax** 
    ::

      response = client.list_roots(
          NextToken='string',
          MaxResults=123
      )
    :type NextToken: string
    :param NextToken: 

      Use this parameter if you receive a ``NextToken`` response in a previous request that indicates that there is more output available. Set it to the value of the previous call's ``NextToken`` response to indicate where the output should continue from.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      (Optional) Use this to limit the number of results you want included in the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the ``NextToken`` response element is present and has a value (is not null). Include that value as the ``NextToken`` request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check ``NextToken`` after every operation to ensure that you receive all of the results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Roots': [
                {
                    'Id': 'string',
                    'Arn': 'string',
                    'Name': 'string',
                    'PolicyTypes': [
                        {
                            'Type': 'SERVICE_CONTROL_POLICY',
                            'Status': 'ENABLED'|'PENDING_ENABLE'|'PENDING_DISABLE'
                        },
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Roots** *(list) --* 

          A list of roots that are defined in an organization.

          
          

          - *(dict) --* 

            Contains details about a root. A root is a top-level parent node in the hierarchy of an organization that can contain organizational units (OUs) and accounts. Every root contains every AWS account in the organization. Each root enables the accounts to be organized in a different way and to have different policy types enabled for use in that root.

            
            

            - **Id** *(string) --* 

              The unique identifier (ID) for the root.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a root ID string requires "r-" followed by from 4 to 32 lower-case letters or digits.

              
            

            - **Arn** *(string) --* 

              The Amazon Resource Name (ARN) of the root.

               

              For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

              
            

            - **Name** *(string) --* 

              The friendly name of the root.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

              
            

            - **PolicyTypes** *(list) --* 

              The types of policies that are currently enabled for the root and therefore can be attached to the root or to its OUs or accounts.

              
              

              - *(dict) --* 

                Contains information about a policy type and its status in the associated root.

                
                

                - **Type** *(string) --* 

                  The name of the policy type.

                  
                

                - **Status** *(string) --* 

                  The status of the policy type as it relates to the associated root. To attach a policy of the specified type to a root or to an OU or account in that root, it must be available in the organization and enabled for that root.

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          If present, this value indicates that there is more output available than is included in the current response. Use this value in the ``NextToken`` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the ``NextToken`` response element comes back as ``null`` .

          
    

  .. py:method:: list_targets_for_policy(**kwargs)

    

    Lists all the roots, OUs, and accounts to which the specified policy is attached.

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListTargetsForPolicy>`_    


    **Request Syntax** 
    ::

      response = client.list_targets_for_policy(
          PolicyId='string',
          NextToken='string',
          MaxResults=123
      )
    :type PolicyId: string
    :param PolicyId: **[REQUIRED]** 

      The unique identifier (ID) of the policy for which you want to know its attachments.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires "p-" followed by from 8 to 128 lower-case letters or digits.

      

    
    :type NextToken: string
    :param NextToken: 

      Use this parameter if you receive a ``NextToken`` response in a previous request that indicates that there is more output available. Set it to the value of the previous call's ``NextToken`` response to indicate where the output should continue from.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      (Optional) Use this to limit the number of results you want included in the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the ``NextToken`` response element is present and has a value (is not null). Include that value as the ``NextToken`` request parameter in the next call to the operation to get the next part of the results. Note that Organizations might return fewer results than the maximum even when there are more results available. You should check ``NextToken`` after every operation to ensure that you receive all of the results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Targets': [
                {
                    'TargetId': 'string',
                    'Arn': 'string',
                    'Name': 'string',
                    'Type': 'ACCOUNT'|'ORGANIZATIONAL_UNIT'|'ROOT'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Targets** *(list) --* 

          A list of structures, each of which contains details about one of the entities to which the specified policy is attached.

          
          

          - *(dict) --* 

            Contains information about a root, OU, or account that a policy is attached to.

            
            

            - **TargetId** *(string) --* 

              The unique identifier (ID) of the policy target.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a target ID string requires one of the following:

               

               
              * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits. 
               
              * Account: a string that consists of exactly 12 digits. 
               
              * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits. 
               

              
            

            - **Arn** *(string) --* 

              The Amazon Resource Name (ARN) of the policy target.

               

              For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

              
            

            - **Name** *(string) --* 

              The friendly name of the policy target.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

              
            

            - **Type** *(string) --* 

              The type of the policy target.

              
        
      
        

        - **NextToken** *(string) --* 

          If present, this value indicates that there is more output available than is included in the current response. Use this value in the ``NextToken`` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the ``NextToken`` response element comes back as ``null`` .

          
    

  .. py:method:: move_account(**kwargs)

    

    Moves an account from its current source parent root or OU to the specified destination parent root or OU.

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/MoveAccount>`_    


    **Request Syntax** 
    ::

      response = client.move_account(
          AccountId='string',
          SourceParentId='string',
          DestinationParentId='string'
      )
    :type AccountId: string
    :param AccountId: **[REQUIRED]** 

      The unique identifier (ID) of the account that you want to move.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires exactly 12 digits.

      

    
    :type SourceParentId: string
    :param SourceParentId: **[REQUIRED]** 

      The unique identifier (ID) of the root or organizational unit that you want to move the account from.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a parent ID string requires one of the following:

       

       
      * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits. 
       
      * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits. 
       

      

    
    :type DestinationParentId: string
    :param DestinationParentId: **[REQUIRED]** 

      The unique identifier (ID) of the root or organizational unit that you want to move the account to.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a parent ID string requires one of the following:

       

       
      * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits. 
       
      * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits. 
       

      

    
    
    :returns: None

  .. py:method:: remove_account_from_organization(**kwargs)

    

    Removes the specified account from the organization.

     

    The removed account becomes a stand-alone account that is not a member of any organization. It is no longer subject to any policies and is responsible for its own bill payments. The organization's master account is no longer charged for any expenses accrued by the member account after it is removed from the organization.

     

    This operation can be called only from the organization's master account. Member accounts can remove themselves with  LeaveOrganization instead.

     

    .. warning::

       

       
      * You can remove an account from your organization only if the account is configured with the information required to operate as a standalone account. When you create an account in an organization using the AWS Organizations console, API, or CLI commands, the information required of standalone accounts is *not* automatically collected. For an account that you want to make standalone, you must accept the End User License Agreement (EULA), choose a support plan, provide and verify the required contact information, and provide a current payment method. AWS uses the payment method to charge for any billable (not free tier) AWS activity that occurs while the account is not attached to an organization. To remove an account that does not yet have this information, you must sign in as the member account and follow the steps at `To leave an organization when all required account information has not yet been provided <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html#leave-without-all-info>`__ in the *AWS Organizations User Guide* . 
       
      * You can remove a member account only after you enable IAM user access to billing in the member account. For more information, see `Activating Access to the Billing and Cost Management Console <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/grantaccess.html#ControllingAccessWebsite-Activate>`__ in the *AWS Billing and Cost Management User Guide* . 
       

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/RemoveAccountFromOrganization>`_    


    **Request Syntax** 
    ::

      response = client.remove_account_from_organization(
          AccountId='string'
      )
    :type AccountId: string
    :param AccountId: **[REQUIRED]** 

      The unique identifier (ID) of the member account that you want to remove from the organization.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires exactly 12 digits.

      

    
    
    :returns: None

  .. py:method:: update_organizational_unit(**kwargs)

    

    Renames the specified organizational unit (OU). The ID and ARN do not change. The child OUs and accounts remain in place, and any attached policies of the OU remain attached. 

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/UpdateOrganizationalUnit>`_    


    **Request Syntax** 
    ::

      response = client.update_organizational_unit(
          OrganizationalUnitId='string',
          Name='string'
      )
    :type OrganizationalUnitId: string
    :param OrganizationalUnitId: **[REQUIRED]** 

      The unique identifier (ID) of the OU that you want to rename. You can get the ID from the  ListOrganizationalUnitsForParent operation.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.

      

    
    :type Name: string
    :param Name: 

      The new name that you want to assign to the OU.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'OrganizationalUnit': {
                'Id': 'string',
                'Arn': 'string',
                'Name': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **OrganizationalUnit** *(dict) --* 

          A structure that contains the details about the specified OU, including its new name.

          
          

          - **Id** *(string) --* 

            The unique identifier (ID) associated with this OU.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.

            
          

          - **Arn** *(string) --* 

            The Amazon Resource Name (ARN) of this OU.

             

            For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

            
          

          - **Name** *(string) --* 

            The friendly name of this OU.

             

            The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

            
      
    

  .. py:method:: update_policy(**kwargs)

    

    Updates an existing policy with a new name, description, or content. If any parameter is not supplied, that value remains unchanged. Note that you cannot change a policy's type.

     

    This operation can be called only from the organization's master account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/UpdatePolicy>`_    


    **Request Syntax** 
    ::

      response = client.update_policy(
          PolicyId='string',
          Name='string',
          Description='string',
          Content='string'
      )
    :type PolicyId: string
    :param PolicyId: **[REQUIRED]** 

      The unique identifier (ID) of the policy that you want to update.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires "p-" followed by from 8 to 128 lower-case letters or digits.

      

    
    :type Name: string
    :param Name: 

      If provided, the new name for the policy.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

      

    
    :type Description: string
    :param Description: 

      If provided, the new description for the policy.

      

    
    :type Content: string
    :param Content: 

      If provided, the new content for the policy. The text must be correctly formatted JSON that complies with the syntax for the policy's type. For more information, see `Service Control Policy Syntax <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_scp-syntax.html>`__ in the *AWS Organizations User Guide* .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Policy': {
                'PolicySummary': {
                    'Id': 'string',
                    'Arn': 'string',
                    'Name': 'string',
                    'Description': 'string',
                    'Type': 'SERVICE_CONTROL_POLICY',
                    'AwsManaged': True|False
                },
                'Content': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Policy** *(dict) --* 

          A structure that contains details about the updated policy, showing the requested changes.

          
          

          - **PolicySummary** *(dict) --* 

            A structure that contains additional details about the policy.

            
            

            - **Id** *(string) --* 

              The unique identifier (ID) of the policy.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires "p-" followed by from 8 to 128 lower-case letters or digits.

              
            

            - **Arn** *(string) --* 

              The Amazon Resource Name (ARN) of the policy.

               

              For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

              
            

            - **Name** *(string) --* 

              The friendly name of the policy.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

              
            

            - **Description** *(string) --* 

              The description of the policy.

              
            

            - **Type** *(string) --* 

              The type of policy.

              
            

            - **AwsManaged** *(boolean) --* 

              A boolean value that indicates whether the specified policy is an AWS managed policy. If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.

              
        
          

          - **Content** *(string) --* 

            The text content of the policy.

            
      
    

==========
Paginators
==========


The available paginators are:

* :py:class:`Organizations.Paginator.ListAccounts`


* :py:class:`Organizations.Paginator.ListAccountsForParent`


* :py:class:`Organizations.Paginator.ListChildren`


* :py:class:`Organizations.Paginator.ListCreateAccountStatus`


* :py:class:`Organizations.Paginator.ListHandshakesForAccount`


* :py:class:`Organizations.Paginator.ListHandshakesForOrganization`


* :py:class:`Organizations.Paginator.ListOrganizationalUnitsForParent`


* :py:class:`Organizations.Paginator.ListParents`


* :py:class:`Organizations.Paginator.ListPolicies`


* :py:class:`Organizations.Paginator.ListPoliciesForTarget`


* :py:class:`Organizations.Paginator.ListRoots`


* :py:class:`Organizations.Paginator.ListTargetsForPolicy`



.. py:class:: Organizations.Paginator.ListAccounts

  ::

    
    paginator = client.get_paginator('list_accounts')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Organizations.Client.list_accounts`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListAccounts>`_    


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
            'Accounts': [
                {
                    'Id': 'string',
                    'Arn': 'string',
                    'Email': 'string',
                    'Name': 'string',
                    'Status': 'ACTIVE'|'SUSPENDED',
                    'JoinedMethod': 'INVITED'|'CREATED',
                    'JoinedTimestamp': datetime(2015, 1, 1)
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Accounts** *(list) --* 

          A list of objects in the organization.

          
          

          - *(dict) --* 

            Contains information about an AWS account that is a member of an organization.

            
            

            - **Id** *(string) --* 

              The unique identifier (ID) of the account.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires exactly 12 digits.

              
            

            - **Arn** *(string) --* 

              The Amazon Resource Name (ARN) of the account.

               

              For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

              
            

            - **Email** *(string) --* 

              The email address associated with the AWS account.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for this parameter is a string of characters that represents a standard Internet email address.

              
            

            - **Name** *(string) --* 

              The friendly name of the account.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

              
            

            - **Status** *(string) --* 

              The status of the account in the organization.

              
            

            - **JoinedMethod** *(string) --* 

              The method by which the account joined the organization.

              
            

            - **JoinedTimestamp** *(datetime) --* 

              The date the account became a part of the organization.

              
        
      
    

.. py:class:: Organizations.Paginator.ListAccountsForParent

  ::

    
    paginator = client.get_paginator('list_accounts_for_parent')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Organizations.Client.list_accounts_for_parent`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListAccountsForParent>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          ParentId='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type ParentId: string
    :param ParentId: **[REQUIRED]** 

      The unique identifier (ID) for the parent root or organization unit (OU) whose accounts you want to list.

      

    
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
            'Accounts': [
                {
                    'Id': 'string',
                    'Arn': 'string',
                    'Email': 'string',
                    'Name': 'string',
                    'Status': 'ACTIVE'|'SUSPENDED',
                    'JoinedMethod': 'INVITED'|'CREATED',
                    'JoinedTimestamp': datetime(2015, 1, 1)
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Accounts** *(list) --* 

          A list of the accounts in the specified root or OU.

          
          

          - *(dict) --* 

            Contains information about an AWS account that is a member of an organization.

            
            

            - **Id** *(string) --* 

              The unique identifier (ID) of the account.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires exactly 12 digits.

              
            

            - **Arn** *(string) --* 

              The Amazon Resource Name (ARN) of the account.

               

              For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

              
            

            - **Email** *(string) --* 

              The email address associated with the AWS account.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for this parameter is a string of characters that represents a standard Internet email address.

              
            

            - **Name** *(string) --* 

              The friendly name of the account.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

              
            

            - **Status** *(string) --* 

              The status of the account in the organization.

              
            

            - **JoinedMethod** *(string) --* 

              The method by which the account joined the organization.

              
            

            - **JoinedTimestamp** *(datetime) --* 

              The date the account became a part of the organization.

              
        
      
    

.. py:class:: Organizations.Paginator.ListChildren

  ::

    
    paginator = client.get_paginator('list_children')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Organizations.Client.list_children`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListChildren>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          ParentId='string',
          ChildType='ACCOUNT'|'ORGANIZATIONAL_UNIT',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type ParentId: string
    :param ParentId: **[REQUIRED]** 

      The unique identifier (ID) for the parent root or OU whose children you want to list.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a parent ID string requires one of the following:

       

       
      * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits. 
       
      * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits. 
       

      

    
    :type ChildType: string
    :param ChildType: **[REQUIRED]** 

      Filters the output to include only the specified child type.

      

    
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
            'Children': [
                {
                    'Id': 'string',
                    'Type': 'ACCOUNT'|'ORGANIZATIONAL_UNIT'
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Children** *(list) --* 

          The list of children of the specified parent container.

          
          

          - *(dict) --* 

            Contains a list of child entities, either OUs or accounts.

            
            

            - **Id** *(string) --* 

              The unique identifier (ID) of this child entity.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a child ID string requires one of the following:

               

               
              * Account: a string that consists of exactly 12 digits. 
               
              * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits. 
               

              
            

            - **Type** *(string) --* 

              The type of this child entity.

              
        
      
    

.. py:class:: Organizations.Paginator.ListCreateAccountStatus

  ::

    
    paginator = client.get_paginator('list_create_account_status')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Organizations.Client.list_create_account_status`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListCreateAccountStatus>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          States=[
              'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
          ],
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type States: list
    :param States: 

      A list of one or more states that you want included in the response. If this parameter is not present, then all requests are included in the response.

      

    
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
            'CreateAccountStatuses': [
                {
                    'Id': 'string',
                    'AccountName': 'string',
                    'State': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
                    'RequestedTimestamp': datetime(2015, 1, 1),
                    'CompletedTimestamp': datetime(2015, 1, 1),
                    'AccountId': 'string',
                    'FailureReason': 'ACCOUNT_LIMIT_EXCEEDED'|'EMAIL_ALREADY_EXISTS'|'INVALID_ADDRESS'|'INVALID_EMAIL'|'CONCURRENT_ACCOUNT_MODIFICATION'|'INTERNAL_FAILURE'
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CreateAccountStatuses** *(list) --* 

          A list of objects with details about the requests. Certain elements, such as the accountId number, are present in the output only after the account has been successfully created.

          
          

          - *(dict) --* 

            Contains the status about a  CreateAccount request to create an AWS account in an organization.

            
            

            - **Id** *(string) --* 

              The unique identifier (ID) that references this request. You get this value from the response of the initial  CreateAccount request to create the account.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an create account request ID string requires "car-" followed by from 8 to 32 lower-case letters or digits.

              
            

            - **AccountName** *(string) --* 

              The account name given to the account when it was created.

              
            

            - **State** *(string) --* 

              The status of the request.

              
            

            - **RequestedTimestamp** *(datetime) --* 

              The date and time that the request was made for the account creation.

              
            

            - **CompletedTimestamp** *(datetime) --* 

              The date and time that the account was created and the request completed.

              
            

            - **AccountId** *(string) --* 

              If the account was created successfully, the unique identifier (ID) of the new account.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an account ID string requires exactly 12 digits.

              
            

            - **FailureReason** *(string) --* 

              If the request failed, a description of the reason for the failure.

               

               
              * ACCOUNT_LIMIT_EXCEEDED: The account could not be created because you have reached the limit on the number of accounts in your organization. 
               
              * EMAIL_ALREADY_EXISTS: The account could not be created because another AWS account with that email address already exists. 
               
              * INVALID_ADDRESS: The account could not be created because the address you provided is not valid. 
               
              * INVALID_EMAIL: The account could not be created because the email address you provided is not valid. 
               
              * INTERNAL_FAILURE: The account could not be created because of an internal failure. Try again later. If the problem persists, contact Customer Support. 
               

              
        
      
    

.. py:class:: Organizations.Paginator.ListHandshakesForAccount

  ::

    
    paginator = client.get_paginator('list_handshakes_for_account')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Organizations.Client.list_handshakes_for_account`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListHandshakesForAccount>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          Filter={
              'ActionType': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
              'ParentHandshakeId': 'string'
          },
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type Filter: dict
    :param Filter: 

      Filters the handshakes that you want included in the response. The default is all types. Use the ``ActionType`` element to limit the output to only a specified type, such as ``INVITE`` , ``ENABLE-FULL-CONTROL`` , or ``APPROVE-FULL-CONTROL`` . Alternatively, for the ``ENABLE-FULL-CONTROL`` handshake that generates a separate child handshake for each member account, you can specify ``ParentHandshakeId`` to see only the handshakes that were generated by that parent request.

      

    
      - **ActionType** *(string) --* 

        Specifies the type of handshake action.

         

        If you specify ``ActionType`` , you cannot also specify ``ParentHandshakeId`` .

        

      
      - **ParentHandshakeId** *(string) --* 

        Specifies the parent handshake. Only used for handshake types that are a child of another type.

         

        If you specify ``ParentHandshakeId`` , you cannot also specify ``ActionType`` .

         

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

        

      
    
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
            'Handshakes': [
                {
                    'Id': 'string',
                    'Arn': 'string',
                    'Parties': [
                        {
                            'Id': 'string',
                            'Type': 'ACCOUNT'|'ORGANIZATION'|'EMAIL'
                        },
                    ],
                    'State': 'REQUESTED'|'OPEN'|'CANCELED'|'ACCEPTED'|'DECLINED'|'EXPIRED',
                    'RequestedTimestamp': datetime(2015, 1, 1),
                    'ExpirationTimestamp': datetime(2015, 1, 1),
                    'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
                    'Resources': [
                        {
                            'Value': 'string',
                            'Type': 'ACCOUNT'|'ORGANIZATION'|'ORGANIZATION_FEATURE_SET'|'EMAIL'|'MASTER_EMAIL'|'MASTER_NAME'|'NOTES'|'PARENT_HANDSHAKE',
                            'Resources': {'... recursive ...'}
                        },
                    ]
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Handshakes** *(list) --* 

          A list of  Handshake objects with details about each of the handshakes that is associated with the specified account.

          
          

          - *(dict) --* 

            Contains information that must be exchanged to securely establish a relationship between two accounts (an *originator* and a *recipient* ). For example, when a master account (the originator) invites another account (the recipient) to join its organization, the two accounts exchange information as a series of handshake requests and responses.

             

             **Note:** Handshakes that are CANCELED, ACCEPTED, or DECLINED show up in lists for only 30 days after entering that state After that they are deleted.

            
            

            - **Id** *(string) --* 

              The unique identifier (ID) of a handshake. The originating account creates the ID when it initiates the handshake.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

              
            

            - **Arn** *(string) --* 

              The Amazon Resource Name (ARN) of a handshake.

               

              For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

              
            

            - **Parties** *(list) --* 

              Information about the two accounts that are participating in the handshake.

              
              

              - *(dict) --* 

                Identifies a participant in a handshake.

                
                

                - **Id** *(string) --* 

                  The unique identifier (ID) for the party.

                   

                  The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

                  
                

                - **Type** *(string) --* 

                  The type of party.

                  
            
          
            

            - **State** *(string) --* 

              The current state of the handshake. Use the state to trace the flow of the handshake through the process from its creation to its acceptance. The meaning of each of the valid values is as follows:

               

               
              * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some handshake types) and not all recipients have responded yet. The request stays in this state until all recipients respond. 
               
              * **OPEN** : This handshake was sent to multiple recipients (applicable to only some policy types) and all recipients have responded, allowing the originator to complete the handshake action. 
               
              * **CANCELED** : This handshake is no longer active because it was canceled by the originating account. 
               
              * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient. 
               
              * **DECLINED** : This handshake is no longer active because it was declined by the recipient account. 
               
              * **EXPIRED** : This handshake is no longer active because the originator did not receive a response of any kind from the recipient before the expiration time (15 days). 
               

              
            

            - **RequestedTimestamp** *(datetime) --* 

              The date and time that the handshake request was made.

              
            

            - **ExpirationTimestamp** *(datetime) --* 

              The date and time that the handshake expires. If the recipient of the handshake request fails to respond before the specified date and time, the handshake becomes inactive and is no longer valid.

              
            

            - **Action** *(string) --* 

              The type of handshake, indicating what action occurs when the recipient accepts the handshake. The following handshake types are supported:

               

               
              * **INVITE** : This type of handshake represents a request to join an organization. It is always sent from the master account to only non-member accounts. 
               
              * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all features in an organization. It is always sent from the master account to only *invited* member accounts. Created accounts do not receive this because those accounts were created by the organization's master account and approval is inferred. 
               
              * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations service when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It is sent only to the master account and signals the master that it can finalize the process to enable all features. 
               

              
            

            - **Resources** *(list) --* 

              Additional information that is needed to process the handshake.

              
              

              - *(dict) --* 

                Contains additional data that is needed to process a handshake.

                
                

                - **Value** *(string) --* 

                  The information that is passed to the other party in the handshake. The format of the value string must match the requirements of the specified type.

                  
                

                - **Type** *(string) --* 

                  The type of information being passed, specifying how the value is to be interpreted by the other party:

                   

                   
                  * ``ACCOUNT`` - Specifies an AWS account ID number. 
                   
                  * ``ORGANIZATION`` - Specifies an organization ID number. 
                   
                  * ``EMAIL`` - Specifies the email address that is associated with the account that receives the handshake.  
                   
                  * ``OWNER_EMAIL`` - Specifies the email address associated with the master account. Included as information about an organization.  
                   
                  * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as information about an organization.  
                   
                  * ``NOTES`` - Additional text provided by the handshake initiator and intended for the recipient to read. 
                   

                  
                

                - **Resources** *(list) --* 

                  When needed, contains an additional array of ``HandshakeResource`` objects.

                  
            
          
        
      
    

.. py:class:: Organizations.Paginator.ListHandshakesForOrganization

  ::

    
    paginator = client.get_paginator('list_handshakes_for_organization')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Organizations.Client.list_handshakes_for_organization`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListHandshakesForOrganization>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          Filter={
              'ActionType': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
              'ParentHandshakeId': 'string'
          },
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type Filter: dict
    :param Filter: 

      A filter of the handshakes that you want included in the response. The default is all types. Use the ``ActionType`` element to limit the output to only a specified type, such as ``INVITE`` , ``ENABLE-ALL-FEATURES`` , or ``APPROVE-ALL-FEATURES`` . Alternatively, for the ``ENABLE-ALL-FEATURES`` handshake that generates a separate child handshake for each member account, you can specify the ``ParentHandshakeId`` to see only the handshakes that were generated by that parent request.

      

    
      - **ActionType** *(string) --* 

        Specifies the type of handshake action.

         

        If you specify ``ActionType`` , you cannot also specify ``ParentHandshakeId`` .

        

      
      - **ParentHandshakeId** *(string) --* 

        Specifies the parent handshake. Only used for handshake types that are a child of another type.

         

        If you specify ``ParentHandshakeId`` , you cannot also specify ``ActionType`` .

         

        The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

        

      
    
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
            'Handshakes': [
                {
                    'Id': 'string',
                    'Arn': 'string',
                    'Parties': [
                        {
                            'Id': 'string',
                            'Type': 'ACCOUNT'|'ORGANIZATION'|'EMAIL'
                        },
                    ],
                    'State': 'REQUESTED'|'OPEN'|'CANCELED'|'ACCEPTED'|'DECLINED'|'EXPIRED',
                    'RequestedTimestamp': datetime(2015, 1, 1),
                    'ExpirationTimestamp': datetime(2015, 1, 1),
                    'Action': 'INVITE'|'ENABLE_ALL_FEATURES'|'APPROVE_ALL_FEATURES'|'ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE',
                    'Resources': [
                        {
                            'Value': 'string',
                            'Type': 'ACCOUNT'|'ORGANIZATION'|'ORGANIZATION_FEATURE_SET'|'EMAIL'|'MASTER_EMAIL'|'MASTER_NAME'|'NOTES'|'PARENT_HANDSHAKE',
                            'Resources': {'... recursive ...'}
                        },
                    ]
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Handshakes** *(list) --* 

          A list of  Handshake objects with details about each of the handshakes that are associated with an organization.

          
          

          - *(dict) --* 

            Contains information that must be exchanged to securely establish a relationship between two accounts (an *originator* and a *recipient* ). For example, when a master account (the originator) invites another account (the recipient) to join its organization, the two accounts exchange information as a series of handshake requests and responses.

             

             **Note:** Handshakes that are CANCELED, ACCEPTED, or DECLINED show up in lists for only 30 days after entering that state After that they are deleted.

            
            

            - **Id** *(string) --* 

              The unique identifier (ID) of a handshake. The originating account creates the ID when it initiates the handshake.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

              
            

            - **Arn** *(string) --* 

              The Amazon Resource Name (ARN) of a handshake.

               

              For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

              
            

            - **Parties** *(list) --* 

              Information about the two accounts that are participating in the handshake.

              
              

              - *(dict) --* 

                Identifies a participant in a handshake.

                
                

                - **Id** *(string) --* 

                  The unique identifier (ID) for the party.

                   

                  The `regex pattern <http://wikipedia.org/wiki/regex>`__ for handshake ID string requires "h-" followed by from 8 to 32 lower-case letters or digits.

                  
                

                - **Type** *(string) --* 

                  The type of party.

                  
            
          
            

            - **State** *(string) --* 

              The current state of the handshake. Use the state to trace the flow of the handshake through the process from its creation to its acceptance. The meaning of each of the valid values is as follows:

               

               
              * **REQUESTED** : This handshake was sent to multiple recipients (applicable to only some handshake types) and not all recipients have responded yet. The request stays in this state until all recipients respond. 
               
              * **OPEN** : This handshake was sent to multiple recipients (applicable to only some policy types) and all recipients have responded, allowing the originator to complete the handshake action. 
               
              * **CANCELED** : This handshake is no longer active because it was canceled by the originating account. 
               
              * **ACCEPTED** : This handshake is complete because it has been accepted by the recipient. 
               
              * **DECLINED** : This handshake is no longer active because it was declined by the recipient account. 
               
              * **EXPIRED** : This handshake is no longer active because the originator did not receive a response of any kind from the recipient before the expiration time (15 days). 
               

              
            

            - **RequestedTimestamp** *(datetime) --* 

              The date and time that the handshake request was made.

              
            

            - **ExpirationTimestamp** *(datetime) --* 

              The date and time that the handshake expires. If the recipient of the handshake request fails to respond before the specified date and time, the handshake becomes inactive and is no longer valid.

              
            

            - **Action** *(string) --* 

              The type of handshake, indicating what action occurs when the recipient accepts the handshake. The following handshake types are supported:

               

               
              * **INVITE** : This type of handshake represents a request to join an organization. It is always sent from the master account to only non-member accounts. 
               
              * **ENABLE_ALL_FEATURES** : This type of handshake represents a request to enable all features in an organization. It is always sent from the master account to only *invited* member accounts. Created accounts do not receive this because those accounts were created by the organization's master account and approval is inferred. 
               
              * **APPROVE_ALL_FEATURES** : This type of handshake is sent from the Organizations service when all member accounts have approved the ``ENABLE_ALL_FEATURES`` invitation. It is sent only to the master account and signals the master that it can finalize the process to enable all features. 
               

              
            

            - **Resources** *(list) --* 

              Additional information that is needed to process the handshake.

              
              

              - *(dict) --* 

                Contains additional data that is needed to process a handshake.

                
                

                - **Value** *(string) --* 

                  The information that is passed to the other party in the handshake. The format of the value string must match the requirements of the specified type.

                  
                

                - **Type** *(string) --* 

                  The type of information being passed, specifying how the value is to be interpreted by the other party:

                   

                   
                  * ``ACCOUNT`` - Specifies an AWS account ID number. 
                   
                  * ``ORGANIZATION`` - Specifies an organization ID number. 
                   
                  * ``EMAIL`` - Specifies the email address that is associated with the account that receives the handshake.  
                   
                  * ``OWNER_EMAIL`` - Specifies the email address associated with the master account. Included as information about an organization.  
                   
                  * ``OWNER_NAME`` - Specifies the name associated with the master account. Included as information about an organization.  
                   
                  * ``NOTES`` - Additional text provided by the handshake initiator and intended for the recipient to read. 
                   

                  
                

                - **Resources** *(list) --* 

                  When needed, contains an additional array of ``HandshakeResource`` objects.

                  
            
          
        
      
    

.. py:class:: Organizations.Paginator.ListOrganizationalUnitsForParent

  ::

    
    paginator = client.get_paginator('list_organizational_units_for_parent')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Organizations.Client.list_organizational_units_for_parent`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListOrganizationalUnitsForParent>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          ParentId='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type ParentId: string
    :param ParentId: **[REQUIRED]** 

      The unique identifier (ID) of the root or OU whose child OUs you want to list.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a parent ID string requires one of the following:

       

       
      * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits. 
       
      * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits. 
       

      

    
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
            'OrganizationalUnits': [
                {
                    'Id': 'string',
                    'Arn': 'string',
                    'Name': 'string'
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **OrganizationalUnits** *(list) --* 

          A list of the OUs in the specified root or parent OU.

          
          

          - *(dict) --* 

            Contains details about an organizational unit (OU). An OU is a container of AWS accounts within a root of an organization. Policies that are attached to an OU apply to all accounts contained in that OU and in any child OUs.

            
            

            - **Id** *(string) --* 

              The unique identifier (ID) associated with this OU.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for an organizational unit ID string requires "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits.

              
            

            - **Arn** *(string) --* 

              The Amazon Resource Name (ARN) of this OU.

               

              For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

              
            

            - **Name** *(string) --* 

              The friendly name of this OU.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

              
        
      
    

.. py:class:: Organizations.Paginator.ListParents

  ::

    
    paginator = client.get_paginator('list_parents')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Organizations.Client.list_parents`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListParents>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          ChildId='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type ChildId: string
    :param ChildId: **[REQUIRED]** 

      The unique identifier (ID) of the OU or account whose parent containers you want to list. Do not specify a root.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a child ID string requires one of the following:

       

       
      * Account: a string that consists of exactly 12 digits. 
       
      * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that contains the OU) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits. 
       

      

    
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
            'Parents': [
                {
                    'Id': 'string',
                    'Type': 'ROOT'|'ORGANIZATIONAL_UNIT'
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Parents** *(list) --* 

          A list of parents for the specified child account or OU.

          
          

          - *(dict) --* 

            Contains information about either a root or an organizational unit (OU) that can contain OUs or accounts in an organization.

            
            

            - **Id** *(string) --* 

              The unique identifier (ID) of the parent entity.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a parent ID string requires one of the following:

               

               
              * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits. 
               
              * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits. 
               

              
            

            - **Type** *(string) --* 

              The type of the parent entity.

              
        
      
    

.. py:class:: Organizations.Paginator.ListPolicies

  ::

    
    paginator = client.get_paginator('list_policies')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Organizations.Client.list_policies`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListPolicies>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          Filter='SERVICE_CONTROL_POLICY',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type Filter: string
    :param Filter: **[REQUIRED]** 

      Specifies the type of policy that you want to include in the response.

      

    
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
            'Policies': [
                {
                    'Id': 'string',
                    'Arn': 'string',
                    'Name': 'string',
                    'Description': 'string',
                    'Type': 'SERVICE_CONTROL_POLICY',
                    'AwsManaged': True|False
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Policies** *(list) --* 

          A list of policies that match the filter criteria in the request. The output list does not include the policy contents. To see the content for a policy, see  DescribePolicy .

          
          

          - *(dict) --* 

            Contains information about a policy, but does not include the content. To see the content of a policy, see  DescribePolicy .

            
            

            - **Id** *(string) --* 

              The unique identifier (ID) of the policy.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires "p-" followed by from 8 to 128 lower-case letters or digits.

              
            

            - **Arn** *(string) --* 

              The Amazon Resource Name (ARN) of the policy.

               

              For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

              
            

            - **Name** *(string) --* 

              The friendly name of the policy.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

              
            

            - **Description** *(string) --* 

              The description of the policy.

              
            

            - **Type** *(string) --* 

              The type of policy.

              
            

            - **AwsManaged** *(boolean) --* 

              A boolean value that indicates whether the specified policy is an AWS managed policy. If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.

              
        
      
    

.. py:class:: Organizations.Paginator.ListPoliciesForTarget

  ::

    
    paginator = client.get_paginator('list_policies_for_target')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Organizations.Client.list_policies_for_target`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListPoliciesForTarget>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          TargetId='string',
          Filter='SERVICE_CONTROL_POLICY',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type TargetId: string
    :param TargetId: **[REQUIRED]** 

      The unique identifier (ID) of the root, organizational unit, or account whose policies you want to list.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a target ID string requires one of the following:

       

       
      * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits. 
       
      * Account: a string that consists of exactly 12 digits. 
       
      * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits. 
       

      

    
    :type Filter: string
    :param Filter: **[REQUIRED]** 

      The type of policy that you want to include in the returned list.

      

    
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
            'Policies': [
                {
                    'Id': 'string',
                    'Arn': 'string',
                    'Name': 'string',
                    'Description': 'string',
                    'Type': 'SERVICE_CONTROL_POLICY',
                    'AwsManaged': True|False
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Policies** *(list) --* 

          The list of policies that match the criteria in the request.

          
          

          - *(dict) --* 

            Contains information about a policy, but does not include the content. To see the content of a policy, see  DescribePolicy .

            
            

            - **Id** *(string) --* 

              The unique identifier (ID) of the policy.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires "p-" followed by from 8 to 128 lower-case letters or digits.

              
            

            - **Arn** *(string) --* 

              The Amazon Resource Name (ARN) of the policy.

               

              For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

              
            

            - **Name** *(string) --* 

              The friendly name of the policy.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

              
            

            - **Description** *(string) --* 

              The description of the policy.

              
            

            - **Type** *(string) --* 

              The type of policy.

              
            

            - **AwsManaged** *(boolean) --* 

              A boolean value that indicates whether the specified policy is an AWS managed policy. If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.

              
        
      
    

.. py:class:: Organizations.Paginator.ListRoots

  ::

    
    paginator = client.get_paginator('list_roots')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Organizations.Client.list_roots`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListRoots>`_    


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
            'Roots': [
                {
                    'Id': 'string',
                    'Arn': 'string',
                    'Name': 'string',
                    'PolicyTypes': [
                        {
                            'Type': 'SERVICE_CONTROL_POLICY',
                            'Status': 'ENABLED'|'PENDING_ENABLE'|'PENDING_DISABLE'
                        },
                    ]
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Roots** *(list) --* 

          A list of roots that are defined in an organization.

          
          

          - *(dict) --* 

            Contains details about a root. A root is a top-level parent node in the hierarchy of an organization that can contain organizational units (OUs) and accounts. Every root contains every AWS account in the organization. Each root enables the accounts to be organized in a different way and to have different policy types enabled for use in that root.

            
            

            - **Id** *(string) --* 

              The unique identifier (ID) for the root.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a root ID string requires "r-" followed by from 4 to 32 lower-case letters or digits.

              
            

            - **Arn** *(string) --* 

              The Amazon Resource Name (ARN) of the root.

               

              For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

              
            

            - **Name** *(string) --* 

              The friendly name of the root.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

              
            

            - **PolicyTypes** *(list) --* 

              The types of policies that are currently enabled for the root and therefore can be attached to the root or to its OUs or accounts.

              
              

              - *(dict) --* 

                Contains information about a policy type and its status in the associated root.

                
                

                - **Type** *(string) --* 

                  The name of the policy type.

                  
                

                - **Status** *(string) --* 

                  The status of the policy type as it relates to the associated root. To attach a policy of the specified type to a root or to an OU or account in that root, it must be available in the organization and enabled for that root.

                  
            
          
        
      
    

.. py:class:: Organizations.Paginator.ListTargetsForPolicy

  ::

    
    paginator = client.get_paginator('list_targets_for_policy')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Organizations.Client.list_targets_for_policy`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/organizations-2016-11-28/ListTargetsForPolicy>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          PolicyId='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type PolicyId: string
    :param PolicyId: **[REQUIRED]** 

      The unique identifier (ID) of the policy for which you want to know its attachments.

       

      The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a policy ID string requires "p-" followed by from 8 to 128 lower-case letters or digits.

      

    
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
            'Targets': [
                {
                    'TargetId': 'string',
                    'Arn': 'string',
                    'Name': 'string',
                    'Type': 'ACCOUNT'|'ORGANIZATIONAL_UNIT'|'ROOT'
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Targets** *(list) --* 

          A list of structures, each of which contains details about one of the entities to which the specified policy is attached.

          
          

          - *(dict) --* 

            Contains information about a root, OU, or account that a policy is attached to.

            
            

            - **TargetId** *(string) --* 

              The unique identifier (ID) of the policy target.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ for a target ID string requires one of the following:

               

               
              * Root: a string that begins with "r-" followed by from 4 to 32 lower-case letters or digits. 
               
              * Account: a string that consists of exactly 12 digits. 
               
              * Organizational unit (OU): a string that begins with "ou-" followed by from 4 to 32 lower-case letters or digits (the ID of the root that the OU is in) followed by a second "-" dash and from 8 to 32 additional lower-case letters or digits. 
               

              
            

            - **Arn** *(string) --* 

              The Amazon Resource Name (ARN) of the policy target.

               

              For more information about ARNs in Organizations, see `ARN Formats Supported by Organizations <http://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions.html#orgs-permissions-arns>`__ in the *AWS Organizations User Guide* .

              
            

            - **Name** *(string) --* 

              The friendly name of the policy target.

               

              The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

              
            

            - **Type** *(string) --* 

              The type of the policy target.

              
        
      
    