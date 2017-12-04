

*********
GuardDuty
*********

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: GuardDuty.Client

  A low-level client representing Amazon GuardDuty::

    
    import boto3
    
    client = boto3.client('guardduty')

  
  These are the available methods:
  
  *   :py:meth:`~GuardDuty.Client.accept_invitation`

  
  *   :py:meth:`~GuardDuty.Client.archive_findings`

  
  *   :py:meth:`~GuardDuty.Client.can_paginate`

  
  *   :py:meth:`~GuardDuty.Client.create_detector`

  
  *   :py:meth:`~GuardDuty.Client.create_ip_set`

  
  *   :py:meth:`~GuardDuty.Client.create_members`

  
  *   :py:meth:`~GuardDuty.Client.create_sample_findings`

  
  *   :py:meth:`~GuardDuty.Client.create_threat_intel_set`

  
  *   :py:meth:`~GuardDuty.Client.decline_invitations`

  
  *   :py:meth:`~GuardDuty.Client.delete_detector`

  
  *   :py:meth:`~GuardDuty.Client.delete_invitations`

  
  *   :py:meth:`~GuardDuty.Client.delete_ip_set`

  
  *   :py:meth:`~GuardDuty.Client.delete_members`

  
  *   :py:meth:`~GuardDuty.Client.delete_threat_intel_set`

  
  *   :py:meth:`~GuardDuty.Client.disassociate_from_master_account`

  
  *   :py:meth:`~GuardDuty.Client.disassociate_members`

  
  *   :py:meth:`~GuardDuty.Client.generate_presigned_url`

  
  *   :py:meth:`~GuardDuty.Client.get_detector`

  
  *   :py:meth:`~GuardDuty.Client.get_findings`

  
  *   :py:meth:`~GuardDuty.Client.get_findings_statistics`

  
  *   :py:meth:`~GuardDuty.Client.get_invitations_count`

  
  *   :py:meth:`~GuardDuty.Client.get_ip_set`

  
  *   :py:meth:`~GuardDuty.Client.get_master_account`

  
  *   :py:meth:`~GuardDuty.Client.get_members`

  
  *   :py:meth:`~GuardDuty.Client.get_paginator`

  
  *   :py:meth:`~GuardDuty.Client.get_threat_intel_set`

  
  *   :py:meth:`~GuardDuty.Client.get_waiter`

  
  *   :py:meth:`~GuardDuty.Client.invite_members`

  
  *   :py:meth:`~GuardDuty.Client.list_detectors`

  
  *   :py:meth:`~GuardDuty.Client.list_findings`

  
  *   :py:meth:`~GuardDuty.Client.list_invitations`

  
  *   :py:meth:`~GuardDuty.Client.list_ip_sets`

  
  *   :py:meth:`~GuardDuty.Client.list_members`

  
  *   :py:meth:`~GuardDuty.Client.list_threat_intel_sets`

  
  *   :py:meth:`~GuardDuty.Client.start_monitoring_members`

  
  *   :py:meth:`~GuardDuty.Client.stop_monitoring_members`

  
  *   :py:meth:`~GuardDuty.Client.unarchive_findings`

  
  *   :py:meth:`~GuardDuty.Client.update_detector`

  
  *   :py:meth:`~GuardDuty.Client.update_findings_feedback`

  
  *   :py:meth:`~GuardDuty.Client.update_ip_set`

  
  *   :py:meth:`~GuardDuty.Client.update_threat_intel_set`

  

  .. py:method:: accept_invitation(**kwargs)

    Accepts the invitation to be monitored by a master GuardDuty account.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/AcceptInvitation>`_    


    **Request Syntax** 
    ::

      response = client.accept_invitation(
          DetectorId='string',
          InvitationId='string',
          MasterId='string'
      )
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The unique ID of the detector of the GuardDuty member account.

    
    :type InvitationId: string
    :param InvitationId: This value is used to validate the master account to the member account.

    
    :type MasterId: string
    :param MasterId: The account ID of the master GuardDuty account whose invitation you're accepting.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 200 response
    

  .. py:method:: archive_findings(**kwargs)

    Archives Amazon GuardDuty findings specified by the list of finding IDs.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ArchiveFindings>`_    


    **Request Syntax** 
    ::

      response = client.archive_findings(
          DetectorId='string',
          FindingIds=[
              'string',
          ]
      )
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The ID of the detector that specifies the GuardDuty service whose findings you want to archive.

    
    :type FindingIds: list
    :param FindingIds: IDs of the findings that you want to archive.

    
      - *(string) --* The unique identifier for the Finding

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 200 response
    

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


  .. py:method:: create_detector(**kwargs)

    Creates a single Amazon GuardDuty detector. A detector is an object that represents the GuardDuty service. A detector must be created in order for GuardDuty to become operational.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/CreateDetector>`_    


    **Request Syntax** 
    ::

      response = client.create_detector(
          Enable=True|False
      )
    :type Enable: boolean
    :param Enable: A boolean value that specifies whether the detector is to be enabled.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DetectorId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **DetectorId** *(string) --* The unique ID of the created detector.
    

  .. py:method:: create_ip_set(**kwargs)

    Creates a new IPSet - a list of trusted IP addresses that have been whitelisted for secure communication with AWS infrastructure and applications.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/CreateIPSet>`_    


    **Request Syntax** 
    ::

      response = client.create_ip_set(
          Activate=True|False,
          DetectorId='string',
          Format='TXT'|'STIX'|'OTX_CSV'|'ALIEN_VAULT'|'PROOF_POINT'|'FIRE_EYE',
          Location='string',
          Name='string'
      )
    :type Activate: boolean
    :param Activate: A boolean value that indicates whether GuardDuty is to start using the uploaded IPSet.

    
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The unique ID of the detector that you want to update.

    
    :type Format: string
    :param Format: The format of the file that contains the IPSet.

    
    :type Location: string
    :param Location: The URI of the file that contains the IPSet. For example (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key)

    
    :type Name: string
    :param Name: The user friendly name to identify the IPSet. This name is displayed in all findings that are triggered by activity that involves IP addresses included in this IPSet.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'IpSetId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **IpSetId** *(string) --* The unique identifier for an IP Set
    

  .. py:method:: create_members(**kwargs)

    Creates member accounts of the current AWS account by specifying a list of AWS account IDs. The current AWS account can then invite these members to manage GuardDuty in their accounts.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/CreateMembers>`_    


    **Request Syntax** 
    ::

      response = client.create_members(
          AccountDetails=[
              {
                  'AccountId': 'string',
                  'Email': 'string'
              },
          ],
          DetectorId='string'
      )
    :type AccountDetails: list
    :param AccountDetails: A list of account ID and email address pairs of the accounts that you want to associate with the master GuardDuty account.

    
      - *(dict) --* An object containing the member's accountId and email address.

      
        - **AccountId** *(string) --* Member account ID.

        
        - **Email** *(string) --* Member account's email address.

        
      
  
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The unique ID of the detector of the GuardDuty account with which you want to associate member accounts.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UnprocessedAccounts': [
                {
                    'AccountId': 'string',
                    'Result': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **UnprocessedAccounts** *(list) --* A list of objects containing the unprocessed account and a result string explaining why it was unprocessed.
          

          - *(dict) --* An object containing the unprocessed account and a result string explaining why it was unprocessed.
            

            - **AccountId** *(string) --* AWS Account ID.
            

            - **Result** *(string) --* A reason why the account hasn't been processed.
        
      
    

  .. py:method:: create_sample_findings(**kwargs)

    Generates example findings of types specified by the list of finding types. If 'NULL' is specified for findingTypes, the API generates example findings of all supported finding types.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/CreateSampleFindings>`_    


    **Request Syntax** 
    ::

      response = client.create_sample_findings(
          DetectorId='string',
          FindingTypes=[
              'string',
          ]
      )
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The ID of the detector to create sample findings for.

    
    :type FindingTypes: list
    :param FindingTypes: Types of sample findings that you want to generate.

    
      - *(string) --* The finding type for the finding

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 200 response
    

  .. py:method:: create_threat_intel_set(**kwargs)

    Create a new ThreatIntelSet. ThreatIntelSets consist of known malicious IP addresses. GuardDuty generates findings based on ThreatIntelSets.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/CreateThreatIntelSet>`_    


    **Request Syntax** 
    ::

      response = client.create_threat_intel_set(
          Activate=True|False,
          DetectorId='string',
          Format='TXT'|'STIX'|'OTX_CSV'|'ALIEN_VAULT'|'PROOF_POINT'|'FIRE_EYE',
          Location='string',
          Name='string'
      )
    :type Activate: boolean
    :param Activate: A boolean value that indicates whether GuardDuty is to start using the uploaded ThreatIntelSet.

    
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The unique ID of the detector that you want to update.

    
    :type Format: string
    :param Format: The format of the file that contains the ThreatIntelSet.

    
    :type Location: string
    :param Location: The URI of the file that contains the ThreatIntelSet. For example (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key).

    
    :type Name: string
    :param Name: A user-friendly ThreatIntelSet name that is displayed in all finding generated by activity that involves IP addresses included in this ThreatIntelSet.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ThreatIntelSetId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **ThreatIntelSetId** *(string) --* The unique identifier for an threat intel set
    

  .. py:method:: decline_invitations(**kwargs)

    Declines invitations sent to the current member account by AWS account specified by their account IDs.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DeclineInvitations>`_    


    **Request Syntax** 
    ::

      response = client.decline_invitations(
          AccountIds=[
              'string',
          ]
      )
    :type AccountIds: list
    :param AccountIds: A list of account IDs of the AWS accounts that sent invitations to the current member account that you want to decline invitations from.

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UnprocessedAccounts': [
                {
                    'AccountId': 'string',
                    'Result': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **UnprocessedAccounts** *(list) --* A list of objects containing the unprocessed account and a result string explaining why it was unprocessed.
          

          - *(dict) --* An object containing the unprocessed account and a result string explaining why it was unprocessed.
            

            - **AccountId** *(string) --* AWS Account ID.
            

            - **Result** *(string) --* A reason why the account hasn't been processed.
        
      
    

  .. py:method:: delete_detector(**kwargs)

    Deletes a Amazon GuardDuty detector specified by the detector ID.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DeleteDetector>`_    


    **Request Syntax** 
    ::

      response = client.delete_detector(
          DetectorId='string'
      )
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The unique ID that specifies the detector that you want to delete.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 200 response
    

  .. py:method:: delete_invitations(**kwargs)

    Deletes invitations sent to the current member account by AWS accounts specified by their account IDs.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DeleteInvitations>`_    


    **Request Syntax** 
    ::

      response = client.delete_invitations(
          AccountIds=[
              'string',
          ]
      )
    :type AccountIds: list
    :param AccountIds: A list of account IDs of the AWS accounts that sent invitations to the current member account that you want to delete invitations from.

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UnprocessedAccounts': [
                {
                    'AccountId': 'string',
                    'Result': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **UnprocessedAccounts** *(list) --* A list of objects containing the unprocessed account and a result string explaining why it was unprocessed.
          

          - *(dict) --* An object containing the unprocessed account and a result string explaining why it was unprocessed.
            

            - **AccountId** *(string) --* AWS Account ID.
            

            - **Result** *(string) --* A reason why the account hasn't been processed.
        
      
    

  .. py:method:: delete_ip_set(**kwargs)

    Deletes the IPSet specified by the IPSet ID.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DeleteIPSet>`_    


    **Request Syntax** 
    ::

      response = client.delete_ip_set(
          DetectorId='string',
          IpSetId='string'
      )
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The detectorID that specifies the GuardDuty service whose IPSet you want to delete.

    
    :type IpSetId: string
    :param IpSetId: **[REQUIRED]** The unique ID that specifies the IPSet that you want to delete.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 200 response
    

  .. py:method:: delete_members(**kwargs)

    Deletes GuardDuty member accounts (to the current GuardDuty master account) specified by the account IDs.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DeleteMembers>`_    


    **Request Syntax** 
    ::

      response = client.delete_members(
          AccountIds=[
              'string',
          ],
          DetectorId='string'
      )
    :type AccountIds: list
    :param AccountIds: A list of account IDs of the GuardDuty member accounts that you want to delete.

    
      - *(string) --* 

      
  
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The unique ID of the detector of the GuardDuty account whose members you want to delete.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UnprocessedAccounts': [
                {
                    'AccountId': 'string',
                    'Result': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **UnprocessedAccounts** *(list) --* A list of objects containing the unprocessed account and a result string explaining why it was unprocessed.
          

          - *(dict) --* An object containing the unprocessed account and a result string explaining why it was unprocessed.
            

            - **AccountId** *(string) --* AWS Account ID.
            

            - **Result** *(string) --* A reason why the account hasn't been processed.
        
      
    

  .. py:method:: delete_threat_intel_set(**kwargs)

    Deletes ThreatIntelSet specified by the ThreatIntelSet ID.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DeleteThreatIntelSet>`_    


    **Request Syntax** 
    ::

      response = client.delete_threat_intel_set(
          DetectorId='string',
          ThreatIntelSetId='string'
      )
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The detectorID that specifies the GuardDuty service whose ThreatIntelSet you want to delete.

    
    :type ThreatIntelSetId: string
    :param ThreatIntelSetId: **[REQUIRED]** The unique ID that specifies the ThreatIntelSet that you want to delete.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 200 response
    

  .. py:method:: disassociate_from_master_account(**kwargs)

    Disassociates the current GuardDuty member account from its master account.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DisassociateFromMasterAccount>`_    


    **Request Syntax** 
    ::

      response = client.disassociate_from_master_account(
          DetectorId='string'
      )
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The unique ID of the detector of the GuardDuty member account.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 200 response
    

  .. py:method:: disassociate_members(**kwargs)

    Disassociates GuardDuty member accounts (to the current GuardDuty master account) specified by the account IDs.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/DisassociateMembers>`_    


    **Request Syntax** 
    ::

      response = client.disassociate_members(
          AccountIds=[
              'string',
          ],
          DetectorId='string'
      )
    :type AccountIds: list
    :param AccountIds: A list of account IDs of the GuardDuty member accounts that you want to disassociate from master.

    
      - *(string) --* 

      
  
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The unique ID of the detector of the GuardDuty account whose members you want to disassociate from master.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UnprocessedAccounts': [
                {
                    'AccountId': 'string',
                    'Result': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **UnprocessedAccounts** *(list) --* A list of objects containing the unprocessed account and a result string explaining why it was unprocessed.
          

          - *(dict) --* An object containing the unprocessed account and a result string explaining why it was unprocessed.
            

            - **AccountId** *(string) --* AWS Account ID.
            

            - **Result** *(string) --* A reason why the account hasn't been processed.
        
      
    

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


  .. py:method:: get_detector(**kwargs)

    Retrieves an Amazon GuardDuty detector specified by the detectorId.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetDetector>`_    


    **Request Syntax** 
    ::

      response = client.get_detector(
          DetectorId='string'
      )
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The unique ID of the detector that you want to retrieve.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CreatedAt': 'string',
            'ServiceRole': 'string',
            'Status': 'ENABLED'|'DISABLED',
            'UpdatedAt': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **CreatedAt** *(string) --* The first time a resource was created. The format will be ISO-8601.
        

        - **ServiceRole** *(string) --* Customer serviceRole name or ARN for accessing customer resources
        

        - **Status** *(string) --* The status of detector.
        

        - **UpdatedAt** *(string) --* The first time a resource was created. The format will be ISO-8601.
    

  .. py:method:: get_findings(**kwargs)

    Describes Amazon GuardDuty findings specified by finding IDs.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetFindings>`_    


    **Request Syntax** 
    ::

      response = client.get_findings(
          DetectorId='string',
          FindingIds=[
              'string',
          ],
          SortCriteria={
              'AttributeName': 'string',
              'OrderBy': 'ASC'|'DESC'
          }
      )
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The ID of the detector that specifies the GuardDuty service whose findings you want to retrieve.

    
    :type FindingIds: list
    :param FindingIds: IDs of the findings that you want to retrieve.

    
      - *(string) --* The unique identifier for the Finding

      
  
    :type SortCriteria: dict
    :param SortCriteria: Represents the criteria used for sorting findings.

    
      - **AttributeName** *(string) --* Represents the finding attribute (for example, accountId) by which to sort findings.

      
      - **OrderBy** *(string) --* Order by which the sorted findings are to be displayed.

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Findings': [
                {
                    'AccountId': 'string',
                    'Arn': 'string',
                    'Confidence': 123.0,
                    'CreatedAt': 'string',
                    'Description': 'string',
                    'Id': 'string',
                    'Partition': 'string',
                    'Region': 'string',
                    'Resource': {
                        'InstanceDetails': {
                            'AvailabilityZone': 'string',
                            'IamInstanceProfile': {
                                'Arn': 'string',
                                'Id': 'string'
                            },
                            'ImageId': 'string',
                            'InstanceId': 'string',
                            'InstanceState': 'string',
                            'InstanceType': 'string',
                            'LaunchTime': 'string',
                            'NetworkInterfaces': [
                                {
                                    'Ipv6Addresses': [
                                        'string',
                                    ],
                                    'PrivateDnsName': 'string',
                                    'PrivateIpAddress': 'string',
                                    'PrivateIpAddresses': [
                                        {
                                            'PrivateDnsName': 'string',
                                            'PrivateIpAddress': 'string'
                                        },
                                    ],
                                    'PublicDnsName': 'string',
                                    'PublicIp': 'string',
                                    'SecurityGroups': [
                                        {
                                            'GroupId': 'string',
                                            'GroupName': 'string'
                                        },
                                    ],
                                    'SubnetId': 'string',
                                    'VpcId': 'string'
                                },
                            ],
                            'Platform': 'string',
                            'ProductCodes': [
                                {
                                    'Code': 'string',
                                    'ProductType': 'string'
                                },
                            ],
                            'Tags': [
                                {
                                    'Key': 'string',
                                    'Value': 'string'
                                },
                            ]
                        },
                        'ResourceType': 'string'
                    },
                    'SchemaVersion': 'string',
                    'Service': {
                        'Action': {
                            'ActionType': 'string',
                            'AwsApiCallAction': {
                                'Api': 'string',
                                'CallerType': 'string',
                                'DomainDetails': {}
                                ,
                                'RemoteIpDetails': {
                                    'City': {
                                        'CityName': 'string'
                                    },
                                    'Country': {
                                        'CountryCode': 'string',
                                        'CountryName': 'string'
                                    },
                                    'GeoLocation': {
                                        'Lat': 123.0,
                                        'Lon': 123.0
                                    },
                                    'IpAddressV4': 'string',
                                    'Organization': {
                                        'Asn': 'string',
                                        'AsnOrg': 'string',
                                        'Isp': 'string',
                                        'Org': 'string'
                                    }
                                },
                                'ServiceName': 'string'
                            },
                            'DnsRequestAction': {
                                'Domain': 'string'
                            },
                            'NetworkConnectionAction': {
                                'Blocked': True|False,
                                'ConnectionDirection': 'string',
                                'LocalPortDetails': {
                                    'Port': 123,
                                    'PortName': 'string'
                                },
                                'Protocol': 'string',
                                'RemoteIpDetails': {
                                    'City': {
                                        'CityName': 'string'
                                    },
                                    'Country': {
                                        'CountryCode': 'string',
                                        'CountryName': 'string'
                                    },
                                    'GeoLocation': {
                                        'Lat': 123.0,
                                        'Lon': 123.0
                                    },
                                    'IpAddressV4': 'string',
                                    'Organization': {
                                        'Asn': 'string',
                                        'AsnOrg': 'string',
                                        'Isp': 'string',
                                        'Org': 'string'
                                    }
                                },
                                'RemotePortDetails': {
                                    'Port': 123,
                                    'PortName': 'string'
                                }
                            }
                        },
                        'Archived': True|False,
                        'Count': 123,
                        'DetectorId': 'string',
                        'EventFirstSeen': 'string',
                        'EventLastSeen': 'string',
                        'ResourceRole': 'string',
                        'ServiceName': 'string',
                        'UserFeedback': 'string'
                    },
                    'Severity': 123.0,
                    'Title': 'string',
                    'Type': 'string',
                    'UpdatedAt': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **Findings** *(list) --* A list of findings.
          

          - *(dict) --* Representation of a abnormal or suspicious activity.
            

            - **AccountId** *(string) --* AWS account ID where the activity occurred that prompted GuardDuty to generate a finding.
            

            - **Arn** *(string) --* The ARN of a finding described by the action.
            

            - **Confidence** *(float) --* The confidence level of a finding.
            

            - **CreatedAt** *(string) --* The time stamp at which a finding was generated.
            

            - **Description** *(string) --* The description of a finding.
            

            - **Id** *(string) --* The identifier that corresponds to a finding described by the action.
            

            - **Partition** *(string) --* The AWS resource partition.
            

            - **Region** *(string) --* The AWS region where the activity occurred that prompted GuardDuty to generate a finding.
            

            - **Resource** *(dict) --* The AWS resource associated with the activity that prompted GuardDuty to generate a finding.
              

              - **InstanceDetails** *(dict) --* The information about the EC2 instance associated with the activity that prompted GuardDuty to generate a finding.
                

                - **AvailabilityZone** *(string) --* The availability zone of the EC2 instance.
                

                - **IamInstanceProfile** *(dict) --* The profile information of the EC2 instance.
                  

                  - **Arn** *(string) --* AWS EC2 instance profile ARN.
                  

                  - **Id** *(string) --* AWS EC2 instance profile ID.
              
                

                - **ImageId** *(string) --* The image ID of the EC2 instance.
                

                - **InstanceId** *(string) --* The ID of the EC2 instance.
                

                - **InstanceState** *(string) --* The state of the EC2 instance.
                

                - **InstanceType** *(string) --* The type of the EC2 instance.
                

                - **LaunchTime** *(string) --* The launch time of the EC2 instance.
                

                - **NetworkInterfaces** *(list) --* The network interface information of the EC2 instance.
                  

                  - *(dict) --* The network interface information of the EC2 instance.
                    

                    - **Ipv6Addresses** *(list) --* A list of EC2 instance IPv6 address information.
                      

                      - *(string) --* IpV6 address of the EC2 instance.
                  
                    

                    - **PrivateDnsName** *(string) --* Private DNS name of the EC2 instance.
                    

                    - **PrivateIpAddress** *(string) --* Private IP address of the EC2 instance.
                    

                    - **PrivateIpAddresses** *(list) --* Other private IP address information of the EC2 instance.
                      

                      - *(dict) --* Other private IP address information of the EC2 instance.
                        

                        - **PrivateDnsName** *(string) --* Private DNS name of the EC2 instance.
                        

                        - **PrivateIpAddress** *(string) --* Private IP address of the EC2 instance.
                    
                  
                    

                    - **PublicDnsName** *(string) --* Public DNS name of the EC2 instance.
                    

                    - **PublicIp** *(string) --* Public IP address of the EC2 instance.
                    

                    - **SecurityGroups** *(list) --* Security groups associated with the EC2 instance.
                      

                      - *(dict) --* Security groups associated with the EC2 instance.
                        

                        - **GroupId** *(string) --* EC2 instance's security group ID.
                        

                        - **GroupName** *(string) --* EC2 instance's security group name.
                    
                  
                    

                    - **SubnetId** *(string) --* The subnet ID of the EC2 instance.
                    

                    - **VpcId** *(string) --* The VPC ID of the EC2 instance.
                
              
                

                - **Platform** *(string) --* The platform of the EC2 instance.
                

                - **ProductCodes** *(list) --* The product code of the EC2 instance.
                  

                  - *(dict) --* The product code of the EC2 instance.
                    

                    - **Code** *(string) --* Product code information.
                    

                    - **ProductType** *(string) --* Product code type.
                
              
                

                - **Tags** *(list) --* The tags of the EC2 instance.
                  

                  - *(dict) --* A tag of the EC2 instance.
                    

                    - **Key** *(string) --* EC2 instance tag key.
                    

                    - **Value** *(string) --* EC2 instance tag value.
                
              
            
              

              - **ResourceType** *(string) --* The type of the AWS resource.
          
            

            - **SchemaVersion** *(string) --* Findings' schema version.
            

            - **Service** *(dict) --* Additional information assigned to the generated finding by GuardDuty.
              

              - **Action** *(dict) --* Information about the activity described in a finding.
                

                - **ActionType** *(string) --* GuardDuty Finding activity type.
                

                - **AwsApiCallAction** *(dict) --* Information about the AWS_API_CALL action described in this finding.
                  

                  - **Api** *(string) --* AWS API name.
                  

                  - **CallerType** *(string) --* AWS API caller type.
                  

                  - **DomainDetails** *(dict) --* Domain information for the AWS API call.
                
                  

                  - **RemoteIpDetails** *(dict) --* Remote IP information of the connection.
                    

                    - **City** *(dict) --* City information of the remote IP address.
                      

                      - **CityName** *(string) --* City name of the remote IP address.
                  
                    

                    - **Country** *(dict) --* Country code of the remote IP address.
                      

                      - **CountryCode** *(string) --* Country code of the remote IP address.
                      

                      - **CountryName** *(string) --* Country name of the remote IP address.
                  
                    

                    - **GeoLocation** *(dict) --* Location information of the remote IP address.
                      

                      - **Lat** *(float) --* Latitude information of remote IP address.
                      

                      - **Lon** *(float) --* Longitude information of remote IP address.
                  
                    

                    - **IpAddressV4** *(string) --* IPV4 remote address of the connection.
                    

                    - **Organization** *(dict) --* ISP Organization information of the remote IP address.
                      

                      - **Asn** *(string) --* Autonomous system number of the internet provider of the remote IP address.
                      

                      - **AsnOrg** *(string) --* Organization that registered this ASN.
                      

                      - **Isp** *(string) --* ISP information for the internet provider.
                      

                      - **Org** *(string) --* Name of the internet provider.
                  
                
                  

                  - **ServiceName** *(string) --* AWS service name whose API was invoked.
              
                

                - **DnsRequestAction** *(dict) --* Information about the DNS_REQUEST action described in this finding.
                  

                  - **Domain** *(string) --* Domain information for the DNS request.
              
                

                - **NetworkConnectionAction** *(dict) --* Information about the NETWORK_CONNECTION action described in this finding.
                  

                  - **Blocked** *(boolean) --* Network connection blocked information.
                  

                  - **ConnectionDirection** *(string) --* Network connection direction.
                  

                  - **LocalPortDetails** *(dict) --* Local port information of the connection.
                    

                    - **Port** *(integer) --* Port number of the local connection.
                    

                    - **PortName** *(string) --* Port name of the local connection.
                
                  

                  - **Protocol** *(string) --* Network connection protocol.
                  

                  - **RemoteIpDetails** *(dict) --* Remote IP information of the connection.
                    

                    - **City** *(dict) --* City information of the remote IP address.
                      

                      - **CityName** *(string) --* City name of the remote IP address.
                  
                    

                    - **Country** *(dict) --* Country code of the remote IP address.
                      

                      - **CountryCode** *(string) --* Country code of the remote IP address.
                      

                      - **CountryName** *(string) --* Country name of the remote IP address.
                  
                    

                    - **GeoLocation** *(dict) --* Location information of the remote IP address.
                      

                      - **Lat** *(float) --* Latitude information of remote IP address.
                      

                      - **Lon** *(float) --* Longitude information of remote IP address.
                  
                    

                    - **IpAddressV4** *(string) --* IPV4 remote address of the connection.
                    

                    - **Organization** *(dict) --* ISP Organization information of the remote IP address.
                      

                      - **Asn** *(string) --* Autonomous system number of the internet provider of the remote IP address.
                      

                      - **AsnOrg** *(string) --* Organization that registered this ASN.
                      

                      - **Isp** *(string) --* ISP information for the internet provider.
                      

                      - **Org** *(string) --* Name of the internet provider.
                  
                
                  

                  - **RemotePortDetails** *(dict) --* Remote port information of the connection.
                    

                    - **Port** *(integer) --* Port number of the remote connection.
                    

                    - **PortName** *(string) --* Port name of the remote connection.
                
              
            
              

              - **Archived** *(boolean) --* Indicates whether this finding is archived.
              

              - **Count** *(integer) --* Total count of the occurrences of this finding type.
              

              - **DetectorId** *(string) --* Detector ID for the GuardDuty service.
              

              - **EventFirstSeen** *(string) --* First seen timestamp of the activity that prompted GuardDuty to generate this finding.
              

              - **EventLastSeen** *(string) --* Last seen timestamp of the activity that prompted GuardDuty to generate this finding.
              

              - **ResourceRole** *(string) --* Resource role information for this finding.
              

              - **ServiceName** *(string) --* The name of the AWS service (GuardDuty) that generated a finding.
              

              - **UserFeedback** *(string) --* Feedback left about the finding.
          
            

            - **Severity** *(float) --* The severity of a finding.
            

            - **Title** *(string) --* The title of a finding.
            

            - **Type** *(string) --* The type of a finding described by the action.
            

            - **UpdatedAt** *(string) --* The time stamp at which a finding was last updated.
        
      
    

  .. py:method:: get_findings_statistics(**kwargs)

    Lists Amazon GuardDuty findings' statistics for the specified detector ID.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetFindingsStatistics>`_    


    **Request Syntax** 
    ::

      response = client.get_findings_statistics(
          DetectorId='string',
          FindingCriteria={
              'Criterion': {
                  'string': {
                      'Eq': [
                          'string',
                      ],
                      'Gt': 123,
                      'Gte': 123,
                      'Lt': 123,
                      'Lte': 123,
                      'Neq': [
                          'string',
                      ]
                  }
              }
          },
          FindingStatisticTypes=[
              'COUNT_BY_SEVERITY',
          ]
      )
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The ID of the detector that specifies the GuardDuty service whose findings' statistics you want to retrieve.

    
    :type FindingCriteria: dict
    :param FindingCriteria: Represents the criteria used for querying findings.

    
      - **Criterion** *(dict) --* Represents a map of finding properties that match specified conditions and values when querying findings.

      
        - *(string) --* 

        
          - *(dict) --* Finding attribute (for example, accountId) for which conditions and values must be specified when querying findings.

          
            - **Eq** *(list) --* Represents the equal condition to be applied to a single field when querying for findings.

            
              - *(string) --* 

              
          
            - **Gt** *(integer) --* Represents the greater than condition to be applied to a single field when querying for findings.

            
            - **Gte** *(integer) --* Represents the greater than equal condition to be applied to a single field when querying for findings.

            
            - **Lt** *(integer) --* Represents the less than condition to be applied to a single field when querying for findings.

            
            - **Lte** *(integer) --* Represents the less than equal condition to be applied to a single field when querying for findings.

            
            - **Neq** *(list) --* Represents the not equal condition to be applied to a single field when querying for findings.

            
              - *(string) --* 

              
          
          
    
  
    
    :type FindingStatisticTypes: list
    :param FindingStatisticTypes: Types of finding statistics to retrieve.

    
      - *(string) --* The types of finding statistics.

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'FindingStatistics': {
                'CountBySeverity': {
                    'string': 123
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **FindingStatistics** *(dict) --* Finding statistics object.
          

          - **CountBySeverity** *(dict) --* Represents a map of severity to count statistic for a set of findings
            

            - *(string) --* 
              

              - *(integer) --* The count of findings for the given severity.
        
      
      
    

  .. py:method:: get_invitations_count()

    Returns the count of all GuardDuty membership invitations that were sent to the current member account except the currently accepted invitation.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetInvitationsCount>`_    


    **Request Syntax** 
    ::

      response = client.get_invitations_count()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'InvitationsCount': 123
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **InvitationsCount** *(integer) --* The number of received invitations.
    

  .. py:method:: get_ip_set(**kwargs)

    Retrieves the IPSet specified by the IPSet ID.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetIPSet>`_    


    **Request Syntax** 
    ::

      response = client.get_ip_set(
          DetectorId='string',
          IpSetId='string'
      )
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The detectorID that specifies the GuardDuty service whose IPSet you want to retrieve.

    
    :type IpSetId: string
    :param IpSetId: **[REQUIRED]** The unique ID that specifies the IPSet that you want to describe.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Format': 'TXT'|'STIX'|'OTX_CSV'|'ALIEN_VAULT'|'PROOF_POINT'|'FIRE_EYE',
            'Location': 'string',
            'Name': 'string',
            'Status': 'INACTIVE'|'ACTIVATING'|'ACTIVE'|'DEACTIVATING'|'ERROR'|'DELETE_PENDING'|'DELETED'
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **Format** *(string) --* The format of the file that contains the IPSet.
        

        - **Location** *(string) --* The URI of the file that contains the IPSet. For example (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key)
        

        - **Name** *(string) --* The user friendly name to identify the IPSet. This name is displayed in all findings that are triggered by activity that involves IP addresses included in this IPSet.
        

        - **Status** *(string) --* The status of ipSet file uploaded.
    

  .. py:method:: get_master_account(**kwargs)

    Provides the details for the GuardDuty master account to the current GuardDuty member account.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetMasterAccount>`_    


    **Request Syntax** 
    ::

      response = client.get_master_account(
          DetectorId='string'
      )
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The unique ID of the detector of the GuardDuty member account.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Master': {
                'AccountId': 'string',
                'InvitationId': 'string',
                'InvitedAt': 'string',
                'RelationshipStatus': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **Master** *(dict) --* Contains details about the master account.
          

          - **AccountId** *(string) --* Master account ID
          

          - **InvitationId** *(string) --* This value is used to validate the master account to the member account.
          

          - **InvitedAt** *(string) --* Timestamp at which the invitation was sent
          

          - **RelationshipStatus** *(string) --* The status of the relationship between the master and member accounts.
      
    

  .. py:method:: get_members(**kwargs)

    Retrieves GuardDuty member accounts (to the current GuardDuty master account) specified by the account IDs.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetMembers>`_    


    **Request Syntax** 
    ::

      response = client.get_members(
          AccountIds=[
              'string',
          ],
          DetectorId='string'
      )
    :type AccountIds: list
    :param AccountIds: A list of account IDs of the GuardDuty member accounts that you want to describe.

    
      - *(string) --* 

      
  
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The unique ID of the detector of the GuardDuty account whose members you want to retrieve.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Members': [
                {
                    'AccountId': 'string',
                    'DetectorId': 'string',
                    'Email': 'string',
                    'InvitedAt': 'string',
                    'MasterId': 'string',
                    'RelationshipStatus': 'string',
                    'UpdatedAt': 'string'
                },
            ],
            'UnprocessedAccounts': [
                {
                    'AccountId': 'string',
                    'Result': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **Members** *(list) --* A list of member descriptions.
          

          - *(dict) --* Contains details about the member account.
            

            - **AccountId** *(string) --* AWS account ID.
            

            - **DetectorId** *(string) --* The unique identifier for a detector.
            

            - **Email** *(string) --* Member account's email address.
            

            - **InvitedAt** *(string) --* Timestamp at which the invitation was sent
            

            - **MasterId** *(string) --* The master account ID.
            

            - **RelationshipStatus** *(string) --* The status of the relationship between the member and the master.
            

            - **UpdatedAt** *(string) --* The first time a resource was created. The format will be ISO-8601.
        
      
        

        - **UnprocessedAccounts** *(list) --* A list of objects containing the unprocessed account and a result string explaining why it was unprocessed.
          

          - *(dict) --* An object containing the unprocessed account and a result string explaining why it was unprocessed.
            

            - **AccountId** *(string) --* AWS Account ID.
            

            - **Result** *(string) --* A reason why the account hasn't been processed.
        
      
    

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


  .. py:method:: get_threat_intel_set(**kwargs)

    Retrieves the ThreatIntelSet that is specified by the ThreatIntelSet ID.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/GetThreatIntelSet>`_    


    **Request Syntax** 
    ::

      response = client.get_threat_intel_set(
          DetectorId='string',
          ThreatIntelSetId='string'
      )
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The detectorID that specifies the GuardDuty service whose ThreatIntelSet you want to describe.

    
    :type ThreatIntelSetId: string
    :param ThreatIntelSetId: **[REQUIRED]** The unique ID that specifies the ThreatIntelSet that you want to describe.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Format': 'TXT'|'STIX'|'OTX_CSV'|'ALIEN_VAULT'|'PROOF_POINT'|'FIRE_EYE',
            'Location': 'string',
            'Name': 'string',
            'Status': 'INACTIVE'|'ACTIVATING'|'ACTIVE'|'DEACTIVATING'|'ERROR'|'DELETE_PENDING'|'DELETED'
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **Format** *(string) --* The format of the threatIntelSet.
        

        - **Location** *(string) --* The URI of the file that contains the ThreatIntelSet. For example (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key).
        

        - **Name** *(string) --* A user-friendly ThreatIntelSet name that is displayed in all finding generated by activity that involves IP addresses included in this ThreatIntelSet.
        

        - **Status** *(string) --* The status of threatIntelSet file uploaded.
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: invite_members(**kwargs)

    Invites other AWS accounts (created as members of the current AWS account by CreateMembers) to enable GuardDuty and allow the current AWS account to view and manage these accounts' GuardDuty findings on their behalf as the master account.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/InviteMembers>`_    


    **Request Syntax** 
    ::

      response = client.invite_members(
          AccountIds=[
              'string',
          ],
          DetectorId='string',
          Message='string'
      )
    :type AccountIds: list
    :param AccountIds: A list of account IDs of the accounts that you want to invite to GuardDuty as members.

    
      - *(string) --* 

      
  
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The unique ID of the detector of the GuardDuty account with which you want to invite members.

    
    :type Message: string
    :param Message: The invitation message that you want to send to the accounts that you're inviting to GuardDuty as members.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UnprocessedAccounts': [
                {
                    'AccountId': 'string',
                    'Result': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **UnprocessedAccounts** *(list) --* A list of objects containing the unprocessed account and a result string explaining why it was unprocessed.
          

          - *(dict) --* An object containing the unprocessed account and a result string explaining why it was unprocessed.
            

            - **AccountId** *(string) --* AWS Account ID.
            

            - **Result** *(string) --* A reason why the account hasn't been processed.
        
      
    

  .. py:method:: list_detectors(**kwargs)

    Lists detectorIds of all the existing Amazon GuardDuty detector resources.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListDetectors>`_    


    **Request Syntax** 
    ::

      response = client.list_detectors(
          MaxResults=123,
          NextToken='string'
      )
    :type MaxResults: integer
    :param MaxResults: You can use this parameter to indicate the maximum number of detectors that you want in the response.

    
    :type NextToken: string
    :param NextToken: You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the ListDetectors action. For subsequent calls to the action fill nextToken in the request with the value of nextToken from the previous response to continue listing data.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DetectorIds': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **DetectorIds** *(list) --* A list of detector Ids.
          

          - *(string) --* The unique identifier for a detector.
      
        

        - **NextToken** *(string) --* You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.
    

  .. py:method:: list_findings(**kwargs)

    Lists Amazon GuardDuty findings for the specified detector ID.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListFindings>`_    


    **Request Syntax** 
    ::

      response = client.list_findings(
          DetectorId='string',
          FindingCriteria={
              'Criterion': {
                  'string': {
                      'Eq': [
                          'string',
                      ],
                      'Gt': 123,
                      'Gte': 123,
                      'Lt': 123,
                      'Lte': 123,
                      'Neq': [
                          'string',
                      ]
                  }
              }
          },
          MaxResults=123,
          NextToken='string',
          SortCriteria={
              'AttributeName': 'string',
              'OrderBy': 'ASC'|'DESC'
          }
      )
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The ID of the detector that specifies the GuardDuty service whose findings you want to list.

    
    :type FindingCriteria: dict
    :param FindingCriteria: Represents the criteria used for querying findings.

    
      - **Criterion** *(dict) --* Represents a map of finding properties that match specified conditions and values when querying findings.

      
        - *(string) --* 

        
          - *(dict) --* Finding attribute (for example, accountId) for which conditions and values must be specified when querying findings.

          
            - **Eq** *(list) --* Represents the equal condition to be applied to a single field when querying for findings.

            
              - *(string) --* 

              
          
            - **Gt** *(integer) --* Represents the greater than condition to be applied to a single field when querying for findings.

            
            - **Gte** *(integer) --* Represents the greater than equal condition to be applied to a single field when querying for findings.

            
            - **Lt** *(integer) --* Represents the less than condition to be applied to a single field when querying for findings.

            
            - **Lte** *(integer) --* Represents the less than equal condition to be applied to a single field when querying for findings.

            
            - **Neq** *(list) --* Represents the not equal condition to be applied to a single field when querying for findings.

            
              - *(string) --* 

              
          
          
    
  
    
    :type MaxResults: integer
    :param MaxResults: You can use this parameter to indicate the maximum number of items you want in the response. The default value is 50. The maximum value is 50.

    
    :type NextToken: string
    :param NextToken: You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the ListFindings action. For subsequent calls to the action fill nextToken in the request with the value of nextToken from the previous response to continue listing data.

    
    :type SortCriteria: dict
    :param SortCriteria: Represents the criteria used for sorting findings.

    
      - **AttributeName** *(string) --* Represents the finding attribute (for example, accountId) by which to sort findings.

      
      - **OrderBy** *(string) --* Order by which the sorted findings are to be displayed.

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'FindingIds': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **FindingIds** *(list) --* The list of the Findings.
          

          - *(string) --* The unique identifier for the Finding
      
        

        - **NextToken** *(string) --* You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.
    

  .. py:method:: list_invitations(**kwargs)

    Lists all GuardDuty membership invitations that were sent to the current AWS account.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListInvitations>`_    


    **Request Syntax** 
    ::

      response = client.list_invitations(
          MaxResults=123,
          NextToken='string'
      )
    :type MaxResults: integer
    :param MaxResults: You can use this parameter to indicate the maximum number of invitations you want in the response. The default value is 50. The maximum value is 50.

    
    :type NextToken: string
    :param NextToken: You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the ListInvitations action. Subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Invitations': [
                {
                    'AccountId': 'string',
                    'InvitationId': 'string',
                    'InvitedAt': 'string',
                    'RelationshipStatus': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **Invitations** *(list) --* A list of invitation descriptions.
          

          - *(dict) --* Invitation from an AWS account to become the current account's master.
            

            - **AccountId** *(string) --* Inviter account ID
            

            - **InvitationId** *(string) --* This value is used to validate the inviter account to the member account.
            

            - **InvitedAt** *(string) --* Timestamp at which the invitation was sent
            

            - **RelationshipStatus** *(string) --* The status of the relationship between the inviter and invitee accounts.
        
      
        

        - **NextToken** *(string) --* You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.
    

  .. py:method:: list_ip_sets(**kwargs)

    Lists the IPSets of the GuardDuty service specified by the detector ID.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListIPSets>`_    


    **Request Syntax** 
    ::

      response = client.list_ip_sets(
          DetectorId='string',
          MaxResults=123,
          NextToken='string'
      )
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The unique ID of the detector that you want to retrieve.

    
    :type MaxResults: integer
    :param MaxResults: You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 7. The maximum value is 7.

    
    :type NextToken: string
    :param NextToken: You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the ListIPSet action. For subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'IpSetIds': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **IpSetIds** *(list) --* A list of the IP set IDs
          

          - *(string) --* The unique identifier for an IP Set
      
        

        - **NextToken** *(string) --* You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.
    

  .. py:method:: list_members(**kwargs)

    Lists details about all member accounts for the current GuardDuty master account.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListMembers>`_    


    **Request Syntax** 
    ::

      response = client.list_members(
          DetectorId='string',
          MaxResults=123,
          NextToken='string',
          OnlyAssociated='string'
      )
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The unique ID of the detector of the GuardDuty account whose members you want to list.

    
    :type MaxResults: integer
    :param MaxResults: You can use this parameter to indicate the maximum number of items you want in the response. The default value is 1. The maximum value is 50.

    
    :type NextToken: string
    :param NextToken: You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the ListMembers action. Subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.

    
    :type OnlyAssociated: string
    :param OnlyAssociated: Specifies what member accounts the response is to include based on their relationship status with the master account. The default value is TRUE. If onlyAssociated is set to TRUE, the response will include member accounts whose relationship status with the master is set to Enabled, Disabled. If onlyAssociated is set to FALSE, the response will include all existing member accounts.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Members': [
                {
                    'AccountId': 'string',
                    'DetectorId': 'string',
                    'Email': 'string',
                    'InvitedAt': 'string',
                    'MasterId': 'string',
                    'RelationshipStatus': 'string',
                    'UpdatedAt': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **Members** *(list) --* A list of member descriptions.
          

          - *(dict) --* Contains details about the member account.
            

            - **AccountId** *(string) --* AWS account ID.
            

            - **DetectorId** *(string) --* The unique identifier for a detector.
            

            - **Email** *(string) --* Member account's email address.
            

            - **InvitedAt** *(string) --* Timestamp at which the invitation was sent
            

            - **MasterId** *(string) --* The master account ID.
            

            - **RelationshipStatus** *(string) --* The status of the relationship between the member and the master.
            

            - **UpdatedAt** *(string) --* The first time a resource was created. The format will be ISO-8601.
        
      
        

        - **NextToken** *(string) --* You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.
    

  .. py:method:: list_threat_intel_sets(**kwargs)

    Lists the ThreatIntelSets of the GuardDuty service specified by the detector ID.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListThreatIntelSets>`_    


    **Request Syntax** 
    ::

      response = client.list_threat_intel_sets(
          DetectorId='string',
          MaxResults=123,
          NextToken='string'
      )
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The detectorID that specifies the GuardDuty service whose ThreatIntelSets you want to list.

    
    :type MaxResults: integer
    :param MaxResults: You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 7. The maximum value is 7.

    
    :type NextToken: string
    :param NextToken: Pagination token to start retrieving threat intel sets from.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextToken': 'string',
            'ThreatIntelSetIds': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **NextToken** *(string) --* You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action fill nextToken in the request with the value of NextToken from the previous response to continue listing data.
        

        - **ThreatIntelSetIds** *(list) --* The list of the threat intel set IDs
          

          - *(string) --* The unique identifier for an threat intel set
      
    

  .. py:method:: start_monitoring_members(**kwargs)

    Re-enables GuardDuty to monitor findings of the member accounts specified by the account IDs. A master GuardDuty account can run this command after disabling GuardDuty from monitoring these members' findings by running StopMonitoringMembers.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/StartMonitoringMembers>`_    


    **Request Syntax** 
    ::

      response = client.start_monitoring_members(
          AccountIds=[
              'string',
          ],
          DetectorId='string'
      )
    :type AccountIds: list
    :param AccountIds: A list of account IDs of the GuardDuty member accounts whose findings you want the master account to monitor.

    
      - *(string) --* 

      
  
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The unique ID of the detector of the GuardDuty account whom you want to re-enable to monitor members' findings.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UnprocessedAccounts': [
                {
                    'AccountId': 'string',
                    'Result': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **UnprocessedAccounts** *(list) --* A list of objects containing the unprocessed account and a result string explaining why it was unprocessed.
          

          - *(dict) --* An object containing the unprocessed account and a result string explaining why it was unprocessed.
            

            - **AccountId** *(string) --* AWS Account ID.
            

            - **Result** *(string) --* A reason why the account hasn't been processed.
        
      
    

  .. py:method:: stop_monitoring_members(**kwargs)

    Disables GuardDuty from monitoring findings of the member accounts specified by the account IDs. After running this command, a master GuardDuty account can run StartMonitoringMembers to re-enable GuardDuty to monitor these members' findings.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/StopMonitoringMembers>`_    


    **Request Syntax** 
    ::

      response = client.stop_monitoring_members(
          AccountIds=[
              'string',
          ],
          DetectorId='string'
      )
    :type AccountIds: list
    :param AccountIds: A list of account IDs of the GuardDuty member accounts whose findings you want the master account to stop monitoring.

    
      - *(string) --* 

      
  
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The unique ID of the detector of the GuardDuty account that you want to stop from monitor members' findings.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'UnprocessedAccounts': [
                {
                    'AccountId': 'string',
                    'Result': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **UnprocessedAccounts** *(list) --* A list of objects containing the unprocessed account and a result string explaining why it was unprocessed.
          

          - *(dict) --* An object containing the unprocessed account and a result string explaining why it was unprocessed.
            

            - **AccountId** *(string) --* AWS Account ID.
            

            - **Result** *(string) --* A reason why the account hasn't been processed.
        
      
    

  .. py:method:: unarchive_findings(**kwargs)

    Unarchives Amazon GuardDuty findings specified by the list of finding IDs.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/UnarchiveFindings>`_    


    **Request Syntax** 
    ::

      response = client.unarchive_findings(
          DetectorId='string',
          FindingIds=[
              'string',
          ]
      )
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The ID of the detector that specifies the GuardDuty service whose findings you want to unarchive.

    
    :type FindingIds: list
    :param FindingIds: IDs of the findings that you want to unarchive.

    
      - *(string) --* The unique identifier for the Finding

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 200 response
    

  .. py:method:: update_detector(**kwargs)

    Updates an Amazon GuardDuty detector specified by the detectorId.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/UpdateDetector>`_    


    **Request Syntax** 
    ::

      response = client.update_detector(
          DetectorId='string',
          Enable=True|False
      )
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The unique ID of the detector that you want to update.

    
    :type Enable: boolean
    :param Enable: Updated boolean value for the detector that specifies whether the detector is enabled.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 200 response
    

  .. py:method:: update_findings_feedback(**kwargs)

    Marks specified Amazon GuardDuty findings as useful or not useful.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/UpdateFindingsFeedback>`_    


    **Request Syntax** 
    ::

      response = client.update_findings_feedback(
          Comments='string',
          DetectorId='string',
          Feedback='USEFUL'|'NOT_USEFUL',
          FindingIds=[
              'string',
          ]
      )
    :type Comments: string
    :param Comments: Additional feedback about the GuardDuty findings.

    
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The ID of the detector that specifies the GuardDuty service whose findings you want to mark as useful or not useful.

    
    :type Feedback: string
    :param Feedback: Valid values: USEFUL | NOT_USEFUL

    
    :type FindingIds: list
    :param FindingIds: IDs of the findings that you want to mark as useful or not useful.

    
      - *(string) --* The unique identifier for the Finding

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 200 response
    

  .. py:method:: update_ip_set(**kwargs)

    Updates the IPSet specified by the IPSet ID.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/UpdateIPSet>`_    


    **Request Syntax** 
    ::

      response = client.update_ip_set(
          Activate=True|False,
          DetectorId='string',
          IpSetId='string',
          Location='string',
          Name='string'
      )
    :type Activate: boolean
    :param Activate: The updated boolean value that specifies whether the IPSet is active or not.

    
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The detectorID that specifies the GuardDuty service whose IPSet you want to update.

    
    :type IpSetId: string
    :param IpSetId: **[REQUIRED]** The unique ID that specifies the IPSet that you want to update.

    
    :type Location: string
    :param Location: The updated URI of the file that contains the IPSet. For example (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key).

    
    :type Name: string
    :param Name: The unique ID that specifies the IPSet that you want to update.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 200 response
    

  .. py:method:: update_threat_intel_set(**kwargs)

    Updates the ThreatIntelSet specified by ThreatIntelSet ID.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/UpdateThreatIntelSet>`_    


    **Request Syntax** 
    ::

      response = client.update_threat_intel_set(
          Activate=True|False,
          DetectorId='string',
          Location='string',
          Name='string',
          ThreatIntelSetId='string'
      )
    :type Activate: boolean
    :param Activate: The updated boolean value that specifies whether the ThreateIntelSet is active or not.

    
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The detectorID that specifies the GuardDuty service whose ThreatIntelSet you want to update.

    
    :type Location: string
    :param Location: The updated URI of the file that contains the ThreateIntelSet. For example (https://s3.us-west-2.amazonaws.com/my-bucket/my-object-key)

    
    :type Name: string
    :param Name: The unique ID that specifies the ThreatIntelSet that you want to update.

    
    :type ThreatIntelSetId: string
    :param ThreatIntelSetId: **[REQUIRED]** The unique ID that specifies the ThreatIntelSet that you want to update.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 200 response
    

==========
Paginators
==========


The available paginators are:

* :py:class:`GuardDuty.Paginator.ListDetectors`


* :py:class:`GuardDuty.Paginator.ListFindings`


* :py:class:`GuardDuty.Paginator.ListIPSets`


* :py:class:`GuardDuty.Paginator.ListInvitations`


* :py:class:`GuardDuty.Paginator.ListMembers`


* :py:class:`GuardDuty.Paginator.ListThreatIntelSets`



.. py:class:: GuardDuty.Paginator.ListDetectors

  ::

    
    paginator = client.get_paginator('list_detectors')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`GuardDuty.Client.list_detectors`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListDetectors>`_    


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
            'DetectorIds': [
                'string',
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **DetectorIds** *(list) --* A list of detector Ids.
          

          - *(string) --* The unique identifier for a detector.
      
    

.. py:class:: GuardDuty.Paginator.ListFindings

  ::

    
    paginator = client.get_paginator('list_findings')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`GuardDuty.Client.list_findings`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListFindings>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          DetectorId='string',
          FindingCriteria={
              'Criterion': {
                  'string': {
                      'Eq': [
                          'string',
                      ],
                      'Gt': 123,
                      'Gte': 123,
                      'Lt': 123,
                      'Lte': 123,
                      'Neq': [
                          'string',
                      ]
                  }
              }
          },
          SortCriteria={
              'AttributeName': 'string',
              'OrderBy': 'ASC'|'DESC'
          },
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The ID of the detector that specifies the GuardDuty service whose findings you want to list.

    
    :type FindingCriteria: dict
    :param FindingCriteria: Represents the criteria used for querying findings.

    
      - **Criterion** *(dict) --* Represents a map of finding properties that match specified conditions and values when querying findings.

      
        - *(string) --* 

        
          - *(dict) --* Finding attribute (for example, accountId) for which conditions and values must be specified when querying findings.

          
            - **Eq** *(list) --* Represents the equal condition to be applied to a single field when querying for findings.

            
              - *(string) --* 

              
          
            - **Gt** *(integer) --* Represents the greater than condition to be applied to a single field when querying for findings.

            
            - **Gte** *(integer) --* Represents the greater than equal condition to be applied to a single field when querying for findings.

            
            - **Lt** *(integer) --* Represents the less than condition to be applied to a single field when querying for findings.

            
            - **Lte** *(integer) --* Represents the less than equal condition to be applied to a single field when querying for findings.

            
            - **Neq** *(list) --* Represents the not equal condition to be applied to a single field when querying for findings.

            
              - *(string) --* 

              
          
          
    
  
    
    :type SortCriteria: dict
    :param SortCriteria: Represents the criteria used for sorting findings.

    
      - **AttributeName** *(string) --* Represents the finding attribute (for example, accountId) by which to sort findings.

      
      - **OrderBy** *(string) --* Order by which the sorted findings are to be displayed.

      
    
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
            'FindingIds': [
                'string',
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **FindingIds** *(list) --* The list of the Findings.
          

          - *(string) --* The unique identifier for the Finding
      
    

.. py:class:: GuardDuty.Paginator.ListIPSets

  ::

    
    paginator = client.get_paginator('list_ip_sets')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`GuardDuty.Client.list_ip_sets`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListIPSets>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          DetectorId='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The unique ID of the detector that you want to retrieve.

    
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
            'IpSetIds': [
                'string',
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **IpSetIds** *(list) --* A list of the IP set IDs
          

          - *(string) --* The unique identifier for an IP Set
      
    

.. py:class:: GuardDuty.Paginator.ListInvitations

  ::

    
    paginator = client.get_paginator('list_invitations')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`GuardDuty.Client.list_invitations`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListInvitations>`_    


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
            'Invitations': [
                {
                    'AccountId': 'string',
                    'InvitationId': 'string',
                    'InvitedAt': 'string',
                    'RelationshipStatus': 'string'
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **Invitations** *(list) --* A list of invitation descriptions.
          

          - *(dict) --* Invitation from an AWS account to become the current account's master.
            

            - **AccountId** *(string) --* Inviter account ID
            

            - **InvitationId** *(string) --* This value is used to validate the inviter account to the member account.
            

            - **InvitedAt** *(string) --* Timestamp at which the invitation was sent
            

            - **RelationshipStatus** *(string) --* The status of the relationship between the inviter and invitee accounts.
        
      
    

.. py:class:: GuardDuty.Paginator.ListMembers

  ::

    
    paginator = client.get_paginator('list_members')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`GuardDuty.Client.list_members`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListMembers>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          DetectorId='string',
          OnlyAssociated='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The unique ID of the detector of the GuardDuty account whose members you want to list.

    
    :type OnlyAssociated: string
    :param OnlyAssociated: Specifies what member accounts the response is to include based on their relationship status with the master account. The default value is TRUE. If onlyAssociated is set to TRUE, the response will include member accounts whose relationship status with the master is set to Enabled, Disabled. If onlyAssociated is set to FALSE, the response will include all existing member accounts.

    
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
            'Members': [
                {
                    'AccountId': 'string',
                    'DetectorId': 'string',
                    'Email': 'string',
                    'InvitedAt': 'string',
                    'MasterId': 'string',
                    'RelationshipStatus': 'string',
                    'UpdatedAt': 'string'
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **Members** *(list) --* A list of member descriptions.
          

          - *(dict) --* Contains details about the member account.
            

            - **AccountId** *(string) --* AWS account ID.
            

            - **DetectorId** *(string) --* The unique identifier for a detector.
            

            - **Email** *(string) --* Member account's email address.
            

            - **InvitedAt** *(string) --* Timestamp at which the invitation was sent
            

            - **MasterId** *(string) --* The master account ID.
            

            - **RelationshipStatus** *(string) --* The status of the relationship between the member and the master.
            

            - **UpdatedAt** *(string) --* The first time a resource was created. The format will be ISO-8601.
        
      
    

.. py:class:: GuardDuty.Paginator.ListThreatIntelSets

  ::

    
    paginator = client.get_paginator('list_threat_intel_sets')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`GuardDuty.Client.list_threat_intel_sets`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListThreatIntelSets>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          DetectorId='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type DetectorId: string
    :param DetectorId: **[REQUIRED]** The detectorID that specifies the GuardDuty service whose ThreatIntelSets you want to list.

    
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
            'ThreatIntelSetIds': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 200 response
        

        - **ThreatIntelSetIds** *(list) --* The list of the threat intel set IDs
          

          - *(string) --* The unique identifier for an threat intel set
      
    