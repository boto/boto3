

*******
Glacier
*******

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: Glacier.Client

  A low-level client representing Amazon Glacier::

    
    import boto3
    
    client = boto3.client('glacier')

  
  These are the available methods:
  
  *   :py:meth:`~Glacier.Client.abort_multipart_upload`

  
  *   :py:meth:`~Glacier.Client.abort_vault_lock`

  
  *   :py:meth:`~Glacier.Client.add_tags_to_vault`

  
  *   :py:meth:`~Glacier.Client.can_paginate`

  
  *   :py:meth:`~Glacier.Client.complete_multipart_upload`

  
  *   :py:meth:`~Glacier.Client.complete_vault_lock`

  
  *   :py:meth:`~Glacier.Client.create_vault`

  
  *   :py:meth:`~Glacier.Client.delete_archive`

  
  *   :py:meth:`~Glacier.Client.delete_vault`

  
  *   :py:meth:`~Glacier.Client.delete_vault_access_policy`

  
  *   :py:meth:`~Glacier.Client.delete_vault_notifications`

  
  *   :py:meth:`~Glacier.Client.describe_job`

  
  *   :py:meth:`~Glacier.Client.describe_vault`

  
  *   :py:meth:`~Glacier.Client.generate_presigned_url`

  
  *   :py:meth:`~Glacier.Client.get_data_retrieval_policy`

  
  *   :py:meth:`~Glacier.Client.get_job_output`

  
  *   :py:meth:`~Glacier.Client.get_paginator`

  
  *   :py:meth:`~Glacier.Client.get_vault_access_policy`

  
  *   :py:meth:`~Glacier.Client.get_vault_lock`

  
  *   :py:meth:`~Glacier.Client.get_vault_notifications`

  
  *   :py:meth:`~Glacier.Client.get_waiter`

  
  *   :py:meth:`~Glacier.Client.initiate_job`

  
  *   :py:meth:`~Glacier.Client.initiate_multipart_upload`

  
  *   :py:meth:`~Glacier.Client.initiate_vault_lock`

  
  *   :py:meth:`~Glacier.Client.list_jobs`

  
  *   :py:meth:`~Glacier.Client.list_multipart_uploads`

  
  *   :py:meth:`~Glacier.Client.list_parts`

  
  *   :py:meth:`~Glacier.Client.list_provisioned_capacity`

  
  *   :py:meth:`~Glacier.Client.list_tags_for_vault`

  
  *   :py:meth:`~Glacier.Client.list_vaults`

  
  *   :py:meth:`~Glacier.Client.purchase_provisioned_capacity`

  
  *   :py:meth:`~Glacier.Client.remove_tags_from_vault`

  
  *   :py:meth:`~Glacier.Client.set_data_retrieval_policy`

  
  *   :py:meth:`~Glacier.Client.set_vault_access_policy`

  
  *   :py:meth:`~Glacier.Client.set_vault_notifications`

  
  *   :py:meth:`~Glacier.Client.upload_archive`

  
  *   :py:meth:`~Glacier.Client.upload_multipart_part`

  

  .. py:method:: abort_multipart_upload(**kwargs)

    

    This operation aborts a multipart upload identified by the upload ID.

     

    After the Abort Multipart Upload request succeeds, you cannot upload any more parts to the multipart upload or complete the multipart upload. Aborting a completed upload fails. However, aborting an already-aborted upload will succeed, for a short time. For more information about uploading a part and completing a multipart upload, see  UploadMultipartPart and  CompleteMultipartUpload .

     

    This operation is idempotent.

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and underlying REST API, see `Working with Archives in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-archives.html>`__ and `Abort Multipart Upload <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-abort-upload.html>`__ in the *Amazon Glacier Developer Guide* . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/AbortMultipartUpload>`_    


    **Request Syntax** 
    ::

      response = client.abort_multipart_upload(
          vaultName='string',
          uploadId='string'
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    :type uploadId: string
    :param uploadId: **[REQUIRED]** 

      The upload ID of the multipart upload to delete.

      

    
    
    :returns: None

    **Examples** 

    The example deletes an in-progress multipart upload to a vault named my-vault:
    ::

      response = client.abort_multipart_upload(
          accountId='-',
          uploadId='19gaRezEXAMPLES6Ry5YYdqthHOC_kGRCT03L9yetr220UmPtBYKk-OssZtLqyFu7sY1_lR7vgFuJV6NtcV5zpsJ',
          vaultName='my-vault',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: abort_vault_lock(**kwargs)

    

    This operation aborts the vault locking process if the vault lock is not in the ``Locked`` state. If the vault lock is in the ``Locked`` state when this operation is requested, the operation returns an ``AccessDeniedException`` error. Aborting the vault locking process removes the vault lock policy from the specified vault. 

     

    A vault lock is put into the ``InProgress`` state by calling  InitiateVaultLock . A vault lock is put into the ``Locked`` state by calling  CompleteVaultLock . You can get the state of a vault lock by calling  GetVaultLock . For more information about the vault locking process, see `Amazon Glacier Vault Lock <http://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock.html>`__ . For more information about vault lock policies, see `Amazon Glacier Access Control with Vault Lock Policies <http://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock-policy.html>`__ . 

     

    This operation is idempotent. You can successfully invoke this operation multiple times, if the vault lock is in the ``InProgress`` state or if there is no policy associated with the vault.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/AbortVaultLock>`_    


    **Request Syntax** 
    ::

      response = client.abort_vault_lock(
          vaultName='string'
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    
    :returns: None

    **Examples** 

    The example aborts the vault locking process if the vault lock is not in the Locked state for the vault named examplevault.
    ::

      response = client.abort_vault_lock(
          accountId='-',
          vaultName='examplevault',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: add_tags_to_vault(**kwargs)

    

    This operation adds the specified tags to a vault. Each tag is composed of a key and a value. Each vault can have up to 10 tags. If your request would cause the tag limit for the vault to be exceeded, the operation throws the ``LimitExceededException`` error. If a tag already exists on the vault under a specified key, the existing key value will be overwritten. For more information about tags, see `Tagging Amazon Glacier Resources <http://docs.aws.amazon.com/amazonglacier/latest/dev/tagging.html>`__ . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/AddTagsToVault>`_    


    **Request Syntax** 
    ::

      response = client.add_tags_to_vault(
          vaultName='string',
          Tags={
              'string': 'string'
          }
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    :type Tags: dict
    :param Tags: 

      The tags to add to the vault. Each tag is composed of a key and a value. The value can be an empty string.

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    
    :returns: None

    **Examples** 

    The example adds two tags to a my-vault.
    ::

      response = client.add_tags_to_vault(
          Tags={
              'examplekey1': 'examplevalue1',
              'examplekey2': 'examplevalue2',
          },
          accountId='-',
          vaultName='my-vault',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

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


  .. py:method:: complete_multipart_upload(**kwargs)

    

    You call this operation to inform Amazon Glacier that all the archive parts have been uploaded and that Amazon Glacier can now assemble the archive from the uploaded parts. After assembling and saving the archive to the vault, Amazon Glacier returns the URI path of the newly created archive resource. Using the URI path, you can then access the archive. After you upload an archive, you should save the archive ID returned to retrieve the archive at a later point. You can also get the vault inventory to obtain a list of archive IDs in a vault. For more information, see  InitiateJob .

     

    In the request, you must include the computed SHA256 tree hash of the entire archive you have uploaded. For information about computing a SHA256 tree hash, see `Computing Checksums <http://docs.aws.amazon.com/amazonglacier/latest/dev/checksum-calculations.html>`__ . On the server side, Amazon Glacier also constructs the SHA256 tree hash of the assembled archive. If the values match, Amazon Glacier saves the archive to the vault; otherwise, it returns an error, and the operation fails. The  ListParts operation returns a list of parts uploaded for a specific multipart upload. It includes checksum information for each uploaded part that can be used to debug a bad checksum issue.

     

    Additionally, Amazon Glacier also checks for any missing content ranges when assembling the archive, if missing content ranges are found, Amazon Glacier returns an error and the operation fails.

     

    Complete Multipart Upload is an idempotent operation. After your first successful complete multipart upload, if you call the operation again within a short period, the operation will succeed and return the same archive ID. This is useful in the event you experience a network issue that causes an aborted connection or receive a 500 server error, in which case you can repeat your Complete Multipart Upload request and get the same archive ID without creating duplicate archives. Note, however, that after the multipart upload completes, you cannot call the List Parts operation and the multipart upload will not appear in List Multipart Uploads response, even if idempotent complete is possible.

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and underlying REST API, see `Uploading Large Archives in Parts (Multipart Upload) <http://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-archive-mpu.html>`__ and `Complete Multipart Upload <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-complete-upload.html>`__ in the *Amazon Glacier Developer Guide* . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/CompleteMultipartUpload>`_    


    **Request Syntax** 
    ::

      response = client.complete_multipart_upload(
          vaultName='string',
          uploadId='string',
          archiveSize='string',
          checksum='string'
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    :type uploadId: string
    :param uploadId: **[REQUIRED]** 

      The upload ID of the multipart upload.

      

    
    :type archiveSize: string
    :param archiveSize: 

      The total size, in bytes, of the entire archive. This value should be the sum of all the sizes of the individual parts that you uploaded.

      

    
    :type checksum: string
    :param checksum: 

      The SHA256 tree hash of the entire archive. It is the tree hash of SHA256 tree hash of the individual parts. If the value you specify in the request does not match the SHA256 tree hash of the final assembled archive as computed by Amazon Glacier, Amazon Glacier returns an error and the request fails.

            
        This is a required field.

        Ideally you will want to compute this value with checksums from
        previous uploaded parts, using the algorithm described in
        `Glacier documentation <http://docs.aws.amazon.com/amazonglacier/latest/dev/checksum-calculations.html>`_.

        But if you prefer, you can also use botocore.utils.calculate_tree_hash()
        to compute it from raw file by::

            checksum = calculate_tree_hash(open('your_file.txt', 'rb'))

        


    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'location': 'string',
            'checksum': 'string',
            'archiveId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the Amazon Glacier response to your request.

         

        For information about the underlying REST API, see `Upload Archive <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-post.html>`__ . For conceptual information, see `Working with Archives in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-archives.html>`__ .

        
        

        - **location** *(string) --* 

          The relative URI path of the newly added archive resource.

          
        

        - **checksum** *(string) --* 

          The checksum of the archive computed by Amazon Glacier.

          
        

        - **archiveId** *(string) --* 

          The ID of the archive. This value is also included as part of the location.

          
    

    **Examples** 

    The example completes a multipart upload for a 3 MiB archive.
    ::

      response = client.complete_multipart_upload(
          accountId='-',
          archiveSize='3145728',
          checksum='9628195fcdbcbbe76cdde456d4646fa7de5f219fb39823836d81f0cc0e18aa67',
          uploadId='19gaRezEXAMPLES6Ry5YYdqthHOC_kGRCT03L9yetr220UmPtBYKk-OssZtLqyFu7sY1_lR7vgFuJV6NtcV5zpsJ',
          vaultName='my-vault',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'archiveId': 'NkbByEejwEggmBz2fTHgJrg0XBoDfjP4q6iu87-TjhqG6eGoOY9Z8i1_AUyUsuhPAdTqLHy8pTl5nfCFJmDl2yEZONi5L26Omw12vcs01MNGntHEQL8MBfGlqrEXAMPLEArchiveId',
          'checksum': '9628195fcdbcbbe76cdde456d4646fa7de5f219fb39823836d81f0cc0e18aa67',
          'location': '/111122223333/vaults/my-vault/archives/NkbByEejwEggmBz2fTHgJrg0XBoDfjP4q6iu87-TjhqG6eGoOY9Z8i1_AUyUsuhPAdTqLHy8pTl5nfCFJmDl2yEZONi5L26Omw12vcs01MNGntHEQL8MBfGlqrEXAMPLEArchiveId',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: complete_vault_lock(**kwargs)

    

    This operation completes the vault locking process by transitioning the vault lock from the ``InProgress`` state to the ``Locked`` state, which causes the vault lock policy to become unchangeable. A vault lock is put into the ``InProgress`` state by calling  InitiateVaultLock . You can obtain the state of the vault lock by calling  GetVaultLock . For more information about the vault locking process, `Amazon Glacier Vault Lock <http://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock.html>`__ . 

     

    This operation is idempotent. This request is always successful if the vault lock is in the ``Locked`` state and the provided lock ID matches the lock ID originally used to lock the vault.

     

    If an invalid lock ID is passed in the request when the vault lock is in the ``Locked`` state, the operation returns an ``AccessDeniedException`` error. If an invalid lock ID is passed in the request when the vault lock is in the ``InProgress`` state, the operation throws an ``InvalidParameter`` error.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/CompleteVaultLock>`_    


    **Request Syntax** 
    ::

      response = client.complete_vault_lock(
          vaultName='string',
          lockId='string'
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    :type lockId: string
    :param lockId: **[REQUIRED]** 

      The ``lockId`` value is the lock ID obtained from a  InitiateVaultLock request.

      

    
    
    :returns: None

    **Examples** 

    The example completes the vault locking process by transitioning the vault lock from the InProgress state to the Locked state.
    ::

      response = client.complete_vault_lock(
          accountId='-',
          lockId='AE863rKkWZU53SLW5be4DUcW',
          vaultName='example-vault',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_vault(**kwargs)

    

    This operation creates a new vault with the specified name. The name of the vault must be unique within a region for an AWS account. You can create up to 1,000 vaults per account. If you need to create more vaults, contact Amazon Glacier.

     

    You must use the following guidelines when naming a vault.

     

     
    * Names can be between 1 and 255 characters long. 
     
    * Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), and '.' (period). 
     

     

    This operation is idempotent.

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and underlying REST API, see `Creating a Vault in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/creating-vaults.html>`__ and `Create Vault <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-put.html>`__ in the *Amazon Glacier Developer Guide* . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/CreateVault>`_    


    **Request Syntax** 
    ::

      response = client.create_vault(
          vaultName='string'
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'location': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the Amazon Glacier response to your request.

        
        

        - **location** *(string) --* 

          The URI of the vault that was created.

          
    

    **Examples** 

    The following example creates a new vault named my-vault.
    ::

      response = client.create_vault(
          accountId='-',
          vaultName='my-vault',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'location': '/111122223333/vaults/my-vault',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_archive(**kwargs)

    

    This operation deletes an archive from a vault. Subsequent requests to initiate a retrieval of this archive will fail. Archive retrievals that are in progress for this archive ID may or may not succeed according to the following scenarios:

     

     
    * If the archive retrieval job is actively preparing the data for download when Amazon Glacier receives the delete archive request, the archival retrieval operation might fail. 
     
    * If the archive retrieval job has successfully prepared the archive for download when Amazon Glacier receives the delete archive request, you will be able to download the output. 
     

     

    This operation is idempotent. Attempting to delete an already-deleted archive does not result in an error.

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and underlying REST API, see `Deleting an Archive in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-an-archive.html>`__ and `Delete Archive <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-delete.html>`__ in the *Amazon Glacier Developer Guide* . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/DeleteArchive>`_    


    **Request Syntax** 
    ::

      response = client.delete_archive(
          vaultName='string',
          archiveId='string'
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    :type archiveId: string
    :param archiveId: **[REQUIRED]** 

      The ID of the archive to delete.

      

    
    
    :returns: None

    **Examples** 

    The example deletes the archive specified by the archive ID.
    ::

      response = client.delete_archive(
          accountId='-',
          archiveId='NkbByEejwEggmBz2fTHgJrg0XBoDfjP4q6iu87-TjhqG6eGoOY9Z8i1_AUyUsuhPAdTqLHy8pTl5nfCFJmDl2yEZONi5L26Omw12vcs01MNGntHEQL8MBfGlqrEXAMPLEArchiveId',
          vaultName='examplevault',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_vault(**kwargs)

    

    This operation deletes a vault. Amazon Glacier will delete a vault only if there are no archives in the vault as of the last inventory and there have been no writes to the vault since the last inventory. If either of these conditions is not satisfied, the vault deletion fails (that is, the vault is not removed) and Amazon Glacier returns an error. You can use  DescribeVault to return the number of archives in a vault, and you can use `Initiate a Job (POST jobs) <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html>`__ to initiate a new inventory retrieval for a vault. The inventory contains the archive IDs you use to delete archives using `Delete Archive (DELETE archive) <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-delete.html>`__ .

     

    This operation is idempotent.

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and underlying REST API, see `Deleting a Vault in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-vaults.html>`__ and `Delete Vault <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-delete.html>`__ in the *Amazon Glacier Developer Guide* . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/DeleteVault>`_    


    **Request Syntax** 
    ::

      response = client.delete_vault(
          vaultName='string'
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    
    :returns: None

    **Examples** 

    The example deletes a vault named my-vault:
    ::

      response = client.delete_vault(
          accountId='-',
          vaultName='my-vault',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_vault_access_policy(**kwargs)

    

    This operation deletes the access policy associated with the specified vault. The operation is eventually consistent; that is, it might take some time for Amazon Glacier to completely remove the access policy, and you might still see the effect of the policy for a short time after you send the delete request.

     

    This operation is idempotent. You can invoke delete multiple times, even if there is no policy associated with the vault. For more information about vault access policies, see `Amazon Glacier Access Control with Vault Access Policies <http://docs.aws.amazon.com/amazonglacier/latest/dev/vault-access-policy.html>`__ . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/DeleteVaultAccessPolicy>`_    


    **Request Syntax** 
    ::

      response = client.delete_vault_access_policy(
          vaultName='string'
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. 

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    
    :returns: None

    **Examples** 

    The example deletes the access policy associated with the vault named examplevault.
    ::

      response = client.delete_vault_access_policy(
          accountId='-',
          vaultName='examplevault',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_vault_notifications(**kwargs)

    

    This operation deletes the notification configuration set for a vault. The operation is eventually consistent; that is, it might take some time for Amazon Glacier to completely disable the notifications and you might still receive some notifications for a short time after you send the delete request.

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and underlying REST API, see `Configuring Vault Notifications in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/configuring-notifications.html>`__ and `Delete Vault Notification Configuration <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-notifications-delete.html>`__ in the Amazon Glacier Developer Guide. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/DeleteVaultNotifications>`_    


    **Request Syntax** 
    ::

      response = client.delete_vault_notifications(
          vaultName='string'
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. 

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    
    :returns: None

    **Examples** 

    The example deletes the notification configuration set for the vault named examplevault.
    ::

      response = client.delete_vault_notifications(
          accountId='-',
          vaultName='examplevault',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_job(**kwargs)

    

    This operation returns information about a job you previously initiated, including the job initiation date, the user who initiated the job, the job status code/message and the Amazon SNS topic to notify after Amazon Glacier completes the job. For more information about initiating a job, see  InitiateJob . 

     

    .. note::

       

      This operation enables you to check the status of your job. However, it is strongly recommended that you set up an Amazon SNS topic and specify it in your initiate job request so that Amazon Glacier can notify the topic after it completes the job.

       

     

    A job ID will not expire for at least 24 hours after Amazon Glacier completes the job.

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For more information about using this operation, see the documentation for the underlying REST API `Describe Job <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-describe-job-get.html>`__ in the *Amazon Glacier Developer Guide* . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/DescribeJob>`_    


    **Request Syntax** 
    ::

      response = client.describe_job(
          vaultName='string',
          jobId='string'
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. 

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    :type jobId: string
    :param jobId: **[REQUIRED]** 

      The ID of the job to describe.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'JobId': 'string',
            'JobDescription': 'string',
            'Action': 'ArchiveRetrieval'|'InventoryRetrieval'|'Select',
            'ArchiveId': 'string',
            'VaultARN': 'string',
            'CreationDate': 'string',
            'Completed': True|False,
            'StatusCode': 'InProgress'|'Succeeded'|'Failed',
            'StatusMessage': 'string',
            'ArchiveSizeInBytes': 123,
            'InventorySizeInBytes': 123,
            'SNSTopic': 'string',
            'CompletionDate': 'string',
            'SHA256TreeHash': 'string',
            'ArchiveSHA256TreeHash': 'string',
            'RetrievalByteRange': 'string',
            'Tier': 'string',
            'InventoryRetrievalParameters': {
                'Format': 'string',
                'StartDate': 'string',
                'EndDate': 'string',
                'Limit': 'string',
                'Marker': 'string'
            },
            'JobOutputPath': 'string',
            'SelectParameters': {
                'InputSerialization': {
                    'csv': {
                        'FileHeaderInfo': 'USE'|'IGNORE'|'NONE',
                        'Comments': 'string',
                        'QuoteEscapeCharacter': 'string',
                        'RecordDelimiter': 'string',
                        'FieldDelimiter': 'string',
                        'QuoteCharacter': 'string'
                    }
                },
                'ExpressionType': 'SQL',
                'Expression': 'string',
                'OutputSerialization': {
                    'csv': {
                        'QuoteFields': 'ALWAYS'|'ASNEEDED',
                        'QuoteEscapeCharacter': 'string',
                        'RecordDelimiter': 'string',
                        'FieldDelimiter': 'string',
                        'QuoteCharacter': 'string'
                    }
                }
            },
            'OutputLocation': {
                'S3': {
                    'BucketName': 'string',
                    'Prefix': 'string',
                    'Encryption': {
                        'EncryptionType': 'aws:kms'|'AES256',
                        'KMSKeyId': 'string',
                        'KMSContext': 'string'
                    },
                    'CannedACL': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control',
                    'AccessControlList': [
                        {
                            'Grantee': {
                                'Type': 'AmazonCustomerByEmail'|'CanonicalUser'|'Group',
                                'DisplayName': 'string',
                                'URI': 'string',
                                'ID': 'string',
                                'EmailAddress': 'string'
                            },
                            'Permission': 'FULL_CONTROL'|'WRITE'|'WRITE_ACP'|'READ'|'READ_ACP'
                        },
                    ],
                    'Tagging': {
                        'string': 'string'
                    },
                    'UserMetadata': {
                        'string': 'string'
                    },
                    'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the description of an Amazon Glacier job.

        
        

        - **JobId** *(string) --* 

          An opaque string that identifies an Amazon Glacier job.

          
        

        - **JobDescription** *(string) --* 

          The job description provided when initiating the job.

          
        

        - **Action** *(string) --* 

          The job type. This value is either ``ArchiveRetrieval`` , ``InventoryRetrieval`` , or ``Select`` . 

          
        

        - **ArchiveId** *(string) --* 

          The archive ID requested for a select job or archive retrieval. Otherwise, this field is null.

          
        

        - **VaultARN** *(string) --* 

          The Amazon Resource Name (ARN) of the vault from which an archive retrieval was requested.

          
        

        - **CreationDate** *(string) --* 

          The UTC date when the job was created. This value is a string representation of ISO 8601 date format, for example ``"2012-03-20T17:03:43.221Z"`` .

          
        

        - **Completed** *(boolean) --* 

          The job status. When a job is completed, you get the job's output using Get Job Output (GET output).

          
        

        - **StatusCode** *(string) --* 

          The status code can be ``InProgress`` , ``Succeeded`` , or ``Failed`` , and indicates the status of the job.

          
        

        - **StatusMessage** *(string) --* 

          A friendly message that describes the job status.

          
        

        - **ArchiveSizeInBytes** *(integer) --* 

          For an archive retrieval job, this value is the size in bytes of the archive being requested for download. For an inventory retrieval or select job, this value is null.

          
        

        - **InventorySizeInBytes** *(integer) --* 

          For an inventory retrieval job, this value is the size in bytes of the inventory requested for download. For an archive retrieval or select job, this value is null.

          
        

        - **SNSTopic** *(string) --* 

          An Amazon SNS topic that receives notification.

          
        

        - **CompletionDate** *(string) --* 

          The UTC time that the job request completed. While the job is in progress, the value is null.

          
        

        - **SHA256TreeHash** *(string) --* 

          For an archive retrieval job, this value is the checksum of the archive. Otherwise, this value is null.

           

          The SHA256 tree hash value for the requested range of an archive. If the **InitiateJob** request for an archive specified a tree-hash aligned range, then this field returns a value.

           

          If the whole archive is retrieved, this value is the same as the ArchiveSHA256TreeHash value.

           

          This field is null for the following:

           

           
          * Archive retrieval jobs that specify a range that is not tree-hash aligned 
           

           

           
          * Archival jobs that specify a range that is equal to the whole archive, when the job status is ``InProgress``   
           

           

           
          * Inventory jobs 
           
          * Select jobs 
           

          
        

        - **ArchiveSHA256TreeHash** *(string) --* 

          The SHA256 tree hash of the entire archive for an archive retrieval. For inventory retrieval or select jobs, this field is null.

          
        

        - **RetrievalByteRange** *(string) --* 

          The retrieved byte range for archive retrieval jobs in the form *StartByteValue* -*EndByteValue* . If no range was specified in the archive retrieval, then the whole archive is retrieved. In this case, *StartByteValue* equals 0 and *EndByteValue* equals the size of the archive minus 1. For inventory retrieval or select jobs, this field is null. 

          
        

        - **Tier** *(string) --* 

          The retrieval option to use for the archive retrieval. Valid values are ``Expedited`` , ``Standard`` , or ``Bulk`` . ``Standard`` is the default.

          
        

        - **InventoryRetrievalParameters** *(dict) --* 

          Parameters used for range inventory retrieval.

          
          

          - **Format** *(string) --* 

            The output format for the vault inventory list, which is set by the **InitiateJob** request when initiating a job to retrieve a vault inventory. Valid values are ``CSV`` and ``JSON`` .

            
          

          - **StartDate** *(string) --* 

            The start of the date range in Universal Coordinated Time (UTC) for vault inventory retrieval that includes archives created on or after this date. This value should be a string in the ISO 8601 date format, for example ``2013-03-20T17:03:43Z`` .

            
          

          - **EndDate** *(string) --* 

            The end of the date range in UTC for vault inventory retrieval that includes archives created before this date. This value should be a string in the ISO 8601 date format, for example ``2013-03-20T17:03:43Z`` .

            
          

          - **Limit** *(string) --* 

            The maximum number of inventory items returned per vault inventory retrieval request. This limit is set when initiating the job with the a **InitiateJob** request. 

            
          

          - **Marker** *(string) --* 

            An opaque string that represents where to continue pagination of the vault inventory retrieval results. You use the marker in a new **InitiateJob** request to obtain additional inventory items. If there are no more inventory items, this value is ``null`` . For more information, see `Range Inventory Retrieval <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html#api-initiate-job-post-vault-inventory-list-filtering>`__ .

            
      
        

        - **JobOutputPath** *(string) --* 

          Contains the job output location.

          
        

        - **SelectParameters** *(dict) --* 

          Contains the parameters that define a select job.

          
          

          - **InputSerialization** *(dict) --* 

            Describes the serialization format of the object.

            
            

            - **csv** *(dict) --* 

              Describes the serialization of a CSV-encoded object.

              
              

              - **FileHeaderInfo** *(string) --* 

                Describes the first line of input. Valid values are ``None`` , ``Ignore`` , and ``Use`` .

                
              

              - **Comments** *(string) --* 

                A single character used to indicate that a row should be ignored when the character is present at the start of that row.

                
              

              - **QuoteEscapeCharacter** *(string) --* 

                A single character used for escaping the quotation-mark character inside an already escaped value.

                
              

              - **RecordDelimiter** *(string) --* 

                A value used to separate individual records from each other.

                
              

              - **FieldDelimiter** *(string) --* 

                A value used to separate individual fields from each other within a record.

                
              

              - **QuoteCharacter** *(string) --* 

                A value used as an escape character where the field delimiter is part of the value.

                
          
        
          

          - **ExpressionType** *(string) --* 

            The type of the provided expression, for example ``SQL`` .

            
          

          - **Expression** *(string) --* 

            The expression that is used to select the object.

            
          

          - **OutputSerialization** *(dict) --* 

            Describes how the results of the select job are serialized.

            
            

            - **csv** *(dict) --* 

              Describes the serialization of CSV-encoded query results.

              
              

              - **QuoteFields** *(string) --* 

                A value that indicates whether all output fields should be contained within quotation marks.

                
              

              - **QuoteEscapeCharacter** *(string) --* 

                A single character used for escaping the quotation-mark character inside an already escaped value.

                
              

              - **RecordDelimiter** *(string) --* 

                A value used to separate individual records from each other.

                
              

              - **FieldDelimiter** *(string) --* 

                A value used to separate individual fields from each other within a record.

                
              

              - **QuoteCharacter** *(string) --* 

                A value used as an escape character where the field delimiter is part of the value.

                
          
        
      
        

        - **OutputLocation** *(dict) --* 

          Contains the location where the data from the select job is stored.

          
          

          - **S3** *(dict) --* 

            Describes an S3 location that will receive the results of the restore request.

            
            

            - **BucketName** *(string) --* 

              The name of the bucket where the restore results are stored.

              
            

            - **Prefix** *(string) --* 

              The prefix that is prepended to the restore results for this request.

              
            

            - **Encryption** *(dict) --* 

              Contains information about the encryption used to store the job results in Amazon S3.

              
              

              - **EncryptionType** *(string) --* 

                The server-side encryption algorithm used when storing job results in Amazon S3, for example ``AES256`` or ``aws:kms`` .

                
              

              - **KMSKeyId** *(string) --* 

                The AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or Signature Version 4. 

                
              

              - **KMSContext** *(string) --* 

                Optional. If the encryption type is ``aws:kms`` , you can use this value to specify the encryption context for the restore results.

                
          
            

            - **CannedACL** *(string) --* 

              The canned ACL to apply to the restore results.

              
            

            - **AccessControlList** *(list) --* 

              A list of grants that control access to the staged results.

              
              

              - *(dict) --* 

                Contains information about a grant.

                
                

                - **Grantee** *(dict) --* 

                  The grantee.

                  
                  

                  - **Type** *(string) --* 

                    Type of grantee

                    
                  

                  - **DisplayName** *(string) --* 

                    Screen name of the grantee.

                    
                  

                  - **URI** *(string) --* 

                    URI of the grantee group.

                    
                  

                  - **ID** *(string) --* 

                    The canonical user ID of the grantee.

                    
                  

                  - **EmailAddress** *(string) --* 

                    Email address of the grantee.

                    
              
                

                - **Permission** *(string) --* 

                  Specifies the permission given to the grantee. 

                  
            
          
            

            - **Tagging** *(dict) --* 

              The tag-set that is applied to the restore results.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **UserMetadata** *(dict) --* 

              A map of metadata to store with the restore results in Amazon S3.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **StorageClass** *(string) --* 

              The storage class used to store the restore results.

              
        
      
    

    **Examples** 

    The example returns information about the previously initiated job specified by the job ID.
    ::

      response = client.describe_job(
          accountId='-',
          jobId='zbxcm3Z_3z5UkoroF7SuZKrxgGoDc3RloGduS7Eg-RO47Yc6FxsdGBgf_Q2DK5Ejh18CnTS5XW4_XqlNHS61dsO4Cn',
          vaultName='my-vault',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Action': 'InventoryRetrieval',
          'Completed': False,
          'CreationDate': '2015-07-17T20:23:41.616Z',
          'InventoryRetrievalParameters': {
              'Format': 'JSON',
          },
          'JobId': 'zbxcm3Z_3z5UkoroF7SuZKrxgGoDc3RloGduS7Eg-RO47Yc6FxsdGBgf_Q2DK5Ejh18CnTS5XW4_XqlNHS61dsO4CnMW',
          'StatusCode': 'InProgress',
          'VaultARN': 'arn:aws:glacier:us-west-2:0123456789012:vaults/my-vault',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_vault(**kwargs)

    

    This operation returns information about a vault, including the vault's Amazon Resource Name (ARN), the date the vault was created, the number of archives it contains, and the total size of all the archives in the vault. The number of archives and their total size are as of the last inventory generation. This means that if you add or remove an archive from a vault, and then immediately use Describe Vault, the change in contents will not be immediately reflected. If you want to retrieve the latest inventory of the vault, use  InitiateJob . Amazon Glacier generates vault inventories approximately daily. For more information, see `Downloading a Vault Inventory in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/vault-inventory.html>`__ . 

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and underlying REST API, see `Retrieving Vault Metadata in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/retrieving-vault-info.html>`__ and `Describe Vault <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-get.html>`__ in the *Amazon Glacier Developer Guide* . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/DescribeVault>`_    


    **Request Syntax** 
    ::

      response = client.describe_vault(
          vaultName='string'
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. 

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'VaultARN': 'string',
            'VaultName': 'string',
            'CreationDate': 'string',
            'LastInventoryDate': 'string',
            'NumberOfArchives': 123,
            'SizeInBytes': 123
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the Amazon Glacier response to your request.

        
        

        - **VaultARN** *(string) --* 

          The Amazon Resource Name (ARN) of the vault.

          
        

        - **VaultName** *(string) --* 

          The name of the vault.

          
        

        - **CreationDate** *(string) --* 

          The Universal Coordinated Time (UTC) date when the vault was created. This value should be a string in the ISO 8601 date format, for example ``2012-03-20T17:03:43.221Z`` .

          
        

        - **LastInventoryDate** *(string) --* 

          The Universal Coordinated Time (UTC) date when Amazon Glacier completed the last vault inventory. This value should be a string in the ISO 8601 date format, for example ``2012-03-20T17:03:43.221Z`` .

          
        

        - **NumberOfArchives** *(integer) --* 

          The number of archives in the vault as of the last inventory date. This field will return ``null`` if an inventory has not yet run on the vault, for example if you just created the vault.

          
        

        - **SizeInBytes** *(integer) --* 

          Total size, in bytes, of the archives in the vault as of the last inventory date. This field will return null if an inventory has not yet run on the vault, for example if you just created the vault.

          
    

    **Examples** 

    The example retrieves data about a vault named my-vault.
    ::

      response = client.describe_vault(
          accountId='-',
          vaultName='my-vault',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'CreationDate': '2016-09-23T19:27:18.665Z',
          'NumberOfArchives': 0,
          'SizeInBytes': 0,
          'VaultARN': 'arn:aws:glacier:us-west-2:111122223333:vaults/my-vault',
          'VaultName': 'my-vault',
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


  .. py:method:: get_data_retrieval_policy(**kwargs)

    

    This operation returns the current data retrieval policy for the account and region specified in the GET request. For more information about data retrieval policies, see `Amazon Glacier Data Retrieval Policies <http://docs.aws.amazon.com/amazonglacier/latest/dev/data-retrieval-policy.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/GetDataRetrievalPolicy>`_    


    **Request Syntax** 
    ::

      response = client.get_data_retrieval_policy(
          
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID. 

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Policy': {
                'Rules': [
                    {
                        'Strategy': 'string',
                        'BytesPerHour': 123
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the Amazon Glacier response to the ``GetDataRetrievalPolicy`` request.

        
        

        - **Policy** *(dict) --* 

          Contains the returned data retrieval policy in JSON format.

          
          

          - **Rules** *(list) --* 

            The policy rule. Although this is a list type, currently there must be only one rule, which contains a Strategy field and optionally a BytesPerHour field.

            
            

            - *(dict) --* 

              Data retrieval policy rule.

              
              

              - **Strategy** *(string) --* 

                The type of data retrieval policy to set.

                 

                Valid values: BytesPerHour|FreeTier|None

                
              

              - **BytesPerHour** *(integer) --* 

                The maximum number of bytes that can be retrieved in an hour.

                 

                This field is required only if the value of the Strategy field is ``BytesPerHour`` . Your PUT operation will be rejected if the Strategy field is not set to ``BytesPerHour`` and you set this field.

                
          
        
      
    

    **Examples** 

    The example returns the current data retrieval policy for the account.
    ::

      response = client.get_data_retrieval_policy(
          accountId='-',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Policy': {
              'Rules': [
                  {
                      'BytesPerHour': 10737418240,
                      'Strategy': 'BytesPerHour',
                  },
              ],
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_job_output(**kwargs)

    

    This operation downloads the output of the job you initiated using  InitiateJob . Depending on the job type you specified when you initiated the job, the output will be either the content of an archive or a vault inventory.

     

    You can download all the job output or download a portion of the output by specifying a byte range. In the case of an archive retrieval job, depending on the byte range you specify, Amazon Glacier returns the checksum for the portion of the data. You can compute the checksum on the client and verify that the values match to ensure the portion you downloaded is the correct data.

     

    A job ID will not expire for at least 24 hours after Amazon Glacier completes the job. That a byte range. For both archive and inventory retrieval jobs, you should verify the downloaded size against the size returned in the headers from the **Get Job Output** response.

     

    For archive retrieval jobs, you should also verify that the size is what you expected. If you download a portion of the output, the expected size is based on the range of bytes you specified. For example, if you specify a range of ``bytes=0-1048575`` , you should verify your download size is 1,048,576 bytes. If you download an entire archive, the expected size is the size of the archive when you uploaded it to Amazon Glacier The expected size is also returned in the headers from the **Get Job Output** response.

     

    In the case of an archive retrieval job, depending on the byte range you specify, Amazon Glacier returns the checksum for the portion of the data. To ensure the portion you downloaded is the correct data, compute the checksum on the client, verify that the values match, and verify that the size is what you expected.

     

    A job ID does not expire for at least 24 hours after Amazon Glacier completes the job. That is, you can download the job output within the 24 hours period after Amazon Glacier completes the job.

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and the underlying REST API, see `Downloading a Vault Inventory <http://docs.aws.amazon.com/amazonglacier/latest/dev/vault-inventory.html>`__ , `Downloading an Archive <http://docs.aws.amazon.com/amazonglacier/latest/dev/downloading-an-archive.html>`__ , and `Get Job Output <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-job-output-get.html>`__  

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/GetJobOutput>`_    


    **Request Syntax** 
    ::

      response = client.get_job_output(
          vaultName='string',
          jobId='string',
          range='string'
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    :type jobId: string
    :param jobId: **[REQUIRED]** 

      The job ID whose data is downloaded.

      

    
    :type range: string
    :param range: 

      The range of bytes to retrieve from the output. For example, if you want to download the first 1,048,576 bytes, specify the range as ``bytes=0-1048575`` . By default, this operation downloads the entire output.

       

      If the job output is large, then you can use a range to retrieve a portion of the output. This allows you to download the entire output in smaller chunks of bytes. For example, suppose you have 1 GB of job output you want to download and you decide to download 128 MB chunks of data at a time, which is a total of eight Get Job Output requests. You use the following process to download the job output:

       

       
      * Download a 128 MB chunk of output by specifying the appropriate byte range. Verify that all 128 MB of data was received. 
       
      * Along with the data, the response includes a SHA256 tree hash of the payload. You compute the checksum of the payload on the client and compare it with the checksum you received in the response to ensure you received all the expected data. 
       
      * Repeat steps 1 and 2 for all the eight 128 MB chunks of output data, each time specifying the appropriate byte range. 
       
      * After downloading all the parts of the job output, you have a list of eight checksum values. Compute the tree hash of these values to find the checksum of the entire output. Using the  DescribeJob API, obtain job information of the job that provided you the output. The response includes the checksum of the entire archive stored in Amazon Glacier. You compare this value with the checksum you computed to ensure you have downloaded the entire archive content with no errors.  
       

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'body': StreamingBody(),
            'checksum': 'string',
            'status': 123,
            'contentRange': 'string',
            'acceptRanges': 'string',
            'contentType': 'string',
            'archiveDescription': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the Amazon Glacier response to your request.

        
        

        - **body** (:class:`.StreamingBody`) -- 

          The job data, either archive data or inventory data.

          
        

        - **checksum** *(string) --* 

          The checksum of the data in the response. This header is returned only when retrieving the output for an archive retrieval job. Furthermore, this header appears only under the following conditions:

           

           
          * You get the entire range of the archive. 
           
          * You request a range to return of the archive that starts and ends on a multiple of 1 MB. For example, if you have an 3.1 MB archive and you specify a range to return that starts at 1 MB and ends at 2 MB, then the x-amz-sha256-tree-hash is returned as a response header. 
           
          * You request a range of the archive to return that starts on a multiple of 1 MB and goes to the end of the archive. For example, if you have a 3.1 MB archive and you specify a range that starts at 2 MB and ends at 3.1 MB (the end of the archive), then the x-amz-sha256-tree-hash is returned as a response header. 
           

          
        

        - **status** *(integer) --* 

          The HTTP response code for a job output request. The value depends on whether a range was specified in the request.

          
        

        - **contentRange** *(string) --* 

          The range of bytes returned by Amazon Glacier. If only partial output is downloaded, the response provides the range of bytes Amazon Glacier returned. For example, bytes 0-1048575/8388608 returns the first 1 MB from 8 MB.

          
        

        - **acceptRanges** *(string) --* 

          Indicates the range units accepted. For more information, see `RFC2616 <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html>`__ . 

          
        

        - **contentType** *(string) --* 

          The Content-Type depends on whether the job output is an archive or a vault inventory. For archive data, the Content-Type is application/octet-stream. For vault inventory, if you requested CSV format when you initiated the job, the Content-Type is text/csv. Otherwise, by default, vault inventory is returned as JSON, and the Content-Type is application/json.

          
        

        - **archiveDescription** *(string) --* 

          The description of an archive.

          
    

    **Examples** 

    The example downloads the output of a previously initiated inventory retrieval job that is identified by the job ID.
    ::

      response = client.get_job_output(
          accountId='-',
          jobId='zbxcm3Z_3z5UkoroF7SuZKrxgGoDc3RloGduS7Eg-RO47Yc6FxsdGBgf_Q2DK5Ejh18CnTS5XW4_XqlNHS61dsO4CnMW',
          range='',
          vaultName='my-vaul',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'acceptRanges': 'bytes',
          'body': 'inventory-data',
          'contentType': 'application/json',
          'status': 200,
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


  .. py:method:: get_vault_access_policy(**kwargs)

    

    This operation retrieves the ``access-policy`` subresource set on the vault; for more information on setting this subresource, see `Set Vault Access Policy (PUT access-policy) <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-SetVaultAccessPolicy.html>`__ . If there is no access policy set on the vault, the operation returns a ``404 Not found`` error. For more information about vault access policies, see `Amazon Glacier Access Control with Vault Access Policies <http://docs.aws.amazon.com/amazonglacier/latest/dev/vault-access-policy.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/GetVaultAccessPolicy>`_    


    **Request Syntax** 
    ::

      response = client.get_vault_access_policy(
          vaultName='string'
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'policy': {
                'Policy': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Output for GetVaultAccessPolicy.

        
        

        - **policy** *(dict) --* 

          Contains the returned vault access policy as a JSON string.

          
          

          - **Policy** *(string) --* 

            The vault access policy.

            
      
    

    **Examples** 

    The example retrieves the access-policy set on the vault named example-vault.
    ::

      response = client.get_vault_access_policy(
          accountId='-',
          vaultName='example-vault',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'policy': {
              'Policy': '{"Version":"2012-10-17","Statement":[{"Sid":"Define-owner-access-rights","Effect":"Allow","Principal":{"AWS":"arn:aws:iam::999999999999:root"},"Action":"glacier:DeleteArchive","Resource":"arn:aws:glacier:us-west-2:999999999999:vaults/examplevault"}]}',
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_vault_lock(**kwargs)

    

    This operation retrieves the following attributes from the ``lock-policy`` subresource set on the specified vault: 

     

     
    * The vault lock policy set on the vault. 
     
    * The state of the vault lock, which is either ``InProgess`` or ``Locked`` . 
     
    * When the lock ID expires. The lock ID is used to complete the vault locking process. 
     
    * When the vault lock was initiated and put into the ``InProgress`` state. 
     

     

    A vault lock is put into the ``InProgress`` state by calling  InitiateVaultLock . A vault lock is put into the ``Locked`` state by calling  CompleteVaultLock . You can abort the vault locking process by calling  AbortVaultLock . For more information about the vault locking process, `Amazon Glacier Vault Lock <http://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock.html>`__ . 

     

    If there is no vault lock policy set on the vault, the operation returns a ``404 Not found`` error. For more information about vault lock policies, `Amazon Glacier Access Control with Vault Lock Policies <http://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock-policy.html>`__ . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/GetVaultLock>`_    


    **Request Syntax** 
    ::

      response = client.get_vault_lock(
          vaultName='string'
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Policy': 'string',
            'State': 'string',
            'ExpirationDate': 'string',
            'CreationDate': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the Amazon Glacier response to your request.

        
        

        - **Policy** *(string) --* 

          The vault lock policy as a JSON string, which uses "\" as an escape character.

          
        

        - **State** *(string) --* 

          The state of the vault lock. ``InProgress`` or ``Locked`` .

          
        

        - **ExpirationDate** *(string) --* 

          The UTC date and time at which the lock ID expires. This value can be ``null`` if the vault lock is in a ``Locked`` state.

          
        

        - **CreationDate** *(string) --* 

          The UTC date and time at which the vault lock was put into the ``InProgress`` state.

          
    

    **Examples** 

    The example retrieves the attributes from the lock-policy subresource set on the vault named examplevault.
    ::

      response = client.get_vault_lock(
          accountId='-',
          vaultName='examplevault',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'CreationDate': 'exampledate',
          'ExpirationDate': 'exampledate',
          'Policy': '{"Version":"2012-10-17","Statement":[{"Sid":"Define-vault-lock","Effect":"Deny","Principal":{"AWS":"arn:aws:iam::999999999999:root"},"Action":"glacier:DeleteArchive","Resource":"arn:aws:glacier:us-west-2:999999999999:vaults/examplevault","Condition":{"NumericLessThanEquals":{"glacier:ArchiveAgeinDays":"365"}}}]}',
          'State': 'InProgress',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_vault_notifications(**kwargs)

    

    This operation retrieves the ``notification-configuration`` subresource of the specified vault.

     

    For information about setting a notification configuration on a vault, see  SetVaultNotifications . If a notification configuration for a vault is not set, the operation returns a ``404 Not Found`` error. For more information about vault notifications, see `Configuring Vault Notifications in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/configuring-notifications.html>`__ . 

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and underlying REST API, see `Configuring Vault Notifications in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/configuring-notifications.html>`__ and `Get Vault Notification Configuration <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-notifications-get.html>`__ in the *Amazon Glacier Developer Guide* . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/GetVaultNotifications>`_    


    **Request Syntax** 
    ::

      response = client.get_vault_notifications(
          vaultName='string'
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'vaultNotificationConfig': {
                'SNSTopic': 'string',
                'Events': [
                    'string',
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the Amazon Glacier response to your request.

        
        

        - **vaultNotificationConfig** *(dict) --* 

          Returns the notification configuration set on the vault.

          
          

          - **SNSTopic** *(string) --* 

            The Amazon Simple Notification Service (Amazon SNS) topic Amazon Resource Name (ARN).

            
          

          - **Events** *(list) --* 

            A list of one or more events for which Amazon Glacier will send a notification to the specified Amazon SNS topic.

            
            

            - *(string) --* 
        
      
    

    **Examples** 

    The example retrieves the notification-configuration for the vault named my-vault.
    ::

      response = client.get_vault_notifications(
          accountId='-',
          vaultName='my-vault',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'vaultNotificationConfig': {
              'Events': [
                  'InventoryRetrievalCompleted',
                  'ArchiveRetrievalCompleted',
              ],
              'SNSTopic': 'arn:aws:sns:us-west-2:0123456789012:my-vault',
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: initiate_job(**kwargs)

    

    This operation initiates a job of the specified type, which can be a select, an archival retrieval, or a vault retrieval. For more information about using this operation, see the documentation for the underlying REST API `Initiate a Job <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html>`__ . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/InitiateJob>`_    


    **Request Syntax** 
    ::

      response = client.initiate_job(
          vaultName='string',
          jobParameters={
              'Format': 'string',
              'Type': 'string',
              'ArchiveId': 'string',
              'Description': 'string',
              'SNSTopic': 'string',
              'RetrievalByteRange': 'string',
              'Tier': 'string',
              'InventoryRetrievalParameters': {
                  'StartDate': 'string',
                  'EndDate': 'string',
                  'Limit': 'string',
                  'Marker': 'string'
              },
              'SelectParameters': {
                  'InputSerialization': {
                      'csv': {
                          'FileHeaderInfo': 'USE'|'IGNORE'|'NONE',
                          'Comments': 'string',
                          'QuoteEscapeCharacter': 'string',
                          'RecordDelimiter': 'string',
                          'FieldDelimiter': 'string',
                          'QuoteCharacter': 'string'
                      }
                  },
                  'ExpressionType': 'SQL',
                  'Expression': 'string',
                  'OutputSerialization': {
                      'csv': {
                          'QuoteFields': 'ALWAYS'|'ASNEEDED',
                          'QuoteEscapeCharacter': 'string',
                          'RecordDelimiter': 'string',
                          'FieldDelimiter': 'string',
                          'QuoteCharacter': 'string'
                      }
                  }
              },
              'OutputLocation': {
                  'S3': {
                      'BucketName': 'string',
                      'Prefix': 'string',
                      'Encryption': {
                          'EncryptionType': 'aws:kms'|'AES256',
                          'KMSKeyId': 'string',
                          'KMSContext': 'string'
                      },
                      'CannedACL': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control',
                      'AccessControlList': [
                          {
                              'Grantee': {
                                  'Type': 'AmazonCustomerByEmail'|'CanonicalUser'|'Group',
                                  'DisplayName': 'string',
                                  'URI': 'string',
                                  'ID': 'string',
                                  'EmailAddress': 'string'
                              },
                              'Permission': 'FULL_CONTROL'|'WRITE'|'WRITE_ACP'|'READ'|'READ_ACP'
                          },
                      ],
                      'Tagging': {
                          'string': 'string'
                      },
                      'UserMetadata': {
                          'string': 'string'
                      },
                      'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'
                  }
              }
          }
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    :type jobParameters: dict
    :param jobParameters: 

      Provides options for specifying job information.

      

    
      - **Format** *(string) --* 

        When initiating a job to retrieve a vault inventory, you can optionally add this parameter to your request to specify the output format. If you are initiating an inventory job and do not specify a Format field, JSON is the default format. Valid values are "CSV" and "JSON".

        

      
      - **Type** *(string) --* 

        The job type. You can initiate a job to perform a select query on an archive, retrieve an archive, or get an inventory of a vault. Valid values are "select", "archive-retrieval" and "inventory-retrieval".

        

      
      - **ArchiveId** *(string) --* 

        The ID of the archive that you want to retrieve. This field is required only if ``Type`` is set to ``select`` or ``archive-retrieval`` code>. An error occurs if you specify this request parameter for an inventory retrieval job request. 

        

      
      - **Description** *(string) --* 

        The optional description for the job. The description must be less than or equal to 1,024 bytes. The allowable characters are 7-bit ASCII without control codes-specifically, ASCII values 32-126 decimal or 0x20-0x7E hexadecimal.

        

      
      - **SNSTopic** *(string) --* 

        The Amazon SNS topic ARN to which Amazon Glacier sends a notification when the job is completed and the output is ready for you to download. The specified topic publishes the notification to its subscribers. The SNS topic must exist.

        

      
      - **RetrievalByteRange** *(string) --* 

        The byte range to retrieve for an archive retrieval. in the form "*StartByteValue* -*EndByteValue* " If not specified, the whole archive is retrieved. If specified, the byte range must be megabyte (1024*1024) aligned which means that *StartByteValue* must be divisible by 1 MB and *EndByteValue* plus 1 must be divisible by 1 MB or be the end of the archive specified as the archive byte size value minus 1. If RetrievalByteRange is not megabyte aligned, this operation returns a 400 response. 

         

        An error occurs if you specify this field for an inventory retrieval job request.

        

      
      - **Tier** *(string) --* 

        The retrieval option to use for a select or archive retrieval job. Valid values are ``Expedited`` , ``Standard`` , or ``Bulk`` . ``Standard`` is the default.

        

      
      - **InventoryRetrievalParameters** *(dict) --* 

        Input parameters used for range inventory retrieval.

        

      
        - **StartDate** *(string) --* 

          The start of the date range in UTC for vault inventory retrieval that includes archives created on or after this date. This value should be a string in the ISO 8601 date format, for example ``2013-03-20T17:03:43Z`` .

          

        
        - **EndDate** *(string) --* 

          The end of the date range in UTC for vault inventory retrieval that includes archives created before this date. This value should be a string in the ISO 8601 date format, for example ``2013-03-20T17:03:43Z`` .

          

        
        - **Limit** *(string) --* 

          Specifies the maximum number of inventory items returned per vault inventory retrieval request. Valid values are greater than or equal to 1.

          

        
        - **Marker** *(string) --* 

          An opaque string that represents where to continue pagination of the vault inventory retrieval results. You use the marker in a new **InitiateJob** request to obtain additional inventory items. If there are no more inventory items, this value is ``null`` .

          

        
      
      - **SelectParameters** *(dict) --* 

        Contains the parameters that define a job.

        

      
        - **InputSerialization** *(dict) --* 

          Describes the serialization format of the object.

          

        
          - **csv** *(dict) --* 

            Describes the serialization of a CSV-encoded object.

            

          
            - **FileHeaderInfo** *(string) --* 

              Describes the first line of input. Valid values are ``None`` , ``Ignore`` , and ``Use`` .

              

            
            - **Comments** *(string) --* 

              A single character used to indicate that a row should be ignored when the character is present at the start of that row.

              

            
            - **QuoteEscapeCharacter** *(string) --* 

              A single character used for escaping the quotation-mark character inside an already escaped value.

              

            
            - **RecordDelimiter** *(string) --* 

              A value used to separate individual records from each other.

              

            
            - **FieldDelimiter** *(string) --* 

              A value used to separate individual fields from each other within a record.

              

            
            - **QuoteCharacter** *(string) --* 

              A value used as an escape character where the field delimiter is part of the value.

              

            
          
        
        - **ExpressionType** *(string) --* 

          The type of the provided expression, for example ``SQL`` .

          

        
        - **Expression** *(string) --* 

          The expression that is used to select the object.

          

        
        - **OutputSerialization** *(dict) --* 

          Describes how the results of the select job are serialized.

          

        
          - **csv** *(dict) --* 

            Describes the serialization of CSV-encoded query results.

            

          
            - **QuoteFields** *(string) --* 

              A value that indicates whether all output fields should be contained within quotation marks.

              

            
            - **QuoteEscapeCharacter** *(string) --* 

              A single character used for escaping the quotation-mark character inside an already escaped value.

              

            
            - **RecordDelimiter** *(string) --* 

              A value used to separate individual records from each other.

              

            
            - **FieldDelimiter** *(string) --* 

              A value used to separate individual fields from each other within a record.

              

            
            - **QuoteCharacter** *(string) --* 

              A value used as an escape character where the field delimiter is part of the value.

              

            
          
        
      
      - **OutputLocation** *(dict) --* 

        Contains information about the location where the select job results are stored.

        

      
        - **S3** *(dict) --* 

          Describes an S3 location that will receive the results of the restore request.

          

        
          - **BucketName** *(string) --* 

            The name of the bucket where the restore results are stored.

            

          
          - **Prefix** *(string) --* 

            The prefix that is prepended to the restore results for this request.

            

          
          - **Encryption** *(dict) --* 

            Contains information about the encryption used to store the job results in Amazon S3.

            

          
            - **EncryptionType** *(string) --* 

              The server-side encryption algorithm used when storing job results in Amazon S3, for example ``AES256`` or ``aws:kms`` .

              

            
            - **KMSKeyId** *(string) --* 

              The AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or Signature Version 4. 

              

            
            - **KMSContext** *(string) --* 

              Optional. If the encryption type is ``aws:kms`` , you can use this value to specify the encryption context for the restore results.

              

            
          
          - **CannedACL** *(string) --* 

            The canned ACL to apply to the restore results.

            

          
          - **AccessControlList** *(list) --* 

            A list of grants that control access to the staged results.

            

          
            - *(dict) --* 

              Contains information about a grant.

              

            
              - **Grantee** *(dict) --* 

                The grantee.

                

              
                - **Type** *(string) --* **[REQUIRED]** 

                  Type of grantee

                  

                
                - **DisplayName** *(string) --* 

                  Screen name of the grantee.

                  

                
                - **URI** *(string) --* 

                  URI of the grantee group.

                  

                
                - **ID** *(string) --* 

                  The canonical user ID of the grantee.

                  

                
                - **EmailAddress** *(string) --* 

                  Email address of the grantee.

                  

                
              
              - **Permission** *(string) --* 

                Specifies the permission given to the grantee. 

                

              
            
        
          - **Tagging** *(dict) --* 

            The tag-set that is applied to the restore results.

            

          
            - *(string) --* 

            
              - *(string) --* 

              
        
      
          - **UserMetadata** *(dict) --* 

            A map of metadata to store with the restore results in Amazon S3.

            

          
            - *(string) --* 

            
              - *(string) --* 

              
        
      
          - **StorageClass** *(string) --* 

            The storage class used to store the restore results.

            

          
        
      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'location': 'string',
            'jobId': 'string',
            'jobOutputPath': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the Amazon Glacier response to your request.

        
        

        - **location** *(string) --* 

          The relative URI path of the job.

          
        

        - **jobId** *(string) --* 

          The ID of the job.

          
        

        - **jobOutputPath** *(string) --* 

          The path to the location of where the select results are stored.

          
    

    **Examples** 

    The example initiates an inventory-retrieval job for the vault named examplevault.
    ::

      response = client.initiate_job(
          accountId='-',
          jobParameters={
              'Description': 'My inventory job',
              'Format': 'CSV',
              'SNSTopic': 'arn:aws:sns:us-west-2:111111111111:Glacier-InventoryRetrieval-topic-Example',
              'Type': 'inventory-retrieval',
          },
          vaultName='examplevault',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'jobId': ' HkF9p6o7yjhFx-K3CGl6fuSm6VzW9T7esGQfco8nUXVYwS0jlb5gq1JZ55yHgt5vP54ZShjoQzQVVh7vEXAMPLEjobID',
          'location': '/111122223333/vaults/examplevault/jobs/HkF9p6o7yjhFx-K3CGl6fuSm6VzW9T7esGQfco8nUXVYwS0jlb5gq1JZ55yHgt5vP54ZShjoQzQVVh7vEXAMPLEjobID',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: initiate_multipart_upload(**kwargs)

    

    This operation initiates a multipart upload. Amazon Glacier creates a multipart upload resource and returns its ID in the response. The multipart upload ID is used in subsequent requests to upload parts of an archive (see  UploadMultipartPart ).

     

    When you initiate a multipart upload, you specify the part size in number of bytes. The part size must be a megabyte (1024 KB) multiplied by a power of 2-for example, 1048576 (1 MB), 2097152 (2 MB), 4194304 (4 MB), 8388608 (8 MB), and so on. The minimum allowable part size is 1 MB, and the maximum is 4 GB.

     

    Every part you upload to this resource (see  UploadMultipartPart ), except the last one, must have the same size. The last one can be the same size or smaller. For example, suppose you want to upload a 16.2 MB file. If you initiate the multipart upload with a part size of 4 MB, you will upload four parts of 4 MB each and one part of 0.2 MB. 

     

    .. note::

       

      You don't need to know the size of the archive when you start a multipart upload because Amazon Glacier does not require you to specify the overall archive size.

       

     

    After you complete the multipart upload, Amazon Glacier removes the multipart upload resource referenced by the ID. Amazon Glacier also removes the multipart upload resource if you cancel the multipart upload or it may be removed if there is no activity for a period of 24 hours.

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and underlying REST API, see `Uploading Large Archives in Parts (Multipart Upload) <http://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-archive-mpu.html>`__ and `Initiate Multipart Upload <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-initiate-upload.html>`__ in the *Amazon Glacier Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/InitiateMultipartUpload>`_    


    **Request Syntax** 
    ::

      response = client.initiate_multipart_upload(
          vaultName='string',
          archiveDescription='string',
          partSize='string'
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. 

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    :type archiveDescription: string
    :param archiveDescription: 

      The archive description that you are uploading in parts.

       

      The part size must be a megabyte (1024 KB) multiplied by a power of 2, for example 1048576 (1 MB), 2097152 (2 MB), 4194304 (4 MB), 8388608 (8 MB), and so on. The minimum allowable part size is 1 MB, and the maximum is 4 GB (4096 MB).

      

    
    :type partSize: string
    :param partSize: 

      The size of each part except the last, in bytes. The last part can be smaller than this part size.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'location': 'string',
            'uploadId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The Amazon Glacier response to your request.

        
        

        - **location** *(string) --* 

          The relative URI path of the multipart upload ID Amazon Glacier created.

          
        

        - **uploadId** *(string) --* 

          The ID of the multipart upload. This value is also included as part of the location.

          
    

    **Examples** 

    The example initiates a multipart upload to a vault named my-vault with a part size of 1 MiB (1024 x 1024 bytes) per file.
    ::

      response = client.initiate_multipart_upload(
          accountId='-',
          partSize='1048576',
          vaultName='my-vault',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'location': '/111122223333/vaults/my-vault/multipart-uploads/19gaRezEXAMPLES6Ry5YYdqthHOC_kGRCT03L9yetr220UmPtBYKk-OssZtLqyFu7sY1_lR7vgFuJV6NtcV5zpsJ',
          'uploadId': '19gaRezEXAMPLES6Ry5YYdqthHOC_kGRCT03L9yetr220UmPtBYKk-OssZtLqyFu7sY1_lR7vgFuJV6NtcV5zpsJ',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: initiate_vault_lock(**kwargs)

    

    This operation initiates the vault locking process by doing the following:

     

     
    * Installing a vault lock policy on the specified vault. 
     
    * Setting the lock state of vault lock to ``InProgress`` . 
     
    * Returning a lock ID, which is used to complete the vault locking process. 
     

     

    You can set one vault lock policy for each vault and this policy can be up to 20 KB in size. For more information about vault lock policies, see `Amazon Glacier Access Control with Vault Lock Policies <http://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock-policy.html>`__ . 

     

    You must complete the vault locking process within 24 hours after the vault lock enters the ``InProgress`` state. After the 24 hour window ends, the lock ID expires, the vault automatically exits the ``InProgress`` state, and the vault lock policy is removed from the vault. You call  CompleteVaultLock to complete the vault locking process by setting the state of the vault lock to ``Locked`` . 

     

    After a vault lock is in the ``Locked`` state, you cannot initiate a new vault lock for the vault.

     

    You can abort the vault locking process by calling  AbortVaultLock . You can get the state of the vault lock by calling  GetVaultLock . For more information about the vault locking process, `Amazon Glacier Vault Lock <http://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock.html>`__ .

     

    If this operation is called when the vault lock is in the ``InProgress`` state, the operation returns an ``AccessDeniedException`` error. When the vault lock is in the ``InProgress`` state you must call  AbortVaultLock before you can initiate a new vault lock policy. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/InitiateVaultLock>`_    


    **Request Syntax** 
    ::

      response = client.initiate_vault_lock(
          vaultName='string',
          policy={
              'Policy': 'string'
          }
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    :type policy: dict
    :param policy: 

      The vault lock policy as a JSON string, which uses "\" as an escape character.

      

    
      - **Policy** *(string) --* 

        The vault lock policy.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'lockId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the Amazon Glacier response to your request.

        
        

        - **lockId** *(string) --* 

          The lock ID, which is used to complete the vault locking process.

          
    

    **Examples** 

    The example initiates the vault locking process for the vault named my-vault.
    ::

      response = client.initiate_vault_lock(
          accountId='-',
          policy={
              'Policy': '{"Version":"2012-10-17","Statement":[{"Sid":"Define-vault-lock","Effect":"Deny","Principal":{"AWS":"arn:aws:iam::999999999999:root"},"Action":"glacier:DeleteArchive","Resource":"arn:aws:glacier:us-west-2:999999999999:vaults/examplevault","Condition":{"NumericLessThanEquals":{"glacier:ArchiveAgeinDays":"365"}}}]}',
          },
          vaultName='my-vault',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'lockId': 'AE863rKkWZU53SLW5be4DUcW',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_jobs(**kwargs)

    

    This operation lists jobs for a vault, including jobs that are in-progress and jobs that have recently finished. The List Job operation returns a list of these jobs sorted by job initiation time.

     

    .. note::

       

      Amazon Glacier retains recently completed jobs for a period before deleting them; however, it eventually removes completed jobs. The output of completed jobs can be retrieved. Retaining completed jobs for a period of time after they have completed enables you to get a job output in the event you miss the job completion notification or your first attempt to download it fails. For example, suppose you start an archive retrieval job to download an archive. After the job completes, you start to download the archive but encounter a network error. In this scenario, you can retry and download the archive while the job exists.

       

     

    The List Jobs operation supports pagination. You should always check the response ``Marker`` field. If there are no more jobs to list, the ``Marker`` field is set to ``null`` . If there are more jobs to list, the ``Marker`` field is set to a non-null value, which you can use to continue the pagination of the list. To return a list of jobs that begins at a specific job, set the marker request parameter to the ``Marker`` value for that job that you obtained from a previous List Jobs request.

     

    You can set a maximum limit for the number of jobs returned in the response by specifying the ``limit`` parameter in the request. The default limit is 1000. The number of jobs returned might be fewer than the limit, but the number of returned jobs never exceeds the limit.

     

    Additionally, you can filter the jobs list returned by specifying the optional ``statuscode`` parameter or ``completed`` parameter, or both. Using the ``statuscode`` parameter, you can specify to return only jobs that match either the ``InProgress`` , ``Succeeded`` , or ``Failed`` status. Using the ``completed`` parameter, you can specify to return only jobs that were completed (``true`` ) or jobs that were not completed (``false`` ).

     

    For more information about using this operation, see the documentation for the underlying REST API `List Jobs <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-jobs-get.html>`__ . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListJobs>`_    


    **Request Syntax** 
    ::

      response = client.list_jobs(
          vaultName='string',
          limit='string',
          marker='string',
          statuscode='string',
          completed='string'
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. 

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    :type limit: string
    :param limit: 

      The maximum number of jobs to be returned. The default limit is 1000. The number of jobs returned might be fewer than the specified limit, but the number of returned jobs never exceeds the limit.

      

    
    :type marker: string
    :param marker: 

      An opaque string used for pagination. This value specifies the job at which the listing of jobs should begin. Get the marker value from a previous List Jobs response. You only need to include the marker if you are continuing the pagination of results started in a previous List Jobs request.

      

    
    :type statuscode: string
    :param statuscode: 

      The type of job status to return. You can specify the following values: ``InProgress`` , ``Succeeded`` , or ``Failed`` .

      

    
    :type completed: string
    :param completed: 

      The state of the jobs to return. You can specify ``true`` or ``false`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'JobList': [
                {
                    'JobId': 'string',
                    'JobDescription': 'string',
                    'Action': 'ArchiveRetrieval'|'InventoryRetrieval'|'Select',
                    'ArchiveId': 'string',
                    'VaultARN': 'string',
                    'CreationDate': 'string',
                    'Completed': True|False,
                    'StatusCode': 'InProgress'|'Succeeded'|'Failed',
                    'StatusMessage': 'string',
                    'ArchiveSizeInBytes': 123,
                    'InventorySizeInBytes': 123,
                    'SNSTopic': 'string',
                    'CompletionDate': 'string',
                    'SHA256TreeHash': 'string',
                    'ArchiveSHA256TreeHash': 'string',
                    'RetrievalByteRange': 'string',
                    'Tier': 'string',
                    'InventoryRetrievalParameters': {
                        'Format': 'string',
                        'StartDate': 'string',
                        'EndDate': 'string',
                        'Limit': 'string',
                        'Marker': 'string'
                    },
                    'JobOutputPath': 'string',
                    'SelectParameters': {
                        'InputSerialization': {
                            'csv': {
                                'FileHeaderInfo': 'USE'|'IGNORE'|'NONE',
                                'Comments': 'string',
                                'QuoteEscapeCharacter': 'string',
                                'RecordDelimiter': 'string',
                                'FieldDelimiter': 'string',
                                'QuoteCharacter': 'string'
                            }
                        },
                        'ExpressionType': 'SQL',
                        'Expression': 'string',
                        'OutputSerialization': {
                            'csv': {
                                'QuoteFields': 'ALWAYS'|'ASNEEDED',
                                'QuoteEscapeCharacter': 'string',
                                'RecordDelimiter': 'string',
                                'FieldDelimiter': 'string',
                                'QuoteCharacter': 'string'
                            }
                        }
                    },
                    'OutputLocation': {
                        'S3': {
                            'BucketName': 'string',
                            'Prefix': 'string',
                            'Encryption': {
                                'EncryptionType': 'aws:kms'|'AES256',
                                'KMSKeyId': 'string',
                                'KMSContext': 'string'
                            },
                            'CannedACL': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control',
                            'AccessControlList': [
                                {
                                    'Grantee': {
                                        'Type': 'AmazonCustomerByEmail'|'CanonicalUser'|'Group',
                                        'DisplayName': 'string',
                                        'URI': 'string',
                                        'ID': 'string',
                                        'EmailAddress': 'string'
                                    },
                                    'Permission': 'FULL_CONTROL'|'WRITE'|'WRITE_ACP'|'READ'|'READ_ACP'
                                },
                            ],
                            'Tagging': {
                                'string': 'string'
                            },
                            'UserMetadata': {
                                'string': 'string'
                            },
                            'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'
                        }
                    }
                },
            ],
            'Marker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the Amazon Glacier response to your request.

        
        

        - **JobList** *(list) --* 

          A list of job objects. Each job object contains metadata describing the job.

          
          

          - *(dict) --* 

            Contains the description of an Amazon Glacier job.

            
            

            - **JobId** *(string) --* 

              An opaque string that identifies an Amazon Glacier job.

              
            

            - **JobDescription** *(string) --* 

              The job description provided when initiating the job.

              
            

            - **Action** *(string) --* 

              The job type. This value is either ``ArchiveRetrieval`` , ``InventoryRetrieval`` , or ``Select`` . 

              
            

            - **ArchiveId** *(string) --* 

              The archive ID requested for a select job or archive retrieval. Otherwise, this field is null.

              
            

            - **VaultARN** *(string) --* 

              The Amazon Resource Name (ARN) of the vault from which an archive retrieval was requested.

              
            

            - **CreationDate** *(string) --* 

              The UTC date when the job was created. This value is a string representation of ISO 8601 date format, for example ``"2012-03-20T17:03:43.221Z"`` .

              
            

            - **Completed** *(boolean) --* 

              The job status. When a job is completed, you get the job's output using Get Job Output (GET output).

              
            

            - **StatusCode** *(string) --* 

              The status code can be ``InProgress`` , ``Succeeded`` , or ``Failed`` , and indicates the status of the job.

              
            

            - **StatusMessage** *(string) --* 

              A friendly message that describes the job status.

              
            

            - **ArchiveSizeInBytes** *(integer) --* 

              For an archive retrieval job, this value is the size in bytes of the archive being requested for download. For an inventory retrieval or select job, this value is null.

              
            

            - **InventorySizeInBytes** *(integer) --* 

              For an inventory retrieval job, this value is the size in bytes of the inventory requested for download. For an archive retrieval or select job, this value is null.

              
            

            - **SNSTopic** *(string) --* 

              An Amazon SNS topic that receives notification.

              
            

            - **CompletionDate** *(string) --* 

              The UTC time that the job request completed. While the job is in progress, the value is null.

              
            

            - **SHA256TreeHash** *(string) --* 

              For an archive retrieval job, this value is the checksum of the archive. Otherwise, this value is null.

               

              The SHA256 tree hash value for the requested range of an archive. If the **InitiateJob** request for an archive specified a tree-hash aligned range, then this field returns a value.

               

              If the whole archive is retrieved, this value is the same as the ArchiveSHA256TreeHash value.

               

              This field is null for the following:

               

               
              * Archive retrieval jobs that specify a range that is not tree-hash aligned 
               

               

               
              * Archival jobs that specify a range that is equal to the whole archive, when the job status is ``InProgress``   
               

               

               
              * Inventory jobs 
               
              * Select jobs 
               

              
            

            - **ArchiveSHA256TreeHash** *(string) --* 

              The SHA256 tree hash of the entire archive for an archive retrieval. For inventory retrieval or select jobs, this field is null.

              
            

            - **RetrievalByteRange** *(string) --* 

              The retrieved byte range for archive retrieval jobs in the form *StartByteValue* -*EndByteValue* . If no range was specified in the archive retrieval, then the whole archive is retrieved. In this case, *StartByteValue* equals 0 and *EndByteValue* equals the size of the archive minus 1. For inventory retrieval or select jobs, this field is null. 

              
            

            - **Tier** *(string) --* 

              The retrieval option to use for the archive retrieval. Valid values are ``Expedited`` , ``Standard`` , or ``Bulk`` . ``Standard`` is the default.

              
            

            - **InventoryRetrievalParameters** *(dict) --* 

              Parameters used for range inventory retrieval.

              
              

              - **Format** *(string) --* 

                The output format for the vault inventory list, which is set by the **InitiateJob** request when initiating a job to retrieve a vault inventory. Valid values are ``CSV`` and ``JSON`` .

                
              

              - **StartDate** *(string) --* 

                The start of the date range in Universal Coordinated Time (UTC) for vault inventory retrieval that includes archives created on or after this date. This value should be a string in the ISO 8601 date format, for example ``2013-03-20T17:03:43Z`` .

                
              

              - **EndDate** *(string) --* 

                The end of the date range in UTC for vault inventory retrieval that includes archives created before this date. This value should be a string in the ISO 8601 date format, for example ``2013-03-20T17:03:43Z`` .

                
              

              - **Limit** *(string) --* 

                The maximum number of inventory items returned per vault inventory retrieval request. This limit is set when initiating the job with the a **InitiateJob** request. 

                
              

              - **Marker** *(string) --* 

                An opaque string that represents where to continue pagination of the vault inventory retrieval results. You use the marker in a new **InitiateJob** request to obtain additional inventory items. If there are no more inventory items, this value is ``null`` . For more information, see `Range Inventory Retrieval <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html#api-initiate-job-post-vault-inventory-list-filtering>`__ .

                
          
            

            - **JobOutputPath** *(string) --* 

              Contains the job output location.

              
            

            - **SelectParameters** *(dict) --* 

              Contains the parameters that define a select job.

              
              

              - **InputSerialization** *(dict) --* 

                Describes the serialization format of the object.

                
                

                - **csv** *(dict) --* 

                  Describes the serialization of a CSV-encoded object.

                  
                  

                  - **FileHeaderInfo** *(string) --* 

                    Describes the first line of input. Valid values are ``None`` , ``Ignore`` , and ``Use`` .

                    
                  

                  - **Comments** *(string) --* 

                    A single character used to indicate that a row should be ignored when the character is present at the start of that row.

                    
                  

                  - **QuoteEscapeCharacter** *(string) --* 

                    A single character used for escaping the quotation-mark character inside an already escaped value.

                    
                  

                  - **RecordDelimiter** *(string) --* 

                    A value used to separate individual records from each other.

                    
                  

                  - **FieldDelimiter** *(string) --* 

                    A value used to separate individual fields from each other within a record.

                    
                  

                  - **QuoteCharacter** *(string) --* 

                    A value used as an escape character where the field delimiter is part of the value.

                    
              
            
              

              - **ExpressionType** *(string) --* 

                The type of the provided expression, for example ``SQL`` .

                
              

              - **Expression** *(string) --* 

                The expression that is used to select the object.

                
              

              - **OutputSerialization** *(dict) --* 

                Describes how the results of the select job are serialized.

                
                

                - **csv** *(dict) --* 

                  Describes the serialization of CSV-encoded query results.

                  
                  

                  - **QuoteFields** *(string) --* 

                    A value that indicates whether all output fields should be contained within quotation marks.

                    
                  

                  - **QuoteEscapeCharacter** *(string) --* 

                    A single character used for escaping the quotation-mark character inside an already escaped value.

                    
                  

                  - **RecordDelimiter** *(string) --* 

                    A value used to separate individual records from each other.

                    
                  

                  - **FieldDelimiter** *(string) --* 

                    A value used to separate individual fields from each other within a record.

                    
                  

                  - **QuoteCharacter** *(string) --* 

                    A value used as an escape character where the field delimiter is part of the value.

                    
              
            
          
            

            - **OutputLocation** *(dict) --* 

              Contains the location where the data from the select job is stored.

              
              

              - **S3** *(dict) --* 

                Describes an S3 location that will receive the results of the restore request.

                
                

                - **BucketName** *(string) --* 

                  The name of the bucket where the restore results are stored.

                  
                

                - **Prefix** *(string) --* 

                  The prefix that is prepended to the restore results for this request.

                  
                

                - **Encryption** *(dict) --* 

                  Contains information about the encryption used to store the job results in Amazon S3.

                  
                  

                  - **EncryptionType** *(string) --* 

                    The server-side encryption algorithm used when storing job results in Amazon S3, for example ``AES256`` or ``aws:kms`` .

                    
                  

                  - **KMSKeyId** *(string) --* 

                    The AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or Signature Version 4. 

                    
                  

                  - **KMSContext** *(string) --* 

                    Optional. If the encryption type is ``aws:kms`` , you can use this value to specify the encryption context for the restore results.

                    
              
                

                - **CannedACL** *(string) --* 

                  The canned ACL to apply to the restore results.

                  
                

                - **AccessControlList** *(list) --* 

                  A list of grants that control access to the staged results.

                  
                  

                  - *(dict) --* 

                    Contains information about a grant.

                    
                    

                    - **Grantee** *(dict) --* 

                      The grantee.

                      
                      

                      - **Type** *(string) --* 

                        Type of grantee

                        
                      

                      - **DisplayName** *(string) --* 

                        Screen name of the grantee.

                        
                      

                      - **URI** *(string) --* 

                        URI of the grantee group.

                        
                      

                      - **ID** *(string) --* 

                        The canonical user ID of the grantee.

                        
                      

                      - **EmailAddress** *(string) --* 

                        Email address of the grantee.

                        
                  
                    

                    - **Permission** *(string) --* 

                      Specifies the permission given to the grantee. 

                      
                
              
                

                - **Tagging** *(dict) --* 

                  The tag-set that is applied to the restore results.

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
                

                - **UserMetadata** *(dict) --* 

                  A map of metadata to store with the restore results in Amazon S3.

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
                

                - **StorageClass** *(string) --* 

                  The storage class used to store the restore results.

                  
            
          
        
      
        

        - **Marker** *(string) --* 

          An opaque string used for pagination that specifies the job at which the listing of jobs should begin. You get the ``marker`` value from a previous List Jobs response. You only need to include the marker if you are continuing the pagination of the results started in a previous List Jobs request. 

          
    

    **Examples** 

    The example lists jobs for the vault named my-vault.
    ::

      response = client.list_jobs(
          accountId='-',
          vaultName='my-vault',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'JobList': [
              {
                  'Action': 'ArchiveRetrieval',
                  'ArchiveId': 'kKB7ymWJVpPSwhGP6ycSOAekp9ZYe_--zM_mw6k76ZFGEIWQX-ybtRDvc2VkPSDtfKmQrj0IRQLSGsNuDp-AJVlu2ccmDSyDUmZwKbwbpAdGATGDiB3hHO0bjbGehXTcApVud_wyDw',
                  'ArchiveSHA256TreeHash': '9628195fcdbcbbe76cdde932d4646fa7de5f219fb39823836d81f0cc0e18aa67',
                  'ArchiveSizeInBytes': 3145728,
                  'Completed': False,
                  'CreationDate': '2015-07-17T21:16:13.840Z',
                  'JobDescription': 'Retrieve archive on 2015-07-17',
                  'JobId': 'l7IL5-EkXyEY9Ws95fClzIbk2O5uLYaFdAYOi-azsX_Z8V6NH4yERHzars8wTKYQMX6nBDI9cMNHzyZJO59-8N9aHWav',
                  'RetrievalByteRange': '0-3145727',
                  'SHA256TreeHash': '9628195fcdbcbbe76cdde932d4646fa7de5f219fb39823836d81f0cc0e18aa67',
                  'SNSTopic': 'arn:aws:sns:us-west-2:0123456789012:my-vault',
                  'StatusCode': 'InProgress',
                  'VaultARN': 'arn:aws:glacier:us-west-2:0123456789012:vaults/my-vault',
              },
              {
                  'Action': 'InventoryRetrieval',
                  'Completed': False,
                  'CreationDate': '2015-07-17T20:23:41.616Z',
                  'InventoryRetrievalParameters': {
                      'Format': 'JSON',
                  },
                  'JobId': 'zbxcm3Z_3z5UkoroF7SuZKrxgGoDc3RloGduS7Eg-RO47Yc6FxsdGBgf_Q2DK5Ejh18CnTS5XW4_XqlNHS61dsO4CnMW',
                  'StatusCode': 'InProgress',
                  'VaultARN': 'arn:aws:glacier:us-west-2:0123456789012:vaults/my-vault',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_multipart_uploads(**kwargs)

    

    This operation lists in-progress multipart uploads for the specified vault. An in-progress multipart upload is a multipart upload that has been initiated by an  InitiateMultipartUpload request, but has not yet been completed or aborted. The list returned in the List Multipart Upload response has no guaranteed order. 

     

    The List Multipart Uploads operation supports pagination. By default, this operation returns up to 1,000 multipart uploads in the response. You should always check the response for a ``marker`` at which to continue the list; if there are no more items the ``marker`` is ``null`` . To return a list of multipart uploads that begins at a specific upload, set the ``marker`` request parameter to the value you obtained from a previous List Multipart Upload request. You can also limit the number of uploads returned in the response by specifying the ``limit`` parameter in the request.

     

    Note the difference between this operation and listing parts ( ListParts ). The List Multipart Uploads operation lists all multipart uploads for a vault and does not require a multipart upload ID. The List Parts operation requires a multipart upload ID since parts are associated with a single upload.

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and the underlying REST API, see `Working with Archives in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-archives.html>`__ and `List Multipart Uploads <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-list-uploads.html>`__ in the *Amazon Glacier Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListMultipartUploads>`_    


    **Request Syntax** 
    ::

      response = client.list_multipart_uploads(
          vaultName='string',
          marker='string',
          limit='string'
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. 

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    :type marker: string
    :param marker: 

      An opaque string used for pagination. This value specifies the upload at which the listing of uploads should begin. Get the marker value from a previous List Uploads response. You need only include the marker if you are continuing the pagination of results started in a previous List Uploads request.

      

    
    :type limit: string
    :param limit: 

      Specifies the maximum number of uploads returned in the response body. If this value is not specified, the List Uploads operation returns up to 1,000 uploads.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UploadsList': [
                {
                    'MultipartUploadId': 'string',
                    'VaultARN': 'string',
                    'ArchiveDescription': 'string',
                    'PartSizeInBytes': 123,
                    'CreationDate': 'string'
                },
            ],
            'Marker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the Amazon Glacier response to your request.

        
        

        - **UploadsList** *(list) --* 

          A list of in-progress multipart uploads.

          
          

          - *(dict) --* 

            A list of in-progress multipart uploads for a vault.

            
            

            - **MultipartUploadId** *(string) --* 

              The ID of a multipart upload.

              
            

            - **VaultARN** *(string) --* 

              The Amazon Resource Name (ARN) of the vault that contains the archive.

              
            

            - **ArchiveDescription** *(string) --* 

              The description of the archive that was specified in the Initiate Multipart Upload request.

              
            

            - **PartSizeInBytes** *(integer) --* 

              The part size, in bytes, specified in the Initiate Multipart Upload request. This is the size of all the parts in the upload except the last part, which may be smaller than this size.

              
            

            - **CreationDate** *(string) --* 

              The UTC time at which the multipart upload was initiated.

              
        
      
        

        - **Marker** *(string) --* 

          An opaque string that represents where to continue pagination of the results. You use the marker in a new List Multipart Uploads request to obtain more uploads in the list. If there are no more uploads, this value is ``null`` .

          
    

    **Examples** 

    The example lists all the in-progress multipart uploads for the vault named examplevault.
    ::

      response = client.list_multipart_uploads(
          accountId='-',
          vaultName='examplevault',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Marker': 'null',
          'UploadsList': [
              {
                  'ArchiveDescription': 'archive 1',
                  'CreationDate': '2012-03-19T23:20:59.130Z',
                  'MultipartUploadId': 'xsQdFIRsfJr20CW2AbZBKpRZAFTZSJIMtL2hYf8mvp8dM0m4RUzlaqoEye6g3h3ecqB_zqwB7zLDMeSWhwo65re4C4Ev',
                  'PartSizeInBytes': 4194304,
                  'VaultARN': 'arn:aws:glacier:us-west-2:012345678901:vaults/examplevault',
              },
              {
                  'ArchiveDescription': 'archive 2',
                  'CreationDate': '2012-04-01T15:00:00.000Z',
                  'MultipartUploadId': 'nPyGOnyFcx67qqX7E-0tSGiRi88hHMOwOxR-_jNyM6RjVMFfV29lFqZ3rNsSaWBugg6OP92pRtufeHdQH7ClIpSF6uJc',
                  'PartSizeInBytes': 4194304,
                  'VaultARN': 'arn:aws:glacier:us-west-2:012345678901:vaults/examplevault',
              },
              {
                  'ArchiveDescription': 'archive 3',
                  'CreationDate': '2012-03-20T17:03:43.221Z',
                  'MultipartUploadId': 'qt-RBst_7yO8gVIonIBsAxr2t-db0pE4s8MNeGjKjGdNpuU-cdSAcqG62guwV9r5jh5mLyFPzFEitTpNE7iQfHiu1XoV',
                  'PartSizeInBytes': 4194304,
                  'VaultARN': 'arn:aws:glacier:us-west-2:012345678901:vaults/examplevault',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_parts(**kwargs)

    

    This operation lists the parts of an archive that have been uploaded in a specific multipart upload. You can make this request at any time during an in-progress multipart upload before you complete the upload (see  CompleteMultipartUpload . List Parts returns an error for completed uploads. The list returned in the List Parts response is sorted by part range. 

     

    The List Parts operation supports pagination. By default, this operation returns up to 1,000 uploaded parts in the response. You should always check the response for a ``marker`` at which to continue the list; if there are no more items the ``marker`` is ``null`` . To return a list of parts that begins at a specific part, set the ``marker`` request parameter to the value you obtained from a previous List Parts request. You can also limit the number of parts returned in the response by specifying the ``limit`` parameter in the request. 

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and the underlying REST API, see `Working with Archives in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-archives.html>`__ and `List Parts <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-list-parts.html>`__ in the *Amazon Glacier Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListParts>`_    


    **Request Syntax** 
    ::

      response = client.list_parts(
          vaultName='string',
          uploadId='string',
          marker='string',
          limit='string'
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. 

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    :type uploadId: string
    :param uploadId: **[REQUIRED]** 

      The upload ID of the multipart upload.

      

    
    :type marker: string
    :param marker: 

      An opaque string used for pagination. This value specifies the part at which the listing of parts should begin. Get the marker value from the response of a previous List Parts response. You need only include the marker if you are continuing the pagination of results started in a previous List Parts request.

      

    
    :type limit: string
    :param limit: 

      The maximum number of parts to be returned. The default limit is 1000. The number of parts returned might be fewer than the specified limit, but the number of returned parts never exceeds the limit.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'MultipartUploadId': 'string',
            'VaultARN': 'string',
            'ArchiveDescription': 'string',
            'PartSizeInBytes': 123,
            'CreationDate': 'string',
            'Parts': [
                {
                    'RangeInBytes': 'string',
                    'SHA256TreeHash': 'string'
                },
            ],
            'Marker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the Amazon Glacier response to your request.

        
        

        - **MultipartUploadId** *(string) --* 

          The ID of the upload to which the parts are associated.

          
        

        - **VaultARN** *(string) --* 

          The Amazon Resource Name (ARN) of the vault to which the multipart upload was initiated.

          
        

        - **ArchiveDescription** *(string) --* 

          The description of the archive that was specified in the Initiate Multipart Upload request.

          
        

        - **PartSizeInBytes** *(integer) --* 

          The part size in bytes. This is the same value that you specified in the Initiate Multipart Upload request.

          
        

        - **CreationDate** *(string) --* 

          The UTC time at which the multipart upload was initiated.

          
        

        - **Parts** *(list) --* 

          A list of the part sizes of the multipart upload. Each object in the array contains a ``RangeBytes`` and ``sha256-tree-hash`` name/value pair.

          
          

          - *(dict) --* 

            A list of the part sizes of the multipart upload.

            
            

            - **RangeInBytes** *(string) --* 

              The byte range of a part, inclusive of the upper value of the range.

              
            

            - **SHA256TreeHash** *(string) --* 

              The SHA256 tree hash value that Amazon Glacier calculated for the part. This field is never ``null`` .

              
        
      
        

        - **Marker** *(string) --* 

          An opaque string that represents where to continue pagination of the results. You use the marker in a new List Parts request to obtain more jobs in the list. If there are no more parts, this value is ``null`` .

          
    

    **Examples** 

    The example lists all the parts of a multipart upload.
    ::

      response = client.list_parts(
          accountId='-',
          uploadId='OW2fM5iVylEpFEMM9_HpKowRapC3vn5sSL39_396UW9zLFUWVrnRHaPjUJddQ5OxSHVXjYtrN47NBZ-khxOjyEXAMPLE',
          vaultName='examplevault',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ArchiveDescription': 'archive description',
          'CreationDate': '2012-03-20T17:03:43.221Z',
          'Marker': 'null',
          'MultipartUploadId': 'OW2fM5iVylEpFEMM9_HpKowRapC3vn5sSL39_396UW9zLFUWVrnRHaPjUJddQ5OxSHVXjYtrN47NBZ-khxOjyEXAMPLE',
          'PartSizeInBytes': 4194304,
          'Parts': [
              {
                  'RangeInBytes': '0-4194303',
                  'SHA256TreeHash': '01d34dabf7be316472c93b1ef80721f5d4',
              },
              {
                  'RangeInBytes': '4194304-8388607',
                  'SHA256TreeHash': '0195875365afda349fc21c84c099987164',
              },
          ],
          'VaultARN': 'arn:aws:glacier:us-west-2:012345678901:vaults/demo1-vault',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_provisioned_capacity(**kwargs)

    

    This operation lists the provisioned capacity units for the specified AWS account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListProvisionedCapacity>`_    


    **Request Syntax** 
    ::

      response = client.list_provisioned_capacity(
          
      )
    :type accountId: string
    :param accountId: 

      The AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '-' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, don't include any hyphens ('-') in the ID. 

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ProvisionedCapacityList': [
                {
                    'CapacityId': 'string',
                    'StartDate': 'string',
                    'ExpirationDate': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ProvisionedCapacityList** *(list) --* 

          The response body contains the following JSON fields.

          
          

          - *(dict) --* 

            The definition for a provisioned capacity unit.

            
            

            - **CapacityId** *(string) --* 

              The ID that identifies the provisioned capacity unit.

              
            

            - **StartDate** *(string) --* 

              The date that the provisioned capacity unit was purchased, in Universal Coordinated Time (UTC).

              
            

            - **ExpirationDate** *(string) --* 

              The date that the provisioned capacity unit expires, in Universal Coordinated Time (UTC).

              
        
      
    

    **Examples** 

    The example lists the provisioned capacity units for an account.
    ::

      response = client.list_provisioned_capacity(
          accountId='-',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ProvisionedCapacityList': [
              {
                  'CapacityId': 'zSaq7NzHFQDANTfQkDen4V7z',
                  'ExpirationDate': '2016-12-12T00:00:00.000Z',
                  'StartDate': '2016-11-11T20:11:51.095Z',
              },
              {
                  'CapacityId': 'yXaq7NzHFQNADTfQkDen4V7z',
                  'ExpirationDate': '2017-01-15T00:00:00.000Z',
                  'StartDate': '2016-12-13T20:11:51.095Z',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_tags_for_vault(**kwargs)

    

    This operation lists all the tags attached to a vault. The operation returns an empty map if there are no tags. For more information about tags, see `Tagging Amazon Glacier Resources <http://docs.aws.amazon.com/amazonglacier/latest/dev/tagging.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListTagsForVault>`_    


    **Request Syntax** 
    ::

      response = client.list_tags_for_vault(
          vaultName='string'
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Tags': {
                'string': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the Amazon Glacier response to your request.

        
        

        - **Tags** *(dict) --* 

          The tags attached to the vault. Each tag is composed of a key and a value.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
    

    **Examples** 

    The example lists all the tags attached to the vault examplevault.
    ::

      response = client.list_tags_for_vault(
          accountId='-',
          vaultName='examplevault',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Tags': {
              'date': 'july2015',
              'id': '1234',
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_vaults(**kwargs)

    

    This operation lists all vaults owned by the calling user's account. The list returned in the response is ASCII-sorted by vault name.

     

    By default, this operation returns up to 1,000 items. If there are more vaults to list, the response ``marker`` field contains the vault Amazon Resource Name (ARN) at which to continue the list with a new List Vaults request; otherwise, the ``marker`` field is ``null`` . To return a list of vaults that begins at a specific vault, set the ``marker`` request parameter to the vault ARN you obtained from a previous List Vaults request. You can also limit the number of vaults returned in the response by specifying the ``limit`` parameter in the request. 

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and underlying REST API, see `Retrieving Vault Metadata in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/retrieving-vault-info.html>`__ and `List Vaults <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-vaults-get.html>`__ in the *Amazon Glacier Developer Guide* . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListVaults>`_    


    **Request Syntax** 
    ::

      response = client.list_vaults(
          marker='string',
          limit='string'
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type marker: string
    :param marker: 

      A string used for pagination. The marker specifies the vault ARN after which the listing of vaults should begin.

      

    
    :type limit: string
    :param limit: 

      The maximum number of vaults to be returned. The default limit is 1000. The number of vaults returned might be fewer than the specified limit, but the number of returned vaults never exceeds the limit.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'VaultList': [
                {
                    'VaultARN': 'string',
                    'VaultName': 'string',
                    'CreationDate': 'string',
                    'LastInventoryDate': 'string',
                    'NumberOfArchives': 123,
                    'SizeInBytes': 123
                },
            ],
            'Marker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the Amazon Glacier response to your request.

        
        

        - **VaultList** *(list) --* 

          List of vaults.

          
          

          - *(dict) --* 

            Contains the Amazon Glacier response to your request.

            
            

            - **VaultARN** *(string) --* 

              The Amazon Resource Name (ARN) of the vault.

              
            

            - **VaultName** *(string) --* 

              The name of the vault.

              
            

            - **CreationDate** *(string) --* 

              The Universal Coordinated Time (UTC) date when the vault was created. This value should be a string in the ISO 8601 date format, for example ``2012-03-20T17:03:43.221Z`` .

              
            

            - **LastInventoryDate** *(string) --* 

              The Universal Coordinated Time (UTC) date when Amazon Glacier completed the last vault inventory. This value should be a string in the ISO 8601 date format, for example ``2012-03-20T17:03:43.221Z`` .

              
            

            - **NumberOfArchives** *(integer) --* 

              The number of archives in the vault as of the last inventory date. This field will return ``null`` if an inventory has not yet run on the vault, for example if you just created the vault.

              
            

            - **SizeInBytes** *(integer) --* 

              Total size, in bytes, of the archives in the vault as of the last inventory date. This field will return null if an inventory has not yet run on the vault, for example if you just created the vault.

              
        
      
        

        - **Marker** *(string) --* 

          The vault ARN at which to continue pagination of the results. You use the marker in another List Vaults request to obtain more vaults in the list.

          
    

    **Examples** 

    The example lists all vaults owned by the specified AWS account.
    ::

      response = client.list_vaults(
          accountId='-',
          limit='',
          marker='',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'VaultList': [
              {
                  'CreationDate': '2015-04-06T21:23:45.708Z',
                  'LastInventoryDate': '2015-04-07T00:26:19.028Z',
                  'NumberOfArchives': 1,
                  'SizeInBytes': 3178496,
                  'VaultARN': 'arn:aws:glacier:us-west-2:0123456789012:vaults/my-vault',
                  'VaultName': 'my-vault',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: purchase_provisioned_capacity(**kwargs)

    

    This operation purchases a provisioned capacity unit for an AWS account. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/PurchaseProvisionedCapacity>`_    


    **Request Syntax** 
    ::

      response = client.purchase_provisioned_capacity(
          
      )
    :type accountId: string
    :param accountId: 

      The AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '-' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, don't include any hyphens ('-') in the ID. 

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'capacityId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **capacityId** *(string) --* 

          The ID that identifies the provisioned capacity unit.

          
    

    **Examples** 

    The example purchases provisioned capacity unit for an AWS account.
    ::

      response = client.purchase_provisioned_capacity(
          accountId='-',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'capacityId': 'zSaq7NzHFQDANTfQkDen4V7z',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: remove_tags_from_vault(**kwargs)

    

    This operation removes one or more tags from the set of tags attached to a vault. For more information about tags, see `Tagging Amazon Glacier Resources <http://docs.aws.amazon.com/amazonglacier/latest/dev/tagging.html>`__ . This operation is idempotent. The operation will be successful, even if there are no tags attached to the vault. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/RemoveTagsFromVault>`_    


    **Request Syntax** 
    ::

      response = client.remove_tags_from_vault(
          vaultName='string',
          TagKeys=[
              'string',
          ]
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    :type TagKeys: list
    :param TagKeys: 

      A list of tag keys. Each corresponding tag is removed from the vault.

      

    
      - *(string) --* 

      
  
    
    :returns: None

    **Examples** 

    The example removes two tags from the vault named examplevault.
    ::

      response = client.remove_tags_from_vault(
          TagKeys=[
              'examplekey1',
              'examplekey2',
          ],
          accountId='-',
          vaultName='examplevault',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: set_data_retrieval_policy(**kwargs)

    

    This operation sets and then enacts a data retrieval policy in the region specified in the PUT request. You can set one policy per region for an AWS account. The policy is enacted within a few minutes of a successful PUT operation.

     

    The set policy operation does not affect retrieval jobs that were in progress before the policy was enacted. For more information about data retrieval policies, see `Amazon Glacier Data Retrieval Policies <http://docs.aws.amazon.com/amazonglacier/latest/dev/data-retrieval-policy.html>`__ . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/SetDataRetrievalPolicy>`_    


    **Request Syntax** 
    ::

      response = client.set_data_retrieval_policy(
          Policy={
              'Rules': [
                  {
                      'Strategy': 'string',
                      'BytesPerHour': 123
                  },
              ]
          }
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type Policy: dict
    :param Policy: 

      The data retrieval policy in JSON format.

      

    
      - **Rules** *(list) --* 

        The policy rule. Although this is a list type, currently there must be only one rule, which contains a Strategy field and optionally a BytesPerHour field.

        

      
        - *(dict) --* 

          Data retrieval policy rule.

          

        
          - **Strategy** *(string) --* 

            The type of data retrieval policy to set.

             

            Valid values: BytesPerHour|FreeTier|None

            

          
          - **BytesPerHour** *(integer) --* 

            The maximum number of bytes that can be retrieved in an hour.

             

            This field is required only if the value of the Strategy field is ``BytesPerHour`` . Your PUT operation will be rejected if the Strategy field is not set to ``BytesPerHour`` and you set this field.

            

          
        
    
    
    
    :returns: None

    **Examples** 

    The example sets and then enacts a data retrieval policy.
    ::

      response = client.set_data_retrieval_policy(
          Policy={
              'Rules': [
                  {
                      'BytesPerHour': 10737418240,
                      'Strategy': 'BytesPerHour',
                  },
              ],
          },
          accountId='-',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: set_vault_access_policy(**kwargs)

    

    This operation configures an access policy for a vault and will overwrite an existing policy. To configure a vault access policy, send a PUT request to the ``access-policy`` subresource of the vault. An access policy is specific to a vault and is also called a vault subresource. You can set one access policy per vault and the policy can be up to 20 KB in size. For more information about vault access policies, see `Amazon Glacier Access Control with Vault Access Policies <http://docs.aws.amazon.com/amazonglacier/latest/dev/vault-access-policy.html>`__ . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/SetVaultAccessPolicy>`_    


    **Request Syntax** 
    ::

      response = client.set_vault_access_policy(
          vaultName='string',
          policy={
              'Policy': 'string'
          }
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    :type policy: dict
    :param policy: 

      The vault access policy as a JSON string.

      

    
      - **Policy** *(string) --* 

        The vault access policy.

        

      
    
    
    :returns: None

    **Examples** 

    The example configures an access policy for the vault named examplevault.
    ::

      response = client.set_vault_access_policy(
          accountId='-',
          policy={
              'Policy': '{"Version":"2012-10-17","Statement":[{"Sid":"Define-owner-access-rights","Effect":"Allow","Principal":{"AWS":"arn:aws:iam::999999999999:root"},"Action":"glacier:DeleteArchive","Resource":"arn:aws:glacier:us-west-2:999999999999:vaults/examplevault"}]}',
          },
          vaultName='examplevault',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: set_vault_notifications(**kwargs)

    

    This operation configures notifications that will be sent when specific events happen to a vault. By default, you don't get any notifications.

     

    To configure vault notifications, send a PUT request to the ``notification-configuration`` subresource of the vault. The request should include a JSON document that provides an Amazon SNS topic and specific events for which you want Amazon Glacier to send notifications to the topic.

     

    Amazon SNS topics must grant permission to the vault to be allowed to publish notifications to the topic. You can configure a vault to publish a notification for the following vault events:

     

     
    * **ArchiveRetrievalCompleted** This event occurs when a job that was initiated for an archive retrieval is completed ( InitiateJob ). The status of the completed job can be "Succeeded" or "Failed". The notification sent to the SNS topic is the same output as returned from  DescribeJob .  
     
    * **InventoryRetrievalCompleted** This event occurs when a job that was initiated for an inventory retrieval is completed ( InitiateJob ). The status of the completed job can be "Succeeded" or "Failed". The notification sent to the SNS topic is the same output as returned from  DescribeJob .  
     

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and underlying REST API, see `Configuring Vault Notifications in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/configuring-notifications.html>`__ and `Set Vault Notification Configuration <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-notifications-put.html>`__ in the *Amazon Glacier Developer Guide* . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/SetVaultNotifications>`_    


    **Request Syntax** 
    ::

      response = client.set_vault_notifications(
          vaultName='string',
          vaultNotificationConfig={
              'SNSTopic': 'string',
              'Events': [
                  'string',
              ]
          }
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    :type vaultNotificationConfig: dict
    :param vaultNotificationConfig: 

      Provides options for specifying notification configuration.

      

    
      - **SNSTopic** *(string) --* 

        The Amazon Simple Notification Service (Amazon SNS) topic Amazon Resource Name (ARN).

        

      
      - **Events** *(list) --* 

        A list of one or more events for which Amazon Glacier will send a notification to the specified Amazon SNS topic.

        

      
        - *(string) --* 

        
    
    
    
    :returns: None

    **Examples** 

    The example sets the examplevault notification configuration.
    ::

      response = client.set_vault_notifications(
          accountId='-',
          vaultName='examplevault',
          vaultNotificationConfig={
              'Events': [
                  'ArchiveRetrievalCompleted',
                  'InventoryRetrievalCompleted',
              ],
              'SNSTopic': 'arn:aws:sns:us-west-2:012345678901:mytopic',
          },
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: upload_archive(**kwargs)

    

    This operation adds an archive to a vault. This is a synchronous operation, and for a successful upload, your data is durably persisted. Amazon Glacier returns the archive ID in the ``x-amz-archive-id`` header of the response. 

     

    You must use the archive ID to access your data in Amazon Glacier. After you upload an archive, you should save the archive ID returned so that you can retrieve or delete the archive later. Besides saving the archive ID, you can also index it and give it a friendly name to allow for better searching. You can also use the optional archive description field to specify how the archive is referred to in an external index of archives, such as you might create in Amazon DynamoDB. You can also get the vault inventory to obtain a list of archive IDs in a vault. For more information, see  InitiateJob . 

     

    You must provide a SHA256 tree hash of the data you are uploading. For information about computing a SHA256 tree hash, see `Computing Checksums <http://docs.aws.amazon.com/amazonglacier/latest/dev/checksum-calculations.html>`__ . 

     

    You can optionally specify an archive description of up to 1,024 printable ASCII characters. You can get the archive description when you either retrieve the archive or get the vault inventory. For more information, see  InitiateJob . Amazon Glacier does not interpret the description in any way. An archive description does not need to be unique. You cannot use the description to retrieve or sort the archive list. 

     

    Archives are immutable. After you upload an archive, you cannot edit the archive or its description.

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and underlying REST API, see `Uploading an Archive in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-an-archive.html>`__ and `Upload Archive <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-post.html>`__ in the *Amazon Glacier Developer Guide* . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/UploadArchive>`_    


    **Request Syntax** 
    ::

      response = client.upload_archive(
          vaultName='string',
          archiveDescription='string',
          body=b'bytes'|file
      )
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. 

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type archiveDescription: string
    :param archiveDescription: 

      The optional description of the archive you are uploading.

      

    
    :type checksum: string
    :param checksum: 

      The SHA256 tree hash of the data being uploaded.

            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required



    
    :type body: bytes or seekable file-like object
    :param body: 

      The data to upload.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'location': 'string',
            'checksum': 'string',
            'archiveId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the Amazon Glacier response to your request.

         

        For information about the underlying REST API, see `Upload Archive <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-post.html>`__ . For conceptual information, see `Working with Archives in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-archives.html>`__ .

        
        

        - **location** *(string) --* 

          The relative URI path of the newly added archive resource.

          
        

        - **checksum** *(string) --* 

          The checksum of the archive computed by Amazon Glacier.

          
        

        - **archiveId** *(string) --* 

          The ID of the archive. This value is also included as part of the location.

          
    

    **Examples** 

    The example adds an archive to a vault.
    ::

      response = client.upload_archive(
          accountId='-',
          archiveDescription='',
          body='example-data-to-upload',
          checksum='',
          vaultName='my-vault',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'archiveId': 'kKB7ymWJVpPSwhGP6ycSOAekp9ZYe_--zM_mw6k76ZFGEIWQX-ybtRDvc2VkPSDtfKmQrj0IRQLSGsNuDp-AJVlu2ccmDSyDUmZwKbwbpAdGATGDiB3hHO0bjbGehXTcApVud_wyDw',
          'checksum': '969fb39823836d81f0cc028195fcdbcbbe76cdde932d4646fa7de5f21e18aa67',
          'location': '/0123456789012/vaults/my-vault/archives/kKB7ymWJVpPSwhGP6ycSOAekp9ZYe_--zM_mw6k76ZFGEIWQX-ybtRDvc2VkPSDtfKmQrj0IRQLSGsNuDp-AJVlu2ccmDSyDUmZwKbwbpAdGATGDiB3hHO0bjbGehXTcApVud_wyDw',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: upload_multipart_part(**kwargs)

    

    This operation uploads a part of an archive. You can upload archive parts in any order. You can also upload them in parallel. You can upload up to 10,000 parts for a multipart upload.

     

    Amazon Glacier rejects your upload part request if any of the following conditions is true:

     

     
    * **SHA256 tree hash does not match** To ensure that part data is not corrupted in transmission, you compute a SHA256 tree hash of the part and include it in your request. Upon receiving the part data, Amazon Glacier also computes a SHA256 tree hash. If these hash values don't match, the operation fails. For information about computing a SHA256 tree hash, see `Computing Checksums <http://docs.aws.amazon.com/amazonglacier/latest/dev/checksum-calculations.html>`__ . 
     
    * **Part size does not match** The size of each part except the last must match the size specified in the corresponding  InitiateMultipartUpload request. The size of the last part must be the same size as, or smaller than, the specified size. 

    .. note::

       If you upload a part whose size is smaller than the part size you specified in your initiate multipart upload request and that part is not the last part, then the upload part request will succeed. However, the subsequent Complete Multipart Upload request will fail. 

     
     
    * **Range does not align** The byte range value in the request does not align with the part size specified in the corresponding initiate request. For example, if you specify a part size of 4194304 bytes (4 MB), then 0 to 4194303 bytes (4 MB - 1) and 4194304 (4 MB) to 8388607 (8 MB - 1) are valid part ranges. However, if you set a range value of 2 MB to 6 MB, the range does not align with the part size and the upload will fail.  
     

     

    This operation is idempotent. If you upload the same part multiple times, the data included in the most recent request overwrites the previously uploaded data.

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and underlying REST API, see `Uploading Large Archives in Parts (Multipart Upload) <http://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-archive-mpu.html>`__ and `Upload Part <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-upload-part.html>`__ in the *Amazon Glacier Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/UploadMultipartPart>`_    


    **Request Syntax** 
    ::

      response = client.upload_multipart_part(
          vaultName='string',
          uploadId='string',
          range='string',
          body=b'bytes'|file
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. 

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    :type uploadId: string
    :param uploadId: **[REQUIRED]** 

      The upload ID of the multipart upload.

      

    
    :type checksum: string
    :param checksum: 

      The SHA256 tree hash of the data being uploaded.

            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required



    
    :type range: string
    :param range: 

      Identifies the range of bytes in the assembled archive that will be uploaded in this part. Amazon Glacier uses this information to assemble the archive in the proper sequence. The format of this header follows RFC 2616. An example header is Content-Range:bytes 0-4194303/*.

      

    
    :type body: bytes or seekable file-like object
    :param body: 

      The data to upload.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'checksum': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the Amazon Glacier response to your request.

        
        

        - **checksum** *(string) --* 

          The SHA256 tree hash that Amazon Glacier computed for the uploaded part.

          
    

    **Examples** 

    The example uploads the first 1 MiB (1024 x 1024 bytes) part of an archive.
    ::

      response = client.upload_multipart_part(
          accountId='-',
          body='part1',
          checksum='c06f7cd4baacb087002a99a5f48bf953',
          range='bytes 0-1048575/*',
          uploadId='19gaRezEXAMPLES6Ry5YYdqthHOC_kGRCT03L9yetr220UmPtBYKk-OssZtLqyFu7sY1_lR7vgFuJV6NtcV5zpsJ',
          vaultName='examplevault',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'checksum': 'c06f7cd4baacb087002a99a5f48bf953',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

==========
Paginators
==========


The available paginators are:

* :py:class:`Glacier.Paginator.ListJobs`


* :py:class:`Glacier.Paginator.ListMultipartUploads`


* :py:class:`Glacier.Paginator.ListParts`


* :py:class:`Glacier.Paginator.ListVaults`



.. py:class:: Glacier.Paginator.ListJobs

  ::

    
    paginator = client.get_paginator('list_jobs')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Glacier.Client.list_jobs`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListJobs>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          vaultName='string',
          statuscode='string',
          completed='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. 

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    :type statuscode: string
    :param statuscode: 

      The type of job status to return. You can specify the following values: ``InProgress`` , ``Succeeded`` , or ``Failed`` .

      

    
    :type completed: string
    :param completed: 

      The state of the jobs to return. You can specify ``true`` or ``false`` .

      

    
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
            'JobList': [
                {
                    'JobId': 'string',
                    'JobDescription': 'string',
                    'Action': 'ArchiveRetrieval'|'InventoryRetrieval'|'Select',
                    'ArchiveId': 'string',
                    'VaultARN': 'string',
                    'CreationDate': 'string',
                    'Completed': True|False,
                    'StatusCode': 'InProgress'|'Succeeded'|'Failed',
                    'StatusMessage': 'string',
                    'ArchiveSizeInBytes': 123,
                    'InventorySizeInBytes': 123,
                    'SNSTopic': 'string',
                    'CompletionDate': 'string',
                    'SHA256TreeHash': 'string',
                    'ArchiveSHA256TreeHash': 'string',
                    'RetrievalByteRange': 'string',
                    'Tier': 'string',
                    'InventoryRetrievalParameters': {
                        'Format': 'string',
                        'StartDate': 'string',
                        'EndDate': 'string',
                        'Limit': 'string',
                        'Marker': 'string'
                    },
                    'JobOutputPath': 'string',
                    'SelectParameters': {
                        'InputSerialization': {
                            'csv': {
                                'FileHeaderInfo': 'USE'|'IGNORE'|'NONE',
                                'Comments': 'string',
                                'QuoteEscapeCharacter': 'string',
                                'RecordDelimiter': 'string',
                                'FieldDelimiter': 'string',
                                'QuoteCharacter': 'string'
                            }
                        },
                        'ExpressionType': 'SQL',
                        'Expression': 'string',
                        'OutputSerialization': {
                            'csv': {
                                'QuoteFields': 'ALWAYS'|'ASNEEDED',
                                'QuoteEscapeCharacter': 'string',
                                'RecordDelimiter': 'string',
                                'FieldDelimiter': 'string',
                                'QuoteCharacter': 'string'
                            }
                        }
                    },
                    'OutputLocation': {
                        'S3': {
                            'BucketName': 'string',
                            'Prefix': 'string',
                            'Encryption': {
                                'EncryptionType': 'aws:kms'|'AES256',
                                'KMSKeyId': 'string',
                                'KMSContext': 'string'
                            },
                            'CannedACL': 'private'|'public-read'|'public-read-write'|'aws-exec-read'|'authenticated-read'|'bucket-owner-read'|'bucket-owner-full-control',
                            'AccessControlList': [
                                {
                                    'Grantee': {
                                        'Type': 'AmazonCustomerByEmail'|'CanonicalUser'|'Group',
                                        'DisplayName': 'string',
                                        'URI': 'string',
                                        'ID': 'string',
                                        'EmailAddress': 'string'
                                    },
                                    'Permission': 'FULL_CONTROL'|'WRITE'|'WRITE_ACP'|'READ'|'READ_ACP'
                                },
                            ],
                            'Tagging': {
                                'string': 'string'
                            },
                            'UserMetadata': {
                                'string': 'string'
                            },
                            'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA'
                        }
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the Amazon Glacier response to your request.

        
        

        - **JobList** *(list) --* 

          A list of job objects. Each job object contains metadata describing the job.

          
          

          - *(dict) --* 

            Contains the description of an Amazon Glacier job.

            
            

            - **JobId** *(string) --* 

              An opaque string that identifies an Amazon Glacier job.

              
            

            - **JobDescription** *(string) --* 

              The job description provided when initiating the job.

              
            

            - **Action** *(string) --* 

              The job type. This value is either ``ArchiveRetrieval`` , ``InventoryRetrieval`` , or ``Select`` . 

              
            

            - **ArchiveId** *(string) --* 

              The archive ID requested for a select job or archive retrieval. Otherwise, this field is null.

              
            

            - **VaultARN** *(string) --* 

              The Amazon Resource Name (ARN) of the vault from which an archive retrieval was requested.

              
            

            - **CreationDate** *(string) --* 

              The UTC date when the job was created. This value is a string representation of ISO 8601 date format, for example ``"2012-03-20T17:03:43.221Z"`` .

              
            

            - **Completed** *(boolean) --* 

              The job status. When a job is completed, you get the job's output using Get Job Output (GET output).

              
            

            - **StatusCode** *(string) --* 

              The status code can be ``InProgress`` , ``Succeeded`` , or ``Failed`` , and indicates the status of the job.

              
            

            - **StatusMessage** *(string) --* 

              A friendly message that describes the job status.

              
            

            - **ArchiveSizeInBytes** *(integer) --* 

              For an archive retrieval job, this value is the size in bytes of the archive being requested for download. For an inventory retrieval or select job, this value is null.

              
            

            - **InventorySizeInBytes** *(integer) --* 

              For an inventory retrieval job, this value is the size in bytes of the inventory requested for download. For an archive retrieval or select job, this value is null.

              
            

            - **SNSTopic** *(string) --* 

              An Amazon SNS topic that receives notification.

              
            

            - **CompletionDate** *(string) --* 

              The UTC time that the job request completed. While the job is in progress, the value is null.

              
            

            - **SHA256TreeHash** *(string) --* 

              For an archive retrieval job, this value is the checksum of the archive. Otherwise, this value is null.

               

              The SHA256 tree hash value for the requested range of an archive. If the **InitiateJob** request for an archive specified a tree-hash aligned range, then this field returns a value.

               

              If the whole archive is retrieved, this value is the same as the ArchiveSHA256TreeHash value.

               

              This field is null for the following:

               

               
              * Archive retrieval jobs that specify a range that is not tree-hash aligned 
               

               

               
              * Archival jobs that specify a range that is equal to the whole archive, when the job status is ``InProgress``   
               

               

               
              * Inventory jobs 
               
              * Select jobs 
               

              
            

            - **ArchiveSHA256TreeHash** *(string) --* 

              The SHA256 tree hash of the entire archive for an archive retrieval. For inventory retrieval or select jobs, this field is null.

              
            

            - **RetrievalByteRange** *(string) --* 

              The retrieved byte range for archive retrieval jobs in the form *StartByteValue* -*EndByteValue* . If no range was specified in the archive retrieval, then the whole archive is retrieved. In this case, *StartByteValue* equals 0 and *EndByteValue* equals the size of the archive minus 1. For inventory retrieval or select jobs, this field is null. 

              
            

            - **Tier** *(string) --* 

              The retrieval option to use for the archive retrieval. Valid values are ``Expedited`` , ``Standard`` , or ``Bulk`` . ``Standard`` is the default.

              
            

            - **InventoryRetrievalParameters** *(dict) --* 

              Parameters used for range inventory retrieval.

              
              

              - **Format** *(string) --* 

                The output format for the vault inventory list, which is set by the **InitiateJob** request when initiating a job to retrieve a vault inventory. Valid values are ``CSV`` and ``JSON`` .

                
              

              - **StartDate** *(string) --* 

                The start of the date range in Universal Coordinated Time (UTC) for vault inventory retrieval that includes archives created on or after this date. This value should be a string in the ISO 8601 date format, for example ``2013-03-20T17:03:43Z`` .

                
              

              - **EndDate** *(string) --* 

                The end of the date range in UTC for vault inventory retrieval that includes archives created before this date. This value should be a string in the ISO 8601 date format, for example ``2013-03-20T17:03:43Z`` .

                
              

              - **Limit** *(string) --* 

                The maximum number of inventory items returned per vault inventory retrieval request. This limit is set when initiating the job with the a **InitiateJob** request. 

                
              

              - **Marker** *(string) --* 

                An opaque string that represents where to continue pagination of the vault inventory retrieval results. You use the marker in a new **InitiateJob** request to obtain additional inventory items. If there are no more inventory items, this value is ``null`` . For more information, see `Range Inventory Retrieval <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html#api-initiate-job-post-vault-inventory-list-filtering>`__ .

                
          
            

            - **JobOutputPath** *(string) --* 

              Contains the job output location.

              
            

            - **SelectParameters** *(dict) --* 

              Contains the parameters that define a select job.

              
              

              - **InputSerialization** *(dict) --* 

                Describes the serialization format of the object.

                
                

                - **csv** *(dict) --* 

                  Describes the serialization of a CSV-encoded object.

                  
                  

                  - **FileHeaderInfo** *(string) --* 

                    Describes the first line of input. Valid values are ``None`` , ``Ignore`` , and ``Use`` .

                    
                  

                  - **Comments** *(string) --* 

                    A single character used to indicate that a row should be ignored when the character is present at the start of that row.

                    
                  

                  - **QuoteEscapeCharacter** *(string) --* 

                    A single character used for escaping the quotation-mark character inside an already escaped value.

                    
                  

                  - **RecordDelimiter** *(string) --* 

                    A value used to separate individual records from each other.

                    
                  

                  - **FieldDelimiter** *(string) --* 

                    A value used to separate individual fields from each other within a record.

                    
                  

                  - **QuoteCharacter** *(string) --* 

                    A value used as an escape character where the field delimiter is part of the value.

                    
              
            
              

              - **ExpressionType** *(string) --* 

                The type of the provided expression, for example ``SQL`` .

                
              

              - **Expression** *(string) --* 

                The expression that is used to select the object.

                
              

              - **OutputSerialization** *(dict) --* 

                Describes how the results of the select job are serialized.

                
                

                - **csv** *(dict) --* 

                  Describes the serialization of CSV-encoded query results.

                  
                  

                  - **QuoteFields** *(string) --* 

                    A value that indicates whether all output fields should be contained within quotation marks.

                    
                  

                  - **QuoteEscapeCharacter** *(string) --* 

                    A single character used for escaping the quotation-mark character inside an already escaped value.

                    
                  

                  - **RecordDelimiter** *(string) --* 

                    A value used to separate individual records from each other.

                    
                  

                  - **FieldDelimiter** *(string) --* 

                    A value used to separate individual fields from each other within a record.

                    
                  

                  - **QuoteCharacter** *(string) --* 

                    A value used as an escape character where the field delimiter is part of the value.

                    
              
            
          
            

            - **OutputLocation** *(dict) --* 

              Contains the location where the data from the select job is stored.

              
              

              - **S3** *(dict) --* 

                Describes an S3 location that will receive the results of the restore request.

                
                

                - **BucketName** *(string) --* 

                  The name of the bucket where the restore results are stored.

                  
                

                - **Prefix** *(string) --* 

                  The prefix that is prepended to the restore results for this request.

                  
                

                - **Encryption** *(dict) --* 

                  Contains information about the encryption used to store the job results in Amazon S3.

                  
                  

                  - **EncryptionType** *(string) --* 

                    The server-side encryption algorithm used when storing job results in Amazon S3, for example ``AES256`` or ``aws:kms`` .

                    
                  

                  - **KMSKeyId** *(string) --* 

                    The AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or Signature Version 4. 

                    
                  

                  - **KMSContext** *(string) --* 

                    Optional. If the encryption type is ``aws:kms`` , you can use this value to specify the encryption context for the restore results.

                    
              
                

                - **CannedACL** *(string) --* 

                  The canned ACL to apply to the restore results.

                  
                

                - **AccessControlList** *(list) --* 

                  A list of grants that control access to the staged results.

                  
                  

                  - *(dict) --* 

                    Contains information about a grant.

                    
                    

                    - **Grantee** *(dict) --* 

                      The grantee.

                      
                      

                      - **Type** *(string) --* 

                        Type of grantee

                        
                      

                      - **DisplayName** *(string) --* 

                        Screen name of the grantee.

                        
                      

                      - **URI** *(string) --* 

                        URI of the grantee group.

                        
                      

                      - **ID** *(string) --* 

                        The canonical user ID of the grantee.

                        
                      

                      - **EmailAddress** *(string) --* 

                        Email address of the grantee.

                        
                  
                    

                    - **Permission** *(string) --* 

                      Specifies the permission given to the grantee. 

                      
                
              
                

                - **Tagging** *(dict) --* 

                  The tag-set that is applied to the restore results.

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
                

                - **UserMetadata** *(dict) --* 

                  A map of metadata to store with the restore results in Amazon S3.

                  
                  

                  - *(string) --* 
                    

                    - *(string) --* 
              
            
                

                - **StorageClass** *(string) --* 

                  The storage class used to store the restore results.

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: Glacier.Paginator.ListMultipartUploads

  ::

    
    paginator = client.get_paginator('list_multipart_uploads')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Glacier.Client.list_multipart_uploads`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListMultipartUploads>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          vaultName='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. 

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
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
            'UploadsList': [
                {
                    'MultipartUploadId': 'string',
                    'VaultARN': 'string',
                    'ArchiveDescription': 'string',
                    'PartSizeInBytes': 123,
                    'CreationDate': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the Amazon Glacier response to your request.

        
        

        - **UploadsList** *(list) --* 

          A list of in-progress multipart uploads.

          
          

          - *(dict) --* 

            A list of in-progress multipart uploads for a vault.

            
            

            - **MultipartUploadId** *(string) --* 

              The ID of a multipart upload.

              
            

            - **VaultARN** *(string) --* 

              The Amazon Resource Name (ARN) of the vault that contains the archive.

              
            

            - **ArchiveDescription** *(string) --* 

              The description of the archive that was specified in the Initiate Multipart Upload request.

              
            

            - **PartSizeInBytes** *(integer) --* 

              The part size, in bytes, specified in the Initiate Multipart Upload request. This is the size of all the parts in the upload except the last part, which may be smaller than this size.

              
            

            - **CreationDate** *(string) --* 

              The UTC time at which the multipart upload was initiated.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: Glacier.Paginator.ListParts

  ::

    
    paginator = client.get_paginator('list_parts')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Glacier.Client.list_parts`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListParts>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          vaultName='string',
          uploadId='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. 

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    :type uploadId: string
    :param uploadId: **[REQUIRED]** 

      The upload ID of the multipart upload.

      

    
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
            'MultipartUploadId': 'string',
            'VaultARN': 'string',
            'ArchiveDescription': 'string',
            'PartSizeInBytes': 123,
            'CreationDate': 'string',
            'Parts': [
                {
                    'RangeInBytes': 'string',
                    'SHA256TreeHash': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the Amazon Glacier response to your request.

        
        

        - **MultipartUploadId** *(string) --* 

          The ID of the upload to which the parts are associated.

          
        

        - **VaultARN** *(string) --* 

          The Amazon Resource Name (ARN) of the vault to which the multipart upload was initiated.

          
        

        - **ArchiveDescription** *(string) --* 

          The description of the archive that was specified in the Initiate Multipart Upload request.

          
        

        - **PartSizeInBytes** *(integer) --* 

          The part size in bytes. This is the same value that you specified in the Initiate Multipart Upload request.

          
        

        - **CreationDate** *(string) --* 

          The UTC time at which the multipart upload was initiated.

          
        

        - **Parts** *(list) --* 

          A list of the part sizes of the multipart upload. Each object in the array contains a ``RangeBytes`` and ``sha256-tree-hash`` name/value pair.

          
          

          - *(dict) --* 

            A list of the part sizes of the multipart upload.

            
            

            - **RangeInBytes** *(string) --* 

              The byte range of a part, inclusive of the upper value of the range.

              
            

            - **SHA256TreeHash** *(string) --* 

              The SHA256 tree hash value that Amazon Glacier calculated for the part. This field is never ``null`` .

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

.. py:class:: Glacier.Paginator.ListVaults

  ::

    
    paginator = client.get_paginator('list_vaults')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Glacier.Client.list_vaults`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListVaults>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
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
            'VaultList': [
                {
                    'VaultARN': 'string',
                    'VaultName': 'string',
                    'CreationDate': 'string',
                    'LastInventoryDate': 'string',
                    'NumberOfArchives': 123,
                    'SizeInBytes': 123
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the Amazon Glacier response to your request.

        
        

        - **VaultList** *(list) --* 

          List of vaults.

          
          

          - *(dict) --* 

            Contains the Amazon Glacier response to your request.

            
            

            - **VaultARN** *(string) --* 

              The Amazon Resource Name (ARN) of the vault.

              
            

            - **VaultName** *(string) --* 

              The name of the vault.

              
            

            - **CreationDate** *(string) --* 

              The Universal Coordinated Time (UTC) date when the vault was created. This value should be a string in the ISO 8601 date format, for example ``2012-03-20T17:03:43.221Z`` .

              
            

            - **LastInventoryDate** *(string) --* 

              The Universal Coordinated Time (UTC) date when Amazon Glacier completed the last vault inventory. This value should be a string in the ISO 8601 date format, for example ``2012-03-20T17:03:43.221Z`` .

              
            

            - **NumberOfArchives** *(integer) --* 

              The number of archives in the vault as of the last inventory date. This field will return ``null`` if an inventory has not yet run on the vault, for example if you just created the vault.

              
            

            - **SizeInBytes** *(integer) --* 

              Total size, in bytes, of the archives in the vault as of the last inventory date. This field will return null if an inventory has not yet run on the vault, for example if you just created the vault.

              
        
      
        

        - **NextToken** *(string) --* 

          A token to resume pagination.

          
    

=======
Waiters
=======


The available waiters are:

* :py:class:`Glacier.Waiter.VaultExists`


* :py:class:`Glacier.Waiter.VaultNotExists`



.. py:class:: Glacier.Waiter.VaultExists

  ::

    
    waiter = client.get_waiter('vault_exists')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`Glacier.Client.describe_vault` every 3 seconds until a successful state is reached. An error is returned after 15 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/DescribeVault>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          vaultName='string',
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. 

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 3

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 15

        

      
    
    
    :returns: None

.. py:class:: Glacier.Waiter.VaultNotExists

  ::

    
    waiter = client.get_waiter('vault_not_exists')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`Glacier.Client.describe_vault` every 3 seconds until a successful state is reached. An error is returned after 15 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/DescribeVault>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          vaultName='string',
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type accountId: string
    :param accountId: 

      The ``AccountId`` value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '``-`` ' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. 

            Note: this parameter is set to "-" bydefault if no value is not specified.


    
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 3

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 15

        

      
    
    
    :returns: None

================
Service Resource
================



.. py:class:: Glacier.ServiceResource()

  A resource representing Amazon Glacier::

    
    import boto3
    
    glacier = boto3.resource('glacier')

  
  These are the resource's available actions:
  
  *   :py:meth:`create_vault()`

  
  *   :py:meth:`get_available_subresources()`

  
  These are the resource's available sub-resources:
  
  *   :py:meth:`Account()`

  
  *   :py:meth:`Archive()`

  
  *   :py:meth:`Job()`

  
  *   :py:meth:`MultipartUpload()`

  
  *   :py:meth:`Notification()`

  
  *   :py:meth:`Vault()`

  
  These are the resource's available collections:
  
  *   :py:attr:`vaults`

  
  .. rst-class:: admonition-title
  
  Actions
  
  Actions call operations on resources.  They may automatically handle the passing in of arguments set from identifiers and some attributes.
  For more information about actions refer to the :ref:`Resources Introduction Guide<actions_intro>`.
  

  .. py:method:: create_vault(**kwargs)

    

    This operation creates a new vault with the specified name. The name of the vault must be unique within a region for an AWS account. You can create up to 1,000 vaults per account. If you need to create more vaults, contact Amazon Glacier.

     

    You must use the following guidelines when naming a vault.

     

     
    * Names can be between 1 and 255 characters long. 
     
    * Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), and '.' (period). 
     

     

    This operation is idempotent.

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and underlying REST API, see `Creating a Vault in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/creating-vaults.html>`__ and `Create Vault <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-put.html>`__ in the *Amazon Glacier Developer Guide* . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/CreateVault>`_    


    **Request Syntax** 
    ::

      vault = glacier.create_vault(
          vaultName='string'
      )
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    
    :rtype: :py:class:`glacier.Vault`
    :returns: Vault resource
    

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
  

  .. py:method:: Account(id)

    Creates a Account resource.::

      account = glacier.Account('id')

    :type id: string
    :param id: The Account's id identifier. This **must** be set.
    
    :rtype: :py:class:`Glacier.Account`
    :returns: A Account resource
    

  .. py:method:: Archive(account_id,vault_name,id)

    Creates a Archive resource.::

      archive = glacier.Archive('account_id','vault_name','id')

    :type account_id: string
    :param account_id: The Archive's account_id identifier. This **must** be set.
    :type vault_name: string
    :param vault_name: The Archive's vault_name identifier. This **must** be set.
    :type id: string
    :param id: The Archive's id identifier. This **must** be set.
    
    :rtype: :py:class:`Glacier.Archive`
    :returns: A Archive resource
    

  .. py:method:: Job(account_id,vault_name,id)

    Creates a Job resource.::

      job = glacier.Job('account_id','vault_name','id')

    :type account_id: string
    :param account_id: The Job's account_id identifier. This **must** be set.
    :type vault_name: string
    :param vault_name: The Job's vault_name identifier. This **must** be set.
    :type id: string
    :param id: The Job's id identifier. This **must** be set.
    
    :rtype: :py:class:`Glacier.Job`
    :returns: A Job resource
    

  .. py:method:: MultipartUpload(account_id,vault_name,id)

    Creates a MultipartUpload resource.::

      multipart_upload = glacier.MultipartUpload('account_id','vault_name','id')

    :type account_id: string
    :param account_id: The MultipartUpload's account_id identifier. This **must** be set.
    :type vault_name: string
    :param vault_name: The MultipartUpload's vault_name identifier. This **must** be set.
    :type id: string
    :param id: The MultipartUpload's id identifier. This **must** be set.
    
    :rtype: :py:class:`Glacier.MultipartUpload`
    :returns: A MultipartUpload resource
    

  .. py:method:: Notification(account_id,vault_name)

    Creates a Notification resource.::

      notification = glacier.Notification('account_id','vault_name')

    :type account_id: string
    :param account_id: The Notification's account_id identifier. This **must** be set.
    :type vault_name: string
    :param vault_name: The Notification's vault_name identifier. This **must** be set.
    
    :rtype: :py:class:`Glacier.Notification`
    :returns: A Notification resource
    

  .. py:method:: Vault(account_id,name)

    Creates a Vault resource.::

      vault = glacier.Vault('account_id','name')

    :type account_id: string
    :param account_id: The Vault's account_id identifier. This **must** be set.
    :type name: string
    :param name: The Vault's name identifier. This **must** be set.
    
    :rtype: :py:class:`Glacier.Vault`
    :returns: A Vault resource
    
  .. rst-class:: admonition-title
  
  Collections
  
  Collections provide an interface to iterate over and manipulate groups of resources. 
  For more information about collections refer to the :ref:`Resources Introduction Guide<guide_collections>`.
  

  .. py:attribute:: vaults

    A collection of Vault resources

    .. py:method:: all()

      Creates an iterable of all Vault resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListVaults>`_      


      **Request Syntax** 
      ::

        vault_iterator = glacier.vaults.all()
        
      
      :rtype: list(:py:class:`glacier.Vault`)
      :returns: A list of Vault resources
      

    .. py:method:: filter(**kwargs)

      Creates an iterable of all Vault resources in the collection filtered by kwargs passed to method.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListVaults>`_      


      **Request Syntax** 
      ::

        vault_iterator = glacier.vaults.filter(
            marker='string',
            limit='string'
        )
      :type marker: string
      :param marker: 

        A string used for pagination. The marker specifies the vault ARN after which the listing of vaults should begin.

        

      
      :type limit: string
      :param limit: 

        The maximum number of vaults to be returned. The default limit is 1000. The number of vaults returned might be fewer than the specified limit, but the number of returned vaults never exceeds the limit.

        

      
      
      :rtype: list(:py:class:`glacier.Vault`)
      :returns: A list of Vault resources
      

    .. py:method:: limit(**kwargs)

      Creates an iterable up to a specified amount of Vault resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListVaults>`_      


      **Request Syntax** 
      ::

        vault_iterator = glacier.vaults.limit(
            count=123
        )
      :type count: integer
      :param count: The limit to the number of resources in the iterable.

      
      
      :rtype: list(:py:class:`glacier.Vault`)
      :returns: A list of Vault resources
      

    .. py:method:: page_size(**kwargs)

      Creates an iterable of all Vault resources in the collection, but limits the number of items returned by each service call by the specified amount.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListVaults>`_      


      **Request Syntax** 
      ::

        vault_iterator = glacier.vaults.page_size(
            count=123
        )
      :type count: integer
      :param count: The number of items returned by each service call

      
      
      :rtype: list(:py:class:`glacier.Vault`)
      :returns: A list of Vault resources
      

=======
Account
=======



.. py:class:: Glacier.Account(id)

  A resource representing an Amazon Glacier Account::

    
    import boto3
    
    glacier = boto3.resource('glacier')
    account = glacier.Account('id')

  :type id: string
  :param id: The Account's id identifier. This **must** be set.
  
  These are the resource's available identifiers:
  
  *   :py:attr:`id`

  
  These are the resource's available actions:
  
  *   :py:meth:`create_vault()`

  
  *   :py:meth:`get_available_subresources()`

  
  These are the resource's available sub-resources:
  
  *   :py:meth:`Vault()`

  
  These are the resource's available collections:
  
  *   :py:attr:`vaults`

  
  .. rst-class:: admonition-title
  
  Identifiers
  
  Identifiers are properties of a resource that are set upon instantation of the resource.
  For more information about identifiers refer to the :ref:`Resources Introduction Guide<identifiers_attributes_intro>`.
  

  .. py:attribute:: id

    *(string)* The Account's id identifier. This **must** be set.
  .. rst-class:: admonition-title
  
  Actions
  
  Actions call operations on resources.  They may automatically handle the passing in of arguments set from identifiers and some attributes.
  For more information about actions refer to the :ref:`Resources Introduction Guide<actions_intro>`.
  

  .. py:method:: create_vault(**kwargs)

    

    This operation creates a new vault with the specified name. The name of the vault must be unique within a region for an AWS account. You can create up to 1,000 vaults per account. If you need to create more vaults, contact Amazon Glacier.

     

    You must use the following guidelines when naming a vault.

     

     
    * Names can be between 1 and 255 characters long. 
     
    * Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), and '.' (period). 
     

     

    This operation is idempotent.

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and underlying REST API, see `Creating a Vault in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/creating-vaults.html>`__ and `Create Vault <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-put.html>`__ in the *Amazon Glacier Developer Guide* . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/CreateVault>`_    


    **Request Syntax** 
    ::

      vault = account.create_vault(
          vaultName='string'
      )
    :type vaultName: string
    :param vaultName: **[REQUIRED]** 

      The name of the vault.

      

    
    
    :rtype: :py:class:`glacier.Vault`
    :returns: Vault resource
    

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
  

  .. py:method:: Vault(name)

    Creates a Vault resource.::

      vault = account.Vault('name')

    :type name: string
    :param name: The Vault's name identifier. This **must** be set.
    
    :rtype: :py:class:`Glacier.Vault`
    :returns: A Vault resource
    
  .. rst-class:: admonition-title
  
  Collections
  
  Collections provide an interface to iterate over and manipulate groups of resources. 
  For more information about collections refer to the :ref:`Resources Introduction Guide<guide_collections>`.
  

  .. py:attribute:: vaults

    A collection of Vault resources

    .. py:method:: all()

      Creates an iterable of all Vault resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListVaults>`_      


      **Request Syntax** 
      ::

        vault_iterator = account.vaults.all()
        
      
      :rtype: list(:py:class:`glacier.Vault`)
      :returns: A list of Vault resources
      

    .. py:method:: filter(**kwargs)

      Creates an iterable of all Vault resources in the collection filtered by kwargs passed to method.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListVaults>`_      


      **Request Syntax** 
      ::

        vault_iterator = account.vaults.filter(
            marker='string',
            limit='string'
        )
      :type marker: string
      :param marker: 

        A string used for pagination. The marker specifies the vault ARN after which the listing of vaults should begin.

        

      
      :type limit: string
      :param limit: 

        The maximum number of vaults to be returned. The default limit is 1000. The number of vaults returned might be fewer than the specified limit, but the number of returned vaults never exceeds the limit.

        

      
      
      :rtype: list(:py:class:`glacier.Vault`)
      :returns: A list of Vault resources
      

    .. py:method:: limit(**kwargs)

      Creates an iterable up to a specified amount of Vault resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListVaults>`_      


      **Request Syntax** 
      ::

        vault_iterator = account.vaults.limit(
            count=123
        )
      :type count: integer
      :param count: The limit to the number of resources in the iterable.

      
      
      :rtype: list(:py:class:`glacier.Vault`)
      :returns: A list of Vault resources
      

    .. py:method:: page_size(**kwargs)

      Creates an iterable of all Vault resources in the collection, but limits the number of items returned by each service call by the specified amount.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListVaults>`_      


      **Request Syntax** 
      ::

        vault_iterator = account.vaults.page_size(
            count=123
        )
      :type count: integer
      :param count: The number of items returned by each service call

      
      
      :rtype: list(:py:class:`glacier.Vault`)
      :returns: A list of Vault resources
      

=======
Archive
=======



.. py:class:: Glacier.Archive(account_id,vault_name,id)

  A resource representing an Amazon Glacier Archive::

    
    import boto3
    
    glacier = boto3.resource('glacier')
    archive = glacier.Archive('account_id','vault_name','id')

  :type account_id: string
  :param account_id: The Archive's account_id identifier. This **must** be set.
  :type vault_name: string
  :param vault_name: The Archive's vault_name identifier. This **must** be set.
  :type id: string
  :param id: The Archive's id identifier. This **must** be set.
  
  These are the resource's available identifiers:
  
  *   :py:attr:`account_id`

  
  *   :py:attr:`vault_name`

  
  *   :py:attr:`id`

  
  These are the resource's available actions:
  
  *   :py:meth:`delete()`

  
  *   :py:meth:`get_available_subresources()`

  
  *   :py:meth:`initiate_archive_retrieval()`

  
  These are the resource's available sub-resources:
  
  *   :py:meth:`Vault()`

  
  .. rst-class:: admonition-title
  
  Identifiers
  
  Identifiers are properties of a resource that are set upon instantation of the resource.
  For more information about identifiers refer to the :ref:`Resources Introduction Guide<identifiers_attributes_intro>`.
  

  .. py:attribute:: account_id

    *(string)* The Archive's account_id identifier. This **must** be set.

  .. py:attribute:: vault_name

    *(string)* The Archive's vault_name identifier. This **must** be set.

  .. py:attribute:: id

    *(string)* The Archive's id identifier. This **must** be set.
  .. rst-class:: admonition-title
  
  Actions
  
  Actions call operations on resources.  They may automatically handle the passing in of arguments set from identifiers and some attributes.
  For more information about actions refer to the :ref:`Resources Introduction Guide<actions_intro>`.
  

  .. py:method:: delete()

    

    This operation deletes an archive from a vault. Subsequent requests to initiate a retrieval of this archive will fail. Archive retrievals that are in progress for this archive ID may or may not succeed according to the following scenarios:

     

     
    * If the archive retrieval job is actively preparing the data for download when Amazon Glacier receives the delete archive request, the archival retrieval operation might fail. 
     
    * If the archive retrieval job has successfully prepared the archive for download when Amazon Glacier receives the delete archive request, you will be able to download the output. 
     

     

    This operation is idempotent. Attempting to delete an already-deleted archive does not result in an error.

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and underlying REST API, see `Deleting an Archive in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-an-archive.html>`__ and `Delete Archive <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-delete.html>`__ in the *Amazon Glacier Developer Guide* . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/DeleteArchive>`_    


    **Request Syntax** 
    ::

      response = archive.delete()
      
    
    :returns: None

  .. py:method:: get_available_subresources()

        
    Returns a list of all the available sub-resources for this
    Resource.
    
    :returns: A list containing the name of each sub-resource for this
        resource
    :rtype: list of str


  .. py:method:: initiate_archive_retrieval()

    

    This operation initiates a job of the specified type, which can be a select, an archival retrieval, or a vault retrieval. For more information about using this operation, see the documentation for the underlying REST API `Initiate a Job <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html>`__ . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/InitiateJob>`_    


    **Request Syntax** 
    ::

      job = archive.initiate_archive_retrieval()
      
    
    :rtype: :py:class:`glacier.Job`
    :returns: Job resource
    
  .. rst-class:: admonition-title
  
  Sub-resources
  
  Sub-resources are methods that create a new instance of a child resource. This resource's identifiers get passed along to the child.
  For more information about sub-resources refer to the :ref:`Resources Introduction Guide<subresources_intro>`.
  

  .. py:method:: Vault()

    Creates a Vault resource.::

      vault = archive.Vault()

    
    :rtype: :py:class:`Glacier.Vault`
    :returns: A Vault resource
    

===
Job
===



.. py:class:: Glacier.Job(account_id,vault_name,id)

  A resource representing an Amazon Glacier Job::

    
    import boto3
    
    glacier = boto3.resource('glacier')
    job = glacier.Job('account_id','vault_name','id')

  :type account_id: string
  :param account_id: The Job's account_id identifier. This **must** be set.
  :type vault_name: string
  :param vault_name: The Job's vault_name identifier. This **must** be set.
  :type id: string
  :param id: The Job's id identifier. This **must** be set.
  
  These are the resource's available identifiers:
  
  *   :py:attr:`account_id`

  
  *   :py:attr:`vault_name`

  
  *   :py:attr:`id`

  
  These are the resource's available attributes:
  
  *   :py:attr:`action`

  
  *   :py:attr:`archive_id`

  
  *   :py:attr:`archive_sha256_tree_hash`

  
  *   :py:attr:`archive_size_in_bytes`

  
  *   :py:attr:`completed`

  
  *   :py:attr:`completion_date`

  
  *   :py:attr:`creation_date`

  
  *   :py:attr:`inventory_retrieval_parameters`

  
  *   :py:attr:`inventory_size_in_bytes`

  
  *   :py:attr:`job_description`

  
  *   :py:attr:`job_id`

  
  *   :py:attr:`job_output_path`

  
  *   :py:attr:`output_location`

  
  *   :py:attr:`retrieval_byte_range`

  
  *   :py:attr:`select_parameters`

  
  *   :py:attr:`sha256_tree_hash`

  
  *   :py:attr:`sns_topic`

  
  *   :py:attr:`status_code`

  
  *   :py:attr:`status_message`

  
  *   :py:attr:`tier`

  
  *   :py:attr:`vault_arn`

  
  These are the resource's available actions:
  
  *   :py:meth:`get_available_subresources()`

  
  *   :py:meth:`get_output()`

  
  *   :py:meth:`load()`

  
  *   :py:meth:`reload()`

  
  These are the resource's available sub-resources:
  
  *   :py:meth:`Vault()`

  
  .. rst-class:: admonition-title
  
  Identifiers
  
  Identifiers are properties of a resource that are set upon instantation of the resource.
  For more information about identifiers refer to the :ref:`Resources Introduction Guide<identifiers_attributes_intro>`.
  

  .. py:attribute:: account_id

    *(string)* The Job's account_id identifier. This **must** be set.

  .. py:attribute:: vault_name

    *(string)* The Job's vault_name identifier. This **must** be set.

  .. py:attribute:: id

    *(string)* The Job's id identifier. This **must** be set.
  .. rst-class:: admonition-title
  
  Attributes
  
  Attributes provide access to the properties of a resource. Attributes are lazy-loaded the first time one is accessed via the :py:meth:`load` method.
  For more information about attributes refer to the :ref:`Resources Introduction Guide<identifiers_attributes_intro>`.
  

  .. py:attribute:: action

    

    - *(string) --* 

      The job type. This value is either ``ArchiveRetrieval`` , ``InventoryRetrieval`` , or ``Select`` . 

      

  .. py:attribute:: archive_id

    

    - *(string) --* 

      The archive ID requested for a select job or archive retrieval. Otherwise, this field is null.

      

  .. py:attribute:: archive_sha256_tree_hash

    

    - *(string) --* 

      The SHA256 tree hash of the entire archive for an archive retrieval. For inventory retrieval or select jobs, this field is null.

      

  .. py:attribute:: archive_size_in_bytes

    

    - *(integer) --* 

      For an archive retrieval job, this value is the size in bytes of the archive being requested for download. For an inventory retrieval or select job, this value is null.

      

  .. py:attribute:: completed

    

    - *(boolean) --* 

      The job status. When a job is completed, you get the job's output using Get Job Output (GET output).

      

  .. py:attribute:: completion_date

    

    - *(string) --* 

      The UTC time that the job request completed. While the job is in progress, the value is null.

      

  .. py:attribute:: creation_date

    

    - *(string) --* 

      The UTC date when the job was created. This value is a string representation of ISO 8601 date format, for example ``"2012-03-20T17:03:43.221Z"`` .

      

  .. py:attribute:: inventory_retrieval_parameters

    

    - *(dict) --* 

      Parameters used for range inventory retrieval.

      
      

      - **Format** *(string) --* 

        The output format for the vault inventory list, which is set by the **InitiateJob** request when initiating a job to retrieve a vault inventory. Valid values are ``CSV`` and ``JSON`` .

        
      

      - **StartDate** *(string) --* 

        The start of the date range in Universal Coordinated Time (UTC) for vault inventory retrieval that includes archives created on or after this date. This value should be a string in the ISO 8601 date format, for example ``2013-03-20T17:03:43Z`` .

        
      

      - **EndDate** *(string) --* 

        The end of the date range in UTC for vault inventory retrieval that includes archives created before this date. This value should be a string in the ISO 8601 date format, for example ``2013-03-20T17:03:43Z`` .

        
      

      - **Limit** *(string) --* 

        The maximum number of inventory items returned per vault inventory retrieval request. This limit is set when initiating the job with the a **InitiateJob** request. 

        
      

      - **Marker** *(string) --* 

        An opaque string that represents where to continue pagination of the vault inventory retrieval results. You use the marker in a new **InitiateJob** request to obtain additional inventory items. If there are no more inventory items, this value is ``null`` . For more information, see `Range Inventory Retrieval <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html#api-initiate-job-post-vault-inventory-list-filtering>`__ .

        
  

  .. py:attribute:: inventory_size_in_bytes

    

    - *(integer) --* 

      For an inventory retrieval job, this value is the size in bytes of the inventory requested for download. For an archive retrieval or select job, this value is null.

      

  .. py:attribute:: job_description

    

    - *(string) --* 

      The job description provided when initiating the job.

      

  .. py:attribute:: job_id

    

    - *(string) --* 

      An opaque string that identifies an Amazon Glacier job.

      

  .. py:attribute:: job_output_path

    

    - *(string) --* 

      Contains the job output location.

      

  .. py:attribute:: output_location

    

    - *(dict) --* 

      Contains the location where the data from the select job is stored.

      
      

      - **S3** *(dict) --* 

        Describes an S3 location that will receive the results of the restore request.

        
        

        - **BucketName** *(string) --* 

          The name of the bucket where the restore results are stored.

          
        

        - **Prefix** *(string) --* 

          The prefix that is prepended to the restore results for this request.

          
        

        - **Encryption** *(dict) --* 

          Contains information about the encryption used to store the job results in Amazon S3.

          
          

          - **EncryptionType** *(string) --* 

            The server-side encryption algorithm used when storing job results in Amazon S3, for example ``AES256`` or ``aws:kms`` .

            
          

          - **KMSKeyId** *(string) --* 

            The AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or Signature Version 4. 

            
          

          - **KMSContext** *(string) --* 

            Optional. If the encryption type is ``aws:kms`` , you can use this value to specify the encryption context for the restore results.

            
      
        

        - **CannedACL** *(string) --* 

          The canned ACL to apply to the restore results.

          
        

        - **AccessControlList** *(list) --* 

          A list of grants that control access to the staged results.

          
          

          - *(dict) --* 

            Contains information about a grant.

            
            

            - **Grantee** *(dict) --* 

              The grantee.

              
              

              - **Type** *(string) --* 

                Type of grantee

                
              

              - **DisplayName** *(string) --* 

                Screen name of the grantee.

                
              

              - **URI** *(string) --* 

                URI of the grantee group.

                
              

              - **ID** *(string) --* 

                The canonical user ID of the grantee.

                
              

              - **EmailAddress** *(string) --* 

                Email address of the grantee.

                
          
            

            - **Permission** *(string) --* 

              Specifies the permission given to the grantee. 

              
        
      
        

        - **Tagging** *(dict) --* 

          The tag-set that is applied to the restore results.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **UserMetadata** *(dict) --* 

          A map of metadata to store with the restore results in Amazon S3.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **StorageClass** *(string) --* 

          The storage class used to store the restore results.

          
    
  

  .. py:attribute:: retrieval_byte_range

    

    - *(string) --* 

      The retrieved byte range for archive retrieval jobs in the form *StartByteValue* -*EndByteValue* . If no range was specified in the archive retrieval, then the whole archive is retrieved. In this case, *StartByteValue* equals 0 and *EndByteValue* equals the size of the archive minus 1. For inventory retrieval or select jobs, this field is null. 

      

  .. py:attribute:: select_parameters

    

    - *(dict) --* 

      Contains the parameters that define a select job.

      
      

      - **InputSerialization** *(dict) --* 

        Describes the serialization format of the object.

        
        

        - **csv** *(dict) --* 

          Describes the serialization of a CSV-encoded object.

          
          

          - **FileHeaderInfo** *(string) --* 

            Describes the first line of input. Valid values are ``None`` , ``Ignore`` , and ``Use`` .

            
          

          - **Comments** *(string) --* 

            A single character used to indicate that a row should be ignored when the character is present at the start of that row.

            
          

          - **QuoteEscapeCharacter** *(string) --* 

            A single character used for escaping the quotation-mark character inside an already escaped value.

            
          

          - **RecordDelimiter** *(string) --* 

            A value used to separate individual records from each other.

            
          

          - **FieldDelimiter** *(string) --* 

            A value used to separate individual fields from each other within a record.

            
          

          - **QuoteCharacter** *(string) --* 

            A value used as an escape character where the field delimiter is part of the value.

            
      
    
      

      - **ExpressionType** *(string) --* 

        The type of the provided expression, for example ``SQL`` .

        
      

      - **Expression** *(string) --* 

        The expression that is used to select the object.

        
      

      - **OutputSerialization** *(dict) --* 

        Describes how the results of the select job are serialized.

        
        

        - **csv** *(dict) --* 

          Describes the serialization of CSV-encoded query results.

          
          

          - **QuoteFields** *(string) --* 

            A value that indicates whether all output fields should be contained within quotation marks.

            
          

          - **QuoteEscapeCharacter** *(string) --* 

            A single character used for escaping the quotation-mark character inside an already escaped value.

            
          

          - **RecordDelimiter** *(string) --* 

            A value used to separate individual records from each other.

            
          

          - **FieldDelimiter** *(string) --* 

            A value used to separate individual fields from each other within a record.

            
          

          - **QuoteCharacter** *(string) --* 

            A value used as an escape character where the field delimiter is part of the value.

            
      
    
  

  .. py:attribute:: sha256_tree_hash

    

    - *(string) --* 

      For an archive retrieval job, this value is the checksum of the archive. Otherwise, this value is null.

       

      The SHA256 tree hash value for the requested range of an archive. If the **InitiateJob** request for an archive specified a tree-hash aligned range, then this field returns a value.

       

      If the whole archive is retrieved, this value is the same as the ArchiveSHA256TreeHash value.

       

      This field is null for the following:

       

       
      * Archive retrieval jobs that specify a range that is not tree-hash aligned 
       

       

       
      * Archival jobs that specify a range that is equal to the whole archive, when the job status is ``InProgress``   
       

       

       
      * Inventory jobs 
       
      * Select jobs 
       

      

  .. py:attribute:: sns_topic

    

    - *(string) --* 

      An Amazon SNS topic that receives notification.

      

  .. py:attribute:: status_code

    

    - *(string) --* 

      The status code can be ``InProgress`` , ``Succeeded`` , or ``Failed`` , and indicates the status of the job.

      

  .. py:attribute:: status_message

    

    - *(string) --* 

      A friendly message that describes the job status.

      

  .. py:attribute:: tier

    

    - *(string) --* 

      The retrieval option to use for the archive retrieval. Valid values are ``Expedited`` , ``Standard`` , or ``Bulk`` . ``Standard`` is the default.

      

  .. py:attribute:: vault_arn

    

    - *(string) --* 

      The Amazon Resource Name (ARN) of the vault from which an archive retrieval was requested.

      
  .. rst-class:: admonition-title
  
  Actions
  
  Actions call operations on resources.  They may automatically handle the passing in of arguments set from identifiers and some attributes.
  For more information about actions refer to the :ref:`Resources Introduction Guide<actions_intro>`.
  

  .. py:method:: get_available_subresources()

        
    Returns a list of all the available sub-resources for this
    Resource.
    
    :returns: A list containing the name of each sub-resource for this
        resource
    :rtype: list of str


  .. py:method:: get_output(**kwargs)

    

    This operation downloads the output of the job you initiated using  InitiateJob . Depending on the job type you specified when you initiated the job, the output will be either the content of an archive or a vault inventory.

     

    You can download all the job output or download a portion of the output by specifying a byte range. In the case of an archive retrieval job, depending on the byte range you specify, Amazon Glacier returns the checksum for the portion of the data. You can compute the checksum on the client and verify that the values match to ensure the portion you downloaded is the correct data.

     

    A job ID will not expire for at least 24 hours after Amazon Glacier completes the job. That a byte range. For both archive and inventory retrieval jobs, you should verify the downloaded size against the size returned in the headers from the **Get Job Output** response.

     

    For archive retrieval jobs, you should also verify that the size is what you expected. If you download a portion of the output, the expected size is based on the range of bytes you specified. For example, if you specify a range of ``bytes=0-1048575`` , you should verify your download size is 1,048,576 bytes. If you download an entire archive, the expected size is the size of the archive when you uploaded it to Amazon Glacier The expected size is also returned in the headers from the **Get Job Output** response.

     

    In the case of an archive retrieval job, depending on the byte range you specify, Amazon Glacier returns the checksum for the portion of the data. To ensure the portion you downloaded is the correct data, compute the checksum on the client, verify that the values match, and verify that the size is what you expected.

     

    A job ID does not expire for at least 24 hours after Amazon Glacier completes the job. That is, you can download the job output within the 24 hours period after Amazon Glacier completes the job.

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and the underlying REST API, see `Downloading a Vault Inventory <http://docs.aws.amazon.com/amazonglacier/latest/dev/vault-inventory.html>`__ , `Downloading an Archive <http://docs.aws.amazon.com/amazonglacier/latest/dev/downloading-an-archive.html>`__ , and `Get Job Output <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-job-output-get.html>`__  

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/GetJobOutput>`_    


    **Request Syntax** 
    ::

      response = job.get_output(
          range='string'
      )
    :type range: string
    :param range: 

      The range of bytes to retrieve from the output. For example, if you want to download the first 1,048,576 bytes, specify the range as ``bytes=0-1048575`` . By default, this operation downloads the entire output.

       

      If the job output is large, then you can use a range to retrieve a portion of the output. This allows you to download the entire output in smaller chunks of bytes. For example, suppose you have 1 GB of job output you want to download and you decide to download 128 MB chunks of data at a time, which is a total of eight Get Job Output requests. You use the following process to download the job output:

       

       
      * Download a 128 MB chunk of output by specifying the appropriate byte range. Verify that all 128 MB of data was received. 
       
      * Along with the data, the response includes a SHA256 tree hash of the payload. You compute the checksum of the payload on the client and compare it with the checksum you received in the response to ensure you received all the expected data. 
       
      * Repeat steps 1 and 2 for all the eight 128 MB chunks of output data, each time specifying the appropriate byte range. 
       
      * After downloading all the parts of the job output, you have a list of eight checksum values. Compute the tree hash of these values to find the checksum of the entire output. Using the  DescribeJob API, obtain job information of the job that provided you the output. The response includes the checksum of the entire archive stored in Amazon Glacier. You compare this value with the checksum you computed to ensure you have downloaded the entire archive content with no errors.  
       

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'body': StreamingBody(),
            'checksum': 'string',
            'status': 123,
            'contentRange': 'string',
            'acceptRanges': 'string',
            'contentType': 'string',
            'archiveDescription': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the Amazon Glacier response to your request.

        
        

        - **body** (:class:`.StreamingBody`) -- 

          The job data, either archive data or inventory data.

          
        

        - **checksum** *(string) --* 

          The checksum of the data in the response. This header is returned only when retrieving the output for an archive retrieval job. Furthermore, this header appears only under the following conditions:

           

           
          * You get the entire range of the archive. 
           
          * You request a range to return of the archive that starts and ends on a multiple of 1 MB. For example, if you have an 3.1 MB archive and you specify a range to return that starts at 1 MB and ends at 2 MB, then the x-amz-sha256-tree-hash is returned as a response header. 
           
          * You request a range of the archive to return that starts on a multiple of 1 MB and goes to the end of the archive. For example, if you have a 3.1 MB archive and you specify a range that starts at 2 MB and ends at 3.1 MB (the end of the archive), then the x-amz-sha256-tree-hash is returned as a response header. 
           

          
        

        - **status** *(integer) --* 

          The HTTP response code for a job output request. The value depends on whether a range was specified in the request.

          
        

        - **contentRange** *(string) --* 

          The range of bytes returned by Amazon Glacier. If only partial output is downloaded, the response provides the range of bytes Amazon Glacier returned. For example, bytes 0-1048575/8388608 returns the first 1 MB from 8 MB.

          
        

        - **acceptRanges** *(string) --* 

          Indicates the range units accepted. For more information, see `RFC2616 <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html>`__ . 

          
        

        - **contentType** *(string) --* 

          The Content-Type depends on whether the job output is an archive or a vault inventory. For archive data, the Content-Type is application/octet-stream. For vault inventory, if you requested CSV format when you initiated the job, the Content-Type is text/csv. Otherwise, by default, vault inventory is returned as JSON, and the Content-Type is application/json.

          
        

        - **archiveDescription** *(string) --* 

          The description of an archive.

          
    

  .. py:method:: load()

    Calls :py:meth:`Glacier.Client.describe_job` to update the attributes of the Job resource. Note that the load and reload methods are the same method and can be used interchangeably.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/None>`_    


    **Request Syntax** 

    ::

      job.load()
    :returns: None

  .. py:method:: reload()

    Calls :py:meth:`Glacier.Client.describe_job` to update the attributes of the Job resource. Note that the load and reload methods are the same method and can be used interchangeably.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/None>`_    


    **Request Syntax** 

    ::

      job.reload()
    :returns: None
  .. rst-class:: admonition-title
  
  Sub-resources
  
  Sub-resources are methods that create a new instance of a child resource. This resource's identifiers get passed along to the child.
  For more information about sub-resources refer to the :ref:`Resources Introduction Guide<subresources_intro>`.
  

  .. py:method:: Vault()

    Creates a Vault resource.::

      vault = job.Vault()

    
    :rtype: :py:class:`Glacier.Vault`
    :returns: A Vault resource
    

===============
MultipartUpload
===============



.. py:class:: Glacier.MultipartUpload(account_id,vault_name,id)

  A resource representing an Amazon Glacier MultipartUpload::

    
    import boto3
    
    glacier = boto3.resource('glacier')
    multipart_upload = glacier.MultipartUpload('account_id','vault_name','id')

  :type account_id: string
  :param account_id: The MultipartUpload's account_id identifier. This **must** be set.
  :type vault_name: string
  :param vault_name: The MultipartUpload's vault_name identifier. This **must** be set.
  :type id: string
  :param id: The MultipartUpload's id identifier. This **must** be set.
  
  These are the resource's available identifiers:
  
  *   :py:attr:`account_id`

  
  *   :py:attr:`vault_name`

  
  *   :py:attr:`id`

  
  These are the resource's available attributes:
  
  *   :py:attr:`archive_description`

  
  *   :py:attr:`creation_date`

  
  *   :py:attr:`multipart_upload_id`

  
  *   :py:attr:`part_size_in_bytes`

  
  *   :py:attr:`vault_arn`

  
  These are the resource's available actions:
  
  *   :py:meth:`abort()`

  
  *   :py:meth:`complete()`

  
  *   :py:meth:`get_available_subresources()`

  
  *   :py:meth:`parts()`

  
  *   :py:meth:`upload_part()`

  
  These are the resource's available sub-resources:
  
  *   :py:meth:`Vault()`

  
  .. rst-class:: admonition-title
  
  Identifiers
  
  Identifiers are properties of a resource that are set upon instantation of the resource.
  For more information about identifiers refer to the :ref:`Resources Introduction Guide<identifiers_attributes_intro>`.
  

  .. py:attribute:: account_id

    *(string)* The MultipartUpload's account_id identifier. This **must** be set.

  .. py:attribute:: vault_name

    *(string)* The MultipartUpload's vault_name identifier. This **must** be set.

  .. py:attribute:: id

    *(string)* The MultipartUpload's id identifier. This **must** be set.
  .. rst-class:: admonition-title
  
  Attributes
  
  Attributes provide access to the properties of a resource. Attributes are lazy-loaded the first time one is accessed via the :py:meth:`load` method.
  For more information about attributes refer to the :ref:`Resources Introduction Guide<identifiers_attributes_intro>`.
  

  .. py:attribute:: archive_description

    

    - *(string) --* 

      The description of the archive that was specified in the Initiate Multipart Upload request.

      

  .. py:attribute:: creation_date

    

    - *(string) --* 

      The UTC time at which the multipart upload was initiated.

      

  .. py:attribute:: multipart_upload_id

    

    - *(string) --* 

      The ID of a multipart upload.

      

  .. py:attribute:: part_size_in_bytes

    

    - *(integer) --* 

      The part size, in bytes, specified in the Initiate Multipart Upload request. This is the size of all the parts in the upload except the last part, which may be smaller than this size.

      

  .. py:attribute:: vault_arn

    

    - *(string) --* 

      The Amazon Resource Name (ARN) of the vault that contains the archive.

      
  .. rst-class:: admonition-title
  
  Actions
  
  Actions call operations on resources.  They may automatically handle the passing in of arguments set from identifiers and some attributes.
  For more information about actions refer to the :ref:`Resources Introduction Guide<actions_intro>`.
  

  .. py:method:: abort()

    

    This operation aborts a multipart upload identified by the upload ID.

     

    After the Abort Multipart Upload request succeeds, you cannot upload any more parts to the multipart upload or complete the multipart upload. Aborting a completed upload fails. However, aborting an already-aborted upload will succeed, for a short time. For more information about uploading a part and completing a multipart upload, see  UploadMultipartPart and  CompleteMultipartUpload .

     

    This operation is idempotent.

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and underlying REST API, see `Working with Archives in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-archives.html>`__ and `Abort Multipart Upload <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-abort-upload.html>`__ in the *Amazon Glacier Developer Guide* . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/AbortMultipartUpload>`_    


    **Request Syntax** 
    ::

      response = multipart_upload.abort()
      
    
    :returns: None

  .. py:method:: complete(**kwargs)

    

    You call this operation to inform Amazon Glacier that all the archive parts have been uploaded and that Amazon Glacier can now assemble the archive from the uploaded parts. After assembling and saving the archive to the vault, Amazon Glacier returns the URI path of the newly created archive resource. Using the URI path, you can then access the archive. After you upload an archive, you should save the archive ID returned to retrieve the archive at a later point. You can also get the vault inventory to obtain a list of archive IDs in a vault. For more information, see  InitiateJob .

     

    In the request, you must include the computed SHA256 tree hash of the entire archive you have uploaded. For information about computing a SHA256 tree hash, see `Computing Checksums <http://docs.aws.amazon.com/amazonglacier/latest/dev/checksum-calculations.html>`__ . On the server side, Amazon Glacier also constructs the SHA256 tree hash of the assembled archive. If the values match, Amazon Glacier saves the archive to the vault; otherwise, it returns an error, and the operation fails. The  ListParts operation returns a list of parts uploaded for a specific multipart upload. It includes checksum information for each uploaded part that can be used to debug a bad checksum issue.

     

    Additionally, Amazon Glacier also checks for any missing content ranges when assembling the archive, if missing content ranges are found, Amazon Glacier returns an error and the operation fails.

     

    Complete Multipart Upload is an idempotent operation. After your first successful complete multipart upload, if you call the operation again within a short period, the operation will succeed and return the same archive ID. This is useful in the event you experience a network issue that causes an aborted connection or receive a 500 server error, in which case you can repeat your Complete Multipart Upload request and get the same archive ID without creating duplicate archives. Note, however, that after the multipart upload completes, you cannot call the List Parts operation and the multipart upload will not appear in List Multipart Uploads response, even if idempotent complete is possible.

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and underlying REST API, see `Uploading Large Archives in Parts (Multipart Upload) <http://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-archive-mpu.html>`__ and `Complete Multipart Upload <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-complete-upload.html>`__ in the *Amazon Glacier Developer Guide* . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/CompleteMultipartUpload>`_    


    **Request Syntax** 
    ::

      response = multipart_upload.complete(
          archiveSize='string',
          checksum='string'
      )
    :type archiveSize: string
    :param archiveSize: 

      The total size, in bytes, of the entire archive. This value should be the sum of all the sizes of the individual parts that you uploaded.

      

    
    :type checksum: string
    :param checksum: 

      The SHA256 tree hash of the entire archive. It is the tree hash of SHA256 tree hash of the individual parts. If the value you specify in the request does not match the SHA256 tree hash of the final assembled archive as computed by Amazon Glacier, Amazon Glacier returns an error and the request fails.

            
        This is a required field.

        Ideally you will want to compute this value with checksums from
        previous uploaded parts, using the algorithm described in
        `Glacier documentation <http://docs.aws.amazon.com/amazonglacier/latest/dev/checksum-calculations.html>`_.

        But if you prefer, you can also use botocore.utils.calculate_tree_hash()
        to compute it from raw file by::

            checksum = calculate_tree_hash(open('your_file.txt', 'rb'))

        


    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'location': 'string',
            'checksum': 'string',
            'archiveId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the Amazon Glacier response to your request.

         

        For information about the underlying REST API, see `Upload Archive <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-post.html>`__ . For conceptual information, see `Working with Archives in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-archives.html>`__ .

        
        

        - **location** *(string) --* 

          The relative URI path of the newly added archive resource.

          
        

        - **checksum** *(string) --* 

          The checksum of the archive computed by Amazon Glacier.

          
        

        - **archiveId** *(string) --* 

          The ID of the archive. This value is also included as part of the location.

          
    

  .. py:method:: get_available_subresources()

        
    Returns a list of all the available sub-resources for this
    Resource.
    
    :returns: A list containing the name of each sub-resource for this
        resource
    :rtype: list of str


  .. py:method:: parts(**kwargs)

    

    This operation lists the parts of an archive that have been uploaded in a specific multipart upload. You can make this request at any time during an in-progress multipart upload before you complete the upload (see  CompleteMultipartUpload . List Parts returns an error for completed uploads. The list returned in the List Parts response is sorted by part range. 

     

    The List Parts operation supports pagination. By default, this operation returns up to 1,000 uploaded parts in the response. You should always check the response for a ``marker`` at which to continue the list; if there are no more items the ``marker`` is ``null`` . To return a list of parts that begins at a specific part, set the ``marker`` request parameter to the value you obtained from a previous List Parts request. You can also limit the number of parts returned in the response by specifying the ``limit`` parameter in the request. 

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and the underlying REST API, see `Working with Archives in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-archives.html>`__ and `List Parts <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-list-parts.html>`__ in the *Amazon Glacier Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListParts>`_    


    **Request Syntax** 
    ::

      response = multipart_upload.parts(
          marker='string',
          limit='string'
      )
    :type marker: string
    :param marker: 

      An opaque string used for pagination. This value specifies the part at which the listing of parts should begin. Get the marker value from the response of a previous List Parts response. You need only include the marker if you are continuing the pagination of results started in a previous List Parts request.

      

    
    :type limit: string
    :param limit: 

      The maximum number of parts to be returned. The default limit is 1000. The number of parts returned might be fewer than the specified limit, but the number of returned parts never exceeds the limit.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'MultipartUploadId': 'string',
            'VaultARN': 'string',
            'ArchiveDescription': 'string',
            'PartSizeInBytes': 123,
            'CreationDate': 'string',
            'Parts': [
                {
                    'RangeInBytes': 'string',
                    'SHA256TreeHash': 'string'
                },
            ],
            'Marker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the Amazon Glacier response to your request.

        
        

        - **MultipartUploadId** *(string) --* 

          The ID of the upload to which the parts are associated.

          
        

        - **VaultARN** *(string) --* 

          The Amazon Resource Name (ARN) of the vault to which the multipart upload was initiated.

          
        

        - **ArchiveDescription** *(string) --* 

          The description of the archive that was specified in the Initiate Multipart Upload request.

          
        

        - **PartSizeInBytes** *(integer) --* 

          The part size in bytes. This is the same value that you specified in the Initiate Multipart Upload request.

          
        

        - **CreationDate** *(string) --* 

          The UTC time at which the multipart upload was initiated.

          
        

        - **Parts** *(list) --* 

          A list of the part sizes of the multipart upload. Each object in the array contains a ``RangeBytes`` and ``sha256-tree-hash`` name/value pair.

          
          

          - *(dict) --* 

            A list of the part sizes of the multipart upload.

            
            

            - **RangeInBytes** *(string) --* 

              The byte range of a part, inclusive of the upper value of the range.

              
            

            - **SHA256TreeHash** *(string) --* 

              The SHA256 tree hash value that Amazon Glacier calculated for the part. This field is never ``null`` .

              
        
      
        

        - **Marker** *(string) --* 

          An opaque string that represents where to continue pagination of the results. You use the marker in a new List Parts request to obtain more jobs in the list. If there are no more parts, this value is ``null`` .

          
    

  .. py:method:: upload_part(**kwargs)

    

    This operation uploads a part of an archive. You can upload archive parts in any order. You can also upload them in parallel. You can upload up to 10,000 parts for a multipart upload.

     

    Amazon Glacier rejects your upload part request if any of the following conditions is true:

     

     
    * **SHA256 tree hash does not match** To ensure that part data is not corrupted in transmission, you compute a SHA256 tree hash of the part and include it in your request. Upon receiving the part data, Amazon Glacier also computes a SHA256 tree hash. If these hash values don't match, the operation fails. For information about computing a SHA256 tree hash, see `Computing Checksums <http://docs.aws.amazon.com/amazonglacier/latest/dev/checksum-calculations.html>`__ . 
     
    * **Part size does not match** The size of each part except the last must match the size specified in the corresponding  InitiateMultipartUpload request. The size of the last part must be the same size as, or smaller than, the specified size. 

    .. note::

       If you upload a part whose size is smaller than the part size you specified in your initiate multipart upload request and that part is not the last part, then the upload part request will succeed. However, the subsequent Complete Multipart Upload request will fail. 

     
     
    * **Range does not align** The byte range value in the request does not align with the part size specified in the corresponding initiate request. For example, if you specify a part size of 4194304 bytes (4 MB), then 0 to 4194303 bytes (4 MB - 1) and 4194304 (4 MB) to 8388607 (8 MB - 1) are valid part ranges. However, if you set a range value of 2 MB to 6 MB, the range does not align with the part size and the upload will fail.  
     

     

    This operation is idempotent. If you upload the same part multiple times, the data included in the most recent request overwrites the previously uploaded data.

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and underlying REST API, see `Uploading Large Archives in Parts (Multipart Upload) <http://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-archive-mpu.html>`__ and `Upload Part <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-upload-part.html>`__ in the *Amazon Glacier Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/UploadMultipartPart>`_    


    **Request Syntax** 
    ::

      response = multipart_upload.upload_part(
          range='string',
          body=b'bytes'|file
      )
    :type checksum: string
    :param checksum: 

      The SHA256 tree hash of the data being uploaded.

            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required



    
    :type range: string
    :param range: 

      Identifies the range of bytes in the assembled archive that will be uploaded in this part. Amazon Glacier uses this information to assemble the archive in the proper sequence. The format of this header follows RFC 2616. An example header is Content-Range:bytes 0-4194303/*.

      

    
    :type body: bytes or seekable file-like object
    :param body: 

      The data to upload.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'checksum': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the Amazon Glacier response to your request.

        
        

        - **checksum** *(string) --* 

          The SHA256 tree hash that Amazon Glacier computed for the uploaded part.

          
    
  .. rst-class:: admonition-title
  
  Sub-resources
  
  Sub-resources are methods that create a new instance of a child resource. This resource's identifiers get passed along to the child.
  For more information about sub-resources refer to the :ref:`Resources Introduction Guide<subresources_intro>`.
  

  .. py:method:: Vault()

    Creates a Vault resource.::

      vault = multipart_upload.Vault()

    
    :rtype: :py:class:`Glacier.Vault`
    :returns: A Vault resource
    

============
Notification
============



.. py:class:: Glacier.Notification(account_id,vault_name)

  A resource representing an Amazon Glacier Notification::

    
    import boto3
    
    glacier = boto3.resource('glacier')
    notification = glacier.Notification('account_id','vault_name')

  :type account_id: string
  :param account_id: The Notification's account_id identifier. This **must** be set.
  :type vault_name: string
  :param vault_name: The Notification's vault_name identifier. This **must** be set.
  
  These are the resource's available identifiers:
  
  *   :py:attr:`account_id`

  
  *   :py:attr:`vault_name`

  
  These are the resource's available attributes:
  
  *   :py:attr:`events`

  
  *   :py:attr:`sns_topic`

  
  These are the resource's available actions:
  
  *   :py:meth:`delete()`

  
  *   :py:meth:`get_available_subresources()`

  
  *   :py:meth:`load()`

  
  *   :py:meth:`reload()`

  
  *   :py:meth:`set()`

  
  These are the resource's available sub-resources:
  
  *   :py:meth:`Vault()`

  
  .. rst-class:: admonition-title
  
  Identifiers
  
  Identifiers are properties of a resource that are set upon instantation of the resource.
  For more information about identifiers refer to the :ref:`Resources Introduction Guide<identifiers_attributes_intro>`.
  

  .. py:attribute:: account_id

    *(string)* The Notification's account_id identifier. This **must** be set.

  .. py:attribute:: vault_name

    *(string)* The Notification's vault_name identifier. This **must** be set.
  .. rst-class:: admonition-title
  
  Attributes
  
  Attributes provide access to the properties of a resource. Attributes are lazy-loaded the first time one is accessed via the :py:meth:`load` method.
  For more information about attributes refer to the :ref:`Resources Introduction Guide<identifiers_attributes_intro>`.
  

  .. py:attribute:: events

    

    - *(list) --* 

      A list of one or more events for which Amazon Glacier will send a notification to the specified Amazon SNS topic.

      
      

      - *(string) --* 
  

  .. py:attribute:: sns_topic

    

    - *(string) --* 

      The Amazon Simple Notification Service (Amazon SNS) topic Amazon Resource Name (ARN).

      
  .. rst-class:: admonition-title
  
  Actions
  
  Actions call operations on resources.  They may automatically handle the passing in of arguments set from identifiers and some attributes.
  For more information about actions refer to the :ref:`Resources Introduction Guide<actions_intro>`.
  

  .. py:method:: delete()

    

    This operation deletes the notification configuration set for a vault. The operation is eventually consistent; that is, it might take some time for Amazon Glacier to completely disable the notifications and you might still receive some notifications for a short time after you send the delete request.

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and underlying REST API, see `Configuring Vault Notifications in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/configuring-notifications.html>`__ and `Delete Vault Notification Configuration <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-notifications-delete.html>`__ in the Amazon Glacier Developer Guide. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/DeleteVaultNotifications>`_    


    **Request Syntax** 
    ::

      response = notification.delete()
      
    
    :returns: None

  .. py:method:: get_available_subresources()

        
    Returns a list of all the available sub-resources for this
    Resource.
    
    :returns: A list containing the name of each sub-resource for this
        resource
    :rtype: list of str


  .. py:method:: load()

    Calls :py:meth:`Glacier.Client.get_vault_notifications` to update the attributes of the Notification resource. Note that the load and reload methods are the same method and can be used interchangeably.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/None>`_    


    **Request Syntax** 

    ::

      notification.load()
    :returns: None

  .. py:method:: reload()

    Calls :py:meth:`Glacier.Client.get_vault_notifications` to update the attributes of the Notification resource. Note that the load and reload methods are the same method and can be used interchangeably.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/None>`_    


    **Request Syntax** 

    ::

      notification.reload()
    :returns: None

  .. py:method:: set(**kwargs)

    

    This operation configures notifications that will be sent when specific events happen to a vault. By default, you don't get any notifications.

     

    To configure vault notifications, send a PUT request to the ``notification-configuration`` subresource of the vault. The request should include a JSON document that provides an Amazon SNS topic and specific events for which you want Amazon Glacier to send notifications to the topic.

     

    Amazon SNS topics must grant permission to the vault to be allowed to publish notifications to the topic. You can configure a vault to publish a notification for the following vault events:

     

     
    * **ArchiveRetrievalCompleted** This event occurs when a job that was initiated for an archive retrieval is completed ( InitiateJob ). The status of the completed job can be "Succeeded" or "Failed". The notification sent to the SNS topic is the same output as returned from  DescribeJob .  
     
    * **InventoryRetrievalCompleted** This event occurs when a job that was initiated for an inventory retrieval is completed ( InitiateJob ). The status of the completed job can be "Succeeded" or "Failed". The notification sent to the SNS topic is the same output as returned from  DescribeJob .  
     

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and underlying REST API, see `Configuring Vault Notifications in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/configuring-notifications.html>`__ and `Set Vault Notification Configuration <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-notifications-put.html>`__ in the *Amazon Glacier Developer Guide* . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/SetVaultNotifications>`_    


    **Request Syntax** 
    ::

      response = notification.set(
          vaultNotificationConfig={
              'SNSTopic': 'string',
              'Events': [
                  'string',
              ]
          }
      )
    :type vaultNotificationConfig: dict
    :param vaultNotificationConfig: 

      Provides options for specifying notification configuration.

      

    
      - **SNSTopic** *(string) --* 

        The Amazon Simple Notification Service (Amazon SNS) topic Amazon Resource Name (ARN).

        

      
      - **Events** *(list) --* 

        A list of one or more events for which Amazon Glacier will send a notification to the specified Amazon SNS topic.

        

      
        - *(string) --* 

        
    
    
    
    :returns: None
  .. rst-class:: admonition-title
  
  Sub-resources
  
  Sub-resources are methods that create a new instance of a child resource. This resource's identifiers get passed along to the child.
  For more information about sub-resources refer to the :ref:`Resources Introduction Guide<subresources_intro>`.
  

  .. py:method:: Vault()

    Creates a Vault resource.::

      vault = notification.Vault()

    
    :rtype: :py:class:`Glacier.Vault`
    :returns: A Vault resource
    

=====
Vault
=====



.. py:class:: Glacier.Vault(account_id,name)

  A resource representing an Amazon Glacier Vault::

    
    import boto3
    
    glacier = boto3.resource('glacier')
    vault = glacier.Vault('account_id','name')

  :type account_id: string
  :param account_id: The Vault's account_id identifier. This **must** be set.
  :type name: string
  :param name: The Vault's name identifier. This **must** be set.
  
  These are the resource's available identifiers:
  
  *   :py:attr:`account_id`

  
  *   :py:attr:`name`

  
  These are the resource's available attributes:
  
  *   :py:attr:`creation_date`

  
  *   :py:attr:`last_inventory_date`

  
  *   :py:attr:`number_of_archives`

  
  *   :py:attr:`size_in_bytes`

  
  *   :py:attr:`vault_arn`

  
  *   :py:attr:`vault_name`

  
  These are the resource's available actions:
  
  *   :py:meth:`create()`

  
  *   :py:meth:`delete()`

  
  *   :py:meth:`get_available_subresources()`

  
  *   :py:meth:`initiate_inventory_retrieval()`

  
  *   :py:meth:`initiate_multipart_upload()`

  
  *   :py:meth:`load()`

  
  *   :py:meth:`reload()`

  
  *   :py:meth:`upload_archive()`

  
  These are the resource's available sub-resources:
  
  *   :py:meth:`Account()`

  
  *   :py:meth:`Archive()`

  
  *   :py:meth:`Job()`

  
  *   :py:meth:`MultipartUpload()`

  
  *   :py:meth:`Notification()`

  
  These are the resource's available collections:
  
  *   :py:attr:`completed_jobs`

  
  *   :py:attr:`failed_jobs`

  
  *   :py:attr:`jobs`

  
  *   :py:attr:`jobs_in_progress`

  
  *   :py:attr:`multipart_uplaods`

  
  *   :py:attr:`multipart_uploads`

  
  *   :py:attr:`succeeded_jobs`

  
  .. rst-class:: admonition-title
  
  Identifiers
  
  Identifiers are properties of a resource that are set upon instantation of the resource.
  For more information about identifiers refer to the :ref:`Resources Introduction Guide<identifiers_attributes_intro>`.
  

  .. py:attribute:: account_id

    *(string)* The Vault's account_id identifier. This **must** be set.

  .. py:attribute:: name

    *(string)* The Vault's name identifier. This **must** be set.
  .. rst-class:: admonition-title
  
  Attributes
  
  Attributes provide access to the properties of a resource. Attributes are lazy-loaded the first time one is accessed via the :py:meth:`load` method.
  For more information about attributes refer to the :ref:`Resources Introduction Guide<identifiers_attributes_intro>`.
  

  .. py:attribute:: creation_date

    

    - *(string) --* 

      The Universal Coordinated Time (UTC) date when the vault was created. This value should be a string in the ISO 8601 date format, for example ``2012-03-20T17:03:43.221Z`` .

      

  .. py:attribute:: last_inventory_date

    

    - *(string) --* 

      The Universal Coordinated Time (UTC) date when Amazon Glacier completed the last vault inventory. This value should be a string in the ISO 8601 date format, for example ``2012-03-20T17:03:43.221Z`` .

      

  .. py:attribute:: number_of_archives

    

    - *(integer) --* 

      The number of archives in the vault as of the last inventory date. This field will return ``null`` if an inventory has not yet run on the vault, for example if you just created the vault.

      

  .. py:attribute:: size_in_bytes

    

    - *(integer) --* 

      Total size, in bytes, of the archives in the vault as of the last inventory date. This field will return null if an inventory has not yet run on the vault, for example if you just created the vault.

      

  .. py:attribute:: vault_arn

    

    - *(string) --* 

      The Amazon Resource Name (ARN) of the vault.

      

  .. py:attribute:: vault_name

    

    - *(string) --* 

      The name of the vault.

      
  .. rst-class:: admonition-title
  
  Actions
  
  Actions call operations on resources.  They may automatically handle the passing in of arguments set from identifiers and some attributes.
  For more information about actions refer to the :ref:`Resources Introduction Guide<actions_intro>`.
  

  .. py:method:: create()

    

    This operation creates a new vault with the specified name. The name of the vault must be unique within a region for an AWS account. You can create up to 1,000 vaults per account. If you need to create more vaults, contact Amazon Glacier.

     

    You must use the following guidelines when naming a vault.

     

     
    * Names can be between 1 and 255 characters long. 
     
    * Allowed characters are a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), and '.' (period). 
     

     

    This operation is idempotent.

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and underlying REST API, see `Creating a Vault in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/creating-vaults.html>`__ and `Create Vault <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-put.html>`__ in the *Amazon Glacier Developer Guide* . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/CreateVault>`_    


    **Request Syntax** 
    ::

      response = vault.create()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'location': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains the Amazon Glacier response to your request.

        
        

        - **location** *(string) --* 

          The URI of the vault that was created.

          
    

  .. py:method:: delete()

    

    This operation deletes a vault. Amazon Glacier will delete a vault only if there are no archives in the vault as of the last inventory and there have been no writes to the vault since the last inventory. If either of these conditions is not satisfied, the vault deletion fails (that is, the vault is not removed) and Amazon Glacier returns an error. You can use  DescribeVault to return the number of archives in a vault, and you can use `Initiate a Job (POST jobs) <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html>`__ to initiate a new inventory retrieval for a vault. The inventory contains the archive IDs you use to delete archives using `Delete Archive (DELETE archive) <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-delete.html>`__ .

     

    This operation is idempotent.

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and underlying REST API, see `Deleting a Vault in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-vaults.html>`__ and `Delete Vault <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-delete.html>`__ in the *Amazon Glacier Developer Guide* . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/DeleteVault>`_    


    **Request Syntax** 
    ::

      response = vault.delete()
      
    
    :returns: None

  .. py:method:: get_available_subresources()

        
    Returns a list of all the available sub-resources for this
    Resource.
    
    :returns: A list containing the name of each sub-resource for this
        resource
    :rtype: list of str


  .. py:method:: initiate_inventory_retrieval()

    

    This operation initiates a job of the specified type, which can be a select, an archival retrieval, or a vault retrieval. For more information about using this operation, see the documentation for the underlying REST API `Initiate a Job <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html>`__ . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/InitiateJob>`_    


    **Request Syntax** 
    ::

      job = vault.initiate_inventory_retrieval()
      
    
    :rtype: :py:class:`glacier.Job`
    :returns: Job resource
    

  .. py:method:: initiate_multipart_upload(**kwargs)

    

    This operation initiates a multipart upload. Amazon Glacier creates a multipart upload resource and returns its ID in the response. The multipart upload ID is used in subsequent requests to upload parts of an archive (see  UploadMultipartPart ).

     

    When you initiate a multipart upload, you specify the part size in number of bytes. The part size must be a megabyte (1024 KB) multiplied by a power of 2-for example, 1048576 (1 MB), 2097152 (2 MB), 4194304 (4 MB), 8388608 (8 MB), and so on. The minimum allowable part size is 1 MB, and the maximum is 4 GB.

     

    Every part you upload to this resource (see  UploadMultipartPart ), except the last one, must have the same size. The last one can be the same size or smaller. For example, suppose you want to upload a 16.2 MB file. If you initiate the multipart upload with a part size of 4 MB, you will upload four parts of 4 MB each and one part of 0.2 MB. 

     

    .. note::

       

      You don't need to know the size of the archive when you start a multipart upload because Amazon Glacier does not require you to specify the overall archive size.

       

     

    After you complete the multipart upload, Amazon Glacier removes the multipart upload resource referenced by the ID. Amazon Glacier also removes the multipart upload resource if you cancel the multipart upload or it may be removed if there is no activity for a period of 24 hours.

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and underlying REST API, see `Uploading Large Archives in Parts (Multipart Upload) <http://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-archive-mpu.html>`__ and `Initiate Multipart Upload <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-initiate-upload.html>`__ in the *Amazon Glacier Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/InitiateMultipartUpload>`_    


    **Request Syntax** 
    ::

      multipart_upload = vault.initiate_multipart_upload(
          archiveDescription='string',
          partSize='string'
      )
    :type archiveDescription: string
    :param archiveDescription: 

      The archive description that you are uploading in parts.

       

      The part size must be a megabyte (1024 KB) multiplied by a power of 2, for example 1048576 (1 MB), 2097152 (2 MB), 4194304 (4 MB), 8388608 (8 MB), and so on. The minimum allowable part size is 1 MB, and the maximum is 4 GB (4096 MB).

      

    
    :type partSize: string
    :param partSize: 

      The size of each part except the last, in bytes. The last part can be smaller than this part size.

      

    
    
    :rtype: :py:class:`glacier.MultipartUpload`
    :returns: MultipartUpload resource
    

  .. py:method:: load()

    Calls :py:meth:`Glacier.Client.describe_vault` to update the attributes of the Vault resource. Note that the load and reload methods are the same method and can be used interchangeably.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/None>`_    


    **Request Syntax** 

    ::

      vault.load()
    :returns: None

  .. py:method:: reload()

    Calls :py:meth:`Glacier.Client.describe_vault` to update the attributes of the Vault resource. Note that the load and reload methods are the same method and can be used interchangeably.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/None>`_    


    **Request Syntax** 

    ::

      vault.reload()
    :returns: None

  .. py:method:: upload_archive(**kwargs)

    

    This operation adds an archive to a vault. This is a synchronous operation, and for a successful upload, your data is durably persisted. Amazon Glacier returns the archive ID in the ``x-amz-archive-id`` header of the response. 

     

    You must use the archive ID to access your data in Amazon Glacier. After you upload an archive, you should save the archive ID returned so that you can retrieve or delete the archive later. Besides saving the archive ID, you can also index it and give it a friendly name to allow for better searching. You can also use the optional archive description field to specify how the archive is referred to in an external index of archives, such as you might create in Amazon DynamoDB. You can also get the vault inventory to obtain a list of archive IDs in a vault. For more information, see  InitiateJob . 

     

    You must provide a SHA256 tree hash of the data you are uploading. For information about computing a SHA256 tree hash, see `Computing Checksums <http://docs.aws.amazon.com/amazonglacier/latest/dev/checksum-calculations.html>`__ . 

     

    You can optionally specify an archive description of up to 1,024 printable ASCII characters. You can get the archive description when you either retrieve the archive or get the vault inventory. For more information, see  InitiateJob . Amazon Glacier does not interpret the description in any way. An archive description does not need to be unique. You cannot use the description to retrieve or sort the archive list. 

     

    Archives are immutable. After you upload an archive, you cannot edit the archive or its description.

     

    An AWS account has full permission to perform all operations (actions). However, AWS Identity and Access Management (IAM) users don't have any permissions by default. You must grant them explicit permission to perform specific actions. For more information, see `Access Control Using AWS Identity and Access Management (IAM) <http://docs.aws.amazon.com/amazonglacier/latest/dev/using-iam-with-amazon-glacier.html>`__ .

     

    For conceptual information and underlying REST API, see `Uploading an Archive in Amazon Glacier <http://docs.aws.amazon.com/amazonglacier/latest/dev/uploading-an-archive.html>`__ and `Upload Archive <http://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-post.html>`__ in the *Amazon Glacier Developer Guide* . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/UploadArchive>`_    


    **Request Syntax** 
    ::

      archive = vault.upload_archive(
          archiveDescription='string',
          body=b'bytes'|file
      )
    :type archiveDescription: string
    :param archiveDescription: 

      The optional description of the archive you are uploading.

      

    
    :type checksum: string
    :param checksum: 

      The SHA256 tree hash of the data being uploaded.

            Please note that this parameter is automatically populated if it is not provided. Including this parameter is not required



    
    :type body: bytes or seekable file-like object
    :param body: 

      The data to upload.

      

    
    
    :rtype: :py:class:`glacier.Archive`
    :returns: Archive resource
    
  .. rst-class:: admonition-title
  
  Sub-resources
  
  Sub-resources are methods that create a new instance of a child resource. This resource's identifiers get passed along to the child.
  For more information about sub-resources refer to the :ref:`Resources Introduction Guide<subresources_intro>`.
  

  .. py:method:: Account()

    Creates a Account resource.::

      account = vault.Account()

    
    :rtype: :py:class:`Glacier.Account`
    :returns: A Account resource
    

  .. py:method:: Archive(id)

    Creates a Archive resource.::

      archive = vault.Archive('id')

    :type id: string
    :param id: The Archive's id identifier. This **must** be set.
    
    :rtype: :py:class:`Glacier.Archive`
    :returns: A Archive resource
    

  .. py:method:: Job(id)

    Creates a Job resource.::

      job = vault.Job('id')

    :type id: string
    :param id: The Job's id identifier. This **must** be set.
    
    :rtype: :py:class:`Glacier.Job`
    :returns: A Job resource
    

  .. py:method:: MultipartUpload(id)

    Creates a MultipartUpload resource.::

      multipart_upload = vault.MultipartUpload('id')

    :type id: string
    :param id: The MultipartUpload's id identifier. This **must** be set.
    
    :rtype: :py:class:`Glacier.MultipartUpload`
    :returns: A MultipartUpload resource
    

  .. py:method:: Notification()

    Creates a Notification resource.::

      notification = vault.Notification()

    
    :rtype: :py:class:`Glacier.Notification`
    :returns: A Notification resource
    
  .. rst-class:: admonition-title
  
  Collections
  
  Collections provide an interface to iterate over and manipulate groups of resources. 
  For more information about collections refer to the :ref:`Resources Introduction Guide<guide_collections>`.
  

  .. py:attribute:: completed_jobs

    A collection of Job resources

    .. py:method:: all()

      Creates an iterable of all Job resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListJobs>`_      


      **Request Syntax** 
      ::

        job_iterator = vault.completed_jobs.all()
        
      
      :rtype: list(:py:class:`glacier.Job`)
      :returns: A list of Job resources
      

    .. py:method:: filter(**kwargs)

      Creates an iterable of all Job resources in the collection filtered by kwargs passed to method.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListJobs>`_      


      **Request Syntax** 
      ::

        job_iterator = vault.completed_jobs.filter(
            limit='string',
            marker='string',
            statuscode='string',
            
        )
      :type limit: string
      :param limit: 

        The maximum number of jobs to be returned. The default limit is 1000. The number of jobs returned might be fewer than the specified limit, but the number of returned jobs never exceeds the limit.

        

      
      :type marker: string
      :param marker: 

        An opaque string used for pagination. This value specifies the job at which the listing of jobs should begin. Get the marker value from a previous List Jobs response. You only need to include the marker if you are continuing the pagination of results started in a previous List Jobs request.

        

      
      :type statuscode: string
      :param statuscode: 

        The type of job status to return. You can specify the following values: ``InProgress`` , ``Succeeded`` , or ``Failed`` .

        

      
      
      :rtype: list(:py:class:`glacier.Job`)
      :returns: A list of Job resources
      

    .. py:method:: limit(**kwargs)

      Creates an iterable up to a specified amount of Job resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListJobs>`_      


      **Request Syntax** 
      ::

        job_iterator = vault.completed_jobs.limit(
            count=123
        )
      :type count: integer
      :param count: The limit to the number of resources in the iterable.

      
      
      :rtype: list(:py:class:`glacier.Job`)
      :returns: A list of Job resources
      

    .. py:method:: page_size(**kwargs)

      Creates an iterable of all Job resources in the collection, but limits the number of items returned by each service call by the specified amount.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListJobs>`_      


      **Request Syntax** 
      ::

        job_iterator = vault.completed_jobs.page_size(
            count=123
        )
      :type count: integer
      :param count: The number of items returned by each service call

      
      
      :rtype: list(:py:class:`glacier.Job`)
      :returns: A list of Job resources
      

  .. py:attribute:: failed_jobs

    A collection of Job resources

    .. py:method:: all()

      Creates an iterable of all Job resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListJobs>`_      


      **Request Syntax** 
      ::

        job_iterator = vault.failed_jobs.all()
        
      
      :rtype: list(:py:class:`glacier.Job`)
      :returns: A list of Job resources
      

    .. py:method:: filter(**kwargs)

      Creates an iterable of all Job resources in the collection filtered by kwargs passed to method.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListJobs>`_      


      **Request Syntax** 
      ::

        job_iterator = vault.failed_jobs.filter(
            limit='string',
            marker='string',
            completed='string'
        )
      :type limit: string
      :param limit: 

        The maximum number of jobs to be returned. The default limit is 1000. The number of jobs returned might be fewer than the specified limit, but the number of returned jobs never exceeds the limit.

        

      
      :type marker: string
      :param marker: 

        An opaque string used for pagination. This value specifies the job at which the listing of jobs should begin. Get the marker value from a previous List Jobs response. You only need to include the marker if you are continuing the pagination of results started in a previous List Jobs request.

        

      
      :type completed: string
      :param completed: 

        The state of the jobs to return. You can specify ``true`` or ``false`` .

        

      
      
      :rtype: list(:py:class:`glacier.Job`)
      :returns: A list of Job resources
      

    .. py:method:: limit(**kwargs)

      Creates an iterable up to a specified amount of Job resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListJobs>`_      


      **Request Syntax** 
      ::

        job_iterator = vault.failed_jobs.limit(
            count=123
        )
      :type count: integer
      :param count: The limit to the number of resources in the iterable.

      
      
      :rtype: list(:py:class:`glacier.Job`)
      :returns: A list of Job resources
      

    .. py:method:: page_size(**kwargs)

      Creates an iterable of all Job resources in the collection, but limits the number of items returned by each service call by the specified amount.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListJobs>`_      


      **Request Syntax** 
      ::

        job_iterator = vault.failed_jobs.page_size(
            count=123
        )
      :type count: integer
      :param count: The number of items returned by each service call

      
      
      :rtype: list(:py:class:`glacier.Job`)
      :returns: A list of Job resources
      

  .. py:attribute:: jobs

    A collection of Job resources

    .. py:method:: all()

      Creates an iterable of all Job resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListJobs>`_      


      **Request Syntax** 
      ::

        job_iterator = vault.jobs.all()
        
      
      :rtype: list(:py:class:`glacier.Job`)
      :returns: A list of Job resources
      

    .. py:method:: filter(**kwargs)

      Creates an iterable of all Job resources in the collection filtered by kwargs passed to method.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListJobs>`_      


      **Request Syntax** 
      ::

        job_iterator = vault.jobs.filter(
            limit='string',
            marker='string',
            statuscode='string',
            completed='string'
        )
      :type limit: string
      :param limit: 

        The maximum number of jobs to be returned. The default limit is 1000. The number of jobs returned might be fewer than the specified limit, but the number of returned jobs never exceeds the limit.

        

      
      :type marker: string
      :param marker: 

        An opaque string used for pagination. This value specifies the job at which the listing of jobs should begin. Get the marker value from a previous List Jobs response. You only need to include the marker if you are continuing the pagination of results started in a previous List Jobs request.

        

      
      :type statuscode: string
      :param statuscode: 

        The type of job status to return. You can specify the following values: ``InProgress`` , ``Succeeded`` , or ``Failed`` .

        

      
      :type completed: string
      :param completed: 

        The state of the jobs to return. You can specify ``true`` or ``false`` .

        

      
      
      :rtype: list(:py:class:`glacier.Job`)
      :returns: A list of Job resources
      

    .. py:method:: limit(**kwargs)

      Creates an iterable up to a specified amount of Job resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListJobs>`_      


      **Request Syntax** 
      ::

        job_iterator = vault.jobs.limit(
            count=123
        )
      :type count: integer
      :param count: The limit to the number of resources in the iterable.

      
      
      :rtype: list(:py:class:`glacier.Job`)
      :returns: A list of Job resources
      

    .. py:method:: page_size(**kwargs)

      Creates an iterable of all Job resources in the collection, but limits the number of items returned by each service call by the specified amount.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListJobs>`_      


      **Request Syntax** 
      ::

        job_iterator = vault.jobs.page_size(
            count=123
        )
      :type count: integer
      :param count: The number of items returned by each service call

      
      
      :rtype: list(:py:class:`glacier.Job`)
      :returns: A list of Job resources
      

  .. py:attribute:: jobs_in_progress

    A collection of Job resources

    .. py:method:: all()

      Creates an iterable of all Job resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListJobs>`_      


      **Request Syntax** 
      ::

        job_iterator = vault.jobs_in_progress.all()
        
      
      :rtype: list(:py:class:`glacier.Job`)
      :returns: A list of Job resources
      

    .. py:method:: filter(**kwargs)

      Creates an iterable of all Job resources in the collection filtered by kwargs passed to method.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListJobs>`_      


      **Request Syntax** 
      ::

        job_iterator = vault.jobs_in_progress.filter(
            limit='string',
            marker='string',
            completed='string'
        )
      :type limit: string
      :param limit: 

        The maximum number of jobs to be returned. The default limit is 1000. The number of jobs returned might be fewer than the specified limit, but the number of returned jobs never exceeds the limit.

        

      
      :type marker: string
      :param marker: 

        An opaque string used for pagination. This value specifies the job at which the listing of jobs should begin. Get the marker value from a previous List Jobs response. You only need to include the marker if you are continuing the pagination of results started in a previous List Jobs request.

        

      
      :type completed: string
      :param completed: 

        The state of the jobs to return. You can specify ``true`` or ``false`` .

        

      
      
      :rtype: list(:py:class:`glacier.Job`)
      :returns: A list of Job resources
      

    .. py:method:: limit(**kwargs)

      Creates an iterable up to a specified amount of Job resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListJobs>`_      


      **Request Syntax** 
      ::

        job_iterator = vault.jobs_in_progress.limit(
            count=123
        )
      :type count: integer
      :param count: The limit to the number of resources in the iterable.

      
      
      :rtype: list(:py:class:`glacier.Job`)
      :returns: A list of Job resources
      

    .. py:method:: page_size(**kwargs)

      Creates an iterable of all Job resources in the collection, but limits the number of items returned by each service call by the specified amount.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListJobs>`_      


      **Request Syntax** 
      ::

        job_iterator = vault.jobs_in_progress.page_size(
            count=123
        )
      :type count: integer
      :param count: The number of items returned by each service call

      
      
      :rtype: list(:py:class:`glacier.Job`)
      :returns: A list of Job resources
      

  .. py:attribute:: multipart_uplaods

    A collection of MultipartUpload resources

    .. py:method:: all()

      Creates an iterable of all MultipartUpload resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListMultipartUploads>`_      


      **Request Syntax** 
      ::

        multipart_upload_iterator = vault.multipart_uplaods.all()
        
      
      :rtype: list(:py:class:`glacier.MultipartUpload`)
      :returns: A list of MultipartUpload resources
      

    .. py:method:: filter(**kwargs)

      Creates an iterable of all MultipartUpload resources in the collection filtered by kwargs passed to method.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListMultipartUploads>`_      


      **Request Syntax** 
      ::

        multipart_upload_iterator = vault.multipart_uplaods.filter(
            marker='string',
            limit='string'
        )
      :type marker: string
      :param marker: 

        An opaque string used for pagination. This value specifies the upload at which the listing of uploads should begin. Get the marker value from a previous List Uploads response. You need only include the marker if you are continuing the pagination of results started in a previous List Uploads request.

        

      
      :type limit: string
      :param limit: 

        Specifies the maximum number of uploads returned in the response body. If this value is not specified, the List Uploads operation returns up to 1,000 uploads.

        

      
      
      :rtype: list(:py:class:`glacier.MultipartUpload`)
      :returns: A list of MultipartUpload resources
      

    .. py:method:: limit(**kwargs)

      Creates an iterable up to a specified amount of MultipartUpload resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListMultipartUploads>`_      


      **Request Syntax** 
      ::

        multipart_upload_iterator = vault.multipart_uplaods.limit(
            count=123
        )
      :type count: integer
      :param count: The limit to the number of resources in the iterable.

      
      
      :rtype: list(:py:class:`glacier.MultipartUpload`)
      :returns: A list of MultipartUpload resources
      

    .. py:method:: page_size(**kwargs)

      Creates an iterable of all MultipartUpload resources in the collection, but limits the number of items returned by each service call by the specified amount.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListMultipartUploads>`_      


      **Request Syntax** 
      ::

        multipart_upload_iterator = vault.multipart_uplaods.page_size(
            count=123
        )
      :type count: integer
      :param count: The number of items returned by each service call

      
      
      :rtype: list(:py:class:`glacier.MultipartUpload`)
      :returns: A list of MultipartUpload resources
      

  .. py:attribute:: multipart_uploads

    A collection of MultipartUpload resources

    .. py:method:: all()

      Creates an iterable of all MultipartUpload resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListMultipartUploads>`_      


      **Request Syntax** 
      ::

        multipart_upload_iterator = vault.multipart_uploads.all()
        
      
      :rtype: list(:py:class:`glacier.MultipartUpload`)
      :returns: A list of MultipartUpload resources
      

    .. py:method:: filter(**kwargs)

      Creates an iterable of all MultipartUpload resources in the collection filtered by kwargs passed to method.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListMultipartUploads>`_      


      **Request Syntax** 
      ::

        multipart_upload_iterator = vault.multipart_uploads.filter(
            marker='string',
            limit='string'
        )
      :type marker: string
      :param marker: 

        An opaque string used for pagination. This value specifies the upload at which the listing of uploads should begin. Get the marker value from a previous List Uploads response. You need only include the marker if you are continuing the pagination of results started in a previous List Uploads request.

        

      
      :type limit: string
      :param limit: 

        Specifies the maximum number of uploads returned in the response body. If this value is not specified, the List Uploads operation returns up to 1,000 uploads.

        

      
      
      :rtype: list(:py:class:`glacier.MultipartUpload`)
      :returns: A list of MultipartUpload resources
      

    .. py:method:: limit(**kwargs)

      Creates an iterable up to a specified amount of MultipartUpload resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListMultipartUploads>`_      


      **Request Syntax** 
      ::

        multipart_upload_iterator = vault.multipart_uploads.limit(
            count=123
        )
      :type count: integer
      :param count: The limit to the number of resources in the iterable.

      
      
      :rtype: list(:py:class:`glacier.MultipartUpload`)
      :returns: A list of MultipartUpload resources
      

    .. py:method:: page_size(**kwargs)

      Creates an iterable of all MultipartUpload resources in the collection, but limits the number of items returned by each service call by the specified amount.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListMultipartUploads>`_      


      **Request Syntax** 
      ::

        multipart_upload_iterator = vault.multipart_uploads.page_size(
            count=123
        )
      :type count: integer
      :param count: The number of items returned by each service call

      
      
      :rtype: list(:py:class:`glacier.MultipartUpload`)
      :returns: A list of MultipartUpload resources
      

  .. py:attribute:: succeeded_jobs

    A collection of Job resources

    .. py:method:: all()

      Creates an iterable of all Job resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListJobs>`_      


      **Request Syntax** 
      ::

        job_iterator = vault.succeeded_jobs.all()
        
      
      :rtype: list(:py:class:`glacier.Job`)
      :returns: A list of Job resources
      

    .. py:method:: filter(**kwargs)

      Creates an iterable of all Job resources in the collection filtered by kwargs passed to method.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListJobs>`_      


      **Request Syntax** 
      ::

        job_iterator = vault.succeeded_jobs.filter(
            limit='string',
            marker='string',
            completed='string'
        )
      :type limit: string
      :param limit: 

        The maximum number of jobs to be returned. The default limit is 1000. The number of jobs returned might be fewer than the specified limit, but the number of returned jobs never exceeds the limit.

        

      
      :type marker: string
      :param marker: 

        An opaque string used for pagination. This value specifies the job at which the listing of jobs should begin. Get the marker value from a previous List Jobs response. You only need to include the marker if you are continuing the pagination of results started in a previous List Jobs request.

        

      
      :type completed: string
      :param completed: 

        The state of the jobs to return. You can specify ``true`` or ``false`` .

        

      
      
      :rtype: list(:py:class:`glacier.Job`)
      :returns: A list of Job resources
      

    .. py:method:: limit(**kwargs)

      Creates an iterable up to a specified amount of Job resources in the collection.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListJobs>`_      


      **Request Syntax** 
      ::

        job_iterator = vault.succeeded_jobs.limit(
            count=123
        )
      :type count: integer
      :param count: The limit to the number of resources in the iterable.

      
      
      :rtype: list(:py:class:`glacier.Job`)
      :returns: A list of Job resources
      

    .. py:method:: page_size(**kwargs)

      Creates an iterable of all Job resources in the collection, but limits the number of items returned by each service call by the specified amount.

      See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/glacier-2012-06-01/ListJobs>`_      


      **Request Syntax** 
      ::

        job_iterator = vault.succeeded_jobs.page_size(
            count=123
        )
      :type count: integer
      :param count: The number of items returned by each service call

      
      
      :rtype: list(:py:class:`glacier.Job`)
      :returns: A list of Job resources
      