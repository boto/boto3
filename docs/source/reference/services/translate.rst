

*********
Translate
*********

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: Translate.Client

  A low-level client representing Amazon Translate::

    
    import boto3
    
    client = boto3.client('translate')

  
  These are the available methods:
  
  *   :py:meth:`~Translate.Client.can_paginate`

  
  *   :py:meth:`~Translate.Client.generate_presigned_url`

  
  *   :py:meth:`~Translate.Client.get_paginator`

  
  *   :py:meth:`~Translate.Client.get_waiter`

  
  *   :py:meth:`~Translate.Client.translate_text`

  

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

        


  .. py:method:: translate_text(**kwargs)

    

    Translates input text from the source language to the target language. You can translate between English (en) and one of the following languages, or between one of the following languages and English.

     

     
    * Arabic (ar) 
     
    * Chinese (Simplified) (zh) 
     
    * French (fr) 
     
    * German (de) 
     
    * Portuguese (pt) 
     
    * Spanish (es) 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/translate-2017-07-01/TranslateText>`_    


    **Request Syntax** 
    ::

      response = client.translate_text(
          Text='string',
          SourceLanguageCode='string',
          TargetLanguageCode='string'
      )
    :type Text: string
    :param Text: **[REQUIRED]** 

      The text to translate.

      

    
    :type SourceLanguageCode: string
    :param SourceLanguageCode: **[REQUIRED]** 

      One of the supported language codes for the source text. If the ``TargetLanguageCode`` is not "en", the ``SourceLanguageCode`` must be "en".

      

    
    :type TargetLanguageCode: string
    :param TargetLanguageCode: **[REQUIRED]** 

      One of the supported language codes for the target text. If the ``SourceLanguageCode`` is not "en", the ``TargetLanguageCode`` must be "en".

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TranslatedText': 'string',
            'SourceLanguageCode': 'string',
            'TargetLanguageCode': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TranslatedText** *(string) --* 

          The text translated into the target language.

          
        

        - **SourceLanguageCode** *(string) --* 

          The language code for the language of the input text. 

          
        

        - **TargetLanguageCode** *(string) --* 

          The language code for the language of the translated text. 

          
    

==========
Paginators
==========


The available paginators are:
