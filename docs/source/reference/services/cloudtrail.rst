

**********
CloudTrail
**********

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: CloudTrail.Client

  A low-level client representing AWS CloudTrail::

    
    import boto3
    
    client = boto3.client('cloudtrail')

  
  These are the available methods:
  
  *   :py:meth:`~CloudTrail.Client.add_tags`

  
  *   :py:meth:`~CloudTrail.Client.can_paginate`

  
  *   :py:meth:`~CloudTrail.Client.create_trail`

  
  *   :py:meth:`~CloudTrail.Client.delete_trail`

  
  *   :py:meth:`~CloudTrail.Client.describe_trails`

  
  *   :py:meth:`~CloudTrail.Client.generate_presigned_url`

  
  *   :py:meth:`~CloudTrail.Client.get_event_selectors`

  
  *   :py:meth:`~CloudTrail.Client.get_paginator`

  
  *   :py:meth:`~CloudTrail.Client.get_trail_status`

  
  *   :py:meth:`~CloudTrail.Client.get_waiter`

  
  *   :py:meth:`~CloudTrail.Client.list_public_keys`

  
  *   :py:meth:`~CloudTrail.Client.list_tags`

  
  *   :py:meth:`~CloudTrail.Client.lookup_events`

  
  *   :py:meth:`~CloudTrail.Client.put_event_selectors`

  
  *   :py:meth:`~CloudTrail.Client.remove_tags`

  
  *   :py:meth:`~CloudTrail.Client.start_logging`

  
  *   :py:meth:`~CloudTrail.Client.stop_logging`

  
  *   :py:meth:`~CloudTrail.Client.update_trail`

  

  .. py:method:: add_tags(**kwargs)

    

    Adds one or more tags to a trail, up to a limit of 50. Tags must be unique per trail. Overwrites an existing tag's value when a new value is specified for an existing tag key. If you specify a key without a value, the tag will be created with the specified key and a value of null. You can tag a trail that applies to all regions only from the region in which the trail was created (that is, from its home region).

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/AddTags>`_    


    **Request Syntax** 
    ::

      response = client.add_tags(
          ResourceId='string',
          TagsList=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type ResourceId: string
    :param ResourceId: **[REQUIRED]** 

      Specifies the ARN of the trail to which one or more tags will be added. The format of a trail ARN is:

       

       ``arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail``  

      

    
    :type TagsList: list
    :param TagsList: 

      Contains a list of CloudTrail tags, up to a limit of 50

      

    
      - *(dict) --* 

        A custom key-value pair associated with a resource such as a CloudTrail trail.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The key in a key-value pair. The key must be must be no longer than 128 Unicode characters. The key must be unique for the resource to which it applies.

          

        
        - **Value** *(string) --* 

          The value in a key-value pair of a tag. The value must be no longer than 256 Unicode characters.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Returns the objects or data listed below if successful. Otherwise, returns an error.

        
    

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


  .. py:method:: create_trail(**kwargs)

    

    Creates a trail that specifies the settings for delivery of log data to an Amazon S3 bucket. A maximum of five trails can exist in a region, irrespective of the region in which they were created.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/CreateTrail>`_    


    **Request Syntax** 
    ::

      response = client.create_trail(
          Name='string',
          S3BucketName='string',
          S3KeyPrefix='string',
          SnsTopicName='string',
          IncludeGlobalServiceEvents=True|False,
          IsMultiRegionTrail=True|False,
          EnableLogFileValidation=True|False,
          CloudWatchLogsLogGroupArn='string',
          CloudWatchLogsRoleArn='string',
          KmsKeyId='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      Specifies the name of the trail. The name must meet the following requirements:

       

       
      * Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-) 
       
      * Start with a letter or number, and end with a letter or number 
       
      * Be between 3 and 128 characters 
       
      * Have no adjacent periods, underscores or dashes. Names like ``my-_namespace`` and ``my--namespace`` are invalid. 
       
      * Not be in IP address format (for example, 192.168.5.4) 
       

      

    
    :type S3BucketName: string
    :param S3BucketName: **[REQUIRED]** 

      Specifies the name of the Amazon S3 bucket designated for publishing log files. See `Amazon S3 Bucket Naming Requirements <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/create_trail_naming_policy.html>`__ .

      

    
    :type S3KeyPrefix: string
    :param S3KeyPrefix: 

      Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see `Finding Your CloudTrail Log Files <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-find-log-files.html>`__ . The maximum length is 200 characters.

      

    
    :type SnsTopicName: string
    :param SnsTopicName: 

      Specifies the name of the Amazon SNS topic defined for notification of log file delivery. The maximum length is 256 characters.

      

    
    :type IncludeGlobalServiceEvents: boolean
    :param IncludeGlobalServiceEvents: 

      Specifies whether the trail is publishing events from global services such as IAM to the log files.

      

    
    :type IsMultiRegionTrail: boolean
    :param IsMultiRegionTrail: 

      Specifies whether the trail is created in the current region or in all regions. The default is false.

      

    
    :type EnableLogFileValidation: boolean
    :param EnableLogFileValidation: 

      Specifies whether log file integrity validation is enabled. The default is false.

       

      .. note::

         

        When you disable log file integrity validation, the chain of digest files is broken after one hour. CloudTrail will not create digest files for log files that were delivered during a period in which log file integrity validation was disabled. For example, if you enable log file integrity validation at noon on January 1, disable it at noon on January 2, and re-enable it at noon on January 10, digest files will not be created for the log files delivered from noon on January 2 to noon on January 10. The same applies whenever you stop CloudTrail logging or delete a trail.

         

      

    
    :type CloudWatchLogsLogGroupArn: string
    :param CloudWatchLogsLogGroupArn: 

      Specifies a log group name using an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs will be delivered. Not required unless you specify CloudWatchLogsRoleArn.

      

    
    :type CloudWatchLogsRoleArn: string
    :param CloudWatchLogsRoleArn: 

      Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group.

      

    
    :type KmsKeyId: string
    :param KmsKeyId: 

      Specifies the KMS key ID to use to encrypt the logs delivered by CloudTrail. The value can be an alias name prefixed by "alias/", a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.

       

      Examples:

       

       
      * alias/MyAliasName 
       
      * arn:aws:kms:us-east-1:123456789012:alias/MyAliasName 
       
      * arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012 
       
      * 12345678-1234-1234-1234-123456789012 
       

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Name': 'string',
            'S3BucketName': 'string',
            'S3KeyPrefix': 'string',
            'SnsTopicName': 'string',
            'SnsTopicARN': 'string',
            'IncludeGlobalServiceEvents': True|False,
            'IsMultiRegionTrail': True|False,
            'TrailARN': 'string',
            'LogFileValidationEnabled': True|False,
            'CloudWatchLogsLogGroupArn': 'string',
            'CloudWatchLogsRoleArn': 'string',
            'KmsKeyId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Returns the objects or data listed below if successful. Otherwise, returns an error.

        
        

        - **Name** *(string) --* 

          Specifies the name of the trail.

          
        

        - **S3BucketName** *(string) --* 

          Specifies the name of the Amazon S3 bucket designated for publishing log files.

          
        

        - **S3KeyPrefix** *(string) --* 

          Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see `Finding Your CloudTrail Log Files <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-find-log-files.html>`__ .

          
        

        - **SnsTopicName** *(string) --* 

          This field is deprecated. Use SnsTopicARN.

          
        

        - **SnsTopicARN** *(string) --* 

          Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send notifications when log files are delivered. The format of a topic ARN is:

           

           ``arn:aws:sns:us-east-1:123456789012:MyTopic``  

          
        

        - **IncludeGlobalServiceEvents** *(boolean) --* 

          Specifies whether the trail is publishing events from global services such as IAM to the log files.

          
        

        - **IsMultiRegionTrail** *(boolean) --* 

          Specifies whether the trail exists in one region or in all regions.

          
        

        - **TrailARN** *(string) --* 

          Specifies the ARN of the trail that was created. The format of a trail ARN is:

           

           ``arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail``  

          
        

        - **LogFileValidationEnabled** *(boolean) --* 

          Specifies whether log file integrity validation is enabled.

          
        

        - **CloudWatchLogsLogGroupArn** *(string) --* 

          Specifies the Amazon Resource Name (ARN) of the log group to which CloudTrail logs will be delivered.

          
        

        - **CloudWatchLogsRoleArn** *(string) --* 

          Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group.

          
        

        - **KmsKeyId** *(string) --* 

          Specifies the KMS key ID that encrypts the logs delivered by CloudTrail. The value is a fully specified ARN to a KMS key in the format:

           

           ``arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012``  

          
    

  .. py:method:: delete_trail(**kwargs)

    

    Deletes a trail. This operation must be called from the region in which the trail was created. ``DeleteTrail`` cannot be called on the shadow trails (replicated trails in other regions) of a trail that is enabled in all regions.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/DeleteTrail>`_    


    **Request Syntax** 
    ::

      response = client.delete_trail(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      Specifies the name or the CloudTrail ARN of the trail to be deleted. The format of a trail ARN is: ``arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail``  

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Returns the objects or data listed below if successful. Otherwise, returns an error.

        
    

  .. py:method:: describe_trails(**kwargs)

    

    Retrieves settings for the trail associated with the current region for your account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/DescribeTrails>`_    


    **Request Syntax** 
    ::

      response = client.describe_trails(
          trailNameList=[
              'string',
          ],
          includeShadowTrails=True|False
      )
    :type trailNameList: list
    :param trailNameList: 

      Specifies a list of trail names, trail ARNs, or both, of the trails to describe. The format of a trail ARN is:

       

       ``arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail``  

       

      If an empty list is specified, information for the trail in the current region is returned.

       

       
      * If an empty list is specified and ``IncludeShadowTrails`` is false, then information for all trails in the current region is returned. 
       
      * If an empty list is specified and IncludeShadowTrails is null or true, then information for all trails in the current region and any associated shadow trails in other regions is returned. 
       

       

      .. note::

         

        If one or more trail names are specified, information is returned only if the names match the names of trails belonging only to the current region. To return information about a trail in another region, you must specify its trail ARN.

         

      

    
      - *(string) --* 

      
  
    :type includeShadowTrails: boolean
    :param includeShadowTrails: 

      Specifies whether to include shadow trails in the response. A shadow trail is the replication in a region of a trail that was created in a different region. The default is true.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'trailList': [
                {
                    'Name': 'string',
                    'S3BucketName': 'string',
                    'S3KeyPrefix': 'string',
                    'SnsTopicName': 'string',
                    'SnsTopicARN': 'string',
                    'IncludeGlobalServiceEvents': True|False,
                    'IsMultiRegionTrail': True|False,
                    'HomeRegion': 'string',
                    'TrailARN': 'string',
                    'LogFileValidationEnabled': True|False,
                    'CloudWatchLogsLogGroupArn': 'string',
                    'CloudWatchLogsRoleArn': 'string',
                    'KmsKeyId': 'string',
                    'HasCustomEventSelectors': True|False
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Returns the objects or data listed below if successful. Otherwise, returns an error.

        
        

        - **trailList** *(list) --* 

          The list of trail objects.

          
          

          - *(dict) --* 

            The settings for a trail.

            
            

            - **Name** *(string) --* 

              Name of the trail set by calling  CreateTrail . The maximum length is 128 characters.

              
            

            - **S3BucketName** *(string) --* 

              Name of the Amazon S3 bucket into which CloudTrail delivers your trail files. See `Amazon S3 Bucket Naming Requirements <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/create_trail_naming_policy.html>`__ .

              
            

            - **S3KeyPrefix** *(string) --* 

              Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see `Finding Your CloudTrail Log Files <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-find-log-files.html>`__ .The maximum length is 200 characters.

              
            

            - **SnsTopicName** *(string) --* 

              This field is deprecated. Use SnsTopicARN.

              
            

            - **SnsTopicARN** *(string) --* 

              Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send notifications when log files are delivered. The format of a topic ARN is:

               

               ``arn:aws:sns:us-east-1:123456789012:MyTopic``  

              
            

            - **IncludeGlobalServiceEvents** *(boolean) --* 

              Set to **True** to include AWS API calls from AWS global services such as IAM. Otherwise, **False** .

              
            

            - **IsMultiRegionTrail** *(boolean) --* 

              Specifies whether the trail belongs only to one region or exists in all regions.

              
            

            - **HomeRegion** *(string) --* 

              The region in which the trail was created.

              
            

            - **TrailARN** *(string) --* 

              Specifies the ARN of the trail. The format of a trail ARN is:

               

               ``arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail``  

              
            

            - **LogFileValidationEnabled** *(boolean) --* 

              Specifies whether log file validation is enabled.

              
            

            - **CloudWatchLogsLogGroupArn** *(string) --* 

              Specifies an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs will be delivered.

              
            

            - **CloudWatchLogsRoleArn** *(string) --* 

              Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group.

              
            

            - **KmsKeyId** *(string) --* 

              Specifies the KMS key ID that encrypts the logs delivered by CloudTrail. The value is a fully specified ARN to a KMS key in the format:

               

               ``arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012``  

              
            

            - **HasCustomEventSelectors** *(boolean) --* 

              Specifies if the trail has custom event selectors.

              
        
      
    

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


  .. py:method:: get_event_selectors(**kwargs)

    

    Describes the settings for the event selectors that you configured for your trail. The information returned for your event selectors includes the following:

     

     
    * The S3 objects that you are logging for data events. 
     
    * If your event selector includes management events. 
     
    * If your event selector includes read-only events, write-only events, or all.  
     

     

    For more information, see `Logging Data and Management Events for Trails <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html>`__ in the *AWS CloudTrail User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/GetEventSelectors>`_    


    **Request Syntax** 
    ::

      response = client.get_event_selectors(
          TrailName='string'
      )
    :type TrailName: string
    :param TrailName: **[REQUIRED]** 

      Specifies the name of the trail or trail ARN. If you specify a trail name, the string must meet the following requirements:

       

       
      * Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-) 
       
      * Start with a letter or number, and end with a letter or number 
       
      * Be between 3 and 128 characters 
       
      * Have no adjacent periods, underscores or dashes. Names like ``my-_namespace`` and ``my--namespace`` are invalid. 
       
      * Not be in IP address format (for example, 192.168.5.4) 
       

       

      If you specify a trail ARN, it must be in the format:

       

       ``arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail``  

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TrailARN': 'string',
            'EventSelectors': [
                {
                    'ReadWriteType': 'ReadOnly'|'WriteOnly'|'All',
                    'IncludeManagementEvents': True|False,
                    'DataResources': [
                        {
                            'Type': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TrailARN** *(string) --* 

          The specified trail ARN that has the event selectors.

          
        

        - **EventSelectors** *(list) --* 

          The event selectors that are configured for the trail.

          
          

          - *(dict) --* 

            Use event selectors to specify whether you want your trail to log management and/or data events. When an event occurs in your account, CloudTrail evaluates the event selector for all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesn't match any event selector, the trail doesn't log the event.

             

            You can configure up to five event selectors for a trail.

            
            

            - **ReadWriteType** *(string) --* 

              Specify if you want your trail to log read-only events, write-only events, or all. For example, the EC2 ``GetConsoleOutput`` is a read-only API operation and ``RunInstances`` is a write-only API operation.

               

              By default, the value is ``All`` .

              
            

            - **IncludeManagementEvents** *(boolean) --* 

              Specify if you want your event selector to include management events for your trail.

               

              For more information, see `Management Events <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html#logging-management-events>`__ in the *AWS CloudTrail User Guide* .

               

              By default, the value is ``true`` .

              
            

            - **DataResources** *(list) --* 

              CloudTrail supports logging only data events for S3 objects. You can specify up to 250 S3 buckets and object prefixes for a trail.

               

              For more information, see `Data Events <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html#logging-data-events>`__ in the *AWS CloudTrail User Guide* .

              
              

              - *(dict) --* 

                The Amazon S3 objects that you specify in your event selectors for your trail to log data events. Data events are object-level API operations that access S3 objects, such as ``GetObject`` , ``DeleteObject`` , and ``PutObject`` . You can specify up to 250 S3 buckets and object prefixes for a trail. 

                 

                Example

                 

                 
                * You create an event selector for a trail and specify an S3 bucket and an empty prefix, such as ``arn:aws:s3:::bucket-1/`` . 
                 
                * You upload an image file to ``bucket-1`` . 
                 
                * The ``PutObject`` API operation occurs on an object in the S3 bucket that you specified in the event selector. The trail processes and logs the event. 
                 
                * You upload another image file to a different S3 bucket named ``arn:aws:s3:::bucket-2`` . 
                 
                * The event occurs on an object in an S3 bucket that you didn't specify in the event selector. The trail doesn’t log the event. 
                 

                
                

                - **Type** *(string) --* 

                  The resource type in which you want to log data events. You can specify only the following value: ``AWS::S3::Object`` .

                  
                

                - **Values** *(list) --* 

                  A list of ARN-like strings for the specified S3 objects.

                   

                  To log data events for all objects in an S3 bucket, specify the bucket and an empty object prefix such as ``arn:aws:s3:::bucket-1/`` . The trail logs data events for all objects in this S3 bucket.

                   

                  To log data events for specific objects, specify the S3 bucket and object prefix such as ``arn:aws:s3:::bucket-1/example-images`` . The trail logs data events for objects in this S3 bucket that match the prefix.

                  
                  

                  - *(string) --* 
              
            
          
        
      
    

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


  .. py:method:: get_trail_status(**kwargs)

    

    Returns a JSON-formatted list of information about the specified trail. Fields include information on delivery errors, Amazon SNS and Amazon S3 errors, and start and stop logging times for each trail. This operation returns trail status from a single region. To return trail status from all regions, you must call the operation on each region.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/GetTrailStatus>`_    


    **Request Syntax** 
    ::

      response = client.get_trail_status(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      Specifies the name or the CloudTrail ARN of the trail for which you are requesting status. To get the status of a shadow trail (a replication of the trail in another region), you must specify its ARN. The format of a trail ARN is:

       

       ``arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail``  

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'IsLogging': True|False,
            'LatestDeliveryError': 'string',
            'LatestNotificationError': 'string',
            'LatestDeliveryTime': datetime(2015, 1, 1),
            'LatestNotificationTime': datetime(2015, 1, 1),
            'StartLoggingTime': datetime(2015, 1, 1),
            'StopLoggingTime': datetime(2015, 1, 1),
            'LatestCloudWatchLogsDeliveryError': 'string',
            'LatestCloudWatchLogsDeliveryTime': datetime(2015, 1, 1),
            'LatestDigestDeliveryTime': datetime(2015, 1, 1),
            'LatestDigestDeliveryError': 'string',
            'LatestDeliveryAttemptTime': 'string',
            'LatestNotificationAttemptTime': 'string',
            'LatestNotificationAttemptSucceeded': 'string',
            'LatestDeliveryAttemptSucceeded': 'string',
            'TimeLoggingStarted': 'string',
            'TimeLoggingStopped': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Returns the objects or data listed below if successful. Otherwise, returns an error.

        
        

        - **IsLogging** *(boolean) --* 

          Whether the CloudTrail is currently logging AWS API calls.

          
        

        - **LatestDeliveryError** *(string) --* 

          Displays any Amazon S3 error that CloudTrail encountered when attempting to deliver log files to the designated bucket. For more information see the topic `Error Responses <http://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html>`__ in the Amazon S3 API Reference. 

           

          .. note::

             

            This error occurs only when there is a problem with the destination S3 bucket and will not occur for timeouts. To resolve the issue, create a new bucket and call ``UpdateTrail`` to specify the new bucket, or fix the existing objects so that CloudTrail can again write to the bucket.

             

          
        

        - **LatestNotificationError** *(string) --* 

          Displays any Amazon SNS error that CloudTrail encountered when attempting to send a notification. For more information about Amazon SNS errors, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/welcome.html>`__ . 

          
        

        - **LatestDeliveryTime** *(datetime) --* 

          Specifies the date and time that CloudTrail last delivered log files to an account's Amazon S3 bucket.

          
        

        - **LatestNotificationTime** *(datetime) --* 

          Specifies the date and time of the most recent Amazon SNS notification that CloudTrail has written a new log file to an account's Amazon S3 bucket.

          
        

        - **StartLoggingTime** *(datetime) --* 

          Specifies the most recent date and time when CloudTrail started recording API calls for an AWS account.

          
        

        - **StopLoggingTime** *(datetime) --* 

          Specifies the most recent date and time when CloudTrail stopped recording API calls for an AWS account.

          
        

        - **LatestCloudWatchLogsDeliveryError** *(string) --* 

          Displays any CloudWatch Logs error that CloudTrail encountered when attempting to deliver logs to CloudWatch Logs.

          
        

        - **LatestCloudWatchLogsDeliveryTime** *(datetime) --* 

          Displays the most recent date and time when CloudTrail delivered logs to CloudWatch Logs.

          
        

        - **LatestDigestDeliveryTime** *(datetime) --* 

          Specifies the date and time that CloudTrail last delivered a digest file to an account's Amazon S3 bucket.

          
        

        - **LatestDigestDeliveryError** *(string) --* 

          Displays any Amazon S3 error that CloudTrail encountered when attempting to deliver a digest file to the designated bucket. For more information see the topic `Error Responses <http://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html>`__ in the Amazon S3 API Reference. 

           

          .. note::

             

            This error occurs only when there is a problem with the destination S3 bucket and will not occur for timeouts. To resolve the issue, create a new bucket and call ``UpdateTrail`` to specify the new bucket, or fix the existing objects so that CloudTrail can again write to the bucket.

             

          
        

        - **LatestDeliveryAttemptTime** *(string) --* 

          This field is deprecated.

          
        

        - **LatestNotificationAttemptTime** *(string) --* 

          This field is deprecated.

          
        

        - **LatestNotificationAttemptSucceeded** *(string) --* 

          This field is deprecated.

          
        

        - **LatestDeliveryAttemptSucceeded** *(string) --* 

          This field is deprecated.

          
        

        - **TimeLoggingStarted** *(string) --* 

          This field is deprecated.

          
        

        - **TimeLoggingStopped** *(string) --* 

          This field is deprecated.

          
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: list_public_keys(**kwargs)

    

    Returns all public keys whose private keys were used to sign the digest files within the specified time range. The public key is needed to validate digest files that were signed with its corresponding private key.

     

    .. note::

       

      CloudTrail uses different private/public key pairs per region. Each digest file is signed with a private key unique to its region. Therefore, when you validate a digest file from a particular region, you must look in the same region for its corresponding public key.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/ListPublicKeys>`_    


    **Request Syntax** 
    ::

      response = client.list_public_keys(
          StartTime=datetime(2015, 1, 1),
          EndTime=datetime(2015, 1, 1),
          NextToken='string'
      )
    :type StartTime: datetime
    :param StartTime: 

      Optionally specifies, in UTC, the start of the time range to look up public keys for CloudTrail digest files. If not specified, the current time is used, and the current public key is returned.

      

    
    :type EndTime: datetime
    :param EndTime: 

      Optionally specifies, in UTC, the end of the time range to look up public keys for CloudTrail digest files. If not specified, the current time is used.

      

    
    :type NextToken: string
    :param NextToken: 

      Reserved for future use.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'PublicKeyList': [
                {
                    'Value': b'bytes',
                    'ValidityStartTime': datetime(2015, 1, 1),
                    'ValidityEndTime': datetime(2015, 1, 1),
                    'Fingerprint': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Returns the objects or data listed below if successful. Otherwise, returns an error.

        
        

        - **PublicKeyList** *(list) --* 

          Contains an array of PublicKey objects.

           

          .. note::

             

            The returned public keys may have validity time ranges that overlap.

             

          
          

          - *(dict) --* 

            Contains information about a returned public key.

            
            

            - **Value** *(bytes) --* 

              The DER encoded public key value in PKCS#1 format.

              
            

            - **ValidityStartTime** *(datetime) --* 

              The starting time of validity of the public key.

              
            

            - **ValidityEndTime** *(datetime) --* 

              The ending time of validity of the public key.

              
            

            - **Fingerprint** *(string) --* 

              The fingerprint of the public key.

              
        
      
        

        - **NextToken** *(string) --* 

          Reserved for future use.

          
    

  .. py:method:: list_tags(**kwargs)

    

    Lists the tags for the trail in the current region.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/ListTags>`_    


    **Request Syntax** 
    ::

      response = client.list_tags(
          ResourceIdList=[
              'string',
          ],
          NextToken='string'
      )
    :type ResourceIdList: list
    :param ResourceIdList: **[REQUIRED]** 

      Specifies a list of trail ARNs whose tags will be listed. The list has a limit of 20 ARNs. The format of a trail ARN is:

       

       ``arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail``  

      

    
      - *(string) --* 

      
  
    :type NextToken: string
    :param NextToken: 

      Reserved for future use.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResourceTagList': [
                {
                    'ResourceId': 'string',
                    'TagsList': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Returns the objects or data listed below if successful. Otherwise, returns an error.

        
        

        - **ResourceTagList** *(list) --* 

          A list of resource tags.

          
          

          - *(dict) --* 

            A resource tag.

            
            

            - **ResourceId** *(string) --* 

              Specifies the ARN of the resource.

              
            

            - **TagsList** *(list) --* 

              A list of tags.

              
              

              - *(dict) --* 

                A custom key-value pair associated with a resource such as a CloudTrail trail.

                
                

                - **Key** *(string) --* 

                  The key in a key-value pair. The key must be must be no longer than 128 Unicode characters. The key must be unique for the resource to which it applies.

                  
                

                - **Value** *(string) --* 

                  The value in a key-value pair of a tag. The value must be no longer than 256 Unicode characters.

                  
            
          
        
      
        

        - **NextToken** *(string) --* 

          Reserved for future use.

          
    

  .. py:method:: lookup_events(**kwargs)

    

    Looks up API activity events captured by CloudTrail that create, update, or delete resources in your account. Events for a region can be looked up for the times in which you had CloudTrail turned on in that region during the last seven days. Lookup supports the following attributes:

     

     
    * Event ID 
     
    * Event name 
     
    * Event source 
     
    * Resource name 
     
    * Resource type 
     
    * User name 
     

     

    All attributes are optional. The default number of results returned is 10, with a maximum of 50 possible. The response includes a token that you can use to get the next page of results.

     

    .. warning::

       

      The rate of lookup requests is limited to one per second per account. If this limit is exceeded, a throttling error occurs.

       

     

    .. warning::

       

      Events that occurred during the selected time range will not be available for lookup if CloudTrail logging was not enabled when the events occurred.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/LookupEvents>`_    


    **Request Syntax** 
    ::

      response = client.lookup_events(
          LookupAttributes=[
              {
                  'AttributeKey': 'EventId'|'EventName'|'Username'|'ResourceType'|'ResourceName'|'EventSource',
                  'AttributeValue': 'string'
              },
          ],
          StartTime=datetime(2015, 1, 1),
          EndTime=datetime(2015, 1, 1),
          MaxResults=123,
          NextToken='string'
      )
    :type LookupAttributes: list
    :param LookupAttributes: 

      Contains a list of lookup attributes. Currently the list can contain only one item.

      

    
      - *(dict) --* 

        Specifies an attribute and value that filter the events returned.

        

      
        - **AttributeKey** *(string) --* **[REQUIRED]** 

          Specifies an attribute on which to filter the events returned.

          

        
        - **AttributeValue** *(string) --* **[REQUIRED]** 

          Specifies a value for the specified AttributeKey.

          

        
      
  
    :type StartTime: datetime
    :param StartTime: 

      Specifies that only events that occur after or at the specified time are returned. If the specified start time is after the specified end time, an error is returned.

      

    
    :type EndTime: datetime
    :param EndTime: 

      Specifies that only events that occur before or at the specified time are returned. If the specified end time is before the specified start time, an error is returned.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The number of events to return. Possible values are 1 through 50. The default is 10.

      

    
    :type NextToken: string
    :param NextToken: 

      The token to use to get the next page of results after a previous API call. This token must be passed in with the same parameters that were specified in the the original call. For example, if the original call specified an AttributeKey of 'Username' with a value of 'root', the call with NextToken should include those same parameters.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Events': [
                {
                    'EventId': 'string',
                    'EventName': 'string',
                    'EventTime': datetime(2015, 1, 1),
                    'EventSource': 'string',
                    'Username': 'string',
                    'Resources': [
                        {
                            'ResourceType': 'string',
                            'ResourceName': 'string'
                        },
                    ],
                    'CloudTrailEvent': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains a response to a LookupEvents action.

        
        

        - **Events** *(list) --* 

          A list of events returned based on the lookup attributes specified and the CloudTrail event. The events list is sorted by time. The most recent event is listed first.

          
          

          - *(dict) --* 

            Contains information about an event that was returned by a lookup request. The result includes a representation of a CloudTrail event.

            
            

            - **EventId** *(string) --* 

              The CloudTrail ID of the event returned.

              
            

            - **EventName** *(string) --* 

              The name of the event returned.

              
            

            - **EventTime** *(datetime) --* 

              The date and time of the event returned.

              
            

            - **EventSource** *(string) --* 

              The AWS service that the request was made to.

              
            

            - **Username** *(string) --* 

              A user name or role name of the requester that called the API in the event returned.

              
            

            - **Resources** *(list) --* 

              A list of resources referenced by the event returned.

              
              

              - *(dict) --* 

                Specifies the type and name of a resource referenced by an event.

                
                

                - **ResourceType** *(string) --* 

                  The type of a resource referenced by the event returned. When the resource type cannot be determined, null is returned. Some examples of resource types are: **Instance** for EC2, **Trail** for CloudTrail, **DBInstance** for RDS, and **AccessKey** for IAM. For a list of resource types supported for event lookup, see `Resource Types Supported for Event Lookup <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/lookup_supported_resourcetypes.html>`__ .

                  
                

                - **ResourceName** *(string) --* 

                  The name of the resource referenced by the event returned. These are user-created names whose values will depend on the environment. For example, the resource name might be "auto-scaling-test-group" for an Auto Scaling Group or "i-1234567" for an EC2 Instance.

                  
            
          
            

            - **CloudTrailEvent** *(string) --* 

              A JSON string that contains a representation of the event returned.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use to get the next page of results after a previous API call. If the token does not appear, there are no more results to return. The token must be passed in with the same parameters as the previous call. For example, if the original call specified an AttributeKey of 'Username' with a value of 'root', the call with NextToken should include those same parameters.

          
    

  .. py:method:: put_event_selectors(**kwargs)

    

    Configures an event selector for your trail. Use event selectors to specify whether you want your trail to log management and/or data events. When an event occurs in your account, CloudTrail evaluates the event selectors in all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesn't match any event selector, the trail doesn't log the event. 

     

    Example

     

     
    * You create an event selector for a trail and specify that you want write-only events. 
     
    * The EC2 ``GetConsoleOutput`` and ``RunInstances`` API operations occur in your account. 
     
    * CloudTrail evaluates whether the events match your event selectors. 
     
    * The ``RunInstances`` is a write-only event and it matches your event selector. The trail logs the event. 
     
    * The ``GetConsoleOutput`` is a read-only event but it doesn't match your event selector. The trail doesn't log the event.  
     

     

    The ``PutEventSelectors`` operation must be called from the region in which the trail was created; otherwise, an ``InvalidHomeRegionException`` is thrown.

     

    You can configure up to five event selectors for each trail. For more information, see `Logging Data and Management Events for Trails <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html>`__ in the *AWS CloudTrail User Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/PutEventSelectors>`_    


    **Request Syntax** 
    ::

      response = client.put_event_selectors(
          TrailName='string',
          EventSelectors=[
              {
                  'ReadWriteType': 'ReadOnly'|'WriteOnly'|'All',
                  'IncludeManagementEvents': True|False,
                  'DataResources': [
                      {
                          'Type': 'string',
                          'Values': [
                              'string',
                          ]
                      },
                  ]
              },
          ]
      )
    :type TrailName: string
    :param TrailName: **[REQUIRED]** 

      Specifies the name of the trail or trail ARN. If you specify a trail name, the string must meet the following requirements:

       

       
      * Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-) 
       
      * Start with a letter or number, and end with a letter or number 
       
      * Be between 3 and 128 characters 
       
      * Have no adjacent periods, underscores or dashes. Names like ``my-_namespace`` and ``my--namespace`` are invalid. 
       
      * Not be in IP address format (for example, 192.168.5.4) 
       

       

      If you specify a trail ARN, it must be in the format:

       

       ``arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail``  

      

    
    :type EventSelectors: list
    :param EventSelectors: **[REQUIRED]** 

      Specifies the settings for your event selectors. You can configure up to five event selectors for a trail.

      

    
      - *(dict) --* 

        Use event selectors to specify whether you want your trail to log management and/or data events. When an event occurs in your account, CloudTrail evaluates the event selector for all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesn't match any event selector, the trail doesn't log the event.

         

        You can configure up to five event selectors for a trail.

        

      
        - **ReadWriteType** *(string) --* 

          Specify if you want your trail to log read-only events, write-only events, or all. For example, the EC2 ``GetConsoleOutput`` is a read-only API operation and ``RunInstances`` is a write-only API operation.

           

          By default, the value is ``All`` .

          

        
        - **IncludeManagementEvents** *(boolean) --* 

          Specify if you want your event selector to include management events for your trail.

           

          For more information, see `Management Events <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html#logging-management-events>`__ in the *AWS CloudTrail User Guide* .

           

          By default, the value is ``true`` .

          

        
        - **DataResources** *(list) --* 

          CloudTrail supports logging only data events for S3 objects. You can specify up to 250 S3 buckets and object prefixes for a trail.

           

          For more information, see `Data Events <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html#logging-data-events>`__ in the *AWS CloudTrail User Guide* .

          

        
          - *(dict) --* 

            The Amazon S3 objects that you specify in your event selectors for your trail to log data events. Data events are object-level API operations that access S3 objects, such as ``GetObject`` , ``DeleteObject`` , and ``PutObject`` . You can specify up to 250 S3 buckets and object prefixes for a trail. 

             

            Example

             

             
            * You create an event selector for a trail and specify an S3 bucket and an empty prefix, such as ``arn:aws:s3:::bucket-1/`` . 
             
            * You upload an image file to ``bucket-1`` . 
             
            * The ``PutObject`` API operation occurs on an object in the S3 bucket that you specified in the event selector. The trail processes and logs the event. 
             
            * You upload another image file to a different S3 bucket named ``arn:aws:s3:::bucket-2`` . 
             
            * The event occurs on an object in an S3 bucket that you didn't specify in the event selector. The trail doesn’t log the event. 
             

            

          
            - **Type** *(string) --* 

              The resource type in which you want to log data events. You can specify only the following value: ``AWS::S3::Object`` .

              

            
            - **Values** *(list) --* 

              A list of ARN-like strings for the specified S3 objects.

               

              To log data events for all objects in an S3 bucket, specify the bucket and an empty object prefix such as ``arn:aws:s3:::bucket-1/`` . The trail logs data events for all objects in this S3 bucket.

               

              To log data events for specific objects, specify the S3 bucket and object prefix such as ``arn:aws:s3:::bucket-1/example-images`` . The trail logs data events for objects in this S3 bucket that match the prefix.

              

            
              - *(string) --* 

              
          
          
      
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TrailARN': 'string',
            'EventSelectors': [
                {
                    'ReadWriteType': 'ReadOnly'|'WriteOnly'|'All',
                    'IncludeManagementEvents': True|False,
                    'DataResources': [
                        {
                            'Type': 'string',
                            'Values': [
                                'string',
                            ]
                        },
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TrailARN** *(string) --* 

          Specifies the ARN of the trail that was updated with event selectors. The format of a trail ARN is:

           

           ``arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail``  

          
        

        - **EventSelectors** *(list) --* 

          Specifies the event selectors configured for your trail.

          
          

          - *(dict) --* 

            Use event selectors to specify whether you want your trail to log management and/or data events. When an event occurs in your account, CloudTrail evaluates the event selector for all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesn't match any event selector, the trail doesn't log the event.

             

            You can configure up to five event selectors for a trail.

            
            

            - **ReadWriteType** *(string) --* 

              Specify if you want your trail to log read-only events, write-only events, or all. For example, the EC2 ``GetConsoleOutput`` is a read-only API operation and ``RunInstances`` is a write-only API operation.

               

              By default, the value is ``All`` .

              
            

            - **IncludeManagementEvents** *(boolean) --* 

              Specify if you want your event selector to include management events for your trail.

               

              For more information, see `Management Events <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html#logging-management-events>`__ in the *AWS CloudTrail User Guide* .

               

              By default, the value is ``true`` .

              
            

            - **DataResources** *(list) --* 

              CloudTrail supports logging only data events for S3 objects. You can specify up to 250 S3 buckets and object prefixes for a trail.

               

              For more information, see `Data Events <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-and-data-events-with-cloudtrail.html#logging-data-events>`__ in the *AWS CloudTrail User Guide* .

              
              

              - *(dict) --* 

                The Amazon S3 objects that you specify in your event selectors for your trail to log data events. Data events are object-level API operations that access S3 objects, such as ``GetObject`` , ``DeleteObject`` , and ``PutObject`` . You can specify up to 250 S3 buckets and object prefixes for a trail. 

                 

                Example

                 

                 
                * You create an event selector for a trail and specify an S3 bucket and an empty prefix, such as ``arn:aws:s3:::bucket-1/`` . 
                 
                * You upload an image file to ``bucket-1`` . 
                 
                * The ``PutObject`` API operation occurs on an object in the S3 bucket that you specified in the event selector. The trail processes and logs the event. 
                 
                * You upload another image file to a different S3 bucket named ``arn:aws:s3:::bucket-2`` . 
                 
                * The event occurs on an object in an S3 bucket that you didn't specify in the event selector. The trail doesn’t log the event. 
                 

                
                

                - **Type** *(string) --* 

                  The resource type in which you want to log data events. You can specify only the following value: ``AWS::S3::Object`` .

                  
                

                - **Values** *(list) --* 

                  A list of ARN-like strings for the specified S3 objects.

                   

                  To log data events for all objects in an S3 bucket, specify the bucket and an empty object prefix such as ``arn:aws:s3:::bucket-1/`` . The trail logs data events for all objects in this S3 bucket.

                   

                  To log data events for specific objects, specify the S3 bucket and object prefix such as ``arn:aws:s3:::bucket-1/example-images`` . The trail logs data events for objects in this S3 bucket that match the prefix.

                  
                  

                  - *(string) --* 
              
            
          
        
      
    

  .. py:method:: remove_tags(**kwargs)

    

    Removes the specified tags from a trail.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/RemoveTags>`_    


    **Request Syntax** 
    ::

      response = client.remove_tags(
          ResourceId='string',
          TagsList=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type ResourceId: string
    :param ResourceId: **[REQUIRED]** 

      Specifies the ARN of the trail from which tags should be removed. The format of a trail ARN is:

       

       ``arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail``  

      

    
    :type TagsList: list
    :param TagsList: 

      Specifies a list of tags to be removed.

      

    
      - *(dict) --* 

        A custom key-value pair associated with a resource such as a CloudTrail trail.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The key in a key-value pair. The key must be must be no longer than 128 Unicode characters. The key must be unique for the resource to which it applies.

          

        
        - **Value** *(string) --* 

          The value in a key-value pair of a tag. The value must be no longer than 256 Unicode characters.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Returns the objects or data listed below if successful. Otherwise, returns an error.

        
    

  .. py:method:: start_logging(**kwargs)

    

    Starts the recording of AWS API calls and log file delivery for a trail. For a trail that is enabled in all regions, this operation must be called from the region in which the trail was created. This operation cannot be called on the shadow trails (replicated trails in other regions) of a trail that is enabled in all regions.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/StartLogging>`_    


    **Request Syntax** 
    ::

      response = client.start_logging(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      Specifies the name or the CloudTrail ARN of the trail for which CloudTrail logs AWS API calls. The format of a trail ARN is:

       

       ``arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail``  

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Returns the objects or data listed below if successful. Otherwise, returns an error.

        
    

  .. py:method:: stop_logging(**kwargs)

    

    Suspends the recording of AWS API calls and log file delivery for the specified trail. Under most circumstances, there is no need to use this action. You can update a trail without stopping it first. This action is the only way to stop recording. For a trail enabled in all regions, this operation must be called from the region in which the trail was created, or an ``InvalidHomeRegionException`` will occur. This operation cannot be called on the shadow trails (replicated trails in other regions) of a trail enabled in all regions.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/StopLogging>`_    


    **Request Syntax** 
    ::

      response = client.stop_logging(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      Specifies the name or the CloudTrail ARN of the trail for which CloudTrail will stop logging AWS API calls. The format of a trail ARN is:

       

       ``arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail``  

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        Returns the objects or data listed below if successful. Otherwise, returns an error.

        
    

  .. py:method:: update_trail(**kwargs)

    

    Updates the settings that specify delivery of log files. Changes to a trail do not require stopping the CloudTrail service. Use this action to designate an existing bucket for log delivery. If the existing bucket has previously been a target for CloudTrail log files, an IAM policy exists for the bucket. ``UpdateTrail`` must be called from the region in which the trail was created; otherwise, an ``InvalidHomeRegionException`` is thrown.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/UpdateTrail>`_    


    **Request Syntax** 
    ::

      response = client.update_trail(
          Name='string',
          S3BucketName='string',
          S3KeyPrefix='string',
          SnsTopicName='string',
          IncludeGlobalServiceEvents=True|False,
          IsMultiRegionTrail=True|False,
          EnableLogFileValidation=True|False,
          CloudWatchLogsLogGroupArn='string',
          CloudWatchLogsRoleArn='string',
          KmsKeyId='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      Specifies the name of the trail or trail ARN. If ``Name`` is a trail name, the string must meet the following requirements:

       

       
      * Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-) 
       
      * Start with a letter or number, and end with a letter or number 
       
      * Be between 3 and 128 characters 
       
      * Have no adjacent periods, underscores or dashes. Names like ``my-_namespace`` and ``my--namespace`` are invalid. 
       
      * Not be in IP address format (for example, 192.168.5.4) 
       

       

      If ``Name`` is a trail ARN, it must be in the format:

       

       ``arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail``  

      

    
    :type S3BucketName: string
    :param S3BucketName: 

      Specifies the name of the Amazon S3 bucket designated for publishing log files. See `Amazon S3 Bucket Naming Requirements <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/create_trail_naming_policy.html>`__ .

      

    
    :type S3KeyPrefix: string
    :param S3KeyPrefix: 

      Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see `Finding Your CloudTrail Log Files <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-find-log-files.html>`__ . The maximum length is 200 characters.

      

    
    :type SnsTopicName: string
    :param SnsTopicName: 

      Specifies the name of the Amazon SNS topic defined for notification of log file delivery. The maximum length is 256 characters.

      

    
    :type IncludeGlobalServiceEvents: boolean
    :param IncludeGlobalServiceEvents: 

      Specifies whether the trail is publishing events from global services such as IAM to the log files.

      

    
    :type IsMultiRegionTrail: boolean
    :param IsMultiRegionTrail: 

      Specifies whether the trail applies only to the current region or to all regions. The default is false. If the trail exists only in the current region and this value is set to true, shadow trails (replications of the trail) will be created in the other regions. If the trail exists in all regions and this value is set to false, the trail will remain in the region where it was created, and its shadow trails in other regions will be deleted.

      

    
    :type EnableLogFileValidation: boolean
    :param EnableLogFileValidation: 

      Specifies whether log file validation is enabled. The default is false.

       

      .. note::

         

        When you disable log file integrity validation, the chain of digest files is broken after one hour. CloudTrail will not create digest files for log files that were delivered during a period in which log file integrity validation was disabled. For example, if you enable log file integrity validation at noon on January 1, disable it at noon on January 2, and re-enable it at noon on January 10, digest files will not be created for the log files delivered from noon on January 2 to noon on January 10. The same applies whenever you stop CloudTrail logging or delete a trail.

         

      

    
    :type CloudWatchLogsLogGroupArn: string
    :param CloudWatchLogsLogGroupArn: 

      Specifies a log group name using an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs will be delivered. Not required unless you specify CloudWatchLogsRoleArn.

      

    
    :type CloudWatchLogsRoleArn: string
    :param CloudWatchLogsRoleArn: 

      Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group.

      

    
    :type KmsKeyId: string
    :param KmsKeyId: 

      Specifies the KMS key ID to use to encrypt the logs delivered by CloudTrail. The value can be an alias name prefixed by "alias/", a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.

       

      Examples:

       

       
      * alias/MyAliasName 
       
      * arn:aws:kms:us-east-1:123456789012:alias/MyAliasName 
       
      * arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012 
       
      * 12345678-1234-1234-1234-123456789012 
       

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Name': 'string',
            'S3BucketName': 'string',
            'S3KeyPrefix': 'string',
            'SnsTopicName': 'string',
            'SnsTopicARN': 'string',
            'IncludeGlobalServiceEvents': True|False,
            'IsMultiRegionTrail': True|False,
            'TrailARN': 'string',
            'LogFileValidationEnabled': True|False,
            'CloudWatchLogsLogGroupArn': 'string',
            'CloudWatchLogsRoleArn': 'string',
            'KmsKeyId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Returns the objects or data listed below if successful. Otherwise, returns an error.

        
        

        - **Name** *(string) --* 

          Specifies the name of the trail.

          
        

        - **S3BucketName** *(string) --* 

          Specifies the name of the Amazon S3 bucket designated for publishing log files.

          
        

        - **S3KeyPrefix** *(string) --* 

          Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see `Finding Your CloudTrail Log Files <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-find-log-files.html>`__ .

          
        

        - **SnsTopicName** *(string) --* 

          This field is deprecated. Use SnsTopicARN.

          
        

        - **SnsTopicARN** *(string) --* 

          Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send notifications when log files are delivered. The format of a topic ARN is:

           

           ``arn:aws:sns:us-east-1:123456789012:MyTopic``  

          
        

        - **IncludeGlobalServiceEvents** *(boolean) --* 

          Specifies whether the trail is publishing events from global services such as IAM to the log files.

          
        

        - **IsMultiRegionTrail** *(boolean) --* 

          Specifies whether the trail exists in one region or in all regions.

          
        

        - **TrailARN** *(string) --* 

          Specifies the ARN of the trail that was updated. The format of a trail ARN is:

           

           ``arn:aws:cloudtrail:us-east-1:123456789012:trail/MyTrail``  

          
        

        - **LogFileValidationEnabled** *(boolean) --* 

          Specifies whether log file integrity validation is enabled.

          
        

        - **CloudWatchLogsLogGroupArn** *(string) --* 

          Specifies the Amazon Resource Name (ARN) of the log group to which CloudTrail logs will be delivered.

          
        

        - **CloudWatchLogsRoleArn** *(string) --* 

          Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group.

          
        

        - **KmsKeyId** *(string) --* 

          Specifies the KMS key ID that encrypts the logs delivered by CloudTrail. The value is a fully specified ARN to a KMS key in the format:

           

           ``arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012``  

          
    

==========
Paginators
==========


The available paginators are:

* :py:class:`CloudTrail.Paginator.LookupEvents`



.. py:class:: CloudTrail.Paginator.LookupEvents

  ::

    
    paginator = client.get_paginator('lookup_events')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`CloudTrail.Client.lookup_events`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/LookupEvents>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          LookupAttributes=[
              {
                  'AttributeKey': 'EventId'|'EventName'|'Username'|'ResourceType'|'ResourceName'|'EventSource',
                  'AttributeValue': 'string'
              },
          ],
          StartTime=datetime(2015, 1, 1),
          EndTime=datetime(2015, 1, 1),
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type LookupAttributes: list
    :param LookupAttributes: 

      Contains a list of lookup attributes. Currently the list can contain only one item.

      

    
      - *(dict) --* 

        Specifies an attribute and value that filter the events returned.

        

      
        - **AttributeKey** *(string) --* **[REQUIRED]** 

          Specifies an attribute on which to filter the events returned.

          

        
        - **AttributeValue** *(string) --* **[REQUIRED]** 

          Specifies a value for the specified AttributeKey.

          

        
      
  
    :type StartTime: datetime
    :param StartTime: 

      Specifies that only events that occur after or at the specified time are returned. If the specified start time is after the specified end time, an error is returned.

      

    
    :type EndTime: datetime
    :param EndTime: 

      Specifies that only events that occur before or at the specified time are returned. If the specified end time is before the specified start time, an error is returned.

      

    
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
                    'EventId': 'string',
                    'EventName': 'string',
                    'EventTime': datetime(2015, 1, 1),
                    'EventSource': 'string',
                    'Username': 'string',
                    'Resources': [
                        {
                            'ResourceType': 'string',
                            'ResourceName': 'string'
                        },
                    ],
                    'CloudTrailEvent': 'string'
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 

        Contains a response to a LookupEvents action.

        
        

        - **Events** *(list) --* 

          A list of events returned based on the lookup attributes specified and the CloudTrail event. The events list is sorted by time. The most recent event is listed first.

          
          

          - *(dict) --* 

            Contains information about an event that was returned by a lookup request. The result includes a representation of a CloudTrail event.

            
            

            - **EventId** *(string) --* 

              The CloudTrail ID of the event returned.

              
            

            - **EventName** *(string) --* 

              The name of the event returned.

              
            

            - **EventTime** *(datetime) --* 

              The date and time of the event returned.

              
            

            - **EventSource** *(string) --* 

              The AWS service that the request was made to.

              
            

            - **Username** *(string) --* 

              A user name or role name of the requester that called the API in the event returned.

              
            

            - **Resources** *(list) --* 

              A list of resources referenced by the event returned.

              
              

              - *(dict) --* 

                Specifies the type and name of a resource referenced by an event.

                
                

                - **ResourceType** *(string) --* 

                  The type of a resource referenced by the event returned. When the resource type cannot be determined, null is returned. Some examples of resource types are: **Instance** for EC2, **Trail** for CloudTrail, **DBInstance** for RDS, and **AccessKey** for IAM. For a list of resource types supported for event lookup, see `Resource Types Supported for Event Lookup <http://docs.aws.amazon.com/awscloudtrail/latest/userguide/lookup_supported_resourcetypes.html>`__ .

                  
                

                - **ResourceName** *(string) --* 

                  The name of the resource referenced by the event returned. These are user-created names whose values will depend on the environment. For example, the resource name might be "auto-scaling-test-group" for an Auto Scaling Group or "i-1234567" for an EC2 Instance.

                  
            
          
            

            - **CloudTrailEvent** *(string) --* 

              A JSON string that contains a representation of the event returned.

              
        
      
    