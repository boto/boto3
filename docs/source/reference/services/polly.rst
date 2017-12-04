

*****
Polly
*****

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: Polly.Client

  A low-level client representing Amazon Polly::

    
    import boto3
    
    client = boto3.client('polly')

  
  These are the available methods:
  
  *   :py:meth:`~Polly.Client.can_paginate`

  
  *   :py:meth:`~Polly.Client.delete_lexicon`

  
  *   :py:meth:`~Polly.Client.describe_voices`

  
  *   :py:meth:`~Polly.Client.generate_presigned_url`

  
  *   :py:meth:`~Polly.Client.get_lexicon`

  
  *   :py:meth:`~Polly.Client.get_paginator`

  
  *   :py:meth:`~Polly.Client.get_waiter`

  
  *   :py:meth:`~Polly.Client.list_lexicons`

  
  *   :py:meth:`~Polly.Client.put_lexicon`

  
  *   :py:meth:`~Polly.Client.synthesize_speech`

  

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


  .. py:method:: delete_lexicon(**kwargs)

    

    Deletes the specified pronunciation lexicon stored in an AWS Region. A lexicon which has been deleted is not available for speech synthesis, nor is it possible to retrieve it using either the ``GetLexicon`` or ``ListLexicon`` APIs.

     

    For more information, see `Managing Lexicons <http://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/DeleteLexicon>`_    


    **Request Syntax** 
    ::

      response = client.delete_lexicon(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the lexicon to delete. Must be an existing lexicon in the region.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

    **Examples** 

    Deletes a specified pronunciation lexicon stored in an AWS Region.
    ::

      response = client.delete_lexicon(
          Name='example',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: describe_voices(**kwargs)

    

    Returns the list of voices that are available for use when requesting speech synthesis. Each voice speaks a specified language, is either male or female, and is identified by an ID, which is the ASCII version of the voice name. 

     

    When synthesizing speech ( ``SynthesizeSpeech`` ), you provide the voice ID for the voice you want from the list of voices returned by ``DescribeVoices`` .

     

    For example, you want your news reader application to read news in a specific language, but giving a user the option to choose the voice. Using the ``DescribeVoices`` operation you can provide the user with a list of available voices to select from.

     

    You can optionally specify a language code to filter the available voices. For example, if you specify ``en-US`` , the operation returns a list of all available US English voices. 

     

    This operation requires permissions to perform the ``polly:DescribeVoices`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/DescribeVoices>`_    


    **Request Syntax** 
    ::

      response = client.describe_voices(
          LanguageCode='cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ko-KR'|'ja-JP'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
          NextToken='string'
      )
    :type LanguageCode: string
    :param LanguageCode: 

      The language identification tag (ISO 639 code for the language name-ISO 3166 country code) for filtering the list of voices returned. If you don't specify this optional parameter, all available voices are returned. 

      

    
    :type NextToken: string
    :param NextToken: 

      An opaque pagination token returned from the previous ``DescribeVoices`` operation. If present, this indicates where to continue the listing.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Voices': [
                {
                    'Gender': 'Female'|'Male',
                    'Id': 'Geraint'|'Gwyneth'|'Mads'|'Naja'|'Hans'|'Marlene'|'Nicole'|'Russell'|'Amy'|'Brian'|'Emma'|'Raveena'|'Ivy'|'Joanna'|'Joey'|'Justin'|'Kendra'|'Kimberly'|'Matthew'|'Salli'|'Conchita'|'Enrique'|'Miguel'|'Penelope'|'Chantal'|'Celine'|'Mathieu'|'Dora'|'Karl'|'Carla'|'Giorgio'|'Mizuki'|'Liv'|'Lotte'|'Ruben'|'Ewa'|'Jacek'|'Jan'|'Maja'|'Ricardo'|'Vitoria'|'Cristiano'|'Ines'|'Carmen'|'Maxim'|'Tatyana'|'Astrid'|'Filiz'|'Vicki'|'Takumi'|'Seoyeon'|'Aditi',
                    'LanguageCode': 'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ko-KR'|'ja-JP'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
                    'LanguageName': 'string',
                    'Name': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Voices** *(list) --* 

          A list of voices with their properties.

          
          

          - *(dict) --* 

            Description of the voice.

            
            

            - **Gender** *(string) --* 

              Gender of the voice.

              
            

            - **Id** *(string) --* 

              Amazon Polly assigned voice ID. This is the ID that you specify when calling the ``SynthesizeSpeech`` operation.

              
            

            - **LanguageCode** *(string) --* 

              Language code of the voice.

              
            

            - **LanguageName** *(string) --* 

              Human readable name of the language in English.

              
            

            - **Name** *(string) --* 

              Name of the voice (for example, Salli, Kendra, etc.). This provides a human readable voice name that you might display in your application.

              
        
      
        

        - **NextToken** *(string) --* 

          The pagination token to use in the next request to continue the listing of voices. ``NextToken`` is returned only if the response is truncated.

          
    

    **Examples** 

    Returns the list of voices that are available for use when requesting speech synthesis. Displayed languages are those within the specified language code. If no language code is specified, voices for all available languages are displayed.
    ::

      response = client.describe_voices(
          LanguageCode='en-GB',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Voices': [
              {
                  'Gender': 'Female',
                  'Id': 'Emma',
                  'LanguageCode': 'en-GB',
                  'LanguageName': 'British English',
                  'Name': 'Emma',
              },
              {
                  'Gender': 'Male',
                  'Id': 'Brian',
                  'LanguageCode': 'en-GB',
                  'LanguageName': 'British English',
                  'Name': 'Brian',
              },
              {
                  'Gender': 'Female',
                  'Id': 'Amy',
                  'LanguageCode': 'en-GB',
                  'LanguageName': 'British English',
                  'Name': 'Amy',
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


  .. py:method:: get_lexicon(**kwargs)

    

    Returns the content of the specified pronunciation lexicon stored in an AWS Region. For more information, see `Managing Lexicons <http://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/GetLexicon>`_    


    **Request Syntax** 
    ::

      response = client.get_lexicon(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      Name of the lexicon.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Lexicon': {
                'Content': 'string',
                'Name': 'string'
            },
            'LexiconAttributes': {
                'Alphabet': 'string',
                'LanguageCode': 'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ko-KR'|'ja-JP'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
                'LastModified': datetime(2015, 1, 1),
                'LexiconArn': 'string',
                'LexemesCount': 123,
                'Size': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Lexicon** *(dict) --* 

          Lexicon object that provides name and the string content of the lexicon. 

          
          

          - **Content** *(string) --* 

            Lexicon content in string format. The content of a lexicon must be in PLS format.

            
          

          - **Name** *(string) --* 

            Name of the lexicon.

            
      
        

        - **LexiconAttributes** *(dict) --* 

          Metadata of the lexicon, including phonetic alphabetic used, language code, lexicon ARN, number of lexemes defined in the lexicon, and size of lexicon in bytes.

          
          

          - **Alphabet** *(string) --* 

            Phonetic alphabet used in the lexicon. Valid values are ``ipa`` and ``x-sampa`` .

            
          

          - **LanguageCode** *(string) --* 

            Language code that the lexicon applies to. A lexicon with a language code such as "en" would be applied to all English languages (en-GB, en-US, en-AUS, en-WLS, and so on.

            
          

          - **LastModified** *(datetime) --* 

            Date lexicon was last modified (a timestamp value).

            
          

          - **LexiconArn** *(string) --* 

            Amazon Resource Name (ARN) of the lexicon.

            
          

          - **LexemesCount** *(integer) --* 

            Number of lexemes in the lexicon.

            
          

          - **Size** *(integer) --* 

            Total size of the lexicon, in characters.

            
      
    

    **Examples** 

    Returns the content of the specified pronunciation lexicon stored in an AWS Region.
    ::

      response = client.get_lexicon(
          Name='',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Lexicon': {
              'Content': '<?xml version="1.0" encoding="UTF-8"?>\r\n<lexicon version="1.0" \r\n      xmlns="http://www.w3.org/2005/01/pronunciation-lexicon"\r\n      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" \r\n      xsi:schemaLocation="http://www.w3.org/2005/01/pronunciation-lexicon \r\n        http://www.w3.org/TR/2007/CR-pronunciation-lexicon-20071212/pls.xsd"\r\n      alphabet="ipa" \r\n      xml:lang="en-US">\r\n  <lexeme>\r\n    <grapheme>W3C</grapheme>\r\n    <alias>World Wide Web Consortium</alias>\r\n  </lexeme>\r\n</lexicon>',
              'Name': 'example',
          },
          'LexiconAttributes': {
              'Alphabet': 'ipa',
              'LanguageCode': 'en-US',
              'LastModified': 1478542980.117,
              'LexemesCount': 1,
              'LexiconArn': 'arn:aws:polly:us-east-1:123456789012:lexicon/example',
              'Size': 503,
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


  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: list_lexicons(**kwargs)

    

    Returns a list of pronunciation lexicons stored in an AWS Region. For more information, see `Managing Lexicons <http://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/ListLexicons>`_    


    **Request Syntax** 
    ::

      response = client.list_lexicons(
          NextToken='string'
      )
    :type NextToken: string
    :param NextToken: 

      An opaque pagination token returned from previous ``ListLexicons`` operation. If present, indicates where to continue the list of lexicons.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Lexicons': [
                {
                    'Name': 'string',
                    'Attributes': {
                        'Alphabet': 'string',
                        'LanguageCode': 'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ko-KR'|'ja-JP'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
                        'LastModified': datetime(2015, 1, 1),
                        'LexiconArn': 'string',
                        'LexemesCount': 123,
                        'Size': 123
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Lexicons** *(list) --* 

          A list of lexicon names and attributes.

          
          

          - *(dict) --* 

            Describes the content of the lexicon.

            
            

            - **Name** *(string) --* 

              Name of the lexicon.

              
            

            - **Attributes** *(dict) --* 

              Provides lexicon metadata.

              
              

              - **Alphabet** *(string) --* 

                Phonetic alphabet used in the lexicon. Valid values are ``ipa`` and ``x-sampa`` .

                
              

              - **LanguageCode** *(string) --* 

                Language code that the lexicon applies to. A lexicon with a language code such as "en" would be applied to all English languages (en-GB, en-US, en-AUS, en-WLS, and so on.

                
              

              - **LastModified** *(datetime) --* 

                Date lexicon was last modified (a timestamp value).

                
              

              - **LexiconArn** *(string) --* 

                Amazon Resource Name (ARN) of the lexicon.

                
              

              - **LexemesCount** *(integer) --* 

                Number of lexemes in the lexicon.

                
              

              - **Size** *(integer) --* 

                Total size of the lexicon, in characters.

                
          
        
      
        

        - **NextToken** *(string) --* 

          The pagination token to use in the next request to continue the listing of lexicons. ``NextToken`` is returned only if the response is truncated.

          
    

    **Examples** 

    Returns a list of pronunciation lexicons stored in an AWS Region.
    ::

      response = client.list_lexicons(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Lexicons': [
              {
                  'Attributes': {
                      'Alphabet': 'ipa',
                      'LanguageCode': 'en-US',
                      'LastModified': 1478542980.117,
                      'LexemesCount': 1,
                      'LexiconArn': 'arn:aws:polly:us-east-1:123456789012:lexicon/example',
                      'Size': 503,
                  },
                  'Name': 'example',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: put_lexicon(**kwargs)

    

    Stores a pronunciation lexicon in an AWS Region. If a lexicon with the same name already exists in the region, it is overwritten by the new lexicon. Lexicon operations have eventual consistency, therefore, it might take some time before the lexicon is available to the SynthesizeSpeech operation.

     

    For more information, see `Managing Lexicons <http://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/PutLexicon>`_    


    **Request Syntax** 
    ::

      response = client.put_lexicon(
          Name='string',
          Content='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      Name of the lexicon. The name must follow the regular express format [0-9A-Za-z]{1,20}. That is, the name is a case-sensitive alphanumeric string up to 20 characters long. 

      

    
    :type Content: string
    :param Content: **[REQUIRED]** 

      Content of the PLS lexicon as string data.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

    **Examples** 

    Stores a pronunciation lexicon in an AWS Region.
    ::

      response = client.put_lexicon(
          Content='file://example.pls',
          Name='W3C',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: synthesize_speech(**kwargs)

    

    Synthesizes UTF-8 input, plain text or SSML, to a stream of bytes. SSML input must be valid, well-formed SSML. Some alphabets might not be available with all the voices (for example, Cyrillic might not be read at all by English voices) unless phoneme mapping is used. For more information, see `How it Works <http://docs.aws.amazon.com/polly/latest/dg/how-text-to-speech-works.html>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/SynthesizeSpeech>`_    


    **Request Syntax** 
    ::

      response = client.synthesize_speech(
          LexiconNames=[
              'string',
          ],
          OutputFormat='json'|'mp3'|'ogg_vorbis'|'pcm',
          SampleRate='string',
          SpeechMarkTypes=[
              'sentence'|'ssml'|'viseme'|'word',
          ],
          Text='string',
          TextType='ssml'|'text',
          VoiceId='Geraint'|'Gwyneth'|'Mads'|'Naja'|'Hans'|'Marlene'|'Nicole'|'Russell'|'Amy'|'Brian'|'Emma'|'Raveena'|'Ivy'|'Joanna'|'Joey'|'Justin'|'Kendra'|'Kimberly'|'Matthew'|'Salli'|'Conchita'|'Enrique'|'Miguel'|'Penelope'|'Chantal'|'Celine'|'Mathieu'|'Dora'|'Karl'|'Carla'|'Giorgio'|'Mizuki'|'Liv'|'Lotte'|'Ruben'|'Ewa'|'Jacek'|'Jan'|'Maja'|'Ricardo'|'Vitoria'|'Cristiano'|'Ines'|'Carmen'|'Maxim'|'Tatyana'|'Astrid'|'Filiz'|'Vicki'|'Takumi'|'Seoyeon'|'Aditi'
      )
    :type LexiconNames: list
    :param LexiconNames: 

      List of one or more pronunciation lexicon names you want the service to apply during synthesis. Lexicons are applied only if the language of the lexicon is the same as the language of the voice. For information about storing lexicons, see `PutLexicon <http://docs.aws.amazon.com/polly/latest/dg/API_PutLexicon.html>`__ .

      

    
      - *(string) --* 

      
  
    :type OutputFormat: string
    :param OutputFormat: **[REQUIRED]** 

      The format in which the returned output will be encoded. For audio stream, this will be mp3, ogg_vorbis, or pcm. For speech marks, this will be json. 

      

    
    :type SampleRate: string
    :param SampleRate: 

      The audio frequency specified in Hz. 

       

      The valid values for ``mp3`` and ``ogg_vorbis`` are "8000", "16000", and "22050". The default value is "22050". 

       

      Valid values for ``pcm`` are "8000" and "16000" The default value is "16000". 

      

    
    :type SpeechMarkTypes: list
    :param SpeechMarkTypes: 

      The type of speech marks returned for the input text.

      

    
      - *(string) --* 

      
  
    :type Text: string
    :param Text: **[REQUIRED]** 

      Input text to synthesize. If you specify ``ssml`` as the ``TextType`` , follow the SSML format for the input text. 

      

    
    :type TextType: string
    :param TextType: 

      Specifies whether the input text is plain text or SSML. The default value is plain text. For more information, see `Using SSML <http://docs.aws.amazon.com/polly/latest/dg/ssml.html>`__ .

      

    
    :type VoiceId: string
    :param VoiceId: **[REQUIRED]** 

      Voice ID to use for the synthesis. You can get a list of available voice IDs by calling the `DescribeVoices <http://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html>`__ operation. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AudioStream': StreamingBody(),
            'ContentType': 'string',
            'RequestCharacters': 123
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **AudioStream** (:class:`.StreamingBody`) -- 

          Stream containing the synthesized speech. 

          
        

        - **ContentType** *(string) --* 

          Specifies the type audio stream. This should reflect the ``OutputFormat`` parameter in your request. 

           

           
          * If you request ``mp3`` as the ``OutputFormat`` , the ``ContentType`` returned is audio/mpeg.  
           
          * If you request ``ogg_vorbis`` as the ``OutputFormat`` , the ``ContentType`` returned is audio/ogg.  
           
          * If you request ``pcm`` as the ``OutputFormat`` , the ``ContentType`` returned is audio/pcm in a signed 16-bit, 1 channel (mono), little-endian format.  
           
          * If you request ``json`` as the ``OutputFormat`` , the ``ContentType`` returned is audio/json. 
           

           

           

          
        

        - **RequestCharacters** *(integer) --* 

          Number of characters synthesized.

          
    

    **Examples** 

    Synthesizes plain text or SSML into a file of human-like speech.
    ::

      response = client.synthesize_speech(
          LexiconNames=[
              'example',
          ],
          OutputFormat='mp3',
          SampleRate='8000',
          Text='All Gaul is divided into three parts',
          TextType='text',
          VoiceId='Joanna',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'AudioStream': 'TEXT',
          'ContentType': 'audio/mpeg',
          'RequestCharacters': 37,
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

==========
Paginators
==========


The available paginators are:

* :py:class:`Polly.Paginator.DescribeVoices`



.. py:class:: Polly.Paginator.DescribeVoices

  ::

    
    paginator = client.get_paginator('describe_voices')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Polly.Client.describe_voices`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/polly-2016-06-10/DescribeVoices>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          LanguageCode='cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ko-KR'|'ja-JP'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type LanguageCode: string
    :param LanguageCode: 

      The language identification tag (ISO 639 code for the language name-ISO 3166 country code) for filtering the list of voices returned. If you don't specify this optional parameter, all available voices are returned. 

      

    
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
            'Voices': [
                {
                    'Gender': 'Female'|'Male',
                    'Id': 'Geraint'|'Gwyneth'|'Mads'|'Naja'|'Hans'|'Marlene'|'Nicole'|'Russell'|'Amy'|'Brian'|'Emma'|'Raveena'|'Ivy'|'Joanna'|'Joey'|'Justin'|'Kendra'|'Kimberly'|'Matthew'|'Salli'|'Conchita'|'Enrique'|'Miguel'|'Penelope'|'Chantal'|'Celine'|'Mathieu'|'Dora'|'Karl'|'Carla'|'Giorgio'|'Mizuki'|'Liv'|'Lotte'|'Ruben'|'Ewa'|'Jacek'|'Jan'|'Maja'|'Ricardo'|'Vitoria'|'Cristiano'|'Ines'|'Carmen'|'Maxim'|'Tatyana'|'Astrid'|'Filiz'|'Vicki'|'Takumi'|'Seoyeon'|'Aditi',
                    'LanguageCode': 'cy-GB'|'da-DK'|'de-DE'|'en-AU'|'en-GB'|'en-GB-WLS'|'en-IN'|'en-US'|'es-ES'|'es-US'|'fr-CA'|'fr-FR'|'is-IS'|'it-IT'|'ko-KR'|'ja-JP'|'nb-NO'|'nl-NL'|'pl-PL'|'pt-BR'|'pt-PT'|'ro-RO'|'ru-RU'|'sv-SE'|'tr-TR',
                    'LanguageName': 'string',
                    'Name': 'string'
                },
            ],
            
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Voices** *(list) --* 

          A list of voices with their properties.

          
          

          - *(dict) --* 

            Description of the voice.

            
            

            - **Gender** *(string) --* 

              Gender of the voice.

              
            

            - **Id** *(string) --* 

              Amazon Polly assigned voice ID. This is the ID that you specify when calling the ``SynthesizeSpeech`` operation.

              
            

            - **LanguageCode** *(string) --* 

              Language code of the voice.

              
            

            - **LanguageName** *(string) --* 

              Human readable name of the language in English.

              
            

            - **Name** *(string) --* 

              Name of the voice (for example, Salli, Kendra, etc.). This provides a human readable voice name that you might display in your application.

              
        
      
    