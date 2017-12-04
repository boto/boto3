

***
SES
***

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: SES.Client

  A low-level client representing Amazon Simple Email Service (SES)::

    
    import boto3
    
    client = boto3.client('ses')

  
  These are the available methods:
  
  *   :py:meth:`~SES.Client.can_paginate`

  
  *   :py:meth:`~SES.Client.clone_receipt_rule_set`

  
  *   :py:meth:`~SES.Client.create_configuration_set`

  
  *   :py:meth:`~SES.Client.create_configuration_set_event_destination`

  
  *   :py:meth:`~SES.Client.create_configuration_set_tracking_options`

  
  *   :py:meth:`~SES.Client.create_custom_verification_email_template`

  
  *   :py:meth:`~SES.Client.create_receipt_filter`

  
  *   :py:meth:`~SES.Client.create_receipt_rule`

  
  *   :py:meth:`~SES.Client.create_receipt_rule_set`

  
  *   :py:meth:`~SES.Client.create_template`

  
  *   :py:meth:`~SES.Client.delete_configuration_set`

  
  *   :py:meth:`~SES.Client.delete_configuration_set_event_destination`

  
  *   :py:meth:`~SES.Client.delete_configuration_set_tracking_options`

  
  *   :py:meth:`~SES.Client.delete_custom_verification_email_template`

  
  *   :py:meth:`~SES.Client.delete_identity`

  
  *   :py:meth:`~SES.Client.delete_identity_policy`

  
  *   :py:meth:`~SES.Client.delete_receipt_filter`

  
  *   :py:meth:`~SES.Client.delete_receipt_rule`

  
  *   :py:meth:`~SES.Client.delete_receipt_rule_set`

  
  *   :py:meth:`~SES.Client.delete_template`

  
  *   :py:meth:`~SES.Client.delete_verified_email_address`

  
  *   :py:meth:`~SES.Client.describe_active_receipt_rule_set`

  
  *   :py:meth:`~SES.Client.describe_configuration_set`

  
  *   :py:meth:`~SES.Client.describe_receipt_rule`

  
  *   :py:meth:`~SES.Client.describe_receipt_rule_set`

  
  *   :py:meth:`~SES.Client.generate_presigned_url`

  
  *   :py:meth:`~SES.Client.get_account_sending_enabled`

  
  *   :py:meth:`~SES.Client.get_custom_verification_email_template`

  
  *   :py:meth:`~SES.Client.get_identity_dkim_attributes`

  
  *   :py:meth:`~SES.Client.get_identity_mail_from_domain_attributes`

  
  *   :py:meth:`~SES.Client.get_identity_notification_attributes`

  
  *   :py:meth:`~SES.Client.get_identity_policies`

  
  *   :py:meth:`~SES.Client.get_identity_verification_attributes`

  
  *   :py:meth:`~SES.Client.get_paginator`

  
  *   :py:meth:`~SES.Client.get_send_quota`

  
  *   :py:meth:`~SES.Client.get_send_statistics`

  
  *   :py:meth:`~SES.Client.get_template`

  
  *   :py:meth:`~SES.Client.get_waiter`

  
  *   :py:meth:`~SES.Client.list_configuration_sets`

  
  *   :py:meth:`~SES.Client.list_custom_verification_email_templates`

  
  *   :py:meth:`~SES.Client.list_identities`

  
  *   :py:meth:`~SES.Client.list_identity_policies`

  
  *   :py:meth:`~SES.Client.list_receipt_filters`

  
  *   :py:meth:`~SES.Client.list_receipt_rule_sets`

  
  *   :py:meth:`~SES.Client.list_templates`

  
  *   :py:meth:`~SES.Client.list_verified_email_addresses`

  
  *   :py:meth:`~SES.Client.put_identity_policy`

  
  *   :py:meth:`~SES.Client.reorder_receipt_rule_set`

  
  *   :py:meth:`~SES.Client.send_bounce`

  
  *   :py:meth:`~SES.Client.send_bulk_templated_email`

  
  *   :py:meth:`~SES.Client.send_custom_verification_email`

  
  *   :py:meth:`~SES.Client.send_email`

  
  *   :py:meth:`~SES.Client.send_raw_email`

  
  *   :py:meth:`~SES.Client.send_templated_email`

  
  *   :py:meth:`~SES.Client.set_active_receipt_rule_set`

  
  *   :py:meth:`~SES.Client.set_identity_dkim_enabled`

  
  *   :py:meth:`~SES.Client.set_identity_feedback_forwarding_enabled`

  
  *   :py:meth:`~SES.Client.set_identity_headers_in_notifications_enabled`

  
  *   :py:meth:`~SES.Client.set_identity_mail_from_domain`

  
  *   :py:meth:`~SES.Client.set_identity_notification_topic`

  
  *   :py:meth:`~SES.Client.set_receipt_rule_position`

  
  *   :py:meth:`~SES.Client.test_render_template`

  
  *   :py:meth:`~SES.Client.update_account_sending_enabled`

  
  *   :py:meth:`~SES.Client.update_configuration_set_event_destination`

  
  *   :py:meth:`~SES.Client.update_configuration_set_reputation_metrics_enabled`

  
  *   :py:meth:`~SES.Client.update_configuration_set_sending_enabled`

  
  *   :py:meth:`~SES.Client.update_configuration_set_tracking_options`

  
  *   :py:meth:`~SES.Client.update_custom_verification_email_template`

  
  *   :py:meth:`~SES.Client.update_receipt_rule`

  
  *   :py:meth:`~SES.Client.update_template`

  
  *   :py:meth:`~SES.Client.verify_domain_dkim`

  
  *   :py:meth:`~SES.Client.verify_domain_identity`

  
  *   :py:meth:`~SES.Client.verify_email_address`

  
  *   :py:meth:`~SES.Client.verify_email_identity`

  

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


  .. py:method:: clone_receipt_rule_set(**kwargs)

    

    Creates a receipt rule set by cloning an existing one. All receipt rules and configurations are copied to the new receipt rule set and are completely independent of the source rule set.

     

    For information about setting up rule sets, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rule-set.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/CloneReceiptRuleSet>`_    


    **Request Syntax** 
    ::

      response = client.clone_receipt_rule_set(
          RuleSetName='string',
          OriginalRuleSetName='string'
      )
    :type RuleSetName: string
    :param RuleSetName: **[REQUIRED]** 

      The name of the rule set to create. The name must:

       

       
      * Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-). 
       
      * Start and end with a letter or number. 
       
      * Contain less than 64 characters. 
       

      

    
    :type OriginalRuleSetName: string
    :param OriginalRuleSetName: **[REQUIRED]** 

      The name of the rule set to clone.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

    **Examples** 

    The following example creates a receipt rule set by cloning an existing one:
    ::

      response = client.clone_receipt_rule_set(
          OriginalRuleSetName='RuleSetToClone',
          RuleSetName='RuleSetToCreate',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_configuration_set(**kwargs)

    

    Creates a configuration set.

     

    Configuration sets enable you to publish email sending events. For information about using configuration sets, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/CreateConfigurationSet>`_    


    **Request Syntax** 
    ::

      response = client.create_configuration_set(
          ConfigurationSet={
              'Name': 'string'
          }
      )
    :type ConfigurationSet: dict
    :param ConfigurationSet: **[REQUIRED]** 

      A data structure that contains the name of the configuration set.

      

    
      - **Name** *(string) --* **[REQUIRED]** 

        The name of the configuration set. The name must meet the following requirements:

         

         
        * Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
         
        * Contain 64 characters or fewer. 
         

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

  .. py:method:: create_configuration_set_event_destination(**kwargs)

    

    Creates a configuration set event destination.

     

    .. note::

       

      When you create or update an event destination, you must provide one, and only one, destination. The destination can be Amazon CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS).

       

     

    An event destination is the AWS service to which Amazon SES publishes the email sending events associated with a configuration set. For information about using configuration sets, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/CreateConfigurationSetEventDestination>`_    


    **Request Syntax** 
    ::

      response = client.create_configuration_set_event_destination(
          ConfigurationSetName='string',
          EventDestination={
              'Name': 'string',
              'Enabled': True|False,
              'MatchingEventTypes': [
                  'send'|'reject'|'bounce'|'complaint'|'delivery'|'open'|'click'|'renderingFailure',
              ],
              'KinesisFirehoseDestination': {
                  'IAMRoleARN': 'string',
                  'DeliveryStreamARN': 'string'
              },
              'CloudWatchDestination': {
                  'DimensionConfigurations': [
                      {
                          'DimensionName': 'string',
                          'DimensionValueSource': 'messageTag'|'emailHeader'|'linkTag',
                          'DefaultDimensionValue': 'string'
                      },
                  ]
              },
              'SNSDestination': {
                  'TopicARN': 'string'
              }
          }
      )
    :type ConfigurationSetName: string
    :param ConfigurationSetName: **[REQUIRED]** 

      The name of the configuration set that the event destination should be associated with.

      

    
    :type EventDestination: dict
    :param EventDestination: **[REQUIRED]** 

      An object that describes the AWS service that email sending event information will be published to.

      

    
      - **Name** *(string) --* **[REQUIRED]** 

        The name of the event destination. The name must:

         

         
        * Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
         
        * Contain less than 64 characters. 
         

        

      
      - **Enabled** *(boolean) --* 

        Sets whether Amazon SES publishes events to this destination when you send an email with the associated configuration set. Set to ``true`` to enable publishing to this destination; set to ``false`` to prevent publishing to this destination. The default value is ``false`` .

        

      
      - **MatchingEventTypes** *(list) --* **[REQUIRED]** 

        The type of email sending events to publish to the event destination.

        

      
        - *(string) --* 

        
    
      - **KinesisFirehoseDestination** *(dict) --* 

        An object that contains the delivery stream ARN and the IAM role ARN associated with an Amazon Kinesis Firehose event destination.

        

      
        - **IAMRoleARN** *(string) --* **[REQUIRED]** 

          The ARN of the IAM role under which Amazon SES publishes email sending events to the Amazon Kinesis Firehose stream.

          

        
        - **DeliveryStreamARN** *(string) --* **[REQUIRED]** 

          The ARN of the Amazon Kinesis Firehose stream that email sending events should be published to.

          

        
      
      - **CloudWatchDestination** *(dict) --* 

        An object that contains the names, default values, and sources of the dimensions associated with an Amazon CloudWatch event destination.

        

      
        - **DimensionConfigurations** *(list) --* **[REQUIRED]** 

          A list of dimensions upon which to categorize your emails when you publish email sending events to Amazon CloudWatch.

          

        
          - *(dict) --* 

            Contains the dimension configuration to use when you publish email sending events to Amazon CloudWatch.

             

            For information about publishing email sending events to Amazon CloudWatch, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

            

          
            - **DimensionName** *(string) --* **[REQUIRED]** 

              The name of an Amazon CloudWatch dimension associated with an email sending metric. The name must:

               

               
              * Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
               
              * Contain less than 256 characters. 
               

              

            
            - **DimensionValueSource** *(string) --* **[REQUIRED]** 

              The place where Amazon SES finds the value of a dimension to publish to Amazon CloudWatch. If you want Amazon SES to use the message tags that you specify using an ``X-SES-MESSAGE-TAGS`` header or a parameter to the ``SendEmail`` /``SendRawEmail`` API, choose ``messageTag`` . If you want Amazon SES to use your own email headers, choose ``emailHeader`` .

              

            
            - **DefaultDimensionValue** *(string) --* **[REQUIRED]** 

              The default value of the dimension that is published to Amazon CloudWatch if you do not provide the value of the dimension when you send an email. The default value must:

               

               
              * Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
               
              * Contain less than 256 characters. 
               

              

            
          
      
      
      - **SNSDestination** *(dict) --* 

        An object that contains the topic ARN associated with an Amazon Simple Notification Service (Amazon SNS) event destination.

        

      
        - **TopicARN** *(string) --* **[REQUIRED]** 

          The ARN of the Amazon SNS topic that email sending events will be published to. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          

        
      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

  .. py:method:: create_configuration_set_tracking_options(**kwargs)

    

    Creates an association between a configuration set and a custom domain for open and click event tracking. 

     

    By default, images and links used for tracking open and click events are hosted on domains operated by Amazon SES. You can configure a subdomain of your own to handle these events. For information about using configuration sets, see `Configuring Custom Domains to Handle Open and Click Tracking <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/configure-custom-open-click-domains.html>`__ in the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/Welcome.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/CreateConfigurationSetTrackingOptions>`_    


    **Request Syntax** 
    ::

      response = client.create_configuration_set_tracking_options(
          ConfigurationSetName='string',
          TrackingOptions={
              'CustomRedirectDomain': 'string'
          }
      )
    :type ConfigurationSetName: string
    :param ConfigurationSetName: **[REQUIRED]** 

      The name of the configuration set that the tracking options should be associated with.

      

    
    :type TrackingOptions: dict
    :param TrackingOptions: **[REQUIRED]** 

      A domain that is used to redirect email recipients to an Amazon SES-operated domain. This domain captures open and click events generated by Amazon SES emails.

       

      For more information, see `Configuring Custom Domains to Handle Open and Click Tracking <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/configure-custom-open-click-domains.html>`__ in the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/Welcome.html>`__ .

      

    
      - **CustomRedirectDomain** *(string) --* 

        The custom subdomain that will be used to redirect email recipients to the Amazon SES event tracking domain.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

  .. py:method:: create_custom_verification_email_template(**kwargs)

    

    Creates a new custom verification email template.

     

    For more information about custom verification email templates, see `Using Custom Verification Email Templates <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-verification-emails.html>`__ in the *Amazon SES Developer Guide* .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/CreateCustomVerificationEmailTemplate>`_    


    **Request Syntax** 
    ::

      response = client.create_custom_verification_email_template(
          TemplateName='string',
          FromEmailAddress='string',
          TemplateSubject='string',
          TemplateContent='string',
          SuccessRedirectionURL='string',
          FailureRedirectionURL='string'
      )
    :type TemplateName: string
    :param TemplateName: **[REQUIRED]** 

      The name of the custom verification email template.

      

    
    :type FromEmailAddress: string
    :param FromEmailAddress: **[REQUIRED]** 

      The email address that the custom verification email is sent from.

      

    
    :type TemplateSubject: string
    :param TemplateSubject: **[REQUIRED]** 

      The subject line of the custom verification email.

      

    
    :type TemplateContent: string
    :param TemplateContent: **[REQUIRED]** 

      The content of the custom verification email. The total size of the email must be less than 10 MB. The message body may contain HTML, with some limitations. For more information, see `Custom Verification Email Frequently Asked Questions <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-verification-emails.html#custom-verification-emails-faq>`__ in the *Amazon SES Developer Guide* .

      

    
    :type SuccessRedirectionURL: string
    :param SuccessRedirectionURL: **[REQUIRED]** 

      The URL that the recipient of the verification email is sent to if his or her address is successfully verified.

      

    
    :type FailureRedirectionURL: string
    :param FailureRedirectionURL: **[REQUIRED]** 

      The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.

      

    
    
    :returns: None

  .. py:method:: create_receipt_filter(**kwargs)

    

    Creates a new IP address filter.

     

    For information about setting up IP address filters, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-ip-filters.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/CreateReceiptFilter>`_    


    **Request Syntax** 
    ::

      response = client.create_receipt_filter(
          Filter={
              'Name': 'string',
              'IpFilter': {
                  'Policy': 'Block'|'Allow',
                  'Cidr': 'string'
              }
          }
      )
    :type Filter: dict
    :param Filter: **[REQUIRED]** 

      A data structure that describes the IP address filter to create, which consists of a name, an IP address range, and whether to allow or block mail from it.

      

    
      - **Name** *(string) --* **[REQUIRED]** 

        The name of the IP address filter. The name must:

         

         
        * Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-). 
         
        * Start and end with a letter or number. 
         
        * Contain less than 64 characters. 
         

        

      
      - **IpFilter** *(dict) --* **[REQUIRED]** 

        A structure that provides the IP addresses to block or allow, and whether to block or allow incoming mail from them.

        

      
        - **Policy** *(string) --* **[REQUIRED]** 

          Indicates whether to block or allow incoming mail from the specified IP addresses.

          

        
        - **Cidr** *(string) --* **[REQUIRED]** 

          A single IP address or a range of IP addresses that you want to block or allow, specified in Classless Inter-Domain Routing (CIDR) notation. An example of a single email address is 10.0.0.1. An example of a range of IP addresses is 10.0.0.1/24. For more information about CIDR notation, see `RFC 2317 <https://tools.ietf.org/html/rfc2317>`__ .

          

        
      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

    **Examples** 

    The following example creates a new IP address filter:
    ::

      response = client.create_receipt_filter(
          Filter={
              'IpFilter': {
                  'Cidr': '1.2.3.4/24',
                  'Policy': 'Allow',
              },
              'Name': 'MyFilter',
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

    

  .. py:method:: create_receipt_rule(**kwargs)

    

    Creates a receipt rule.

     

    For information about setting up receipt rules, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/CreateReceiptRule>`_    


    **Request Syntax** 
    ::

      response = client.create_receipt_rule(
          RuleSetName='string',
          After='string',
          Rule={
              'Name': 'string',
              'Enabled': True|False,
              'TlsPolicy': 'Require'|'Optional',
              'Recipients': [
                  'string',
              ],
              'Actions': [
                  {
                      'S3Action': {
                          'TopicArn': 'string',
                          'BucketName': 'string',
                          'ObjectKeyPrefix': 'string',
                          'KmsKeyArn': 'string'
                      },
                      'BounceAction': {
                          'TopicArn': 'string',
                          'SmtpReplyCode': 'string',
                          'StatusCode': 'string',
                          'Message': 'string',
                          'Sender': 'string'
                      },
                      'WorkmailAction': {
                          'TopicArn': 'string',
                          'OrganizationArn': 'string'
                      },
                      'LambdaAction': {
                          'TopicArn': 'string',
                          'FunctionArn': 'string',
                          'InvocationType': 'Event'|'RequestResponse'
                      },
                      'StopAction': {
                          'Scope': 'RuleSet',
                          'TopicArn': 'string'
                      },
                      'AddHeaderAction': {
                          'HeaderName': 'string',
                          'HeaderValue': 'string'
                      },
                      'SNSAction': {
                          'TopicArn': 'string',
                          'Encoding': 'UTF-8'|'Base64'
                      }
                  },
              ],
              'ScanEnabled': True|False
          }
      )
    :type RuleSetName: string
    :param RuleSetName: **[REQUIRED]** 

      The name of the rule set that the receipt rule will be added to.

      

    
    :type After: string
    :param After: 

      The name of an existing rule after which the new rule will be placed. If this parameter is null, the new rule will be inserted at the beginning of the rule list.

      

    
    :type Rule: dict
    :param Rule: **[REQUIRED]** 

      A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy.

      

    
      - **Name** *(string) --* **[REQUIRED]** 

        The name of the receipt rule. The name must:

         

         
        * Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-). 
         
        * Start and end with a letter or number. 
         
        * Contain less than 64 characters. 
         

        

      
      - **Enabled** *(boolean) --* 

        If ``true`` , the receipt rule is active. The default value is ``false`` .

        

      
      - **TlsPolicy** *(string) --* 

        Specifies whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). If this parameter is set to ``Require`` , Amazon SES will bounce emails that are not received over TLS. The default is ``Optional`` .

        

      
      - **Recipients** *(list) --* 

        The recipient domains and email addresses that the receipt rule applies to. If this field is not specified, this rule will match all recipients under all verified domains.

        

      
        - *(string) --* 

        
    
      - **Actions** *(list) --* 

        An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule.

        

      
        - *(dict) --* 

          An action that Amazon SES can take when it receives an email on behalf of one or more email addresses or domains that you own. An instance of this data type can represent only one action.

           

          For information about setting up receipt rules, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html>`__ .

          

        
          - **S3Action** *(dict) --* 

            Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and, optionally, publishes a notification to Amazon SNS.

            

          
            - **TopicArn** *(string) --* 

              The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3 bucket. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

              

            
            - **BucketName** *(string) --* **[REQUIRED]** 

              The name of the Amazon S3 bucket that incoming email will be saved to.

              

            
            - **ObjectKeyPrefix** *(string) --* 

              The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory name that enables you to store similar data under the same directory in a bucket.

              

            
            - **KmsKeyArn** *(string) --* 

              The customer master key that Amazon SES should use to encrypt your emails before saving them to the Amazon S3 bucket. You can use the default master key or a custom master key you created in AWS KMS as follows:

               

               
              * To use the default master key, provide an ARN in the form of ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if your AWS account ID is 123456789012 and you want to use the default master key in the US West (Oregon) region, the ARN of the default master key would be ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default master key, you don't need to perform any extra steps to give Amazon SES permission to use the key. 
               
              * To use a custom master key you created in AWS KMS, provide the ARN of the master key and ensure that you add a statement to your key's policy to give Amazon SES permission to use it. For more information about giving permissions, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html>`__ . 
               

               

              For more information about key policies, see the `AWS KMS Developer Guide <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`__ . If you do not specify a master key, Amazon SES will not encrypt your emails.

               

              .. warning::

                 

                Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3 server-side encryption. This means that you must use the Amazon S3 encryption client to decrypt the email after retrieving it from Amazon S3, as the service has no access to use your AWS KMS keys for decryption. This encryption client is currently available with the `AWS Java SDK <http://aws.amazon.com/sdk-for-java/>`__ and `AWS Ruby SDK <http://aws.amazon.com/sdk-for-ruby/>`__ only. For more information about client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer Guide <http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__ .

                 

              

            
          
          - **BounceAction** *(dict) --* 

            Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).

            

          
            - **TopicArn** *(string) --* 

              The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action is taken. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

              

            
            - **SmtpReplyCode** *(string) --* **[REQUIRED]** 

              The SMTP reply code, as defined by `RFC 5321 <https://tools.ietf.org/html/rfc5321>`__ .

              

            
            - **StatusCode** *(string) --* 

              The SMTP enhanced status code, as defined by `RFC 3463 <https://tools.ietf.org/html/rfc3463>`__ .

              

            
            - **Message** *(string) --* **[REQUIRED]** 

              Human-readable text to include in the bounce message.

              

            
            - **Sender** *(string) --* **[REQUIRED]** 

              The email address of the sender of the bounced email. This is the address from which the bounce message will be sent.

              

            
          
          - **WorkmailAction** *(dict) --* 

            Calls Amazon WorkMail and, optionally, publishes a notification to Amazon SNS.

            

          
            - **TopicArn** *(string) --* 

              The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action is called. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

              

            
            - **OrganizationArn** *(string) --* **[REQUIRED]** 

              The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail organization ARN is ``arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7`` . For information about Amazon WorkMail organizations, see the `Amazon WorkMail Administrator Guide <http://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`__ .

              

            
          
          - **LambdaAction** *(dict) --* 

            Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.

            

          
            - **TopicArn** *(string) --* 

              The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action is taken. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

              

            
            - **FunctionArn** *(string) --* **[REQUIRED]** 

              The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS Lambda function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction`` . For more information about AWS Lambda, see the `AWS Lambda Developer Guide <http://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`__ .

              

            
            - **InvocationType** *(string) --* 

              The invocation type of the AWS Lambda function. An invocation type of ``RequestResponse`` means that the execution of the function will immediately result in a response, and a value of ``Event`` means that the function will be invoked asynchronously. The default value is ``Event`` . For information about AWS Lambda invocation types, see the `AWS Lambda Developer Guide <http://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`__ .

               

              .. warning::

                 

                There is a 30-second timeout on ``RequestResponse`` invocations. You should use ``Event`` invocation in most cases. Use ``RequestResponse`` only when you want to make a mail flow decision, such as whether to stop the receipt rule or the receipt rule set.

                 

              

            
          
          - **StopAction** *(dict) --* 

            Terminates the evaluation of the receipt rule set and optionally publishes a notification to Amazon SNS.

            

          
            - **Scope** *(string) --* **[REQUIRED]** 

              The name of the RuleSet that is being stopped.

              

            
            - **TopicArn** *(string) --* 

              The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is taken. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

              

            
          
          - **AddHeaderAction** *(dict) --* 

            Adds a header to the received email.

            

          
            - **HeaderName** *(string) --* **[REQUIRED]** 

              The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

              

            
            - **HeaderValue** *(string) --* **[REQUIRED]** 

              Must be less than 2048 characters, and must not contain newline characters ("\r" or "\n").

              

            
          
          - **SNSAction** *(dict) --* 

            Publishes the email content within a notification to Amazon SNS.

            

          
            - **TopicArn** *(string) --* **[REQUIRED]** 

              The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

              

            
            - **Encoding** *(string) --* 

              The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier to use, but may not preserve all special characters when a message was encoded with a different encoding format. Base64 preserves all special characters. The default value is UTF-8.

              

            
          
        
    
      - **ScanEnabled** *(boolean) --* 

        If ``true`` , then messages that this receipt rule applies to are scanned for spam and viruses. The default value is ``false`` .

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

    **Examples** 

    The following example creates a new receipt rule:
    ::

      response = client.create_receipt_rule(
          After='',
          Rule={
              'Actions': [
                  {
                      'S3Action': {
                          'BucketName': 'MyBucket',
                          'ObjectKeyPrefix': 'email',
                      },
                  },
              ],
              'Enabled': True,
              'Name': 'MyRule',
              'ScanEnabled': True,
              'TlsPolicy': 'Optional',
          },
          RuleSetName='MyRuleSet',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_receipt_rule_set(**kwargs)

    

    Creates an empty receipt rule set.

     

    For information about setting up receipt rule sets, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rule-set.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/CreateReceiptRuleSet>`_    


    **Request Syntax** 
    ::

      response = client.create_receipt_rule_set(
          RuleSetName='string'
      )
    :type RuleSetName: string
    :param RuleSetName: **[REQUIRED]** 

      The name of the rule set to create. The name must:

       

       
      * Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-). 
       
      * Start and end with a letter or number. 
       
      * Contain less than 64 characters. 
       

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

    **Examples** 

    The following example creates an empty receipt rule set:
    ::

      response = client.create_receipt_rule_set(
          RuleSetName='MyRuleSet',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_template(**kwargs)

    

    Creates an email template. Email templates enable you to send personalized email to one or more destinations in a single API operation. For more information, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-email-api.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/CreateTemplate>`_    


    **Request Syntax** 
    ::

      response = client.create_template(
          Template={
              'TemplateName': 'string',
              'SubjectPart': 'string',
              'TextPart': 'string',
              'HtmlPart': 'string'
          }
      )
    :type Template: dict
    :param Template: **[REQUIRED]** 

      The content of the email, composed of a subject line, an HTML part, and a text-only part.

      

    
      - **TemplateName** *(string) --* **[REQUIRED]** 

        The name of the template. You will refer to this name when you send email using the ``SendTemplatedEmail`` or ``SendBulkTemplatedEmail`` operations.

        

      
      - **SubjectPart** *(string) --* 

        The subject line of the email.

        

      
      - **TextPart** *(string) --* 

        The email body that will be visible to recipients whose email clients do not display HTML.

        

      
      - **HtmlPart** *(string) --* 

        The HTML body of the email.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_configuration_set(**kwargs)

    

    Deletes a configuration set. Configuration sets enable you to publish email sending events. For information about using configuration sets, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/DeleteConfigurationSet>`_    


    **Request Syntax** 
    ::

      response = client.delete_configuration_set(
          ConfigurationSetName='string'
      )
    :type ConfigurationSetName: string
    :param ConfigurationSetName: **[REQUIRED]** 

      The name of the configuration set to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

  .. py:method:: delete_configuration_set_event_destination(**kwargs)

    

    Deletes a configuration set event destination. Configuration set event destinations are associated with configuration sets, which enable you to publish email sending events. For information about using configuration sets, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/DeleteConfigurationSetEventDestination>`_    


    **Request Syntax** 
    ::

      response = client.delete_configuration_set_event_destination(
          ConfigurationSetName='string',
          EventDestinationName='string'
      )
    :type ConfigurationSetName: string
    :param ConfigurationSetName: **[REQUIRED]** 

      The name of the configuration set from which to delete the event destination.

      

    
    :type EventDestinationName: string
    :param EventDestinationName: **[REQUIRED]** 

      The name of the event destination to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

  .. py:method:: delete_configuration_set_tracking_options(**kwargs)

    

    Deletes an association between a configuration set and a custom domain for open and click event tracking.

     

    By default, images and links used for tracking open and click events are hosted on domains operated by Amazon SES. You can configure a subdomain of your own to handle these events. For information about using configuration sets, see `Configuring Custom Domains to Handle Open and Click Tracking <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/configure-custom-open-click-domains.html>`__ in the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/Welcome.html>`__ .

     

    .. note::

       

      Deleting this kind of association will result in emails sent using the specified configuration set to capture open and click events using the standard, Amazon SES-operated domains.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/DeleteConfigurationSetTrackingOptions>`_    


    **Request Syntax** 
    ::

      response = client.delete_configuration_set_tracking_options(
          ConfigurationSetName='string'
      )
    :type ConfigurationSetName: string
    :param ConfigurationSetName: **[REQUIRED]** 

      The name of the configuration set from which you want to delete the tracking options.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

  .. py:method:: delete_custom_verification_email_template(**kwargs)

    

    Deletes an existing custom verification email template. 

     

    For more information about custom verification email templates, see `Using Custom Verification Email Templates <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-verification-emails.html>`__ in the *Amazon SES Developer Guide* .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/DeleteCustomVerificationEmailTemplate>`_    


    **Request Syntax** 
    ::

      response = client.delete_custom_verification_email_template(
          TemplateName='string'
      )
    :type TemplateName: string
    :param TemplateName: **[REQUIRED]** 

      The name of the custom verification email template that you want to delete.

      

    
    
    :returns: None

  .. py:method:: delete_identity(**kwargs)

    

    Deletes the specified identity (an email address or a domain) from the list of verified identities.

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/DeleteIdentity>`_    


    **Request Syntax** 
    ::

      response = client.delete_identity(
          Identity='string'
      )
    :type Identity: string
    :param Identity: **[REQUIRED]** 

      The identity to be removed from the list of identities for the AWS Account.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

    **Examples** 

    The following example deletes an identity from the list of identities that have been submitted for verification with Amazon SES:
    ::

      response = client.delete_identity(
          Identity='user@example.com',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_identity_policy(**kwargs)

    

    Deletes the specified sending authorization policy for the given identity (an email address or a domain). This API returns successfully even if a policy with the specified name does not exist.

     

    .. note::

       

      This API is for the identity owner only. If you have not verified the identity, this API will return an error.

       

     

    Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/DeleteIdentityPolicy>`_    


    **Request Syntax** 
    ::

      response = client.delete_identity_policy(
          Identity='string',
          PolicyName='string'
      )
    :type Identity: string
    :param Identity: **[REQUIRED]** 

      The identity that is associated with the policy that you want to delete. You can specify the identity by using its name or by using its Amazon Resource Name (ARN). Examples: ``user@example.com`` , ``example.com`` , ``arn:aws:ses:us-east-1:123456789012:identity/example.com`` .

       

      To successfully call this API, you must own the identity.

      

    
    :type PolicyName: string
    :param PolicyName: **[REQUIRED]** 

      The name of the policy to be deleted.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

    **Examples** 

    The following example deletes a sending authorization policy for an identity:
    ::

      response = client.delete_identity_policy(
          Identity='user@example.com',
          PolicyName='MyPolicy',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_receipt_filter(**kwargs)

    

    Deletes the specified IP address filter.

     

    For information about managing IP address filters, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-ip-filters.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/DeleteReceiptFilter>`_    


    **Request Syntax** 
    ::

      response = client.delete_receipt_filter(
          FilterName='string'
      )
    :type FilterName: string
    :param FilterName: **[REQUIRED]** 

      The name of the IP address filter to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

    **Examples** 

    The following example deletes an IP address filter:
    ::

      response = client.delete_receipt_filter(
          FilterName='MyFilter',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_receipt_rule(**kwargs)

    

    Deletes the specified receipt rule.

     

    For information about managing receipt rules, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rules.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/DeleteReceiptRule>`_    


    **Request Syntax** 
    ::

      response = client.delete_receipt_rule(
          RuleSetName='string',
          RuleName='string'
      )
    :type RuleSetName: string
    :param RuleSetName: **[REQUIRED]** 

      The name of the receipt rule set that contains the receipt rule to delete.

      

    
    :type RuleName: string
    :param RuleName: **[REQUIRED]** 

      The name of the receipt rule to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

    **Examples** 

    The following example deletes a receipt rule:
    ::

      response = client.delete_receipt_rule(
          RuleName='MyRule',
          RuleSetName='MyRuleSet',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_receipt_rule_set(**kwargs)

    

    Deletes the specified receipt rule set and all of the receipt rules it contains.

     

    .. note::

       

      The currently active rule set cannot be deleted.

       

     

    For information about managing receipt rule sets, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rule-sets.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/DeleteReceiptRuleSet>`_    


    **Request Syntax** 
    ::

      response = client.delete_receipt_rule_set(
          RuleSetName='string'
      )
    :type RuleSetName: string
    :param RuleSetName: **[REQUIRED]** 

      The name of the receipt rule set to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

    **Examples** 

    The following example deletes a receipt rule set:
    ::

      response = client.delete_receipt_rule_set(
          RuleSetName='MyRuleSet',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_template(**kwargs)

    

    Deletes an email template.

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/DeleteTemplate>`_    


    **Request Syntax** 
    ::

      response = client.delete_template(
          TemplateName='string'
      )
    :type TemplateName: string
    :param TemplateName: **[REQUIRED]** 

      The name of the template to be deleted.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_verified_email_address(**kwargs)

    

    Deprecated. Use the ``DeleteIdentity`` operation to delete email addresses and domains.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/DeleteVerifiedEmailAddress>`_    


    **Request Syntax** 
    ::

      response = client.delete_verified_email_address(
          EmailAddress='string'
      )
    :type EmailAddress: string
    :param EmailAddress: **[REQUIRED]** 

      An email address to be removed from the list of verified addresses.

      

    
    
    :returns: None

    **Examples** 

    The following example deletes an email address from the list of identities that have been submitted for verification with Amazon SES:
    ::

      response = client.delete_verified_email_address(
          EmailAddress='user@example.com',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_active_receipt_rule_set()

    

    Returns the metadata and receipt rules for the receipt rule set that is currently active.

     

    For information about setting up receipt rule sets, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rule-set.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/DescribeActiveReceiptRuleSet>`_    


    **Request Syntax** 
    ::

      response = client.describe_active_receipt_rule_set()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Metadata': {
                'Name': 'string',
                'CreatedTimestamp': datetime(2015, 1, 1)
            },
            'Rules': [
                {
                    'Name': 'string',
                    'Enabled': True|False,
                    'TlsPolicy': 'Require'|'Optional',
                    'Recipients': [
                        'string',
                    ],
                    'Actions': [
                        {
                            'S3Action': {
                                'TopicArn': 'string',
                                'BucketName': 'string',
                                'ObjectKeyPrefix': 'string',
                                'KmsKeyArn': 'string'
                            },
                            'BounceAction': {
                                'TopicArn': 'string',
                                'SmtpReplyCode': 'string',
                                'StatusCode': 'string',
                                'Message': 'string',
                                'Sender': 'string'
                            },
                            'WorkmailAction': {
                                'TopicArn': 'string',
                                'OrganizationArn': 'string'
                            },
                            'LambdaAction': {
                                'TopicArn': 'string',
                                'FunctionArn': 'string',
                                'InvocationType': 'Event'|'RequestResponse'
                            },
                            'StopAction': {
                                'Scope': 'RuleSet',
                                'TopicArn': 'string'
                            },
                            'AddHeaderAction': {
                                'HeaderName': 'string',
                                'HeaderValue': 'string'
                            },
                            'SNSAction': {
                                'TopicArn': 'string',
                                'Encoding': 'UTF-8'|'Base64'
                            }
                        },
                    ],
                    'ScanEnabled': True|False
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the metadata and receipt rules for the receipt rule set that is currently active.

        
        

        - **Metadata** *(dict) --* 

          The metadata for the currently active receipt rule set. The metadata consists of the rule set name and a timestamp of when the rule set was created.

          
          

          - **Name** *(string) --* 

            The name of the receipt rule set. The name must:

             

             
            * Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-). 
             
            * Start and end with a letter or number. 
             
            * Contain less than 64 characters. 
             

            
          

          - **CreatedTimestamp** *(datetime) --* 

            The date and time the receipt rule set was created.

            
      
        

        - **Rules** *(list) --* 

          The receipt rules that belong to the active rule set.

          
          

          - *(dict) --* 

            Receipt rules enable you to specify which actions Amazon SES should take when it receives mail on behalf of one or more email addresses or domains that you own.

             

            Each receipt rule defines a set of email addresses or domains that it applies to. If the email addresses or domains match at least one recipient address of the message, Amazon SES executes all of the receipt rule's actions on the message.

             

            For information about setting up receipt rules, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html>`__ .

            
            

            - **Name** *(string) --* 

              The name of the receipt rule. The name must:

               

               
              * Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-). 
               
              * Start and end with a letter or number. 
               
              * Contain less than 64 characters. 
               

              
            

            - **Enabled** *(boolean) --* 

              If ``true`` , the receipt rule is active. The default value is ``false`` .

              
            

            - **TlsPolicy** *(string) --* 

              Specifies whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). If this parameter is set to ``Require`` , Amazon SES will bounce emails that are not received over TLS. The default is ``Optional`` .

              
            

            - **Recipients** *(list) --* 

              The recipient domains and email addresses that the receipt rule applies to. If this field is not specified, this rule will match all recipients under all verified domains.

              
              

              - *(string) --* 
          
            

            - **Actions** *(list) --* 

              An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule.

              
              

              - *(dict) --* 

                An action that Amazon SES can take when it receives an email on behalf of one or more email addresses or domains that you own. An instance of this data type can represent only one action.

                 

                For information about setting up receipt rules, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html>`__ .

                
                

                - **S3Action** *(dict) --* 

                  Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and, optionally, publishes a notification to Amazon SNS.

                  
                  

                  - **TopicArn** *(string) --* 

                    The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3 bucket. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

                    
                  

                  - **BucketName** *(string) --* 

                    The name of the Amazon S3 bucket that incoming email will be saved to.

                    
                  

                  - **ObjectKeyPrefix** *(string) --* 

                    The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory name that enables you to store similar data under the same directory in a bucket.

                    
                  

                  - **KmsKeyArn** *(string) --* 

                    The customer master key that Amazon SES should use to encrypt your emails before saving them to the Amazon S3 bucket. You can use the default master key or a custom master key you created in AWS KMS as follows:

                     

                     
                    * To use the default master key, provide an ARN in the form of ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if your AWS account ID is 123456789012 and you want to use the default master key in the US West (Oregon) region, the ARN of the default master key would be ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default master key, you don't need to perform any extra steps to give Amazon SES permission to use the key. 
                     
                    * To use a custom master key you created in AWS KMS, provide the ARN of the master key and ensure that you add a statement to your key's policy to give Amazon SES permission to use it. For more information about giving permissions, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html>`__ . 
                     

                     

                    For more information about key policies, see the `AWS KMS Developer Guide <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`__ . If you do not specify a master key, Amazon SES will not encrypt your emails.

                     

                    .. warning::

                       

                      Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3 server-side encryption. This means that you must use the Amazon S3 encryption client to decrypt the email after retrieving it from Amazon S3, as the service has no access to use your AWS KMS keys for decryption. This encryption client is currently available with the `AWS Java SDK <http://aws.amazon.com/sdk-for-java/>`__ and `AWS Ruby SDK <http://aws.amazon.com/sdk-for-ruby/>`__ only. For more information about client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer Guide <http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__ .

                       

                    
              
                

                - **BounceAction** *(dict) --* 

                  Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).

                  
                  

                  - **TopicArn** *(string) --* 

                    The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action is taken. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

                    
                  

                  - **SmtpReplyCode** *(string) --* 

                    The SMTP reply code, as defined by `RFC 5321 <https://tools.ietf.org/html/rfc5321>`__ .

                    
                  

                  - **StatusCode** *(string) --* 

                    The SMTP enhanced status code, as defined by `RFC 3463 <https://tools.ietf.org/html/rfc3463>`__ .

                    
                  

                  - **Message** *(string) --* 

                    Human-readable text to include in the bounce message.

                    
                  

                  - **Sender** *(string) --* 

                    The email address of the sender of the bounced email. This is the address from which the bounce message will be sent.

                    
              
                

                - **WorkmailAction** *(dict) --* 

                  Calls Amazon WorkMail and, optionally, publishes a notification to Amazon SNS.

                  
                  

                  - **TopicArn** *(string) --* 

                    The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action is called. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

                    
                  

                  - **OrganizationArn** *(string) --* 

                    The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail organization ARN is ``arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7`` . For information about Amazon WorkMail organizations, see the `Amazon WorkMail Administrator Guide <http://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`__ .

                    
              
                

                - **LambdaAction** *(dict) --* 

                  Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.

                  
                  

                  - **TopicArn** *(string) --* 

                    The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action is taken. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

                    
                  

                  - **FunctionArn** *(string) --* 

                    The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS Lambda function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction`` . For more information about AWS Lambda, see the `AWS Lambda Developer Guide <http://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`__ .

                    
                  

                  - **InvocationType** *(string) --* 

                    The invocation type of the AWS Lambda function. An invocation type of ``RequestResponse`` means that the execution of the function will immediately result in a response, and a value of ``Event`` means that the function will be invoked asynchronously. The default value is ``Event`` . For information about AWS Lambda invocation types, see the `AWS Lambda Developer Guide <http://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`__ .

                     

                    .. warning::

                       

                      There is a 30-second timeout on ``RequestResponse`` invocations. You should use ``Event`` invocation in most cases. Use ``RequestResponse`` only when you want to make a mail flow decision, such as whether to stop the receipt rule or the receipt rule set.

                       

                    
              
                

                - **StopAction** *(dict) --* 

                  Terminates the evaluation of the receipt rule set and optionally publishes a notification to Amazon SNS.

                  
                  

                  - **Scope** *(string) --* 

                    The name of the RuleSet that is being stopped.

                    
                  

                  - **TopicArn** *(string) --* 

                    The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is taken. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

                    
              
                

                - **AddHeaderAction** *(dict) --* 

                  Adds a header to the received email.

                  
                  

                  - **HeaderName** *(string) --* 

                    The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

                    
                  

                  - **HeaderValue** *(string) --* 

                    Must be less than 2048 characters, and must not contain newline characters ("\r" or "\n").

                    
              
                

                - **SNSAction** *(dict) --* 

                  Publishes the email content within a notification to Amazon SNS.

                  
                  

                  - **TopicArn** *(string) --* 

                    The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

                    
                  

                  - **Encoding** *(string) --* 

                    The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier to use, but may not preserve all special characters when a message was encoded with a different encoding format. Base64 preserves all special characters. The default value is UTF-8.

                    
              
            
          
            

            - **ScanEnabled** *(boolean) --* 

              If ``true`` , then messages that this receipt rule applies to are scanned for spam and viruses. The default value is ``false`` .

              
        
      
    

    **Examples** 

    The following example returns the metadata and receipt rules for the receipt rule set that is currently active:
    ::

      response = client.describe_active_receipt_rule_set(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Metadata': {
              'CreatedTimestamp': datetime(2016, 7, 15, 16, 25, 59, 4, 197, 0),
              'Name': 'default-rule-set',
          },
          'Rules': [
              {
                  'Actions': [
                      {
                          'S3Action': {
                              'BucketName': 'MyBucket',
                              'ObjectKeyPrefix': 'email',
                          },
                      },
                  ],
                  'Enabled': True,
                  'Name': 'MyRule',
                  'ScanEnabled': True,
                  'TlsPolicy': 'Optional',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_configuration_set(**kwargs)

    

    Returns the details of the specified configuration set. For information about using configuration sets, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/DescribeConfigurationSet>`_    


    **Request Syntax** 
    ::

      response = client.describe_configuration_set(
          ConfigurationSetName='string',
          ConfigurationSetAttributeNames=[
              'eventDestinations'|'trackingOptions'|'reputationOptions',
          ]
      )
    :type ConfigurationSetName: string
    :param ConfigurationSetName: **[REQUIRED]** 

      The name of the configuration set to describe.

      

    
    :type ConfigurationSetAttributeNames: list
    :param ConfigurationSetAttributeNames: 

      A list of configuration set attributes to return.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ConfigurationSet': {
                'Name': 'string'
            },
            'EventDestinations': [
                {
                    'Name': 'string',
                    'Enabled': True|False,
                    'MatchingEventTypes': [
                        'send'|'reject'|'bounce'|'complaint'|'delivery'|'open'|'click'|'renderingFailure',
                    ],
                    'KinesisFirehoseDestination': {
                        'IAMRoleARN': 'string',
                        'DeliveryStreamARN': 'string'
                    },
                    'CloudWatchDestination': {
                        'DimensionConfigurations': [
                            {
                                'DimensionName': 'string',
                                'DimensionValueSource': 'messageTag'|'emailHeader'|'linkTag',
                                'DefaultDimensionValue': 'string'
                            },
                        ]
                    },
                    'SNSDestination': {
                        'TopicARN': 'string'
                    }
                },
            ],
            'TrackingOptions': {
                'CustomRedirectDomain': 'string'
            },
            'ReputationOptions': {
                'SendingEnabled': True|False,
                'ReputationMetricsEnabled': True|False,
                'LastFreshStart': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the details of a configuration set. Configuration sets enable you to publish email sending events. For information about using configuration sets, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

        
        

        - **ConfigurationSet** *(dict) --* 

          The configuration set object associated with the specified configuration set.

          
          

          - **Name** *(string) --* 

            The name of the configuration set. The name must meet the following requirements:

             

             
            * Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
             
            * Contain 64 characters or fewer. 
             

            
      
        

        - **EventDestinations** *(list) --* 

          A list of event destinations associated with the configuration set. 

          
          

          - *(dict) --* 

            Contains information about the event destination that the specified email sending events will be published to.

             

            .. note::

               

              When you create or update an event destination, you must provide one, and only one, destination. The destination can be Amazon CloudWatch, Amazon Kinesis Firehose or Amazon Simple Notification Service (Amazon SNS).

               

             

            Event destinations are associated with configuration sets, which enable you to publish email sending events to Amazon CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS). For information about using configuration sets, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

            
            

            - **Name** *(string) --* 

              The name of the event destination. The name must:

               

               
              * Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
               
              * Contain less than 64 characters. 
               

              
            

            - **Enabled** *(boolean) --* 

              Sets whether Amazon SES publishes events to this destination when you send an email with the associated configuration set. Set to ``true`` to enable publishing to this destination; set to ``false`` to prevent publishing to this destination. The default value is ``false`` .

              
            

            - **MatchingEventTypes** *(list) --* 

              The type of email sending events to publish to the event destination.

              
              

              - *(string) --* 
          
            

            - **KinesisFirehoseDestination** *(dict) --* 

              An object that contains the delivery stream ARN and the IAM role ARN associated with an Amazon Kinesis Firehose event destination.

              
              

              - **IAMRoleARN** *(string) --* 

                The ARN of the IAM role under which Amazon SES publishes email sending events to the Amazon Kinesis Firehose stream.

                
              

              - **DeliveryStreamARN** *(string) --* 

                The ARN of the Amazon Kinesis Firehose stream that email sending events should be published to.

                
          
            

            - **CloudWatchDestination** *(dict) --* 

              An object that contains the names, default values, and sources of the dimensions associated with an Amazon CloudWatch event destination.

              
              

              - **DimensionConfigurations** *(list) --* 

                A list of dimensions upon which to categorize your emails when you publish email sending events to Amazon CloudWatch.

                
                

                - *(dict) --* 

                  Contains the dimension configuration to use when you publish email sending events to Amazon CloudWatch.

                   

                  For information about publishing email sending events to Amazon CloudWatch, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

                  
                  

                  - **DimensionName** *(string) --* 

                    The name of an Amazon CloudWatch dimension associated with an email sending metric. The name must:

                     

                     
                    * Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
                     
                    * Contain less than 256 characters. 
                     

                    
                  

                  - **DimensionValueSource** *(string) --* 

                    The place where Amazon SES finds the value of a dimension to publish to Amazon CloudWatch. If you want Amazon SES to use the message tags that you specify using an ``X-SES-MESSAGE-TAGS`` header or a parameter to the ``SendEmail`` /``SendRawEmail`` API, choose ``messageTag`` . If you want Amazon SES to use your own email headers, choose ``emailHeader`` .

                    
                  

                  - **DefaultDimensionValue** *(string) --* 

                    The default value of the dimension that is published to Amazon CloudWatch if you do not provide the value of the dimension when you send an email. The default value must:

                     

                     
                    * Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
                     
                    * Contain less than 256 characters. 
                     

                    
              
            
          
            

            - **SNSDestination** *(dict) --* 

              An object that contains the topic ARN associated with an Amazon Simple Notification Service (Amazon SNS) event destination.

              
              

              - **TopicARN** *(string) --* 

                The ARN of the Amazon SNS topic that email sending events will be published to. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

                
          
        
      
        

        - **TrackingOptions** *(dict) --* 

          The name of the custom open and click tracking domain associated with the configuration set.

          
          

          - **CustomRedirectDomain** *(string) --* 

            The custom subdomain that will be used to redirect email recipients to the Amazon SES event tracking domain.

            
      
        

        - **ReputationOptions** *(dict) --* 

          An object that represents the reputation settings for the configuration set. 

          
          

          - **SendingEnabled** *(boolean) --* 

            Describes whether email sending is enabled or disabled for the configuration set. If the value is ``true`` , then Amazon SES will send emails that use the configuration set. If the value is ``false`` , Amazon SES will not send emails that use the configuration set. The default value is ``true`` . You can change this setting using  UpdateConfigurationSetSendingEnabled .

            
          

          - **ReputationMetricsEnabled** *(boolean) --* 

            Describes whether or not Amazon SES publishes reputation metrics for the configuration set, such as bounce and complaint rates, to Amazon CloudWatch.

             

            If the value is ``true`` , reputation metrics are published. If the value is ``false`` , reputation metrics are not published. The default value is ``false`` .

            
          

          - **LastFreshStart** *(datetime) --* 

            The date and time at which the reputation metrics for the configuration set were last reset. Resetting these metrics is known as a *fresh start* .

             

            When you disable email sending for a configuration set using  UpdateConfigurationSetSendingEnabled and later re-enable it, the reputation metrics for the configuration set (but not for the entire Amazon SES account) are reset.

             

            If email sending for the configuration set has never been disabled and later re-enabled, the value of this attribute is ``null`` .

            
      
    

  .. py:method:: describe_receipt_rule(**kwargs)

    

    Returns the details of the specified receipt rule.

     

    For information about setting up receipt rules, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/DescribeReceiptRule>`_    


    **Request Syntax** 
    ::

      response = client.describe_receipt_rule(
          RuleSetName='string',
          RuleName='string'
      )
    :type RuleSetName: string
    :param RuleSetName: **[REQUIRED]** 

      The name of the receipt rule set that the receipt rule belongs to.

      

    
    :type RuleName: string
    :param RuleName: **[REQUIRED]** 

      The name of the receipt rule.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Rule': {
                'Name': 'string',
                'Enabled': True|False,
                'TlsPolicy': 'Require'|'Optional',
                'Recipients': [
                    'string',
                ],
                'Actions': [
                    {
                        'S3Action': {
                            'TopicArn': 'string',
                            'BucketName': 'string',
                            'ObjectKeyPrefix': 'string',
                            'KmsKeyArn': 'string'
                        },
                        'BounceAction': {
                            'TopicArn': 'string',
                            'SmtpReplyCode': 'string',
                            'StatusCode': 'string',
                            'Message': 'string',
                            'Sender': 'string'
                        },
                        'WorkmailAction': {
                            'TopicArn': 'string',
                            'OrganizationArn': 'string'
                        },
                        'LambdaAction': {
                            'TopicArn': 'string',
                            'FunctionArn': 'string',
                            'InvocationType': 'Event'|'RequestResponse'
                        },
                        'StopAction': {
                            'Scope': 'RuleSet',
                            'TopicArn': 'string'
                        },
                        'AddHeaderAction': {
                            'HeaderName': 'string',
                            'HeaderValue': 'string'
                        },
                        'SNSAction': {
                            'TopicArn': 'string',
                            'Encoding': 'UTF-8'|'Base64'
                        }
                    },
                ],
                'ScanEnabled': True|False
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the details of a receipt rule.

        
        

        - **Rule** *(dict) --* 

          A data structure that contains the specified receipt rule's name, actions, recipients, domains, enabled status, scan status, and Transport Layer Security (TLS) policy.

          
          

          - **Name** *(string) --* 

            The name of the receipt rule. The name must:

             

             
            * Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-). 
             
            * Start and end with a letter or number. 
             
            * Contain less than 64 characters. 
             

            
          

          - **Enabled** *(boolean) --* 

            If ``true`` , the receipt rule is active. The default value is ``false`` .

            
          

          - **TlsPolicy** *(string) --* 

            Specifies whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). If this parameter is set to ``Require`` , Amazon SES will bounce emails that are not received over TLS. The default is ``Optional`` .

            
          

          - **Recipients** *(list) --* 

            The recipient domains and email addresses that the receipt rule applies to. If this field is not specified, this rule will match all recipients under all verified domains.

            
            

            - *(string) --* 
        
          

          - **Actions** *(list) --* 

            An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule.

            
            

            - *(dict) --* 

              An action that Amazon SES can take when it receives an email on behalf of one or more email addresses or domains that you own. An instance of this data type can represent only one action.

               

              For information about setting up receipt rules, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html>`__ .

              
              

              - **S3Action** *(dict) --* 

                Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and, optionally, publishes a notification to Amazon SNS.

                
                

                - **TopicArn** *(string) --* 

                  The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3 bucket. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

                  
                

                - **BucketName** *(string) --* 

                  The name of the Amazon S3 bucket that incoming email will be saved to.

                  
                

                - **ObjectKeyPrefix** *(string) --* 

                  The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory name that enables you to store similar data under the same directory in a bucket.

                  
                

                - **KmsKeyArn** *(string) --* 

                  The customer master key that Amazon SES should use to encrypt your emails before saving them to the Amazon S3 bucket. You can use the default master key or a custom master key you created in AWS KMS as follows:

                   

                   
                  * To use the default master key, provide an ARN in the form of ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if your AWS account ID is 123456789012 and you want to use the default master key in the US West (Oregon) region, the ARN of the default master key would be ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default master key, you don't need to perform any extra steps to give Amazon SES permission to use the key. 
                   
                  * To use a custom master key you created in AWS KMS, provide the ARN of the master key and ensure that you add a statement to your key's policy to give Amazon SES permission to use it. For more information about giving permissions, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html>`__ . 
                   

                   

                  For more information about key policies, see the `AWS KMS Developer Guide <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`__ . If you do not specify a master key, Amazon SES will not encrypt your emails.

                   

                  .. warning::

                     

                    Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3 server-side encryption. This means that you must use the Amazon S3 encryption client to decrypt the email after retrieving it from Amazon S3, as the service has no access to use your AWS KMS keys for decryption. This encryption client is currently available with the `AWS Java SDK <http://aws.amazon.com/sdk-for-java/>`__ and `AWS Ruby SDK <http://aws.amazon.com/sdk-for-ruby/>`__ only. For more information about client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer Guide <http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__ .

                     

                  
            
              

              - **BounceAction** *(dict) --* 

                Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).

                
                

                - **TopicArn** *(string) --* 

                  The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action is taken. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

                  
                

                - **SmtpReplyCode** *(string) --* 

                  The SMTP reply code, as defined by `RFC 5321 <https://tools.ietf.org/html/rfc5321>`__ .

                  
                

                - **StatusCode** *(string) --* 

                  The SMTP enhanced status code, as defined by `RFC 3463 <https://tools.ietf.org/html/rfc3463>`__ .

                  
                

                - **Message** *(string) --* 

                  Human-readable text to include in the bounce message.

                  
                

                - **Sender** *(string) --* 

                  The email address of the sender of the bounced email. This is the address from which the bounce message will be sent.

                  
            
              

              - **WorkmailAction** *(dict) --* 

                Calls Amazon WorkMail and, optionally, publishes a notification to Amazon SNS.

                
                

                - **TopicArn** *(string) --* 

                  The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action is called. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

                  
                

                - **OrganizationArn** *(string) --* 

                  The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail organization ARN is ``arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7`` . For information about Amazon WorkMail organizations, see the `Amazon WorkMail Administrator Guide <http://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`__ .

                  
            
              

              - **LambdaAction** *(dict) --* 

                Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.

                
                

                - **TopicArn** *(string) --* 

                  The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action is taken. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

                  
                

                - **FunctionArn** *(string) --* 

                  The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS Lambda function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction`` . For more information about AWS Lambda, see the `AWS Lambda Developer Guide <http://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`__ .

                  
                

                - **InvocationType** *(string) --* 

                  The invocation type of the AWS Lambda function. An invocation type of ``RequestResponse`` means that the execution of the function will immediately result in a response, and a value of ``Event`` means that the function will be invoked asynchronously. The default value is ``Event`` . For information about AWS Lambda invocation types, see the `AWS Lambda Developer Guide <http://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`__ .

                   

                  .. warning::

                     

                    There is a 30-second timeout on ``RequestResponse`` invocations. You should use ``Event`` invocation in most cases. Use ``RequestResponse`` only when you want to make a mail flow decision, such as whether to stop the receipt rule or the receipt rule set.

                     

                  
            
              

              - **StopAction** *(dict) --* 

                Terminates the evaluation of the receipt rule set and optionally publishes a notification to Amazon SNS.

                
                

                - **Scope** *(string) --* 

                  The name of the RuleSet that is being stopped.

                  
                

                - **TopicArn** *(string) --* 

                  The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is taken. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

                  
            
              

              - **AddHeaderAction** *(dict) --* 

                Adds a header to the received email.

                
                

                - **HeaderName** *(string) --* 

                  The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

                  
                

                - **HeaderValue** *(string) --* 

                  Must be less than 2048 characters, and must not contain newline characters ("\r" or "\n").

                  
            
              

              - **SNSAction** *(dict) --* 

                Publishes the email content within a notification to Amazon SNS.

                
                

                - **TopicArn** *(string) --* 

                  The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

                  
                

                - **Encoding** *(string) --* 

                  The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier to use, but may not preserve all special characters when a message was encoded with a different encoding format. Base64 preserves all special characters. The default value is UTF-8.

                  
            
          
        
          

          - **ScanEnabled** *(boolean) --* 

            If ``true`` , then messages that this receipt rule applies to are scanned for spam and viruses. The default value is ``false`` .

            
      
    

    **Examples** 

    The following example returns the details of a receipt rule:
    ::

      response = client.describe_receipt_rule(
          RuleName='MyRule',
          RuleSetName='MyRuleSet',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Rule': {
              'Actions': [
                  {
                      'S3Action': {
                          'BucketName': 'MyBucket',
                          'ObjectKeyPrefix': 'email',
                      },
                  },
              ],
              'Enabled': True,
              'Name': 'MyRule',
              'ScanEnabled': True,
              'TlsPolicy': 'Optional',
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_receipt_rule_set(**kwargs)

    

    Returns the details of the specified receipt rule set.

     

    For information about managing receipt rule sets, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rule-sets.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/DescribeReceiptRuleSet>`_    


    **Request Syntax** 
    ::

      response = client.describe_receipt_rule_set(
          RuleSetName='string'
      )
    :type RuleSetName: string
    :param RuleSetName: **[REQUIRED]** 

      The name of the receipt rule set to describe.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Metadata': {
                'Name': 'string',
                'CreatedTimestamp': datetime(2015, 1, 1)
            },
            'Rules': [
                {
                    'Name': 'string',
                    'Enabled': True|False,
                    'TlsPolicy': 'Require'|'Optional',
                    'Recipients': [
                        'string',
                    ],
                    'Actions': [
                        {
                            'S3Action': {
                                'TopicArn': 'string',
                                'BucketName': 'string',
                                'ObjectKeyPrefix': 'string',
                                'KmsKeyArn': 'string'
                            },
                            'BounceAction': {
                                'TopicArn': 'string',
                                'SmtpReplyCode': 'string',
                                'StatusCode': 'string',
                                'Message': 'string',
                                'Sender': 'string'
                            },
                            'WorkmailAction': {
                                'TopicArn': 'string',
                                'OrganizationArn': 'string'
                            },
                            'LambdaAction': {
                                'TopicArn': 'string',
                                'FunctionArn': 'string',
                                'InvocationType': 'Event'|'RequestResponse'
                            },
                            'StopAction': {
                                'Scope': 'RuleSet',
                                'TopicArn': 'string'
                            },
                            'AddHeaderAction': {
                                'HeaderName': 'string',
                                'HeaderValue': 'string'
                            },
                            'SNSAction': {
                                'TopicArn': 'string',
                                'Encoding': 'UTF-8'|'Base64'
                            }
                        },
                    ],
                    'ScanEnabled': True|False
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the details of the specified receipt rule set.

        
        

        - **Metadata** *(dict) --* 

          The metadata for the receipt rule set, which consists of the rule set name and the timestamp of when the rule set was created.

          
          

          - **Name** *(string) --* 

            The name of the receipt rule set. The name must:

             

             
            * Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-). 
             
            * Start and end with a letter or number. 
             
            * Contain less than 64 characters. 
             

            
          

          - **CreatedTimestamp** *(datetime) --* 

            The date and time the receipt rule set was created.

            
      
        

        - **Rules** *(list) --* 

          A list of the receipt rules that belong to the specified receipt rule set.

          
          

          - *(dict) --* 

            Receipt rules enable you to specify which actions Amazon SES should take when it receives mail on behalf of one or more email addresses or domains that you own.

             

            Each receipt rule defines a set of email addresses or domains that it applies to. If the email addresses or domains match at least one recipient address of the message, Amazon SES executes all of the receipt rule's actions on the message.

             

            For information about setting up receipt rules, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html>`__ .

            
            

            - **Name** *(string) --* 

              The name of the receipt rule. The name must:

               

               
              * Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-). 
               
              * Start and end with a letter or number. 
               
              * Contain less than 64 characters. 
               

              
            

            - **Enabled** *(boolean) --* 

              If ``true`` , the receipt rule is active. The default value is ``false`` .

              
            

            - **TlsPolicy** *(string) --* 

              Specifies whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). If this parameter is set to ``Require`` , Amazon SES will bounce emails that are not received over TLS. The default is ``Optional`` .

              
            

            - **Recipients** *(list) --* 

              The recipient domains and email addresses that the receipt rule applies to. If this field is not specified, this rule will match all recipients under all verified domains.

              
              

              - *(string) --* 
          
            

            - **Actions** *(list) --* 

              An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule.

              
              

              - *(dict) --* 

                An action that Amazon SES can take when it receives an email on behalf of one or more email addresses or domains that you own. An instance of this data type can represent only one action.

                 

                For information about setting up receipt rules, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html>`__ .

                
                

                - **S3Action** *(dict) --* 

                  Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and, optionally, publishes a notification to Amazon SNS.

                  
                  

                  - **TopicArn** *(string) --* 

                    The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3 bucket. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

                    
                  

                  - **BucketName** *(string) --* 

                    The name of the Amazon S3 bucket that incoming email will be saved to.

                    
                  

                  - **ObjectKeyPrefix** *(string) --* 

                    The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory name that enables you to store similar data under the same directory in a bucket.

                    
                  

                  - **KmsKeyArn** *(string) --* 

                    The customer master key that Amazon SES should use to encrypt your emails before saving them to the Amazon S3 bucket. You can use the default master key or a custom master key you created in AWS KMS as follows:

                     

                     
                    * To use the default master key, provide an ARN in the form of ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if your AWS account ID is 123456789012 and you want to use the default master key in the US West (Oregon) region, the ARN of the default master key would be ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default master key, you don't need to perform any extra steps to give Amazon SES permission to use the key. 
                     
                    * To use a custom master key you created in AWS KMS, provide the ARN of the master key and ensure that you add a statement to your key's policy to give Amazon SES permission to use it. For more information about giving permissions, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html>`__ . 
                     

                     

                    For more information about key policies, see the `AWS KMS Developer Guide <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`__ . If you do not specify a master key, Amazon SES will not encrypt your emails.

                     

                    .. warning::

                       

                      Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3 server-side encryption. This means that you must use the Amazon S3 encryption client to decrypt the email after retrieving it from Amazon S3, as the service has no access to use your AWS KMS keys for decryption. This encryption client is currently available with the `AWS Java SDK <http://aws.amazon.com/sdk-for-java/>`__ and `AWS Ruby SDK <http://aws.amazon.com/sdk-for-ruby/>`__ only. For more information about client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer Guide <http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__ .

                       

                    
              
                

                - **BounceAction** *(dict) --* 

                  Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).

                  
                  

                  - **TopicArn** *(string) --* 

                    The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action is taken. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

                    
                  

                  - **SmtpReplyCode** *(string) --* 

                    The SMTP reply code, as defined by `RFC 5321 <https://tools.ietf.org/html/rfc5321>`__ .

                    
                  

                  - **StatusCode** *(string) --* 

                    The SMTP enhanced status code, as defined by `RFC 3463 <https://tools.ietf.org/html/rfc3463>`__ .

                    
                  

                  - **Message** *(string) --* 

                    Human-readable text to include in the bounce message.

                    
                  

                  - **Sender** *(string) --* 

                    The email address of the sender of the bounced email. This is the address from which the bounce message will be sent.

                    
              
                

                - **WorkmailAction** *(dict) --* 

                  Calls Amazon WorkMail and, optionally, publishes a notification to Amazon SNS.

                  
                  

                  - **TopicArn** *(string) --* 

                    The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action is called. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

                    
                  

                  - **OrganizationArn** *(string) --* 

                    The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail organization ARN is ``arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7`` . For information about Amazon WorkMail organizations, see the `Amazon WorkMail Administrator Guide <http://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`__ .

                    
              
                

                - **LambdaAction** *(dict) --* 

                  Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.

                  
                  

                  - **TopicArn** *(string) --* 

                    The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action is taken. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

                    
                  

                  - **FunctionArn** *(string) --* 

                    The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS Lambda function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction`` . For more information about AWS Lambda, see the `AWS Lambda Developer Guide <http://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`__ .

                    
                  

                  - **InvocationType** *(string) --* 

                    The invocation type of the AWS Lambda function. An invocation type of ``RequestResponse`` means that the execution of the function will immediately result in a response, and a value of ``Event`` means that the function will be invoked asynchronously. The default value is ``Event`` . For information about AWS Lambda invocation types, see the `AWS Lambda Developer Guide <http://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`__ .

                     

                    .. warning::

                       

                      There is a 30-second timeout on ``RequestResponse`` invocations. You should use ``Event`` invocation in most cases. Use ``RequestResponse`` only when you want to make a mail flow decision, such as whether to stop the receipt rule or the receipt rule set.

                       

                    
              
                

                - **StopAction** *(dict) --* 

                  Terminates the evaluation of the receipt rule set and optionally publishes a notification to Amazon SNS.

                  
                  

                  - **Scope** *(string) --* 

                    The name of the RuleSet that is being stopped.

                    
                  

                  - **TopicArn** *(string) --* 

                    The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is taken. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

                    
              
                

                - **AddHeaderAction** *(dict) --* 

                  Adds a header to the received email.

                  
                  

                  - **HeaderName** *(string) --* 

                    The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

                    
                  

                  - **HeaderValue** *(string) --* 

                    Must be less than 2048 characters, and must not contain newline characters ("\r" or "\n").

                    
              
                

                - **SNSAction** *(dict) --* 

                  Publishes the email content within a notification to Amazon SNS.

                  
                  

                  - **TopicArn** *(string) --* 

                    The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

                    
                  

                  - **Encoding** *(string) --* 

                    The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier to use, but may not preserve all special characters when a message was encoded with a different encoding format. Base64 preserves all special characters. The default value is UTF-8.

                    
              
            
          
            

            - **ScanEnabled** *(boolean) --* 

              If ``true`` , then messages that this receipt rule applies to are scanned for spam and viruses. The default value is ``false`` .

              
        
      
    

    **Examples** 

    The following example returns the metadata and receipt rules of a receipt rule set:
    ::

      response = client.describe_receipt_rule_set(
          RuleSetName='MyRuleSet',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Metadata': {
              'CreatedTimestamp': datetime(2016, 7, 15, 16, 25, 59, 4, 197, 0),
              'Name': 'MyRuleSet',
          },
          'Rules': [
              {
                  'Actions': [
                      {
                          'S3Action': {
                              'BucketName': 'MyBucket',
                              'ObjectKeyPrefix': 'email',
                          },
                      },
                  ],
                  'Enabled': True,
                  'Name': 'MyRule',
                  'ScanEnabled': True,
                  'TlsPolicy': 'Optional',
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


  .. py:method:: get_account_sending_enabled()

    

    Returns the email sending status of the Amazon SES account.

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/GetAccountSendingEnabled>`_    


    **Request Syntax** 

    ::

      response = client.get_account_sending_enabled()
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Enabled': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a request to return the email sending status for your Amazon SES account.

        
        

        - **Enabled** *(boolean) --* 

          Describes whether email sending is enabled or disabled for your Amazon SES account.

          
    

  .. py:method:: get_custom_verification_email_template(**kwargs)

    

    Returns the custom email verification template for the template name you specify.

     

    For more information about custom verification email templates, see `Using Custom Verification Email Templates <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-verification-emails.html>`__ in the *Amazon SES Developer Guide* .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/GetCustomVerificationEmailTemplate>`_    


    **Request Syntax** 
    ::

      response = client.get_custom_verification_email_template(
          TemplateName='string'
      )
    :type TemplateName: string
    :param TemplateName: **[REQUIRED]** 

      The name of the custom verification email template that you want to retrieve.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TemplateName': 'string',
            'FromEmailAddress': 'string',
            'TemplateSubject': 'string',
            'TemplateContent': 'string',
            'SuccessRedirectionURL': 'string',
            'FailureRedirectionURL': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The content of the custom verification email template.

        
        

        - **TemplateName** *(string) --* 

          The name of the custom verification email template.

          
        

        - **FromEmailAddress** *(string) --* 

          The email address that the custom verification email is sent from.

          
        

        - **TemplateSubject** *(string) --* 

          The subject line of the custom verification email.

          
        

        - **TemplateContent** *(string) --* 

          The content of the custom verification email.

          
        

        - **SuccessRedirectionURL** *(string) --* 

          The URL that the recipient of the verification email is sent to if his or her address is successfully verified.

          
        

        - **FailureRedirectionURL** *(string) --* 

          The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.

          
    

  .. py:method:: get_identity_dkim_attributes(**kwargs)

    

    Returns the current status of Easy DKIM signing for an entity. For domain name identities, this operation also returns the DKIM tokens that are required for Easy DKIM signing, and whether Amazon SES has successfully verified that these tokens have been published.

     

    This operation takes a list of identities as input and returns the following information for each:

     

     
    * Whether Easy DKIM signing is enabled or disabled. 
     
    * A set of DKIM tokens that represent the identity. If the identity is an email address, the tokens represent the domain of that address. 
     
    * Whether Amazon SES has successfully verified the DKIM tokens published in the domain's DNS. This information is only returned for domain name identities, not for email addresses. 
     

     

    This operation is throttled at one request per second and can only get DKIM attributes for up to 100 identities at a time.

     

    For more information about creating DNS records using DKIM tokens, go to the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim-dns-records.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/GetIdentityDkimAttributes>`_    


    **Request Syntax** 
    ::

      response = client.get_identity_dkim_attributes(
          Identities=[
              'string',
          ]
      )
    :type Identities: list
    :param Identities: **[REQUIRED]** 

      A list of one or more verified identities - email addresses, domains, or both.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DkimAttributes': {
                'string': {
                    'DkimEnabled': True|False,
                    'DkimVerificationStatus': 'Pending'|'Success'|'Failed'|'TemporaryFailure'|'NotStarted',
                    'DkimTokens': [
                        'string',
                    ]
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the status of Amazon SES Easy DKIM signing for an identity. For domain identities, this response also contains the DKIM tokens that are required for Easy DKIM signing, and whether Amazon SES successfully verified that these tokens were published.

        
        

        - **DkimAttributes** *(dict) --* 

          The DKIM attributes for an email address or a domain.

          
          

          - *(string) --* 
            

            - *(dict) --* 

              Represents the DKIM attributes of a verified email address or a domain.

              
              

              - **DkimEnabled** *(boolean) --* 

                True if DKIM signing is enabled for email sent from the identity; false otherwise. The default value is true.

                
              

              - **DkimVerificationStatus** *(string) --* 

                Describes whether Amazon SES has successfully verified the DKIM DNS records (tokens) published in the domain name's DNS. (This only applies to domain identities, not email address identities.)

                
              

              - **DkimTokens** *(list) --* 

                A set of character strings that represent the domain's identity. Using these tokens, you will need to create DNS CNAME records that point to DKIM public keys hosted by Amazon SES. Amazon Web Services will eventually detect that you have updated your DNS records; this detection process may take up to 72 hours. Upon successful detection, Amazon SES will be able to DKIM-sign email originating from that domain. (This only applies to domain identities, not email address identities.)

                 

                For more information about creating DNS records using DKIM tokens, go to the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim-dns-records.html>`__ .

                
                

                - *(string) --* 
            
          
      
    
    

    **Examples** 

    The following example retrieves the Amazon SES Easy DKIM attributes for a list of identities:
    ::

      response = client.get_identity_dkim_attributes(
          Identities=[
              'example.com',
              'user@example.com',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'DkimAttributes': {
              'example.com': {
                  'DkimEnabled': True,
                  'DkimTokens': [
                      'EXAMPLEjcs5xoyqytjsotsijas7236gr',
                      'EXAMPLEjr76cvoc6mysspnioorxsn6ep',
                      'EXAMPLEkbmkqkhlm2lyz77ppkulerm4k',
                  ],
                  'DkimVerificationStatus': 'Success',
              },
              'user@example.com': {
                  'DkimEnabled': False,
                  'DkimVerificationStatus': 'NotStarted',
              },
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_identity_mail_from_domain_attributes(**kwargs)

    

    Returns the custom MAIL FROM attributes for a list of identities (email addresses : domains).

     

    This operation is throttled at one request per second and can only get custom MAIL FROM attributes for up to 100 identities at a time.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/GetIdentityMailFromDomainAttributes>`_    


    **Request Syntax** 
    ::

      response = client.get_identity_mail_from_domain_attributes(
          Identities=[
              'string',
          ]
      )
    :type Identities: list
    :param Identities: **[REQUIRED]** 

      A list of one or more identities.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'MailFromDomainAttributes': {
                'string': {
                    'MailFromDomain': 'string',
                    'MailFromDomainStatus': 'Pending'|'Success'|'Failed'|'TemporaryFailure',
                    'BehaviorOnMXFailure': 'UseDefaultValue'|'RejectMessage'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the custom MAIL FROM attributes for a list of identities.

        
        

        - **MailFromDomainAttributes** *(dict) --* 

          A map of identities to custom MAIL FROM attributes.

          
          

          - *(string) --* 
            

            - *(dict) --* 

              Represents the custom MAIL FROM domain attributes of a verified identity (email address or domain).

              
              

              - **MailFromDomain** *(string) --* 

                The custom MAIL FROM domain that the identity is configured to use.

                
              

              - **MailFromDomainStatus** *(string) --* 

                The state that indicates whether Amazon SES has successfully read the MX record required for custom MAIL FROM domain setup. If the state is ``Success`` , Amazon SES uses the specified custom MAIL FROM domain when the verified identity sends an email. All other states indicate that Amazon SES takes the action described by ``BehaviorOnMXFailure`` .

                
              

              - **BehaviorOnMXFailure** *(string) --* 

                The action that Amazon SES takes if it cannot successfully read the required MX record when you send an email. A value of ``UseDefaultValue`` indicates that if Amazon SES cannot read the required MX record, it uses amazonses.com (or a subdomain of that) as the MAIL FROM domain. A value of ``RejectMessage`` indicates that if Amazon SES cannot read the required MX record, Amazon SES returns a ``MailFromDomainNotVerified`` error and does not send the email.

                 

                The custom MAIL FROM setup states that result in this behavior are ``Pending`` , ``Failed`` , and ``TemporaryFailure`` .

                
          
      
    
    

    **Examples** 

    The following example returns the custom MAIL FROM attributes for an identity:
    ::

      response = client.get_identity_mail_from_domain_attributes(
          Identities=[
              'example.com',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'MailFromDomainAttributes': {
              'example.com': {
                  'BehaviorOnMXFailure': 'UseDefaultValue',
                  'MailFromDomain': 'bounces.example.com',
                  'MailFromDomainStatus': 'Success',
              },
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_identity_notification_attributes(**kwargs)

    

    Given a list of verified identities (email addresses and/or domains), returns a structure describing identity notification attributes.

     

    This operation is throttled at one request per second and can only get notification attributes for up to 100 identities at a time.

     

    For more information about using notifications with Amazon SES, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/notifications.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/GetIdentityNotificationAttributes>`_    


    **Request Syntax** 
    ::

      response = client.get_identity_notification_attributes(
          Identities=[
              'string',
          ]
      )
    :type Identities: list
    :param Identities: **[REQUIRED]** 

      A list of one or more identities. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: ``user@example.com`` , ``example.com`` , ``arn:aws:ses:us-east-1:123456789012:identity/example.com`` .

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NotificationAttributes': {
                'string': {
                    'BounceTopic': 'string',
                    'ComplaintTopic': 'string',
                    'DeliveryTopic': 'string',
                    'ForwardingEnabled': True|False,
                    'HeadersInBounceNotificationsEnabled': True|False,
                    'HeadersInComplaintNotificationsEnabled': True|False,
                    'HeadersInDeliveryNotificationsEnabled': True|False
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the notification attributes for a list of identities.

        
        

        - **NotificationAttributes** *(dict) --* 

          A map of Identity to IdentityNotificationAttributes.

          
          

          - *(string) --* 
            

            - *(dict) --* 

              Represents the notification attributes of an identity, including whether an identity has Amazon Simple Notification Service (Amazon SNS) topics set for bounce, complaint, and/or delivery notifications, and whether feedback forwarding is enabled for bounce and complaint notifications.

              
              

              - **BounceTopic** *(string) --* 

                The Amazon Resource Name (ARN) of the Amazon SNS topic where Amazon SES will publish bounce notifications.

                
              

              - **ComplaintTopic** *(string) --* 

                The Amazon Resource Name (ARN) of the Amazon SNS topic where Amazon SES will publish complaint notifications.

                
              

              - **DeliveryTopic** *(string) --* 

                The Amazon Resource Name (ARN) of the Amazon SNS topic where Amazon SES will publish delivery notifications.

                
              

              - **ForwardingEnabled** *(boolean) --* 

                Describes whether Amazon SES will forward bounce and complaint notifications as email. ``true`` indicates that Amazon SES will forward bounce and complaint notifications as email, while ``false`` indicates that bounce and complaint notifications will be published only to the specified bounce and complaint Amazon SNS topics.

                
              

              - **HeadersInBounceNotificationsEnabled** *(boolean) --* 

                Describes whether Amazon SES includes the original email headers in Amazon SNS notifications of type ``Bounce`` . A value of ``true`` specifies that Amazon SES will include headers in bounce notifications, and a value of ``false`` specifies that Amazon SES will not include headers in bounce notifications.

                
              

              - **HeadersInComplaintNotificationsEnabled** *(boolean) --* 

                Describes whether Amazon SES includes the original email headers in Amazon SNS notifications of type ``Complaint`` . A value of ``true`` specifies that Amazon SES will include headers in complaint notifications, and a value of ``false`` specifies that Amazon SES will not include headers in complaint notifications.

                
              

              - **HeadersInDeliveryNotificationsEnabled** *(boolean) --* 

                Describes whether Amazon SES includes the original email headers in Amazon SNS notifications of type ``Delivery`` . A value of ``true`` specifies that Amazon SES will include headers in delivery notifications, and a value of ``false`` specifies that Amazon SES will not include headers in delivery notifications.

                
          
      
    
    

    **Examples** 

    The following example returns the notification attributes for an identity:
    ::

      response = client.get_identity_notification_attributes(
          Identities=[
              'example.com',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'NotificationAttributes': {
              'example.com': {
                  'BounceTopic': 'arn:aws:sns:us-east-1:EXAMPLE65304:ExampleTopic',
                  'ForwardingEnabled': True,
                  'HeadersInBounceNotificationsEnabled': False,
                  'HeadersInComplaintNotificationsEnabled': False,
                  'HeadersInDeliveryNotificationsEnabled': False,
              },
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_identity_policies(**kwargs)

    

    Returns the requested sending authorization policies for the given identity (an email address or a domain). The policies are returned as a map of policy names to policy contents. You can retrieve a maximum of 20 policies at a time.

     

    .. note::

       

      This API is for the identity owner only. If you have not verified the identity, this API will return an error.

       

     

    Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/GetIdentityPolicies>`_    


    **Request Syntax** 
    ::

      response = client.get_identity_policies(
          Identity='string',
          PolicyNames=[
              'string',
          ]
      )
    :type Identity: string
    :param Identity: **[REQUIRED]** 

      The identity for which the policies will be retrieved. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: ``user@example.com`` , ``example.com`` , ``arn:aws:ses:us-east-1:123456789012:identity/example.com`` .

       

      To successfully call this API, you must own the identity.

      

    
    :type PolicyNames: list
    :param PolicyNames: **[REQUIRED]** 

      A list of the names of policies to be retrieved. You can retrieve a maximum of 20 policies at a time. If you do not know the names of the policies that are attached to the identity, you can use ``ListIdentityPolicies`` .

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Policies': {
                'string': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents the requested sending authorization policies.

        
        

        - **Policies** *(dict) --* 

          A map of policy names to policies.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
    

    **Examples** 

    The following example returns a sending authorization policy for an identity:
    ::

      response = client.get_identity_policies(
          Identity='example.com',
          PolicyNames=[
              'MyPolicy',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Policies': {
              'MyPolicy': '{"Version":"2008-10-17","Statement":[{"Sid":"stmt1469123904194","Effect":"Allow","Principal":{"AWS":"arn:aws:iam::123456789012:root"},"Action":["ses:SendEmail","ses:SendRawEmail"],"Resource":"arn:aws:ses:us-east-1:EXAMPLE65304:identity/example.com"}]}',
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_identity_verification_attributes(**kwargs)

    

    Given a list of identities (email addresses and/or domains), returns the verification status and (for domain identities) the verification token for each identity.

     

    The verification status of an email address is "Pending" until the email address owner clicks the link within the verification email that Amazon SES sent to that address. If the email address owner clicks the link within 24 hours, the verification status of the email address changes to "Success". If the link is not clicked within 24 hours, the verification status changes to "Failed." In that case, if you still want to verify the email address, you must restart the verification process from the beginning.

     

    For domain identities, the domain's verification status is "Pending" as Amazon SES searches for the required TXT record in the DNS settings of the domain. When Amazon SES detects the record, the domain's verification status changes to "Success". If Amazon SES is unable to detect the record within 72 hours, the domain's verification status changes to "Failed." In that case, if you still want to verify the domain, you must restart the verification process from the beginning.

     

    This operation is throttled at one request per second and can only get verification attributes for up to 100 identities at a time.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/GetIdentityVerificationAttributes>`_    


    **Request Syntax** 
    ::

      response = client.get_identity_verification_attributes(
          Identities=[
              'string',
          ]
      )
    :type Identities: list
    :param Identities: **[REQUIRED]** 

      A list of identities.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'VerificationAttributes': {
                'string': {
                    'VerificationStatus': 'Pending'|'Success'|'Failed'|'TemporaryFailure'|'NotStarted',
                    'VerificationToken': 'string'
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        The Amazon SES verification status of a list of identities. For domain identities, this response also contains the verification token.

        
        

        - **VerificationAttributes** *(dict) --* 

          A map of Identities to IdentityVerificationAttributes objects.

          
          

          - *(string) --* 
            

            - *(dict) --* 

              Represents the verification attributes of a single identity.

              
              

              - **VerificationStatus** *(string) --* 

                The verification status of the identity: "Pending", "Success", "Failed", or "TemporaryFailure".

                
              

              - **VerificationToken** *(string) --* 

                The verification token for a domain identity. Null for email address identities.

                
          
      
    
    

    **Examples** 

    The following example returns the verification status and the verification token for a domain identity:
    ::

      response = client.get_identity_verification_attributes(
          Identities=[
              'example.com',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'VerificationAttributes': {
              'example.com': {
                  'VerificationStatus': 'Success',
                  'VerificationToken': 'EXAMPLE3VYb9EDI2nTOQRi/Tf6MI/6bD6THIGiP1MVY=',
              },
          },
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


  .. py:method:: get_send_quota()

    

    Provides the sending limits for the Amazon SES account. 

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/GetSendQuota>`_    


    **Request Syntax** 

    ::

      response = client.get_send_quota()
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Max24HourSend': 123.0,
            'MaxSendRate': 123.0,
            'SentLast24Hours': 123.0
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents your Amazon SES daily sending quota, maximum send rate, and the number of emails you have sent in the last 24 hours.

        
        

        - **Max24HourSend** *(float) --* 

          The maximum number of emails the user is allowed to send in a 24-hour interval. A value of -1 signifies an unlimited quota.

          
        

        - **MaxSendRate** *(float) --* 

          The maximum number of emails that Amazon SES can accept from the user's account per second.

           

          .. note::

             

            The rate at which Amazon SES accepts the user's messages might be less than the maximum send rate.

             

          
        

        - **SentLast24Hours** *(float) --* 

          The number of emails sent during the previous 24 hours.

          
    

    **Examples** 

    The following example returns the Amazon SES sending limits for an AWS account:
    ::

      response = client.get_send_quota(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Max24HourSend': 200,
          'MaxSendRate': 1,
          'SentLast24Hours': 1,
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_send_statistics()

    

    Provides sending statistics for the Amazon SES account. The result is a list of data points, representing the last two weeks of sending activity. Each data point in the list contains statistics for a 15-minute period of time.

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/GetSendStatistics>`_    


    **Request Syntax** 

    ::

      response = client.get_send_statistics()
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'SendDataPoints': [
                {
                    'Timestamp': datetime(2015, 1, 1),
                    'DeliveryAttempts': 123,
                    'Bounces': 123,
                    'Complaints': 123,
                    'Rejects': 123
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a list of data points. This list contains aggregated data from the previous two weeks of your sending activity with Amazon SES.

        
        

        - **SendDataPoints** *(list) --* 

          A list of data points, each of which represents 15 minutes of activity.

          
          

          - *(dict) --* 

            Represents sending statistics data. Each ``SendDataPoint`` contains statistics for a 15-minute period of sending activity. 

            
            

            - **Timestamp** *(datetime) --* 

              Time of the data point.

              
            

            - **DeliveryAttempts** *(integer) --* 

              Number of emails that have been sent.

              
            

            - **Bounces** *(integer) --* 

              Number of emails that have bounced.

              
            

            - **Complaints** *(integer) --* 

              Number of unwanted emails that were rejected by recipients.

              
            

            - **Rejects** *(integer) --* 

              Number of emails rejected by Amazon SES.

              
        
      
    

    **Examples** 

    The following example returns Amazon SES sending statistics:
    ::

      response = client.get_send_statistics(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'SendDataPoints': [
              {
                  'Bounces': 0,
                  'Complaints': 0,
                  'DeliveryAttempts': 5,
                  'Rejects': 0,
                  'Timestamp': datetime(2016, 7, 13, 22, 43, 0, 2, 195, 0),
              },
              {
                  'Bounces': 0,
                  'Complaints': 0,
                  'DeliveryAttempts': 3,
                  'Rejects': 0,
                  'Timestamp': datetime(2016, 7, 13, 23, 13, 0, 2, 195, 0),
              },
              {
                  'Bounces': 0,
                  'Complaints': 0,
                  'DeliveryAttempts': 1,
                  'Rejects': 0,
                  'Timestamp': datetime(2016, 7, 13, 21, 13, 0, 2, 195, 0),
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_template(**kwargs)

    

    Displays the template object (which includes the Subject line, HTML part and text part) for the template you specify.

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/GetTemplate>`_    


    **Request Syntax** 
    ::

      response = client.get_template(
          TemplateName='string'
      )
    :type TemplateName: string
    :param TemplateName: **[REQUIRED]** 

      The name of the template you want to retrieve.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Template': {
                'TemplateName': 'string',
                'SubjectPart': 'string',
                'TextPart': 'string',
                'HtmlPart': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Template** *(dict) --* 

          The content of the email, composed of a subject line, an HTML part, and a text-only part.

          
          

          - **TemplateName** *(string) --* 

            The name of the template. You will refer to this name when you send email using the ``SendTemplatedEmail`` or ``SendBulkTemplatedEmail`` operations.

            
          

          - **SubjectPart** *(string) --* 

            The subject line of the email.

            
          

          - **TextPart** *(string) --* 

            The email body that will be visible to recipients whose email clients do not display HTML.

            
          

          - **HtmlPart** *(string) --* 

            The HTML body of the email.

            
      
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: list_configuration_sets(**kwargs)

    

    Provides a list of the configuration sets associated with your Amazon SES account. For information about using configuration sets, see `Monitoring Your Amazon SES Sending Activity <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ in the *Amazon SES Developer Guide.*  

     

    You can execute this operation no more than once per second. This operation will return up to 1,000 configuration sets each time it is run. If your Amazon SES account has more than 1,000 configuration sets, this operation will also return a NextToken element. You can then execute the ``ListConfigurationSets`` operation again, passing the ``NextToken`` parameter and the value of the NextToken element to retrieve additional results.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/ListConfigurationSets>`_    


    **Request Syntax** 
    ::

      response = client.list_configuration_sets(
          NextToken='string',
          MaxItems=123
      )
    :type NextToken: string
    :param NextToken: 

      A token returned from a previous call to ``ListConfigurationSets`` to indicate the position of the configuration set in the configuration set list.

      

    
    :type MaxItems: integer
    :param MaxItems: 

      The number of configuration sets to return.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ConfigurationSets': [
                {
                    'Name': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A list of configuration sets associated with your AWS account. Configuration sets enable you to publish email sending events. For information about using configuration sets, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

        
        

        - **ConfigurationSets** *(list) --* 

          A list of configuration sets.

          
          

          - *(dict) --* 

            The name of the configuration set.

             

            Configuration sets let you create groups of rules that you can apply to the emails you send using Amazon SES. For more information about using configuration sets, see `Using Amazon SES Configuration Sets <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/using-configuration-sets.html>`__ in the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/>`__ .

            
            

            - **Name** *(string) --* 

              The name of the configuration set. The name must meet the following requirements:

               

               
              * Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
               
              * Contain 64 characters or fewer. 
               

              
        
      
        

        - **NextToken** *(string) --* 

          A token indicating that there are additional configuration sets available to be listed. Pass this token to successive calls of ``ListConfigurationSets`` . 

          
    

  .. py:method:: list_custom_verification_email_templates(**kwargs)

    

    Lists the existing custom verification email templates for your account.

     

    For more information about custom verification email templates, see `Using Custom Verification Email Templates <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-verification-emails.html>`__ in the *Amazon SES Developer Guide* .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/ListCustomVerificationEmailTemplates>`_    


    **Request Syntax** 
    ::

      response = client.list_custom_verification_email_templates(
          NextToken='string',
          MaxResults=123
      )
    :type NextToken: string
    :param NextToken: 

      A token returned from a previous call to ``ListCustomVerificationEmailTemplates`` to indicate the position in the list of email templates.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of custom verification email templates to return. This value must be at least 1 and less than or equal to 50. If you do not specify a value, or if you specify a value less than 1 or greater than 50, the operation will return up to 50 results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CustomVerificationEmailTemplates': [
                {
                    'TemplateName': 'string',
                    'FromEmailAddress': 'string',
                    'TemplateSubject': 'string',
                    'SuccessRedirectionURL': 'string',
                    'FailureRedirectionURL': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A paginated list of custom verification email templates.

        
        

        - **CustomVerificationEmailTemplates** *(list) --* 

          A list of the custom verification email templates that exist in your account.

          
          

          - *(dict) --* 

            Contains information about a custom verification email template.

            
            

            - **TemplateName** *(string) --* 

              The name of the custom verification email template.

              
            

            - **FromEmailAddress** *(string) --* 

              The email address that the custom verification email is sent from.

              
            

            - **TemplateSubject** *(string) --* 

              The subject line of the custom verification email.

              
            

            - **SuccessRedirectionURL** *(string) --* 

              The URL that the recipient of the verification email is sent to if his or her address is successfully verified.

              
            

            - **FailureRedirectionURL** *(string) --* 

              The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.

              
        
      
        

        - **NextToken** *(string) --* 

          A token indicating that there are additional custom verification email templates available to be listed. Pass this token to a subsequent call to ``ListCustomVerificationEmailTemplates`` to retrieve the next 50 custom verification email templates.

          
    

  .. py:method:: list_identities(**kwargs)

    

    Returns a list containing all of the identities (email addresses and domains) for your AWS account, regardless of verification status.

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/ListIdentities>`_    


    **Request Syntax** 
    ::

      response = client.list_identities(
          IdentityType='EmailAddress'|'Domain',
          NextToken='string',
          MaxItems=123
      )
    :type IdentityType: string
    :param IdentityType: 

      The type of the identities to list. Possible values are "EmailAddress" and "Domain". If this parameter is omitted, then all identities will be listed.

      

    
    :type NextToken: string
    :param NextToken: 

      The token to use for pagination.

      

    
    :type MaxItems: integer
    :param MaxItems: 

      The maximum number of identities per page. Possible values are 1-1000 inclusive.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Identities': [
                'string',
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A list of all identities that you have attempted to verify under your AWS account, regardless of verification status.

        
        

        - **Identities** *(list) --* 

          A list of identities.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          The token used for pagination.

          
    

    **Examples** 

    The following example lists the email address identities that have been submitted for verification with Amazon SES:
    ::

      response = client.list_identities(
          IdentityType='EmailAddress',
          MaxItems=123,
          NextToken='',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Identities': [
              'user@example.com',
          ],
          'NextToken': '',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_identity_policies(**kwargs)

    

    Returns a list of sending authorization policies that are attached to the given identity (an email address or a domain). This API returns only a list. If you want the actual policy content, you can use ``GetIdentityPolicies`` .

     

    .. note::

       

      This API is for the identity owner only. If you have not verified the identity, this API will return an error.

       

     

    Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/ListIdentityPolicies>`_    


    **Request Syntax** 
    ::

      response = client.list_identity_policies(
          Identity='string'
      )
    :type Identity: string
    :param Identity: **[REQUIRED]** 

      The identity that is associated with the policy for which the policies will be listed. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: ``user@example.com`` , ``example.com`` , ``arn:aws:ses:us-east-1:123456789012:identity/example.com`` .

       

      To successfully call this API, you must own the identity.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'PolicyNames': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A list of names of sending authorization policies that apply to an identity.

        
        

        - **PolicyNames** *(list) --* 

          A list of names of policies that apply to the specified identity.

          
          

          - *(string) --* 
      
    

    **Examples** 

    The following example returns a list of sending authorization policies that are attached to an identity:
    ::

      response = client.list_identity_policies(
          Identity='example.com',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'PolicyNames': [
              'MyPolicy',
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_receipt_filters()

    

    Lists the IP address filters associated with your AWS account.

     

    For information about managing IP address filters, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-ip-filters.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/ListReceiptFilters>`_    


    **Request Syntax** 
    ::

      response = client.list_receipt_filters()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Filters': [
                {
                    'Name': 'string',
                    'IpFilter': {
                        'Policy': 'Block'|'Allow',
                        'Cidr': 'string'
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A list of IP address filters that exist under your AWS account.

        
        

        - **Filters** *(list) --* 

          A list of IP address filter data structures, which each consist of a name, an IP address range, and whether to allow or block mail from it.

          
          

          - *(dict) --* 

            A receipt IP address filter enables you to specify whether to accept or reject mail originating from an IP address or range of IP addresses.

             

            For information about setting up IP address filters, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-ip-filters.html>`__ .

            
            

            - **Name** *(string) --* 

              The name of the IP address filter. The name must:

               

               
              * Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-). 
               
              * Start and end with a letter or number. 
               
              * Contain less than 64 characters. 
               

              
            

            - **IpFilter** *(dict) --* 

              A structure that provides the IP addresses to block or allow, and whether to block or allow incoming mail from them.

              
              

              - **Policy** *(string) --* 

                Indicates whether to block or allow incoming mail from the specified IP addresses.

                
              

              - **Cidr** *(string) --* 

                A single IP address or a range of IP addresses that you want to block or allow, specified in Classless Inter-Domain Routing (CIDR) notation. An example of a single email address is 10.0.0.1. An example of a range of IP addresses is 10.0.0.1/24. For more information about CIDR notation, see `RFC 2317 <https://tools.ietf.org/html/rfc2317>`__ .

                
          
        
      
    

    **Examples** 

    The following example lists the IP address filters that are associated with an AWS account:
    ::

      response = client.list_receipt_filters(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Filters': [
              {
                  'IpFilter': {
                      'Cidr': '1.2.3.4/24',
                      'Policy': 'Block',
                  },
                  'Name': 'MyFilter',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_receipt_rule_sets(**kwargs)

    

    Lists the receipt rule sets that exist under your AWS account. If there are additional receipt rule sets to be retrieved, you will receive a ``NextToken`` that you can provide to the next call to ``ListReceiptRuleSets`` to retrieve the additional entries.

     

    For information about managing receipt rule sets, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rule-sets.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/ListReceiptRuleSets>`_    


    **Request Syntax** 
    ::

      response = client.list_receipt_rule_sets(
          NextToken='string'
      )
    :type NextToken: string
    :param NextToken: 

      A token returned from a previous call to ``ListReceiptRuleSets`` to indicate the position in the receipt rule set list.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'RuleSets': [
                {
                    'Name': 'string',
                    'CreatedTimestamp': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        A list of receipt rule sets that exist under your AWS account.

        
        

        - **RuleSets** *(list) --* 

          The metadata for the currently active receipt rule set. The metadata consists of the rule set name and the timestamp of when the rule set was created.

          
          

          - *(dict) --* 

            Information about a receipt rule set.

             

            A receipt rule set is a collection of rules that specify what Amazon SES should do with mail it receives on behalf of your account's verified domains.

             

            For information about setting up receipt rule sets, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rule-set.html>`__ .

            
            

            - **Name** *(string) --* 

              The name of the receipt rule set. The name must:

               

               
              * Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-). 
               
              * Start and end with a letter or number. 
               
              * Contain less than 64 characters. 
               

              
            

            - **CreatedTimestamp** *(datetime) --* 

              The date and time the receipt rule set was created.

              
        
      
        

        - **NextToken** *(string) --* 

          A token indicating that there are additional receipt rule sets available to be listed. Pass this token to successive calls of ``ListReceiptRuleSets`` to retrieve up to 100 receipt rule sets at a time.

          
    

    **Examples** 

    The following example lists the receipt rule sets that exist under an AWS account:
    ::

      response = client.list_receipt_rule_sets(
          NextToken='',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'NextToken': '',
          'RuleSets': [
              {
                  'CreatedTimestamp': datetime(2016, 7, 15, 16, 25, 59, 4, 197, 0),
                  'Name': 'MyRuleSet',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_templates(**kwargs)

    

    Lists the email templates present in your Amazon SES account.

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/ListTemplates>`_    


    **Request Syntax** 
    ::

      response = client.list_templates(
          NextToken='string',
          MaxItems=123
      )
    :type NextToken: string
    :param NextToken: 

      The token to use for pagination.

      

    
    :type MaxItems: integer
    :param MaxItems: 

      The maximum number of templates to return. This value must be at least 1 and less than or equal to 10. If you do not specify a value, or if you specify a value less than 1 or greater than 10, the operation will return up to 10 results.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TemplatesMetadata': [
                {
                    'Name': 'string',
                    'CreatedTimestamp': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TemplatesMetadata** *(list) --* 

          An array the contains the name of creation time stamp for each template in your Amazon SES account.

          
          

          - *(dict) --* 

            Information about an email template.

            
            

            - **Name** *(string) --* 

              The name of the template.

              
            

            - **CreatedTimestamp** *(datetime) --* 

              The time and date the template was created.

              
        
      
        

        - **NextToken** *(string) --* 

          The token to use for pagination.

          
    

  .. py:method:: list_verified_email_addresses()

    

    Deprecated. Use the ``ListIdentities`` operation to list the email addresses and domains associated with your account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/ListVerifiedEmailAddresses>`_    


    **Request Syntax** 

    ::

      response = client.list_verified_email_addresses()
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'VerifiedEmailAddresses': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        A list of email addresses that you have verified with Amazon SES under your AWS account.

        
        

        - **VerifiedEmailAddresses** *(list) --* 

          A list of email addresses that have been verified.

          
          

          - *(string) --* 
      
    

    **Examples** 

    The following example lists all email addresses that have been submitted for verification with Amazon SES:
    ::

      response = client.list_verified_email_addresses(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'VerifiedEmailAddresses': [
              'user1@example.com',
              'user2@example.com',
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: put_identity_policy(**kwargs)

    

    Adds or updates a sending authorization policy for the specified identity (an email address or a domain).

     

    .. note::

       

      This API is for the identity owner only. If you have not verified the identity, this API will return an error.

       

     

    Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/PutIdentityPolicy>`_    


    **Request Syntax** 
    ::

      response = client.put_identity_policy(
          Identity='string',
          PolicyName='string',
          Policy='string'
      )
    :type Identity: string
    :param Identity: **[REQUIRED]** 

      The identity that the policy will apply to. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: ``user@example.com`` , ``example.com`` , ``arn:aws:ses:us-east-1:123456789012:identity/example.com`` .

       

      To successfully call this API, you must own the identity.

      

    
    :type PolicyName: string
    :param PolicyName: **[REQUIRED]** 

      The name of the policy.

       

      The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.

      

    
    :type Policy: string
    :param Policy: **[REQUIRED]** 

      The text of the policy in JSON format. The policy cannot exceed 4 KB.

       

      For information about the syntax of sending authorization policies, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization-policies.html>`__ . 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

    **Examples** 

    The following example adds a sending authorization policy to an identity:
    ::

      response = client.put_identity_policy(
          Identity='example.com',
          Policy='{"Version":"2008-10-17","Statement":[{"Sid":"stmt1469123904194","Effect":"Allow","Principal":{"AWS":"arn:aws:iam::123456789012:root"},"Action":["ses:SendEmail","ses:SendRawEmail"],"Resource":"arn:aws:ses:us-east-1:EXAMPLE65304:identity/example.com"}]}',
          PolicyName='MyPolicy',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: reorder_receipt_rule_set(**kwargs)

    

    Reorders the receipt rules within a receipt rule set.

     

    .. note::

       

      All of the rules in the rule set must be represented in this request. That is, this API will return an error if the reorder request doesn't explicitly position all of the rules.

       

     

    For information about managing receipt rule sets, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rule-sets.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/ReorderReceiptRuleSet>`_    


    **Request Syntax** 
    ::

      response = client.reorder_receipt_rule_set(
          RuleSetName='string',
          RuleNames=[
              'string',
          ]
      )
    :type RuleSetName: string
    :param RuleSetName: **[REQUIRED]** 

      The name of the receipt rule set to reorder.

      

    
    :type RuleNames: list
    :param RuleNames: **[REQUIRED]** 

      A list of the specified receipt rule set's receipt rules in the order that you want to put them.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

    **Examples** 

    The following example reorders the receipt rules within a receipt rule set:
    ::

      response = client.reorder_receipt_rule_set(
          RuleNames=[
              'MyRule',
              'MyOtherRule',
          ],
          RuleSetName='MyRuleSet',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: send_bounce(**kwargs)

    

    Generates and sends a bounce message to the sender of an email you received through Amazon SES. You can only use this API on an email up to 24 hours after you receive it.

     

    .. note::

       

      You cannot use this API to send generic bounces for mail that was not received by Amazon SES.

       

     

    For information about receiving email through Amazon SES, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/SendBounce>`_    


    **Request Syntax** 
    ::

      response = client.send_bounce(
          OriginalMessageId='string',
          BounceSender='string',
          Explanation='string',
          MessageDsn={
              'ReportingMta': 'string',
              'ArrivalDate': datetime(2015, 1, 1),
              'ExtensionFields': [
                  {
                      'Name': 'string',
                      'Value': 'string'
                  },
              ]
          },
          BouncedRecipientInfoList=[
              {
                  'Recipient': 'string',
                  'RecipientArn': 'string',
                  'BounceType': 'DoesNotExist'|'MessageTooLarge'|'ExceededQuota'|'ContentRejected'|'Undefined'|'TemporaryFailure',
                  'RecipientDsnFields': {
                      'FinalRecipient': 'string',
                      'Action': 'failed'|'delayed'|'delivered'|'relayed'|'expanded',
                      'RemoteMta': 'string',
                      'Status': 'string',
                      'DiagnosticCode': 'string',
                      'LastAttemptDate': datetime(2015, 1, 1),
                      'ExtensionFields': [
                          {
                              'Name': 'string',
                              'Value': 'string'
                          },
                      ]
                  }
              },
          ],
          BounceSenderArn='string'
      )
    :type OriginalMessageId: string
    :param OriginalMessageId: **[REQUIRED]** 

      The message ID of the message to be bounced.

      

    
    :type BounceSender: string
    :param BounceSender: **[REQUIRED]** 

      The address to use in the "From" header of the bounce message. This must be an identity that you have verified with Amazon SES.

      

    
    :type Explanation: string
    :param Explanation: 

      Human-readable text for the bounce message to explain the failure. If not specified, the text will be auto-generated based on the bounced recipient information.

      

    
    :type MessageDsn: dict
    :param MessageDsn: 

      Message-related DSN fields. If not specified, Amazon SES will choose the values.

      

    
      - **ReportingMta** *(string) --* **[REQUIRED]** 

        The reporting MTA that attempted to deliver the message, formatted as specified in `RFC 3464 <https://tools.ietf.org/html/rfc3464>`__ (``mta-name-type; mta-name`` ). The default value is ``dns; inbound-smtp.[region].amazonaws.com`` .

        

      
      - **ArrivalDate** *(datetime) --* 

        When the message was received by the reporting mail transfer agent (MTA), in `RFC 822 <https://www.ietf.org/rfc/rfc0822.txt>`__ date-time format.

        

      
      - **ExtensionFields** *(list) --* 

        Additional X-headers to include in the DSN.

        

      
        - *(dict) --* 

          Additional X-headers to include in the Delivery Status Notification (DSN) when an email that Amazon SES receives on your behalf bounces.

           

          For information about receiving email through Amazon SES, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email.html>`__ .

          

        
          - **Name** *(string) --* **[REQUIRED]** 

            The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

            

          
          - **Value** *(string) --* **[REQUIRED]** 

            The value of the header to add. Must be less than 2048 characters, and must not contain newline characters ("\r" or "\n").

            

          
        
    
    
    :type BouncedRecipientInfoList: list
    :param BouncedRecipientInfoList: **[REQUIRED]** 

      A list of recipients of the bounced message, including the information required to create the Delivery Status Notifications (DSNs) for the recipients. You must specify at least one ``BouncedRecipientInfo`` in the list.

      

    
      - *(dict) --* 

        Recipient-related information to include in the Delivery Status Notification (DSN) when an email that Amazon SES receives on your behalf bounces.

         

        For information about receiving email through Amazon SES, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email.html>`__ .

        

      
        - **Recipient** *(string) --* **[REQUIRED]** 

          The email address of the recipient of the bounced email.

          

        
        - **RecipientArn** *(string) --* 

          This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to receive email for the recipient of the bounced email. For more information about sending authorization, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html>`__ .

          

        
        - **BounceType** *(string) --* 

          The reason for the bounce. You must provide either this parameter or ``RecipientDsnFields`` .

          

        
        - **RecipientDsnFields** *(dict) --* 

          Recipient-related DSN fields, most of which would normally be filled in automatically when provided with a ``BounceType`` . You must provide either this parameter or ``BounceType`` .

          

        
          - **FinalRecipient** *(string) --* 

            The email address that the message was ultimately delivered to. This corresponds to the ``Final-Recipient`` in the DSN. If not specified, ``FinalRecipient`` will be set to the ``Recipient`` specified in the ``BouncedRecipientInfo`` structure. Either ``FinalRecipient`` or the recipient in ``BouncedRecipientInfo`` must be a recipient of the original bounced message.

             

            .. note::

               

              Do not prepend the ``FinalRecipient`` email address with ``rfc 822;`` , as described in `RFC 3798 <https://tools.ietf.org/html/rfc3798>`__ .

               

            

          
          - **Action** *(string) --* **[REQUIRED]** 

            The action performed by the reporting mail transfer agent (MTA) as a result of its attempt to deliver the message to the recipient address. This is required by `RFC 3464 <https://tools.ietf.org/html/rfc3464>`__ .

            

          
          - **RemoteMta** *(string) --* 

            The MTA to which the remote MTA attempted to deliver the message, formatted as specified in `RFC 3464 <https://tools.ietf.org/html/rfc3464>`__ (``mta-name-type; mta-name`` ). This parameter typically applies only to propagating synchronous bounces.

            

          
          - **Status** *(string) --* **[REQUIRED]** 

            The status code that indicates what went wrong. This is required by `RFC 3464 <https://tools.ietf.org/html/rfc3464>`__ .

            

          
          - **DiagnosticCode** *(string) --* 

            An extended explanation of what went wrong; this is usually an SMTP response. See `RFC 3463 <https://tools.ietf.org/html/rfc3463>`__ for the correct formatting of this parameter.

            

          
          - **LastAttemptDate** *(datetime) --* 

            The time the final delivery attempt was made, in `RFC 822 <https://www.ietf.org/rfc/rfc0822.txt>`__ date-time format.

            

          
          - **ExtensionFields** *(list) --* 

            Additional X-headers to include in the DSN.

            

          
            - *(dict) --* 

              Additional X-headers to include in the Delivery Status Notification (DSN) when an email that Amazon SES receives on your behalf bounces.

               

              For information about receiving email through Amazon SES, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email.html>`__ .

              

            
              - **Name** *(string) --* **[REQUIRED]** 

                The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

                

              
              - **Value** *(string) --* **[REQUIRED]** 

                The value of the header to add. Must be less than 2048 characters, and must not contain newline characters ("\r" or "\n").

                

              
            
        
        
      
  
    :type BounceSenderArn: string
    :param BounceSenderArn: 

      This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the address in the "From" header of the bounce. For more information about sending authorization, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html>`__ .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'MessageId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a unique message ID.

        
        

        - **MessageId** *(string) --* 

          The message ID of the bounce message.

          
    

  .. py:method:: send_bulk_templated_email(**kwargs)

    

    Composes an email message to multiple destinations. The message body is created using an email template.

     

    In order to send email using the ``SendBulkTemplatedEmail`` operation, your call to the API must meet the following requirements:

     

     
    * The call must refer to an existing email template. You can create email templates using the  CreateTemplate operation. 
     
    * The message must be sent from a verified email address or domain. 
     
    * If your account is still in the Amazon SES sandbox, you may only send to verified addresses or domains, or to email addresses associated with the Amazon SES Mailbox Simulator. For more information, see `Verifying Email Addresses and Domains <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html>`__ in the *Amazon SES Developer Guide.*   
     
    * The total size of the message, including attachments, must be less than 10 MB. 
     
    * Each ``Destination`` parameter must include at least one recipient email address. The recipient address can be a To: address, a CC: address, or a BCC: address. If a recipient email address is invalid (that is, it is not in the format *UserName@[SubDomain.]Domain.TopLevelDomain* ), the entire message will be rejected, even if the message contains other recipients that are valid. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/SendBulkTemplatedEmail>`_    


    **Request Syntax** 
    ::

      response = client.send_bulk_templated_email(
          Source='string',
          SourceArn='string',
          ReplyToAddresses=[
              'string',
          ],
          ReturnPath='string',
          ReturnPathArn='string',
          ConfigurationSetName='string',
          DefaultTags=[
              {
                  'Name': 'string',
                  'Value': 'string'
              },
          ],
          Template='string',
          TemplateArn='string',
          DefaultTemplateData='string',
          Destinations=[
              {
                  'Destination': {
                      'ToAddresses': [
                          'string',
                      ],
                      'CcAddresses': [
                          'string',
                      ],
                      'BccAddresses': [
                          'string',
                      ]
                  },
                  'ReplacementTags': [
                      {
                          'Name': 'string',
                          'Value': 'string'
                      },
                  ],
                  'ReplacementTemplateData': 'string'
              },
          ]
      )
    :type Source: string
    :param Source: **[REQUIRED]** 

      The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html>`__ .

       

      If you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the ``SourceArn`` parameter. For more information about sending authorization, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html>`__ .

       

      .. note::

         

        Amazon SES does not support the SMTPUTF8 extension, as described in `RFC6531 <https://tools.ietf.org/html/rfc6531>`__ . For this reason, the *local part* of a source email address (the part of the email address that precedes the @ sign) may only contain `7-bit ASCII characters <https://en.wikipedia.org/wiki/Email_address#Local-part>`__ . If the *domain part* of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in `RFC3492 <https://tools.ietf.org/html/rfc3492.html>`__ . The sender name (also known as the *friendly name* ) may contain non-ASCII characters. These characters must be encoded using MIME encoded-word syntax, as described in `RFC 2047 <https://tools.ietf.org/html/rfc2047>`__ . MIME encoded-word syntax uses the following form: ``=?charset?encoding?encoded-text?=`` .

         

      

    
    :type SourceArn: string
    :param SourceArn: 

      This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the ``Source`` parameter.

       

      For example, if the owner of ``example.com`` (which has ARN ``arn:aws:ses:us-east-1:123456789012:identity/example.com`` ) attaches a policy to it that authorizes you to send from ``user@example.com`` , then you would specify the ``SourceArn`` to be ``arn:aws:ses:us-east-1:123456789012:identity/example.com`` , and the ``Source`` to be ``user@example.com`` .

       

      For more information about sending authorization, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html>`__ .

      

    
    :type ReplyToAddresses: list
    :param ReplyToAddresses: 

      The reply-to email address(es) for the message. If the recipient replies to the message, each reply-to address will receive the reply.

      

    
      - *(string) --* 

      
  
    :type ReturnPath: string
    :param ReturnPath: 

      The email address that bounces and complaints will be forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message will be returned from the recipient's ISP; this message will then be forwarded to the email address specified by the ``ReturnPath`` parameter. The ``ReturnPath`` parameter is never overwritten. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. 

      

    
    :type ReturnPathArn: string
    :param ReturnPathArn: 

      This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the ``ReturnPath`` parameter.

       

      For example, if the owner of ``example.com`` (which has ARN ``arn:aws:ses:us-east-1:123456789012:identity/example.com`` ) attaches a policy to it that authorizes you to use ``feedback@example.com`` , then you would specify the ``ReturnPathArn`` to be ``arn:aws:ses:us-east-1:123456789012:identity/example.com`` , and the ``ReturnPath`` to be ``feedback@example.com`` .

       

      For more information about sending authorization, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html>`__ .

      

    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: 

      The name of the configuration set to use when you send an email using ``SendBulkTemplatedEmail`` .

      

    
    :type DefaultTags: list
    :param DefaultTags: 

      A list of tags, in the form of name/value pairs, to apply to an email that you send to a destination using ``SendBulkTemplatedEmail`` .

      

    
      - *(dict) --* 

        Contains the name and value of a tag that you can provide to ``SendEmail`` or ``SendRawEmail`` to apply to an email.

         

        Message tags, which you use with configuration sets, enable you to publish email sending events. For information about using configuration sets, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

        

      
        - **Name** *(string) --* **[REQUIRED]** 

          The name of the tag. The name must:

           

           
          * Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
           
          * Contain less than 256 characters. 
           

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          The value of the tag. The value must:

           

           
          * Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
           
          * Contain less than 256 characters. 
           

          

        
      
  
    :type Template: string
    :param Template: **[REQUIRED]** 

      The template to use when sending this email.

      

    
    :type TemplateArn: string
    :param TemplateArn: 

      The ARN of the template to use when sending this email.

      

    
    :type DefaultTemplateData: string
    :param DefaultTemplateData: 

      A list of replacement values to apply to the template when replacement data is not specified in a Destination object. These values act as a default or fallback option when no other data is available.

       

      The template data is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.

      

    
    :type Destinations: list
    :param Destinations: **[REQUIRED]** 

      One or more ``Destination`` objects. All of the recipients in a ``Destination`` will receive the same version of the email. You can specify up to 50 ``Destination`` objects within a ``Destinations`` array.

      

    
      - *(dict) --* 

        An array that contains one or more Destinations, as well as the tags and replacement data associated with each of those Destinations.

        

      
        - **Destination** *(dict) --* **[REQUIRED]** 

          Represents the destination of the message, consisting of To:, CC:, and BCC: fields.

           

          .. note::

             

            Amazon SES does not support the SMTPUTF8 extension, as described in `RFC6531 <https://tools.ietf.org/html/rfc6531>`__ . For this reason, the *local part* of a destination email address (the part of the email address that precedes the @ sign) may only contain `7-bit ASCII characters <https://en.wikipedia.org/wiki/Email_address#Local-part>`__ . If the *domain part* of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in `RFC3492 <https://tools.ietf.org/html/rfc3492.html>`__ .

             

          

        
          - **ToAddresses** *(list) --* 

            The To: field(s) of the message.

            

          
            - *(string) --* 

            
        
          - **CcAddresses** *(list) --* 

            The CC: field(s) of the message.

            

          
            - *(string) --* 

            
        
          - **BccAddresses** *(list) --* 

            The BCC: field(s) of the message.

            

          
            - *(string) --* 

            
        
        
        - **ReplacementTags** *(list) --* 

          A list of tags, in the form of name/value pairs, to apply to an email that you send using ``SendBulkTemplatedEmail`` . Tags correspond to characteristics of the email that you define, so that you can publish email sending events.

          

        
          - *(dict) --* 

            Contains the name and value of a tag that you can provide to ``SendEmail`` or ``SendRawEmail`` to apply to an email.

             

            Message tags, which you use with configuration sets, enable you to publish email sending events. For information about using configuration sets, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

            

          
            - **Name** *(string) --* **[REQUIRED]** 

              The name of the tag. The name must:

               

               
              * Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
               
              * Contain less than 256 characters. 
               

              

            
            - **Value** *(string) --* **[REQUIRED]** 

              The value of the tag. The value must:

               

               
              * Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
               
              * Contain less than 256 characters. 
               

              

            
          
      
        - **ReplacementTemplateData** *(string) --* 

          A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Status': [
                {
                    'Status': 'Success'|'MessageRejected'|'MailFromDomainNotVerified'|'ConfigurationSetDoesNotExist'|'TemplateDoesNotExist'|'AccountSuspended'|'AccountThrottled'|'AccountDailyQuotaExceeded'|'InvalidSendingPoolName'|'AccountSendingPaused'|'ConfigurationSetSendingPaused'|'InvalidParameterValue'|'TransientFailure'|'Failed',
                    'Error': 'string',
                    'MessageId': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Status** *(list) --* 

          The unique message identifier returned from the ``SendBulkTemplatedEmail`` action.

          
          

          - *(dict) --* 

            An object that contains the response from the ``SendBulkTemplatedEmail`` operation.

            
            

            - **Status** *(string) --* 

              The status of a message sent using the ``SendBulkTemplatedEmail`` operation.

               

              Possible values for this parameter include:

               

               
              * ``Success`` : Amazon SES accepted the message, and will attempt to deliver it to the recipients. 
               
              * ``MessageRejected`` : The message was rejected because it contained a virus. 
               
              * ``MailFromDomainNotVerified`` : The sender's email address or domain was not verified. 
               
              * ``ConfigurationSetDoesNotExist`` : The configuration set you specified does not exist. 
               
              * ``TemplateDoesNotExist`` : The template you specified does not exist. 
               
              * ``AccountSuspended`` : Your account has been shut down because of issues related to your email sending practices. 
               
              * ``AccountThrottled`` : The number of emails you can send has been reduced because your account has exceeded its allocated sending limit. 
               
              * ``AccountDailyQuotaExceeded`` : You have reached or exceeded the maximum number of emails you can send from your account in a 24-hour period. 
               
              * ``InvalidSendingPoolName`` : The configuration set you specified refers to an IP pool that does not exist. 
               
              * ``AccountSendingPaused`` : Email sending for the Amazon SES account was disabled using the  UpdateAccountSendingEnabled operation. 
               
              * ``ConfigurationSetSendingPaused`` : Email sending for this configuration set was disabled using the  UpdateConfigurationSetSendingEnabled operation. 
               
              * ``InvalidParameterValue`` : One or more of the parameters you specified when calling this operation was invalid. See the error message for additional information. 
               
              * ``TransientFailure`` : Amazon SES was unable to process your request because of a temporary issue. 
               
              * ``Failed`` : Amazon SES was unable to process your request. See the error message for additional information. 
               

              
            

            - **Error** *(string) --* 

              A description of an error that prevented a message being sent using the ``SendBulkTemplatedEmail`` operation.

              
            

            - **MessageId** *(string) --* 

              The unique message identifier returned from the ``SendBulkTemplatedEmail`` operation.

              
        
      
    

  .. py:method:: send_custom_verification_email(**kwargs)

    

    Sends a custom verification email to a specified recipient. Verification emails sent using this operation are counted against your 24-hour sending quota and per-second sending rate.

     

    For more information about custom verification email templates, see `Using Custom Verification Email Templates <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-verification-emails.html>`__ in the *Amazon SES Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/SendCustomVerificationEmail>`_    


    **Request Syntax** 
    ::

      response = client.send_custom_verification_email(
          EmailAddress='string',
          TemplateName='string',
          ConfigurationSetName='string'
      )
    :type EmailAddress: string
    :param EmailAddress: **[REQUIRED]** 

      The email address to verify.

      

    
    :type TemplateName: string
    :param TemplateName: **[REQUIRED]** 

      The name of the custom verification email template to use when sending the verification email.

      

    
    :type ConfigurationSetName: string
    :param ConfigurationSetName: 

      Name of a configuration set to use when sending the verification email.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'MessageId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The response received when attempting to send the custom verification email.

        
        

        - **MessageId** *(string) --* 

          The unique message identifier returned from the ``SendCustomVerificationEmail`` operation.

          
    

  .. py:method:: send_email(**kwargs)

    

    Composes an email message and immediately queues it for sending. In order to send email using the ``SendEmail`` operation, your message must meet the following requirements:

     

     
    * The message must be sent from a verified email address or domain. If you attempt to send email using a non-verified address or domain, the operation will result in an "Email address not verified" error.  
     
    * If your account is still in the Amazon SES sandbox, you may only send to verified addresses or domains, or to email addresses associated with the Amazon SES Mailbox Simulator. For more information, see `Verifying Email Addresses and Domains <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html>`__ in the *Amazon SES Developer Guide.*   
     
    * The total size of the message, including attachments, must be smaller than 10 MB. 
     
    * The message must include at least one recipient email address. The recipient address can be a To: address, a CC: address, or a BCC: address. If a recipient email address is invalid (that is, it is not in the format *UserName@[SubDomain.]Domain.TopLevelDomain* ), the entire message will be rejected, even if the message contains other recipients that are valid. 
     
    * The message may not include more than 50 recipients, across the To:, CC: and BCC: fields. If you need to send an email message to a larger audience, you can divide your recipient list into groups of 50 or fewer, and then call the ``SendEmail`` operation several times to send the message to each group. 
     

     

    .. warning::

       

      For every message that you send, the total number of recipients (including each recipient in the To:, CC: and BCC: fields) is counted against the maximum number of emails you can send in a 24-hour period (your *sending quota* ). For more information about sending quotas in Amazon SES, see `Managing Your Amazon SES Sending Limits <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/manage-sending-limits.html>`__ in the *Amazon SES Developer Guide.*  

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/SendEmail>`_    


    **Request Syntax** 
    ::

      response = client.send_email(
          Source='string',
          Destination={
              'ToAddresses': [
                  'string',
              ],
              'CcAddresses': [
                  'string',
              ],
              'BccAddresses': [
                  'string',
              ]
          },
          Message={
              'Subject': {
                  'Data': 'string',
                  'Charset': 'string'
              },
              'Body': {
                  'Text': {
                      'Data': 'string',
                      'Charset': 'string'
                  },
                  'Html': {
                      'Data': 'string',
                      'Charset': 'string'
                  }
              }
          },
          ReplyToAddresses=[
              'string',
          ],
          ReturnPath='string',
          SourceArn='string',
          ReturnPathArn='string',
          Tags=[
              {
                  'Name': 'string',
                  'Value': 'string'
              },
          ],
          ConfigurationSetName='string'
      )
    :type Source: string
    :param Source: **[REQUIRED]** 

      The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html>`__ .

       

      If you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the ``SourceArn`` parameter. For more information about sending authorization, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html>`__ .

       

      .. note::

         

        Amazon SES does not support the SMTPUTF8 extension, as described in `RFC6531 <https://tools.ietf.org/html/rfc6531>`__ . For this reason, the *local part* of a source email address (the part of the email address that precedes the @ sign) may only contain `7-bit ASCII characters <https://en.wikipedia.org/wiki/Email_address#Local-part>`__ . If the *domain part* of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in `RFC3492 <https://tools.ietf.org/html/rfc3492.html>`__ . The sender name (also known as the *friendly name* ) may contain non-ASCII characters. These characters must be encoded using MIME encoded-word syntax, as described in `RFC 2047 <https://tools.ietf.org/html/rfc2047>`__ . MIME encoded-word syntax uses the following form: ``=?charset?encoding?encoded-text?=`` .

         

      

    
    :type Destination: dict
    :param Destination: **[REQUIRED]** 

      The destination for this email, composed of To:, CC:, and BCC: fields.

      

    
      - **ToAddresses** *(list) --* 

        The To: field(s) of the message.

        

      
        - *(string) --* 

        
    
      - **CcAddresses** *(list) --* 

        The CC: field(s) of the message.

        

      
        - *(string) --* 

        
    
      - **BccAddresses** *(list) --* 

        The BCC: field(s) of the message.

        

      
        - *(string) --* 

        
    
    
    :type Message: dict
    :param Message: **[REQUIRED]** 

      The message to be sent.

      

    
      - **Subject** *(dict) --* **[REQUIRED]** 

        The subject of the message: A short summary of the content, which will appear in the recipient's inbox.

        

      
        - **Data** *(string) --* **[REQUIRED]** 

          The textual data of the content.

          

        
        - **Charset** *(string) --* 

          The character set of the content.

          

        
      
      - **Body** *(dict) --* **[REQUIRED]** 

        The message body.

        

      
        - **Text** *(dict) --* 

          The content of the message, in text format. Use this for text-based email clients, or clients on high-latency networks (such as mobile devices).

          

        
          - **Data** *(string) --* **[REQUIRED]** 

            The textual data of the content.

            

          
          - **Charset** *(string) --* 

            The character set of the content.

            

          
        
        - **Html** *(dict) --* 

          The content of the message, in HTML format. Use this for email clients that can process HTML. You can include clickable links, formatted text, and much more in an HTML message.

          

        
          - **Data** *(string) --* **[REQUIRED]** 

            The textual data of the content.

            

          
          - **Charset** *(string) --* 

            The character set of the content.

            

          
        
      
    
    :type ReplyToAddresses: list
    :param ReplyToAddresses: 

      The reply-to email address(es) for the message. If the recipient replies to the message, each reply-to address will receive the reply.

      

    
      - *(string) --* 

      
  
    :type ReturnPath: string
    :param ReturnPath: 

      The email address that bounces and complaints will be forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message will be returned from the recipient's ISP; this message will then be forwarded to the email address specified by the ``ReturnPath`` parameter. The ``ReturnPath`` parameter is never overwritten. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. 

      

    
    :type SourceArn: string
    :param SourceArn: 

      This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the ``Source`` parameter.

       

      For example, if the owner of ``example.com`` (which has ARN ``arn:aws:ses:us-east-1:123456789012:identity/example.com`` ) attaches a policy to it that authorizes you to send from ``user@example.com`` , then you would specify the ``SourceArn`` to be ``arn:aws:ses:us-east-1:123456789012:identity/example.com`` , and the ``Source`` to be ``user@example.com`` .

       

      For more information about sending authorization, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html>`__ .

      

    
    :type ReturnPathArn: string
    :param ReturnPathArn: 

      This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the ``ReturnPath`` parameter.

       

      For example, if the owner of ``example.com`` (which has ARN ``arn:aws:ses:us-east-1:123456789012:identity/example.com`` ) attaches a policy to it that authorizes you to use ``feedback@example.com`` , then you would specify the ``ReturnPathArn`` to be ``arn:aws:ses:us-east-1:123456789012:identity/example.com`` , and the ``ReturnPath`` to be ``feedback@example.com`` .

       

      For more information about sending authorization, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html>`__ .

      

    
    :type Tags: list
    :param Tags: 

      A list of tags, in the form of name/value pairs, to apply to an email that you send using ``SendEmail`` . Tags correspond to characteristics of the email that you define, so that you can publish email sending events.

      

    
      - *(dict) --* 

        Contains the name and value of a tag that you can provide to ``SendEmail`` or ``SendRawEmail`` to apply to an email.

         

        Message tags, which you use with configuration sets, enable you to publish email sending events. For information about using configuration sets, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

        

      
        - **Name** *(string) --* **[REQUIRED]** 

          The name of the tag. The name must:

           

           
          * Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
           
          * Contain less than 256 characters. 
           

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          The value of the tag. The value must:

           

           
          * Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
           
          * Contain less than 256 characters. 
           

          

        
      
  
    :type ConfigurationSetName: string
    :param ConfigurationSetName: 

      The name of the configuration set to use when you send an email using ``SendEmail`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'MessageId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a unique message ID.

        
        

        - **MessageId** *(string) --* 

          The unique message identifier returned from the ``SendEmail`` action. 

          
    

    **Examples** 

    The following example sends a formatted email:
    ::

      response = client.send_email(
          Destination={
              'BccAddresses': [
              ],
              'CcAddresses': [
                  'recipient3@example.com',
              ],
              'ToAddresses': [
                  'recipient1@example.com',
                  'recipient2@example.com',
              ],
          },
          Message={
              'Body': {
                  'Html': {
                      'Charset': 'UTF-8',
                      'Data': 'This message body contains HTML formatting. It can, for example, contain links like this one: <a class="ulink" href="http://docs.aws.amazon.com/ses/latest/DeveloperGuide" target="_blank">Amazon SES Developer Guide</a>.',
                  },
                  'Text': {
                      'Charset': 'UTF-8',
                      'Data': 'This is the message body in text format.',
                  },
              },
              'Subject': {
                  'Charset': 'UTF-8',
                  'Data': 'Test email',
              },
          },
          ReplyToAddresses=[
          ],
          ReturnPath='',
          ReturnPathArn='',
          Source='sender@example.com',
          SourceArn='',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'MessageId': 'EXAMPLE78603177f-7a5433e7-8edb-42ae-af10-f0181f34d6ee-000000',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: send_raw_email(**kwargs)

    

    Composes an email message and immediately queues it for sending. When calling this operation, you may specify the message headers as well as the content. The ``SendRawEmail`` operation is particularly useful for sending multipart MIME emails (such as those that contain both a plain-text and an HTML version). 

     

    In order to send email using the ``SendRawEmail`` operation, your message must meet the following requirements:

     

     
    * The message must be sent from a verified email address or domain. If you attempt to send email using a non-verified address or domain, the operation will result in an "Email address not verified" error.  
     
    * If your account is still in the Amazon SES sandbox, you may only send to verified addresses or domains, or to email addresses associated with the Amazon SES Mailbox Simulator. For more information, see `Verifying Email Addresses and Domains <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html>`__ in the *Amazon SES Developer Guide.*   
     
    * The total size of the message, including attachments, must be smaller than 10 MB. 
     
    * The message must include at least one recipient email address. The recipient address can be a To: address, a CC: address, or a BCC: address. If a recipient email address is invalid (that is, it is not in the format *UserName@[SubDomain.]Domain.TopLevelDomain* ), the entire message will be rejected, even if the message contains other recipients that are valid. 
     
    * The message may not include more than 50 recipients, across the To:, CC: and BCC: fields. If you need to send an email message to a larger audience, you can divide your recipient list into groups of 50 or fewer, and then call the ``SendRawEmail`` operation several times to send the message to each group. 
     

     

    .. warning::

       

      For every message that you send, the total number of recipients (including each recipient in the To:, CC: and BCC: fields) is counted against the maximum number of emails you can send in a 24-hour period (your *sending quota* ). For more information about sending quotas in Amazon SES, see `Managing Your Amazon SES Sending Limits <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/manage-sending-limits.html>`__ in the *Amazon SES Developer Guide.*  

       

     

    Additionally, keep the following considerations in mind when using the ``SendRawEmail`` operation:

     

     
    * Although you can customize the message headers when using the ``SendRawEmail`` operation, Amazon SES will automatically apply its own ``Message-ID`` and ``Date`` headers; if you passed these headers when creating the message, they will be overwritten by the values that Amazon SES provides. 
     
    * If you are using sending authorization to send on behalf of another user, ``SendRawEmail`` enables you to specify the cross-account identity for the email's Source, From, and Return-Path parameters in one of two ways: you can pass optional parameters ``SourceArn`` , ``FromArn`` , and/or ``ReturnPathArn`` to the API, or you can include the following X-headers in the header of your raw email: 

       
      * ``X-SES-SOURCE-ARN``   
       
      * ``X-SES-FROM-ARN``   
       
      * ``X-SES-RETURN-PATH-ARN``   
       

     

    .. warning::

       

      Do not include these X-headers in the DKIM signature; Amazon SES will remove them before sending the email.

       

     

    For most common sending authorization scenarios, we recommend that you specify the ``SourceIdentityArn`` parameter and not the ``FromIdentityArn`` or ``ReturnPathIdentityArn`` parameters. If you only specify the ``SourceIdentityArn`` parameter, Amazon SES will set the From and Return Path addresses to the identity specified in ``SourceIdentityArn`` . For more information about sending authorization, see the `Using Sending Authorization with Amazon SES <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html>`__ in the *Amazon SES Developer Guide.*  

     
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/SendRawEmail>`_    


    **Request Syntax** 
    ::

      response = client.send_raw_email(
          Source='string',
          Destinations=[
              'string',
          ],
          RawMessage={
              'Data': b'bytes'
          },
          FromArn='string',
          SourceArn='string',
          ReturnPathArn='string',
          Tags=[
              {
                  'Name': 'string',
                  'Value': 'string'
              },
          ],
          ConfigurationSetName='string'
      )
    :type Source: string
    :param Source: 

      The identity's email address. If you do not provide a value for this parameter, you must specify a "From" address in the raw text of the message. (You can also specify both.)

       

      .. note::

         

        Amazon SES does not support the SMTPUTF8 extension, as described in`RFC6531 <https://tools.ietf.org/html/rfc6531>`__ . For this reason, the *local part* of a source email address (the part of the email address that precedes the @ sign) may only contain `7-bit ASCII characters <https://en.wikipedia.org/wiki/Email_address#Local-part>`__ . If the *domain part* of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in `RFC3492 <https://tools.ietf.org/html/rfc3492.html>`__ . The sender name (also known as the *friendly name* ) may contain non-ASCII characters. These characters must be encoded using MIME encoded-word syntax, as described in `RFC 2047 <https://tools.ietf.org/html/rfc2047>`__ . MIME encoded-word syntax uses the following form: ``=?charset?encoding?encoded-text?=`` .

         

       

      If you specify the ``Source`` parameter and have feedback forwarding enabled, then bounces and complaints will be sent to this email address. This takes precedence over any Return-Path header that you might include in the raw text of the message.

      

    
    :type Destinations: list
    :param Destinations: 

      A list of destinations for the message, consisting of To:, CC:, and BCC: addresses.

      

    
      - *(string) --* 

      
  
    :type RawMessage: dict
    :param RawMessage: **[REQUIRED]** 

      The raw text of the message. The client is responsible for ensuring the following:

       

       
      * Message must contain a header and a body, separated by a blank line. 
       
      * All required header fields must be present. 
       
      * Each part of a multipart MIME message must be formatted properly. 
       
      * MIME content types must be among those supported by Amazon SES. For more information, go to the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/mime-types.html>`__ . 
       
      * Must be base64-encoded. 
       
      * Per `RFC 5321 <https://tools.ietf.org/html/rfc5321#section-4.5.3.1.6>`__ , the maximum length of each line of text, including the <CRLF>, must not exceed 1,000 characters. 
       

      

    
      - **Data** *(bytes) --* **[REQUIRED]** 

        The raw data of the message. This data needs to base64-encoded if you are accessing Amazon SES directly through the HTTPS interface. If you are accessing Amazon SES using an AWS SDK, the SDK takes care of the base 64-encoding for you. In all cases, the client must ensure that the message format complies with Internet email standards regarding email header fields, MIME types, and MIME encoding.

         

        The To:, CC:, and BCC: headers in the raw message can contain a group list.

         

        If you are using ``SendRawEmail`` with sending authorization, you can include X-headers in the raw message to specify the "Source," "From," and "Return-Path" addresses. For more information, see the documentation for ``SendRawEmail`` . 

         

        .. warning::

           

          Do not include these X-headers in the DKIM signature, because they are removed by Amazon SES before sending the email.

           

         

        For more information, go to the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-raw.html>`__ .

        

      
    
    :type FromArn: string
    :param FromArn: 

      This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to specify a particular "From" address in the header of the raw email.

       

      Instead of using this parameter, you can use the X-header ``X-SES-FROM-ARN`` in the raw message of the email. If you use both the ``FromArn`` parameter and the corresponding X-header, Amazon SES uses the value of the ``FromArn`` parameter.

       

      .. note::

         

        For information about when to use this parameter, see the description of ``SendRawEmail`` in this guide, or see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization-delegate-sender-tasks-email.html>`__ .

         

      

    
    :type SourceArn: string
    :param SourceArn: 

      This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the ``Source`` parameter.

       

      For example, if the owner of ``example.com`` (which has ARN ``arn:aws:ses:us-east-1:123456789012:identity/example.com`` ) attaches a policy to it that authorizes you to send from ``user@example.com`` , then you would specify the ``SourceArn`` to be ``arn:aws:ses:us-east-1:123456789012:identity/example.com`` , and the ``Source`` to be ``user@example.com`` .

       

      Instead of using this parameter, you can use the X-header ``X-SES-SOURCE-ARN`` in the raw message of the email. If you use both the ``SourceArn`` parameter and the corresponding X-header, Amazon SES uses the value of the ``SourceArn`` parameter.

       

      .. note::

         

        For information about when to use this parameter, see the description of ``SendRawEmail`` in this guide, or see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization-delegate-sender-tasks-email.html>`__ .

         

      

    
    :type ReturnPathArn: string
    :param ReturnPathArn: 

      This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the ``ReturnPath`` parameter.

       

      For example, if the owner of ``example.com`` (which has ARN ``arn:aws:ses:us-east-1:123456789012:identity/example.com`` ) attaches a policy to it that authorizes you to use ``feedback@example.com`` , then you would specify the ``ReturnPathArn`` to be ``arn:aws:ses:us-east-1:123456789012:identity/example.com`` , and the ``ReturnPath`` to be ``feedback@example.com`` .

       

      Instead of using this parameter, you can use the X-header ``X-SES-RETURN-PATH-ARN`` in the raw message of the email. If you use both the ``ReturnPathArn`` parameter and the corresponding X-header, Amazon SES uses the value of the ``ReturnPathArn`` parameter.

       

      .. note::

         

        For information about when to use this parameter, see the description of ``SendRawEmail`` in this guide, or see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization-delegate-sender-tasks-email.html>`__ .

         

      

    
    :type Tags: list
    :param Tags: 

      A list of tags, in the form of name/value pairs, to apply to an email that you send using ``SendRawEmail`` . Tags correspond to characteristics of the email that you define, so that you can publish email sending events.

      

    
      - *(dict) --* 

        Contains the name and value of a tag that you can provide to ``SendEmail`` or ``SendRawEmail`` to apply to an email.

         

        Message tags, which you use with configuration sets, enable you to publish email sending events. For information about using configuration sets, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

        

      
        - **Name** *(string) --* **[REQUIRED]** 

          The name of the tag. The name must:

           

           
          * Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
           
          * Contain less than 256 characters. 
           

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          The value of the tag. The value must:

           

           
          * Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
           
          * Contain less than 256 characters. 
           

          

        
      
  
    :type ConfigurationSetName: string
    :param ConfigurationSetName: 

      The name of the configuration set to use when you send an email using ``SendRawEmail`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'MessageId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Represents a unique message ID.

        
        

        - **MessageId** *(string) --* 

          The unique message identifier returned from the ``SendRawEmail`` action. 

          
    

    **Examples** 

    The following example sends an email with an attachment:
    ::

      response = client.send_raw_email(
          Destinations=[
          ],
          FromArn='',
          RawMessage={
              'Data': 'From: sender@example.com\nTo: recipient@example.com\nSubject: Test email (contains an attachment)\nMIME-Version: 1.0\nContent-type: Multipart/Mixed; boundary="NextPart"\n\n--NextPart\nContent-Type: text/plain\n\nThis is the message body.\n\n--NextPart\nContent-Type: text/plain;\nContent-Disposition: attachment; filename="attachment.txt"\n\nThis is the text in the attachment.\n\n--NextPart--',
          },
          ReturnPathArn='',
          Source='',
          SourceArn='',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'MessageId': 'EXAMPLEf3f73d99b-c63fb06f-d263-41f8-a0fb-d0dc67d56c07-000000',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: send_templated_email(**kwargs)

    

    Composes an email message using an email template and immediately queues it for sending.

     

    In order to send email using the ``SendTemplatedEmail`` operation, your call to the API must meet the following requirements:

     

     
    * The call must refer to an existing email template. You can create email templates using the  CreateTemplate operation. 
     
    * The message must be sent from a verified email address or domain. 
     
    * If your account is still in the Amazon SES sandbox, you may only send to verified addresses or domains, or to email addresses associated with the Amazon SES Mailbox Simulator. For more information, see `Verifying Email Addresses and Domains <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html>`__ in the *Amazon SES Developer Guide.*   
     
    * The total size of the message, including attachments, must be less than 10 MB. 
     
    * Calls to the ``SendTemplatedEmail`` operation may only include one ``Destination`` parameter. A destination is a set of recipients who will receive the same version of the email. The ``Destination`` parameter can include up to 50 recipients, across the To:, CC: and BCC: fields. 
     
    * The ``Destination`` parameter must include at least one recipient email address. The recipient address can be a To: address, a CC: address, or a BCC: address. If a recipient email address is invalid (that is, it is not in the format *UserName@[SubDomain.]Domain.TopLevelDomain* ), the entire message will be rejected, even if the message contains other recipients that are valid. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/SendTemplatedEmail>`_    


    **Request Syntax** 
    ::

      response = client.send_templated_email(
          Source='string',
          Destination={
              'ToAddresses': [
                  'string',
              ],
              'CcAddresses': [
                  'string',
              ],
              'BccAddresses': [
                  'string',
              ]
          },
          ReplyToAddresses=[
              'string',
          ],
          ReturnPath='string',
          SourceArn='string',
          ReturnPathArn='string',
          Tags=[
              {
                  'Name': 'string',
                  'Value': 'string'
              },
          ],
          ConfigurationSetName='string',
          Template='string',
          TemplateArn='string',
          TemplateData='string'
      )
    :type Source: string
    :param Source: **[REQUIRED]** 

      The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html>`__ .

       

      If you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the ``SourceArn`` parameter. For more information about sending authorization, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html>`__ .

       

      .. note::

         

        Amazon SES does not support the SMTPUTF8 extension, as described in `RFC6531 <https://tools.ietf.org/html/rfc6531>`__ . For this reason, the *local part* of a source email address (the part of the email address that precedes the @ sign) may only contain `7-bit ASCII characters <https://en.wikipedia.org/wiki/Email_address#Local-part>`__ . If the *domain part* of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in `RFC3492 <https://tools.ietf.org/html/rfc3492.html>`__ . The sender name (also known as the *friendly name* ) may contain non-ASCII characters. These characters must be encoded using MIME encoded-word syntax, as described in`RFC 2047 <https://tools.ietf.org/html/rfc2047>`__ . MIME encoded-word syntax uses the following form: ``=?charset?encoding?encoded-text?=`` .

         

      

    
    :type Destination: dict
    :param Destination: **[REQUIRED]** 

      The destination for this email, composed of To:, CC:, and BCC: fields. A Destination can include up to 50 recipients across these three fields.

      

    
      - **ToAddresses** *(list) --* 

        The To: field(s) of the message.

        

      
        - *(string) --* 

        
    
      - **CcAddresses** *(list) --* 

        The CC: field(s) of the message.

        

      
        - *(string) --* 

        
    
      - **BccAddresses** *(list) --* 

        The BCC: field(s) of the message.

        

      
        - *(string) --* 

        
    
    
    :type ReplyToAddresses: list
    :param ReplyToAddresses: 

      The reply-to email address(es) for the message. If the recipient replies to the message, each reply-to address will receive the reply.

      

    
      - *(string) --* 

      
  
    :type ReturnPath: string
    :param ReturnPath: 

      The email address that bounces and complaints will be forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message will be returned from the recipient's ISP; this message will then be forwarded to the email address specified by the ``ReturnPath`` parameter. The ``ReturnPath`` parameter is never overwritten. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. 

      

    
    :type SourceArn: string
    :param SourceArn: 

      This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the ``Source`` parameter.

       

      For example, if the owner of ``example.com`` (which has ARN ``arn:aws:ses:us-east-1:123456789012:identity/example.com`` ) attaches a policy to it that authorizes you to send from ``user@example.com`` , then you would specify the ``SourceArn`` to be ``arn:aws:ses:us-east-1:123456789012:identity/example.com`` , and the ``Source`` to be ``user@example.com`` .

       

      For more information about sending authorization, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html>`__ .

      

    
    :type ReturnPathArn: string
    :param ReturnPathArn: 

      This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the ``ReturnPath`` parameter.

       

      For example, if the owner of ``example.com`` (which has ARN ``arn:aws:ses:us-east-1:123456789012:identity/example.com`` ) attaches a policy to it that authorizes you to use ``feedback@example.com`` , then you would specify the ``ReturnPathArn`` to be ``arn:aws:ses:us-east-1:123456789012:identity/example.com`` , and the ``ReturnPath`` to be ``feedback@example.com`` .

       

      For more information about sending authorization, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html>`__ .

      

    
    :type Tags: list
    :param Tags: 

      A list of tags, in the form of name/value pairs, to apply to an email that you send using ``SendTemplatedEmail`` . Tags correspond to characteristics of the email that you define, so that you can publish email sending events.

      

    
      - *(dict) --* 

        Contains the name and value of a tag that you can provide to ``SendEmail`` or ``SendRawEmail`` to apply to an email.

         

        Message tags, which you use with configuration sets, enable you to publish email sending events. For information about using configuration sets, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

        

      
        - **Name** *(string) --* **[REQUIRED]** 

          The name of the tag. The name must:

           

           
          * Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
           
          * Contain less than 256 characters. 
           

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          The value of the tag. The value must:

           

           
          * Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
           
          * Contain less than 256 characters. 
           

          

        
      
  
    :type ConfigurationSetName: string
    :param ConfigurationSetName: 

      The name of the configuration set to use when you send an email using ``SendTemplatedEmail`` .

      

    
    :type Template: string
    :param Template: **[REQUIRED]** 

      The template to use when sending this email.

      

    
    :type TemplateArn: string
    :param TemplateArn: 

      The ARN of the template to use when sending this email.

      

    
    :type TemplateData: string
    :param TemplateData: **[REQUIRED]** 

      A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'MessageId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **MessageId** *(string) --* 

          The unique message identifier returned from the ``SendTemplatedEmail`` action. 

          
    

  .. py:method:: set_active_receipt_rule_set(**kwargs)

    

    Sets the specified receipt rule set as the active receipt rule set.

     

    .. note::

       

      To disable your email-receiving through Amazon SES completely, you can call this API with RuleSetName set to null.

       

     

    For information about managing receipt rule sets, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rule-sets.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/SetActiveReceiptRuleSet>`_    


    **Request Syntax** 
    ::

      response = client.set_active_receipt_rule_set(
          RuleSetName='string'
      )
    :type RuleSetName: string
    :param RuleSetName: 

      The name of the receipt rule set to make active. Setting this value to null disables all email receiving.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

    **Examples** 

    The following example sets the active receipt rule set:
    ::

      response = client.set_active_receipt_rule_set(
          RuleSetName='RuleSetToActivate',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: set_identity_dkim_enabled(**kwargs)

    

    Enables or disables Easy DKIM signing of email sent from an identity:

     

     
    * If Easy DKIM signing is enabled for a domain name identity (such as ``example.com`` ), then Amazon SES will DKIM-sign all email sent by addresses under that domain name (for example, ``user@example.com`` ). 
     
    * If Easy DKIM signing is enabled for an email address, then Amazon SES will DKIM-sign all email sent by that email address. 
     

     

    For email addresses (for example, ``user@example.com`` ), you can only enable Easy DKIM signing if the corresponding domain (in this case, ``example.com`` ) has been set up for Easy DKIM using the AWS Console or the ``VerifyDomainDkim`` operation.

     

    You can execute this operation no more than once per second.

     

    For more information about Easy DKIM signing, go to the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/SetIdentityDkimEnabled>`_    


    **Request Syntax** 
    ::

      response = client.set_identity_dkim_enabled(
          Identity='string',
          DkimEnabled=True|False
      )
    :type Identity: string
    :param Identity: **[REQUIRED]** 

      The identity for which DKIM signing should be enabled or disabled.

      

    
    :type DkimEnabled: boolean
    :param DkimEnabled: **[REQUIRED]** 

      Sets whether DKIM signing is enabled for an identity. Set to ``true`` to enable DKIM signing for this identity; ``false`` to disable it. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

    **Examples** 

    The following example configures Amazon SES to Easy DKIM-sign the email sent from an identity:
    ::

      response = client.set_identity_dkim_enabled(
          DkimEnabled=True,
          Identity='user@example.com',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: set_identity_feedback_forwarding_enabled(**kwargs)

    

    Given an identity (an email address or a domain), enables or disables whether Amazon SES forwards bounce and complaint notifications as email. Feedback forwarding can only be disabled when Amazon Simple Notification Service (Amazon SNS) topics are specified for both bounces and complaints.

     

    .. note::

       

      Feedback forwarding does not apply to delivery notifications. Delivery notifications are only available through Amazon SNS.

       

     

    You can execute this operation no more than once per second.

     

    For more information about using notifications with Amazon SES, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/notifications.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/SetIdentityFeedbackForwardingEnabled>`_    


    **Request Syntax** 
    ::

      response = client.set_identity_feedback_forwarding_enabled(
          Identity='string',
          ForwardingEnabled=True|False
      )
    :type Identity: string
    :param Identity: **[REQUIRED]** 

      The identity for which to set bounce and complaint notification forwarding. Examples: ``user@example.com`` , ``example.com`` .

      

    
    :type ForwardingEnabled: boolean
    :param ForwardingEnabled: **[REQUIRED]** 

      Sets whether Amazon SES will forward bounce and complaint notifications as email. ``true`` specifies that Amazon SES will forward bounce and complaint notifications as email, in addition to any Amazon SNS topic publishing otherwise specified. ``false`` specifies that Amazon SES will publish bounce and complaint notifications only through Amazon SNS. This value can only be set to ``false`` when Amazon SNS topics are set for both ``Bounce`` and ``Complaint`` notification types.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

    **Examples** 

    The following example configures Amazon SES to forward an identity's bounces and complaints via email:
    ::

      response = client.set_identity_feedback_forwarding_enabled(
          ForwardingEnabled=True,
          Identity='user@example.com',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: set_identity_headers_in_notifications_enabled(**kwargs)

    

    Given an identity (an email address or a domain), sets whether Amazon SES includes the original email headers in the Amazon Simple Notification Service (Amazon SNS) notifications of a specified type.

     

    You can execute this operation no more than once per second.

     

    For more information about using notifications with Amazon SES, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/notifications.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/SetIdentityHeadersInNotificationsEnabled>`_    


    **Request Syntax** 
    ::

      response = client.set_identity_headers_in_notifications_enabled(
          Identity='string',
          NotificationType='Bounce'|'Complaint'|'Delivery',
          Enabled=True|False
      )
    :type Identity: string
    :param Identity: **[REQUIRED]** 

      The identity for which to enable or disable headers in notifications. Examples: ``user@example.com`` , ``example.com`` .

      

    
    :type NotificationType: string
    :param NotificationType: **[REQUIRED]** 

      The notification type for which to enable or disable headers in notifications. 

      

    
    :type Enabled: boolean
    :param Enabled: **[REQUIRED]** 

      Sets whether Amazon SES includes the original email headers in Amazon SNS notifications of the specified notification type. A value of ``true`` specifies that Amazon SES will include headers in notifications, and a value of ``false`` specifies that Amazon SES will not include headers in notifications.

       

      This value can only be set when ``NotificationType`` is already set to use a particular Amazon SNS topic.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

    **Examples** 

    The following example configures Amazon SES to include the original email headers in the Amazon SNS bounce notifications for an identity:
    ::

      response = client.set_identity_headers_in_notifications_enabled(
          Enabled=True,
          Identity='user@example.com',
          NotificationType='Bounce',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: set_identity_mail_from_domain(**kwargs)

    

    Enables or disables the custom MAIL FROM domain setup for a verified identity (an email address or a domain).

     

    .. warning::

       

      To send emails using the specified MAIL FROM domain, you must add an MX record to your MAIL FROM domain's DNS settings. If you want your emails to pass Sender Policy Framework (SPF) checks, you must also add or update an SPF record. For more information, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/mail-from-set.html>`__ .

       

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/SetIdentityMailFromDomain>`_    


    **Request Syntax** 
    ::

      response = client.set_identity_mail_from_domain(
          Identity='string',
          MailFromDomain='string',
          BehaviorOnMXFailure='UseDefaultValue'|'RejectMessage'
      )
    :type Identity: string
    :param Identity: **[REQUIRED]** 

      The verified identity for which you want to enable or disable the specified custom MAIL FROM domain.

      

    
    :type MailFromDomain: string
    :param MailFromDomain: 

      The custom MAIL FROM domain that you want the verified identity to use. The MAIL FROM domain must 1) be a subdomain of the verified identity, 2) not be used in a "From" address if the MAIL FROM domain is the destination of email feedback forwarding (for more information, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/mail-from.html>`__ ), and 3) not be used to receive emails. A value of ``null`` disables the custom MAIL FROM setting for the identity.

      

    
    :type BehaviorOnMXFailure: string
    :param BehaviorOnMXFailure: 

      The action that you want Amazon SES to take if it cannot successfully read the required MX record when you send an email. If you choose ``UseDefaultValue`` , Amazon SES will use amazonses.com (or a subdomain of that) as the MAIL FROM domain. If you choose ``RejectMessage`` , Amazon SES will return a ``MailFromDomainNotVerified`` error and not send the email.

       

      The action specified in ``BehaviorOnMXFailure`` is taken when the custom MAIL FROM domain setup is in the ``Pending`` , ``Failed`` , and ``TemporaryFailure`` states.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

    **Examples** 

    The following example configures Amazon SES to use a custom MAIL FROM domain for an identity:
    ::

      response = client.set_identity_mail_from_domain(
          BehaviorOnMXFailure='UseDefaultValue',
          Identity='user@example.com',
          MailFromDomain='bounces.example.com',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: set_identity_notification_topic(**kwargs)

    

    Given an identity (an email address or a domain), sets the Amazon Simple Notification Service (Amazon SNS) topic to which Amazon SES will publish bounce, complaint, and/or delivery notifications for emails sent with that identity as the ``Source`` .

     

    .. note::

       

      Unless feedback forwarding is enabled, you must specify Amazon SNS topics for bounce and complaint notifications. For more information, see ``SetIdentityFeedbackForwardingEnabled`` .

       

     

    You can execute this operation no more than once per second.

     

    For more information about feedback notification, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/notifications.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/SetIdentityNotificationTopic>`_    


    **Request Syntax** 
    ::

      response = client.set_identity_notification_topic(
          Identity='string',
          NotificationType='Bounce'|'Complaint'|'Delivery',
          SnsTopic='string'
      )
    :type Identity: string
    :param Identity: **[REQUIRED]** 

      The identity for which the Amazon SNS topic will be set. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: ``user@example.com`` , ``example.com`` , ``arn:aws:ses:us-east-1:123456789012:identity/example.com`` .

      

    
    :type NotificationType: string
    :param NotificationType: **[REQUIRED]** 

      The type of notifications that will be published to the specified Amazon SNS topic.

      

    
    :type SnsTopic: string
    :param SnsTopic: 

      The Amazon Resource Name (ARN) of the Amazon SNS topic. If the parameter is omitted from the request or a null value is passed, ``SnsTopic`` is cleared and publishing is disabled.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

    **Examples** 

    The following example sets the Amazon SNS topic to which Amazon SES will publish bounce, complaint, and/or delivery notifications for emails sent with the specified identity as the Source:
    ::

      response = client.set_identity_notification_topic(
          Identity='user@example.com',
          NotificationType='Bounce',
          SnsTopic='arn:aws:sns:us-west-2:111122223333:MyTopic',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: set_receipt_rule_position(**kwargs)

    

    Sets the position of the specified receipt rule in the receipt rule set.

     

    For information about managing receipt rules, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rules.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/SetReceiptRulePosition>`_    


    **Request Syntax** 
    ::

      response = client.set_receipt_rule_position(
          RuleSetName='string',
          RuleName='string',
          After='string'
      )
    :type RuleSetName: string
    :param RuleSetName: **[REQUIRED]** 

      The name of the receipt rule set that contains the receipt rule to reposition.

      

    
    :type RuleName: string
    :param RuleName: **[REQUIRED]** 

      The name of the receipt rule to reposition.

      

    
    :type After: string
    :param After: 

      The name of the receipt rule after which to place the specified receipt rule.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

    **Examples** 

    The following example sets the position of a receipt rule in a receipt rule set:
    ::

      response = client.set_receipt_rule_position(
          After='PutRuleAfterThisRule',
          RuleName='RuleToReposition',
          RuleSetName='MyRuleSet',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: test_render_template(**kwargs)

    

    Creates a preview of the MIME content of an email when provided with a template and a set of replacement data.

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/TestRenderTemplate>`_    


    **Request Syntax** 
    ::

      response = client.test_render_template(
          TemplateName='string',
          TemplateData='string'
      )
    :type TemplateName: string
    :param TemplateName: **[REQUIRED]** 

      The name of the template that you want to render.

      

    
    :type TemplateData: string
    :param TemplateData: **[REQUIRED]** 

      A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'RenderedTemplate': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **RenderedTemplate** *(string) --* 

          The complete MIME message rendered by applying the data in the TemplateData parameter to the template specified in the TemplateName parameter.

          
    

  .. py:method:: update_account_sending_enabled(**kwargs)

    

    Enables or disables email sending across your entire Amazon SES account. You can use this operation in conjunction with Amazon CloudWatch alarms to temporarily pause email sending across your Amazon SES account when reputation metrics (such as your bounce on complaint rate) reach certain thresholds.

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/UpdateAccountSendingEnabled>`_    


    **Request Syntax** 
    ::

      response = client.update_account_sending_enabled(
          Enabled=True|False
      )
    :type Enabled: boolean
    :param Enabled: 

      Describes whether email sending is enabled or disabled for your Amazon SES account.

      

    
    
    :returns: None

  .. py:method:: update_configuration_set_event_destination(**kwargs)

    

    Updates the event destination of a configuration set. Event destinations are associated with configuration sets, which enable you to publish email sending events to Amazon CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS). For information about using configuration sets, see `Monitoring Your Amazon SES Sending Activity <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ in the *Amazon SES Developer Guide.*  

     

    .. note::

       

      When you create or update an event destination, you must provide one, and only one, destination. The destination can be Amazon CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS).

       

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/UpdateConfigurationSetEventDestination>`_    


    **Request Syntax** 
    ::

      response = client.update_configuration_set_event_destination(
          ConfigurationSetName='string',
          EventDestination={
              'Name': 'string',
              'Enabled': True|False,
              'MatchingEventTypes': [
                  'send'|'reject'|'bounce'|'complaint'|'delivery'|'open'|'click'|'renderingFailure',
              ],
              'KinesisFirehoseDestination': {
                  'IAMRoleARN': 'string',
                  'DeliveryStreamARN': 'string'
              },
              'CloudWatchDestination': {
                  'DimensionConfigurations': [
                      {
                          'DimensionName': 'string',
                          'DimensionValueSource': 'messageTag'|'emailHeader'|'linkTag',
                          'DefaultDimensionValue': 'string'
                      },
                  ]
              },
              'SNSDestination': {
                  'TopicARN': 'string'
              }
          }
      )
    :type ConfigurationSetName: string
    :param ConfigurationSetName: **[REQUIRED]** 

      The name of the configuration set that contains the event destination that you want to update.

      

    
    :type EventDestination: dict
    :param EventDestination: **[REQUIRED]** 

      The event destination object that you want to apply to the specified configuration set.

      

    
      - **Name** *(string) --* **[REQUIRED]** 

        The name of the event destination. The name must:

         

         
        * Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
         
        * Contain less than 64 characters. 
         

        

      
      - **Enabled** *(boolean) --* 

        Sets whether Amazon SES publishes events to this destination when you send an email with the associated configuration set. Set to ``true`` to enable publishing to this destination; set to ``false`` to prevent publishing to this destination. The default value is ``false`` .

        

      
      - **MatchingEventTypes** *(list) --* **[REQUIRED]** 

        The type of email sending events to publish to the event destination.

        

      
        - *(string) --* 

        
    
      - **KinesisFirehoseDestination** *(dict) --* 

        An object that contains the delivery stream ARN and the IAM role ARN associated with an Amazon Kinesis Firehose event destination.

        

      
        - **IAMRoleARN** *(string) --* **[REQUIRED]** 

          The ARN of the IAM role under which Amazon SES publishes email sending events to the Amazon Kinesis Firehose stream.

          

        
        - **DeliveryStreamARN** *(string) --* **[REQUIRED]** 

          The ARN of the Amazon Kinesis Firehose stream that email sending events should be published to.

          

        
      
      - **CloudWatchDestination** *(dict) --* 

        An object that contains the names, default values, and sources of the dimensions associated with an Amazon CloudWatch event destination.

        

      
        - **DimensionConfigurations** *(list) --* **[REQUIRED]** 

          A list of dimensions upon which to categorize your emails when you publish email sending events to Amazon CloudWatch.

          

        
          - *(dict) --* 

            Contains the dimension configuration to use when you publish email sending events to Amazon CloudWatch.

             

            For information about publishing email sending events to Amazon CloudWatch, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html>`__ .

            

          
            - **DimensionName** *(string) --* **[REQUIRED]** 

              The name of an Amazon CloudWatch dimension associated with an email sending metric. The name must:

               

               
              * Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
               
              * Contain less than 256 characters. 
               

              

            
            - **DimensionValueSource** *(string) --* **[REQUIRED]** 

              The place where Amazon SES finds the value of a dimension to publish to Amazon CloudWatch. If you want Amazon SES to use the message tags that you specify using an ``X-SES-MESSAGE-TAGS`` header or a parameter to the ``SendEmail`` /``SendRawEmail`` API, choose ``messageTag`` . If you want Amazon SES to use your own email headers, choose ``emailHeader`` .

              

            
            - **DefaultDimensionValue** *(string) --* **[REQUIRED]** 

              The default value of the dimension that is published to Amazon CloudWatch if you do not provide the value of the dimension when you send an email. The default value must:

               

               
              * Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). 
               
              * Contain less than 256 characters. 
               

              

            
          
      
      
      - **SNSDestination** *(dict) --* 

        An object that contains the topic ARN associated with an Amazon Simple Notification Service (Amazon SNS) event destination.

        

      
        - **TopicARN** *(string) --* **[REQUIRED]** 

          The ARN of the Amazon SNS topic that email sending events will be published to. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

          

        
      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

  .. py:method:: update_configuration_set_reputation_metrics_enabled(**kwargs)

    

    Enables or disables the publishing of reputation metrics for emails sent using a specific configuration set. Reputation metrics include bounce and complaint rates. These metrics are published to Amazon CloudWatch. By using Amazon CloudWatch, you can create alarms when bounce or complaint rates exceed a certain threshold.

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/UpdateConfigurationSetReputationMetricsEnabled>`_    


    **Request Syntax** 
    ::

      response = client.update_configuration_set_reputation_metrics_enabled(
          ConfigurationSetName='string',
          Enabled=True|False
      )
    :type ConfigurationSetName: string
    :param ConfigurationSetName: **[REQUIRED]** 

      The name of the configuration set that you want to update.

      

    
    :type Enabled: boolean
    :param Enabled: **[REQUIRED]** 

      Describes whether or not Amazon SES will publish reputation metrics for the configuration set, such as bounce and complaint rates, to Amazon CloudWatch.

      

    
    
    :returns: None

  .. py:method:: update_configuration_set_sending_enabled(**kwargs)

    

    Enables or disables email sending for messages sent using a specific configuration set. You can use this operation in conjunction with Amazon CloudWatch alarms to temporarily pause email sending for a configuration set when the reputation metrics for that configuration set (such as your bounce on complaint rate) reach certain thresholds.

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/UpdateConfigurationSetSendingEnabled>`_    


    **Request Syntax** 
    ::

      response = client.update_configuration_set_sending_enabled(
          ConfigurationSetName='string',
          Enabled=True|False
      )
    :type ConfigurationSetName: string
    :param ConfigurationSetName: **[REQUIRED]** 

      The name of the configuration set that you want to update.

      

    
    :type Enabled: boolean
    :param Enabled: **[REQUIRED]** 

      Describes whether email sending is enabled or disabled for the configuration set. 

      

    
    
    :returns: None

  .. py:method:: update_configuration_set_tracking_options(**kwargs)

    

    Modifies an association between a configuration set and a custom domain for open and click event tracking. 

     

    By default, images and links used for tracking open and click events are hosted on domains operated by Amazon SES. You can configure a subdomain of your own to handle these events. For information about using configuration sets, see `Configuring Custom Domains to Handle Open and Click Tracking <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/configure-custom-open-click-domains.html>`__ in the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/Welcome.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/UpdateConfigurationSetTrackingOptions>`_    


    **Request Syntax** 
    ::

      response = client.update_configuration_set_tracking_options(
          ConfigurationSetName='string',
          TrackingOptions={
              'CustomRedirectDomain': 'string'
          }
      )
    :type ConfigurationSetName: string
    :param ConfigurationSetName: **[REQUIRED]** 

      The name of the configuration set for which you want to update the custom tracking domain.

      

    
    :type TrackingOptions: dict
    :param TrackingOptions: **[REQUIRED]** 

      A domain that is used to redirect email recipients to an Amazon SES-operated domain. This domain captures open and click events generated by Amazon SES emails.

       

      For more information, see `Configuring Custom Domains to Handle Open and Click Tracking <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/configure-custom-open-click-domains.html>`__ in the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/Welcome.html>`__ .

      

    
      - **CustomRedirectDomain** *(string) --* 

        The custom subdomain that will be used to redirect email recipients to the Amazon SES event tracking domain.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

  .. py:method:: update_custom_verification_email_template(**kwargs)

    

    Updates an existing custom verification email template.

     

    For more information about custom verification email templates, see `Using Custom Verification Email Templates <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-verification-emails.html>`__ in the *Amazon SES Developer Guide* .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/UpdateCustomVerificationEmailTemplate>`_    


    **Request Syntax** 
    ::

      response = client.update_custom_verification_email_template(
          TemplateName='string',
          FromEmailAddress='string',
          TemplateSubject='string',
          TemplateContent='string',
          SuccessRedirectionURL='string',
          FailureRedirectionURL='string'
      )
    :type TemplateName: string
    :param TemplateName: **[REQUIRED]** 

      The name of the custom verification email template that you want to update.

      

    
    :type FromEmailAddress: string
    :param FromEmailAddress: 

      The email address that the custom verification email is sent from.

      

    
    :type TemplateSubject: string
    :param TemplateSubject: 

      The subject line of the custom verification email.

      

    
    :type TemplateContent: string
    :param TemplateContent: 

      The content of the custom verification email. The total size of the email must be less than 10 MB. The message body may contain HTML, with some limitations. For more information, see `Custom Verification Email Frequently Asked Questions <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/custom-verification-emails.html#custom-verification-emails-faq>`__ in the *Amazon SES Developer Guide* .

      

    
    :type SuccessRedirectionURL: string
    :param SuccessRedirectionURL: 

      The URL that the recipient of the verification email is sent to if his or her address is successfully verified.

      

    
    :type FailureRedirectionURL: string
    :param FailureRedirectionURL: 

      The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.

      

    
    
    :returns: None

  .. py:method:: update_receipt_rule(**kwargs)

    

    Updates a receipt rule.

     

    For information about managing receipt rules, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-managing-receipt-rules.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/UpdateReceiptRule>`_    


    **Request Syntax** 
    ::

      response = client.update_receipt_rule(
          RuleSetName='string',
          Rule={
              'Name': 'string',
              'Enabled': True|False,
              'TlsPolicy': 'Require'|'Optional',
              'Recipients': [
                  'string',
              ],
              'Actions': [
                  {
                      'S3Action': {
                          'TopicArn': 'string',
                          'BucketName': 'string',
                          'ObjectKeyPrefix': 'string',
                          'KmsKeyArn': 'string'
                      },
                      'BounceAction': {
                          'TopicArn': 'string',
                          'SmtpReplyCode': 'string',
                          'StatusCode': 'string',
                          'Message': 'string',
                          'Sender': 'string'
                      },
                      'WorkmailAction': {
                          'TopicArn': 'string',
                          'OrganizationArn': 'string'
                      },
                      'LambdaAction': {
                          'TopicArn': 'string',
                          'FunctionArn': 'string',
                          'InvocationType': 'Event'|'RequestResponse'
                      },
                      'StopAction': {
                          'Scope': 'RuleSet',
                          'TopicArn': 'string'
                      },
                      'AddHeaderAction': {
                          'HeaderName': 'string',
                          'HeaderValue': 'string'
                      },
                      'SNSAction': {
                          'TopicArn': 'string',
                          'Encoding': 'UTF-8'|'Base64'
                      }
                  },
              ],
              'ScanEnabled': True|False
          }
      )
    :type RuleSetName: string
    :param RuleSetName: **[REQUIRED]** 

      The name of the receipt rule set that the receipt rule belongs to.

      

    
    :type Rule: dict
    :param Rule: **[REQUIRED]** 

      A data structure that contains the updated receipt rule information.

      

    
      - **Name** *(string) --* **[REQUIRED]** 

        The name of the receipt rule. The name must:

         

         
        * Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-). 
         
        * Start and end with a letter or number. 
         
        * Contain less than 64 characters. 
         

        

      
      - **Enabled** *(boolean) --* 

        If ``true`` , the receipt rule is active. The default value is ``false`` .

        

      
      - **TlsPolicy** *(string) --* 

        Specifies whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). If this parameter is set to ``Require`` , Amazon SES will bounce emails that are not received over TLS. The default is ``Optional`` .

        

      
      - **Recipients** *(list) --* 

        The recipient domains and email addresses that the receipt rule applies to. If this field is not specified, this rule will match all recipients under all verified domains.

        

      
        - *(string) --* 

        
    
      - **Actions** *(list) --* 

        An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule.

        

      
        - *(dict) --* 

          An action that Amazon SES can take when it receives an email on behalf of one or more email addresses or domains that you own. An instance of this data type can represent only one action.

           

          For information about setting up receipt rules, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html>`__ .

          

        
          - **S3Action** *(dict) --* 

            Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and, optionally, publishes a notification to Amazon SNS.

            

          
            - **TopicArn** *(string) --* 

              The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3 bucket. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

              

            
            - **BucketName** *(string) --* **[REQUIRED]** 

              The name of the Amazon S3 bucket that incoming email will be saved to.

              

            
            - **ObjectKeyPrefix** *(string) --* 

              The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory name that enables you to store similar data under the same directory in a bucket.

              

            
            - **KmsKeyArn** *(string) --* 

              The customer master key that Amazon SES should use to encrypt your emails before saving them to the Amazon S3 bucket. You can use the default master key or a custom master key you created in AWS KMS as follows:

               

               
              * To use the default master key, provide an ARN in the form of ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if your AWS account ID is 123456789012 and you want to use the default master key in the US West (Oregon) region, the ARN of the default master key would be ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default master key, you don't need to perform any extra steps to give Amazon SES permission to use the key. 
               
              * To use a custom master key you created in AWS KMS, provide the ARN of the master key and ensure that you add a statement to your key's policy to give Amazon SES permission to use it. For more information about giving permissions, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-permissions.html>`__ . 
               

               

              For more information about key policies, see the `AWS KMS Developer Guide <http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`__ . If you do not specify a master key, Amazon SES will not encrypt your emails.

               

              .. warning::

                 

                Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3 server-side encryption. This means that you must use the Amazon S3 encryption client to decrypt the email after retrieving it from Amazon S3, as the service has no access to use your AWS KMS keys for decryption. This encryption client is currently available with the `AWS Java SDK <http://aws.amazon.com/sdk-for-java/>`__ and `AWS Ruby SDK <http://aws.amazon.com/sdk-for-ruby/>`__ only. For more information about client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer Guide <http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__ .

                 

              

            
          
          - **BounceAction** *(dict) --* 

            Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).

            

          
            - **TopicArn** *(string) --* 

              The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action is taken. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

              

            
            - **SmtpReplyCode** *(string) --* **[REQUIRED]** 

              The SMTP reply code, as defined by `RFC 5321 <https://tools.ietf.org/html/rfc5321>`__ .

              

            
            - **StatusCode** *(string) --* 

              The SMTP enhanced status code, as defined by `RFC 3463 <https://tools.ietf.org/html/rfc3463>`__ .

              

            
            - **Message** *(string) --* **[REQUIRED]** 

              Human-readable text to include in the bounce message.

              

            
            - **Sender** *(string) --* **[REQUIRED]** 

              The email address of the sender of the bounced email. This is the address from which the bounce message will be sent.

              

            
          
          - **WorkmailAction** *(dict) --* 

            Calls Amazon WorkMail and, optionally, publishes a notification to Amazon SNS.

            

          
            - **TopicArn** *(string) --* 

              The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action is called. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

              

            
            - **OrganizationArn** *(string) --* **[REQUIRED]** 

              The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail organization ARN is ``arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7`` . For information about Amazon WorkMail organizations, see the `Amazon WorkMail Administrator Guide <http://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`__ .

              

            
          
          - **LambdaAction** *(dict) --* 

            Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.

            

          
            - **TopicArn** *(string) --* 

              The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action is taken. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

              

            
            - **FunctionArn** *(string) --* **[REQUIRED]** 

              The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS Lambda function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction`` . For more information about AWS Lambda, see the `AWS Lambda Developer Guide <http://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`__ .

              

            
            - **InvocationType** *(string) --* 

              The invocation type of the AWS Lambda function. An invocation type of ``RequestResponse`` means that the execution of the function will immediately result in a response, and a value of ``Event`` means that the function will be invoked asynchronously. The default value is ``Event`` . For information about AWS Lambda invocation types, see the `AWS Lambda Developer Guide <http://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`__ .

               

              .. warning::

                 

                There is a 30-second timeout on ``RequestResponse`` invocations. You should use ``Event`` invocation in most cases. Use ``RequestResponse`` only when you want to make a mail flow decision, such as whether to stop the receipt rule or the receipt rule set.

                 

              

            
          
          - **StopAction** *(dict) --* 

            Terminates the evaluation of the receipt rule set and optionally publishes a notification to Amazon SNS.

            

          
            - **Scope** *(string) --* **[REQUIRED]** 

              The name of the RuleSet that is being stopped.

              

            
            - **TopicArn** *(string) --* 

              The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is taken. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

              

            
          
          - **AddHeaderAction** *(dict) --* 

            Adds a header to the received email.

            

          
            - **HeaderName** *(string) --* **[REQUIRED]** 

              The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

              

            
            - **HeaderValue** *(string) --* **[REQUIRED]** 

              Must be less than 2048 characters, and must not contain newline characters ("\r" or "\n").

              

            
          
          - **SNSAction** *(dict) --* 

            Publishes the email content within a notification to Amazon SNS.

            

          
            - **TopicArn** *(string) --* **[REQUIRED]** 

              The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an Amazon SNS topic ARN is ``arn:aws:sns:us-west-2:123456789012:MyTopic`` . For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`__ .

              

            
            - **Encoding** *(string) --* 

              The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier to use, but may not preserve all special characters when a message was encoded with a different encoding format. Base64 preserves all special characters. The default value is UTF-8.

              

            
          
        
    
      - **ScanEnabled** *(boolean) --* 

        If ``true`` , then messages that this receipt rule applies to are scanned for spam and viruses. The default value is ``false`` .

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

    **Examples** 

    The following example updates a receipt rule to use an Amazon S3 action:
    ::

      response = client.update_receipt_rule(
          Rule={
              'Actions': [
                  {
                      'S3Action': {
                          'BucketName': 'MyBucket',
                          'ObjectKeyPrefix': 'email',
                      },
                  },
              ],
              'Enabled': True,
              'Name': 'MyRule',
              'ScanEnabled': True,
              'TlsPolicy': 'Optional',
          },
          RuleSetName='MyRuleSet',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: update_template(**kwargs)

    

    Updates an email template. Email templates enable you to send personalized email to one or more destinations in a single API operation. For more information, see the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-email-api.html>`__ .

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/UpdateTemplate>`_    


    **Request Syntax** 
    ::

      response = client.update_template(
          Template={
              'TemplateName': 'string',
              'SubjectPart': 'string',
              'TextPart': 'string',
              'HtmlPart': 'string'
          }
      )
    :type Template: dict
    :param Template: **[REQUIRED]** 

      The content of the email, composed of a subject line, an HTML part, and a text-only part.

      

    
      - **TemplateName** *(string) --* **[REQUIRED]** 

        The name of the template. You will refer to this name when you send email using the ``SendTemplatedEmail`` or ``SendBulkTemplatedEmail`` operations.

        

      
      - **SubjectPart** *(string) --* 

        The subject line of the email.

        

      
      - **TextPart** *(string) --* 

        The email body that will be visible to recipients whose email clients do not display HTML.

        

      
      - **HtmlPart** *(string) --* 

        The HTML body of the email.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: verify_domain_dkim(**kwargs)

    

    Returns a set of DKIM tokens for a domain. DKIM *tokens* are character strings that represent your domain's identity. Using these tokens, you will need to create DNS CNAME records that point to DKIM public keys hosted by Amazon SES. Amazon Web Services will eventually detect that you have updated your DNS records; this detection process may take up to 72 hours. Upon successful detection, Amazon SES will be able to DKIM-sign email originating from that domain.

     

    You can execute this operation no more than once per second.

     

    To enable or disable Easy DKIM signing for a domain, use the ``SetIdentityDkimEnabled`` operation.

     

    For more information about creating DNS records using DKIM tokens, go to the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim-dns-records.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/VerifyDomainDkim>`_    


    **Request Syntax** 
    ::

      response = client.verify_domain_dkim(
          Domain='string'
      )
    :type Domain: string
    :param Domain: **[REQUIRED]** 

      The name of the domain to be verified for Easy DKIM signing.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DkimTokens': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        Returns CNAME records that you must publish to the DNS server of your domain to set up Easy DKIM with Amazon SES.

        
        

        - **DkimTokens** *(list) --* 

          A set of character strings that represent the domain's identity. If the identity is an email address, the tokens represent the domain of that address.

           

          Using these tokens, you will need to create DNS CNAME records that point to DKIM public keys hosted by Amazon SES. Amazon Web Services will eventually detect that you have updated your DNS records; this detection process may take up to 72 hours. Upon successful detection, Amazon SES will be able to DKIM-sign emails originating from that domain.

           

          For more information about creating DNS records using DKIM tokens, go to the `Amazon SES Developer Guide <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim-dns-records.html>`__ .

          
          

          - *(string) --* 
      
    

    **Examples** 

    The following example generates DKIM tokens for a domain that has been verified with Amazon SES:
    ::

      response = client.verify_domain_dkim(
          Domain='example.com',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'DkimTokens': [
              'EXAMPLEq76owjnks3lnluwg65scbemvw',
              'EXAMPLEi3dnsj67hstzaj673klariwx2',
              'EXAMPLEwfbtcukvimehexktmdtaz6naj',
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: verify_domain_identity(**kwargs)

    

    Adds a domain to the list of identities for your Amazon SES account and attempts to verify it. For more information about verifying domains, see `Verifying Email Addresses and Domains <http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html>`__ in the *Amazon SES Developer Guide.*  

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/VerifyDomainIdentity>`_    


    **Request Syntax** 
    ::

      response = client.verify_domain_identity(
          Domain='string'
      )
    :type Domain: string
    :param Domain: **[REQUIRED]** 

      The domain to be verified.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'VerificationToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        Returns a TXT record that you must publish to the DNS server of your domain to complete domain verification with Amazon SES.

        
        

        - **VerificationToken** *(string) --* 

          A TXT record that you must place in the DNS settings of the domain to complete domain verification with Amazon SES.

           

          As Amazon SES searches for the TXT record, the domain's verification status is "Pending". When Amazon SES detects the record, the domain's verification status changes to "Success". If Amazon SES is unable to detect the record within 72 hours, the domain's verification status changes to "Failed." In that case, if you still want to verify the domain, you must restart the verification process from the beginning.

          
    

    **Examples** 

    The following example starts the domain verification process with Amazon SES:
    ::

      response = client.verify_domain_identity(
          Domain='example.com',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'VerificationToken': 'eoEmxw+YaYhb3h3iVJHuXMJXqeu1q1/wwmvjuEXAMPLE',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: verify_email_address(**kwargs)

    

    Deprecated. Use the ``VerifyEmailIdentity`` operation to verify a new email address.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/VerifyEmailAddress>`_    


    **Request Syntax** 
    ::

      response = client.verify_email_address(
          EmailAddress='string'
      )
    :type EmailAddress: string
    :param EmailAddress: **[REQUIRED]** 

      The email address to be verified.

      

    
    
    :returns: None

    **Examples** 

    The following example starts the email address verification process with Amazon SES:
    ::

      response = client.verify_email_address(
          EmailAddress='user@example.com',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: verify_email_identity(**kwargs)

    

    Adds an email address to the list of identities for your Amazon SES account and attempts to verify it. This operation causes a confirmation email message to be sent to the specified address.

     

    You can execute this operation no more than once per second.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/VerifyEmailIdentity>`_    


    **Request Syntax** 
    ::

      response = client.verify_email_identity(
          EmailAddress='string'
      )
    :type EmailAddress: string
    :param EmailAddress: **[REQUIRED]** 

      The email address to be verified.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 

        An empty element returned on a successful request.

        
    

    **Examples** 

    The following example starts the email address verification process with Amazon SES:
    ::

      response = client.verify_email_identity(
          EmailAddress='user@example.com',
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

* :py:class:`SES.Paginator.ListIdentities`



.. py:class:: SES.Paginator.ListIdentities

  ::

    
    paginator = client.get_paginator('list_identities')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`SES.Client.list_identities`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/ListIdentities>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          IdentityType='EmailAddress'|'Domain',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type IdentityType: string
    :param IdentityType: 

      The type of the identities to list. Possible values are "EmailAddress" and "Domain". If this parameter is omitted, then all identities will be listed.

      

    
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
            'Identities': [
                'string',
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 

        A list of all identities that you have attempted to verify under your AWS account, regardless of verification status.

        
        

        - **Identities** *(list) --* 

          A list of identities.

          
          

          - *(string) --* 
      
    

=======
Waiters
=======


The available waiters are:

* :py:class:`SES.Waiter.IdentityExists`



.. py:class:: SES.Waiter.IdentityExists

  ::

    
    waiter = client.get_waiter('identity_exists')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`SES.Client.get_identity_verification_attributes` every 3 seconds until a successful state is reached. An error is returned after 20 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/GetIdentityVerificationAttributes>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          Identities=[
              'string',
          ],
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type Identities: list
    :param Identities: **[REQUIRED]** 

      A list of identities.

      

    
      - *(string) --* 

      
  
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 3

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 20

        

      
    
    
    :returns: None