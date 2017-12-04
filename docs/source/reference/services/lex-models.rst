

***********************
LexModelBuildingService
***********************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: LexModelBuildingService.Client

  A low-level client representing Amazon Lex Model Building Service::

    
    import boto3
    
    client = boto3.client('lex-models')

  
  These are the available methods:
  
  *   :py:meth:`~LexModelBuildingService.Client.can_paginate`

  
  *   :py:meth:`~LexModelBuildingService.Client.create_bot_version`

  
  *   :py:meth:`~LexModelBuildingService.Client.create_intent_version`

  
  *   :py:meth:`~LexModelBuildingService.Client.create_slot_type_version`

  
  *   :py:meth:`~LexModelBuildingService.Client.delete_bot`

  
  *   :py:meth:`~LexModelBuildingService.Client.delete_bot_alias`

  
  *   :py:meth:`~LexModelBuildingService.Client.delete_bot_channel_association`

  
  *   :py:meth:`~LexModelBuildingService.Client.delete_bot_version`

  
  *   :py:meth:`~LexModelBuildingService.Client.delete_intent`

  
  *   :py:meth:`~LexModelBuildingService.Client.delete_intent_version`

  
  *   :py:meth:`~LexModelBuildingService.Client.delete_slot_type`

  
  *   :py:meth:`~LexModelBuildingService.Client.delete_slot_type_version`

  
  *   :py:meth:`~LexModelBuildingService.Client.delete_utterances`

  
  *   :py:meth:`~LexModelBuildingService.Client.generate_presigned_url`

  
  *   :py:meth:`~LexModelBuildingService.Client.get_bot`

  
  *   :py:meth:`~LexModelBuildingService.Client.get_bot_alias`

  
  *   :py:meth:`~LexModelBuildingService.Client.get_bot_aliases`

  
  *   :py:meth:`~LexModelBuildingService.Client.get_bot_channel_association`

  
  *   :py:meth:`~LexModelBuildingService.Client.get_bot_channel_associations`

  
  *   :py:meth:`~LexModelBuildingService.Client.get_bot_versions`

  
  *   :py:meth:`~LexModelBuildingService.Client.get_bots`

  
  *   :py:meth:`~LexModelBuildingService.Client.get_builtin_intent`

  
  *   :py:meth:`~LexModelBuildingService.Client.get_builtin_intents`

  
  *   :py:meth:`~LexModelBuildingService.Client.get_builtin_slot_types`

  
  *   :py:meth:`~LexModelBuildingService.Client.get_export`

  
  *   :py:meth:`~LexModelBuildingService.Client.get_intent`

  
  *   :py:meth:`~LexModelBuildingService.Client.get_intent_versions`

  
  *   :py:meth:`~LexModelBuildingService.Client.get_intents`

  
  *   :py:meth:`~LexModelBuildingService.Client.get_paginator`

  
  *   :py:meth:`~LexModelBuildingService.Client.get_slot_type`

  
  *   :py:meth:`~LexModelBuildingService.Client.get_slot_type_versions`

  
  *   :py:meth:`~LexModelBuildingService.Client.get_slot_types`

  
  *   :py:meth:`~LexModelBuildingService.Client.get_utterances_view`

  
  *   :py:meth:`~LexModelBuildingService.Client.get_waiter`

  
  *   :py:meth:`~LexModelBuildingService.Client.put_bot`

  
  *   :py:meth:`~LexModelBuildingService.Client.put_bot_alias`

  
  *   :py:meth:`~LexModelBuildingService.Client.put_intent`

  
  *   :py:meth:`~LexModelBuildingService.Client.put_slot_type`

  

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


  .. py:method:: create_bot_version(**kwargs)

    

    Creates a new version of the bot based on the ``$LATEST`` version. If the ``$LATEST`` version of this resource hasn't changed since you created the last version, Amazon Lex doesn't create a new version. It returns the last created version.

     

    .. note::

       

      You can update only the ``$LATEST`` version of the bot. You can't update the numbered versions that you create with the ``CreateBotVersion`` operation.

       

     

    When you create the first version of a bot, Amazon Lex sets the version to 1. Subsequent versions increment by 1. For more information, see  versioning-intro . 

     

    This operation requires permission for the ``lex:CreateBotVersion`` action. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/CreateBotVersion>`_    


    **Request Syntax** 
    ::

      response = client.create_bot_version(
          name='string',
          checksum='string'
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the bot that you want to create a new version of. The name is case sensitive. 

      

    
    :type checksum: string
    :param checksum: 

      Identifies a specific revision of the ``$LATEST`` version of the bot. If you specify a checksum and the ``$LATEST`` version of the bot has a different checksum, a ``PreconditionFailedException`` exception is returned and Amazon Lex doesn't publish a new version. If you don't specify a checksum, Amazon Lex publishes the ``$LATEST`` version.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'name': 'string',
            'description': 'string',
            'intents': [
                {
                    'intentName': 'string',
                    'intentVersion': 'string'
                },
            ],
            'clarificationPrompt': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML',
                        'content': 'string'
                    },
                ],
                'maxAttempts': 123,
                'responseCard': 'string'
            },
            'abortStatement': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML',
                        'content': 'string'
                    },
                ],
                'responseCard': 'string'
            },
            'status': 'BUILDING'|'READY'|'FAILED'|'NOT_BUILT',
            'failureReason': 'string',
            'lastUpdatedDate': datetime(2015, 1, 1),
            'createdDate': datetime(2015, 1, 1),
            'idleSessionTTLInSeconds': 123,
            'voiceId': 'string',
            'checksum': 'string',
            'version': 'string',
            'locale': 'en-US',
            'childDirected': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **name** *(string) --* 

          The name of the bot.

          
        

        - **description** *(string) --* 

          A description of the bot.

          
        

        - **intents** *(list) --* 

          An array of ``Intent`` objects. For more information, see  PutBot .

          
          

          - *(dict) --* 

            Identifies the specific version of an intent.

            
            

            - **intentName** *(string) --* 

              The name of the intent.

              
            

            - **intentVersion** *(string) --* 

              The version of the intent.

              
        
      
        

        - **clarificationPrompt** *(dict) --* 

          The message that Amazon Lex uses when it doesn't understand the user's request. For more information, see  PutBot . 

          
          

          - **messages** *(list) --* 

            An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

            
            

            - *(dict) --* 

              The message object that provides the message text and its type.

              
              

              - **contentType** *(string) --* 

                The content type of the message string.

                
              

              - **content** *(string) --* 

                The text of the message.

                
          
        
          

          - **maxAttempts** *(integer) --* 

            The number of times to prompt the user for information.

            
          

          - **responseCard** *(string) --* 

            A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card . 

            
      
        

        - **abortStatement** *(dict) --* 

          The message that Amazon Lex uses to abort a conversation. For more information, see  PutBot .

          
          

          - **messages** *(list) --* 

            A collection of message objects.

            
            

            - *(dict) --* 

              The message object that provides the message text and its type.

              
              

              - **contentType** *(string) --* 

                The content type of the message string.

                
              

              - **content** *(string) --* 

                The text of the message.

                
          
        
          

          - **responseCard** *(string) --* 

            At runtime, if the client is using the `PostText <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card. 

            
      
        

        - **status** *(string) --* 

          When you send a request to create or update a bot, Amazon Lex sets the ``status`` response element to ``BUILDING`` . After Amazon Lex builds the bot, it sets ``status`` to ``READY`` . If Amazon Lex can't build the bot, it sets ``status`` to ``FAILED`` . Amazon Lex returns the reason for the failure in the ``failureReason`` response element. 

          
        

        - **failureReason** *(string) --* 

          If ``status`` is ``FAILED`` , Amazon Lex provides the reason that it failed to build the bot.

          
        

        - **lastUpdatedDate** *(datetime) --* 

          The date when the ``$LATEST`` version of this bot was updated. 

          
        

        - **createdDate** *(datetime) --* 

          The date when the bot version was created.

          
        

        - **idleSessionTTLInSeconds** *(integer) --* 

          The maximum time in seconds that Amazon Lex retains the data gathered in a conversation. For more information, see  PutBot .

          
        

        - **voiceId** *(string) --* 

          The Amazon Polly voice ID that Amazon Lex uses for voice interactions with the user.

          
        

        - **checksum** *(string) --* 

          Checksum identifying the version of the bot that was created.

          
        

        - **version** *(string) --* 

          The version of the bot. 

          
        

        - **locale** *(string) --* 

          Specifies the target locale for the bot. 

          
        

        - **childDirected** *(boolean) --* 

          For each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to the Children's Online Privacy Protection Act (COPPA) by specifying ``true`` or ``false`` in the ``childDirected`` field. By specifying ``true`` in the ``childDirected`` field, you confirm that your use of Amazon Lex **is** related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. By specifying ``false`` in the ``childDirected`` field, you confirm that your use of Amazon Lex **is not** related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not specify a default value for the ``childDirected`` field that does not accurately reflect whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA.

           

          If your use of Amazon Lex relates to a website, program, or other application that is directed in whole or in part, to children under age 13, you must obtain any required verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in connection with websites, programs, or other applications that are directed or targeted, in whole or in part, to children under age 13, see the `Amazon Lex FAQ. <https://aws.amazon.com/lex/faqs#data-security>`__  

          
    

  .. py:method:: create_intent_version(**kwargs)

    

    Creates a new version of an intent based on the ``$LATEST`` version of the intent. If the ``$LATEST`` version of this intent hasn't changed since you last updated it, Amazon Lex doesn't create a new version. It returns the last version you created.

     

    .. note::

       

      You can update only the ``$LATEST`` version of the intent. You can't update the numbered versions that you create with the ``CreateIntentVersion`` operation.

       

     

    When you create a version of an intent, Amazon Lex sets the version to 1. Subsequent versions increment by 1. For more information, see  versioning-intro . 

     

    This operation requires permissions to perform the ``lex:CreateIntentVersion`` action. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/CreateIntentVersion>`_    


    **Request Syntax** 
    ::

      response = client.create_intent_version(
          name='string',
          checksum='string'
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the intent that you want to create a new version of. The name is case sensitive. 

      

    
    :type checksum: string
    :param checksum: 

      Checksum of the ``$LATEST`` version of the intent that should be used to create the new version. If you specify a checksum and the ``$LATEST`` version of the intent has a different checksum, Amazon Lex returns a ``PreconditionFailedException`` exception and doesn't publish a new version. If you don't specify a checksum, Amazon Lex publishes the ``$LATEST`` version.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'name': 'string',
            'description': 'string',
            'slots': [
                {
                    'name': 'string',
                    'description': 'string',
                    'slotConstraint': 'Required'|'Optional',
                    'slotType': 'string',
                    'slotTypeVersion': 'string',
                    'valueElicitationPrompt': {
                        'messages': [
                            {
                                'contentType': 'PlainText'|'SSML',
                                'content': 'string'
                            },
                        ],
                        'maxAttempts': 123,
                        'responseCard': 'string'
                    },
                    'priority': 123,
                    'sampleUtterances': [
                        'string',
                    ],
                    'responseCard': 'string'
                },
            ],
            'sampleUtterances': [
                'string',
            ],
            'confirmationPrompt': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML',
                        'content': 'string'
                    },
                ],
                'maxAttempts': 123,
                'responseCard': 'string'
            },
            'rejectionStatement': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML',
                        'content': 'string'
                    },
                ],
                'responseCard': 'string'
            },
            'followUpPrompt': {
                'prompt': {
                    'messages': [
                        {
                            'contentType': 'PlainText'|'SSML',
                            'content': 'string'
                        },
                    ],
                    'maxAttempts': 123,
                    'responseCard': 'string'
                },
                'rejectionStatement': {
                    'messages': [
                        {
                            'contentType': 'PlainText'|'SSML',
                            'content': 'string'
                        },
                    ],
                    'responseCard': 'string'
                }
            },
            'conclusionStatement': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML',
                        'content': 'string'
                    },
                ],
                'responseCard': 'string'
            },
            'dialogCodeHook': {
                'uri': 'string',
                'messageVersion': 'string'
            },
            'fulfillmentActivity': {
                'type': 'ReturnIntent'|'CodeHook',
                'codeHook': {
                    'uri': 'string',
                    'messageVersion': 'string'
                }
            },
            'parentIntentSignature': 'string',
            'lastUpdatedDate': datetime(2015, 1, 1),
            'createdDate': datetime(2015, 1, 1),
            'version': 'string',
            'checksum': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **name** *(string) --* 

          The name of the intent.

          
        

        - **description** *(string) --* 

          A description of the intent.

          
        

        - **slots** *(list) --* 

          An array of slot types that defines the information required to fulfill the intent.

          
          

          - *(dict) --* 

            Identifies the version of a specific slot.

            
            

            - **name** *(string) --* 

              The name of the slot.

              
            

            - **description** *(string) --* 

              A description of the slot.

              
            

            - **slotConstraint** *(string) --* 

              Specifies whether the slot is required or optional. 

              
            

            - **slotType** *(string) --* 

              The type of the slot, either a custom slot type that you defined or one of the built-in slot types.

              
            

            - **slotTypeVersion** *(string) --* 

              The version of the slot type.

              
            

            - **valueElicitationPrompt** *(dict) --* 

              The prompt that Amazon Lex uses to elicit the slot value from the user.

              
              

              - **messages** *(list) --* 

                An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

                
                

                - *(dict) --* 

                  The message object that provides the message text and its type.

                  
                  

                  - **contentType** *(string) --* 

                    The content type of the message string.

                    
                  

                  - **content** *(string) --* 

                    The text of the message.

                    
              
            
              

              - **maxAttempts** *(integer) --* 

                The number of times to prompt the user for information.

                
              

              - **responseCard** *(string) --* 

                A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card . 

                
          
            

            - **priority** *(integer) --* 

              Directs Lex the order in which to elicit this slot value from the user. For example, if the intent has two slots with priorities 1 and 2, AWS Lex first elicits a value for the slot with priority 1.

               

              If multiple slots share the same priority, the order in which Lex elicits values is arbitrary.

              
            

            - **sampleUtterances** *(list) --* 

              If you know a specific pattern with which users might respond to an Amazon Lex request for a slot value, you can provide those utterances to improve accuracy. This is optional. In most cases, Amazon Lex is capable of understanding user utterances. 

              
              

              - *(string) --* 
          
            

            - **responseCard** *(string) --* 

              A set of possible responses for the slot type used by text-based clients. A user chooses an option from the response card, instead of using text to reply. 

              
        
      
        

        - **sampleUtterances** *(list) --* 

          An array of sample utterances configured for the intent. 

          
          

          - *(string) --* 
      
        

        - **confirmationPrompt** *(dict) --* 

          If defined, the prompt that Amazon Lex uses to confirm the user's intent before fulfilling it. 

          
          

          - **messages** *(list) --* 

            An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

            
            

            - *(dict) --* 

              The message object that provides the message text and its type.

              
              

              - **contentType** *(string) --* 

                The content type of the message string.

                
              

              - **content** *(string) --* 

                The text of the message.

                
          
        
          

          - **maxAttempts** *(integer) --* 

            The number of times to prompt the user for information.

            
          

          - **responseCard** *(string) --* 

            A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card . 

            
      
        

        - **rejectionStatement** *(dict) --* 

          If the user answers "no" to the question defined in ``confirmationPrompt`` , Amazon Lex responds with this statement to acknowledge that the intent was canceled. 

          
          

          - **messages** *(list) --* 

            A collection of message objects.

            
            

            - *(dict) --* 

              The message object that provides the message text and its type.

              
              

              - **contentType** *(string) --* 

                The content type of the message string.

                
              

              - **content** *(string) --* 

                The text of the message.

                
          
        
          

          - **responseCard** *(string) --* 

            At runtime, if the client is using the `PostText <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card. 

            
      
        

        - **followUpPrompt** *(dict) --* 

          If defined, Amazon Lex uses this prompt to solicit additional user activity after the intent is fulfilled. 

          
          

          - **prompt** *(dict) --* 

            Prompts for information from the user. 

            
            

            - **messages** *(list) --* 

              An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

              
              

              - *(dict) --* 

                The message object that provides the message text and its type.

                
                

                - **contentType** *(string) --* 

                  The content type of the message string.

                  
                

                - **content** *(string) --* 

                  The text of the message.

                  
            
          
            

            - **maxAttempts** *(integer) --* 

              The number of times to prompt the user for information.

              
            

            - **responseCard** *(string) --* 

              A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card . 

              
        
          

          - **rejectionStatement** *(dict) --* 

            If the user answers "no" to the question defined in the ``prompt`` field, Amazon Lex responds with this statement to acknowledge that the intent was canceled. 

            
            

            - **messages** *(list) --* 

              A collection of message objects.

              
              

              - *(dict) --* 

                The message object that provides the message text and its type.

                
                

                - **contentType** *(string) --* 

                  The content type of the message string.

                  
                

                - **content** *(string) --* 

                  The text of the message.

                  
            
          
            

            - **responseCard** *(string) --* 

              At runtime, if the client is using the `PostText <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card. 

              
        
      
        

        - **conclusionStatement** *(dict) --* 

          After the Lambda function specified in the ``fulfillmentActivity`` field fulfills the intent, Amazon Lex conveys this statement to the user. 

          
          

          - **messages** *(list) --* 

            A collection of message objects.

            
            

            - *(dict) --* 

              The message object that provides the message text and its type.

              
              

              - **contentType** *(string) --* 

                The content type of the message string.

                
              

              - **content** *(string) --* 

                The text of the message.

                
          
        
          

          - **responseCard** *(string) --* 

            At runtime, if the client is using the `PostText <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card. 

            
      
        

        - **dialogCodeHook** *(dict) --* 

          If defined, Amazon Lex invokes this Lambda function for each user input.

          
          

          - **uri** *(string) --* 

            The Amazon Resource Name (ARN) of the Lambda function.

            
          

          - **messageVersion** *(string) --* 

            The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see  using-lambda .

            
      
        

        - **fulfillmentActivity** *(dict) --* 

          Describes how the intent is fulfilled. 

          
          

          - **type** *(string) --* 

            How the intent should be fulfilled, either by running a Lambda function or by returning the slot data to the client application. 

            
          

          - **codeHook** *(dict) --* 

            A description of the Lambda function that is run to fulfill the intent. 

            
            

            - **uri** *(string) --* 

              The Amazon Resource Name (ARN) of the Lambda function.

              
            

            - **messageVersion** *(string) --* 

              The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see  using-lambda .

              
        
      
        

        - **parentIntentSignature** *(string) --* 

          A unique identifier for a built-in intent.

          
        

        - **lastUpdatedDate** *(datetime) --* 

          The date that the intent was updated. 

          
        

        - **createdDate** *(datetime) --* 

          The date that the intent was created.

          
        

        - **version** *(string) --* 

          The version number assigned to the new version of the intent.

          
        

        - **checksum** *(string) --* 

          Checksum of the intent version created.

          
    

  .. py:method:: create_slot_type_version(**kwargs)

    

    Creates a new version of a slot type based on the ``$LATEST`` version of the specified slot type. If the ``$LATEST`` version of this resource has not changed since the last version that you created, Amazon Lex doesn't create a new version. It returns the last version that you created. 

     

    .. note::

       

      You can update only the ``$LATEST`` version of a slot type. You can't update the numbered versions that you create with the ``CreateSlotTypeVersion`` operation.

       

     

    When you create a version of a slot type, Amazon Lex sets the version to 1. Subsequent versions increment by 1. For more information, see  versioning-intro . 

     

    This operation requires permissions for the ``lex:CreateSlotTypeVersion`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/CreateSlotTypeVersion>`_    


    **Request Syntax** 
    ::

      response = client.create_slot_type_version(
          name='string',
          checksum='string'
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the slot type that you want to create a new version for. The name is case sensitive. 

      

    
    :type checksum: string
    :param checksum: 

      Checksum for the ``$LATEST`` version of the slot type that you want to publish. If you specify a checksum and the ``$LATEST`` version of the slot type has a different checksum, Amazon Lex returns a ``PreconditionFailedException`` exception and doesn't publish the new version. If you don't specify a checksum, Amazon Lex publishes the ``$LATEST`` version.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'name': 'string',
            'description': 'string',
            'enumerationValues': [
                {
                    'value': 'string',
                    'synonyms': [
                        'string',
                    ]
                },
            ],
            'lastUpdatedDate': datetime(2015, 1, 1),
            'createdDate': datetime(2015, 1, 1),
            'version': 'string',
            'checksum': 'string',
            'valueSelectionStrategy': 'ORIGINAL_VALUE'|'TOP_RESOLUTION'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **name** *(string) --* 

          The name of the slot type.

          
        

        - **description** *(string) --* 

          A description of the slot type.

          
        

        - **enumerationValues** *(list) --* 

          A list of ``EnumerationValue`` objects that defines the values that the slot type can take.

          
          

          - *(dict) --* 

            Each slot type can have a set of values. Each enumeration value represents a value the slot type can take. 

             

            For example, a pizza ordering bot could have a slot type that specifies the type of crust that the pizza should have. The slot type could include the values 

             

             
            * thick 
             
            * thin 
             
            * stuffed 
             

            
            

            - **value** *(string) --* 

              The value of the slot type.

              
            

            - **synonyms** *(list) --* 

              Additional values related to the slot type value.

              
              

              - *(string) --* 
          
        
      
        

        - **lastUpdatedDate** *(datetime) --* 

          The date that the slot type was updated. When you create a resource, the creation date and last update date are the same.

          
        

        - **createdDate** *(datetime) --* 

          The date that the slot type was created.

          
        

        - **version** *(string) --* 

          The version assigned to the new slot type version. 

          
        

        - **checksum** *(string) --* 

          Checksum of the ``$LATEST`` version of the slot type.

          
        

        - **valueSelectionStrategy** *(string) --* 

          The strategy that Amazon Lex uses to determine the value of the slot. For more information, see  PutSlotType .

          
    

  .. py:method:: delete_bot(**kwargs)

    

    Deletes all versions of the bot, including the ``$LATEST`` version. To delete a specific version of the bot, use the  DeleteBotVersion operation.

     

    If a bot has an alias, you can't delete it. Instead, the ``DeleteBot`` operation returns a ``ResourceInUseException`` exception that includes a reference to the alias that refers to the bot. To remove the reference to the bot, delete the alias. If you get the same exception again, delete the referring alias until the ``DeleteBot`` operation is successful.

     

    This operation requires permissions for the ``lex:DeleteBot`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/DeleteBot>`_    


    **Request Syntax** 
    ::

      response = client.delete_bot(
          name='string'
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the bot. The name is case sensitive. 

      

    
    
    :returns: None

  .. py:method:: delete_bot_alias(**kwargs)

    

    Deletes an alias for the specified bot. 

     

    You can't delete an alias that is used in the association between a bot and a messaging channel. If an alias is used in a channel association, the ``DeleteBot`` operation returns a ``ResourceInUseException`` exception that includes a reference to the channel association that refers to the bot. You can remove the reference to the alias by deleting the channel association. If you get the same exception again, delete the referring association until the ``DeleteBotAlias`` operation is successful.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/DeleteBotAlias>`_    


    **Request Syntax** 
    ::

      response = client.delete_bot_alias(
          name='string',
          botName='string'
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the alias to delete. The name is case sensitive. 

      

    
    :type botName: string
    :param botName: **[REQUIRED]** 

      The name of the bot that the alias points to.

      

    
    
    :returns: None

  .. py:method:: delete_bot_channel_association(**kwargs)

    

    Deletes the association between an Amazon Lex bot and a messaging platform.

     

    This operation requires permission for the ``lex:DeleteBotChannelAssociation`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/DeleteBotChannelAssociation>`_    


    **Request Syntax** 
    ::

      response = client.delete_bot_channel_association(
          name='string',
          botName='string',
          botAlias='string'
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the association. The name is case sensitive. 

      

    
    :type botName: string
    :param botName: **[REQUIRED]** 

      The name of the Amazon Lex bot.

      

    
    :type botAlias: string
    :param botAlias: **[REQUIRED]** 

      An alias that points to the specific version of the Amazon Lex bot to which this association is being made.

      

    
    
    :returns: None

  .. py:method:: delete_bot_version(**kwargs)

    

    Deletes a specific version of a bot. To delete all versions of a bot, use the  DeleteBot operation. 

     

    This operation requires permissions for the ``lex:DeleteBotVersion`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/DeleteBotVersion>`_    


    **Request Syntax** 
    ::

      response = client.delete_bot_version(
          name='string',
          version='string'
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the bot.

      

    
    :type version: string
    :param version: **[REQUIRED]** 

      The version of the bot to delete. You cannot delete the ``$LATEST`` version of the bot. To delete the ``$LATEST`` version, use the  DeleteBot operation.

      

    
    
    :returns: None

  .. py:method:: delete_intent(**kwargs)

    

    Deletes all versions of the intent, including the ``$LATEST`` version. To delete a specific version of the intent, use the  DeleteIntentVersion operation.

     

    You can delete a version of an intent only if it is not referenced. To delete an intent that is referred to in one or more bots (see  how-it-works ), you must remove those references first. 

     

    .. note::

       

      If you get the ``ResourceInUseException`` exception, it provides an example reference that shows where the intent is referenced. To remove the reference to the intent, either update the bot or delete it. If you get the same exception when you attempt to delete the intent again, repeat until the intent has no references and the call to ``DeleteIntent`` is successful. 

       

     

    This operation requires permission for the ``lex:DeleteIntent`` action. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/DeleteIntent>`_    


    **Request Syntax** 
    ::

      response = client.delete_intent(
          name='string'
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the intent. The name is case sensitive. 

      

    
    
    :returns: None

  .. py:method:: delete_intent_version(**kwargs)

    

    Deletes a specific version of an intent. To delete all versions of a intent, use the  DeleteIntent operation. 

     

    This operation requires permissions for the ``lex:DeleteIntentVersion`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/DeleteIntentVersion>`_    


    **Request Syntax** 
    ::

      response = client.delete_intent_version(
          name='string',
          version='string'
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the intent.

      

    
    :type version: string
    :param version: **[REQUIRED]** 

      The version of the intent to delete. You cannot delete the ``$LATEST`` version of the intent. To delete the ``$LATEST`` version, use the  DeleteIntent operation.

      

    
    
    :returns: None

  .. py:method:: delete_slot_type(**kwargs)

    

    Deletes all versions of the slot type, including the ``$LATEST`` version. To delete a specific version of the slot type, use the  DeleteSlotTypeVersion operation.

     

    You can delete a version of a slot type only if it is not referenced. To delete a slot type that is referred to in one or more intents, you must remove those references first. 

     

    .. note::

       

      If you get the ``ResourceInUseException`` exception, the exception provides an example reference that shows the intent where the slot type is referenced. To remove the reference to the slot type, either update the intent or delete it. If you get the same exception when you attempt to delete the slot type again, repeat until the slot type has no references and the ``DeleteSlotType`` call is successful. 

       

     

    This operation requires permission for the ``lex:DeleteSlotType`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/DeleteSlotType>`_    


    **Request Syntax** 
    ::

      response = client.delete_slot_type(
          name='string'
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the slot type. The name is case sensitive. 

      

    
    
    :returns: None

  .. py:method:: delete_slot_type_version(**kwargs)

    

    Deletes a specific version of a slot type. To delete all versions of a slot type, use the  DeleteSlotType operation. 

     

    This operation requires permissions for the ``lex:DeleteSlotTypeVersion`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/DeleteSlotTypeVersion>`_    


    **Request Syntax** 
    ::

      response = client.delete_slot_type_version(
          name='string',
          version='string'
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the slot type.

      

    
    :type version: string
    :param version: **[REQUIRED]** 

      The version of the slot type to delete. You cannot delete the ``$LATEST`` version of the slot type. To delete the ``$LATEST`` version, use the  DeleteSlotType operation.

      

    
    
    :returns: None

  .. py:method:: delete_utterances(**kwargs)

    

    Deletes stored utterances.

     

    Amazon Lex stores the utterances that users send to your bot unless the ``childDirected`` field in the bot is set to ``true`` . Utterances are stored for 15 days for use with the  GetUtterancesView operation, and then stored indefinitely for use in improving the ability of your bot to respond to user input.

     

    Use the ``DeleteStoredUtterances`` operation to manually delete stored utterances for a specific user.

     

    This operation requires permissions for the ``lex:DeleteUtterances`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/DeleteUtterances>`_    


    **Request Syntax** 
    ::

      response = client.delete_utterances(
          botName='string',
          userId='string'
      )
    :type botName: string
    :param botName: **[REQUIRED]** 

      The name of the bot that stored the utterances.

      

    
    :type userId: string
    :param userId: **[REQUIRED]** 

      The unique identifier for the user that made the utterances. This is the user ID that was sent in the `PostContent <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostContent.html>`__ or `PostText <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ operation request that contained the utterance.

      

    
    
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


  .. py:method:: get_bot(**kwargs)

    

    Returns metadata information for a specific bot. You must provide the bot name and the bot version or alias. 

     

    This operation requires permissions for the ``lex:GetBot`` action. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetBot>`_    


    **Request Syntax** 
    ::

      response = client.get_bot(
          name='string',
          versionOrAlias='string'
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the bot. The name is case sensitive. 

      

    
    :type versionOrAlias: string
    :param versionOrAlias: **[REQUIRED]** 

      The version or alias of the bot.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'name': 'string',
            'description': 'string',
            'intents': [
                {
                    'intentName': 'string',
                    'intentVersion': 'string'
                },
            ],
            'clarificationPrompt': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML',
                        'content': 'string'
                    },
                ],
                'maxAttempts': 123,
                'responseCard': 'string'
            },
            'abortStatement': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML',
                        'content': 'string'
                    },
                ],
                'responseCard': 'string'
            },
            'status': 'BUILDING'|'READY'|'FAILED'|'NOT_BUILT',
            'failureReason': 'string',
            'lastUpdatedDate': datetime(2015, 1, 1),
            'createdDate': datetime(2015, 1, 1),
            'idleSessionTTLInSeconds': 123,
            'voiceId': 'string',
            'checksum': 'string',
            'version': 'string',
            'locale': 'en-US',
            'childDirected': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **name** *(string) --* 

          The name of the bot.

          
        

        - **description** *(string) --* 

          A description of the bot.

          
        

        - **intents** *(list) --* 

          An array of ``intent`` objects. For more information, see  PutBot .

          
          

          - *(dict) --* 

            Identifies the specific version of an intent.

            
            

            - **intentName** *(string) --* 

              The name of the intent.

              
            

            - **intentVersion** *(string) --* 

              The version of the intent.

              
        
      
        

        - **clarificationPrompt** *(dict) --* 

          The message Amazon Lex uses when it doesn't understand the user's request. For more information, see  PutBot . 

          
          

          - **messages** *(list) --* 

            An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

            
            

            - *(dict) --* 

              The message object that provides the message text and its type.

              
              

              - **contentType** *(string) --* 

                The content type of the message string.

                
              

              - **content** *(string) --* 

                The text of the message.

                
          
        
          

          - **maxAttempts** *(integer) --* 

            The number of times to prompt the user for information.

            
          

          - **responseCard** *(string) --* 

            A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card . 

            
      
        

        - **abortStatement** *(dict) --* 

          The message that Amazon Lex returns when the user elects to end the conversation without completing it. For more information, see  PutBot .

          
          

          - **messages** *(list) --* 

            A collection of message objects.

            
            

            - *(dict) --* 

              The message object that provides the message text and its type.

              
              

              - **contentType** *(string) --* 

                The content type of the message string.

                
              

              - **content** *(string) --* 

                The text of the message.

                
          
        
          

          - **responseCard** *(string) --* 

            At runtime, if the client is using the `PostText <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card. 

            
      
        

        - **status** *(string) --* 

          The status of the bot. If the bot is ready to run, the status is ``READY`` . If there was a problem with building the bot, the status is ``FAILED`` and the ``failureReason`` explains why the bot did not build. If the bot was saved but not built, the status is ``NOT BUILT`` .

          
        

        - **failureReason** *(string) --* 

          If ``status`` is ``FAILED`` , Amazon Lex explains why it failed to build the bot.

          
        

        - **lastUpdatedDate** *(datetime) --* 

          The date that the bot was updated. When you create a resource, the creation date and last updated date are the same. 

          
        

        - **createdDate** *(datetime) --* 

          The date that the bot was created.

          
        

        - **idleSessionTTLInSeconds** *(integer) --* 

          The maximum time in seconds that Amazon Lex retains the data gathered in a conversation. For more information, see  PutBot .

          
        

        - **voiceId** *(string) --* 

          The Amazon Polly voice ID that Amazon Lex uses for voice interaction with the user. For more information, see  PutBot .

          
        

        - **checksum** *(string) --* 

          Checksum of the bot used to identify a specific revision of the bot's ``$LATEST`` version.

          
        

        - **version** *(string) --* 

          The version of the bot. For a new bot, the version is always ``$LATEST`` .

          
        

        - **locale** *(string) --* 

          The target locale for the bot. 

          
        

        - **childDirected** *(boolean) --* 

          For each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to the Children's Online Privacy Protection Act (COPPA) by specifying ``true`` or ``false`` in the ``childDirected`` field. By specifying ``true`` in the ``childDirected`` field, you confirm that your use of Amazon Lex **is** related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. By specifying ``false`` in the ``childDirected`` field, you confirm that your use of Amazon Lex **is not** related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not specify a default value for the ``childDirected`` field that does not accurately reflect whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA.

           

          If your use of Amazon Lex relates to a website, program, or other application that is directed in whole or in part, to children under age 13, you must obtain any required verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in connection with websites, programs, or other applications that are directed or targeted, in whole or in part, to children under age 13, see the `Amazon Lex FAQ. <https://aws.amazon.com/lex/faqs#data-security>`__  

          
    

  .. py:method:: get_bot_alias(**kwargs)

    

    Returns information about an Amazon Lex bot alias. For more information about aliases, see  versioning-aliases .

     

    This operation requires permissions for the ``lex:GetBotAlias`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetBotAlias>`_    


    **Request Syntax** 
    ::

      response = client.get_bot_alias(
          name='string',
          botName='string'
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the bot alias. The name is case sensitive.

      

    
    :type botName: string
    :param botName: **[REQUIRED]** 

      The name of the bot.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'name': 'string',
            'description': 'string',
            'botVersion': 'string',
            'botName': 'string',
            'lastUpdatedDate': datetime(2015, 1, 1),
            'createdDate': datetime(2015, 1, 1),
            'checksum': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **name** *(string) --* 

          The name of the bot alias.

          
        

        - **description** *(string) --* 

          A description of the bot alias.

          
        

        - **botVersion** *(string) --* 

          The version of the bot that the alias points to.

          
        

        - **botName** *(string) --* 

          The name of the bot that the alias points to.

          
        

        - **lastUpdatedDate** *(datetime) --* 

          The date that the bot alias was updated. When you create a resource, the creation date and the last updated date are the same.

          
        

        - **createdDate** *(datetime) --* 

          The date that the bot alias was created.

          
        

        - **checksum** *(string) --* 

          Checksum of the bot alias.

          
    

  .. py:method:: get_bot_aliases(**kwargs)

    

    Returns a list of aliases for a specified Amazon Lex bot.

     

    This operation requires permissions for the ``lex:GetBotAliases`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetBotAliases>`_    


    **Request Syntax** 
    ::

      response = client.get_bot_aliases(
          botName='string',
          nextToken='string',
          maxResults=123,
          nameContains='string'
      )
    :type botName: string
    :param botName: **[REQUIRED]** 

      The name of the bot.

      

    
    :type nextToken: string
    :param nextToken: 

      A pagination token for fetching the next page of aliases. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of aliases, specify the pagination token in the next request. 

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of aliases to return in the response. The default is 50. . 

      

    
    :type nameContains: string
    :param nameContains: 

      Substring to match in bot alias names. An alias will be returned if any part of its name matches the substring. For example, "xyz" matches both "xyzabc" and "abcxyz."

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'BotAliases': [
                {
                    'name': 'string',
                    'description': 'string',
                    'botVersion': 'string',
                    'botName': 'string',
                    'lastUpdatedDate': datetime(2015, 1, 1),
                    'createdDate': datetime(2015, 1, 1),
                    'checksum': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **BotAliases** *(list) --* 

          An array of ``BotAliasMetadata`` objects, each describing a bot alias.

          
          

          - *(dict) --* 

            Provides information about a bot alias.

            
            

            - **name** *(string) --* 

              The name of the bot alias.

              
            

            - **description** *(string) --* 

              A description of the bot alias.

              
            

            - **botVersion** *(string) --* 

              The version of the Amazon Lex bot to which the alias points.

              
            

            - **botName** *(string) --* 

              The name of the bot to which the alias points.

              
            

            - **lastUpdatedDate** *(datetime) --* 

              The date that the bot alias was updated. When you create a resource, the creation date and last updated date are the same.

              
            

            - **createdDate** *(datetime) --* 

              The date that the bot alias was created.

              
            

            - **checksum** *(string) --* 

              Checksum of the bot alias.

              
        
      
        

        - **nextToken** *(string) --* 

          A pagination token for fetching next page of aliases. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of aliases, specify the pagination token in the next request. 

          
    

  .. py:method:: get_bot_channel_association(**kwargs)

    

    Returns information about the association between an Amazon Lex bot and a messaging platform.

     

    This operation requires permissions for the ``lex:GetBotChannelAssociation`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetBotChannelAssociation>`_    


    **Request Syntax** 
    ::

      response = client.get_bot_channel_association(
          name='string',
          botName='string',
          botAlias='string'
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the association between the bot and the channel. The name is case sensitive. 

      

    
    :type botName: string
    :param botName: **[REQUIRED]** 

      The name of the Amazon Lex bot.

      

    
    :type botAlias: string
    :param botAlias: **[REQUIRED]** 

      An alias pointing to the specific version of the Amazon Lex bot to which this association is being made.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'name': 'string',
            'description': 'string',
            'botAlias': 'string',
            'botName': 'string',
            'createdDate': datetime(2015, 1, 1),
            'type': 'Facebook'|'Slack'|'Twilio-Sms',
            'botConfiguration': {
                'string': 'string'
            },
            'status': 'IN_PROGRESS'|'CREATED'|'FAILED',
            'failureReason': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **name** *(string) --* 

          The name of the association between the bot and the channel.

          
        

        - **description** *(string) --* 

          A description of the association between the bot and the channel.

          
        

        - **botAlias** *(string) --* 

          An alias pointing to the specific version of the Amazon Lex bot to which this association is being made.

          
        

        - **botName** *(string) --* 

          The name of the Amazon Lex bot.

          
        

        - **createdDate** *(datetime) --* 

          The date that the association between the bot and the channel was created.

          
        

        - **type** *(string) --* 

          The type of the messaging platform.

          
        

        - **botConfiguration** *(dict) --* 

          Provides information that the messaging platform needs to communicate with the Amazon Lex bot.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **status** *(string) --* 

          The status of the bot channel. 

           

           
          * ``CREATED`` - The channel has been created and is ready for use. 
           
          * ``IN_PROGRESS`` - Channel creation is in progress. 
           
          * ``FAILED`` - There was an error creating the channel. For information about the reason for the failure, see the ``failureReason`` field. 
           

          
        

        - **failureReason** *(string) --* 

          If ``status`` is ``FAILED`` , Amazon Lex provides the reason that it failed to create the association.

          
    

  .. py:method:: get_bot_channel_associations(**kwargs)

    

    Returns a list of all of the channels associated with the specified bot. 

     

    The ``GetBotChannelAssociations`` operation requires permissions for the ``lex:GetBotChannelAssociations`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetBotChannelAssociations>`_    


    **Request Syntax** 
    ::

      response = client.get_bot_channel_associations(
          botName='string',
          botAlias='string',
          nextToken='string',
          maxResults=123,
          nameContains='string'
      )
    :type botName: string
    :param botName: **[REQUIRED]** 

      The name of the Amazon Lex bot in the association.

      

    
    :type botAlias: string
    :param botAlias: **[REQUIRED]** 

      An alias pointing to the specific version of the Amazon Lex bot to which this association is being made.

      

    
    :type nextToken: string
    :param nextToken: 

      A pagination token for fetching the next page of associations. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of associations, specify the pagination token in the next request. 

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of associations to return in the response. The default is 50. 

      

    
    :type nameContains: string
    :param nameContains: 

      Substring to match in channel association names. An association will be returned if any part of its name matches the substring. For example, "xyz" matches both "xyzabc" and "abcxyz." To return all bot channel associations, use a hyphen ("-") as the ``nameContains`` parameter.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'botChannelAssociations': [
                {
                    'name': 'string',
                    'description': 'string',
                    'botAlias': 'string',
                    'botName': 'string',
                    'createdDate': datetime(2015, 1, 1),
                    'type': 'Facebook'|'Slack'|'Twilio-Sms',
                    'botConfiguration': {
                        'string': 'string'
                    },
                    'status': 'IN_PROGRESS'|'CREATED'|'FAILED',
                    'failureReason': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **botChannelAssociations** *(list) --* 

          An array of objects, one for each association, that provides information about the Amazon Lex bot and its association with the channel. 

          
          

          - *(dict) --* 

            Represents an association between an Amazon Lex bot and an external messaging platform.

            
            

            - **name** *(string) --* 

              The name of the association between the bot and the channel. 

              
            

            - **description** *(string) --* 

              A text description of the association you are creating. 

              
            

            - **botAlias** *(string) --* 

              An alias pointing to the specific version of the Amazon Lex bot to which this association is being made. 

              
            

            - **botName** *(string) --* 

              The name of the Amazon Lex bot to which this association is being made. 

               

              .. note::

                 

                Currently, Amazon Lex supports associations with Facebook and Slack, and Twilio.

                 

              
            

            - **createdDate** *(datetime) --* 

              The date that the association between the Amazon Lex bot and the channel was created. 

              
            

            - **type** *(string) --* 

              Specifies the type of association by indicating the type of channel being established between the Amazon Lex bot and the external messaging platform.

              
            

            - **botConfiguration** *(dict) --* 

              Provides information necessary to communicate with the messaging platform. 

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
            

            - **status** *(string) --* 

              The status of the bot channel. 

               

               
              * ``CREATED`` - The channel has been created and is ready for use. 
               
              * ``IN_PROGRESS`` - Channel creation is in progress. 
               
              * ``FAILED`` - There was an error creating the channel. For information about the reason for the failure, see the ``failureReason`` field. 
               

              
            

            - **failureReason** *(string) --* 

              If ``status`` is ``FAILED`` , Amazon Lex provides the reason that it failed to create the association.

              
        
      
        

        - **nextToken** *(string) --* 

          A pagination token that fetches the next page of associations. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of associations, specify the pagination token in the next request. 

          
    

  .. py:method:: get_bot_versions(**kwargs)

    

    Gets information about all of the versions of a bot.

     

    The ``GetBotVersions`` operation returns a ``BotMetadata`` object for each version of a bot. For example, if a bot has three numbered versions, the ``GetBotVersions`` operation returns four ``BotMetadata`` objects in the response, one for each numbered version and one for the ``$LATEST`` version. 

     

    The ``GetBotVersions`` operation always returns at least one version, the ``$LATEST`` version.

     

    This operation requires permissions for the ``lex:GetBotVersions`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetBotVersions>`_    


    **Request Syntax** 
    ::

      response = client.get_bot_versions(
          name='string',
          nextToken='string',
          maxResults=123
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the bot for which versions should be returned.

      

    
    :type nextToken: string
    :param nextToken: 

      A pagination token for fetching the next page of bot versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request. 

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of bot versions to return in the response. The default is 10.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'bots': [
                {
                    'name': 'string',
                    'description': 'string',
                    'status': 'BUILDING'|'READY'|'FAILED'|'NOT_BUILT',
                    'lastUpdatedDate': datetime(2015, 1, 1),
                    'createdDate': datetime(2015, 1, 1),
                    'version': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **bots** *(list) --* 

          An array of ``BotMetadata`` objects, one for each numbered version of the bot plus one for the ``$LATEST`` version.

          
          

          - *(dict) --* 

            Provides information about a bot. .

            
            

            - **name** *(string) --* 

              The name of the bot. 

              
            

            - **description** *(string) --* 

              A description of the bot.

              
            

            - **status** *(string) --* 

              The status of the bot.

              
            

            - **lastUpdatedDate** *(datetime) --* 

              The date that the bot was updated. When you create a bot, the creation date and last updated date are the same. 

              
            

            - **createdDate** *(datetime) --* 

              The date that the bot was created.

              
            

            - **version** *(string) --* 

              The version of the bot. For a new bot, the version is always ``$LATEST`` .

              
        
      
        

        - **nextToken** *(string) --* 

          A pagination token for fetching the next page of bot versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request. 

          
    

  .. py:method:: get_bots(**kwargs)

    

    Returns bot information as follows: 

     

     
    * If you provide the ``nameContains`` field, the response includes information for the ``$LATEST`` version of all bots whose name contains the specified string. 
     
    * If you don't specify the ``nameContains`` field, the operation returns information about the ``$LATEST`` version of all of your bots. 
     

     

    This operation requires permission for the ``lex:GetBots`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetBots>`_    


    **Request Syntax** 
    ::

      response = client.get_bots(
          nextToken='string',
          maxResults=123,
          nameContains='string'
      )
    :type nextToken: string
    :param nextToken: 

      A pagination token that fetches the next page of bots. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of bots, specify the pagination token in the next request. 

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of bots to return in the response that the request will return. The default is 10.

      

    
    :type nameContains: string
    :param nameContains: 

      Substring to match in bot names. A bot will be returned if any part of its name matches the substring. For example, "xyz" matches both "xyzabc" and "abcxyz."

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'bots': [
                {
                    'name': 'string',
                    'description': 'string',
                    'status': 'BUILDING'|'READY'|'FAILED'|'NOT_BUILT',
                    'lastUpdatedDate': datetime(2015, 1, 1),
                    'createdDate': datetime(2015, 1, 1),
                    'version': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **bots** *(list) --* 

          An array of ``botMetadata`` objects, with one entry for each bot. 

          
          

          - *(dict) --* 

            Provides information about a bot. .

            
            

            - **name** *(string) --* 

              The name of the bot. 

              
            

            - **description** *(string) --* 

              A description of the bot.

              
            

            - **status** *(string) --* 

              The status of the bot.

              
            

            - **lastUpdatedDate** *(datetime) --* 

              The date that the bot was updated. When you create a bot, the creation date and last updated date are the same. 

              
            

            - **createdDate** *(datetime) --* 

              The date that the bot was created.

              
            

            - **version** *(string) --* 

              The version of the bot. For a new bot, the version is always ``$LATEST`` .

              
        
      
        

        - **nextToken** *(string) --* 

          If the response is truncated, it includes a pagination token that you can specify in your next request to fetch the next page of bots. 

          
    

  .. py:method:: get_builtin_intent(**kwargs)

    

    Returns information about a built-in intent.

     

    This operation requires permission for the ``lex:GetBuiltinIntent`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetBuiltinIntent>`_    


    **Request Syntax** 
    ::

      response = client.get_builtin_intent(
          signature='string'
      )
    :type signature: string
    :param signature: **[REQUIRED]** 

      The unique identifier for a built-in intent. To find the signature for an intent, see `Standard Built-in Intents <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents>`__ in the *Alexa Skills Kit* .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'signature': 'string',
            'supportedLocales': [
                'en-US',
            ],
            'slots': [
                {
                    'name': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **signature** *(string) --* 

          The unique identifier for a built-in intent.

          
        

        - **supportedLocales** *(list) --* 

          A list of locales that the intent supports.

          
          

          - *(string) --* 
      
        

        - **slots** *(list) --* 

          An array of ``BuiltinIntentSlot`` objects, one entry for each slot type in the intent.

          
          

          - *(dict) --* 

            Provides information about a slot used in a built-in intent.

            
            

            - **name** *(string) --* 

              A list of the slots defined for the intent.

              
        
      
    

  .. py:method:: get_builtin_intents(**kwargs)

    

    Gets a list of built-in intents that meet the specified criteria.

     

    This operation requires permission for the ``lex:GetBuiltinIntents`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetBuiltinIntents>`_    


    **Request Syntax** 
    ::

      response = client.get_builtin_intents(
          locale='en-US',
          signatureContains='string',
          nextToken='string',
          maxResults=123
      )
    :type locale: string
    :param locale: 

      A list of locales that the intent supports.

      

    
    :type signatureContains: string
    :param signatureContains: 

      Substring to match in built-in intent signatures. An intent will be returned if any part of its signature matches the substring. For example, "xyz" matches both "xyzabc" and "abcxyz." To find the signature for an intent, see `Standard Built-in Intents <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents>`__ in the *Alexa Skills Kit* .

      

    
    :type nextToken: string
    :param nextToken: 

      A pagination token that fetches the next page of intents. If this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of intents, use the pagination token in the next request.

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of intents to return in the response. The default is 10.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'intents': [
                {
                    'signature': 'string',
                    'supportedLocales': [
                        'en-US',
                    ]
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **intents** *(list) --* 

          An array of ``builtinIntentMetadata`` objects, one for each intent in the response.

          
          

          - *(dict) --* 

            Provides metadata for a built-in intent.

            
            

            - **signature** *(string) --* 

              A unique identifier for the built-in intent. To find the signature for an intent, see `Standard Built-in Intents <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents>`__ in the *Alexa Skills Kit* .

              
            

            - **supportedLocales** *(list) --* 

              A list of identifiers for the locales that the intent supports.

              
              

              - *(string) --* 
          
        
      
        

        - **nextToken** *(string) --* 

          A pagination token that fetches the next page of intents. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of intents, specify the pagination token in the next request.

          
    

  .. py:method:: get_builtin_slot_types(**kwargs)

    

    Gets a list of built-in slot types that meet the specified criteria.

     

    For a list of built-in slot types, see `Slot Type Reference <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/slot-type-reference>`__ in the *Alexa Skills Kit* .

     

    This operation requires permission for the ``lex:GetBuiltInSlotTypes`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetBuiltinSlotTypes>`_    


    **Request Syntax** 
    ::

      response = client.get_builtin_slot_types(
          locale='en-US',
          signatureContains='string',
          nextToken='string',
          maxResults=123
      )
    :type locale: string
    :param locale: 

      A list of locales that the slot type supports.

      

    
    :type signatureContains: string
    :param signatureContains: 

      Substring to match in built-in slot type signatures. A slot type will be returned if any part of its signature matches the substring. For example, "xyz" matches both "xyzabc" and "abcxyz."

      

    
    :type nextToken: string
    :param nextToken: 

      A pagination token that fetches the next page of slot types. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of slot types, specify the pagination token in the next request.

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of slot types to return in the response. The default is 10.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'slotTypes': [
                {
                    'signature': 'string',
                    'supportedLocales': [
                        'en-US',
                    ]
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **slotTypes** *(list) --* 

          An array of ``BuiltInSlotTypeMetadata`` objects, one entry for each slot type returned.

          
          

          - *(dict) --* 

            Provides information about a built in slot type.

            
            

            - **signature** *(string) --* 

              A unique identifier for the built-in slot type. To find the signature for a slot type, see `Slot Type Reference <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/slot-type-reference>`__ in the *Alexa Skills Kit* .

              
            

            - **supportedLocales** *(list) --* 

              A list of target locales for the slot. 

              
              

              - *(string) --* 
          
        
      
        

        - **nextToken** *(string) --* 

          If the response is truncated, the response includes a pagination token that you can use in your next request to fetch the next page of slot types.

          
    

  .. py:method:: get_export(**kwargs)

    

    Exports the contents of a Amazon Lex resource in a specified format. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetExport>`_    


    **Request Syntax** 
    ::

      response = client.get_export(
          name='string',
          version='string',
          resourceType='BOT',
          exportType='ALEXA_SKILLS_KIT'
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the bot to export.

      

    
    :type version: string
    :param version: **[REQUIRED]** 

      The version of the bot to export.

      

    
    :type resourceType: string
    :param resourceType: **[REQUIRED]** 

      The type of resource to export. 

      

    
    :type exportType: string
    :param exportType: **[REQUIRED]** 

      The format of the exported data.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'name': 'string',
            'version': 'string',
            'resourceType': 'BOT',
            'exportType': 'ALEXA_SKILLS_KIT',
            'exportStatus': 'IN_PROGRESS'|'READY'|'FAILED',
            'failureReason': 'string',
            'url': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **name** *(string) --* 

          The name of the bot being exported.

          
        

        - **version** *(string) --* 

          The version of the bot being exported.

          
        

        - **resourceType** *(string) --* 

          The type of the exported resource.

          
        

        - **exportType** *(string) --* 

          The format of the exported data.

          
        

        - **exportStatus** *(string) --* 

          The status of the export. 

           

           
          * ``IN_PROGRESS`` - The export is in progress. 
           
          * ``READY`` - The export is complete. 
           
          * ``FAILED`` - The export could not be completed. 
           

          
        

        - **failureReason** *(string) --* 

          If ``status`` is ``FAILED`` , Amazon Lex provides the reason that it failed to export the resource.

          
        

        - **url** *(string) --* 

          An S3 pre-signed URL that provides the location of the exported resource. The exported resource is a ZIP archive that contains the exported resource in JSON format. The structure of the archive may change. Your code should not rely on the archive structure.

          
    

  .. py:method:: get_intent(**kwargs)

    

    Returns information about an intent. In addition to the intent name, you must specify the intent version. 

     

    This operation requires permissions to perform the ``lex:GetIntent`` action. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetIntent>`_    


    **Request Syntax** 
    ::

      response = client.get_intent(
          name='string',
          version='string'
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the intent. The name is case sensitive. 

      

    
    :type version: string
    :param version: **[REQUIRED]** 

      The version of the intent.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'name': 'string',
            'description': 'string',
            'slots': [
                {
                    'name': 'string',
                    'description': 'string',
                    'slotConstraint': 'Required'|'Optional',
                    'slotType': 'string',
                    'slotTypeVersion': 'string',
                    'valueElicitationPrompt': {
                        'messages': [
                            {
                                'contentType': 'PlainText'|'SSML',
                                'content': 'string'
                            },
                        ],
                        'maxAttempts': 123,
                        'responseCard': 'string'
                    },
                    'priority': 123,
                    'sampleUtterances': [
                        'string',
                    ],
                    'responseCard': 'string'
                },
            ],
            'sampleUtterances': [
                'string',
            ],
            'confirmationPrompt': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML',
                        'content': 'string'
                    },
                ],
                'maxAttempts': 123,
                'responseCard': 'string'
            },
            'rejectionStatement': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML',
                        'content': 'string'
                    },
                ],
                'responseCard': 'string'
            },
            'followUpPrompt': {
                'prompt': {
                    'messages': [
                        {
                            'contentType': 'PlainText'|'SSML',
                            'content': 'string'
                        },
                    ],
                    'maxAttempts': 123,
                    'responseCard': 'string'
                },
                'rejectionStatement': {
                    'messages': [
                        {
                            'contentType': 'PlainText'|'SSML',
                            'content': 'string'
                        },
                    ],
                    'responseCard': 'string'
                }
            },
            'conclusionStatement': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML',
                        'content': 'string'
                    },
                ],
                'responseCard': 'string'
            },
            'dialogCodeHook': {
                'uri': 'string',
                'messageVersion': 'string'
            },
            'fulfillmentActivity': {
                'type': 'ReturnIntent'|'CodeHook',
                'codeHook': {
                    'uri': 'string',
                    'messageVersion': 'string'
                }
            },
            'parentIntentSignature': 'string',
            'lastUpdatedDate': datetime(2015, 1, 1),
            'createdDate': datetime(2015, 1, 1),
            'version': 'string',
            'checksum': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **name** *(string) --* 

          The name of the intent.

          
        

        - **description** *(string) --* 

          A description of the intent.

          
        

        - **slots** *(list) --* 

          An array of intent slots configured for the intent.

          
          

          - *(dict) --* 

            Identifies the version of a specific slot.

            
            

            - **name** *(string) --* 

              The name of the slot.

              
            

            - **description** *(string) --* 

              A description of the slot.

              
            

            - **slotConstraint** *(string) --* 

              Specifies whether the slot is required or optional. 

              
            

            - **slotType** *(string) --* 

              The type of the slot, either a custom slot type that you defined or one of the built-in slot types.

              
            

            - **slotTypeVersion** *(string) --* 

              The version of the slot type.

              
            

            - **valueElicitationPrompt** *(dict) --* 

              The prompt that Amazon Lex uses to elicit the slot value from the user.

              
              

              - **messages** *(list) --* 

                An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

                
                

                - *(dict) --* 

                  The message object that provides the message text and its type.

                  
                  

                  - **contentType** *(string) --* 

                    The content type of the message string.

                    
                  

                  - **content** *(string) --* 

                    The text of the message.

                    
              
            
              

              - **maxAttempts** *(integer) --* 

                The number of times to prompt the user for information.

                
              

              - **responseCard** *(string) --* 

                A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card . 

                
          
            

            - **priority** *(integer) --* 

              Directs Lex the order in which to elicit this slot value from the user. For example, if the intent has two slots with priorities 1 and 2, AWS Lex first elicits a value for the slot with priority 1.

               

              If multiple slots share the same priority, the order in which Lex elicits values is arbitrary.

              
            

            - **sampleUtterances** *(list) --* 

              If you know a specific pattern with which users might respond to an Amazon Lex request for a slot value, you can provide those utterances to improve accuracy. This is optional. In most cases, Amazon Lex is capable of understanding user utterances. 

              
              

              - *(string) --* 
          
            

            - **responseCard** *(string) --* 

              A set of possible responses for the slot type used by text-based clients. A user chooses an option from the response card, instead of using text to reply. 

              
        
      
        

        - **sampleUtterances** *(list) --* 

          An array of sample utterances configured for the intent.

          
          

          - *(string) --* 
      
        

        - **confirmationPrompt** *(dict) --* 

          If defined in the bot, Amazon Lex uses prompt to confirm the intent before fulfilling the user's request. For more information, see  PutIntent . 

          
          

          - **messages** *(list) --* 

            An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

            
            

            - *(dict) --* 

              The message object that provides the message text and its type.

              
              

              - **contentType** *(string) --* 

                The content type of the message string.

                
              

              - **content** *(string) --* 

                The text of the message.

                
          
        
          

          - **maxAttempts** *(integer) --* 

            The number of times to prompt the user for information.

            
          

          - **responseCard** *(string) --* 

            A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card . 

            
      
        

        - **rejectionStatement** *(dict) --* 

          If the user answers "no" to the question defined in ``confirmationPrompt`` , Amazon Lex responds with this statement to acknowledge that the intent was canceled. 

          
          

          - **messages** *(list) --* 

            A collection of message objects.

            
            

            - *(dict) --* 

              The message object that provides the message text and its type.

              
              

              - **contentType** *(string) --* 

                The content type of the message string.

                
              

              - **content** *(string) --* 

                The text of the message.

                
          
        
          

          - **responseCard** *(string) --* 

            At runtime, if the client is using the `PostText <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card. 

            
      
        

        - **followUpPrompt** *(dict) --* 

          If defined in the bot, Amazon Lex uses this prompt to solicit additional user activity after the intent is fulfilled. For more information, see  PutIntent .

          
          

          - **prompt** *(dict) --* 

            Prompts for information from the user. 

            
            

            - **messages** *(list) --* 

              An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

              
              

              - *(dict) --* 

                The message object that provides the message text and its type.

                
                

                - **contentType** *(string) --* 

                  The content type of the message string.

                  
                

                - **content** *(string) --* 

                  The text of the message.

                  
            
          
            

            - **maxAttempts** *(integer) --* 

              The number of times to prompt the user for information.

              
            

            - **responseCard** *(string) --* 

              A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card . 

              
        
          

          - **rejectionStatement** *(dict) --* 

            If the user answers "no" to the question defined in the ``prompt`` field, Amazon Lex responds with this statement to acknowledge that the intent was canceled. 

            
            

            - **messages** *(list) --* 

              A collection of message objects.

              
              

              - *(dict) --* 

                The message object that provides the message text and its type.

                
                

                - **contentType** *(string) --* 

                  The content type of the message string.

                  
                

                - **content** *(string) --* 

                  The text of the message.

                  
            
          
            

            - **responseCard** *(string) --* 

              At runtime, if the client is using the `PostText <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card. 

              
        
      
        

        - **conclusionStatement** *(dict) --* 

          After the Lambda function specified in the ``fulfillmentActivity`` element fulfills the intent, Amazon Lex conveys this statement to the user.

          
          

          - **messages** *(list) --* 

            A collection of message objects.

            
            

            - *(dict) --* 

              The message object that provides the message text and its type.

              
              

              - **contentType** *(string) --* 

                The content type of the message string.

                
              

              - **content** *(string) --* 

                The text of the message.

                
          
        
          

          - **responseCard** *(string) --* 

            At runtime, if the client is using the `PostText <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card. 

            
      
        

        - **dialogCodeHook** *(dict) --* 

          If defined in the bot, Amazon Amazon Lex invokes this Lambda function for each user input. For more information, see  PutIntent . 

          
          

          - **uri** *(string) --* 

            The Amazon Resource Name (ARN) of the Lambda function.

            
          

          - **messageVersion** *(string) --* 

            The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see  using-lambda .

            
      
        

        - **fulfillmentActivity** *(dict) --* 

          Describes how the intent is fulfilled. For more information, see  PutIntent . 

          
          

          - **type** *(string) --* 

            How the intent should be fulfilled, either by running a Lambda function or by returning the slot data to the client application. 

            
          

          - **codeHook** *(dict) --* 

            A description of the Lambda function that is run to fulfill the intent. 

            
            

            - **uri** *(string) --* 

              The Amazon Resource Name (ARN) of the Lambda function.

              
            

            - **messageVersion** *(string) --* 

              The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see  using-lambda .

              
        
      
        

        - **parentIntentSignature** *(string) --* 

          A unique identifier for a built-in intent.

          
        

        - **lastUpdatedDate** *(datetime) --* 

          The date that the intent was updated. When you create a resource, the creation date and the last updated date are the same. 

          
        

        - **createdDate** *(datetime) --* 

          The date that the intent was created.

          
        

        - **version** *(string) --* 

          The version of the intent.

          
        

        - **checksum** *(string) --* 

          Checksum of the intent.

          
    

  .. py:method:: get_intent_versions(**kwargs)

    

    Gets information about all of the versions of an intent.

     

    The ``GetIntentVersions`` operation returns an ``IntentMetadata`` object for each version of an intent. For example, if an intent has three numbered versions, the ``GetIntentVersions`` operation returns four ``IntentMetadata`` objects in the response, one for each numbered version and one for the ``$LATEST`` version. 

     

    The ``GetIntentVersions`` operation always returns at least one version, the ``$LATEST`` version.

     

    This operation requires permissions for the ``lex:GetIntentVersions`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetIntentVersions>`_    


    **Request Syntax** 
    ::

      response = client.get_intent_versions(
          name='string',
          nextToken='string',
          maxResults=123
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the intent for which versions should be returned.

      

    
    :type nextToken: string
    :param nextToken: 

      A pagination token for fetching the next page of intent versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request. 

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of intent versions to return in the response. The default is 10.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'intents': [
                {
                    'name': 'string',
                    'description': 'string',
                    'lastUpdatedDate': datetime(2015, 1, 1),
                    'createdDate': datetime(2015, 1, 1),
                    'version': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **intents** *(list) --* 

          An array of ``IntentMetadata`` objects, one for each numbered version of the intent plus one for the ``$LATEST`` version.

          
          

          - *(dict) --* 

            Provides information about an intent.

            
            

            - **name** *(string) --* 

              The name of the intent.

              
            

            - **description** *(string) --* 

              A description of the intent.

              
            

            - **lastUpdatedDate** *(datetime) --* 

              The date that the intent was updated. When you create an intent, the creation date and last updated date are the same.

              
            

            - **createdDate** *(datetime) --* 

              The date that the intent was created.

              
            

            - **version** *(string) --* 

              The version of the intent.

              
        
      
        

        - **nextToken** *(string) --* 

          A pagination token for fetching the next page of intent versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request. 

          
    

  .. py:method:: get_intents(**kwargs)

    

    Returns intent information as follows: 

     

     
    * If you specify the ``nameContains`` field, returns the ``$LATEST`` version of all intents that contain the specified string. 
     
    * If you don't specify the ``nameContains`` field, returns information about the ``$LATEST`` version of all intents.  
     

     

    The operation requires permission for the ``lex:GetIntents`` action. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetIntents>`_    


    **Request Syntax** 
    ::

      response = client.get_intents(
          nextToken='string',
          maxResults=123,
          nameContains='string'
      )
    :type nextToken: string
    :param nextToken: 

      A pagination token that fetches the next page of intents. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of intents, specify the pagination token in the next request. 

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of intents to return in the response. The default is 10.

      

    
    :type nameContains: string
    :param nameContains: 

      Substring to match in intent names. An intent will be returned if any part of its name matches the substring. For example, "xyz" matches both "xyzabc" and "abcxyz."

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'intents': [
                {
                    'name': 'string',
                    'description': 'string',
                    'lastUpdatedDate': datetime(2015, 1, 1),
                    'createdDate': datetime(2015, 1, 1),
                    'version': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **intents** *(list) --* 

          An array of ``Intent`` objects. For more information, see  PutBot .

          
          

          - *(dict) --* 

            Provides information about an intent.

            
            

            - **name** *(string) --* 

              The name of the intent.

              
            

            - **description** *(string) --* 

              A description of the intent.

              
            

            - **lastUpdatedDate** *(datetime) --* 

              The date that the intent was updated. When you create an intent, the creation date and last updated date are the same.

              
            

            - **createdDate** *(datetime) --* 

              The date that the intent was created.

              
            

            - **version** *(string) --* 

              The version of the intent.

              
        
      
        

        - **nextToken** *(string) --* 

          If the response is truncated, the response includes a pagination token that you can specify in your next request to fetch the next page of intents. 

          
    

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


  .. py:method:: get_slot_type(**kwargs)

    

    Returns information about a specific version of a slot type. In addition to specifying the slot type name, you must specify the slot type version.

     

    This operation requires permissions for the ``lex:GetSlotType`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetSlotType>`_    


    **Request Syntax** 
    ::

      response = client.get_slot_type(
          name='string',
          version='string'
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the slot type. The name is case sensitive. 

      

    
    :type version: string
    :param version: **[REQUIRED]** 

      The version of the slot type. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'name': 'string',
            'description': 'string',
            'enumerationValues': [
                {
                    'value': 'string',
                    'synonyms': [
                        'string',
                    ]
                },
            ],
            'lastUpdatedDate': datetime(2015, 1, 1),
            'createdDate': datetime(2015, 1, 1),
            'version': 'string',
            'checksum': 'string',
            'valueSelectionStrategy': 'ORIGINAL_VALUE'|'TOP_RESOLUTION'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **name** *(string) --* 

          The name of the slot type.

          
        

        - **description** *(string) --* 

          A description of the slot type.

          
        

        - **enumerationValues** *(list) --* 

          A list of ``EnumerationValue`` objects that defines the values that the slot type can take.

          
          

          - *(dict) --* 

            Each slot type can have a set of values. Each enumeration value represents a value the slot type can take. 

             

            For example, a pizza ordering bot could have a slot type that specifies the type of crust that the pizza should have. The slot type could include the values 

             

             
            * thick 
             
            * thin 
             
            * stuffed 
             

            
            

            - **value** *(string) --* 

              The value of the slot type.

              
            

            - **synonyms** *(list) --* 

              Additional values related to the slot type value.

              
              

              - *(string) --* 
          
        
      
        

        - **lastUpdatedDate** *(datetime) --* 

          The date that the slot type was updated. When you create a resource, the creation date and last update date are the same.

          
        

        - **createdDate** *(datetime) --* 

          The date that the slot type was created.

          
        

        - **version** *(string) --* 

          The version of the slot type.

          
        

        - **checksum** *(string) --* 

          Checksum of the ``$LATEST`` version of the slot type.

          
        

        - **valueSelectionStrategy** *(string) --* 

          The strategy that Amazon Lex uses to determine the value of the slot. For more information, see  PutSlotType .

          
    

  .. py:method:: get_slot_type_versions(**kwargs)

    

    Gets information about all versions of a slot type.

     

    The ``GetSlotTypeVersions`` operation returns a ``SlotTypeMetadata`` object for each version of a slot type. For example, if a slot type has three numbered versions, the ``GetSlotTypeVersions`` operation returns four ``SlotTypeMetadata`` objects in the response, one for each numbered version and one for the ``$LATEST`` version. 

     

    The ``GetSlotTypeVersions`` operation always returns at least one version, the ``$LATEST`` version.

     

    This operation requires permissions for the ``lex:GetSlotTypeVersions`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetSlotTypeVersions>`_    


    **Request Syntax** 
    ::

      response = client.get_slot_type_versions(
          name='string',
          nextToken='string',
          maxResults=123
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the slot type for which versions should be returned.

      

    
    :type nextToken: string
    :param nextToken: 

      A pagination token for fetching the next page of slot type versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request. 

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of slot type versions to return in the response. The default is 10.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'slotTypes': [
                {
                    'name': 'string',
                    'description': 'string',
                    'lastUpdatedDate': datetime(2015, 1, 1),
                    'createdDate': datetime(2015, 1, 1),
                    'version': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **slotTypes** *(list) --* 

          An array of ``SlotTypeMetadata`` objects, one for each numbered version of the slot type plus one for the ``$LATEST`` version.

          
          

          - *(dict) --* 

            Provides information about a slot type..

            
            

            - **name** *(string) --* 

              The name of the slot type.

              
            

            - **description** *(string) --* 

              A description of the slot type.

              
            

            - **lastUpdatedDate** *(datetime) --* 

              The date that the slot type was updated. When you create a resource, the creation date and last updated date are the same. 

              
            

            - **createdDate** *(datetime) --* 

              The date that the slot type was created.

              
            

            - **version** *(string) --* 

              The version of the slot type.

              
        
      
        

        - **nextToken** *(string) --* 

          A pagination token for fetching the next page of slot type versions. If the response to this call is truncated, Amazon Lex returns a pagination token in the response. To fetch the next page of versions, specify the pagination token in the next request. 

          
    

  .. py:method:: get_slot_types(**kwargs)

    

    Returns slot type information as follows: 

     

     
    * If you specify the ``nameContains`` field, returns the ``$LATEST`` version of all slot types that contain the specified string. 
     
    * If you don't specify the ``nameContains`` field, returns information about the ``$LATEST`` version of all slot types.  
     

     

    The operation requires permission for the ``lex:GetSlotTypes`` action. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetSlotTypes>`_    


    **Request Syntax** 
    ::

      response = client.get_slot_types(
          nextToken='string',
          maxResults=123,
          nameContains='string'
      )
    :type nextToken: string
    :param nextToken: 

      A pagination token that fetches the next page of slot types. If the response to this API call is truncated, Amazon Lex returns a pagination token in the response. To fetch next page of slot types, specify the pagination token in the next request.

      

    
    :type maxResults: integer
    :param maxResults: 

      The maximum number of slot types to return in the response. The default is 10.

      

    
    :type nameContains: string
    :param nameContains: 

      Substring to match in slot type names. A slot type will be returned if any part of its name matches the substring. For example, "xyz" matches both "xyzabc" and "abcxyz."

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'slotTypes': [
                {
                    'name': 'string',
                    'description': 'string',
                    'lastUpdatedDate': datetime(2015, 1, 1),
                    'createdDate': datetime(2015, 1, 1),
                    'version': 'string'
                },
            ],
            'nextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **slotTypes** *(list) --* 

          An array of objects, one for each slot type, that provides information such as the name of the slot type, the version, and a description.

          
          

          - *(dict) --* 

            Provides information about a slot type..

            
            

            - **name** *(string) --* 

              The name of the slot type.

              
            

            - **description** *(string) --* 

              A description of the slot type.

              
            

            - **lastUpdatedDate** *(datetime) --* 

              The date that the slot type was updated. When you create a resource, the creation date and last updated date are the same. 

              
            

            - **createdDate** *(datetime) --* 

              The date that the slot type was created.

              
            

            - **version** *(string) --* 

              The version of the slot type.

              
        
      
        

        - **nextToken** *(string) --* 

          If the response is truncated, it includes a pagination token that you can specify in your next request to fetch the next page of slot types.

          
    

  .. py:method:: get_utterances_view(**kwargs)

    

    Use the ``GetUtterancesView`` operation to get information about the utterances that your users have made to your bot. You can use this list to tune the utterances that your bot responds to.

     

    For example, say that you have created a bot to order flowers. After your users have used your bot for a while, use the ``GetUtterancesView`` operation to see the requests that they have made and whether they have been successful. You might find that the utterance "I want flowers" is not being recognized. You could add this utterance to the ``OrderFlowers`` intent so that your bot recognizes that utterance.

     

    After you publish a new version of a bot, you can get information about the old version and the new so that you can compare the performance across the two versions. 

     

    Data is available for the last 15 days. You can request information for up to 5 versions in each request. The response contains information about a maximum of 100 utterances for each version.

     

    If the bot's ``childDirected`` field is set to ``true`` , utterances for the bot are not stored and cannot be retrieved with the ``GetUtterancesView`` operation. For more information, see  PutBot .

     

    This operation requires permissions for the ``lex:GetUtterancesView`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/GetUtterancesView>`_    


    **Request Syntax** 
    ::

      response = client.get_utterances_view(
          botName='string',
          botVersions=[
              'string',
          ],
          statusType='Detected'|'Missed'
      )
    :type botName: string
    :param botName: **[REQUIRED]** 

      The name of the bot for which utterance information should be returned.

      

    
    :type botVersions: list
    :param botVersions: **[REQUIRED]** 

      An array of bot versions for which utterance information should be returned. The limit is 5 versions per request.

      

    
      - *(string) --* 

      
  
    :type statusType: string
    :param statusType: **[REQUIRED]** 

      To return utterances that were recognized and handled, use``Detected`` . To return utterances that were not recognized, use ``Missed`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'botName': 'string',
            'utterances': [
                {
                    'botVersion': 'string',
                    'utterances': [
                        {
                            'utteranceString': 'string',
                            'count': 123,
                            'distinctUsers': 123,
                            'firstUtteredDate': datetime(2015, 1, 1),
                            'lastUtteredDate': datetime(2015, 1, 1)
                        },
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **botName** *(string) --* 

          The name of the bot for which utterance information was returned.

          
        

        - **utterances** *(list) --* 

          An array of  UtteranceList objects, each containing a list of  UtteranceData objects describing the utterances that were processed by your bot. The response contains a maximum of 100 ``UtteranceData`` objects for each version.

          
          

          - *(dict) --* 

            Provides a list of utterances that have been made to a specific version of your bot. The list contains a maximum of 100 utterances.

            
            

            - **botVersion** *(string) --* 

              The version of the bot that processed the list.

              
            

            - **utterances** *(list) --* 

              One or more  UtteranceData objects that contain information about the utterances that have been made to a bot. The maximum number of object is 100.

              
              

              - *(dict) --* 

                Provides information about a single utterance that was made to your bot. 

                
                

                - **utteranceString** *(string) --* 

                  The text that was entered by the user or the text representation of an audio clip.

                  
                

                - **count** *(integer) --* 

                  The number of times that the utterance was processed.

                  
                

                - **distinctUsers** *(integer) --* 

                  The total number of individuals that used the utterance.

                  
                

                - **firstUtteredDate** *(datetime) --* 

                  The date that the utterance was first recorded.

                  
                

                - **lastUtteredDate** *(datetime) --* 

                  The date that the utterance was last recorded.

                  
            
          
        
      
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: put_bot(**kwargs)

    

    Creates an Amazon Lex conversational bot or replaces an existing bot. When you create or update a bot you are only required to specify a name. You can use this to add intents later, or to remove intents from an existing bot. When you create a bot with a name only, the bot is created or updated but Amazon Lex returns the ```` response ``FAILED`` . You can build the bot after you add one or more intents. For more information about Amazon Lex bots, see  how-it-works . 

     

    If you specify the name of an existing bot, the fields in the request replace the existing values in the ``$LATEST`` version of the bot. Amazon Lex removes any fields that you don't provide values for in the request, except for the ``idleTTLInSeconds`` and ``privacySettings`` fields, which are set to their default values. If you don't specify values for required fields, Amazon Lex throws an exception.

     

    This operation requires permissions for the ``lex:PutBot`` action. For more information, see  auth-and-access-control .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/PutBot>`_    


    **Request Syntax** 
    ::

      response = client.put_bot(
          name='string',
          description='string',
          intents=[
              {
                  'intentName': 'string',
                  'intentVersion': 'string'
              },
          ],
          clarificationPrompt={
              'messages': [
                  {
                      'contentType': 'PlainText'|'SSML',
                      'content': 'string'
                  },
              ],
              'maxAttempts': 123,
              'responseCard': 'string'
          },
          abortStatement={
              'messages': [
                  {
                      'contentType': 'PlainText'|'SSML',
                      'content': 'string'
                  },
              ],
              'responseCard': 'string'
          },
          idleSessionTTLInSeconds=123,
          voiceId='string',
          checksum='string',
          processBehavior='SAVE'|'BUILD',
          locale='en-US',
          childDirected=True|False
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the bot. The name is *not* case sensitive. 

      

    
    :type description: string
    :param description: 

      A description of the bot.

      

    
    :type intents: list
    :param intents: 

      An array of ``Intent`` objects. Each intent represents a command that a user can express. For example, a pizza ordering bot might support an OrderPizza intent. For more information, see  how-it-works .

      

    
      - *(dict) --* 

        Identifies the specific version of an intent.

        

      
        - **intentName** *(string) --* **[REQUIRED]** 

          The name of the intent.

          

        
        - **intentVersion** *(string) --* **[REQUIRED]** 

          The version of the intent.

          

        
      
  
    :type clarificationPrompt: dict
    :param clarificationPrompt: 

      When Amazon Lex doesn't understand the user's intent, it uses this message to get clarification. To specify how many times Amazon Lex should repeate the clarification prompt, use the ``maxAttempts`` field. If Amazon Lex still doesn't understand, it sends the message in the ``abortStatement`` field. 

       

      When you create a clarification prompt, make sure that it suggests the correct response from the user. for example, for a bot that orders pizza and drinks, you might create this clarification prompt: "What would you like to do? You can say 'Order a pizza' or 'Order a drink.'"

      

    
      - **messages** *(list) --* **[REQUIRED]** 

        An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

        

      
        - *(dict) --* 

          The message object that provides the message text and its type.

          

        
          - **contentType** *(string) --* **[REQUIRED]** 

            The content type of the message string.

            

          
          - **content** *(string) --* **[REQUIRED]** 

            The text of the message.

            

          
        
    
      - **maxAttempts** *(integer) --* **[REQUIRED]** 

        The number of times to prompt the user for information.

        

      
      - **responseCard** *(string) --* 

        A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card . 

        

      
    
    :type abortStatement: dict
    :param abortStatement: 

      When Amazon Lex can't understand the user's input in context, it tries to elicit the information a few times. After that, Amazon Lex sends the message defined in ``abortStatement`` to the user, and then aborts the conversation. To set the number of retries, use the ``valueElicitationPrompt`` field for the slot type. 

       

      For example, in a pizza ordering bot, Amazon Lex might ask a user "What type of crust would you like?" If the user's response is not one of the expected responses (for example, "thin crust, "deep dish," etc.), Amazon Lex tries to elicit a correct response a few more times. 

       

      For example, in a pizza ordering application, ``OrderPizza`` might be one of the intents. This intent might require the ``CrustType`` slot. You specify the ``valueElicitationPrompt`` field when you create the ``CrustType`` slot.

      

    
      - **messages** *(list) --* **[REQUIRED]** 

        A collection of message objects.

        

      
        - *(dict) --* 

          The message object that provides the message text and its type.

          

        
          - **contentType** *(string) --* **[REQUIRED]** 

            The content type of the message string.

            

          
          - **content** *(string) --* **[REQUIRED]** 

            The text of the message.

            

          
        
    
      - **responseCard** *(string) --* 

        At runtime, if the client is using the `PostText <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card. 

        

      
    
    :type idleSessionTTLInSeconds: integer
    :param idleSessionTTLInSeconds: 

      The maximum time in seconds that Amazon Lex retains the data gathered in a conversation.

       

      A user interaction session remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Lex deletes any data provided before the timeout.

       

      For example, suppose that a user chooses the OrderPizza intent, but gets sidetracked halfway through placing an order. If the user doesn't complete the order within the specified time, Amazon Lex discards the slot information that it gathered, and the user must start over.

       

      If you don't include the ``idleSessionTTLInSeconds`` element in a ``PutBot`` operation request, Amazon Lex uses the default value. This is also true if the request replaces an existing bot.

       

      The default is 300 seconds (5 minutes).

      

    
    :type voiceId: string
    :param voiceId: 

      The Amazon Polly voice ID that you want Amazon Lex to use for voice interactions with the user. The locale configured for the voice must match the locale of the bot. For more information, see `Available Voices <http://docs.aws.amazon.com/polly/latest/dg/voicelist.html>`__ in the *Amazon Polly Developer Guide* .

      

    
    :type checksum: string
    :param checksum: 

      Identifies a specific revision of the ``$LATEST`` version.

       

      When you create a new bot, leave the ``checksum`` field blank. If you specify a checksum you get a ``BadRequestException`` exception.

       

      When you want to update a bot, set the ``checksum`` field to the checksum of the most recent revision of the ``$LATEST`` version. If you don't specify the ``checksum`` field, or if the checksum does not match the ``$LATEST`` version, you get a ``PreconditionFailedException`` exception.

      

    
    :type processBehavior: string
    :param processBehavior: 

      If you set the ``processBehavior`` element to ``Build`` , Amazon Lex builds the bot so that it can be run. If you set the element to ``Save`` Amazon Lex saves the bot, but doesn't build it. 

       

      If you don't specify this value, the default value is ``Save`` .

      

    
    :type locale: string
    :param locale: **[REQUIRED]** 

      Specifies the target locale for the bot. Any intent used in the bot must be compatible with the locale of the bot. 

       

      The default is ``en-US`` .

      

    
    :type childDirected: boolean
    :param childDirected: **[REQUIRED]** 

      For each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to the Children's Online Privacy Protection Act (COPPA) by specifying ``true`` or ``false`` in the ``childDirected`` field. By specifying ``true`` in the ``childDirected`` field, you confirm that your use of Amazon Lex **is** related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. By specifying ``false`` in the ``childDirected`` field, you confirm that your use of Amazon Lex **is not** related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not specify a default value for the ``childDirected`` field that does not accurately reflect whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA.

       

      If your use of Amazon Lex relates to a website, program, or other application that is directed in whole or in part, to children under age 13, you must obtain any required verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in connection with websites, programs, or other applications that are directed or targeted, in whole or in part, to children under age 13, see the `Amazon Lex FAQ. <https://aws.amazon.com/lex/faqs#data-security>`__  

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'name': 'string',
            'description': 'string',
            'intents': [
                {
                    'intentName': 'string',
                    'intentVersion': 'string'
                },
            ],
            'clarificationPrompt': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML',
                        'content': 'string'
                    },
                ],
                'maxAttempts': 123,
                'responseCard': 'string'
            },
            'abortStatement': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML',
                        'content': 'string'
                    },
                ],
                'responseCard': 'string'
            },
            'status': 'BUILDING'|'READY'|'FAILED'|'NOT_BUILT',
            'failureReason': 'string',
            'lastUpdatedDate': datetime(2015, 1, 1),
            'createdDate': datetime(2015, 1, 1),
            'idleSessionTTLInSeconds': 123,
            'voiceId': 'string',
            'checksum': 'string',
            'version': 'string',
            'locale': 'en-US',
            'childDirected': True|False
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **name** *(string) --* 

          The name of the bot.

          
        

        - **description** *(string) --* 

          A description of the bot.

          
        

        - **intents** *(list) --* 

          An array of ``Intent`` objects. For more information, see  PutBot .

          
          

          - *(dict) --* 

            Identifies the specific version of an intent.

            
            

            - **intentName** *(string) --* 

              The name of the intent.

              
            

            - **intentVersion** *(string) --* 

              The version of the intent.

              
        
      
        

        - **clarificationPrompt** *(dict) --* 

          The prompts that Amazon Lex uses when it doesn't understand the user's intent. For more information, see  PutBot . 

          
          

          - **messages** *(list) --* 

            An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

            
            

            - *(dict) --* 

              The message object that provides the message text and its type.

              
              

              - **contentType** *(string) --* 

                The content type of the message string.

                
              

              - **content** *(string) --* 

                The text of the message.

                
          
        
          

          - **maxAttempts** *(integer) --* 

            The number of times to prompt the user for information.

            
          

          - **responseCard** *(string) --* 

            A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card . 

            
      
        

        - **abortStatement** *(dict) --* 

          The message that Amazon Lex uses to abort a conversation. For more information, see  PutBot .

          
          

          - **messages** *(list) --* 

            A collection of message objects.

            
            

            - *(dict) --* 

              The message object that provides the message text and its type.

              
              

              - **contentType** *(string) --* 

                The content type of the message string.

                
              

              - **content** *(string) --* 

                The text of the message.

                
          
        
          

          - **responseCard** *(string) --* 

            At runtime, if the client is using the `PostText <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card. 

            
      
        

        - **status** *(string) --* 

          When you send a request to create a bot with ``processBehavior`` set to ``BUILD`` , Amazon Lex sets the ``status`` response element to ``BUILDING`` . After Amazon Lex builds the bot, it sets ``status`` to ``READY`` . If Amazon Lex can't build the bot, Amazon Lex sets ``status`` to ``FAILED`` . Amazon Lex returns the reason for the failure in the ``failureReason`` response element. 

           

          When you set ``processBehavior`` to ``SAVE`` , Amazon Lex sets the status code to ``NOT BUILT`` .

          
        

        - **failureReason** *(string) --* 

          If ``status`` is ``FAILED`` , Amazon Lex provides the reason that it failed to build the bot.

          
        

        - **lastUpdatedDate** *(datetime) --* 

          The date that the bot was updated. When you create a resource, the creation date and last updated date are the same.

          
        

        - **createdDate** *(datetime) --* 

          The date that the bot was created.

          
        

        - **idleSessionTTLInSeconds** *(integer) --* 

          The maximum length of time that Amazon Lex retains the data gathered in a conversation. For more information, see  PutBot .

          
        

        - **voiceId** *(string) --* 

          The Amazon Polly voice ID that Amazon Lex uses for voice interaction with the user. For more information, see  PutBot .

          
        

        - **checksum** *(string) --* 

          Checksum of the bot that you created.

          
        

        - **version** *(string) --* 

          The version of the bot. For a new bot, the version is always ``$LATEST`` .

          
        

        - **locale** *(string) --* 

          The target locale for the bot. 

          
        

        - **childDirected** *(boolean) --* 

          For each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to the Children's Online Privacy Protection Act (COPPA) by specifying ``true`` or ``false`` in the ``childDirected`` field. By specifying ``true`` in the ``childDirected`` field, you confirm that your use of Amazon Lex **is** related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. By specifying ``false`` in the ``childDirected`` field, you confirm that your use of Amazon Lex **is not** related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not specify a default value for the ``childDirected`` field that does not accurately reflect whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA.

           

          If your use of Amazon Lex relates to a website, program, or other application that is directed in whole or in part, to children under age 13, you must obtain any required verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in connection with websites, programs, or other applications that are directed or targeted, in whole or in part, to children under age 13, see the `Amazon Lex FAQ. <https://aws.amazon.com/lex/faqs#data-security>`__  

          
    

  .. py:method:: put_bot_alias(**kwargs)

    

    Creates an alias for the specified version of the bot or replaces an alias for the specified bot. To change the version of the bot that the alias points to, replace the alias. For more information about aliases, see  versioning-aliases .

     

    This operation requires permissions for the ``lex:PutBotAlias`` action. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/PutBotAlias>`_    


    **Request Syntax** 
    ::

      response = client.put_bot_alias(
          name='string',
          description='string',
          botVersion='string',
          botName='string',
          checksum='string'
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the alias. The name is *not* case sensitive.

      

    
    :type description: string
    :param description: 

      A description of the alias.

      

    
    :type botVersion: string
    :param botVersion: **[REQUIRED]** 

      The version of the bot.

      

    
    :type botName: string
    :param botName: **[REQUIRED]** 

      The name of the bot.

      

    
    :type checksum: string
    :param checksum: 

      Identifies a specific revision of the ``$LATEST`` version.

       

      When you create a new bot alias, leave the ``checksum`` field blank. If you specify a checksum you get a ``BadRequestException`` exception.

       

      When you want to update a bot alias, set the ``checksum`` field to the checksum of the most recent revision of the ``$LATEST`` version. If you don't specify the ``checksum`` field, or if the checksum does not match the ``$LATEST`` version, you get a ``PreconditionFailedException`` exception.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'name': 'string',
            'description': 'string',
            'botVersion': 'string',
            'botName': 'string',
            'lastUpdatedDate': datetime(2015, 1, 1),
            'createdDate': datetime(2015, 1, 1),
            'checksum': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **name** *(string) --* 

          The name of the alias.

          
        

        - **description** *(string) --* 

          A description of the alias.

          
        

        - **botVersion** *(string) --* 

          The version of the bot that the alias points to.

          
        

        - **botName** *(string) --* 

          The name of the bot that the alias points to.

          
        

        - **lastUpdatedDate** *(datetime) --* 

          The date that the bot alias was updated. When you create a resource, the creation date and the last updated date are the same.

          
        

        - **createdDate** *(datetime) --* 

          The date that the bot alias was created.

          
        

        - **checksum** *(string) --* 

          The checksum for the current version of the alias.

          
    

  .. py:method:: put_intent(**kwargs)

    

    Creates an intent or replaces an existing intent.

     

    To define the interaction between the user and your bot, you use one or more intents. For a pizza ordering bot, for example, you would create an ``OrderPizza`` intent. 

     

    To create an intent or replace an existing intent, you must provide the following:

     

     
    * Intent name. For example, ``OrderPizza`` . 
     
    * Sample utterances. For example, "Can I order a pizza, please." and "I want to order a pizza." 
     
    * Information to be gathered. You specify slot types for the information that your bot will request from the user. You can specify standard slot types, such as a date or a time, or custom slot types such as the size and crust of a pizza. 
     
    * How the intent will be fulfilled. You can provide a Lambda function or configure the intent to return the intent information to the client application. If you use a Lambda function, when all of the intent information is available, Amazon Lex invokes your Lambda function. If you configure your intent to return the intent information to the client application.  
     

     

    You can specify other optional information in the request, such as:

     

     
    * A confirmation prompt to ask the user to confirm an intent. For example, "Shall I order your pizza?" 
     
    * A conclusion statement to send to the user after the intent has been fulfilled. For example, "I placed your pizza order." 
     
    * A follow-up prompt that asks the user for additional activity. For example, asking "Do you want to order a drink with your pizza?" 
     

     

    If you specify an existing intent name to update the intent, Amazon Lex replaces the values in the ``$LATEST`` version of the intent with the values in the request. Amazon Lex removes fields that you don't provide in the request. If you don't specify the required fields, Amazon Lex throws an exception. When you update the ``$LATEST`` version of an intent, the ``status`` field of any bot that uses the ``$LATEST`` version of the intent is set to ``NOT_BUILT`` .

     

    For more information, see  how-it-works .

     

    This operation requires permissions for the ``lex:PutIntent`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/PutIntent>`_    


    **Request Syntax** 
    ::

      response = client.put_intent(
          name='string',
          description='string',
          slots=[
              {
                  'name': 'string',
                  'description': 'string',
                  'slotConstraint': 'Required'|'Optional',
                  'slotType': 'string',
                  'slotTypeVersion': 'string',
                  'valueElicitationPrompt': {
                      'messages': [
                          {
                              'contentType': 'PlainText'|'SSML',
                              'content': 'string'
                          },
                      ],
                      'maxAttempts': 123,
                      'responseCard': 'string'
                  },
                  'priority': 123,
                  'sampleUtterances': [
                      'string',
                  ],
                  'responseCard': 'string'
              },
          ],
          sampleUtterances=[
              'string',
          ],
          confirmationPrompt={
              'messages': [
                  {
                      'contentType': 'PlainText'|'SSML',
                      'content': 'string'
                  },
              ],
              'maxAttempts': 123,
              'responseCard': 'string'
          },
          rejectionStatement={
              'messages': [
                  {
                      'contentType': 'PlainText'|'SSML',
                      'content': 'string'
                  },
              ],
              'responseCard': 'string'
          },
          followUpPrompt={
              'prompt': {
                  'messages': [
                      {
                          'contentType': 'PlainText'|'SSML',
                          'content': 'string'
                      },
                  ],
                  'maxAttempts': 123,
                  'responseCard': 'string'
              },
              'rejectionStatement': {
                  'messages': [
                      {
                          'contentType': 'PlainText'|'SSML',
                          'content': 'string'
                      },
                  ],
                  'responseCard': 'string'
              }
          },
          conclusionStatement={
              'messages': [
                  {
                      'contentType': 'PlainText'|'SSML',
                      'content': 'string'
                  },
              ],
              'responseCard': 'string'
          },
          dialogCodeHook={
              'uri': 'string',
              'messageVersion': 'string'
          },
          fulfillmentActivity={
              'type': 'ReturnIntent'|'CodeHook',
              'codeHook': {
                  'uri': 'string',
                  'messageVersion': 'string'
              }
          },
          parentIntentSignature='string',
          checksum='string'
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the intent. The name is *not* case sensitive. 

       

      The name can't match a built-in intent name, or a built-in intent name with "AMAZON." removed. For example, because there is a built-in intent called ``AMAZON.HelpIntent`` , you can't create a custom intent called ``HelpIntent`` .

       

      For a list of built-in intents, see `Standard Built-in Intents <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents>`__ in the *Alexa Skills Kit* .

      

    
    :type description: string
    :param description: 

      A description of the intent.

      

    
    :type slots: list
    :param slots: 

      An array of intent slots. At runtime, Amazon Lex elicits required slot values from the user using prompts defined in the slots. For more information, see  how-it-works . 

      

    
      - *(dict) --* 

        Identifies the version of a specific slot.

        

      
        - **name** *(string) --* **[REQUIRED]** 

          The name of the slot.

          

        
        - **description** *(string) --* 

          A description of the slot.

          

        
        - **slotConstraint** *(string) --* **[REQUIRED]** 

          Specifies whether the slot is required or optional. 

          

        
        - **slotType** *(string) --* 

          The type of the slot, either a custom slot type that you defined or one of the built-in slot types.

          

        
        - **slotTypeVersion** *(string) --* 

          The version of the slot type.

          

        
        - **valueElicitationPrompt** *(dict) --* 

          The prompt that Amazon Lex uses to elicit the slot value from the user.

          

        
          - **messages** *(list) --* **[REQUIRED]** 

            An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

            

          
            - *(dict) --* 

              The message object that provides the message text and its type.

              

            
              - **contentType** *(string) --* **[REQUIRED]** 

                The content type of the message string.

                

              
              - **content** *(string) --* **[REQUIRED]** 

                The text of the message.

                

              
            
        
          - **maxAttempts** *(integer) --* **[REQUIRED]** 

            The number of times to prompt the user for information.

            

          
          - **responseCard** *(string) --* 

            A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card . 

            

          
        
        - **priority** *(integer) --* 

          Directs Lex the order in which to elicit this slot value from the user. For example, if the intent has two slots with priorities 1 and 2, AWS Lex first elicits a value for the slot with priority 1.

           

          If multiple slots share the same priority, the order in which Lex elicits values is arbitrary.

          

        
        - **sampleUtterances** *(list) --* 

          If you know a specific pattern with which users might respond to an Amazon Lex request for a slot value, you can provide those utterances to improve accuracy. This is optional. In most cases, Amazon Lex is capable of understanding user utterances. 

          

        
          - *(string) --* 

          
      
        - **responseCard** *(string) --* 

          A set of possible responses for the slot type used by text-based clients. A user chooses an option from the response card, instead of using text to reply. 

          

        
      
  
    :type sampleUtterances: list
    :param sampleUtterances: 

      An array of utterances (strings) that a user might say to signal the intent. For example, "I want {PizzaSize} pizza", "Order {Quantity} {PizzaSize} pizzas". 

       

      In each utterance, a slot name is enclosed in curly braces. 

      

    
      - *(string) --* 

      
  
    :type confirmationPrompt: dict
    :param confirmationPrompt: 

      Prompts the user to confirm the intent. This question should have a yes or no answer.

       

      Amazon Lex uses this prompt to ensure that the user acknowledges that the intent is ready for fulfillment. For example, with the ``OrderPizza`` intent, you might want to confirm that the order is correct before placing it. For other intents, such as intents that simply respond to user questions, you might not need to ask the user for confirmation before providing the information. 

       

      .. note::

         

        You you must provide both the ``rejectionStatement`` and the ``confirmationPrompt`` , or neither.

         

      

    
      - **messages** *(list) --* **[REQUIRED]** 

        An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

        

      
        - *(dict) --* 

          The message object that provides the message text and its type.

          

        
          - **contentType** *(string) --* **[REQUIRED]** 

            The content type of the message string.

            

          
          - **content** *(string) --* **[REQUIRED]** 

            The text of the message.

            

          
        
    
      - **maxAttempts** *(integer) --* **[REQUIRED]** 

        The number of times to prompt the user for information.

        

      
      - **responseCard** *(string) --* 

        A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card . 

        

      
    
    :type rejectionStatement: dict
    :param rejectionStatement: 

      When the user answers "no" to the question defined in ``confirmationPrompt`` , Amazon Lex responds with this statement to acknowledge that the intent was canceled. 

       

      .. note::

         

        You must provide both the ``rejectionStatement`` and the ``confirmationPrompt`` , or neither.

         

      

    
      - **messages** *(list) --* **[REQUIRED]** 

        A collection of message objects.

        

      
        - *(dict) --* 

          The message object that provides the message text and its type.

          

        
          - **contentType** *(string) --* **[REQUIRED]** 

            The content type of the message string.

            

          
          - **content** *(string) --* **[REQUIRED]** 

            The text of the message.

            

          
        
    
      - **responseCard** *(string) --* 

        At runtime, if the client is using the `PostText <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card. 

        

      
    
    :type followUpPrompt: dict
    :param followUpPrompt: 

      Amazon Lex uses this prompt to solicit additional activity after fulfilling an intent. For example, after the ``OrderPizza`` intent is fulfilled, you might prompt the user to order a drink.

       

      The action that Amazon Lex takes depends on the user's response, as follows:

       

       
      * If the user says "Yes" it responds with the clarification prompt that is configured for the bot. 
       
      * if the user says "Yes" and continues with an utterance that triggers an intent it starts a conversation for the intent. 
       
      * If the user says "No" it responds with the rejection statement configured for the the follow-up prompt. 
       
      * If it doesn't recognize the utterance it repeats the follow-up prompt again. 
       

       

      The ``followUpPrompt`` field and the ``conclusionStatement`` field are mutually exclusive. You can specify only one. 

      

    
      - **prompt** *(dict) --* **[REQUIRED]** 

        Prompts for information from the user. 

        

      
        - **messages** *(list) --* **[REQUIRED]** 

          An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

          

        
          - *(dict) --* 

            The message object that provides the message text and its type.

            

          
            - **contentType** *(string) --* **[REQUIRED]** 

              The content type of the message string.

              

            
            - **content** *(string) --* **[REQUIRED]** 

              The text of the message.

              

            
          
      
        - **maxAttempts** *(integer) --* **[REQUIRED]** 

          The number of times to prompt the user for information.

          

        
        - **responseCard** *(string) --* 

          A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card . 

          

        
      
      - **rejectionStatement** *(dict) --* **[REQUIRED]** 

        If the user answers "no" to the question defined in the ``prompt`` field, Amazon Lex responds with this statement to acknowledge that the intent was canceled. 

        

      
        - **messages** *(list) --* **[REQUIRED]** 

          A collection of message objects.

          

        
          - *(dict) --* 

            The message object that provides the message text and its type.

            

          
            - **contentType** *(string) --* **[REQUIRED]** 

              The content type of the message string.

              

            
            - **content** *(string) --* **[REQUIRED]** 

              The text of the message.

              

            
          
      
        - **responseCard** *(string) --* 

          At runtime, if the client is using the `PostText <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card. 

          

        
      
    
    :type conclusionStatement: dict
    :param conclusionStatement: 

      The statement that you want Amazon Lex to convey to the user after the intent is successfully fulfilled by the Lambda function. 

       

      This element is relevant only if you provide a Lambda function in the ``fulfillmentActivity`` . If you return the intent to the client application, you can't specify this element.

       

      .. note::

         

        The ``followUpPrompt`` and ``conclusionStatement`` are mutually exclusive. You can specify only one.

         

      

    
      - **messages** *(list) --* **[REQUIRED]** 

        A collection of message objects.

        

      
        - *(dict) --* 

          The message object that provides the message text and its type.

          

        
          - **contentType** *(string) --* **[REQUIRED]** 

            The content type of the message string.

            

          
          - **content** *(string) --* **[REQUIRED]** 

            The text of the message.

            

          
        
    
      - **responseCard** *(string) --* 

        At runtime, if the client is using the `PostText <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card. 

        

      
    
    :type dialogCodeHook: dict
    :param dialogCodeHook: 

      Specifies a Lambda function to invoke for each user input. You can invoke this Lambda function to personalize user interaction. 

       

      For example, suppose your bot determines that the user is John. Your Lambda function might retrieve John's information from a backend database and prepopulate some of the values. For example, if you find that John is gluten intolerant, you might set the corresponding intent slot, ``GlutenIntolerant`` , to true. You might find John's phone number and set the corresponding session attribute. 

      

    
      - **uri** *(string) --* **[REQUIRED]** 

        The Amazon Resource Name (ARN) of the Lambda function.

        

      
      - **messageVersion** *(string) --* **[REQUIRED]** 

        The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see  using-lambda .

        

      
    
    :type fulfillmentActivity: dict
    :param fulfillmentActivity: 

      Required. Describes how the intent is fulfilled. For example, after a user provides all of the information for a pizza order, ``fulfillmentActivity`` defines how the bot places an order with a local pizza store. 

       

      You might configure Amazon Lex to return all of the intent information to the client application, or direct it to invoke a Lambda function that can process the intent (for example, place an order with a pizzeria). 

      

    
      - **type** *(string) --* **[REQUIRED]** 

        How the intent should be fulfilled, either by running a Lambda function or by returning the slot data to the client application. 

        

      
      - **codeHook** *(dict) --* 

        A description of the Lambda function that is run to fulfill the intent. 

        

      
        - **uri** *(string) --* **[REQUIRED]** 

          The Amazon Resource Name (ARN) of the Lambda function.

          

        
        - **messageVersion** *(string) --* **[REQUIRED]** 

          The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see  using-lambda .

          

        
      
    
    :type parentIntentSignature: string
    :param parentIntentSignature: 

      A unique identifier for the built-in intent to base this intent on. To find the signature for an intent, see `Standard Built-in Intents <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents>`__ in the *Alexa Skills Kit* .

      

    
    :type checksum: string
    :param checksum: 

      Identifies a specific revision of the ``$LATEST`` version.

       

      When you create a new intent, leave the ``checksum`` field blank. If you specify a checksum you get a ``BadRequestException`` exception.

       

      When you want to update a intent, set the ``checksum`` field to the checksum of the most recent revision of the ``$LATEST`` version. If you don't specify the ``checksum`` field, or if the checksum does not match the ``$LATEST`` version, you get a ``PreconditionFailedException`` exception.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'name': 'string',
            'description': 'string',
            'slots': [
                {
                    'name': 'string',
                    'description': 'string',
                    'slotConstraint': 'Required'|'Optional',
                    'slotType': 'string',
                    'slotTypeVersion': 'string',
                    'valueElicitationPrompt': {
                        'messages': [
                            {
                                'contentType': 'PlainText'|'SSML',
                                'content': 'string'
                            },
                        ],
                        'maxAttempts': 123,
                        'responseCard': 'string'
                    },
                    'priority': 123,
                    'sampleUtterances': [
                        'string',
                    ],
                    'responseCard': 'string'
                },
            ],
            'sampleUtterances': [
                'string',
            ],
            'confirmationPrompt': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML',
                        'content': 'string'
                    },
                ],
                'maxAttempts': 123,
                'responseCard': 'string'
            },
            'rejectionStatement': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML',
                        'content': 'string'
                    },
                ],
                'responseCard': 'string'
            },
            'followUpPrompt': {
                'prompt': {
                    'messages': [
                        {
                            'contentType': 'PlainText'|'SSML',
                            'content': 'string'
                        },
                    ],
                    'maxAttempts': 123,
                    'responseCard': 'string'
                },
                'rejectionStatement': {
                    'messages': [
                        {
                            'contentType': 'PlainText'|'SSML',
                            'content': 'string'
                        },
                    ],
                    'responseCard': 'string'
                }
            },
            'conclusionStatement': {
                'messages': [
                    {
                        'contentType': 'PlainText'|'SSML',
                        'content': 'string'
                    },
                ],
                'responseCard': 'string'
            },
            'dialogCodeHook': {
                'uri': 'string',
                'messageVersion': 'string'
            },
            'fulfillmentActivity': {
                'type': 'ReturnIntent'|'CodeHook',
                'codeHook': {
                    'uri': 'string',
                    'messageVersion': 'string'
                }
            },
            'parentIntentSignature': 'string',
            'lastUpdatedDate': datetime(2015, 1, 1),
            'createdDate': datetime(2015, 1, 1),
            'version': 'string',
            'checksum': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **name** *(string) --* 

          The name of the intent.

          
        

        - **description** *(string) --* 

          A description of the intent.

          
        

        - **slots** *(list) --* 

          An array of intent slots that are configured for the intent.

          
          

          - *(dict) --* 

            Identifies the version of a specific slot.

            
            

            - **name** *(string) --* 

              The name of the slot.

              
            

            - **description** *(string) --* 

              A description of the slot.

              
            

            - **slotConstraint** *(string) --* 

              Specifies whether the slot is required or optional. 

              
            

            - **slotType** *(string) --* 

              The type of the slot, either a custom slot type that you defined or one of the built-in slot types.

              
            

            - **slotTypeVersion** *(string) --* 

              The version of the slot type.

              
            

            - **valueElicitationPrompt** *(dict) --* 

              The prompt that Amazon Lex uses to elicit the slot value from the user.

              
              

              - **messages** *(list) --* 

                An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

                
                

                - *(dict) --* 

                  The message object that provides the message text and its type.

                  
                  

                  - **contentType** *(string) --* 

                    The content type of the message string.

                    
                  

                  - **content** *(string) --* 

                    The text of the message.

                    
              
            
              

              - **maxAttempts** *(integer) --* 

                The number of times to prompt the user for information.

                
              

              - **responseCard** *(string) --* 

                A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card . 

                
          
            

            - **priority** *(integer) --* 

              Directs Lex the order in which to elicit this slot value from the user. For example, if the intent has two slots with priorities 1 and 2, AWS Lex first elicits a value for the slot with priority 1.

               

              If multiple slots share the same priority, the order in which Lex elicits values is arbitrary.

              
            

            - **sampleUtterances** *(list) --* 

              If you know a specific pattern with which users might respond to an Amazon Lex request for a slot value, you can provide those utterances to improve accuracy. This is optional. In most cases, Amazon Lex is capable of understanding user utterances. 

              
              

              - *(string) --* 
          
            

            - **responseCard** *(string) --* 

              A set of possible responses for the slot type used by text-based clients. A user chooses an option from the response card, instead of using text to reply. 

              
        
      
        

        - **sampleUtterances** *(list) --* 

          An array of sample utterances that are configured for the intent. 

          
          

          - *(string) --* 
      
        

        - **confirmationPrompt** *(dict) --* 

          If defined in the intent, Amazon Lex prompts the user to confirm the intent before fulfilling it.

          
          

          - **messages** *(list) --* 

            An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

            
            

            - *(dict) --* 

              The message object that provides the message text and its type.

              
              

              - **contentType** *(string) --* 

                The content type of the message string.

                
              

              - **content** *(string) --* 

                The text of the message.

                
          
        
          

          - **maxAttempts** *(integer) --* 

            The number of times to prompt the user for information.

            
          

          - **responseCard** *(string) --* 

            A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card . 

            
      
        

        - **rejectionStatement** *(dict) --* 

          If the user answers "no" to the question defined in ``confirmationPrompt`` Amazon Lex responds with this statement to acknowledge that the intent was canceled. 

          
          

          - **messages** *(list) --* 

            A collection of message objects.

            
            

            - *(dict) --* 

              The message object that provides the message text and its type.

              
              

              - **contentType** *(string) --* 

                The content type of the message string.

                
              

              - **content** *(string) --* 

                The text of the message.

                
          
        
          

          - **responseCard** *(string) --* 

            At runtime, if the client is using the `PostText <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card. 

            
      
        

        - **followUpPrompt** *(dict) --* 

          If defined in the intent, Amazon Lex uses this prompt to solicit additional user activity after the intent is fulfilled.

          
          

          - **prompt** *(dict) --* 

            Prompts for information from the user. 

            
            

            - **messages** *(list) --* 

              An array of objects, each of which provides a message string and its type. You can specify the message string in plain text or in Speech Synthesis Markup Language (SSML).

              
              

              - *(dict) --* 

                The message object that provides the message text and its type.

                
                

                - **contentType** *(string) --* 

                  The content type of the message string.

                  
                

                - **content** *(string) --* 

                  The text of the message.

                  
            
          
            

            - **maxAttempts** *(integer) --* 

              The number of times to prompt the user for information.

              
            

            - **responseCard** *(string) --* 

              A response card. Amazon Lex uses this prompt at runtime, in the ``PostText`` API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see  ex-resp-card . 

              
        
          

          - **rejectionStatement** *(dict) --* 

            If the user answers "no" to the question defined in the ``prompt`` field, Amazon Lex responds with this statement to acknowledge that the intent was canceled. 

            
            

            - **messages** *(list) --* 

              A collection of message objects.

              
              

              - *(dict) --* 

                The message object that provides the message text and its type.

                
                

                - **contentType** *(string) --* 

                  The content type of the message string.

                  
                

                - **content** *(string) --* 

                  The text of the message.

                  
            
          
            

            - **responseCard** *(string) --* 

              At runtime, if the client is using the `PostText <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card. 

              
        
      
        

        - **conclusionStatement** *(dict) --* 

          After the Lambda function specified in the``fulfillmentActivity`` intent fulfills the intent, Amazon Lex conveys this statement to the user.

          
          

          - **messages** *(list) --* 

            A collection of message objects.

            
            

            - *(dict) --* 

              The message object that provides the message text and its type.

              
              

              - **contentType** *(string) --* 

                The content type of the message string.

                
              

              - **content** *(string) --* 

                The text of the message.

                
          
        
          

          - **responseCard** *(string) --* 

            At runtime, if the client is using the `PostText <http://docs.aws.amazon.com/lex/latest/dg/API_runtime_PostText.html>`__ API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card. 

            
      
        

        - **dialogCodeHook** *(dict) --* 

          If defined in the intent, Amazon Lex invokes this Lambda function for each user input.

          
          

          - **uri** *(string) --* 

            The Amazon Resource Name (ARN) of the Lambda function.

            
          

          - **messageVersion** *(string) --* 

            The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see  using-lambda .

            
      
        

        - **fulfillmentActivity** *(dict) --* 

          If defined in the intent, Amazon Lex invokes this Lambda function to fulfill the intent after the user provides all of the information required by the intent.

          
          

          - **type** *(string) --* 

            How the intent should be fulfilled, either by running a Lambda function or by returning the slot data to the client application. 

            
          

          - **codeHook** *(dict) --* 

            A description of the Lambda function that is run to fulfill the intent. 

            
            

            - **uri** *(string) --* 

              The Amazon Resource Name (ARN) of the Lambda function.

              
            

            - **messageVersion** *(string) --* 

              The version of the request-response that you want Amazon Lex to use to invoke your Lambda function. For more information, see  using-lambda .

              
        
      
        

        - **parentIntentSignature** *(string) --* 

          A unique identifier for the built-in intent that this intent is based on.

          
        

        - **lastUpdatedDate** *(datetime) --* 

          The date that the intent was updated. When you create a resource, the creation date and last update dates are the same.

          
        

        - **createdDate** *(datetime) --* 

          The date that the intent was created.

          
        

        - **version** *(string) --* 

          The version of the intent. For a new intent, the version is always ``$LATEST`` .

          
        

        - **checksum** *(string) --* 

          Checksum of the ``$LATEST`` version of the intent created or updated.

          
    

  .. py:method:: put_slot_type(**kwargs)

    

    Creates a custom slot type or replaces an existing custom slot type.

     

    To create a custom slot type, specify a name for the slot type and a set of enumeration values, which are the values that a slot of this type can assume. For more information, see  how-it-works .

     

    If you specify the name of an existing slot type, the fields in the request replace the existing values in the ``$LATEST`` version of the slot type. Amazon Lex removes the fields that you don't provide in the request. If you don't specify required fields, Amazon Lex throws an exception. When you update the ``$LATEST`` version of a slot type, if a bot uses the ``$LATEST`` version of an intent that contains the slot type, the bot's ``status`` field is set to ``NOT_BUILT`` .

     

    This operation requires permissions for the ``lex:PutSlotType`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/lex-models-2017-04-19/PutSlotType>`_    


    **Request Syntax** 
    ::

      response = client.put_slot_type(
          name='string',
          description='string',
          enumerationValues=[
              {
                  'value': 'string',
                  'synonyms': [
                      'string',
                  ]
              },
          ],
          checksum='string',
          valueSelectionStrategy='ORIGINAL_VALUE'|'TOP_RESOLUTION'
      )
    :type name: string
    :param name: **[REQUIRED]** 

      The name of the slot type. The name is *not* case sensitive. 

       

      The name can't match a built-in slot type name, or a built-in slot type name with "AMAZON." removed. For example, because there is a built-in slot type called ``AMAZON.DATE`` , you can't create a custom slot type called ``DATE`` .

       

      For a list of built-in slot types, see `Slot Type Reference <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/slot-type-reference>`__ in the *Alexa Skills Kit* .

      

    
    :type description: string
    :param description: 

      A description of the slot type.

      

    
    :type enumerationValues: list
    :param enumerationValues: 

      A list of ``EnumerationValue`` objects that defines the values that the slot type can take. Each value can have a list of ``synonyms`` , which are additional values that help train the machine learning model about the values that it resolves for a slot. 

       

      When Amazon Lex resolves a slot value, it generates a resolution list that contains up to five possible values for the slot. If you are using a Lambda function, this resolution list is passed to the function. If you are not using a Lambda function you can choose to return the value that the user entered or the first value in the resolution list as the slot value. The ``valueSelectionStrategy`` field indicates the option to use. 

      

    
      - *(dict) --* 

        Each slot type can have a set of values. Each enumeration value represents a value the slot type can take. 

         

        For example, a pizza ordering bot could have a slot type that specifies the type of crust that the pizza should have. The slot type could include the values 

         

         
        * thick 
         
        * thin 
         
        * stuffed 
         

        

      
        - **value** *(string) --* **[REQUIRED]** 

          The value of the slot type.

          

        
        - **synonyms** *(list) --* 

          Additional values related to the slot type value.

          

        
          - *(string) --* 

          
      
      
  
    :type checksum: string
    :param checksum: 

      Identifies a specific revision of the ``$LATEST`` version.

       

      When you create a new slot type, leave the ``checksum`` field blank. If you specify a checksum you get a ``BadRequestException`` exception.

       

      When you want to update a slot type, set the ``checksum`` field to the checksum of the most recent revision of the ``$LATEST`` version. If you don't specify the ``checksum`` field, or if the checksum does not match the ``$LATEST`` version, you get a ``PreconditionFailedException`` exception.

      

    
    :type valueSelectionStrategy: string
    :param valueSelectionStrategy: 

      Determines the slot resolution strategy that Amazon Lex uses to return slot type values. The field can be set to one of the following values:

       

       
      * ``ORIGINAL_VALUE`` - Returns the value entered by the user, if the user value is similar to the slot value. 
       
      * ``TOP_RESOLUTION`` - If there is a resolution list for the slot, return the first value in the resolution list as the slot type value. If there is no resolution list, null is returned. 
       

       

      If you don't specify the ``valueSelectionStrategy`` , the default is ``ORIGINAL_VALUE`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'name': 'string',
            'description': 'string',
            'enumerationValues': [
                {
                    'value': 'string',
                    'synonyms': [
                        'string',
                    ]
                },
            ],
            'lastUpdatedDate': datetime(2015, 1, 1),
            'createdDate': datetime(2015, 1, 1),
            'version': 'string',
            'checksum': 'string',
            'valueSelectionStrategy': 'ORIGINAL_VALUE'|'TOP_RESOLUTION'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **name** *(string) --* 

          The name of the slot type.

          
        

        - **description** *(string) --* 

          A description of the slot type.

          
        

        - **enumerationValues** *(list) --* 

          A list of ``EnumerationValue`` objects that defines the values that the slot type can take.

          
          

          - *(dict) --* 

            Each slot type can have a set of values. Each enumeration value represents a value the slot type can take. 

             

            For example, a pizza ordering bot could have a slot type that specifies the type of crust that the pizza should have. The slot type could include the values 

             

             
            * thick 
             
            * thin 
             
            * stuffed 
             

            
            

            - **value** *(string) --* 

              The value of the slot type.

              
            

            - **synonyms** *(list) --* 

              Additional values related to the slot type value.

              
              

              - *(string) --* 
          
        
      
        

        - **lastUpdatedDate** *(datetime) --* 

          The date that the slot type was updated. When you create a slot type, the creation date and last update date are the same.

          
        

        - **createdDate** *(datetime) --* 

          The date that the slot type was created.

          
        

        - **version** *(string) --* 

          The version of the slot type. For a new slot type, the version is always ``$LATEST`` . 

          
        

        - **checksum** *(string) --* 

          Checksum of the ``$LATEST`` version of the slot type.

          
        

        - **valueSelectionStrategy** *(string) --* 

          The slot resolution strategy that Amazon Lex uses to determine the value of the slot. For more information, see  PutSlotType .

          
    

==========
Paginators
==========


The available paginators are:
