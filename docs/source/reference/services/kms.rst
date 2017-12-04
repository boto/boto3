

***
KMS
***

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: KMS.Client

  A low-level client representing AWS Key Management Service (KMS)::

    
    import boto3
    
    client = boto3.client('kms')

  
  These are the available methods:
  
  *   :py:meth:`~KMS.Client.can_paginate`

  
  *   :py:meth:`~KMS.Client.cancel_key_deletion`

  
  *   :py:meth:`~KMS.Client.create_alias`

  
  *   :py:meth:`~KMS.Client.create_grant`

  
  *   :py:meth:`~KMS.Client.create_key`

  
  *   :py:meth:`~KMS.Client.decrypt`

  
  *   :py:meth:`~KMS.Client.delete_alias`

  
  *   :py:meth:`~KMS.Client.delete_imported_key_material`

  
  *   :py:meth:`~KMS.Client.describe_key`

  
  *   :py:meth:`~KMS.Client.disable_key`

  
  *   :py:meth:`~KMS.Client.disable_key_rotation`

  
  *   :py:meth:`~KMS.Client.enable_key`

  
  *   :py:meth:`~KMS.Client.enable_key_rotation`

  
  *   :py:meth:`~KMS.Client.encrypt`

  
  *   :py:meth:`~KMS.Client.generate_data_key`

  
  *   :py:meth:`~KMS.Client.generate_data_key_without_plaintext`

  
  *   :py:meth:`~KMS.Client.generate_presigned_url`

  
  *   :py:meth:`~KMS.Client.generate_random`

  
  *   :py:meth:`~KMS.Client.get_key_policy`

  
  *   :py:meth:`~KMS.Client.get_key_rotation_status`

  
  *   :py:meth:`~KMS.Client.get_paginator`

  
  *   :py:meth:`~KMS.Client.get_parameters_for_import`

  
  *   :py:meth:`~KMS.Client.get_waiter`

  
  *   :py:meth:`~KMS.Client.import_key_material`

  
  *   :py:meth:`~KMS.Client.list_aliases`

  
  *   :py:meth:`~KMS.Client.list_grants`

  
  *   :py:meth:`~KMS.Client.list_key_policies`

  
  *   :py:meth:`~KMS.Client.list_keys`

  
  *   :py:meth:`~KMS.Client.list_resource_tags`

  
  *   :py:meth:`~KMS.Client.list_retirable_grants`

  
  *   :py:meth:`~KMS.Client.put_key_policy`

  
  *   :py:meth:`~KMS.Client.re_encrypt`

  
  *   :py:meth:`~KMS.Client.retire_grant`

  
  *   :py:meth:`~KMS.Client.revoke_grant`

  
  *   :py:meth:`~KMS.Client.schedule_key_deletion`

  
  *   :py:meth:`~KMS.Client.tag_resource`

  
  *   :py:meth:`~KMS.Client.untag_resource`

  
  *   :py:meth:`~KMS.Client.update_alias`

  
  *   :py:meth:`~KMS.Client.update_key_description`

  

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


  .. py:method:: cancel_key_deletion(**kwargs)

    

    Cancels the deletion of a customer master key (CMK). When this operation is successful, the CMK is set to the ``Disabled`` state. To enable a CMK, use  EnableKey . You cannot perform this operation on a CMK in a different AWS account.

     

    For more information about scheduling and canceling deletion of a CMK, see `Deleting Customer Master Keys <http://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html>`__ in the *AWS Key Management Service Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/CancelKeyDeletion>`_    


    **Request Syntax** 
    ::

      response = client.cancel_key_deletion(
          KeyId='string'
      )
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      The unique identifier for the customer master key (CMK) for which to cancel deletion.

       

      Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'KeyId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **KeyId** *(string) --* 

          The unique identifier of the master key for which deletion is canceled.

          
    

    **Examples** 

    The following example cancels deletion of the specified CMK.
    ::

      response = client.cancel_key_deletion(
          # The identifier of the CMK whose deletion you are canceling. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
          KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          # The ARN of the CMK whose deletion you canceled.
          'KeyId': 'arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_alias(**kwargs)

    

    Creates a display name for a customer master key (CMK). You can use an alias to identify a CMK in selected operations, such as  Encrypt and  GenerateDataKey . 

     

    Each CMK can have multiple aliases, but each alias points to only one CMK. The alias name must be unique in the AWS account and region. To simplify code that runs in multiple regions, use the same alias name, but point it to a different CMK in each region. 

     

    Because an alias is not a property of a CMK, you can delete and change the aliases of a CMK without affecting the CMK. Also, aliases do not appear in the response from the  DescribeKey operation. To get the aliases of all CMKs, use the  ListAliases operation.

     

    An alias must start with the word ``alias`` followed by a forward slash (``alias/`` ). The alias name can contain only alphanumeric characters, forward slashes (/), underscores (_), and dashes (-). Alias names cannot begin with ``aws`` ; that alias name prefix is reserved by Amazon Web Services (AWS).

     

    The alias and the CMK it is mapped to must be in the same AWS account and the same region. You cannot perform this operation on an alias in a different AWS account.

     

    To map an existing alias to a different CMK, call  UpdateAlias .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/CreateAlias>`_    


    **Request Syntax** 
    ::

      response = client.create_alias(
          AliasName='string',
          TargetKeyId='string'
      )
    :type AliasName: string
    :param AliasName: **[REQUIRED]** 

      String that contains the display name. The name must start with the word "alias" followed by a forward slash (alias/). Aliases that begin with "alias/AWS" are reserved.

      

    
    :type TargetKeyId: string
    :param TargetKeyId: **[REQUIRED]** 

      Identifies the CMK for which you are creating the alias. This value cannot be an alias.

       

      Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

      

    
    
    :returns: None

    **Examples** 

    The following example creates an alias for the specified customer master key (CMK).
    ::

      response = client.create_alias(
          # The alias to create. Aliases must begin with 'alias/'. Do not use aliases that begin with 'alias/aws' because they are reserved for use by AWS.
          AliasName='alias/ExampleAlias',
          # The identifier of the CMK whose alias you are creating. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
          TargetKeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_grant(**kwargs)

    

    Adds a grant to a customer master key (CMK). The grant specifies who can use the CMK and under what conditions. When setting permissions, grants are an alternative to key policies. 

     

    To perform this operation on a CMK in a different AWS account, specify the key ARN in the value of the KeyId parameter. For more information about grants, see `Grants <http://docs.aws.amazon.com/kms/latest/developerguide/grants.html>`__ in the *AWS Key Management Service Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/CreateGrant>`_    


    **Request Syntax** 
    ::

      response = client.create_grant(
          KeyId='string',
          GranteePrincipal='string',
          RetiringPrincipal='string',
          Operations=[
              'Decrypt'|'Encrypt'|'GenerateDataKey'|'GenerateDataKeyWithoutPlaintext'|'ReEncryptFrom'|'ReEncryptTo'|'CreateGrant'|'RetireGrant'|'DescribeKey',
          ],
          Constraints={
              'EncryptionContextSubset': {
                  'string': 'string'
              },
              'EncryptionContextEquals': {
                  'string': 'string'
              }
          },
          GrantTokens=[
              'string',
          ],
          Name='string'
      )
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      The unique identifier for the customer master key (CMK) that the grant applies to.

       

      Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

      

    
    :type GranteePrincipal: string
    :param GranteePrincipal: **[REQUIRED]** 

      The principal that is given permission to perform the operations that the grant permits.

       

      To specify the principal, use the `Amazon Resource Name (ARN) <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ of an AWS principal. Valid AWS principals include AWS accounts (root), IAM users, IAM roles, federated users, and assumed role users. For examples of the ARN syntax to use for specifying a principal, see `AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-iam>`__ in the Example ARNs section of the *AWS General Reference* .

      

    
    :type RetiringPrincipal: string
    :param RetiringPrincipal: 

      The principal that is given permission to retire the grant by using  RetireGrant operation.

       

      To specify the principal, use the `Amazon Resource Name (ARN) <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ of an AWS principal. Valid AWS principals include AWS accounts (root), IAM users, federated users, and assumed role users. For examples of the ARN syntax to use for specifying a principal, see `AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-iam>`__ in the Example ARNs section of the *AWS General Reference* .

      

    
    :type Operations: list
    :param Operations: **[REQUIRED]** 

      A list of operations that the grant permits.

      

    
      - *(string) --* 

      
  
    :type Constraints: dict
    :param Constraints: 

      A structure that you can use to allow certain operations in the grant only when the desired encryption context is present. For more information about encryption context, see `Encryption Context <http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html>`__ in the *AWS Key Management Service Developer Guide* .

      

    
      - **EncryptionContextSubset** *(dict) --* 

        A list of key-value pairs, all of which must be present in the encryption context of certain subsequent operations that the grant allows. When certain subsequent operations allowed by the grant include encryption context that matches this list or is a superset of this list, the grant allows the operation. Otherwise, the grant does not allow the operation.

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
      - **EncryptionContextEquals** *(dict) --* 

        A list of key-value pairs that must be present in the encryption context of certain subsequent operations that the grant allows. When certain subsequent operations allowed by the grant include encryption context that matches this list, the grant allows the operation. Otherwise, the grant does not allow the operation.

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
    
    :type GrantTokens: list
    :param GrantTokens: 

      A list of grant tokens.

       

      For more information, see `Grant Tokens <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in the *AWS Key Management Service Developer Guide* .

      

    
      - *(string) --* 

      
  
    :type Name: string
    :param Name: 

      A friendly name for identifying the grant. Use this value to prevent unintended creation of duplicate grants when retrying this request.

       

      When this value is absent, all ``CreateGrant`` requests result in a new grant with a unique ``GrantId`` even if all the supplied parameters are identical. This can result in unintended duplicates when you retry the ``CreateGrant`` request.

       

      When this value is present, you can retry a ``CreateGrant`` request with identical parameters; if the grant already exists, the original ``GrantId`` is returned without creating a new grant. Note that the returned grant token is unique with every ``CreateGrant`` request, even when a duplicate ``GrantId`` is returned. All grant tokens obtained in this way can be used interchangeably.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'GrantToken': 'string',
            'GrantId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **GrantToken** *(string) --* 

          The grant token.

           

          For more information, see `Grant Tokens <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in the *AWS Key Management Service Developer Guide* .

          
        

        - **GrantId** *(string) --* 

          The unique identifier for the grant.

           

          You can use the ``GrantId`` in a subsequent  RetireGrant or  RevokeGrant operation.

          
    

    **Examples** 

    The following example creates a grant that allows the specified IAM role to encrypt data with the specified customer master key (CMK).
    ::

      response = client.create_grant(
          # The identity that is given permission to perform the operations specified in the grant.
          GranteePrincipal='arn:aws:iam::111122223333:role/ExampleRole',
          # The identifier of the CMK to which the grant applies. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
          KeyId='arn:aws:kms:us-east-2:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab',
          # A list of operations that the grant allows.
          Operations=[
              'Encrypt',
              'Decrypt',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          # The unique identifier of the grant.
          'GrantId': '0c237476b39f8bc44e45212e08498fbe3151305030726c0590dd8d3e9f3d6a60',
          # The grant token.
          'GrantToken': 'AQpAM2RhZTk1MGMyNTk2ZmZmMzEyYWVhOWViN2I1MWM4Mzc0MWFiYjc0ZDE1ODkyNGFlNTIzODZhMzgyZjBlNGY3NiKIAgEBAgB4Pa6VDCWW__MSrqnre1HIN0Grt00ViSSuUjhqOC8OT3YAAADfMIHcBgkqhkiG9w0BBwaggc4wgcsCAQAwgcUGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMmqLyBTAegIn9XlK5AgEQgIGXZQjkBcl1dykDdqZBUQ6L1OfUivQy7JVYO2-ZJP7m6f1g8GzV47HX5phdtONAP7K_HQIflcgpkoCqd_fUnE114mSmiagWkbQ5sqAVV3ov-VeqgrvMe5ZFEWLMSluvBAqdjHEdMIkHMlhlj4ENZbzBfo9Wxk8b8SnwP4kc4gGivedzFXo-dwN8fxjjq_ZZ9JFOj2ijIbj5FyogDCN0drOfi8RORSEuCEmPvjFRMFAwcmwFkN2NPp89amA',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_key(**kwargs)

    

    Creates a customer master key (CMK) in the caller's AWS account.

     

    You can use a CMK to encrypt small amounts of data (4 KiB or less) directly, but CMKs are more commonly used to encrypt data encryption keys (DEKs), which are used to encrypt raw data. For more information about DEKs and the difference between CMKs and DEKs, see the following:

     

     
    * The  GenerateDataKey operation 
     
    * `AWS Key Management Service Concepts <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`__ in the *AWS Key Management Service Developer Guide*   
     

     

    You cannot use this operation to create a CMK in a different AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/CreateKey>`_    


    **Request Syntax** 
    ::

      response = client.create_key(
          Policy='string',
          Description='string',
          KeyUsage='ENCRYPT_DECRYPT',
          Origin='AWS_KMS'|'EXTERNAL',
          BypassPolicyLockoutSafetyCheck=True|False,
          Tags=[
              {
                  'TagKey': 'string',
                  'TagValue': 'string'
              },
          ]
      )
    :type Policy: string
    :param Policy: 

      The key policy to attach to the CMK.

       

      If you specify a policy and do not set ``BypassPolicyLockoutSafetyCheck`` to true, the policy must meet the following criteria:

       

       
      * It must allow the principal that is making the ``CreateKey`` request to make a subsequent  PutKeyPolicy request on the CMK. This reduces the likelihood that the CMK becomes unmanageable. For more information, refer to the scenario in the `Default Key Policy <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam>`__ section in the *AWS Key Management Service Developer Guide* . 
       
      * The principals that are specified in the key policy must exist and be visible to AWS KMS. When you create a new AWS principal (for example, an IAM user or role), you might need to enforce a delay before specifying the new principal in a key policy because the new principal might not immediately be visible to AWS KMS. For more information, see `Changes that I make are not always immediately visible <http://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency>`__ in the *IAM User Guide* . 
       

       

      If you do not specify a policy, AWS KMS attaches a default key policy to the CMK. For more information, see `Default Key Policy <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default>`__ in the *AWS Key Management Service Developer Guide* .

       

      The policy size limit is 32 kilobytes (32768 bytes).

      

    
    :type Description: string
    :param Description: 

      A description of the CMK.

       

      Use a description that helps you decide whether the CMK is appropriate for a task.

      

    
    :type KeyUsage: string
    :param KeyUsage: 

      The intended use of the CMK.

       

      You can use CMKs only for symmetric encryption and decryption.

      

    
    :type Origin: string
    :param Origin: 

      The source of the CMK's key material.

       

      The default is ``AWS_KMS`` , which means AWS KMS creates the key material. When this parameter is set to ``EXTERNAL`` , the request creates a CMK without key material so that you can import key material from your existing key management infrastructure. For more information about importing key material into AWS KMS, see `Importing Key Material <http://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html>`__ in the *AWS Key Management Service Developer Guide* .

       

      The CMK's ``Origin`` is immutable and is set when the CMK is created.

      

    
    :type BypassPolicyLockoutSafetyCheck: boolean
    :param BypassPolicyLockoutSafetyCheck: 

      A flag to indicate whether to bypass the key policy lockout safety check.

       

      .. warning::

         

        Setting this value to true increases the likelihood that the CMK becomes unmanageable. Do not set this value to true indiscriminately.

         

        For more information, refer to the scenario in the `Default Key Policy <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam>`__ section in the *AWS Key Management Service Developer Guide* .

         

       

      Use this parameter only when you include a policy in the request and you intend to prevent the principal that is making the request from making a subsequent  PutKeyPolicy request on the CMK.

       

      The default value is false.

      

    
    :type Tags: list
    :param Tags: 

      One or more tags. Each tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.

       

      Use this parameter to tag the CMK when it is created. Alternately, you can omit this parameter and instead tag the CMK after it is created using  TagResource .

      

    
      - *(dict) --* 

        A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.

         

        For information about the rules that apply to tag keys and tag values, see `User-Defined Tag Restrictions <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html>`__ in the *AWS Billing and Cost Management User Guide* .

        

      
        - **TagKey** *(string) --* **[REQUIRED]** 

          The key of the tag.

          

        
        - **TagValue** *(string) --* **[REQUIRED]** 

          The value of the tag.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'KeyMetadata': {
                'AWSAccountId': 'string',
                'KeyId': 'string',
                'Arn': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'Enabled': True|False,
                'Description': 'string',
                'KeyUsage': 'ENCRYPT_DECRYPT',
                'KeyState': 'Enabled'|'Disabled'|'PendingDeletion'|'PendingImport',
                'DeletionDate': datetime(2015, 1, 1),
                'ValidTo': datetime(2015, 1, 1),
                'Origin': 'AWS_KMS'|'EXTERNAL',
                'ExpirationModel': 'KEY_MATERIAL_EXPIRES'|'KEY_MATERIAL_DOES_NOT_EXPIRE',
                'KeyManager': 'AWS'|'CUSTOMER'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **KeyMetadata** *(dict) --* 

          Metadata associated with the CMK.

          
          

          - **AWSAccountId** *(string) --* 

            The twelve-digit account ID of the AWS account that owns the CMK.

            
          

          - **KeyId** *(string) --* 

            The globally unique identifier for the CMK.

            
          

          - **Arn** *(string) --* 

            The Amazon Resource Name (ARN) of the CMK. For examples, see `AWS Key Management Service (AWS KMS) <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kms>`__ in the Example ARNs section of the *AWS General Reference* .

            
          

          - **CreationDate** *(datetime) --* 

            The date and time when the CMK was created.

            
          

          - **Enabled** *(boolean) --* 

            Specifies whether the CMK is enabled. When ``KeyState`` is ``Enabled`` this value is true, otherwise it is false.

            
          

          - **Description** *(string) --* 

            The description of the CMK.

            
          

          - **KeyUsage** *(string) --* 

            The cryptographic operations for which you can use the CMK. Currently the only allowed value is ``ENCRYPT_DECRYPT`` , which means you can use the CMK for the  Encrypt and  Decrypt operations.

            
          

          - **KeyState** *(string) --* 

            The state of the CMK.

             

            For more information about how key state affects the use of a CMK, see `How Key State Affects the Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .

            
          

          - **DeletionDate** *(datetime) --* 

            The date and time after which AWS KMS deletes the CMK. This value is present only when ``KeyState`` is ``PendingDeletion`` , otherwise this value is omitted.

            
          

          - **ValidTo** *(datetime) --* 

            The time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. This value is present only for CMKs whose ``Origin`` is ``EXTERNAL`` and whose ``ExpirationModel`` is ``KEY_MATERIAL_EXPIRES`` , otherwise this value is omitted.

            
          

          - **Origin** *(string) --* 

            The source of the CMK's key material. When this value is ``AWS_KMS`` , AWS KMS created the key material. When this value is ``EXTERNAL`` , the key material was imported from your existing key management infrastructure or the CMK lacks key material.

            
          

          - **ExpirationModel** *(string) --* 

            Specifies whether the CMK's key material expires. This value is present only when ``Origin`` is ``EXTERNAL`` , otherwise this value is omitted.

            
          

          - **KeyManager** *(string) --* 

            The CMK's manager. CMKs are either customer-managed or AWS-managed. For more information about the difference, see `Customer Master Keys <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys>`__ in the *AWS Key Management Service Developer Guide* .

            
      
    

    **Examples** 

    The following example creates a CMK.
    ::

      response = client.create_key(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          # An object that contains information about the CMK created by this operation.
          'KeyMetadata': {
              'AWSAccountId': '111122223333',
              'Arn': 'arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
              'CreationDate': datetime(2016, 11, 1, 10, 15, 42, 1, 306, 0),
              'Description': '',
              'Enabled': True,
              'KeyId': '1234abcd-12ab-34cd-56ef-1234567890ab',
              'KeyState': 'Enabled',
              'KeyUsage': 'ENCRYPT_DECRYPT',
              'Origin': 'AWS_KMS',
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: decrypt(**kwargs)

    

    Decrypts ciphertext. Ciphertext is plaintext that has been previously encrypted by using any of the following operations:

     

     
    *  GenerateDataKey   
     
    *  GenerateDataKeyWithoutPlaintext   
     
    *  Encrypt   
     

     

    Note that if a caller has been granted access permissions to all keys (through, for example, IAM user policies that grant ``Decrypt`` permission on all resources), then ciphertext encrypted by using keys in other accounts where the key grants access to the caller can be decrypted. To remedy this, we recommend that you do not grant ``Decrypt`` access in an IAM user policy. Instead grant ``Decrypt`` access only in key policies. If you must grant ``Decrypt`` access in an IAM user policy, you should scope the resource to specific keys or to specific trusted accounts.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/Decrypt>`_    


    **Request Syntax** 
    ::

      response = client.decrypt(
          CiphertextBlob=b'bytes',
          EncryptionContext={
              'string': 'string'
          },
          GrantTokens=[
              'string',
          ]
      )
    :type CiphertextBlob: bytes
    :param CiphertextBlob: **[REQUIRED]** 

      Ciphertext to be decrypted. The blob includes metadata.

      

    
    :type EncryptionContext: dict
    :param EncryptionContext: 

      The encryption context. If this was specified in the  Encrypt function, it must be specified here or the decryption operation will fail. For more information, see `Encryption Context <http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html>`__ .

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type GrantTokens: list
    :param GrantTokens: 

      A list of grant tokens.

       

      For more information, see `Grant Tokens <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in the *AWS Key Management Service Developer Guide* .

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'KeyId': 'string',
            'Plaintext': b'bytes'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **KeyId** *(string) --* 

          ARN of the key used to perform the decryption. This value is returned if no errors are encountered during the operation.

          
        

        - **Plaintext** *(bytes) --* 

          Decrypted plaintext data. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not encoded.

          
    

    **Examples** 

    The following example decrypts data that was encrypted with a customer master key (CMK) in AWS KMS.
    ::

      response = client.decrypt(
          # The encrypted data (ciphertext).
          CiphertextBlob='<binary data>',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          # The Amazon Resource Name (ARN) of the CMK that was used to decrypt the data.
          'KeyId': 'arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
          # The decrypted (plaintext) data.
          'Plaintext': '<binary data>',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_alias(**kwargs)

    

    Deletes the specified alias. You cannot perform this operation on an alias in a different AWS account. 

     

    Because an alias is not a property of a CMK, you can delete and change the aliases of a CMK without affecting the CMK. Also, aliases do not appear in the response from the  DescribeKey operation. To get the aliases of all CMKs, use the  ListAliases operation. 

     

    Each CMK can have multiple aliases. To change the alias of a CMK, use  DeleteAlias to delete the current alias and  CreateAlias to create a new alias. To associate an existing alias with a different customer master key (CMK), call  UpdateAlias .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DeleteAlias>`_    


    **Request Syntax** 
    ::

      response = client.delete_alias(
          AliasName='string'
      )
    :type AliasName: string
    :param AliasName: **[REQUIRED]** 

      The alias to be deleted. The name must start with the word "alias" followed by a forward slash (alias/). Aliases that begin with "alias/aws" are reserved.

      

    
    
    :returns: None

    **Examples** 

    The following example deletes the specified alias.
    ::

      response = client.delete_alias(
          # The alias to delete.
          AliasName='alias/ExampleAlias',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_imported_key_material(**kwargs)

    

    Deletes key material that you previously imported. This operation makes the specified customer master key (CMK) unusable. For more information about importing key material into AWS KMS, see `Importing Key Material <http://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html>`__ in the *AWS Key Management Service Developer Guide* . You cannot perform this operation on a CMK in a different AWS account.

     

    When the specified CMK is in the ``PendingDeletion`` state, this operation does not change the CMK's state. Otherwise, it changes the CMK's state to ``PendingImport`` .

     

    After you delete key material, you can use  ImportKeyMaterial to reimport the same key material into the CMK.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DeleteImportedKeyMaterial>`_    


    **Request Syntax** 
    ::

      response = client.delete_imported_key_material(
          KeyId='string'
      )
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      The identifier of the CMK whose key material to delete. The CMK's ``Origin`` must be ``EXTERNAL`` .

       

      Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

      

    
    
    :returns: None

    **Examples** 

    The following example deletes the imported key material from the specified customer master key (CMK).
    ::

      response = client.delete_imported_key_material(
          # The identifier of the CMK whose imported key material you are deleting. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
          KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_key(**kwargs)

    

    Provides detailed information about the specified customer master key (CMK).

     

    To perform this operation on a CMK in a different AWS account, specify the key ARN or alias ARN in the value of the KeyId parameter.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DescribeKey>`_    


    **Request Syntax** 
    ::

      response = client.describe_key(
          KeyId='string',
          GrantTokens=[
              'string',
          ]
      )
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      A unique identifier for the customer master key (CMK).

       

      To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with "alias/". To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Alias name: ``alias/ExampleAlias``   
       
      * Alias ARN: ``arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias name and alias ARN, use  ListAliases .

      

    
    :type GrantTokens: list
    :param GrantTokens: 

      A list of grant tokens.

       

      For more information, see `Grant Tokens <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in the *AWS Key Management Service Developer Guide* .

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'KeyMetadata': {
                'AWSAccountId': 'string',
                'KeyId': 'string',
                'Arn': 'string',
                'CreationDate': datetime(2015, 1, 1),
                'Enabled': True|False,
                'Description': 'string',
                'KeyUsage': 'ENCRYPT_DECRYPT',
                'KeyState': 'Enabled'|'Disabled'|'PendingDeletion'|'PendingImport',
                'DeletionDate': datetime(2015, 1, 1),
                'ValidTo': datetime(2015, 1, 1),
                'Origin': 'AWS_KMS'|'EXTERNAL',
                'ExpirationModel': 'KEY_MATERIAL_EXPIRES'|'KEY_MATERIAL_DOES_NOT_EXPIRE',
                'KeyManager': 'AWS'|'CUSTOMER'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **KeyMetadata** *(dict) --* 

          Metadata associated with the key.

          
          

          - **AWSAccountId** *(string) --* 

            The twelve-digit account ID of the AWS account that owns the CMK.

            
          

          - **KeyId** *(string) --* 

            The globally unique identifier for the CMK.

            
          

          - **Arn** *(string) --* 

            The Amazon Resource Name (ARN) of the CMK. For examples, see `AWS Key Management Service (AWS KMS) <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kms>`__ in the Example ARNs section of the *AWS General Reference* .

            
          

          - **CreationDate** *(datetime) --* 

            The date and time when the CMK was created.

            
          

          - **Enabled** *(boolean) --* 

            Specifies whether the CMK is enabled. When ``KeyState`` is ``Enabled`` this value is true, otherwise it is false.

            
          

          - **Description** *(string) --* 

            The description of the CMK.

            
          

          - **KeyUsage** *(string) --* 

            The cryptographic operations for which you can use the CMK. Currently the only allowed value is ``ENCRYPT_DECRYPT`` , which means you can use the CMK for the  Encrypt and  Decrypt operations.

            
          

          - **KeyState** *(string) --* 

            The state of the CMK.

             

            For more information about how key state affects the use of a CMK, see `How Key State Affects the Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .

            
          

          - **DeletionDate** *(datetime) --* 

            The date and time after which AWS KMS deletes the CMK. This value is present only when ``KeyState`` is ``PendingDeletion`` , otherwise this value is omitted.

            
          

          - **ValidTo** *(datetime) --* 

            The time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. This value is present only for CMKs whose ``Origin`` is ``EXTERNAL`` and whose ``ExpirationModel`` is ``KEY_MATERIAL_EXPIRES`` , otherwise this value is omitted.

            
          

          - **Origin** *(string) --* 

            The source of the CMK's key material. When this value is ``AWS_KMS`` , AWS KMS created the key material. When this value is ``EXTERNAL`` , the key material was imported from your existing key management infrastructure or the CMK lacks key material.

            
          

          - **ExpirationModel** *(string) --* 

            Specifies whether the CMK's key material expires. This value is present only when ``Origin`` is ``EXTERNAL`` , otherwise this value is omitted.

            
          

          - **KeyManager** *(string) --* 

            The CMK's manager. CMKs are either customer-managed or AWS-managed. For more information about the difference, see `Customer Master Keys <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys>`__ in the *AWS Key Management Service Developer Guide* .

            
      
    

    **Examples** 

    The following example returns information (metadata) about the specified CMK.
    ::

      response = client.describe_key(
          # The identifier of the CMK that you want information about. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
          KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          # An object that contains information about the specified CMK.
          'KeyMetadata': {
              'AWSAccountId': '111122223333',
              'Arn': 'arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
              'CreationDate': datetime(2015, 10, 12, 11, 45, 7, 0, 285, 0),
              'Description': '',
              'Enabled': True,
              'KeyId': '1234abcd-12ab-34cd-56ef-1234567890ab',
              'KeyState': 'Enabled',
              'KeyUsage': 'ENCRYPT_DECRYPT',
              'Origin': 'AWS_KMS',
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: disable_key(**kwargs)

    

    Sets the state of a customer master key (CMK) to disabled, thereby preventing its use for cryptographic operations. You cannot perform this operation on a CMK in a different AWS account.

     

    For more information about how key state affects the use of a CMK, see `How Key State Affects the Use of a Customer Master Key <http://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key Management Service Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DisableKey>`_    


    **Request Syntax** 
    ::

      response = client.disable_key(
          KeyId='string'
      )
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      A unique identifier for the customer master key (CMK).

       

      Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

      

    
    
    :returns: None

    **Examples** 

    The following example disables the specified CMK.
    ::

      response = client.disable_key(
          # The identifier of the CMK to disable. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
          KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: disable_key_rotation(**kwargs)

    

    Disables automatic rotation of the key material for the specified customer master key (CMK). You cannot perform this operation on a CMK in a different AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DisableKeyRotation>`_    


    **Request Syntax** 
    ::

      response = client.disable_key_rotation(
          KeyId='string'
      )
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      A unique identifier for the customer master key (CMK).

       

      Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

      

    
    
    :returns: None

    **Examples** 

    The following example disables automatic annual rotation of the key material for the specified CMK.
    ::

      response = client.disable_key_rotation(
          # The identifier of the CMK whose key material will no longer be rotated. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
          KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: enable_key(**kwargs)

    

    Sets the state of a customer master key (CMK) to enabled, thereby permitting its use for cryptographic operations. You cannot perform this operation on a CMK in a different AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/EnableKey>`_    


    **Request Syntax** 
    ::

      response = client.enable_key(
          KeyId='string'
      )
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      A unique identifier for the customer master key (CMK).

       

      Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

      

    
    
    :returns: None

    **Examples** 

    The following example enables the specified CMK.
    ::

      response = client.enable_key(
          # The identifier of the CMK to enable. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
          KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: enable_key_rotation(**kwargs)

    

    Enables automatic rotation of the key material for the specified customer master key (CMK). You cannot perform this operation on a CMK in a different AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/EnableKeyRotation>`_    


    **Request Syntax** 
    ::

      response = client.enable_key_rotation(
          KeyId='string'
      )
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      A unique identifier for the customer master key (CMK).

       

      Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

      

    
    
    :returns: None

    **Examples** 

    The following example enables automatic annual rotation of the key material for the specified CMK.
    ::

      response = client.enable_key_rotation(
          # The identifier of the CMK whose key material will be rotated annually. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
          KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: encrypt(**kwargs)

    

    Encrypts plaintext into ciphertext by using a customer master key (CMK). The ``Encrypt`` operation has two primary use cases:

     

     
    * You can encrypt up to 4 kilobytes (4096 bytes) of arbitrary data such as an RSA key, a database password, or other sensitive information. 
     
    * To move encrypted data from one AWS region to another, you can use this operation to encrypt in the new region the plaintext data key that was used to encrypt the data in the original region. This provides you with an encrypted copy of the data key that can be decrypted in the new region and used there to decrypt the encrypted data. 
     

     

    To perform this operation on a CMK in a different AWS account, specify the key ARN or alias ARN in the value of the KeyId parameter.

     

    Unless you are moving encrypted data from one region to another, you don't use this operation to encrypt a generated data key within a region. To get data keys that are already encrypted, call the  GenerateDataKey or  GenerateDataKeyWithoutPlaintext operation. Data keys don't need to be encrypted again by calling ``Encrypt`` .

     

    To encrypt data locally in your application, use the  GenerateDataKey operation to return a plaintext data encryption key and a copy of the key encrypted under the CMK of your choosing.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/Encrypt>`_    


    **Request Syntax** 
    ::

      response = client.encrypt(
          KeyId='string',
          Plaintext=b'bytes',
          EncryptionContext={
              'string': 'string'
          },
          GrantTokens=[
              'string',
          ]
      )
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      A unique identifier for the customer master key (CMK).

       

      To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with "alias/". To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Alias name: ``alias/ExampleAlias``   
       
      * Alias ARN: ``arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias name and alias ARN, use  ListAliases .

      

    
    :type Plaintext: bytes
    :param Plaintext: **[REQUIRED]** 

      Data to be encrypted.

      

    
    :type EncryptionContext: dict
    :param EncryptionContext: 

      Name-value pair that specifies the encryption context to be used for authenticated encryption. If used here, the same value must be supplied to the ``Decrypt`` API or decryption will fail. For more information, see `Encryption Context <http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html>`__ .

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type GrantTokens: list
    :param GrantTokens: 

      A list of grant tokens.

       

      For more information, see `Grant Tokens <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in the *AWS Key Management Service Developer Guide* .

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CiphertextBlob': b'bytes',
            'KeyId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CiphertextBlob** *(bytes) --* 

          The encrypted plaintext. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not encoded.

          
        

        - **KeyId** *(string) --* 

          The ID of the key used during encryption.

          
    

    **Examples** 

    The following example encrypts data with the specified customer master key (CMK).
    ::

      response = client.encrypt(
          # The identifier of the CMK to use for encryption. You can use the key ID or Amazon Resource Name (ARN) of the CMK, or the name or ARN of an alias that refers to the CMK.
          KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
          # The data to encrypt.
          Plaintext='<binary data>',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          # The encrypted data (ciphertext).
          'CiphertextBlob': '<binary data>',
          # The ARN of the CMK that was used to encrypt the data.
          'KeyId': 'arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: generate_data_key(**kwargs)

    

    Returns a data encryption key that you can use in your application to encrypt data locally. 

     

    You must specify the customer master key (CMK) under which to generate the data key. You must also specify the length of the data key using either the ``KeySpec`` or ``NumberOfBytes`` field. You must specify one field or the other, but not both. For common key lengths (128-bit and 256-bit symmetric keys), we recommend that you use ``KeySpec`` . To perform this operation on a CMK in a different AWS account, specify the key ARN or alias ARN in the value of the KeyId parameter.

     

    This operation returns a plaintext copy of the data key in the ``Plaintext`` field of the response, and an encrypted copy of the data key in the ``CiphertextBlob`` field. The data key is encrypted under the CMK specified in the ``KeyId`` field of the request. 

     

    We recommend that you use the following pattern to encrypt data locally in your application:

     

     
    * Use this operation (``GenerateDataKey`` ) to get a data encryption key. 
     
    * Use the plaintext data encryption key (returned in the ``Plaintext`` field of the response) to encrypt data locally, then erase the plaintext data key from memory. 
     
    * Store the encrypted data key (returned in the ``CiphertextBlob`` field of the response) alongside the locally encrypted data. 
     

     

    To decrypt data locally:

     

     
    * Use the  Decrypt operation to decrypt the encrypted data key into a plaintext copy of the data key. 
     
    * Use the plaintext data key to decrypt data locally, then erase the plaintext data key from memory. 
     

     

    To return only an encrypted copy of the data key, use  GenerateDataKeyWithoutPlaintext . To return a random byte string that is cryptographically secure, use  GenerateRandom .

     

    If you use the optional ``EncryptionContext`` field, you must store at least enough information to be able to reconstruct the full encryption context when you later send the ciphertext to the  Decrypt operation. It is a good practice to choose an encryption context that you can reconstruct on the fly to better secure the ciphertext. For more information, see `Encryption Context <http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html>`__ in the *AWS Key Management Service Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GenerateDataKey>`_    


    **Request Syntax** 
    ::

      response = client.generate_data_key(
          KeyId='string',
          EncryptionContext={
              'string': 'string'
          },
          NumberOfBytes=123,
          KeySpec='AES_256'|'AES_128',
          GrantTokens=[
              'string',
          ]
      )
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      The identifier of the CMK under which to generate and encrypt the data encryption key.

       

      To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with "alias/". To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Alias name: ``alias/ExampleAlias``   
       
      * Alias ARN: ``arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias name and alias ARN, use  ListAliases .

      

    
    :type EncryptionContext: dict
    :param EncryptionContext: 

      A set of key-value pairs that represents additional authenticated data.

       

      For more information, see `Encryption Context <http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html>`__ in the *AWS Key Management Service Developer Guide* .

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type NumberOfBytes: integer
    :param NumberOfBytes: 

      The length of the data encryption key in bytes. For example, use the value 64 to generate a 512-bit data key (64 bytes is 512 bits). For common key lengths (128-bit and 256-bit symmetric keys), we recommend that you use the ``KeySpec`` field instead of this one.

      

    
    :type KeySpec: string
    :param KeySpec: 

      The length of the data encryption key. Use ``AES_128`` to generate a 128-bit symmetric key, or ``AES_256`` to generate a 256-bit symmetric key.

      

    
    :type GrantTokens: list
    :param GrantTokens: 

      A list of grant tokens.

       

      For more information, see `Grant Tokens <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in the *AWS Key Management Service Developer Guide* .

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CiphertextBlob': b'bytes',
            'Plaintext': b'bytes',
            'KeyId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CiphertextBlob** *(bytes) --* 

          The encrypted data encryption key. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not encoded.

          
        

        - **Plaintext** *(bytes) --* 

          The data encryption key. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not encoded. Use this data key for local encryption and decryption, then remove it from memory as soon as possible.

          
        

        - **KeyId** *(string) --* 

          The identifier of the CMK under which the data encryption key was generated and encrypted.

          
    

    **Examples** 

    The following example generates a 256-bit symmetric data encryption key (data key) in two formats. One is the unencrypted (plainext) data key, and the other is the data key encrypted with the specified customer master key (CMK).
    ::

      response = client.generate_data_key(
          # The identifier of the CMK to use to encrypt the data key. You can use the key ID or Amazon Resource Name (ARN) of the CMK, or the name or ARN of an alias that refers to the CMK.
          KeyId='alias/ExampleAlias',
          # Specifies the type of data key to return.
          KeySpec='AES_256',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          # The encrypted data key.
          'CiphertextBlob': '<binary data>',
          # The ARN of the CMK that was used to encrypt the data key.
          'KeyId': 'arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
          # The unencrypted (plaintext) data key.
          'Plaintext': '<binary data>',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: generate_data_key_without_plaintext(**kwargs)

    

    Returns a data encryption key encrypted under a customer master key (CMK). This operation is identical to  GenerateDataKey but returns only the encrypted copy of the data key. 

     

    To perform this operation on a CMK in a different AWS account, specify the key ARN or alias ARN in the value of the KeyId parameter.

     

    This operation is useful in a system that has multiple components with different degrees of trust. For example, consider a system that stores encrypted data in containers. Each container stores the encrypted data and an encrypted copy of the data key. One component of the system, called the *control plane* , creates new containers. When it creates a new container, it uses this operation (``GenerateDataKeyWithoutPlaintext`` ) to get an encrypted data key and then stores it in the container. Later, a different component of the system, called the *data plane* , puts encrypted data into the containers. To do this, it passes the encrypted data key to the  Decrypt operation, then uses the returned plaintext data key to encrypt data, and finally stores the encrypted data in the container. In this system, the control plane never sees the plaintext data key.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GenerateDataKeyWithoutPlaintext>`_    


    **Request Syntax** 
    ::

      response = client.generate_data_key_without_plaintext(
          KeyId='string',
          EncryptionContext={
              'string': 'string'
          },
          KeySpec='AES_256'|'AES_128',
          NumberOfBytes=123,
          GrantTokens=[
              'string',
          ]
      )
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      The identifier of the customer master key (CMK) under which to generate and encrypt the data encryption key.

       

      To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with "alias/". To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Alias name: ``alias/ExampleAlias``   
       
      * Alias ARN: ``arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias name and alias ARN, use  ListAliases .

      

    
    :type EncryptionContext: dict
    :param EncryptionContext: 

      A set of key-value pairs that represents additional authenticated data.

       

      For more information, see `Encryption Context <http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html>`__ in the *AWS Key Management Service Developer Guide* .

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type KeySpec: string
    :param KeySpec: 

      The length of the data encryption key. Use ``AES_128`` to generate a 128-bit symmetric key, or ``AES_256`` to generate a 256-bit symmetric key.

      

    
    :type NumberOfBytes: integer
    :param NumberOfBytes: 

      The length of the data encryption key in bytes. For example, use the value 64 to generate a 512-bit data key (64 bytes is 512 bits). For common key lengths (128-bit and 256-bit symmetric keys), we recommend that you use the ``KeySpec`` field instead of this one.

      

    
    :type GrantTokens: list
    :param GrantTokens: 

      A list of grant tokens.

       

      For more information, see `Grant Tokens <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in the *AWS Key Management Service Developer Guide* .

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CiphertextBlob': b'bytes',
            'KeyId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CiphertextBlob** *(bytes) --* 

          The encrypted data encryption key. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not encoded.

          
        

        - **KeyId** *(string) --* 

          The identifier of the CMK under which the data encryption key was generated and encrypted.

          
    

    **Examples** 

    The following example generates an encrypted copy of a 256-bit symmetric data encryption key (data key). The data key is encrypted with the specified customer master key (CMK).
    ::

      response = client.generate_data_key_without_plaintext(
          # The identifier of the CMK to use to encrypt the data key. You can use the key ID or Amazon Resource Name (ARN) of the CMK, or the name or ARN of an alias that refers to the CMK.
          KeyId='alias/ExampleAlias',
          # Specifies the type of data key to return.
          KeySpec='AES_256',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          # The encrypted data key.
          'CiphertextBlob': '<binary data>',
          # The ARN of the CMK that was used to encrypt the data key.
          'KeyId': 'arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
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


  .. py:method:: generate_random(**kwargs)

    

    Returns a random byte string that is cryptographically secure.

     

    For more information about entropy and random number generation, see the `AWS Key Management Service Cryptographic Details <https://d0.awsstatic.com/whitepapers/KMS-Cryptographic-Details.pdf>`__ whitepaper.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GenerateRandom>`_    


    **Request Syntax** 
    ::

      response = client.generate_random(
          NumberOfBytes=123
      )
    :type NumberOfBytes: integer
    :param NumberOfBytes: 

      The length of the byte string.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Plaintext': b'bytes'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Plaintext** *(bytes) --* 

          The random byte string. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not encoded.

          
    

    **Examples** 

    The following example uses AWS KMS to generate 32 bytes of random data.
    ::

      response = client.generate_random(
          # The length of the random data, specified in number of bytes.
          NumberOfBytes=32,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          # The random data.
          'Plaintext': '<binary data>',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_key_policy(**kwargs)

    

    Gets a key policy attached to the specified customer master key (CMK). You cannot perform this operation on a CMK in a different AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GetKeyPolicy>`_    


    **Request Syntax** 
    ::

      response = client.get_key_policy(
          KeyId='string',
          PolicyName='string'
      )
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      A unique identifier for the customer master key (CMK).

       

      Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

      

    
    :type PolicyName: string
    :param PolicyName: **[REQUIRED]** 

      Specifies the name of the policy. The only valid name is ``default`` . To get the names of key policies, use  ListKeyPolicies .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Policy': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Policy** *(string) --* 

          A policy document in JSON format.

          
    

    **Examples** 

    The following example retrieves the key policy for the specified customer master key (CMK).
    ::

      response = client.get_key_policy(
          # The identifier of the CMK whose key policy you want to retrieve. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
          KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
          # The name of the key policy to retrieve.
          PolicyName='default',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          # The key policy document.
          'Policy': '{\n  "Version" : "2012-10-17",\n  "Id" : "key-default-1",\n  "Statement" : [ {\n    "Sid" : "Enable IAM User Permissions",\n    "Effect" : "Allow",\n    "Principal" : {\n      "AWS" : "arn:aws:iam::111122223333:root"\n    },\n    "Action" : "kms:*",\n    "Resource" : "*"\n  } ]\n}',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_key_rotation_status(**kwargs)

    

    Gets a Boolean value that indicates whether automatic rotation of the key material is enabled for the specified customer master key (CMK).

     

    To perform this operation on a CMK in a different AWS account, specify the key ARN in the value of the KeyId parameter.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GetKeyRotationStatus>`_    


    **Request Syntax** 
    ::

      response = client.get_key_rotation_status(
          KeyId='string'
      )
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      A unique identifier for the customer master key (CMK).

       

      Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'KeyRotationEnabled': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **KeyRotationEnabled** *(boolean) --* 

          A Boolean value that specifies whether key rotation is enabled.

          
    

    **Examples** 

    The following example retrieves the status of automatic annual rotation of the key material for the specified CMK.
    ::

      response = client.get_key_rotation_status(
          # The identifier of the CMK whose key material rotation status you want to retrieve. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
          KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          # A boolean that indicates the key material rotation status. Returns true when automatic annual rotation of the key material is enabled, or false when it is not.
          'KeyRotationEnabled': True,
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

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


  .. py:method:: get_parameters_for_import(**kwargs)

    

    Returns the items you need in order to import key material into AWS KMS from your existing key management infrastructure. For more information about importing key material into AWS KMS, see `Importing Key Material <http://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html>`__ in the *AWS Key Management Service Developer Guide* .

     

    You must specify the key ID of the customer master key (CMK) into which you will import key material. This CMK's ``Origin`` must be ``EXTERNAL`` . You must also specify the wrapping algorithm and type of wrapping key (public key) that you will use to encrypt the key material. You cannot perform this operation on a CMK in a different AWS account.

     

    This operation returns a public key and an import token. Use the public key to encrypt the key material. Store the import token to send with a subsequent  ImportKeyMaterial request. The public key and import token from the same response must be used together. These items are valid for 24 hours. When they expire, they cannot be used for a subsequent  ImportKeyMaterial request. To get new ones, send another ``GetParametersForImport`` request.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GetParametersForImport>`_    


    **Request Syntax** 
    ::

      response = client.get_parameters_for_import(
          KeyId='string',
          WrappingAlgorithm='RSAES_PKCS1_V1_5'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256',
          WrappingKeySpec='RSA_2048'
      )
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      The identifier of the CMK into which you will import key material. The CMK's ``Origin`` must be ``EXTERNAL`` .

       

      Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

      

    
    :type WrappingAlgorithm: string
    :param WrappingAlgorithm: **[REQUIRED]** 

      The algorithm you will use to encrypt the key material before importing it with  ImportKeyMaterial . For more information, see `Encrypt the Key Material <http://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-encrypt-key-material.html>`__ in the *AWS Key Management Service Developer Guide* .

      

    
    :type WrappingKeySpec: string
    :param WrappingKeySpec: **[REQUIRED]** 

      The type of wrapping key (public key) to return in the response. Only 2048-bit RSA public keys are supported.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'KeyId': 'string',
            'ImportToken': b'bytes',
            'PublicKey': b'bytes',
            'ParametersValidTo': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **KeyId** *(string) --* 

          The identifier of the CMK to use in a subsequent  ImportKeyMaterial request. This is the same CMK specified in the ``GetParametersForImport`` request.

          
        

        - **ImportToken** *(bytes) --* 

          The import token to send in a subsequent  ImportKeyMaterial request.

          
        

        - **PublicKey** *(bytes) --* 

          The public key to use to encrypt the key material before importing it with  ImportKeyMaterial .

          
        

        - **ParametersValidTo** *(datetime) --* 

          The time at which the import token and public key are no longer valid. After this time, you cannot use them to make an  ImportKeyMaterial request and you must send another ``GetParametersForImport`` request to get new ones.

          
    

    **Examples** 

    The following example retrieves the public key and import token for the specified CMK.
    ::

      response = client.get_parameters_for_import(
          # The identifier of the CMK for which to retrieve the public key and import token. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
          KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
          # The algorithm that you will use to encrypt the key material before importing it.
          WrappingAlgorithm='RSAES_OAEP_SHA_1',
          # The type of wrapping key (public key) to return in the response.
          WrappingKeySpec='RSA_2048',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          # The import token to send with a subsequent ImportKeyMaterial request.
          'ImportToken': '<binary data>',
          # The ARN of the CMK for which you are retrieving the public key and import token. This is the same CMK specified in the request.
          'KeyId': 'arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
          # The time at which the import token and public key are no longer valid.
          'ParametersValidTo': datetime(2016, 12, 1, 14, 52, 17, 3, 336, 0),
          # The public key to use to encrypt the key material before importing it.
          'PublicKey': '<binary data>',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: import_key_material(**kwargs)

    

    Imports key material into an existing AWS KMS customer master key (CMK) that was created without key material. You cannot perform this operation on a CMK in a different AWS account. For more information about creating CMKs with no key material and then importing key material, see `Importing Key Material <http://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html>`__ in the *AWS Key Management Service Developer Guide* .

     

    Before using this operation, call  GetParametersForImport . Its response includes a public key and an import token. Use the public key to encrypt the key material. Then, submit the import token from the same ``GetParametersForImport`` response.

     

    When calling this operation, you must specify the following values:

     

     
    * The key ID or key ARN of a CMK with no key material. Its ``Origin`` must be ``EXTERNAL`` . To create a CMK with no key material, call  CreateKey and set the value of its ``Origin`` parameter to ``EXTERNAL`` . To get the ``Origin`` of a CMK, call  DescribeKey .) 
     
    * The encrypted key material. To get the public key to encrypt the key material, call  GetParametersForImport . 
     
    * The import token that  GetParametersForImport returned. This token and the public key used to encrypt the key material must have come from the same response. 
     
    * Whether the key material expires and if so, when. If you set an expiration date, you can change it only by reimporting the same key material and specifying a new expiration date. If the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. To use the CMK again, you must reimport the same key material. 
     

     

    When this operation is successful, the CMK's key state changes from ``PendingImport`` to ``Enabled`` , and you can use the CMK. After you successfully import key material into a CMK, you can reimport the same key material into that CMK, but you cannot import different key material.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ImportKeyMaterial>`_    


    **Request Syntax** 
    ::

      response = client.import_key_material(
          KeyId='string',
          ImportToken=b'bytes',
          EncryptedKeyMaterial=b'bytes',
          ValidTo=datetime(2015, 1, 1),
          ExpirationModel='KEY_MATERIAL_EXPIRES'|'KEY_MATERIAL_DOES_NOT_EXPIRE'
      )
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      The identifier of the CMK to import the key material into. The CMK's ``Origin`` must be ``EXTERNAL`` .

       

      Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

      

    
    :type ImportToken: bytes
    :param ImportToken: **[REQUIRED]** 

      The import token that you received in the response to a previous  GetParametersForImport request. It must be from the same response that contained the public key that you used to encrypt the key material.

      

    
    :type EncryptedKeyMaterial: bytes
    :param EncryptedKeyMaterial: **[REQUIRED]** 

      The encrypted key material to import. It must be encrypted with the public key that you received in the response to a previous  GetParametersForImport request, using the wrapping algorithm that you specified in that request.

      

    
    :type ValidTo: datetime
    :param ValidTo: 

      The time at which the imported key material expires. When the key material expires, AWS KMS deletes the key material and the CMK becomes unusable. You must omit this parameter when the ``ExpirationModel`` parameter is set to ``KEY_MATERIAL_DOES_NOT_EXPIRE`` . Otherwise it is required.

      

    
    :type ExpirationModel: string
    :param ExpirationModel: 

      Specifies whether the key material expires. The default is ``KEY_MATERIAL_EXPIRES`` , in which case you must include the ``ValidTo`` parameter. When this parameter is set to ``KEY_MATERIAL_DOES_NOT_EXPIRE`` , you must omit the ``ValidTo`` parameter.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

    **Examples** 

    The following example imports key material into the specified CMK.
    ::

      response = client.import_key_material(
          # The encrypted key material to import.
          EncryptedKeyMaterial='<binary data>',
          # A value that specifies whether the key material expires.
          ExpirationModel='KEY_MATERIAL_DOES_NOT_EXPIRE',
          # The import token that you received in the response to a previous GetParametersForImport request.
          ImportToken='<binary data>',
          # The identifier of the CMK to import the key material into. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
          KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_aliases(**kwargs)

    

    Gets a list of all aliases in the caller's AWS account and region. You cannot list aliases in other accounts. For more information about aliases, see  CreateAlias .

     

    The response might include several aliases that do not have a ``TargetKeyId`` field because they are not associated with a CMK. These are predefined aliases that are reserved for CMKs managed by AWS services. If an alias is not associated with a CMK, the alias does not count against the `alias limit <http://docs.aws.amazon.com/kms/latest/developerguide/limits.html#aliases-limit>`__ for your account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListAliases>`_    


    **Request Syntax** 
    ::

      response = client.list_aliases(
          Limit=123,
          Marker='string'
      )
    :type Limit: integer
    :param Limit: 

      Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.

       

      This value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.

      

    
    :type Marker: string
    :param Marker: 

      Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of ``NextMarker`` from the truncated response you just received.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Aliases': [
                {
                    'AliasName': 'string',
                    'AliasArn': 'string',
                    'TargetKeyId': 'string'
                },
            ],
            'NextMarker': 'string',
            'Truncated': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Aliases** *(list) --* 

          A list of aliases.

          
          

          - *(dict) --* 

            Contains information about an alias.

            
            

            - **AliasName** *(string) --* 

              String that contains the alias.

              
            

            - **AliasArn** *(string) --* 

              String that contains the key ARN.

              
            

            - **TargetKeyId** *(string) --* 

              String that contains the key identifier referred to by the alias.

              
        
      
        

        - **NextMarker** *(string) --* 

          When ``Truncated`` is true, this element is present and contains the value to use for the ``Marker`` parameter in a subsequent request.

          
        

        - **Truncated** *(boolean) --* 

          A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the ``NextMarker`` element in this response to the ``Marker`` parameter in a subsequent request.

          
    

    **Examples** 

    The following example lists aliases.
    ::

      response = client.list_aliases(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          # A list of aliases, including the key ID of the customer master key (CMK) that each alias refers to.
          'Aliases': [
              {
                  'AliasArn': 'arn:aws:kms:us-east-2:111122223333:alias/aws/acm',
                  'AliasName': 'alias/aws/acm',
                  'TargetKeyId': 'da03f6f7-d279-427a-9cae-de48d07e5b66',
              },
              {
                  'AliasArn': 'arn:aws:kms:us-east-2:111122223333:alias/aws/ebs',
                  'AliasName': 'alias/aws/ebs',
                  'TargetKeyId': '25a217e7-7170-4b8c-8bf6-045ea5f70e5b',
              },
              {
                  'AliasArn': 'arn:aws:kms:us-east-2:111122223333:alias/aws/rds',
                  'AliasName': 'alias/aws/rds',
                  'TargetKeyId': '7ec3104e-c3f2-4b5c-bf42-bfc4772c6685',
              },
              {
                  'AliasArn': 'arn:aws:kms:us-east-2:111122223333:alias/aws/redshift',
                  'AliasName': 'alias/aws/redshift',
                  'TargetKeyId': '08f7a25a-69e2-4fb5-8f10-393db27326fa',
              },
              {
                  'AliasArn': 'arn:aws:kms:us-east-2:111122223333:alias/aws/s3',
                  'AliasName': 'alias/aws/s3',
                  'TargetKeyId': 'd2b0f1a3-580d-4f79-b836-bc983be8cfa5',
              },
              {
                  'AliasArn': 'arn:aws:kms:us-east-2:111122223333:alias/example1',
                  'AliasName': 'alias/example1',
                  'TargetKeyId': '4da1e216-62d0-46c5-a7c0-5f3a3d2f8046',
              },
              {
                  'AliasArn': 'arn:aws:kms:us-east-2:111122223333:alias/example2',
                  'AliasName': 'alias/example2',
                  'TargetKeyId': 'f32fef59-2cc2-445b-8573-2d73328acbee',
              },
              {
                  'AliasArn': 'arn:aws:kms:us-east-2:111122223333:alias/example3',
                  'AliasName': 'alias/example3',
                  'TargetKeyId': '1374ef38-d34e-4d5f-b2c9-4e0daee38855',
              },
          ],
          # A boolean that indicates whether there are more items in the list. Returns true when there are more items, or false when there are not.
          'Truncated': False,
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_grants(**kwargs)

    

    Gets a list of all grants for the specified customer master key (CMK).

     

    To perform this operation on a CMK in a different AWS account, specify the key ARN in the value of the KeyId parameter.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListGrants>`_    


    **Request Syntax** 
    ::

      response = client.list_grants(
          Limit=123,
          Marker='string',
          KeyId='string'
      )
    :type Limit: integer
    :param Limit: 

      Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.

       

      This value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.

      

    
    :type Marker: string
    :param Marker: 

      Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of ``NextMarker`` from the truncated response you just received.

      

    
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      A unique identifier for the customer master key (CMK).

       

      Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Grants': [
                {
                    'KeyId': 'string',
                    'GrantId': 'string',
                    'Name': 'string',
                    'CreationDate': datetime(2015, 1, 1),
                    'GranteePrincipal': 'string',
                    'RetiringPrincipal': 'string',
                    'IssuingAccount': 'string',
                    'Operations': [
                        'Decrypt'|'Encrypt'|'GenerateDataKey'|'GenerateDataKeyWithoutPlaintext'|'ReEncryptFrom'|'ReEncryptTo'|'CreateGrant'|'RetireGrant'|'DescribeKey',
                    ],
                    'Constraints': {
                        'EncryptionContextSubset': {
                            'string': 'string'
                        },
                        'EncryptionContextEquals': {
                            'string': 'string'
                        }
                    }
                },
            ],
            'NextMarker': 'string',
            'Truncated': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Grants** *(list) --* 

          A list of grants.

          
          

          - *(dict) --* 

            Contains information about an entry in a list of grants.

            
            

            - **KeyId** *(string) --* 

              The unique identifier for the customer master key (CMK) to which the grant applies.

              
            

            - **GrantId** *(string) --* 

              The unique identifier for the grant.

              
            

            - **Name** *(string) --* 

              The friendly name that identifies the grant. If a name was provided in the  CreateGrant request, that name is returned. Otherwise this value is null.

              
            

            - **CreationDate** *(datetime) --* 

              The date and time when the grant was created.

              
            

            - **GranteePrincipal** *(string) --* 

              The principal that receives the grant's permissions.

              
            

            - **RetiringPrincipal** *(string) --* 

              The principal that can retire the grant.

              
            

            - **IssuingAccount** *(string) --* 

              The AWS account under which the grant was issued.

              
            

            - **Operations** *(list) --* 

              The list of operations permitted by the grant.

              
              

              - *(string) --* 
          
            

            - **Constraints** *(dict) --* 

              A list of key-value pairs that must be present in the encryption context of certain subsequent operations that the grant allows.

              
              

              - **EncryptionContextSubset** *(dict) --* 

                A list of key-value pairs, all of which must be present in the encryption context of certain subsequent operations that the grant allows. When certain subsequent operations allowed by the grant include encryption context that matches this list or is a superset of this list, the grant allows the operation. Otherwise, the grant does not allow the operation.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **EncryptionContextEquals** *(dict) --* 

                A list of key-value pairs that must be present in the encryption context of certain subsequent operations that the grant allows. When certain subsequent operations allowed by the grant include encryption context that matches this list, the grant allows the operation. Otherwise, the grant does not allow the operation.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
          
        
      
        

        - **NextMarker** *(string) --* 

          When ``Truncated`` is true, this element is present and contains the value to use for the ``Marker`` parameter in a subsequent request.

          
        

        - **Truncated** *(boolean) --* 

          A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the ``NextMarker`` element in this response to the ``Marker`` parameter in a subsequent request.

          
    

    **Examples** 

    The following example lists grants for the specified CMK.
    ::

      response = client.list_grants(
          # The identifier of the CMK whose grants you want to list. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
          KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          # A list of grants.
          'Grants': [
              {
                  'CreationDate': datetime(2016, 10, 25, 14, 37, 41, 1, 299, 0),
                  'GrantId': '91ad875e49b04a9d1f3bdeb84d821f9db6ea95e1098813f6d47f0c65fbe2a172',
                  'GranteePrincipal': 'acm.us-east-2.amazonaws.com',
                  'IssuingAccount': 'arn:aws:iam::111122223333:root',
                  'KeyId': 'arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
                  'Operations': [
                      'Encrypt',
                      'ReEncryptFrom',
                      'ReEncryptTo',
                  ],
                  'RetiringPrincipal': 'acm.us-east-2.amazonaws.com',
              },
              {
                  'CreationDate': datetime(2016, 10, 25, 14, 37, 41, 1, 299, 0),
                  'GrantId': 'a5d67d3e207a8fc1f4928749ee3e52eb0440493a8b9cf05bbfad91655b056200',
                  'GranteePrincipal': 'acm.us-east-2.amazonaws.com',
                  'IssuingAccount': 'arn:aws:iam::111122223333:root',
                  'KeyId': 'arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
                  'Operations': [
                      'ReEncryptFrom',
                      'ReEncryptTo',
                  ],
                  'RetiringPrincipal': 'acm.us-east-2.amazonaws.com',
              },
              {
                  'CreationDate': datetime(2016, 10, 25, 14, 37, 41, 1, 299, 0),
                  'GrantId': 'c541aaf05d90cb78846a73b346fc43e65be28b7163129488c738e0c9e0628f4f',
                  'GranteePrincipal': 'acm.us-east-2.amazonaws.com',
                  'IssuingAccount': 'arn:aws:iam::111122223333:root',
                  'KeyId': 'arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
                  'Operations': [
                      'Encrypt',
                      'ReEncryptFrom',
                      'ReEncryptTo',
                  ],
                  'RetiringPrincipal': 'acm.us-east-2.amazonaws.com',
              },
              {
                  'CreationDate': datetime(2016, 10, 25, 14, 37, 41, 1, 299, 0),
                  'GrantId': 'dd2052c67b4c76ee45caf1dc6a1e2d24e8dc744a51b36ae2f067dc540ce0105c',
                  'GranteePrincipal': 'acm.us-east-2.amazonaws.com',
                  'IssuingAccount': 'arn:aws:iam::111122223333:root',
                  'KeyId': 'arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
                  'Operations': [
                      'Encrypt',
                      'ReEncryptFrom',
                      'ReEncryptTo',
                  ],
                  'RetiringPrincipal': 'acm.us-east-2.amazonaws.com',
              },
          ],
          # A boolean that indicates whether there are more items in the list. Returns true when there are more items, or false when there are not.
          'Truncated': True,
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_key_policies(**kwargs)

    

    Gets the names of the key policies that are attached to a customer master key (CMK). This operation is designed to get policy names that you can use in a  GetKeyPolicy operation. However, the only valid policy name is ``default`` . You cannot perform this operation on a CMK in a different AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListKeyPolicies>`_    


    **Request Syntax** 
    ::

      response = client.list_key_policies(
          KeyId='string',
          Limit=123,
          Marker='string'
      )
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      A unique identifier for the customer master key (CMK).

       

      Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

      

    
    :type Limit: integer
    :param Limit: 

      Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.

       

      This value is optional. If you include a value, it must be between 1 and 1000, inclusive. If you do not include a value, it defaults to 100.

       

      Currently only 1 policy can be attached to a key.

      

    
    :type Marker: string
    :param Marker: 

      Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of ``NextMarker`` from the truncated response you just received.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'PolicyNames': [
                'string',
            ],
            'NextMarker': 'string',
            'Truncated': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **PolicyNames** *(list) --* 

          A list of policy names. Currently, there is only one policy and it is named "Default".

          
          

          - *(string) --* 
      
        

        - **NextMarker** *(string) --* 

          When ``Truncated`` is true, this element is present and contains the value to use for the ``Marker`` parameter in a subsequent request.

          
        

        - **Truncated** *(boolean) --* 

          A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the ``NextMarker`` element in this response to the ``Marker`` parameter in a subsequent request.

          
    

    **Examples** 

    The following example lists key policies for the specified CMK.
    ::

      response = client.list_key_policies(
          # The identifier of the CMK whose key policies you want to list. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
          KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          # A list of key policy names.
          'PolicyNames': [
              'default',
          ],
          # A boolean that indicates whether there are more items in the list. Returns true when there are more items, or false when there are not.
          'Truncated': False,
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_keys(**kwargs)

    

    Gets a list of all customer master keys (CMKs) in the caller's AWS account and region.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListKeys>`_    


    **Request Syntax** 
    ::

      response = client.list_keys(
          Limit=123,
          Marker='string'
      )
    :type Limit: integer
    :param Limit: 

      Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.

       

      This value is optional. If you include a value, it must be between 1 and 1000, inclusive. If you do not include a value, it defaults to 100.

      

    
    :type Marker: string
    :param Marker: 

      Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of ``NextMarker`` from the truncated response you just received.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Keys': [
                {
                    'KeyId': 'string',
                    'KeyArn': 'string'
                },
            ],
            'NextMarker': 'string',
            'Truncated': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Keys** *(list) --* 

          A list of customer master keys (CMKs).

          
          

          - *(dict) --* 

            Contains information about each entry in the key list.

            
            

            - **KeyId** *(string) --* 

              Unique identifier of the key.

              
            

            - **KeyArn** *(string) --* 

              ARN of the key.

              
        
      
        

        - **NextMarker** *(string) --* 

          When ``Truncated`` is true, this element is present and contains the value to use for the ``Marker`` parameter in a subsequent request.

          
        

        - **Truncated** *(boolean) --* 

          A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the ``NextMarker`` element in this response to the ``Marker`` parameter in a subsequent request.

          
    

    **Examples** 

    The following example lists CMKs.
    ::

      response = client.list_keys(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          # A list of CMKs, including the key ID and Amazon Resource Name (ARN) of each one.
          'Keys': [
              {
                  'KeyArn': 'arn:aws:kms:us-east-2:111122223333:key/0d990263-018e-4e65-a703-eff731de951e',
                  'KeyId': '0d990263-018e-4e65-a703-eff731de951e',
              },
              {
                  'KeyArn': 'arn:aws:kms:us-east-2:111122223333:key/144be297-0ae1-44ac-9c8f-93cd8c82f841',
                  'KeyId': '144be297-0ae1-44ac-9c8f-93cd8c82f841',
              },
              {
                  'KeyArn': 'arn:aws:kms:us-east-2:111122223333:key/21184251-b765-428e-b852-2c7353e72571',
                  'KeyId': '21184251-b765-428e-b852-2c7353e72571',
              },
              {
                  'KeyArn': 'arn:aws:kms:us-east-2:111122223333:key/214fe92f-5b03-4ae1-b350-db2a45dbe10c',
                  'KeyId': '214fe92f-5b03-4ae1-b350-db2a45dbe10c',
              },
              {
                  'KeyArn': 'arn:aws:kms:us-east-2:111122223333:key/339963f2-e523-49d3-af24-a0fe752aa458',
                  'KeyId': '339963f2-e523-49d3-af24-a0fe752aa458',
              },
              {
                  'KeyArn': 'arn:aws:kms:us-east-2:111122223333:key/b776a44b-df37-4438-9be4-a27494e4271a',
                  'KeyId': 'b776a44b-df37-4438-9be4-a27494e4271a',
              },
              {
                  'KeyArn': 'arn:aws:kms:us-east-2:111122223333:key/deaf6c9e-cf2c-46a6-bf6d-0b6d487cffbb',
                  'KeyId': 'deaf6c9e-cf2c-46a6-bf6d-0b6d487cffbb',
              },
          ],
          # A boolean that indicates whether there are more items in the list. Returns true when there are more items, or false when there are not.
          'Truncated': False,
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_resource_tags(**kwargs)

    

    Returns a list of all tags for the specified customer master key (CMK).

     

    You cannot perform this operation on a CMK in a different AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListResourceTags>`_    


    **Request Syntax** 
    ::

      response = client.list_resource_tags(
          KeyId='string',
          Limit=123,
          Marker='string'
      )
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      A unique identifier for the customer master key (CMK).

       

      Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

      

    
    :type Limit: integer
    :param Limit: 

      Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.

       

      This value is optional. If you include a value, it must be between 1 and 50, inclusive. If you do not include a value, it defaults to 50.

      

    
    :type Marker: string
    :param Marker: 

      Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of ``NextMarker`` from the truncated response you just received.

       

      Do not attempt to construct this value. Use only the value of ``NextMarker`` from the truncated response you just received.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Tags': [
                {
                    'TagKey': 'string',
                    'TagValue': 'string'
                },
            ],
            'NextMarker': 'string',
            'Truncated': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Tags** *(list) --* 

          A list of tags. Each tag consists of a tag key and a tag value.

          
          

          - *(dict) --* 

            A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.

             

            For information about the rules that apply to tag keys and tag values, see `User-Defined Tag Restrictions <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html>`__ in the *AWS Billing and Cost Management User Guide* .

            
            

            - **TagKey** *(string) --* 

              The key of the tag.

              
            

            - **TagValue** *(string) --* 

              The value of the tag.

              
        
      
        

        - **NextMarker** *(string) --* 

          When ``Truncated`` is true, this element is present and contains the value to use for the ``Marker`` parameter in a subsequent request.

           

          Do not assume or infer any information from this value.

          
        

        - **Truncated** *(boolean) --* 

          A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the ``NextMarker`` element in this response to the ``Marker`` parameter in a subsequent request.

          
    

  .. py:method:: list_retirable_grants(**kwargs)

    

    Returns a list of all grants for which the grant's ``RetiringPrincipal`` matches the one specified.

     

    A typical use is to list all grants that you are able to retire. To retire a grant, use  RetireGrant .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListRetirableGrants>`_    


    **Request Syntax** 
    ::

      response = client.list_retirable_grants(
          Limit=123,
          Marker='string',
          RetiringPrincipal='string'
      )
    :type Limit: integer
    :param Limit: 

      Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.

       

      This value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.

      

    
    :type Marker: string
    :param Marker: 

      Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of ``NextMarker`` from the truncated response you just received.

      

    
    :type RetiringPrincipal: string
    :param RetiringPrincipal: **[REQUIRED]** 

      The retiring principal for which to list grants.

       

      To specify the retiring principal, use the `Amazon Resource Name (ARN) <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ of an AWS principal. Valid AWS principals include AWS accounts (root), IAM users, federated users, and assumed role users. For examples of the ARN syntax for specifying a principal, see `AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-iam>`__ in the Example ARNs section of the *Amazon Web Services General Reference* .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Grants': [
                {
                    'KeyId': 'string',
                    'GrantId': 'string',
                    'Name': 'string',
                    'CreationDate': datetime(2015, 1, 1),
                    'GranteePrincipal': 'string',
                    'RetiringPrincipal': 'string',
                    'IssuingAccount': 'string',
                    'Operations': [
                        'Decrypt'|'Encrypt'|'GenerateDataKey'|'GenerateDataKeyWithoutPlaintext'|'ReEncryptFrom'|'ReEncryptTo'|'CreateGrant'|'RetireGrant'|'DescribeKey',
                    ],
                    'Constraints': {
                        'EncryptionContextSubset': {
                            'string': 'string'
                        },
                        'EncryptionContextEquals': {
                            'string': 'string'
                        }
                    }
                },
            ],
            'NextMarker': 'string',
            'Truncated': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Grants** *(list) --* 

          A list of grants.

          
          

          - *(dict) --* 

            Contains information about an entry in a list of grants.

            
            

            - **KeyId** *(string) --* 

              The unique identifier for the customer master key (CMK) to which the grant applies.

              
            

            - **GrantId** *(string) --* 

              The unique identifier for the grant.

              
            

            - **Name** *(string) --* 

              The friendly name that identifies the grant. If a name was provided in the  CreateGrant request, that name is returned. Otherwise this value is null.

              
            

            - **CreationDate** *(datetime) --* 

              The date and time when the grant was created.

              
            

            - **GranteePrincipal** *(string) --* 

              The principal that receives the grant's permissions.

              
            

            - **RetiringPrincipal** *(string) --* 

              The principal that can retire the grant.

              
            

            - **IssuingAccount** *(string) --* 

              The AWS account under which the grant was issued.

              
            

            - **Operations** *(list) --* 

              The list of operations permitted by the grant.

              
              

              - *(string) --* 
          
            

            - **Constraints** *(dict) --* 

              A list of key-value pairs that must be present in the encryption context of certain subsequent operations that the grant allows.

              
              

              - **EncryptionContextSubset** *(dict) --* 

                A list of key-value pairs, all of which must be present in the encryption context of certain subsequent operations that the grant allows. When certain subsequent operations allowed by the grant include encryption context that matches this list or is a superset of this list, the grant allows the operation. Otherwise, the grant does not allow the operation.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **EncryptionContextEquals** *(dict) --* 

                A list of key-value pairs that must be present in the encryption context of certain subsequent operations that the grant allows. When certain subsequent operations allowed by the grant include encryption context that matches this list, the grant allows the operation. Otherwise, the grant does not allow the operation.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
          
        
      
        

        - **NextMarker** *(string) --* 

          When ``Truncated`` is true, this element is present and contains the value to use for the ``Marker`` parameter in a subsequent request.

          
        

        - **Truncated** *(boolean) --* 

          A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the ``NextMarker`` element in this response to the ``Marker`` parameter in a subsequent request.

          
    

    **Examples** 

    The following example lists the grants that the specified principal (identity) can retire.
    ::

      response = client.list_retirable_grants(
          # The retiring principal whose grants you want to list. Use the Amazon Resource Name (ARN) of an AWS principal such as an AWS account (root), IAM user, federated user, or assumed role user.
          RetiringPrincipal='arn:aws:iam::111122223333:role/ExampleRole',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          # A list of grants that the specified principal can retire.
          'Grants': [
              {
                  'CreationDate': datetime(2016, 12, 7, 11, 9, 35, 2, 342, 0),
                  'GrantId': '0c237476b39f8bc44e45212e08498fbe3151305030726c0590dd8d3e9f3d6a60',
                  'GranteePrincipal': 'arn:aws:iam::111122223333:role/ExampleRole',
                  'IssuingAccount': 'arn:aws:iam::444455556666:root',
                  'KeyId': 'arn:aws:kms:us-east-2:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab',
                  'Operations': [
                      'Decrypt',
                      'Encrypt',
                  ],
                  'RetiringPrincipal': 'arn:aws:iam::111122223333:role/ExampleRole',
              },
          ],
          # A boolean that indicates whether there are more items in the list. Returns true when there are more items, or false when there are not.
          'Truncated': False,
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: put_key_policy(**kwargs)

    

    Attaches a key policy to the specified customer master key (CMK). You cannot perform this operation on a CMK in a different AWS account.

     

    For more information about key policies, see `Key Policies <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ in the *AWS Key Management Service Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/PutKeyPolicy>`_    


    **Request Syntax** 
    ::

      response = client.put_key_policy(
          KeyId='string',
          PolicyName='string',
          Policy='string',
          BypassPolicyLockoutSafetyCheck=True|False
      )
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      A unique identifier for the customer master key (CMK).

       

      Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

      

    
    :type PolicyName: string
    :param PolicyName: **[REQUIRED]** 

      The name of the key policy. The only valid value is ``default`` .

      

    
    :type Policy: string
    :param Policy: **[REQUIRED]** 

      The key policy to attach to the CMK.

       

      If you do not set ``BypassPolicyLockoutSafetyCheck`` to true, the policy must meet the following criteria:

       

       
      * It must allow the principal that is making the ``PutKeyPolicy`` request to make a subsequent ``PutKeyPolicy`` request on the CMK. This reduces the likelihood that the CMK becomes unmanageable. For more information, refer to the scenario in the `Default Key Policy <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam>`__ section in the *AWS Key Management Service Developer Guide* . 
       
      * The principals that are specified in the key policy must exist and be visible to AWS KMS. When you create a new AWS principal (for example, an IAM user or role), you might need to enforce a delay before specifying the new principal in a key policy because the new principal might not immediately be visible to AWS KMS. For more information, see `Changes that I make are not always immediately visible <http://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency>`__ in the *IAM User Guide* . 
       

       

      The policy size limit is 32 kilobytes (32768 bytes).

      

    
    :type BypassPolicyLockoutSafetyCheck: boolean
    :param BypassPolicyLockoutSafetyCheck: 

      A flag to indicate whether to bypass the key policy lockout safety check.

       

      .. warning::

         

        Setting this value to true increases the likelihood that the CMK becomes unmanageable. Do not set this value to true indiscriminately.

         

        For more information, refer to the scenario in the `Default Key Policy <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam>`__ section in the *AWS Key Management Service Developer Guide* .

         

       

      Use this parameter only when you intend to prevent the principal that is making the request from making a subsequent ``PutKeyPolicy`` request on the CMK.

       

      The default value is false.

      

    
    
    :returns: None

    **Examples** 

    The following example attaches a key policy to the specified CMK.
    ::

      response = client.put_key_policy(
          # The identifier of the CMK to attach the key policy to. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
          KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
          # The key policy document.
          Policy='{\n    "Version": "2012-10-17",\n    "Id": "custom-policy-2016-12-07",\n    "Statement": [\n        {\n            "Sid": "Enable IAM User Permissions",\n            "Effect": "Allow",\n            "Principal": {\n                "AWS": "arn:aws:iam::111122223333:root"\n            },\n            "Action": "kms:*",\n            "Resource": "*"\n        },\n        {\n            "Sid": "Allow access for Key Administrators",\n            "Effect": "Allow",\n            "Principal": {\n                "AWS": [\n                    "arn:aws:iam::111122223333:user/ExampleAdminUser",\n                    "arn:aws:iam::111122223333:role/ExampleAdminRole"\n                ]\n            },\n            "Action": [\n                "kms:Create*",\n                "kms:Describe*",\n                "kms:Enable*",\n                "kms:List*",\n                "kms:Put*",\n                "kms:Update*",\n                "kms:Revoke*",\n                "kms:Disable*",\n                "kms:Get*",\n                "kms:Delete*",\n                "kms:ScheduleKeyDeletion",\n                "kms:CancelKeyDeletion"\n            ],\n            "Resource": "*"\n        },\n        {\n            "Sid": "Allow use of the key",\n            "Effect": "Allow",\n            "Principal": {\n                "AWS": "arn:aws:iam::111122223333:role/ExamplePowerUserRole"\n            },\n            "Action": [\n                "kms:Encrypt",\n                "kms:Decrypt",\n                "kms:ReEncrypt*",\n                "kms:GenerateDataKey*",\n                "kms:DescribeKey"\n            ],\n            "Resource": "*"\n        },\n        {\n            "Sid": "Allow attachment of persistent resources",\n            "Effect": "Allow",\n            "Principal": {\n                "AWS": "arn:aws:iam::111122223333:role/ExamplePowerUserRole"\n            },\n            "Action": [\n                "kms:CreateGrant",\n                "kms:ListGrants",\n                "kms:RevokeGrant"\n            ],\n            "Resource": "*",\n            "Condition": {\n                "Bool": {\n                    "kms:GrantIsForAWSResource": "true"\n                }\n            }\n        }\n    ]\n}\n',
          # The name of the key policy.
          PolicyName='default',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: re_encrypt(**kwargs)

    

    Encrypts data on the server side with a new customer master key (CMK) without exposing the plaintext of the data on the client side. The data is first decrypted and then reencrypted. You can also use this operation to change the encryption context of a ciphertext. 

     

    You can reencrypt data using CMKs in different AWS accounts.

     

    Unlike other operations, ``ReEncrypt`` is authorized twice, once as ``ReEncryptFrom`` on the source CMK and once as ``ReEncryptTo`` on the destination CMK. We recommend that you include the ``"kms:ReEncrypt*"`` permission in your `key policies <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ to permit reencryption from or to the CMK. This permission is automatically included in the key policy when you create a CMK through the console, but you must include it manually when you create a CMK programmatically or when you set a key policy with the  PutKeyPolicy operation.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ReEncrypt>`_    


    **Request Syntax** 
    ::

      response = client.re_encrypt(
          CiphertextBlob=b'bytes',
          SourceEncryptionContext={
              'string': 'string'
          },
          DestinationKeyId='string',
          DestinationEncryptionContext={
              'string': 'string'
          },
          GrantTokens=[
              'string',
          ]
      )
    :type CiphertextBlob: bytes
    :param CiphertextBlob: **[REQUIRED]** 

      Ciphertext of the data to reencrypt.

      

    
    :type SourceEncryptionContext: dict
    :param SourceEncryptionContext: 

      Encryption context used to encrypt and decrypt the data specified in the ``CiphertextBlob`` parameter.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type DestinationKeyId: string
    :param DestinationKeyId: **[REQUIRED]** 

      A unique identifier for the CMK that is used to reencrypt the data.

       

      To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. When using an alias name, prefix it with "alias/". To specify a CMK in a different AWS account, you must use the key ARN or alias ARN.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Alias name: ``alias/ExampleAlias``   
       
      * Alias ARN: ``arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias name and alias ARN, use  ListAliases .

      

    
    :type DestinationEncryptionContext: dict
    :param DestinationEncryptionContext: 

      Encryption context to use when the data is reencrypted.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type GrantTokens: list
    :param GrantTokens: 

      A list of grant tokens.

       

      For more information, see `Grant Tokens <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in the *AWS Key Management Service Developer Guide* .

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CiphertextBlob': b'bytes',
            'SourceKeyId': 'string',
            'KeyId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CiphertextBlob** *(bytes) --* 

          The reencrypted data. When you use the HTTP API or the AWS CLI, the value is Base64-encoded. Otherwise, it is not encoded.

          
        

        - **SourceKeyId** *(string) --* 

          Unique identifier of the CMK used to originally encrypt the data.

          
        

        - **KeyId** *(string) --* 

          Unique identifier of the CMK used to reencrypt the data.

          
    

    **Examples** 

    The following example reencrypts data with the specified CMK.
    ::

      response = client.re_encrypt(
          # The data to reencrypt.
          CiphertextBlob='<binary data>',
          # The identifier of the CMK to use to reencrypt the data. You can use the key ID or Amazon Resource Name (ARN) of the CMK, or the name or ARN of an alias that refers to the CMK.
          DestinationKeyId='0987dcba-09fe-87dc-65ba-ab0987654321',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          # The reencrypted data.
          'CiphertextBlob': '<binary data>',
          # The ARN of the CMK that was used to reencrypt the data.
          'KeyId': 'arn:aws:kms:us-east-2:111122223333:key/0987dcba-09fe-87dc-65ba-ab0987654321',
          # The ARN of the CMK that was used to originally encrypt the data.
          'SourceKeyId': 'arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: retire_grant(**kwargs)

    

    Retires a grant. To clean up, you can retire a grant when you're done using it. You should revoke a grant when you intend to actively deny operations that depend on it. The following are permitted to call this API:

     

     
    * The AWS account (root user) under which the grant was created 
     
    * The ``RetiringPrincipal`` , if present in the grant 
     
    * The ``GranteePrincipal`` , if ``RetireGrant`` is an operation specified in the grant 
     

     

    You must identify the grant to retire by its grant token or by a combination of the grant ID and the Amazon Resource Name (ARN) of the customer master key (CMK). A grant token is a unique variable-length base64-encoded string. A grant ID is a 64 character unique identifier of a grant. The  CreateGrant operation returns both.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/RetireGrant>`_    


    **Request Syntax** 
    ::

      response = client.retire_grant(
          GrantToken='string',
          KeyId='string',
          GrantId='string'
      )
    :type GrantToken: string
    :param GrantToken: 

      Token that identifies the grant to be retired.

      

    
    :type KeyId: string
    :param KeyId: 

      The Amazon Resource Name (ARN) of the CMK associated with the grant. 

       

      For example: ``arn:aws:kms:us-east-2:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab``  

      

    
    :type GrantId: string
    :param GrantId: 

      Unique identifier of the grant to retire. The grant ID is returned in the response to a ``CreateGrant`` operation.

       

       
      * Grant ID Example - 0123456789012345678901234567890123456789012345678901234567890123 
       

      

    
    
    :returns: None

    **Examples** 

    The following example retires a grant.
    ::

      response = client.retire_grant(
          # The identifier of the grant to retire.
          GrantId='0c237476b39f8bc44e45212e08498fbe3151305030726c0590dd8d3e9f3d6a60',
          # The Amazon Resource Name (ARN) of the customer master key (CMK) associated with the grant.
          KeyId='arn:aws:kms:us-east-2:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: revoke_grant(**kwargs)

    

    Revokes the specified grant for the specified customer master key (CMK). You can revoke a grant to actively deny operations that depend on it.

     

    To perform this operation on a CMK in a different AWS account, specify the key ARN in the value of the KeyId parameter.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/RevokeGrant>`_    


    **Request Syntax** 
    ::

      response = client.revoke_grant(
          KeyId='string',
          GrantId='string'
      )
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      A unique identifier for the customer master key associated with the grant.

       

      Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

      

    
    :type GrantId: string
    :param GrantId: **[REQUIRED]** 

      Identifier of the grant to be revoked.

      

    
    
    :returns: None

    **Examples** 

    The following example revokes a grant.
    ::

      response = client.revoke_grant(
          # The identifier of the grant to revoke.
          GrantId='0c237476b39f8bc44e45212e08498fbe3151305030726c0590dd8d3e9f3d6a60',
          # The identifier of the customer master key (CMK) associated with the grant. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
          KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: schedule_key_deletion(**kwargs)

    

    Schedules the deletion of a customer master key (CMK). You may provide a waiting period, specified in days, before deletion occurs. If you do not provide a waiting period, the default period of 30 days is used. When this operation is successful, the state of the CMK changes to ``PendingDeletion`` . Before the waiting period ends, you can use  CancelKeyDeletion to cancel the deletion of the CMK. After the waiting period ends, AWS KMS deletes the CMK and all AWS KMS data associated with it, including all aliases that refer to it.

     

    You cannot perform this operation on a CMK in a different AWS account.

     

    .. warning::

       

      Deleting a CMK is a destructive and potentially dangerous operation. When a CMK is deleted, all data that was encrypted under the CMK is rendered unrecoverable. To restrict the use of a CMK without deleting it, use  DisableKey .

       

     

    For more information about scheduling a CMK for deletion, see `Deleting Customer Master Keys <http://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html>`__ in the *AWS Key Management Service Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ScheduleKeyDeletion>`_    


    **Request Syntax** 
    ::

      response = client.schedule_key_deletion(
          KeyId='string',
          PendingWindowInDays=123
      )
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      The unique identifier of the customer master key (CMK) to delete.

       

      Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

      

    
    :type PendingWindowInDays: integer
    :param PendingWindowInDays: 

      The waiting period, specified in number of days. After the waiting period ends, AWS KMS deletes the customer master key (CMK).

       

      This value is optional. If you include a value, it must be between 7 and 30, inclusive. If you do not include a value, it defaults to 30.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'KeyId': 'string',
            'DeletionDate': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **KeyId** *(string) --* 

          The unique identifier of the customer master key (CMK) for which deletion is scheduled.

          
        

        - **DeletionDate** *(datetime) --* 

          The date and time after which AWS KMS deletes the customer master key (CMK).

          
    

    **Examples** 

    The following example schedules the specified CMK for deletion.
    ::

      response = client.schedule_key_deletion(
          # The identifier of the CMK to schedule for deletion. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
          KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
          # The waiting period, specified in number of days. After the waiting period ends, AWS KMS deletes the CMK.
          PendingWindowInDays=7,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          # The date and time after which AWS KMS deletes the CMK.
          'DeletionDate': datetime(2016, 12, 17, 16, 0, 0, 5, 352, 0),
          # The ARN of the CMK that is scheduled for deletion.
          'KeyId': 'arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: tag_resource(**kwargs)

    

    Adds or overwrites one or more tags for the specified customer master key (CMK). You cannot perform this operation on a CMK in a different AWS account.

     

    Each tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.

     

    You cannot use the same tag key more than once per CMK. For example, consider a CMK with one tag whose tag key is ``Purpose`` and tag value is ``Test`` . If you send a ``TagResource`` request for this CMK with a tag key of ``Purpose`` and a tag value of ``Prod`` , it does not create a second tag. Instead, the original tag is overwritten with the new tag value.

     

    For information about the rules that apply to tag keys and tag values, see `User-Defined Tag Restrictions <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html>`__ in the *AWS Billing and Cost Management User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/TagResource>`_    


    **Request Syntax** 
    ::

      response = client.tag_resource(
          KeyId='string',
          Tags=[
              {
                  'TagKey': 'string',
                  'TagValue': 'string'
              },
          ]
      )
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      A unique identifier for the CMK you are tagging.

       

      Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

      

    
    :type Tags: list
    :param Tags: **[REQUIRED]** 

      One or more tags. Each tag consists of a tag key and a tag value.

      

    
      - *(dict) --* 

        A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.

         

        For information about the rules that apply to tag keys and tag values, see `User-Defined Tag Restrictions <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html>`__ in the *AWS Billing and Cost Management User Guide* .

        

      
        - **TagKey** *(string) --* **[REQUIRED]** 

          The key of the tag.

          

        
        - **TagValue** *(string) --* **[REQUIRED]** 

          The value of the tag.

          

        
      
  
    
    :returns: None

  .. py:method:: untag_resource(**kwargs)

    

    Removes the specified tag or tags from the specified customer master key (CMK). You cannot perform this operation on a CMK in a different AWS account.

     

    To remove a tag, you specify the tag key for each tag to remove. You do not specify the tag value. To overwrite the tag value for an existing tag, use  TagResource .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/UntagResource>`_    


    **Request Syntax** 
    ::

      response = client.untag_resource(
          KeyId='string',
          TagKeys=[
              'string',
          ]
      )
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      A unique identifier for the CMK from which you are removing tags.

       

      Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

      

    
    :type TagKeys: list
    :param TagKeys: **[REQUIRED]** 

      One or more tag keys. Specify only the tag keys, not the tag values.

      

    
      - *(string) --* 

      
  
    
    :returns: None

  .. py:method:: update_alias(**kwargs)

    

    Associates an existing alias with a different customer master key (CMK). Each CMK can have multiple aliases, but the aliases must be unique within the account and region. You cannot perform this operation on an alias in a different AWS account.

     

    This operation works only on existing aliases. To change the alias of a CMK to a new value, use  CreateAlias to create a new alias and  DeleteAlias to delete the old alias.

     

    Because an alias is not a property of a CMK, you can create, update, and delete the aliases of a CMK without affecting the CMK. Also, aliases do not appear in the response from the  DescribeKey operation. To get the aliases of all CMKs in the account, use the  ListAliases operation. 

     

    An alias name can contain only alphanumeric characters, forward slashes (/), underscores (_), and dashes (-). An alias must start with the word ``alias`` followed by a forward slash (``alias/`` ). The alias name can contain only alphanumeric characters, forward slashes (/), underscores (_), and dashes (-). Alias names cannot begin with ``aws`` ; that alias name prefix is reserved by Amazon Web Services (AWS).

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/UpdateAlias>`_    


    **Request Syntax** 
    ::

      response = client.update_alias(
          AliasName='string',
          TargetKeyId='string'
      )
    :type AliasName: string
    :param AliasName: **[REQUIRED]** 

      String that contains the name of the alias to be modified. The name must start with the word "alias" followed by a forward slash (alias/). Aliases that begin with "alias/aws" are reserved.

      

    
    :type TargetKeyId: string
    :param TargetKeyId: **[REQUIRED]** 

      Unique identifier of the customer master key to be mapped to the alias.

       

      Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

       

      To verify that the alias is mapped to the correct CMK, use  ListAliases .

      

    
    
    :returns: None

    **Examples** 

    The following example updates the specified alias to refer to the specified customer master key (CMK).
    ::

      response = client.update_alias(
          # The alias to update.
          AliasName='alias/ExampleAlias',
          # The identifier of the CMK that the alias will refer to after this operation succeeds. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
          TargetKeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: update_key_description(**kwargs)

    

    Updates the description of a customer master key (CMK). To see the decription of a CMK, use  DescribeKey . 

     

    You cannot perform this operation on a CMK in a different AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/UpdateKeyDescription>`_    


    **Request Syntax** 
    ::

      response = client.update_key_description(
          KeyId='string',
          Description='string'
      )
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      A unique identifier for the customer master key (CMK).

       

      Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

      

    
    :type Description: string
    :param Description: **[REQUIRED]** 

      New description for the CMK.

      

    
    
    :returns: None

    **Examples** 

    The following example updates the description of the specified CMK.
    ::

      response = client.update_key_description(
          # The updated description.
          Description='Example description that indicates the intended use of this CMK.',
          # The identifier of the CMK whose description you are updating. You can use the key ID or the Amazon Resource Name (ARN) of the CMK.
          KeyId='1234abcd-12ab-34cd-56ef-1234567890ab',
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

* :py:class:`KMS.Paginator.ListAliases`


* :py:class:`KMS.Paginator.ListGrants`


* :py:class:`KMS.Paginator.ListKeyPolicies`


* :py:class:`KMS.Paginator.ListKeys`



.. py:class:: KMS.Paginator.ListAliases

  ::

    
    paginator = client.get_paginator('list_aliases')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`KMS.Client.list_aliases`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListAliases>`_    


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
            'Aliases': [
                {
                    'AliasName': 'string',
                    'AliasArn': 'string',
                    'TargetKeyId': 'string'
                },
            ],
            'Truncated': True|False,
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Aliases** *(list) --* 

          A list of aliases.

          
          

          - *(dict) --* 

            Contains information about an alias.

            
            

            - **AliasName** *(string) --* 

              String that contains the alias.

              
            

            - **AliasArn** *(string) --* 

              String that contains the key ARN.

              
            

            - **TargetKeyId** *(string) --* 

              String that contains the key identifier referred to by the alias.

              
        
      
        

        - **Truncated** *(boolean) --* 

          A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the ``NextMarker`` element in this response to the ``Marker`` parameter in a subsequent request.

          
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: KMS.Paginator.ListGrants

  ::

    
    paginator = client.get_paginator('list_grants')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`KMS.Client.list_grants`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListGrants>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          KeyId='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      A unique identifier for the customer master key (CMK).

       

      Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

      

    
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
            'Grants': [
                {
                    'KeyId': 'string',
                    'GrantId': 'string',
                    'Name': 'string',
                    'CreationDate': datetime(2015, 1, 1),
                    'GranteePrincipal': 'string',
                    'RetiringPrincipal': 'string',
                    'IssuingAccount': 'string',
                    'Operations': [
                        'Decrypt'|'Encrypt'|'GenerateDataKey'|'GenerateDataKeyWithoutPlaintext'|'ReEncryptFrom'|'ReEncryptTo'|'CreateGrant'|'RetireGrant'|'DescribeKey',
                    ],
                    'Constraints': {
                        'EncryptionContextSubset': {
                            'string': 'string'
                        },
                        'EncryptionContextEquals': {
                            'string': 'string'
                        }
                    }
                },
            ],
            'Truncated': True|False,
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Grants** *(list) --* 

          A list of grants.

          
          

          - *(dict) --* 

            Contains information about an entry in a list of grants.

            
            

            - **KeyId** *(string) --* 

              The unique identifier for the customer master key (CMK) to which the grant applies.

              
            

            - **GrantId** *(string) --* 

              The unique identifier for the grant.

              
            

            - **Name** *(string) --* 

              The friendly name that identifies the grant. If a name was provided in the  CreateGrant request, that name is returned. Otherwise this value is null.

              
            

            - **CreationDate** *(datetime) --* 

              The date and time when the grant was created.

              
            

            - **GranteePrincipal** *(string) --* 

              The principal that receives the grant's permissions.

              
            

            - **RetiringPrincipal** *(string) --* 

              The principal that can retire the grant.

              
            

            - **IssuingAccount** *(string) --* 

              The AWS account under which the grant was issued.

              
            

            - **Operations** *(list) --* 

              The list of operations permitted by the grant.

              
              

              - *(string) --* 
          
            

            - **Constraints** *(dict) --* 

              A list of key-value pairs that must be present in the encryption context of certain subsequent operations that the grant allows.

              
              

              - **EncryptionContextSubset** *(dict) --* 

                A list of key-value pairs, all of which must be present in the encryption context of certain subsequent operations that the grant allows. When certain subsequent operations allowed by the grant include encryption context that matches this list or is a superset of this list, the grant allows the operation. Otherwise, the grant does not allow the operation.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
              

              - **EncryptionContextEquals** *(dict) --* 

                A list of key-value pairs that must be present in the encryption context of certain subsequent operations that the grant allows. When certain subsequent operations allowed by the grant include encryption context that matches this list, the grant allows the operation. Otherwise, the grant does not allow the operation.

                
                

                - *(string) --* 
                  

                  - *(string) --* 
            
          
          
        
      
        

        - **Truncated** *(boolean) --* 

          A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the ``NextMarker`` element in this response to the ``Marker`` parameter in a subsequent request.

          
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: KMS.Paginator.ListKeyPolicies

  ::

    
    paginator = client.get_paginator('list_key_policies')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`KMS.Client.list_key_policies`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListKeyPolicies>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          KeyId='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type KeyId: string
    :param KeyId: **[REQUIRED]** 

      A unique identifier for the customer master key (CMK).

       

      Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

       

      For example:

       

       
      * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``   
       
      * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``   
       

       

      To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

      

    
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
            'PolicyNames': [
                'string',
            ],
            'Truncated': True|False,
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **PolicyNames** *(list) --* 

          A list of policy names. Currently, there is only one policy and it is named "Default".

          
          

          - *(string) --* 
      
        

        - **Truncated** *(boolean) --* 

          A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the ``NextMarker`` element in this response to the ``Marker`` parameter in a subsequent request.

          
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: KMS.Paginator.ListKeys

  ::

    
    paginator = client.get_paginator('list_keys')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`KMS.Client.list_keys`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListKeys>`_    


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
            'Keys': [
                {
                    'KeyId': 'string',
                    'KeyArn': 'string'
                },
            ],
            'Truncated': True|False,
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Keys** *(list) --* 

          A list of customer master keys (CMKs).

          
          

          - *(dict) --* 

            Contains information about each entry in the key list.

            
            

            - **KeyId** *(string) --* 

              Unique identifier of the key.

              
            

            - **KeyArn** *(string) --* 

              ARN of the key.

              
        
      
        

        - **Truncated** *(boolean) --* 

          A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the ``NextMarker`` element in this response to the ``Marker`` parameter in a subsequent request.

          
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    