

**********
Comprehend
**********

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: Comprehend.Client

  A low-level client representing Amazon Comprehend::

    
    import boto3
    
    client = boto3.client('comprehend')

  
  These are the available methods:
  
  *   :py:meth:`~Comprehend.Client.batch_detect_dominant_language`

  
  *   :py:meth:`~Comprehend.Client.batch_detect_entities`

  
  *   :py:meth:`~Comprehend.Client.batch_detect_key_phrases`

  
  *   :py:meth:`~Comprehend.Client.batch_detect_sentiment`

  
  *   :py:meth:`~Comprehend.Client.can_paginate`

  
  *   :py:meth:`~Comprehend.Client.describe_topics_detection_job`

  
  *   :py:meth:`~Comprehend.Client.detect_dominant_language`

  
  *   :py:meth:`~Comprehend.Client.detect_entities`

  
  *   :py:meth:`~Comprehend.Client.detect_key_phrases`

  
  *   :py:meth:`~Comprehend.Client.detect_sentiment`

  
  *   :py:meth:`~Comprehend.Client.generate_presigned_url`

  
  *   :py:meth:`~Comprehend.Client.get_paginator`

  
  *   :py:meth:`~Comprehend.Client.get_waiter`

  
  *   :py:meth:`~Comprehend.Client.list_topics_detection_jobs`

  
  *   :py:meth:`~Comprehend.Client.start_topics_detection_job`

  

  .. py:method:: batch_detect_dominant_language(**kwargs)

    

    Determines the dominant language of the input text for a batch of documents. For a list of languages that Amazon Comprehend can detect, see `Amazon Comprehend Supported Languages <http://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html>`__ . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/BatchDetectDominantLanguage>`_    


    **Request Syntax** 
    ::

      response = client.batch_detect_dominant_language(
          TextList=[
              'string',
          ]
      )
    :type TextList: list
    :param TextList: **[REQUIRED]** 

      A list containing the text of the input documents. The list can contain a maximum of 25 documents. Each document should contain at least 20 characters and must contain fewer than 5,000 bytes of UTF-8 encoded characters.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResultList': [
                {
                    'Index': 123,
                    'Languages': [
                        {
                            'LanguageCode': 'string',
                            'Score': ...
                        },
                    ]
                },
            ],
            'ErrorList': [
                {
                    'Index': 123,
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ResultList** *(list) --* 

          A list of objects containing the results of the operation. The results are sorted in ascending order by the ``Index`` field and match the order of the documents in the input list. If all of the documents contain an error, the ``ResultList`` is empty.

          
          

          - *(dict) --* 

            The result of calling the operation. The operation returns one object for each document that is successfully processed by the operation.

            
            

            - **Index** *(integer) --* 

              The zero-based index of the document in the input list.

              
            

            - **Languages** *(list) --* 

              One or more  DominantLanguage objects describing the dominant languages in the document.

              
              

              - *(dict) --* 

                Returns the code for the dominant language in the input text and the level of confidence that Amazon Comprehend has in the accuracy of the detection.

                
                

                - **LanguageCode** *(string) --* 

                  The RFC 5646 language code for the dominant language. 

                  
                

                - **Score** *(float) --* 

                  The level of confidence that Amazon Comprehend has in the accuracy of the detection.

                  
            
          
        
      
        

        - **ErrorList** *(list) --* 

          A list containing one object for each document that contained an error. The results are sorted in ascending order by the ``Index`` field and match the order of the documents in the input list. If there are no errors in the batch, the ``ErrorList`` is empty.

          
          

          - *(dict) --* 

            Describes an error that occurred while processing a document in a batch. The operation returns on ``BatchItemError`` object for each document that contained an error.

            
            

            - **Index** *(integer) --* 

              The zero-based index of the document in the input list.

              
            

            - **ErrorCode** *(string) --* 

              The numeric error code of the error.

              
            

            - **ErrorMessage** *(string) --* 

              A text description of the error.

              
        
      
    

  .. py:method:: batch_detect_entities(**kwargs)

    

    Inspects the text of a batch of documents and returns information about them. For more information about entities, see  how-entities  

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/BatchDetectEntities>`_    


    **Request Syntax** 
    ::

      response = client.batch_detect_entities(
          TextList=[
              'string',
          ],
          LanguageCode='string'
      )
    :type TextList: list
    :param TextList: **[REQUIRED]** 

      A list containing the text of the input documents. The list can contain a maximum of 25 documents. Each document must contain fewer than 5,000 bytes of UTF-8 encoded characters.

      

    
      - *(string) --* 

      
  
    :type LanguageCode: string
    :param LanguageCode: **[REQUIRED]** 

      The language of the input documents. All documents must be in the same language.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResultList': [
                {
                    'Index': 123,
                    'Entities': [
                        {
                            'Score': ...,
                            'Type': 'PERSON'|'LOCATION'|'ORGANIZATION'|'COMMERCIAL_ITEM'|'EVENT'|'DATE'|'QUANTITY'|'TITLE'|'OTHER',
                            'Text': 'string',
                            'BeginOffset': 123,
                            'EndOffset': 123
                        },
                    ]
                },
            ],
            'ErrorList': [
                {
                    'Index': 123,
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ResultList** *(list) --* 

          A list of objects containing the results of the operation. The results are sorted in ascending order by the ``Index`` field and match the order of the documents in the input list. If all of the documents contain an error, the ``ResultList`` is empty.

          
          

          - *(dict) --* 

            The result of calling the operation. The operation returns one object for each document that is successfully processed by the operation.

            
            

            - **Index** *(integer) --* 

              The zero-based index of the document in the input list.

              
            

            - **Entities** *(list) --* 

              One or more  Entity objects, one for each entity detected in the document.

              
              

              - *(dict) --* 

                Provides information about an entity. 

                 

                 

                
                

                - **Score** *(float) --* 

                  The level of confidence that Amazon Comprehend has in the accuracy of the detection.

                  
                

                - **Type** *(string) --* 

                  The entity's type.

                  
                

                - **Text** *(string) --* 

                  The text of the entity.

                  
                

                - **BeginOffset** *(integer) --* 

                  A character offset in the input text that shows where the entity begins (the first character is at position 0). The offset returns the position of each UTF-8 code point in the string. A *code point* is the abstract character from a particular graphical representation. For example, a multi-byte UTF-8 character maps to a single code point.

                  
                

                - **EndOffset** *(integer) --* 

                  A character offset in the input text that shows where the entity ends. The offset returns the position of each UTF-8 code point in the string. A *code point* is the abstract character from a particular graphical representation. For example, a multi-byte UTF-8 character maps to a single code point. 

                  
            
          
        
      
        

        - **ErrorList** *(list) --* 

          A list containing one object for each document that contained an error. The results are sorted in ascending order by the ``Index`` field and match the order of the documents in the input list. If there are no errors in the batch, the ``ErrorList`` is empty.

          
          

          - *(dict) --* 

            Describes an error that occurred while processing a document in a batch. The operation returns on ``BatchItemError`` object for each document that contained an error.

            
            

            - **Index** *(integer) --* 

              The zero-based index of the document in the input list.

              
            

            - **ErrorCode** *(string) --* 

              The numeric error code of the error.

              
            

            - **ErrorMessage** *(string) --* 

              A text description of the error.

              
        
      
    

  .. py:method:: batch_detect_key_phrases(**kwargs)

    

    Detects the key noun phrases found in a batch of documents.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/BatchDetectKeyPhrases>`_    


    **Request Syntax** 
    ::

      response = client.batch_detect_key_phrases(
          TextList=[
              'string',
          ],
          LanguageCode='string'
      )
    :type TextList: list
    :param TextList: **[REQUIRED]** 

      A list containing the text of the input documents. The list can contain a maximum of 25 documents. Each document must contain fewer that 5,000 bytes of UTF-8 encoded characters.

      

    
      - *(string) --* 

      
  
    :type LanguageCode: string
    :param LanguageCode: **[REQUIRED]** 

      The language of the input documents. All documents must be in the same language.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResultList': [
                {
                    'Index': 123,
                    'KeyPhrases': [
                        {
                            'Score': ...,
                            'Text': 'string',
                            'BeginOffset': 123,
                            'EndOffset': 123
                        },
                    ]
                },
            ],
            'ErrorList': [
                {
                    'Index': 123,
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ResultList** *(list) --* 

          A list of objects containing the results of the operation. The results are sorted in ascending order by the ``Index`` field and match the order of the documents in the input list. If all of the documents contain an error, the ``ResultList`` is empty.

          
          

          - *(dict) --* 

            The result of calling the operation. The operation returns one object for each document that is successfully processed by the operation.

            
            

            - **Index** *(integer) --* 

              The zero-based index of the document in the input list.

              
            

            - **KeyPhrases** *(list) --* 

              One or more  KeyPhrase objects, one for each key phrase detected in the document.

              
              

              - *(dict) --* 

                Describes a key noun phrase.

                
                

                - **Score** *(float) --* 

                  The level of confidence that Amazon Comprehend has in the accuracy of the detection.

                  
                

                - **Text** *(string) --* 

                  The text of a key noun phrase.

                  
                

                - **BeginOffset** *(integer) --* 

                  A character offset in the input text that shows where the key phrase begins (the first character is at position 0). The offset returns the position of each UTF-8 code point in the string. A *code point* is the abstract character from a particular graphical representation. For example, a multi-byte UTF-8 character maps to a single code point.

                  
                

                - **EndOffset** *(integer) --* 

                  A character offset in the input text where the key phrase ends. The offset returns the position of each UTF-8 code point in the string. A ``code point`` is the abstract character from a particular graphical representation. For example, a multi-byte UTF-8 character maps to a single code point.

                  
            
          
        
      
        

        - **ErrorList** *(list) --* 

          A list containing one object for each document that contained an error. The results are sorted in ascending order by the ``Index`` field and match the order of the documents in the input list. If there are no errors in the batch, the ``ErrorList`` is empty.

          
          

          - *(dict) --* 

            Describes an error that occurred while processing a document in a batch. The operation returns on ``BatchItemError`` object for each document that contained an error.

            
            

            - **Index** *(integer) --* 

              The zero-based index of the document in the input list.

              
            

            - **ErrorCode** *(string) --* 

              The numeric error code of the error.

              
            

            - **ErrorMessage** *(string) --* 

              A text description of the error.

              
        
      
    

  .. py:method:: batch_detect_sentiment(**kwargs)

    

    Inspects a batch of documents and returns an inference of the prevailing sentiment, ``POSITIVE`` , ``NEUTRAL`` , ``MIXED`` , or ``NEGATIVE`` , in each one.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/BatchDetectSentiment>`_    


    **Request Syntax** 
    ::

      response = client.batch_detect_sentiment(
          TextList=[
              'string',
          ],
          LanguageCode='string'
      )
    :type TextList: list
    :param TextList: **[REQUIRED]** 

      A list containing the text of the input documents. The list can contain a maximum of 25 documents. Each document must contain fewer that 5,000 bytes of UTF-8 encoded characters.

      

    
      - *(string) --* 

      
  
    :type LanguageCode: string
    :param LanguageCode: **[REQUIRED]** 

      The language of the input documents. All documents must be in the same language.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResultList': [
                {
                    'Index': 123,
                    'Sentiment': 'POSITIVE'|'NEGATIVE'|'NEUTRAL'|'MIXED',
                    'SentimentScore': {
                        'Positive': ...,
                        'Negative': ...,
                        'Neutral': ...,
                        'Mixed': ...
                    }
                },
            ],
            'ErrorList': [
                {
                    'Index': 123,
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ResultList** *(list) --* 

          A list of objects containing the results of the operation. The results are sorted in ascending order by the ``Index`` field and match the order of the documents in the input list. If all of the documents contain an error, the ``ResultList`` is empty.

          
          

          - *(dict) --* 

            The result of calling the operation. The operation returns one object for each document that is successfully processed by the operation.

            
            

            - **Index** *(integer) --* 

              The zero-based index of the document in the input list.

              
            

            - **Sentiment** *(string) --* 

              The sentiment detected in the document.

              
            

            - **SentimentScore** *(dict) --* 

              The level of confidence that Amazon Comprehend has in the accuracy of its sentiment detection.

              
              

              - **Positive** *(float) --* 

                The level of confidence that Amazon Comprehend has in the accuracy of its detection of the ``POSITIVE`` sentiment.

                
              

              - **Negative** *(float) --* 

                The level of confidence that Amazon Comprehend has in the accuracy of its detection of the ``NEGATIVE`` sentiment.

                
              

              - **Neutral** *(float) --* 

                The level of confidence that Amazon Comprehend has in the accuracy of its detection of the ``NEUTRAL`` sentiment.

                
              

              - **Mixed** *(float) --* 

                The level of confidence that Amazon Comprehend has in the accuracy of its detection of the ``MIXED`` sentiment.

                
          
        
      
        

        - **ErrorList** *(list) --* 

          A list containing one object for each document that contained an error. The results are sorted in ascending order by the ``Index`` field and match the order of the documents in the input list. If there are no errors in the batch, the ``ErrorList`` is empty.

          
          

          - *(dict) --* 

            Describes an error that occurred while processing a document in a batch. The operation returns on ``BatchItemError`` object for each document that contained an error.

            
            

            - **Index** *(integer) --* 

              The zero-based index of the document in the input list.

              
            

            - **ErrorCode** *(string) --* 

              The numeric error code of the error.

              
            

            - **ErrorMessage** *(string) --* 

              A text description of the error.

              
        
      
    

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


  .. py:method:: describe_topics_detection_job(**kwargs)

    

    Gets the properties associated with a topic detection job. Use this operation to get the status of a detection job.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DescribeTopicsDetectionJob>`_    


    **Request Syntax** 
    ::

      response = client.describe_topics_detection_job(
          JobId='string'
      )
    :type JobId: string
    :param JobId: **[REQUIRED]** 

      The identifier assigned by the user to the detection job.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TopicsDetectionJobProperties': {
                'JobId': 'string',
                'JobName': 'string',
                'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED',
                'Message': 'string',
                'SubmitTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1),
                'InputDataConfig': {
                    'S3Uri': 'string',
                    'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
                },
                'OutputDataConfig': {
                    'S3Uri': 'string'
                },
                'NumberOfTopics': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TopicsDetectionJobProperties** *(dict) --* 

          The list of properties for the requested job.

          
          

          - **JobId** *(string) --* 

            The identifier assigned to the topic detection job.

            
          

          - **JobName** *(string) --* 

            The name of the topic detection job.

            
          

          - **JobStatus** *(string) --* 

            The current status of the topic detection job. If the status is ``Failed`` , the reason for the failure is shown in the ``Message`` field.

            
          

          - **Message** *(string) --* 

            A description for the status of a job.

            
          

          - **SubmitTime** *(datetime) --* 

            The time that the topic detection job was submitted for processing.

            
          

          - **EndTime** *(datetime) --* 

            The time that the topic detection job was completed.

            
          

          - **InputDataConfig** *(dict) --* 

            The input data configuration supplied when you created the topic detection job.

            
            

            - **S3Uri** *(string) --* 

              The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files. 

               

              For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.

              
            

            - **InputFormat** *(string) --* 

              Specifies how the text in an input file should be processed:

               

               
              * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers. 
               
              * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages. 
               

              
        
          

          - **OutputDataConfig** *(dict) --* 

            The output data configuration supplied when you created the topic detection job.

            
            

            - **S3Uri** *(string) --* 

              The Amazon S3 URI where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. 

               

              The service creates an output file called ``output.tar.gz`` . It is a compressed archive that contains two files, ``topic-terms.csv`` that lists the terms associated with each topic, and ``doc-topics.csv`` that lists the documents associated with each topic. For more information, see  topic-modeling .

              
        
          

          - **NumberOfTopics** *(integer) --* 

            The number of topics to detect supplied when you created the topic detection job. The default is 10. 

            
      
    

  .. py:method:: detect_dominant_language(**kwargs)

    

    Determines the dominant language of the input text. For a list of languages that Amazon Comprehend can detect, see `Amazon Comprehend Supported Languages <http://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html>`__ . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DetectDominantLanguage>`_    


    **Request Syntax** 
    ::

      response = client.detect_dominant_language(
          Text='string'
      )
    :type Text: string
    :param Text: **[REQUIRED]** 

      A UTF-8 text string. Each string should contain at least 20 characters and must contain fewer that 5,000 bytes of UTF-8 encoded characters.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Languages': [
                {
                    'LanguageCode': 'string',
                    'Score': ...
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Languages** *(list) --* 

          The languages that Amazon Comprehend detected in the input text. For each language, the response returns the RFC 5646 language code and the level of confidence that Amazon Comprehend has in the accuracy of its inference. For more information about RFC 5646, see `Tags for Identifying Languages <https://tools.ietf.org/html/rfc5646>`__ on the *IETF Tools* web site.

          
          

          - *(dict) --* 

            Returns the code for the dominant language in the input text and the level of confidence that Amazon Comprehend has in the accuracy of the detection.

            
            

            - **LanguageCode** *(string) --* 

              The RFC 5646 language code for the dominant language. 

              
            

            - **Score** *(float) --* 

              The level of confidence that Amazon Comprehend has in the accuracy of the detection.

              
        
      
    

  .. py:method:: detect_entities(**kwargs)

    

    Inspects text for entities, and returns information about them. For more information, about entities, see  how-entities . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DetectEntities>`_    


    **Request Syntax** 
    ::

      response = client.detect_entities(
          Text='string',
          LanguageCode='en'|'es'
      )
    :type Text: string
    :param Text: **[REQUIRED]** 

      A UTF-8 text string. Each string must contain fewer that 5,000 bytes of UTF-8 encoded characters.

      

    
    :type LanguageCode: string
    :param LanguageCode: **[REQUIRED]** 

      The RFC 5646 language code of the input text. If the request does not specify the language code, the service detects the dominant language. If you specify a language code that the service does not support, it returns ``UnsupportedLanguageException`` exception. For more information about RFC 5646, see `Tags for Identifying Languages <https://tools.ietf.org/html/rfc5646>`__ on the *IETF Tools* web site. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Entities': [
                {
                    'Score': ...,
                    'Type': 'PERSON'|'LOCATION'|'ORGANIZATION'|'COMMERCIAL_ITEM'|'EVENT'|'DATE'|'QUANTITY'|'TITLE'|'OTHER',
                    'Text': 'string',
                    'BeginOffset': 123,
                    'EndOffset': 123
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Entities** *(list) --* 

          A collection of entities identified in the input text. For each entity, the response provides the entity text, entity type, where the entity text begins and ends, and the level of confidence that Amazon Comprehend has in the detection. For a list of entity types, see  how-entities . 

          
          

          - *(dict) --* 

            Provides information about an entity. 

             

             

            
            

            - **Score** *(float) --* 

              The level of confidence that Amazon Comprehend has in the accuracy of the detection.

              
            

            - **Type** *(string) --* 

              The entity's type.

              
            

            - **Text** *(string) --* 

              The text of the entity.

              
            

            - **BeginOffset** *(integer) --* 

              A character offset in the input text that shows where the entity begins (the first character is at position 0). The offset returns the position of each UTF-8 code point in the string. A *code point* is the abstract character from a particular graphical representation. For example, a multi-byte UTF-8 character maps to a single code point.

              
            

            - **EndOffset** *(integer) --* 

              A character offset in the input text that shows where the entity ends. The offset returns the position of each UTF-8 code point in the string. A *code point* is the abstract character from a particular graphical representation. For example, a multi-byte UTF-8 character maps to a single code point. 

              
        
      
    

  .. py:method:: detect_key_phrases(**kwargs)

    

    Detects the key noun phrases found in the text. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DetectKeyPhrases>`_    


    **Request Syntax** 
    ::

      response = client.detect_key_phrases(
          Text='string',
          LanguageCode='en'|'es'
      )
    :type Text: string
    :param Text: **[REQUIRED]** 

      A UTF-8 text string. Each string must contain fewer that 5,000 bytes of UTF-8 encoded characters.

      

    
    :type LanguageCode: string
    :param LanguageCode: **[REQUIRED]** 

      The RFC 5646 language code for the input text. If you don't specify a language code, Amazon Comprehend detects the dominant language. If you specify the code for a language that Amazon Comprehend does not support, it returns and ``UnsupportedLanguageException`` . For more information about RFC 5646, see `Tags for Identifying Languages <https://tools.ietf.org/html/rfc5646>`__ on the *IETF Tools* web site.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'KeyPhrases': [
                {
                    'Score': ...,
                    'Text': 'string',
                    'BeginOffset': 123,
                    'EndOffset': 123
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **KeyPhrases** *(list) --* 

          A collection of key phrases that Amazon Comprehend identified in the input text. For each key phrase, the response provides the text of the key phrase, where the key phrase begins and ends, and the level of confidence that Amazon Comprehend has in the accuracy of the detection. 

          
          

          - *(dict) --* 

            Describes a key noun phrase.

            
            

            - **Score** *(float) --* 

              The level of confidence that Amazon Comprehend has in the accuracy of the detection.

              
            

            - **Text** *(string) --* 

              The text of a key noun phrase.

              
            

            - **BeginOffset** *(integer) --* 

              A character offset in the input text that shows where the key phrase begins (the first character is at position 0). The offset returns the position of each UTF-8 code point in the string. A *code point* is the abstract character from a particular graphical representation. For example, a multi-byte UTF-8 character maps to a single code point.

              
            

            - **EndOffset** *(integer) --* 

              A character offset in the input text where the key phrase ends. The offset returns the position of each UTF-8 code point in the string. A ``code point`` is the abstract character from a particular graphical representation. For example, a multi-byte UTF-8 character maps to a single code point.

              
        
      
    

  .. py:method:: detect_sentiment(**kwargs)

    

    Inspects text and returns an inference of the prevailing sentiment (``POSITIVE`` , ``NEUTRAL`` , ``MIXED`` , or ``NEGATIVE`` ). 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/DetectSentiment>`_    


    **Request Syntax** 
    ::

      response = client.detect_sentiment(
          Text='string',
          LanguageCode='en'|'es'
      )
    :type Text: string
    :param Text: **[REQUIRED]** 

      A UTF-8 text string. Each string must contain fewer that 5,000 bytes of UTF-8 encoded characters.

      

    
    :type LanguageCode: string
    :param LanguageCode: **[REQUIRED]** 

      The RFC 5646 language code for the input text. If you don't specify a language code, Amazon Comprehend detects the dominant language. If you specify the code for a language that Amazon Comprehend does not support, it returns and ``UnsupportedLanguageException`` . For more information about RFC 5646, see `Tags for Identifying Languages <https://tools.ietf.org/html/rfc5646>`__ on the *IETF Tools* web site.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Sentiment': 'POSITIVE'|'NEGATIVE'|'NEUTRAL'|'MIXED',
            'SentimentScore': {
                'Positive': ...,
                'Negative': ...,
                'Neutral': ...,
                'Mixed': ...
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Sentiment** *(string) --* 

          The inferred sentiment that Amazon Comprehend has the highest level of confidence in.

          
        

        - **SentimentScore** *(dict) --* 

          An object that lists the sentiments, and their corresponding confidence levels.

          
          

          - **Positive** *(float) --* 

            The level of confidence that Amazon Comprehend has in the accuracy of its detection of the ``POSITIVE`` sentiment.

            
          

          - **Negative** *(float) --* 

            The level of confidence that Amazon Comprehend has in the accuracy of its detection of the ``NEGATIVE`` sentiment.

            
          

          - **Neutral** *(float) --* 

            The level of confidence that Amazon Comprehend has in the accuracy of its detection of the ``NEUTRAL`` sentiment.

            
          

          - **Mixed** *(float) --* 

            The level of confidence that Amazon Comprehend has in the accuracy of its detection of the ``MIXED`` sentiment.

            
      
    

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

        


  .. py:method:: list_topics_detection_jobs(**kwargs)

    

    Gets a list of the topic detection jobs that you have submitted.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/ListTopicsDetectionJobs>`_    


    **Request Syntax** 
    ::

      response = client.list_topics_detection_jobs(
          Filter={
              'JobName': 'string',
              'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED',
              'SubmitTimeBefore': datetime(2015, 1, 1),
              'SubmitTimeAfter': datetime(2015, 1, 1)
          },
          NextToken='string',
          MaxResults=123
      )
    :type Filter: dict
    :param Filter: 

      Filters the jobs that are returned. Jobs can be filtered on their name, status, or the date and time that they were submitted. You can set only one filter at a time.

      

    
      - **JobName** *(string) --* 

        

        

      
      - **JobStatus** *(string) --* 

        Filters the list of topic detection jobs based on job status. Returns only jobs with the specified status.

        

      
      - **SubmitTimeBefore** *(datetime) --* 

        Filters the list of jobs based on the time that the job was submitted for processing. Only returns jobs submitted before the specified time. Jobs are returned in descending order, newest to oldest.

        

      
      - **SubmitTimeAfter** *(datetime) --* 

        Filters the list of jobs based on the time that the job was submitted for processing. Only returns jobs submitted after the specified time. Jobs are returned in ascending order, oldest to newest.

        

      
    
    :type NextToken: string
    :param NextToken: 

      Identifies the next page of results to return.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of results to return in each page.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TopicsDetectionJobPropertiesList': [
                {
                    'JobId': 'string',
                    'JobName': 'string',
                    'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED',
                    'Message': 'string',
                    'SubmitTime': datetime(2015, 1, 1),
                    'EndTime': datetime(2015, 1, 1),
                    'InputDataConfig': {
                        'S3Uri': 'string',
                        'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
                    },
                    'OutputDataConfig': {
                        'S3Uri': 'string'
                    },
                    'NumberOfTopics': 123
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TopicsDetectionJobPropertiesList** *(list) --* 

          A list containing the properties of each job that is returned.

          
          

          - *(dict) --* 

            Provides information about a topic detection job.

            
            

            - **JobId** *(string) --* 

              The identifier assigned to the topic detection job.

              
            

            - **JobName** *(string) --* 

              The name of the topic detection job.

              
            

            - **JobStatus** *(string) --* 

              The current status of the topic detection job. If the status is ``Failed`` , the reason for the failure is shown in the ``Message`` field.

              
            

            - **Message** *(string) --* 

              A description for the status of a job.

              
            

            - **SubmitTime** *(datetime) --* 

              The time that the topic detection job was submitted for processing.

              
            

            - **EndTime** *(datetime) --* 

              The time that the topic detection job was completed.

              
            

            - **InputDataConfig** *(dict) --* 

              The input data configuration supplied when you created the topic detection job.

              
              

              - **S3Uri** *(string) --* 

                The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files. 

                 

                For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.

                
              

              - **InputFormat** *(string) --* 

                Specifies how the text in an input file should be processed:

                 

                 
                * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers. 
                 
                * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages. 
                 

                
          
            

            - **OutputDataConfig** *(dict) --* 

              The output data configuration supplied when you created the topic detection job.

              
              

              - **S3Uri** *(string) --* 

                The Amazon S3 URI where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. 

                 

                The service creates an output file called ``output.tar.gz`` . It is a compressed archive that contains two files, ``topic-terms.csv`` that lists the terms associated with each topic, and ``doc-topics.csv`` that lists the documents associated with each topic. For more information, see  topic-modeling .

                
          
            

            - **NumberOfTopics** *(integer) --* 

              The number of topics to detect supplied when you created the topic detection job. The default is 10. 

              
        
      
        

        - **NextToken** *(string) --* 

          Identifies the next page of results to return.

          
    

  .. py:method:: start_topics_detection_job(**kwargs)

    

    Starts an asynchronous topic detection job. Use the ``DescribeTopicDetectionJob`` operation to track the status of a job.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/StartTopicsDetectionJob>`_    


    **Request Syntax** 
    ::

      response = client.start_topics_detection_job(
          InputDataConfig={
              'S3Uri': 'string',
              'InputFormat': 'ONE_DOC_PER_FILE'|'ONE_DOC_PER_LINE'
          },
          OutputDataConfig={
              'S3Uri': 'string'
          },
          DataAccessRoleArn='string',
          JobName='string',
          NumberOfTopics=123,
          ClientRequestToken='string'
      )
    :type InputDataConfig: dict
    :param InputDataConfig: **[REQUIRED]** 

      Specifies the format and location of the input data for the job.

      

    
      - **S3Uri** *(string) --* **[REQUIRED]** 

        The Amazon S3 URI for the input data. The URI must be in same region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files. 

         

        For example, if you use the URI ``S3://bucketName/prefix`` , if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.

        

      
      - **InputFormat** *(string) --* 

        Specifies how the text in an input file should be processed:

         

         
        * ``ONE_DOC_PER_FILE`` - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers. 
         
        * ``ONE_DOC_PER_LINE`` - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages. 
         

        

      
    
    :type OutputDataConfig: dict
    :param OutputDataConfig: **[REQUIRED]** 

      Specifies where to send the output files.

      

    
      - **S3Uri** *(string) --* **[REQUIRED]** 

        The Amazon S3 URI where you want to write the output data. The URI must be in the same region as the API endpoint that you are calling. 

         

        The service creates an output file called ``output.tar.gz`` . It is a compressed archive that contains two files, ``topic-terms.csv`` that lists the terms associated with each topic, and ``doc-topics.csv`` that lists the documents associated with each topic. For more information, see  topic-modeling .

        

      
    
    :type DataAccessRoleArn: string
    :param DataAccessRoleArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that grants Amazon Comprehend read access to your input data. 

      

    
    :type JobName: string
    :param JobName: 

      The identifier of the job.

      

    
    :type NumberOfTopics: integer
    :param NumberOfTopics: 

      The number of topics to detect.

      

    
    :type ClientRequestToken: string
    :param ClientRequestToken: 

      A unique identifier for the request. If you do not set the client request token, Amazon Comprehend generates one.

      This field is autopopulated if not provided.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'JobId': 'string',
            'JobStatus': 'SUBMITTED'|'IN_PROGRESS'|'COMPLETED'|'FAILED'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **JobId** *(string) --* 

          The identifier generated for the job. To get the status of the job, use this identifier with the ``DescribeTopicDetectionJob`` operation.

          
        

        - **JobStatus** *(string) --* 

          The status of the job: 

           

           
          * SUBMITTED - The job has been received and is queued for processing. 
           
          * IN_PROGRESS - Amazon Comprehend is processing the job. 
           
          * COMPLETED - The job was successfully completed and the output is available. 
           
          * FAILED - The job did not complete. To get details, use the ``DescribeTopicDetectionJob`` operation. 
           

          
    

==========
Paginators
==========


The available paginators are:
