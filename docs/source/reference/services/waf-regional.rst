

***********
WAFRegional
***********

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: WAFRegional.Client

  A low-level client representing AWS WAF Regional::

    
    import boto3
    
    client = boto3.client('waf-regional')

  
  These are the available methods:
  
  *   :py:meth:`~WAFRegional.Client.associate_web_acl`

  
  *   :py:meth:`~WAFRegional.Client.can_paginate`

  
  *   :py:meth:`~WAFRegional.Client.create_byte_match_set`

  
  *   :py:meth:`~WAFRegional.Client.create_geo_match_set`

  
  *   :py:meth:`~WAFRegional.Client.create_ip_set`

  
  *   :py:meth:`~WAFRegional.Client.create_rate_based_rule`

  
  *   :py:meth:`~WAFRegional.Client.create_regex_match_set`

  
  *   :py:meth:`~WAFRegional.Client.create_regex_pattern_set`

  
  *   :py:meth:`~WAFRegional.Client.create_rule`

  
  *   :py:meth:`~WAFRegional.Client.create_rule_group`

  
  *   :py:meth:`~WAFRegional.Client.create_size_constraint_set`

  
  *   :py:meth:`~WAFRegional.Client.create_sql_injection_match_set`

  
  *   :py:meth:`~WAFRegional.Client.create_web_acl`

  
  *   :py:meth:`~WAFRegional.Client.create_xss_match_set`

  
  *   :py:meth:`~WAFRegional.Client.delete_byte_match_set`

  
  *   :py:meth:`~WAFRegional.Client.delete_geo_match_set`

  
  *   :py:meth:`~WAFRegional.Client.delete_ip_set`

  
  *   :py:meth:`~WAFRegional.Client.delete_rate_based_rule`

  
  *   :py:meth:`~WAFRegional.Client.delete_regex_match_set`

  
  *   :py:meth:`~WAFRegional.Client.delete_regex_pattern_set`

  
  *   :py:meth:`~WAFRegional.Client.delete_rule`

  
  *   :py:meth:`~WAFRegional.Client.delete_rule_group`

  
  *   :py:meth:`~WAFRegional.Client.delete_size_constraint_set`

  
  *   :py:meth:`~WAFRegional.Client.delete_sql_injection_match_set`

  
  *   :py:meth:`~WAFRegional.Client.delete_web_acl`

  
  *   :py:meth:`~WAFRegional.Client.delete_xss_match_set`

  
  *   :py:meth:`~WAFRegional.Client.disassociate_web_acl`

  
  *   :py:meth:`~WAFRegional.Client.generate_presigned_url`

  
  *   :py:meth:`~WAFRegional.Client.get_byte_match_set`

  
  *   :py:meth:`~WAFRegional.Client.get_change_token`

  
  *   :py:meth:`~WAFRegional.Client.get_change_token_status`

  
  *   :py:meth:`~WAFRegional.Client.get_geo_match_set`

  
  *   :py:meth:`~WAFRegional.Client.get_ip_set`

  
  *   :py:meth:`~WAFRegional.Client.get_paginator`

  
  *   :py:meth:`~WAFRegional.Client.get_rate_based_rule`

  
  *   :py:meth:`~WAFRegional.Client.get_rate_based_rule_managed_keys`

  
  *   :py:meth:`~WAFRegional.Client.get_regex_match_set`

  
  *   :py:meth:`~WAFRegional.Client.get_regex_pattern_set`

  
  *   :py:meth:`~WAFRegional.Client.get_rule`

  
  *   :py:meth:`~WAFRegional.Client.get_rule_group`

  
  *   :py:meth:`~WAFRegional.Client.get_sampled_requests`

  
  *   :py:meth:`~WAFRegional.Client.get_size_constraint_set`

  
  *   :py:meth:`~WAFRegional.Client.get_sql_injection_match_set`

  
  *   :py:meth:`~WAFRegional.Client.get_waiter`

  
  *   :py:meth:`~WAFRegional.Client.get_web_acl`

  
  *   :py:meth:`~WAFRegional.Client.get_web_acl_for_resource`

  
  *   :py:meth:`~WAFRegional.Client.get_xss_match_set`

  
  *   :py:meth:`~WAFRegional.Client.list_activated_rules_in_rule_group`

  
  *   :py:meth:`~WAFRegional.Client.list_byte_match_sets`

  
  *   :py:meth:`~WAFRegional.Client.list_geo_match_sets`

  
  *   :py:meth:`~WAFRegional.Client.list_ip_sets`

  
  *   :py:meth:`~WAFRegional.Client.list_rate_based_rules`

  
  *   :py:meth:`~WAFRegional.Client.list_regex_match_sets`

  
  *   :py:meth:`~WAFRegional.Client.list_regex_pattern_sets`

  
  *   :py:meth:`~WAFRegional.Client.list_resources_for_web_acl`

  
  *   :py:meth:`~WAFRegional.Client.list_rule_groups`

  
  *   :py:meth:`~WAFRegional.Client.list_rules`

  
  *   :py:meth:`~WAFRegional.Client.list_size_constraint_sets`

  
  *   :py:meth:`~WAFRegional.Client.list_sql_injection_match_sets`

  
  *   :py:meth:`~WAFRegional.Client.list_subscribed_rule_groups`

  
  *   :py:meth:`~WAFRegional.Client.list_web_acls`

  
  *   :py:meth:`~WAFRegional.Client.list_xss_match_sets`

  
  *   :py:meth:`~WAFRegional.Client.update_byte_match_set`

  
  *   :py:meth:`~WAFRegional.Client.update_geo_match_set`

  
  *   :py:meth:`~WAFRegional.Client.update_ip_set`

  
  *   :py:meth:`~WAFRegional.Client.update_rate_based_rule`

  
  *   :py:meth:`~WAFRegional.Client.update_regex_match_set`

  
  *   :py:meth:`~WAFRegional.Client.update_regex_pattern_set`

  
  *   :py:meth:`~WAFRegional.Client.update_rule`

  
  *   :py:meth:`~WAFRegional.Client.update_rule_group`

  
  *   :py:meth:`~WAFRegional.Client.update_size_constraint_set`

  
  *   :py:meth:`~WAFRegional.Client.update_sql_injection_match_set`

  
  *   :py:meth:`~WAFRegional.Client.update_web_acl`

  
  *   :py:meth:`~WAFRegional.Client.update_xss_match_set`

  

  .. py:method:: associate_web_acl(**kwargs)

    

    Associates a web ACL with a resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/AssociateWebACL>`_    


    **Request Syntax** 
    ::

      response = client.associate_web_acl(
          WebACLId='string',
          ResourceArn='string'
      )
    :type WebACLId: string
    :param WebACLId: **[REQUIRED]** 

      A unique identifier (ID) for the web ACL.

      

    
    :type ResourceArn: string
    :param ResourceArn: **[REQUIRED]** 

      The ARN (Amazon Resource Name) of the resource to be protected.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

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


  .. py:method:: create_byte_match_set(**kwargs)

    

    Creates a ``ByteMatchSet`` . You then use  UpdateByteMatchSet to identify the part of a web request that you want AWS WAF to inspect, such as the values of the ``User-Agent`` header or the query string. For example, you can create a ``ByteMatchSet`` that matches any requests with ``User-Agent`` headers that contain the string ``BadBot`` . You can then configure AWS WAF to reject those requests.

     

    To create and configure a ``ByteMatchSet`` , perform the following steps:

     

     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of a ``CreateByteMatchSet`` request. 
     
    * Submit a ``CreateByteMatchSet`` request. 
     
    * Use ``GetChangeToken`` to get the change token that you provide in the ``ChangeToken`` parameter of an ``UpdateByteMatchSet`` request. 
     
    * Submit an  UpdateByteMatchSet request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the value that you want AWS WAF to watch for. 
     

     

    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the `AWS WAF Developer Guide <http://docs.aws.amazon.com/waf/latest/developerguide/>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/CreateByteMatchSet>`_    


    **Request Syntax** 
    ::

      response = client.create_byte_match_set(
          Name='string',
          ChangeToken='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      A friendly name or description of the  ByteMatchSet . You can't change ``Name`` after you create a ``ByteMatchSet`` .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ByteMatchSet': {
                'ByteMatchSetId': 'string',
                'Name': 'string',
                'ByteMatchTuples': [
                    {
                        'FieldToMatch': {
                            'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
                            'Data': 'string'
                        },
                        'TargetString': b'bytes',
                        'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE',
                        'PositionalConstraint': 'EXACTLY'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CONTAINS_WORD'
                    },
                ]
            },
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ByteMatchSet** *(dict) --* 

          A  ByteMatchSet that contains no ``ByteMatchTuple`` objects.

          
          

          - **ByteMatchSetId** *(string) --* 

            The ``ByteMatchSetId`` for a ``ByteMatchSet`` . You use ``ByteMatchSetId`` to get information about a ``ByteMatchSet`` (see  GetByteMatchSet ), update a ``ByteMatchSet`` (see  UpdateByteMatchSet ), insert a ``ByteMatchSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete a ``ByteMatchSet`` from AWS WAF (see  DeleteByteMatchSet ).

             

             ``ByteMatchSetId`` is returned by  CreateByteMatchSet and by  ListByteMatchSets .

            
          

          - **Name** *(string) --* 

            A friendly name or description of the  ByteMatchSet . You can't change ``Name`` after you create a ``ByteMatchSet`` .

            
          

          - **ByteMatchTuples** *(list) --* 

            Specifies the bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests, the location in requests that you want AWS WAF to search, and other settings.

            
            

            - *(dict) --* 

              The bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests, the location in requests that you want AWS WAF to search, and other settings.

              
              

              - **FieldToMatch** *(dict) --* 

                The part of a web request that you want AWS WAF to search, such as a specified header or a query string. For more information, see  FieldToMatch .

                
                

                - **Type** *(string) --* 

                  The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

                   

                   
                  * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the header in ``Data`` . 
                   
                  * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` . 
                   
                  * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a ``?`` character, if any. 
                   
                  * ``URI`` : The part of a web request that identifies a resource, for example, ``/images/daily-ad.jpg`` . 
                   
                  * ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .  
                   

                  
                

                - **Data** *(string) --* 

                  When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . If the value of ``Type`` is any other value, omit ``Data`` .

                   

                  The name of the header is not case sensitive.

                  
            
              

              - **TargetString** *(bytes) --* 

                The value that you want AWS WAF to search for. AWS WAF searches for the specified string in the part of web requests that you specified in ``FieldToMatch`` . The maximum length of the value is 50 bytes.

                 

                Valid values depend on the values that you specified for ``FieldToMatch`` :

                 

                 
                * ``HEADER`` : The value that you want AWS WAF to search for in the request header that you specified in  FieldToMatch , for example, the value of the ``User-Agent`` or ``Referer`` header. 
                 
                * ``METHOD`` : The HTTP method, which indicates the type of operation specified in the request. CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` . 
                 
                * ``QUERY_STRING`` : The value that you want AWS WAF to search for in the query string, which is the part of a URL that appears after a ``?`` character. 
                 
                * ``URI`` : The value that you want AWS WAF to search for in the part of a URL that identifies a resource, for example, ``/images/daily-ad.jpg`` . 
                 
                * ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .  
                 

                 

                If ``TargetString`` includes alphabetic characters A-Z and a-z, note that the value is case sensitive.

                 

                 **If you're using the AWS WAF API**  

                 

                Specify a base64-encoded version of the value. The maximum length of the value before you base64-encode it is 50 bytes.

                 

                For example, suppose the value of ``Type`` is ``HEADER`` and the value of ``Data`` is ``User-Agent`` . If you want to search the ``User-Agent`` header for the value ``BadBot`` , you base64-encode ``BadBot`` using MIME base64 encoding and include the resulting value, ``QmFkQm90`` , in the value of ``TargetString`` .

                 

                 **If you're using the AWS CLI or one of the AWS SDKs**  

                 

                The value that you want AWS WAF to search for. The SDK automatically base64 encodes the value.

                
              

              - **TextTransformation** *(string) --* 

                Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on ``TargetString`` before inspecting a request for a match.

                 

                 **CMD_LINE**  

                 

                When you're concerned that attackers are injecting an operating system commandline command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

                 

                 
                * Delete the following characters: \ " ' ^ 
                 
                * Delete spaces before the following characters: / ( 
                 
                * Replace the following characters with a space: , ; 
                 
                * Replace multiple spaces with one space 
                 
                * Convert uppercase letters (A-Z) to lowercase (a-z) 
                 

                 

                 **COMPRESS_WHITE_SPACE**  

                 

                Use this option to replace the following characters with a space character (decimal 32):

                 

                 
                * \f, formfeed, decimal 12 
                 
                * \t, tab, decimal 9 
                 
                * \n, newline, decimal 10 
                 
                * \r, carriage return, decimal 13 
                 
                * \v, vertical tab, decimal 11 
                 
                * non-breaking space, decimal 160 
                 

                 

                 ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

                 

                 **HTML_ENTITY_DECODE**  

                 

                Use this option to replace HTML-encoded characters with unencoded characters. ``HTML_ENTITY_DECODE`` performs the following operations:

                 

                 
                * Replaces ``(ampersand)quot;`` with ``"``   
                 
                * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160 
                 
                * Replaces ``(ampersand)lt;`` with a "less than" symbol 
                 
                * Replaces ``(ampersand)gt;`` with ``>``   
                 
                * Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` , with the corresponding characters 
                 
                * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with the corresponding characters 
                 

                 

                 **LOWERCASE**  

                 

                Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

                 

                 **URL_DECODE**  

                 

                Use this option to decode a URL-encoded value.

                 

                 **NONE**  

                 

                Specify ``NONE`` if you don't want to perform any text transformations.

                
              

              - **PositionalConstraint** *(string) --* 

                Within the portion of a web request that you want to search (for example, in the query string, if any), specify where you want AWS WAF to search. Valid values include the following:

                 

                 **CONTAINS**  

                 

                The specified part of the web request must include the value of ``TargetString`` , but the location doesn't matter.

                 

                 **CONTAINS_WORD**  

                 

                The specified part of the web request must include the value of ``TargetString`` , and ``TargetString`` must contain only alphanumeric characters or underscore (A-Z, a-z, 0-9, or _). In addition, ``TargetString`` must be a word, which means one of the following:

                 

                 
                * ``TargetString`` exactly matches the value of the specified part of the web request, such as the value of a header. 
                 
                * ``TargetString`` is at the beginning of the specified part of the web request and is followed by a character other than an alphanumeric character or underscore (_), for example, ``BadBot;`` . 
                 
                * ``TargetString`` is at the end of the specified part of the web request and is preceded by a character other than an alphanumeric character or underscore (_), for example, ``;BadBot`` . 
                 
                * ``TargetString`` is in the middle of the specified part of the web request and is preceded and followed by characters other than alphanumeric characters or underscore (_), for example, ``-BadBot;`` . 
                 

                 

                 **EXACTLY**  

                 

                The value of the specified part of the web request must exactly match the value of ``TargetString`` .

                 

                 **STARTS_WITH**  

                 

                The value of ``TargetString`` must appear at the beginning of the specified part of the web request.

                 

                 **ENDS_WITH**  

                 

                The value of ``TargetString`` must appear at the end of the specified part of the web request.

                
          
        
      
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``CreateByteMatchSet`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

  .. py:method:: create_geo_match_set(**kwargs)

    

    Creates an  GeoMatchSet , which you use to specify which web requests you want to allow or block based on the country that the requests originate from. For example, if you're receiving a lot of requests from one or more countries and you want to block the requests, you can create an ``GeoMatchSet`` that contains those countries and then configure AWS WAF to block the requests. 

     

    To create and configure a ``GeoMatchSet`` , perform the following steps:

     

     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of a ``CreateGeoMatchSet`` request. 
     
    * Submit a ``CreateGeoMatchSet`` request. 
     
    * Use ``GetChangeToken`` to get the change token that you provide in the ``ChangeToken`` parameter of an  UpdateGeoMatchSet request. 
     
    * Submit an ``UpdateGeoMatchSetSet`` request to specify the countries that you want AWS WAF to watch for. 
     

     

    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the `AWS WAF Developer Guide <http://docs.aws.amazon.com/waf/latest/developerguide/>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/CreateGeoMatchSet>`_    


    **Request Syntax** 
    ::

      response = client.create_geo_match_set(
          Name='string',
          ChangeToken='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      A friendly name or description of the  GeoMatchSet . You can't change ``Name`` after you create the ``GeoMatchSet`` .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'GeoMatchSet': {
                'GeoMatchSetId': 'string',
                'Name': 'string',
                'GeoMatchConstraints': [
                    {
                        'Type': 'Country',
                        'Value': 'AF'|'AX'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'|'BH'|'BD'|'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BQ'|'BA'|'BW'|'BV'|'BR'|'IO'|'BN'|'BG'|'BF'|'BI'|'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'|'CG'|'CD'|'CK'|'CR'|'CI'|'HR'|'CU'|'CW'|'CY'|'CZ'|'DK'|'DJ'|'DM'|'DO'|'EC'|'EG'|'SV'|'GQ'|'ER'|'EE'|'ET'|'FK'|'FO'|'FJ'|'FI'|'FR'|'GF'|'PF'|'TF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'|'GR'|'GL'|'GD'|'GP'|'GU'|'GT'|'GG'|'GN'|'GW'|'GY'|'HT'|'HM'|'VA'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'|'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KP'|'KR'|'KW'|'KG'|'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'|'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'|'MT'|'MH'|'MQ'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'|'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'|'NR'|'NP'|'NL'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'|'NF'|'MP'|'NO'|'OM'|'PK'|'PW'|'PS'|'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'RE'|'RO'|'RU'|'RW'|'BL'|'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'|'SC'|'SL'|'SG'|'SX'|'SK'|'SI'|'SB'|'SO'|'ZA'|'GS'|'SS'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'|'CH'|'SY'|'TW'|'TJ'|'TZ'|'TH'|'TL'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'UG'|'UA'|'AE'|'GB'|'US'|'UM'|'UY'|'UZ'|'VU'|'VE'|'VN'|'VG'|'VI'|'WF'|'EH'|'YE'|'ZM'|'ZW'
                    },
                ]
            },
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **GeoMatchSet** *(dict) --* 

          The  GeoMatchSet returned in the ``CreateGeoMatchSet`` response. The ``GeoMatchSet`` contains no ``GeoMatchConstraints`` .

          
          

          - **GeoMatchSetId** *(string) --* 

            The ``GeoMatchSetId`` for an ``GeoMatchSet`` . You use ``GeoMatchSetId`` to get information about a ``GeoMatchSet`` (see  GeoMatchSet ), update a ``GeoMatchSet`` (see  UpdateGeoMatchSet ), insert a ``GeoMatchSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete a ``GeoMatchSet`` from AWS WAF (see  DeleteGeoMatchSet ).

             

             ``GeoMatchSetId`` is returned by  CreateGeoMatchSet and by  ListGeoMatchSets .

            
          

          - **Name** *(string) --* 

            A friendly name or description of the  GeoMatchSet . You can't change the name of an ``GeoMatchSet`` after you create it.

            
          

          - **GeoMatchConstraints** *(list) --* 

            An array of  GeoMatchConstraint objects, which contain the country that you want AWS WAF to search for.

            
            

            - *(dict) --* 

              The country from which web requests originate that you want AWS WAF to search for.

              
              

              - **Type** *(string) --* 

                The type of geographical area you want AWS WAF to search for. Currently ``Country`` is the only valid value.

                
              

              - **Value** *(string) --* 

                The country that you want AWS WAF to search for.

                
          
        
      
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``CreateGeoMatchSet`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

  .. py:method:: create_ip_set(**kwargs)

    

    Creates an  IPSet , which you use to specify which web requests you want to allow or block based on the IP addresses that the requests originate from. For example, if you're receiving a lot of requests from one or more individual IP addresses or one or more ranges of IP addresses and you want to block the requests, you can create an ``IPSet`` that contains those IP addresses and then configure AWS WAF to block the requests. 

     

    To create and configure an ``IPSet`` , perform the following steps:

     

     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of a ``CreateIPSet`` request. 
     
    * Submit a ``CreateIPSet`` request. 
     
    * Use ``GetChangeToken`` to get the change token that you provide in the ``ChangeToken`` parameter of an  UpdateIPSet request. 
     
    * Submit an ``UpdateIPSet`` request to specify the IP addresses that you want AWS WAF to watch for. 
     

     

    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the `AWS WAF Developer Guide <http://docs.aws.amazon.com/waf/latest/developerguide/>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/CreateIPSet>`_    


    **Request Syntax** 
    ::

      response = client.create_ip_set(
          Name='string',
          ChangeToken='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      A friendly name or description of the  IPSet . You can't change ``Name`` after you create the ``IPSet`` .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'IPSet': {
                'IPSetId': 'string',
                'Name': 'string',
                'IPSetDescriptors': [
                    {
                        'Type': 'IPV4'|'IPV6',
                        'Value': 'string'
                    },
                ]
            },
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **IPSet** *(dict) --* 

          The  IPSet returned in the ``CreateIPSet`` response.

          
          

          - **IPSetId** *(string) --* 

            The ``IPSetId`` for an ``IPSet`` . You use ``IPSetId`` to get information about an ``IPSet`` (see  GetIPSet ), update an ``IPSet`` (see  UpdateIPSet ), insert an ``IPSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete an ``IPSet`` from AWS WAF (see  DeleteIPSet ).

             

             ``IPSetId`` is returned by  CreateIPSet and by  ListIPSets .

            
          

          - **Name** *(string) --* 

            A friendly name or description of the  IPSet . You can't change the name of an ``IPSet`` after you create it.

            
          

          - **IPSetDescriptors** *(list) --* 

            The IP address type (``IPV4`` or ``IPV6`` ) and the IP address range (in CIDR notation) that web requests originate from. If the ``WebACL`` is associated with a CloudFront distribution and the viewer did not use an HTTP proxy or a load balancer to send the request, this is the value of the c-ip field in the CloudFront access logs.

            
            

            - *(dict) --* 

              Specifies the IP address type (``IPV4`` or ``IPV6`` ) and the IP address range (in CIDR format) that web requests originate from.

              
              

              - **Type** *(string) --* 

                Specify ``IPV4`` or ``IPV6`` .

                
              

              - **Value** *(string) --* 

                Specify an IPv4 address by using CIDR notation. For example:

                 

                 
                * To configure AWS WAF to allow, block, or count requests that originated from the IP address 192.0.2.44, specify ``192.0.2.44/32`` . 
                 
                * To configure AWS WAF to allow, block, or count requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify ``192.0.2.0/24`` . 
                 

                 

                For more information about CIDR notation, see the Wikipedia entry `Classless Inter-Domain Routing <https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`__ .

                 

                Specify an IPv6 address by using CIDR notation. For example:

                 

                 
                * To configure AWS WAF to allow, block, or count requests that originated from the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify ``1111:0000:0000:0000:0000:0000:0000:0111/128`` . 
                 
                * To configure AWS WAF to allow, block, or count requests that originated from IP addresses 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify ``1111:0000:0000:0000:0000:0000:0000:0000/64`` . 
                 

                
          
        
      
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``CreateIPSet`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

    **Examples** 

    The following example creates an IP match set named MyIPSetFriendlyName.
    ::

      response = client.create_ip_set(
          ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          Name='MyIPSetFriendlyName',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          'IPSet': {
              'IPSetDescriptors': [
                  {
                      'Type': 'IPV4',
                      'Value': '192.0.2.44/32',
                  },
              ],
              'IPSetId': 'example1ds3t-46da-4fdb-b8d5-abc321j569j5',
              'Name': 'MyIPSetFriendlyName',
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_rate_based_rule(**kwargs)

    

    Creates a  RateBasedRule . The ``RateBasedRule`` contains a ``RateLimit`` , which specifies the maximum number of requests that AWS WAF allows from a specified IP address in a five-minute period. The ``RateBasedRule`` also contains the ``IPSet`` objects, ``ByteMatchSet`` objects, and other predicates that identify the requests that you want to count or block if these requests exceed the ``RateLimit`` .

     

    If you add more than one predicate to a ``RateBasedRule`` , a request not only must exceed the ``RateLimit`` , but it also must match all the specifications to be counted or blocked. For example, suppose you add the following to a ``RateBasedRule`` :

     

     
    * An ``IPSet`` that matches the IP address ``192.0.2.44/32``   
     
    * A ``ByteMatchSet`` that matches ``BadBot`` in the ``User-Agent`` header 
     

     

    Further, you specify a ``RateLimit`` of 15,000.

     

    You then add the ``RateBasedRule`` to a ``WebACL`` and specify that you want to block requests that meet the conditions in the rule. For a request to be blocked, it must come from the IP address 192.0.2.44 *and* the ``User-Agent`` header in the request must contain the value ``BadBot`` . Further, requests that match these two conditions must be received at a rate of more than 15,000 requests every five minutes. If both conditions are met and the rate is exceeded, AWS WAF blocks the requests. If the rate drops below 15,000 for a five-minute period, AWS WAF no longer blocks the requests.

     

    As a second example, suppose you want to limit requests to a particular page on your site. To do this, you could add the following to a ``RateBasedRule`` :

     

     
    * A ``ByteMatchSet`` with ``FieldToMatch`` of ``URI``   
     
    * A ``PositionalConstraint`` of ``STARTS_WITH``   
     
    * A ``TargetString`` of ``login``   
     

     

    Further, you specify a ``RateLimit`` of 15,000.

     

    By adding this ``RateBasedRule`` to a ``WebACL`` , you could limit requests to your login page without affecting the rest of your site.

     

    To create and configure a ``RateBasedRule`` , perform the following steps:

     

     
    * Create and update the predicates that you want to include in the rule. For more information, see  CreateByteMatchSet ,  CreateIPSet , and  CreateSqlInjectionMatchSet . 
     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of a ``CreateRule`` request. 
     
    * Submit a ``CreateRateBasedRule`` request. 
     
    * Use ``GetChangeToken`` to get the change token that you provide in the ``ChangeToken`` parameter of an  UpdateRule request. 
     
    * Submit an ``UpdateRateBasedRule`` request to specify the predicates that you want to include in the rule. 
     
    * Create and update a ``WebACL`` that contains the ``RateBasedRule`` . For more information, see  CreateWebACL . 
     

     

    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the `AWS WAF Developer Guide <http://docs.aws.amazon.com/waf/latest/developerguide/>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/CreateRateBasedRule>`_    


    **Request Syntax** 
    ::

      response = client.create_rate_based_rule(
          Name='string',
          MetricName='string',
          RateKey='IP',
          RateLimit=123,
          ChangeToken='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      A friendly name or description of the  RateBasedRule . You can't change the name of a ``RateBasedRule`` after you create it.

      

    
    :type MetricName: string
    :param MetricName: **[REQUIRED]** 

      A friendly name or description for the metrics for this ``RateBasedRule`` . The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace. You can't change the name of the metric after you create the ``RateBasedRule`` .

      

    
    :type RateKey: string
    :param RateKey: **[REQUIRED]** 

      The field that AWS WAF uses to determine if requests are likely arriving from a single source and thus subject to rate monitoring. The only valid value for ``RateKey`` is ``IP`` . ``IP`` indicates that requests that arrive from the same IP address are subject to the ``RateLimit`` that is specified in the ``RateBasedRule`` .

      

    
    :type RateLimit: integer
    :param RateLimit: **[REQUIRED]** 

      The maximum number of requests, which have an identical value in the field that is specified by ``RateKey`` , allowed in a five-minute period. If the number of requests exceeds the ``RateLimit`` and the other predicates specified in the rule are also met, AWS WAF triggers the action that is specified for this rule.

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The ``ChangeToken`` that you used to submit the ``CreateRateBasedRule`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Rule': {
                'RuleId': 'string',
                'Name': 'string',
                'MetricName': 'string',
                'MatchPredicates': [
                    {
                        'Negated': True|False,
                        'Type': 'IPMatch'|'ByteMatch'|'SqlInjectionMatch'|'GeoMatch'|'SizeConstraint'|'XssMatch'|'RegexMatch',
                        'DataId': 'string'
                    },
                ],
                'RateKey': 'IP',
                'RateLimit': 123
            },
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Rule** *(dict) --* 

          The  RateBasedRule that is returned in the ``CreateRateBasedRule`` response.

          
          

          - **RuleId** *(string) --* 

            A unique identifier for a ``RateBasedRule`` . You use ``RuleId`` to get more information about a ``RateBasedRule`` (see  GetRateBasedRule ), update a ``RateBasedRule`` (see  UpdateRateBasedRule ), insert a ``RateBasedRule`` into a ``WebACL`` or delete one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``RateBasedRule`` from AWS WAF (see  DeleteRateBasedRule ).

            
          

          - **Name** *(string) --* 

            A friendly name or description for a ``RateBasedRule`` . You can't change the name of a ``RateBasedRule`` after you create it.

            
          

          - **MetricName** *(string) --* 

            A friendly name or description for the metrics for a ``RateBasedRule`` . The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace. You can't change the name of the metric after you create the ``RateBasedRule`` .

            
          

          - **MatchPredicates** *(list) --* 

            The ``Predicates`` object contains one ``Predicate`` element for each  ByteMatchSet ,  IPSet , or  SqlInjectionMatchSet object that you want to include in a ``RateBasedRule`` .

            
            

            - *(dict) --* 

              Specifies the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , and  SizeConstraintSet objects that you want to add to a ``Rule`` and, for each object, indicates whether you want to negate the settings, for example, requests that do NOT originate from the IP address 192.0.2.44. 

              
              

              - **Negated** *(boolean) --* 

                Set ``Negated`` to ``False`` if you want AWS WAF to allow, block, or count requests based on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow or block requests based on that IP address.

                 

                Set ``Negated`` to ``True`` if you want AWS WAF to allow or block a request based on the negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow, block, or count requests based on all IP addresses *except*  ``192.0.2.44`` .

                
              

              - **Type** *(string) --* 

                The type of predicate in a ``Rule`` , such as ``ByteMatchSet`` or ``IPSet`` .

                
              

              - **DataId** *(string) --* 

                A unique identifier for a predicate in a ``Rule`` , such as ``ByteMatchSetId`` or ``IPSetId`` . The ID is returned by the corresponding ``Create`` or ``List`` command.

                
          
        
          

          - **RateKey** *(string) --* 

            The field that AWS WAF uses to determine if requests are likely arriving from single source and thus subject to rate monitoring. The only valid value for ``RateKey`` is ``IP`` . ``IP`` indicates that requests arriving from the same IP address are subject to the ``RateLimit`` that is specified in the ``RateBasedRule`` .

            
          

          - **RateLimit** *(integer) --* 

            The maximum number of requests, which have an identical value in the field specified by the ``RateKey`` , allowed in a five-minute period. If the number of requests exceeds the ``RateLimit`` and the other predicates specified in the rule are also met, AWS WAF triggers the action that is specified for this rule.

            
      
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``CreateRateBasedRule`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

  .. py:method:: create_regex_match_set(**kwargs)

    

    Creates a  RegexMatchSet . You then use  UpdateRegexMatchSet to identify the part of a web request that you want AWS WAF to inspect, such as the values of the ``User-Agent`` header or the query string. For example, you can create a ``RegexMatchSet`` that contains a ``RegexMatchTuple`` that looks for any requests with ``User-Agent`` headers that match a ``RegexPatternSet`` with pattern ``B[a@]dB[o0]t`` . You can then configure AWS WAF to reject those requests.

     

    To create and configure a ``RegexMatchSet`` , perform the following steps:

     

     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of a ``CreateRegexMatchSet`` request. 
     
    * Submit a ``CreateRegexMatchSet`` request. 
     
    * Use ``GetChangeToken`` to get the change token that you provide in the ``ChangeToken`` parameter of an ``UpdateRegexMatchSet`` request. 
     
    * Submit an  UpdateRegexMatchSet request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the value, using a ``RegexPatternSet`` , that you want AWS WAF to watch for. 
     

     

    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the `AWS WAF Developer Guide <http://docs.aws.amazon.com/waf/latest/developerguide/>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/CreateRegexMatchSet>`_    


    **Request Syntax** 
    ::

      response = client.create_regex_match_set(
          Name='string',
          ChangeToken='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      A friendly name or description of the  RegexMatchSet . You can't change ``Name`` after you create a ``RegexMatchSet`` .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'RegexMatchSet': {
                'RegexMatchSetId': 'string',
                'Name': 'string',
                'RegexMatchTuples': [
                    {
                        'FieldToMatch': {
                            'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
                            'Data': 'string'
                        },
                        'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE',
                        'RegexPatternSetId': 'string'
                    },
                ]
            },
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **RegexMatchSet** *(dict) --* 

          A  RegexMatchSet that contains no ``RegexMatchTuple`` objects.

          
          

          - **RegexMatchSetId** *(string) --* 

            The ``RegexMatchSetId`` for a ``RegexMatchSet`` . You use ``RegexMatchSetId`` to get information about a ``RegexMatchSet`` (see  GetRegexMatchSet ), update a ``RegexMatchSet`` (see  UpdateRegexMatchSet ), insert a ``RegexMatchSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete a ``RegexMatchSet`` from AWS WAF (see  DeleteRegexMatchSet ).

             

             ``RegexMatchSetId`` is returned by  CreateRegexMatchSet and by  ListRegexMatchSets .

            
          

          - **Name** *(string) --* 

            A friendly name or description of the  RegexMatchSet . You can't change ``Name`` after you create a ``RegexMatchSet`` .

            
          

          - **RegexMatchTuples** *(list) --* 

            Contains an array of  RegexMatchTuple objects. Each ``RegexMatchTuple`` object contains: 

             

             
            * The part of a web request that you want AWS WAF to inspect, such as a query string or the value of the ``User-Agent`` header.  
             
            * The identifier of the pattern (a regular expression) that you want AWS WAF to look for. For more information, see  RegexPatternSet . 
             
            * Whether to perform any conversions on the request, such as converting it to lowercase, before inspecting it for the specified string. 
             

            
            

            - *(dict) --* 

              The regular expression pattern that you want AWS WAF to search for in web requests, the location in requests that you want AWS WAF to search, and other settings. Each ``RegexMatchTuple`` object contains: 

               

               
              * The part of a web request that you want AWS WAF to inspect, such as a query string or the value of the ``User-Agent`` header.  
               
              * The identifier of the pattern (a regular expression) that you want AWS WAF to look for. For more information, see  RegexPatternSet .  
               
              * Whether to perform any conversions on the request, such as converting it to lowercase, before inspecting it for the specified string. 
               

              
              

              - **FieldToMatch** *(dict) --* 

                Specifies where in a web request to look for the ``RegexPatternSet`` .

                
                

                - **Type** *(string) --* 

                  The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

                   

                   
                  * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the header in ``Data`` . 
                   
                  * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` . 
                   
                  * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a ``?`` character, if any. 
                   
                  * ``URI`` : The part of a web request that identifies a resource, for example, ``/images/daily-ad.jpg`` . 
                   
                  * ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .  
                   

                  
                

                - **Data** *(string) --* 

                  When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . If the value of ``Type`` is any other value, omit ``Data`` .

                   

                  The name of the header is not case sensitive.

                  
            
              

              - **TextTransformation** *(string) --* 

                Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on ``RegexPatternSet`` before inspecting a request for a match.

                 

                 **CMD_LINE**  

                 

                When you're concerned that attackers are injecting an operating system commandline command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

                 

                 
                * Delete the following characters: \ " ' ^ 
                 
                * Delete spaces before the following characters: / ( 
                 
                * Replace the following characters with a space: , ; 
                 
                * Replace multiple spaces with one space 
                 
                * Convert uppercase letters (A-Z) to lowercase (a-z) 
                 

                 

                 **COMPRESS_WHITE_SPACE**  

                 

                Use this option to replace the following characters with a space character (decimal 32):

                 

                 
                * \f, formfeed, decimal 12 
                 
                * \t, tab, decimal 9 
                 
                * \n, newline, decimal 10 
                 
                * \r, carriage return, decimal 13 
                 
                * \v, vertical tab, decimal 11 
                 
                * non-breaking space, decimal 160 
                 

                 

                 ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

                 

                 **HTML_ENTITY_DECODE**  

                 

                Use this option to replace HTML-encoded characters with unencoded characters. ``HTML_ENTITY_DECODE`` performs the following operations:

                 

                 
                * Replaces ``(ampersand)quot;`` with ``"``   
                 
                * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160 
                 
                * Replaces ``(ampersand)lt;`` with a "less than" symbol 
                 
                * Replaces ``(ampersand)gt;`` with ``>``   
                 
                * Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` , with the corresponding characters 
                 
                * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with the corresponding characters 
                 

                 

                 **LOWERCASE**  

                 

                Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

                 

                 **URL_DECODE**  

                 

                Use this option to decode a URL-encoded value.

                 

                 **NONE**  

                 

                Specify ``NONE`` if you don't want to perform any text transformations.

                
              

              - **RegexPatternSetId** *(string) --* 

                The ``RegexPatternSetId`` for a ``RegexPatternSet`` . You use ``RegexPatternSetId`` to get information about a ``RegexPatternSet`` (see  GetRegexPatternSet ), update a ``RegexPatternSet`` (see  UpdateRegexPatternSet ), insert a ``RegexPatternSet`` into a ``RegexMatchSet`` or delete one from a ``RegexMatchSet`` (see  UpdateRegexMatchSet ), and delete an ``RegexPatternSet`` from AWS WAF (see  DeleteRegexPatternSet ).

                 

                 ``RegexPatternSetId`` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .

                
          
        
      
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``CreateRegexMatchSet`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

  .. py:method:: create_regex_pattern_set(**kwargs)

    

    Creates a ``RegexPatternSet`` . You then use  UpdateRegexPatternSet to specify the regular expression (regex) pattern that you want AWS WAF to search for, such as ``B[a@]dB[o0]t`` . You can then configure AWS WAF to reject those requests.

     

    To create and configure a ``RegexPatternSet`` , perform the following steps:

     

     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of a ``CreateRegexPatternSet`` request. 
     
    * Submit a ``CreateRegexPatternSet`` request. 
     
    * Use ``GetChangeToken`` to get the change token that you provide in the ``ChangeToken`` parameter of an ``UpdateRegexPatternSet`` request. 
     
    * Submit an  UpdateRegexPatternSet request to specify the string that you want AWS WAF to watch for. 
     

     

    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the `AWS WAF Developer Guide <http://docs.aws.amazon.com/waf/latest/developerguide/>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/CreateRegexPatternSet>`_    


    **Request Syntax** 
    ::

      response = client.create_regex_pattern_set(
          Name='string',
          ChangeToken='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      A friendly name or description of the  RegexPatternSet . You can't change ``Name`` after you create a ``RegexPatternSet`` .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'RegexPatternSet': {
                'RegexPatternSetId': 'string',
                'Name': 'string',
                'RegexPatternStrings': [
                    'string',
                ]
            },
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **RegexPatternSet** *(dict) --* 

          A  RegexPatternSet that contains no objects.

          
          

          - **RegexPatternSetId** *(string) --* 

            The identifier for the ``RegexPatternSet`` . You use ``RegexPatternSetId`` to get information about a ``RegexPatternSet`` , update a ``RegexPatternSet`` , remove a ``RegexPatternSet`` from a ``RegexMatchSet`` , and delete a ``RegexPatternSet`` from AWS WAF.

             

             ``RegexMatchSetId`` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .

            
          

          - **Name** *(string) --* 

            A friendly name or description of the  RegexPatternSet . You can't change ``Name`` after you create a ``RegexPatternSet`` .

            
          

          - **RegexPatternStrings** *(list) --* 

            Specifies the regular expression (regex) patterns that you want AWS WAF to search for, such as ``B[a@]dB[o0]t`` .

            
            

            - *(string) --* 
        
      
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``CreateRegexPatternSet`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

  .. py:method:: create_rule(**kwargs)

    

    Creates a ``Rule`` , which contains the ``IPSet`` objects, ``ByteMatchSet`` objects, and other predicates that identify the requests that you want to block. If you add more than one predicate to a ``Rule`` , a request must match all of the specifications to be allowed or blocked. For example, suppose you add the following to a ``Rule`` :

     

     
    * An ``IPSet`` that matches the IP address ``192.0.2.44/32``   
     
    * A ``ByteMatchSet`` that matches ``BadBot`` in the ``User-Agent`` header 
     

     

    You then add the ``Rule`` to a ``WebACL`` and specify that you want to blocks requests that satisfy the ``Rule`` . For a request to be blocked, it must come from the IP address 192.0.2.44 *and* the ``User-Agent`` header in the request must contain the value ``BadBot`` .

     

    To create and configure a ``Rule`` , perform the following steps:

     

     
    * Create and update the predicates that you want to include in the ``Rule`` . For more information, see  CreateByteMatchSet ,  CreateIPSet , and  CreateSqlInjectionMatchSet . 
     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of a ``CreateRule`` request. 
     
    * Submit a ``CreateRule`` request. 
     
    * Use ``GetChangeToken`` to get the change token that you provide in the ``ChangeToken`` parameter of an  UpdateRule request. 
     
    * Submit an ``UpdateRule`` request to specify the predicates that you want to include in the ``Rule`` . 
     
    * Create and update a ``WebACL`` that contains the ``Rule`` . For more information, see  CreateWebACL . 
     

     

    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the `AWS WAF Developer Guide <http://docs.aws.amazon.com/waf/latest/developerguide/>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/CreateRule>`_    


    **Request Syntax** 
    ::

      response = client.create_rule(
          Name='string',
          MetricName='string',
          ChangeToken='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      A friendly name or description of the  Rule . You can't change the name of a ``Rule`` after you create it.

      

    
    :type MetricName: string
    :param MetricName: **[REQUIRED]** 

      A friendly name or description for the metrics for this ``Rule`` . The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace. You can't change the name of the metric after you create the ``Rule`` .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Rule': {
                'RuleId': 'string',
                'Name': 'string',
                'MetricName': 'string',
                'Predicates': [
                    {
                        'Negated': True|False,
                        'Type': 'IPMatch'|'ByteMatch'|'SqlInjectionMatch'|'GeoMatch'|'SizeConstraint'|'XssMatch'|'RegexMatch',
                        'DataId': 'string'
                    },
                ]
            },
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Rule** *(dict) --* 

          The  Rule returned in the ``CreateRule`` response.

          
          

          - **RuleId** *(string) --* 

            A unique identifier for a ``Rule`` . You use ``RuleId`` to get more information about a ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule`` from AWS WAF (see  DeleteRule ).

             

             ``RuleId`` is returned by  CreateRule and by  ListRules .

            
          

          - **Name** *(string) --* 

            The friendly name or description for the ``Rule`` . You can't change the name of a ``Rule`` after you create it.

            
          

          - **MetricName** *(string) --* 

            A friendly name or description for the metrics for this ``Rule`` . The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace. You can't change ``MetricName`` after you create the ``Rule`` .

            
          

          - **Predicates** *(list) --* 

            The ``Predicates`` object contains one ``Predicate`` element for each  ByteMatchSet ,  IPSet , or  SqlInjectionMatchSet object that you want to include in a ``Rule`` .

            
            

            - *(dict) --* 

              Specifies the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , and  SizeConstraintSet objects that you want to add to a ``Rule`` and, for each object, indicates whether you want to negate the settings, for example, requests that do NOT originate from the IP address 192.0.2.44. 

              
              

              - **Negated** *(boolean) --* 

                Set ``Negated`` to ``False`` if you want AWS WAF to allow, block, or count requests based on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow or block requests based on that IP address.

                 

                Set ``Negated`` to ``True`` if you want AWS WAF to allow or block a request based on the negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow, block, or count requests based on all IP addresses *except*  ``192.0.2.44`` .

                
              

              - **Type** *(string) --* 

                The type of predicate in a ``Rule`` , such as ``ByteMatchSet`` or ``IPSet`` .

                
              

              - **DataId** *(string) --* 

                A unique identifier for a predicate in a ``Rule`` , such as ``ByteMatchSetId`` or ``IPSetId`` . The ID is returned by the corresponding ``Create`` or ``List`` command.

                
          
        
      
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``CreateRule`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

    **Examples** 

    The following example creates a rule named WAFByteHeaderRule.
    ::

      response = client.create_rule(
          ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          MetricName='WAFByteHeaderRule',
          Name='WAFByteHeaderRule',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          'Rule': {
              'MetricName': 'WAFByteHeaderRule',
              'Name': 'WAFByteHeaderRule',
              'Predicates': [
                  {
                      'DataId': 'MyByteMatchSetID',
                      'Negated': False,
                      'Type': 'ByteMatch',
                  },
              ],
              'RuleId': 'WAFRule-1-Example',
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_rule_group(**kwargs)

    

    Creates a ``RuleGroup`` . A rule group is a collection of predefined rules that you add to a web ACL. You use  UpdateRuleGroup to add rules to the rule group.

     

    Rule groups are subject to the following limits:

     

     
    * Three rule groups per account. You can request an increase to this limit by contacting customer support. 
     
    * One rule group per web ACL. 
     
    * Ten rules per rule group. 
     

     

    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the `AWS WAF Developer Guide <http://docs.aws.amazon.com/waf/latest/developerguide/>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/CreateRuleGroup>`_    


    **Request Syntax** 
    ::

      response = client.create_rule_group(
          Name='string',
          MetricName='string',
          ChangeToken='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      A friendly name or description of the  RuleGroup . You can't change ``Name`` after you create a ``RuleGroup`` .

      

    
    :type MetricName: string
    :param MetricName: **[REQUIRED]** 

      A friendly name or description for the metrics for this ``RuleGroup`` . The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace. You can't change the name of the metric after you create the ``RuleGroup`` .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'RuleGroup': {
                'RuleGroupId': 'string',
                'Name': 'string',
                'MetricName': 'string'
            },
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **RuleGroup** *(dict) --* 

          An empty  RuleGroup .

          
          

          - **RuleGroupId** *(string) --* 

            A unique identifier for a ``RuleGroup`` . You use ``RuleGroupId`` to get more information about a ``RuleGroup`` (see  GetRuleGroup ), update a ``RuleGroup`` (see  UpdateRuleGroup ), insert a ``RuleGroup`` into a ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``RuleGroup`` from AWS WAF (see  DeleteRuleGroup ).

             

             ``RuleGroupId`` is returned by  CreateRuleGroup and by  ListRuleGroups .

            
          

          - **Name** *(string) --* 

            The friendly name or description for the ``RuleGroup`` . You can't change the name of a ``RuleGroup`` after you create it.

            
          

          - **MetricName** *(string) --* 

            A friendly name or description for the metrics for this ``RuleGroup`` . The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace. You can't change the name of the metric after you create the ``RuleGroup`` .

            
      
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``CreateRuleGroup`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

  .. py:method:: create_size_constraint_set(**kwargs)

    

    Creates a ``SizeConstraintSet`` . You then use  UpdateSizeConstraintSet to identify the part of a web request that you want AWS WAF to check for length, such as the length of the ``User-Agent`` header or the length of the query string. For example, you can create a ``SizeConstraintSet`` that matches any requests that have a query string that is longer than 100 bytes. You can then configure AWS WAF to reject those requests.

     

    To create and configure a ``SizeConstraintSet`` , perform the following steps:

     

     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of a ``CreateSizeConstraintSet`` request. 
     
    * Submit a ``CreateSizeConstraintSet`` request. 
     
    * Use ``GetChangeToken`` to get the change token that you provide in the ``ChangeToken`` parameter of an ``UpdateSizeConstraintSet`` request. 
     
    * Submit an  UpdateSizeConstraintSet request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the value that you want AWS WAF to watch for. 
     

     

    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the `AWS WAF Developer Guide <http://docs.aws.amazon.com/waf/latest/developerguide/>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/CreateSizeConstraintSet>`_    


    **Request Syntax** 
    ::

      response = client.create_size_constraint_set(
          Name='string',
          ChangeToken='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      A friendly name or description of the  SizeConstraintSet . You can't change ``Name`` after you create a ``SizeConstraintSet`` .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'SizeConstraintSet': {
                'SizeConstraintSetId': 'string',
                'Name': 'string',
                'SizeConstraints': [
                    {
                        'FieldToMatch': {
                            'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
                            'Data': 'string'
                        },
                        'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE',
                        'ComparisonOperator': 'EQ'|'NE'|'LE'|'LT'|'GE'|'GT',
                        'Size': 123
                    },
                ]
            },
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **SizeConstraintSet** *(dict) --* 

          A  SizeConstraintSet that contains no ``SizeConstraint`` objects.

          
          

          - **SizeConstraintSetId** *(string) --* 

            A unique identifier for a ``SizeConstraintSet`` . You use ``SizeConstraintSetId`` to get information about a ``SizeConstraintSet`` (see  GetSizeConstraintSet ), update a ``SizeConstraintSet`` (see  UpdateSizeConstraintSet ), insert a ``SizeConstraintSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete a ``SizeConstraintSet`` from AWS WAF (see  DeleteSizeConstraintSet ).

             

             ``SizeConstraintSetId`` is returned by  CreateSizeConstraintSet and by  ListSizeConstraintSets .

            
          

          - **Name** *(string) --* 

            The name, if any, of the ``SizeConstraintSet`` .

            
          

          - **SizeConstraints** *(list) --* 

            Specifies the parts of web requests that you want to inspect the size of.

            
            

            - *(dict) --* 

              Specifies a constraint on the size of a part of the web request. AWS WAF uses the ``Size`` , ``ComparisonOperator`` , and ``FieldToMatch`` to build an expression in the form of "``Size``  ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that expression is true, the ``SizeConstraint`` is considered to match.

              
              

              - **FieldToMatch** *(dict) --* 

                Specifies where in a web request to look for the size constraint.

                
                

                - **Type** *(string) --* 

                  The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

                   

                   
                  * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the header in ``Data`` . 
                   
                  * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` . 
                   
                  * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a ``?`` character, if any. 
                   
                  * ``URI`` : The part of a web request that identifies a resource, for example, ``/images/daily-ad.jpg`` . 
                   
                  * ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .  
                   

                  
                

                - **Data** *(string) --* 

                  When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . If the value of ``Type`` is any other value, omit ``Data`` .

                   

                  The name of the header is not case sensitive.

                  
            
              

              - **TextTransformation** *(string) --* 

                Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

                 

                Note that if you choose ``BODY`` for the value of ``Type`` , you must choose ``NONE`` for ``TextTransformation`` because CloudFront forwards only the first 8192 bytes for inspection. 

                 

                 **NONE**  

                 

                Specify ``NONE`` if you don't want to perform any text transformations.

                 

                 **CMD_LINE**  

                 

                When you're concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

                 

                 
                * Delete the following characters: \ " ' ^ 
                 
                * Delete spaces before the following characters: / ( 
                 
                * Replace the following characters with a space: , ; 
                 
                * Replace multiple spaces with one space 
                 
                * Convert uppercase letters (A-Z) to lowercase (a-z) 
                 

                 

                 **COMPRESS_WHITE_SPACE**  

                 

                Use this option to replace the following characters with a space character (decimal 32):

                 

                 
                * \f, formfeed, decimal 12 
                 
                * \t, tab, decimal 9 
                 
                * \n, newline, decimal 10 
                 
                * \r, carriage return, decimal 13 
                 
                * \v, vertical tab, decimal 11 
                 
                * non-breaking space, decimal 160 
                 

                 

                 ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

                 

                 **HTML_ENTITY_DECODE**  

                 

                Use this option to replace HTML-encoded characters with unencoded characters. ``HTML_ENTITY_DECODE`` performs the following operations:

                 

                 
                * Replaces ``(ampersand)quot;`` with ``"``   
                 
                * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160 
                 
                * Replaces ``(ampersand)lt;`` with a "less than" symbol 
                 
                * Replaces ``(ampersand)gt;`` with ``>``   
                 
                * Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` , with the corresponding characters 
                 
                * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with the corresponding characters 
                 

                 

                 **LOWERCASE**  

                 

                Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

                 

                 **URL_DECODE**  

                 

                Use this option to decode a URL-encoded value.

                
              

              - **ComparisonOperator** *(string) --* 

                The type of comparison you want AWS WAF to perform. AWS WAF uses this in combination with the provided ``Size`` and ``FieldToMatch`` to build an expression in the form of "``Size``  ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that expression is true, the ``SizeConstraint`` is considered to match.

                 

                 **EQ** : Used to test if the ``Size`` is equal to the size of the ``FieldToMatch``  

                 

                 **NE** : Used to test if the ``Size`` is not equal to the size of the ``FieldToMatch``  

                 

                 **LE** : Used to test if the ``Size`` is less than or equal to the size of the ``FieldToMatch``  

                 

                 **LT** : Used to test if the ``Size`` is strictly less than the size of the ``FieldToMatch``  

                 

                 **GE** : Used to test if the ``Size`` is greater than or equal to the size of the ``FieldToMatch``  

                 

                 **GT** : Used to test if the ``Size`` is strictly greater than the size of the ``FieldToMatch``  

                
              

              - **Size** *(integer) --* 

                The size in bytes that you want AWS WAF to compare against the size of the specified ``FieldToMatch`` . AWS WAF uses this in combination with ``ComparisonOperator`` and ``FieldToMatch`` to build an expression in the form of "``Size``  ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that expression is true, the ``SizeConstraint`` is considered to match.

                 

                Valid values for size are 0 - 21474836480 bytes (0 - 20 GB).

                 

                If you specify ``URI`` for the value of ``Type`` , the / in the URI counts as one character. For example, the URI ``/logo.jpg`` is nine characters long.

                
          
        
      
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``CreateSizeConstraintSet`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

    **Examples** 

    The following example creates size constraint set named MySampleSizeConstraintSet.
    ::

      response = client.create_size_constraint_set(
          ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          Name='MySampleSizeConstraintSet',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          'SizeConstraintSet': {
              'Name': 'MySampleSizeConstraintSet',
              'SizeConstraintSetId': 'example1ds3t-46da-4fdb-b8d5-abc321j569j5',
              'SizeConstraints': [
                  {
                      'ComparisonOperator': 'GT',
                      'FieldToMatch': {
                          'Type': 'QUERY_STRING',
                      },
                      'Size': 0,
                      'TextTransformation': 'NONE',
                  },
              ],
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_sql_injection_match_set(**kwargs)

    

    Creates a  SqlInjectionMatchSet , which you use to allow, block, or count requests that contain snippets of SQL code in a specified part of web requests. AWS WAF searches for character sequences that are likely to be malicious strings.

     

    To create and configure a ``SqlInjectionMatchSet`` , perform the following steps:

     

     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of a ``CreateSqlInjectionMatchSet`` request. 
     
    * Submit a ``CreateSqlInjectionMatchSet`` request. 
     
    * Use ``GetChangeToken`` to get the change token that you provide in the ``ChangeToken`` parameter of an  UpdateSqlInjectionMatchSet request. 
     
    * Submit an  UpdateSqlInjectionMatchSet request to specify the parts of web requests in which you want to allow, block, or count malicious SQL code. 
     

     

    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the `AWS WAF Developer Guide <http://docs.aws.amazon.com/waf/latest/developerguide/>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/CreateSqlInjectionMatchSet>`_    


    **Request Syntax** 
    ::

      response = client.create_sql_injection_match_set(
          Name='string',
          ChangeToken='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      A friendly name or description for the  SqlInjectionMatchSet that you're creating. You can't change ``Name`` after you create the ``SqlInjectionMatchSet`` .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'SqlInjectionMatchSet': {
                'SqlInjectionMatchSetId': 'string',
                'Name': 'string',
                'SqlInjectionMatchTuples': [
                    {
                        'FieldToMatch': {
                            'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
                            'Data': 'string'
                        },
                        'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                    },
                ]
            },
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The response to a ``CreateSqlInjectionMatchSet`` request.

        
        

        - **SqlInjectionMatchSet** *(dict) --* 

          A  SqlInjectionMatchSet .

          
          

          - **SqlInjectionMatchSetId** *(string) --* 

            A unique identifier for a ``SqlInjectionMatchSet`` . You use ``SqlInjectionMatchSetId`` to get information about a ``SqlInjectionMatchSet`` (see  GetSqlInjectionMatchSet ), update a ``SqlInjectionMatchSet`` (see  UpdateSqlInjectionMatchSet ), insert a ``SqlInjectionMatchSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete a ``SqlInjectionMatchSet`` from AWS WAF (see  DeleteSqlInjectionMatchSet ).

             

             ``SqlInjectionMatchSetId`` is returned by  CreateSqlInjectionMatchSet and by  ListSqlInjectionMatchSets .

            
          

          - **Name** *(string) --* 

            The name, if any, of the ``SqlInjectionMatchSet`` .

            
          

          - **SqlInjectionMatchTuples** *(list) --* 

            Specifies the parts of web requests that you want to inspect for snippets of malicious SQL code.

            
            

            - *(dict) --* 

              Specifies the part of a web request that you want AWS WAF to inspect for snippets of malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.

              
              

              - **FieldToMatch** *(dict) --* 

                Specifies where in a web request to look for snippets of malicious SQL code.

                
                

                - **Type** *(string) --* 

                  The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

                   

                   
                  * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the header in ``Data`` . 
                   
                  * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` . 
                   
                  * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a ``?`` character, if any. 
                   
                  * ``URI`` : The part of a web request that identifies a resource, for example, ``/images/daily-ad.jpg`` . 
                   
                  * ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .  
                   

                  
                

                - **Data** *(string) --* 

                  When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . If the value of ``Type`` is any other value, omit ``Data`` .

                   

                  The name of the header is not case sensitive.

                  
            
              

              - **TextTransformation** *(string) --* 

                Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

                 

                 **CMD_LINE**  

                 

                When you're concerned that attackers are injecting an operating system commandline command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

                 

                 
                * Delete the following characters: \ " ' ^ 
                 
                * Delete spaces before the following characters: / ( 
                 
                * Replace the following characters with a space: , ; 
                 
                * Replace multiple spaces with one space 
                 
                * Convert uppercase letters (A-Z) to lowercase (a-z) 
                 

                 

                 **COMPRESS_WHITE_SPACE**  

                 

                Use this option to replace the following characters with a space character (decimal 32):

                 

                 
                * \f, formfeed, decimal 12 
                 
                * \t, tab, decimal 9 
                 
                * \n, newline, decimal 10 
                 
                * \r, carriage return, decimal 13 
                 
                * \v, vertical tab, decimal 11 
                 
                * non-breaking space, decimal 160 
                 

                 

                 ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

                 

                 **HTML_ENTITY_DECODE**  

                 

                Use this option to replace HTML-encoded characters with unencoded characters. ``HTML_ENTITY_DECODE`` performs the following operations:

                 

                 
                * Replaces ``(ampersand)quot;`` with ``"``   
                 
                * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160 
                 
                * Replaces ``(ampersand)lt;`` with a "less than" symbol 
                 
                * Replaces ``(ampersand)gt;`` with ``>``   
                 
                * Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` , with the corresponding characters 
                 
                * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with the corresponding characters 
                 

                 

                 **LOWERCASE**  

                 

                Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

                 

                 **URL_DECODE**  

                 

                Use this option to decode a URL-encoded value.

                 

                 **NONE**  

                 

                Specify ``NONE`` if you don't want to perform any text transformations.

                
          
        
      
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``CreateSqlInjectionMatchSet`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

    **Examples** 

    The following example creates a SQL injection match set named MySQLInjectionMatchSet.
    ::

      response = client.create_sql_injection_match_set(
          ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          Name='MySQLInjectionMatchSet',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          'SqlInjectionMatchSet': {
              'Name': 'MySQLInjectionMatchSet',
              'SqlInjectionMatchSetId': 'example1ds3t-46da-4fdb-b8d5-abc321j569j5',
              'SqlInjectionMatchTuples': [
                  {
                      'FieldToMatch': {
                          'Type': 'QUERY_STRING',
                      },
                      'TextTransformation': 'URL_DECODE',
                  },
              ],
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_web_acl(**kwargs)

    

    Creates a ``WebACL`` , which contains the ``Rules`` that identify the CloudFront web requests that you want to allow, block, or count. AWS WAF evaluates ``Rules`` in order based on the value of ``Priority`` for each ``Rule`` .

     

    You also specify a default action, either ``ALLOW`` or ``BLOCK`` . If a web request doesn't match any of the ``Rules`` in a ``WebACL`` , AWS WAF responds to the request with the default action. 

     

    To create and configure a ``WebACL`` , perform the following steps:

     

     
    * Create and update the ``ByteMatchSet`` objects and other predicates that you want to include in ``Rules`` . For more information, see  CreateByteMatchSet ,  UpdateByteMatchSet ,  CreateIPSet ,  UpdateIPSet ,  CreateSqlInjectionMatchSet , and  UpdateSqlInjectionMatchSet . 
     
    * Create and update the ``Rules`` that you want to include in the ``WebACL`` . For more information, see  CreateRule and  UpdateRule . 
     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of a ``CreateWebACL`` request. 
     
    * Submit a ``CreateWebACL`` request. 
     
    * Use ``GetChangeToken`` to get the change token that you provide in the ``ChangeToken`` parameter of an  UpdateWebACL request. 
     
    * Submit an  UpdateWebACL request to specify the ``Rules`` that you want to include in the ``WebACL`` , to specify the default action, and to associate the ``WebACL`` with a CloudFront distribution. 
     

     

    For more information about how to use the AWS WAF API, see the `AWS WAF Developer Guide <http://docs.aws.amazon.com/waf/latest/developerguide/>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/CreateWebACL>`_    


    **Request Syntax** 
    ::

      response = client.create_web_acl(
          Name='string',
          MetricName='string',
          DefaultAction={
              'Type': 'BLOCK'|'ALLOW'|'COUNT'
          },
          ChangeToken='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      A friendly name or description of the  WebACL . You can't change ``Name`` after you create the ``WebACL`` .

      

    
    :type MetricName: string
    :param MetricName: **[REQUIRED]** 

      A friendly name or description for the metrics for this ``WebACL`` . The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace. You can't change ``MetricName`` after you create the ``WebACL`` .

      

    
    :type DefaultAction: dict
    :param DefaultAction: **[REQUIRED]** 

      The action that you want AWS WAF to take when a request doesn't match the criteria specified in any of the ``Rule`` objects that are associated with the ``WebACL`` .

      

    
      - **Type** *(string) --* **[REQUIRED]** 

        Specifies how you want AWS WAF to respond to requests that match the settings in a ``Rule`` . Valid settings include the following:

         

         
        * ``ALLOW`` : AWS WAF allows requests 
         
        * ``BLOCK`` : AWS WAF blocks requests 
         
        * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for a ``WebACL`` . 
         

        

      
    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'WebACL': {
                'WebACLId': 'string',
                'Name': 'string',
                'MetricName': 'string',
                'DefaultAction': {
                    'Type': 'BLOCK'|'ALLOW'|'COUNT'
                },
                'Rules': [
                    {
                        'Priority': 123,
                        'RuleId': 'string',
                        'Action': {
                            'Type': 'BLOCK'|'ALLOW'|'COUNT'
                        },
                        'OverrideAction': {
                            'Type': 'NONE'|'COUNT'
                        },
                        'Type': 'REGULAR'|'RATE_BASED'|'GROUP'
                    },
                ]
            },
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **WebACL** *(dict) --* 

          The  WebACL returned in the ``CreateWebACL`` response.

          
          

          - **WebACLId** *(string) --* 

            A unique identifier for a ``WebACL`` . You use ``WebACLId`` to get information about a ``WebACL`` (see  GetWebACL ), update a ``WebACL`` (see  UpdateWebACL ), and delete a ``WebACL`` from AWS WAF (see  DeleteWebACL ).

             

             ``WebACLId`` is returned by  CreateWebACL and by  ListWebACLs .

            
          

          - **Name** *(string) --* 

            A friendly name or description of the ``WebACL`` . You can't change the name of a ``WebACL`` after you create it.

            
          

          - **MetricName** *(string) --* 

            A friendly name or description for the metrics for this ``WebACL`` . The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace. You can't change ``MetricName`` after you create the ``WebACL`` .

            
          

          - **DefaultAction** *(dict) --* 

            The action to perform if none of the ``Rules`` contained in the ``WebACL`` match. The action is specified by the  WafAction object.

            
            

            - **Type** *(string) --* 

              Specifies how you want AWS WAF to respond to requests that match the settings in a ``Rule`` . Valid settings include the following:

               

               
              * ``ALLOW`` : AWS WAF allows requests 
               
              * ``BLOCK`` : AWS WAF blocks requests 
               
              * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for a ``WebACL`` . 
               

              
        
          

          - **Rules** *(list) --* 

            An array that contains the action for each ``Rule`` in a ``WebACL`` , the priority of the ``Rule`` , and the ID of the ``Rule`` .

            
            

            - *(dict) --* 

              The ``ActivatedRule`` object in an  UpdateWebACL request specifies a ``Rule`` that you want to insert or delete, the priority of the ``Rule`` in the ``WebACL`` , and the action that you want AWS WAF to take when a web request matches the ``Rule`` (``ALLOW`` , ``BLOCK`` , or ``COUNT`` ).

               

              To specify whether to insert or delete a ``Rule`` , use the ``Action`` parameter in the  WebACLUpdate data type.

              
              

              - **Priority** *(integer) --* 

                Specifies the order in which the ``Rules`` in a ``WebACL`` are evaluated. Rules with a lower value for ``Priority`` are evaluated before ``Rules`` with a higher value. The value must be a unique integer. If you add multiple ``Rules`` to a ``WebACL`` , the values don't need to be consecutive.

                
              

              - **RuleId** *(string) --* 

                The ``RuleId`` for a ``Rule`` . You use ``RuleId`` to get more information about a ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule`` from AWS WAF (see  DeleteRule ).

                 

                 ``RuleId`` is returned by  CreateRule and by  ListRules .

                
              

              - **Action** *(dict) --* 

                Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the ``Rule`` . Valid values for ``Action`` include the following:

                 

                 
                * ``ALLOW`` : CloudFront responds with the requested object. 
                 
                * ``BLOCK`` : CloudFront responds with an HTTP 403 (Forbidden) status code. 
                 
                * ``COUNT`` : AWS WAF increments a counter of requests that match the conditions in the rule and then continues to inspect the web request based on the remaining rules in the web ACL.  
                 

                 

                The ``Action`` data type within ``ActivatedRule`` is used only when submitting an ``UpdateWebACL`` request. ``ActivatedRule|Action`` is not applicable and therefore not available for ``UpdateRuleGroup`` .

                
                

                - **Type** *(string) --* 

                  Specifies how you want AWS WAF to respond to requests that match the settings in a ``Rule`` . Valid settings include the following:

                   

                   
                  * ``ALLOW`` : AWS WAF allows requests 
                   
                  * ``BLOCK`` : AWS WAF blocks requests 
                   
                  * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for a ``WebACL`` . 
                   

                  
            
              

              - **OverrideAction** *(dict) --* 

                Use the ``OverrideAction`` to test your ``RuleGroup`` .

                 

                Any rule in a ``RuleGroup`` can potentially block a request. If you set the ``OverrideAction`` to ``None`` , the ``RuleGroup`` will block a request if any individual rule in the ``RuleGroup`` matches the request and is configured to block that request. However if you first want to test the ``RuleGroup`` , set the ``OverrideAction`` to ``Count`` . The ``RuleGroup`` will then override any block action specified by individual rules contained within the group. Instead of blocking matching requests, those requests will be counted. You can view a record of counted requests using  GetSampledRequests . 

                 

                The ``OverrideAction`` data type within ``ActivatedRule`` is used only when submitting an ``UpdateRuleGroup`` request. ``ActivatedRule|OverrideAction`` is not applicable and therefore not available for ``UpdateWebACL`` .

                
                

                - **Type** *(string) --* 

                   ``COUNT`` overrides the action specified by the individual rule within a ``RuleGroup`` . If set to ``NONE`` , the rule's action will take place.

                  
            
              

              - **Type** *(string) --* 

                The rule type, either ``REGULAR`` , as defined by  Rule , ``RATE_BASED`` , as defined by  RateBasedRule , or ``GROUP`` , as defined by  RuleGroup . The default is REGULAR. Although this field is optional, be aware that if you try to add a RATE_BASED rule to a web ACL without setting the type, the  UpdateWebACL request will fail because the request tries to add a REGULAR rule with the specified ID, which does not exist. 

                
          
        
      
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``CreateWebACL`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

    **Examples** 

    The following example creates a web ACL named CreateExample.
    ::

      response = client.create_web_acl(
          ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          DefaultAction={
              'Type': 'ALLOW',
          },
          MetricName='CreateExample',
          Name='CreateExample',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          'WebACL': {
              'DefaultAction': {
                  'Type': 'ALLOW',
              },
              'MetricName': 'CreateExample',
              'Name': 'CreateExample',
              'Rules': [
                  {
                      'Action': {
                          'Type': 'ALLOW',
                      },
                      'Priority': 1,
                      'RuleId': 'WAFRule-1-Example',
                  },
              ],
              'WebACLId': 'example-46da-4444-5555-example',
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_xss_match_set(**kwargs)

    

    Creates an  XssMatchSet , which you use to allow, block, or count requests that contain cross-site scripting attacks in the specified part of web requests. AWS WAF searches for character sequences that are likely to be malicious strings.

     

    To create and configure an ``XssMatchSet`` , perform the following steps:

     

     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of a ``CreateXssMatchSet`` request. 
     
    * Submit a ``CreateXssMatchSet`` request. 
     
    * Use ``GetChangeToken`` to get the change token that you provide in the ``ChangeToken`` parameter of an  UpdateXssMatchSet request. 
     
    * Submit an  UpdateXssMatchSet request to specify the parts of web requests in which you want to allow, block, or count cross-site scripting attacks. 
     

     

    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the `AWS WAF Developer Guide <http://docs.aws.amazon.com/waf/latest/developerguide/>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/CreateXssMatchSet>`_    


    **Request Syntax** 
    ::

      response = client.create_xss_match_set(
          Name='string',
          ChangeToken='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      A friendly name or description for the  XssMatchSet that you're creating. You can't change ``Name`` after you create the ``XssMatchSet`` .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'XssMatchSet': {
                'XssMatchSetId': 'string',
                'Name': 'string',
                'XssMatchTuples': [
                    {
                        'FieldToMatch': {
                            'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
                            'Data': 'string'
                        },
                        'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                    },
                ]
            },
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The response to a ``CreateXssMatchSet`` request.

        
        

        - **XssMatchSet** *(dict) --* 

          An  XssMatchSet .

          
          

          - **XssMatchSetId** *(string) --* 

            A unique identifier for an ``XssMatchSet`` . You use ``XssMatchSetId`` to get information about an ``XssMatchSet`` (see  GetXssMatchSet ), update an ``XssMatchSet`` (see  UpdateXssMatchSet ), insert an ``XssMatchSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete an ``XssMatchSet`` from AWS WAF (see  DeleteXssMatchSet ).

             

             ``XssMatchSetId`` is returned by  CreateXssMatchSet and by  ListXssMatchSets .

            
          

          - **Name** *(string) --* 

            The name, if any, of the ``XssMatchSet`` .

            
          

          - **XssMatchTuples** *(list) --* 

            Specifies the parts of web requests that you want to inspect for cross-site scripting attacks.

            
            

            - *(dict) --* 

              Specifies the part of a web request that you want AWS WAF to inspect for cross-site scripting attacks and, if you want AWS WAF to inspect a header, the name of the header.

              
              

              - **FieldToMatch** *(dict) --* 

                Specifies where in a web request to look for cross-site scripting attacks.

                
                

                - **Type** *(string) --* 

                  The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

                   

                   
                  * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the header in ``Data`` . 
                   
                  * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` . 
                   
                  * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a ``?`` character, if any. 
                   
                  * ``URI`` : The part of a web request that identifies a resource, for example, ``/images/daily-ad.jpg`` . 
                   
                  * ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .  
                   

                  
                

                - **Data** *(string) --* 

                  When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . If the value of ``Type`` is any other value, omit ``Data`` .

                   

                  The name of the header is not case sensitive.

                  
            
              

              - **TextTransformation** *(string) --* 

                Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

                 

                 **CMD_LINE**  

                 

                When you're concerned that attackers are injecting an operating system commandline command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

                 

                 
                * Delete the following characters: \ " ' ^ 
                 
                * Delete spaces before the following characters: / ( 
                 
                * Replace the following characters with a space: , ; 
                 
                * Replace multiple spaces with one space 
                 
                * Convert uppercase letters (A-Z) to lowercase (a-z) 
                 

                 

                 **COMPRESS_WHITE_SPACE**  

                 

                Use this option to replace the following characters with a space character (decimal 32):

                 

                 
                * \f, formfeed, decimal 12 
                 
                * \t, tab, decimal 9 
                 
                * \n, newline, decimal 10 
                 
                * \r, carriage return, decimal 13 
                 
                * \v, vertical tab, decimal 11 
                 
                * non-breaking space, decimal 160 
                 

                 

                 ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

                 

                 **HTML_ENTITY_DECODE**  

                 

                Use this option to replace HTML-encoded characters with unencoded characters. ``HTML_ENTITY_DECODE`` performs the following operations:

                 

                 
                * Replaces ``(ampersand)quot;`` with ``"``   
                 
                * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160 
                 
                * Replaces ``(ampersand)lt;`` with a "less than" symbol 
                 
                * Replaces ``(ampersand)gt;`` with ``>``   
                 
                * Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` , with the corresponding characters 
                 
                * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with the corresponding characters 
                 

                 

                 **LOWERCASE**  

                 

                Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

                 

                 **URL_DECODE**  

                 

                Use this option to decode a URL-encoded value.

                 

                 **NONE**  

                 

                Specify ``NONE`` if you don't want to perform any text transformations.

                
          
        
      
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``CreateXssMatchSet`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

    **Examples** 

    The following example creates an XSS match set named MySampleXssMatchSet.
    ::

      response = client.create_xss_match_set(
          ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          Name='MySampleXssMatchSet',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          'XssMatchSet': {
              'Name': 'MySampleXssMatchSet',
              'XssMatchSetId': 'example1ds3t-46da-4fdb-b8d5-abc321j569j5',
              'XssMatchTuples': [
                  {
                      'FieldToMatch': {
                          'Type': 'QUERY_STRING',
                      },
                      'TextTransformation': 'URL_DECODE',
                  },
              ],
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_byte_match_set(**kwargs)

    

    Permanently deletes a  ByteMatchSet . You can't delete a ``ByteMatchSet`` if it's still used in any ``Rules`` or if it still includes any  ByteMatchTuple objects (any filters).

     

    If you just want to remove a ``ByteMatchSet`` from a ``Rule`` , use  UpdateRule .

     

    To permanently delete a ``ByteMatchSet`` , perform the following steps:

     

     
    * Update the ``ByteMatchSet`` to remove filters, if any. For more information, see  UpdateByteMatchSet . 
     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of a ``DeleteByteMatchSet`` request. 
     
    * Submit a ``DeleteByteMatchSet`` request. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/DeleteByteMatchSet>`_    


    **Request Syntax** 
    ::

      response = client.delete_byte_match_set(
          ByteMatchSetId='string',
          ChangeToken='string'
      )
    :type ByteMatchSetId: string
    :param ByteMatchSetId: **[REQUIRED]** 

      The ``ByteMatchSetId`` of the  ByteMatchSet that you want to delete. ``ByteMatchSetId`` is returned by  CreateByteMatchSet and by  ListByteMatchSets .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``DeleteByteMatchSet`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

    **Examples** 

    The following example deletes a byte match set with the ID exampleIDs3t-46da-4fdb-b8d5-abc321j569j5.
    ::

      response = client.delete_byte_match_set(
          ByteMatchSetId='exampleIDs3t-46da-4fdb-b8d5-abc321j569j5',
          ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_geo_match_set(**kwargs)

    

    Permanently deletes a  GeoMatchSet . You can't delete a ``GeoMatchSet`` if it's still used in any ``Rules`` or if it still includes any countries.

     

    If you just want to remove a ``GeoMatchSet`` from a ``Rule`` , use  UpdateRule .

     

    To permanently delete a ``GeoMatchSet`` from AWS WAF, perform the following steps:

     

     
    * Update the ``GeoMatchSet`` to remove any countries. For more information, see  UpdateGeoMatchSet . 
     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of a ``DeleteGeoMatchSet`` request. 
     
    * Submit a ``DeleteGeoMatchSet`` request. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/DeleteGeoMatchSet>`_    


    **Request Syntax** 
    ::

      response = client.delete_geo_match_set(
          GeoMatchSetId='string',
          ChangeToken='string'
      )
    :type GeoMatchSetId: string
    :param GeoMatchSetId: **[REQUIRED]** 

      The ``GeoMatchSetID`` of the  GeoMatchSet that you want to delete. ``GeoMatchSetId`` is returned by  CreateGeoMatchSet and by  ListGeoMatchSets .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``DeleteGeoMatchSet`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

  .. py:method:: delete_ip_set(**kwargs)

    

    Permanently deletes an  IPSet . You can't delete an ``IPSet`` if it's still used in any ``Rules`` or if it still includes any IP addresses.

     

    If you just want to remove an ``IPSet`` from a ``Rule`` , use  UpdateRule .

     

    To permanently delete an ``IPSet`` from AWS WAF, perform the following steps:

     

     
    * Update the ``IPSet`` to remove IP address ranges, if any. For more information, see  UpdateIPSet . 
     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of a ``DeleteIPSet`` request. 
     
    * Submit a ``DeleteIPSet`` request. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/DeleteIPSet>`_    


    **Request Syntax** 
    ::

      response = client.delete_ip_set(
          IPSetId='string',
          ChangeToken='string'
      )
    :type IPSetId: string
    :param IPSetId: **[REQUIRED]** 

      The ``IPSetId`` of the  IPSet that you want to delete. ``IPSetId`` is returned by  CreateIPSet and by  ListIPSets .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``DeleteIPSet`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

    **Examples** 

    The following example deletes an IP match set  with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    ::

      response = client.delete_ip_set(
          ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          IPSetId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_rate_based_rule(**kwargs)

    

    Permanently deletes a  RateBasedRule . You can't delete a rule if it's still used in any ``WebACL`` objects or if it still includes any predicates, such as ``ByteMatchSet`` objects.

     

    If you just want to remove a rule from a ``WebACL`` , use  UpdateWebACL .

     

    To permanently delete a ``RateBasedRule`` from AWS WAF, perform the following steps:

     

     
    * Update the ``RateBasedRule`` to remove predicates, if any. For more information, see  UpdateRateBasedRule . 
     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of a ``DeleteRateBasedRule`` request. 
     
    * Submit a ``DeleteRateBasedRule`` request. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/DeleteRateBasedRule>`_    


    **Request Syntax** 
    ::

      response = client.delete_rate_based_rule(
          RuleId='string',
          ChangeToken='string'
      )
    :type RuleId: string
    :param RuleId: **[REQUIRED]** 

      The ``RuleId`` of the  RateBasedRule that you want to delete. ``RuleId`` is returned by  CreateRateBasedRule and by  ListRateBasedRules .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``DeleteRateBasedRule`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

  .. py:method:: delete_regex_match_set(**kwargs)

    

    Permanently deletes a  RegexMatchSet . You can't delete a ``RegexMatchSet`` if it's still used in any ``Rules`` or if it still includes any ``RegexMatchTuples`` objects (any filters).

     

    If you just want to remove a ``RegexMatchSet`` from a ``Rule`` , use  UpdateRule .

     

    To permanently delete a ``RegexMatchSet`` , perform the following steps:

     

     
    * Update the ``RegexMatchSet`` to remove filters, if any. For more information, see  UpdateRegexMatchSet . 
     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of a ``DeleteRegexMatchSet`` request. 
     
    * Submit a ``DeleteRegexMatchSet`` request. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/DeleteRegexMatchSet>`_    


    **Request Syntax** 
    ::

      response = client.delete_regex_match_set(
          RegexMatchSetId='string',
          ChangeToken='string'
      )
    :type RegexMatchSetId: string
    :param RegexMatchSetId: **[REQUIRED]** 

      The ``RegexMatchSetId`` of the  RegexMatchSet that you want to delete. ``RegexMatchSetId`` is returned by  CreateRegexMatchSet and by  ListRegexMatchSets .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``DeleteRegexMatchSet`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

  .. py:method:: delete_regex_pattern_set(**kwargs)

    

    Permanently deletes a  RegexPatternSet . You can't delete a ``RegexPatternSet`` if it's still used in any ``RegexMatchSet`` or if the ``RegexPatternSet`` is not empty. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/DeleteRegexPatternSet>`_    


    **Request Syntax** 
    ::

      response = client.delete_regex_pattern_set(
          RegexPatternSetId='string',
          ChangeToken='string'
      )
    :type RegexPatternSetId: string
    :param RegexPatternSetId: **[REQUIRED]** 

      The ``RegexPatternSetId`` of the  RegexPatternSet that you want to delete. ``RegexPatternSetId`` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``DeleteRegexPatternSet`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

  .. py:method:: delete_rule(**kwargs)

    

    Permanently deletes a  Rule . You can't delete a ``Rule`` if it's still used in any ``WebACL`` objects or if it still includes any predicates, such as ``ByteMatchSet`` objects.

     

    If you just want to remove a ``Rule`` from a ``WebACL`` , use  UpdateWebACL .

     

    To permanently delete a ``Rule`` from AWS WAF, perform the following steps:

     

     
    * Update the ``Rule`` to remove predicates, if any. For more information, see  UpdateRule . 
     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of a ``DeleteRule`` request. 
     
    * Submit a ``DeleteRule`` request. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/DeleteRule>`_    


    **Request Syntax** 
    ::

      response = client.delete_rule(
          RuleId='string',
          ChangeToken='string'
      )
    :type RuleId: string
    :param RuleId: **[REQUIRED]** 

      The ``RuleId`` of the  Rule that you want to delete. ``RuleId`` is returned by  CreateRule and by  ListRules .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``DeleteRule`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

    **Examples** 

    The following example deletes a rule with the ID WAFRule-1-Example.
    ::

      response = client.delete_rule(
          ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          RuleId='WAFRule-1-Example',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_rule_group(**kwargs)

    

    Permanently deletes a  RuleGroup . You can't delete a ``RuleGroup`` if it's still used in any ``WebACL`` objects or if it still includes any rules.

     

    If you just want to remove a ``RuleGroup`` from a ``WebACL`` , use  UpdateWebACL .

     

    To permanently delete a ``RuleGroup`` from AWS WAF, perform the following steps:

     

     
    * Update the ``RuleGroup`` to remove rules, if any. For more information, see  UpdateRuleGroup . 
     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of a ``DeleteRuleGroup`` request. 
     
    * Submit a ``DeleteRuleGroup`` request. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/DeleteRuleGroup>`_    


    **Request Syntax** 
    ::

      response = client.delete_rule_group(
          RuleGroupId='string',
          ChangeToken='string'
      )
    :type RuleGroupId: string
    :param RuleGroupId: **[REQUIRED]** 

      The ``RuleGroupId`` of the  RuleGroup that you want to delete. ``RuleGroupId`` is returned by  CreateRuleGroup and by  ListRuleGroups .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``DeleteRuleGroup`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

  .. py:method:: delete_size_constraint_set(**kwargs)

    

    Permanently deletes a  SizeConstraintSet . You can't delete a ``SizeConstraintSet`` if it's still used in any ``Rules`` or if it still includes any  SizeConstraint objects (any filters).

     

    If you just want to remove a ``SizeConstraintSet`` from a ``Rule`` , use  UpdateRule .

     

    To permanently delete a ``SizeConstraintSet`` , perform the following steps:

     

     
    * Update the ``SizeConstraintSet`` to remove filters, if any. For more information, see  UpdateSizeConstraintSet . 
     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of a ``DeleteSizeConstraintSet`` request. 
     
    * Submit a ``DeleteSizeConstraintSet`` request. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/DeleteSizeConstraintSet>`_    


    **Request Syntax** 
    ::

      response = client.delete_size_constraint_set(
          SizeConstraintSetId='string',
          ChangeToken='string'
      )
    :type SizeConstraintSetId: string
    :param SizeConstraintSetId: **[REQUIRED]** 

      The ``SizeConstraintSetId`` of the  SizeConstraintSet that you want to delete. ``SizeConstraintSetId`` is returned by  CreateSizeConstraintSet and by  ListSizeConstraintSets .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``DeleteSizeConstraintSet`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

    **Examples** 

    The following example deletes a size constraint set  with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    ::

      response = client.delete_size_constraint_set(
          ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          SizeConstraintSetId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_sql_injection_match_set(**kwargs)

    

    Permanently deletes a  SqlInjectionMatchSet . You can't delete a ``SqlInjectionMatchSet`` if it's still used in any ``Rules`` or if it still contains any  SqlInjectionMatchTuple objects.

     

    If you just want to remove a ``SqlInjectionMatchSet`` from a ``Rule`` , use  UpdateRule .

     

    To permanently delete a ``SqlInjectionMatchSet`` from AWS WAF, perform the following steps:

     

     
    * Update the ``SqlInjectionMatchSet`` to remove filters, if any. For more information, see  UpdateSqlInjectionMatchSet . 
     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of a ``DeleteSqlInjectionMatchSet`` request. 
     
    * Submit a ``DeleteSqlInjectionMatchSet`` request. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/DeleteSqlInjectionMatchSet>`_    


    **Request Syntax** 
    ::

      response = client.delete_sql_injection_match_set(
          SqlInjectionMatchSetId='string',
          ChangeToken='string'
      )
    :type SqlInjectionMatchSetId: string
    :param SqlInjectionMatchSetId: **[REQUIRED]** 

      The ``SqlInjectionMatchSetId`` of the  SqlInjectionMatchSet that you want to delete. ``SqlInjectionMatchSetId`` is returned by  CreateSqlInjectionMatchSet and by  ListSqlInjectionMatchSets .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The response to a request to delete a  SqlInjectionMatchSet from AWS WAF.

        
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``DeleteSqlInjectionMatchSet`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

    **Examples** 

    The following example deletes a SQL injection match set  with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    ::

      response = client.delete_sql_injection_match_set(
          ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          SqlInjectionMatchSetId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_web_acl(**kwargs)

    

    Permanently deletes a  WebACL . You can't delete a ``WebACL`` if it still contains any ``Rules`` .

     

    To delete a ``WebACL`` , perform the following steps:

     

     
    * Update the ``WebACL`` to remove ``Rules`` , if any. For more information, see  UpdateWebACL . 
     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of a ``DeleteWebACL`` request. 
     
    * Submit a ``DeleteWebACL`` request. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/DeleteWebACL>`_    


    **Request Syntax** 
    ::

      response = client.delete_web_acl(
          WebACLId='string',
          ChangeToken='string'
      )
    :type WebACLId: string
    :param WebACLId: **[REQUIRED]** 

      The ``WebACLId`` of the  WebACL that you want to delete. ``WebACLId`` is returned by  CreateWebACL and by  ListWebACLs .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``DeleteWebACL`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

    **Examples** 

    The following example deletes a web ACL with the ID example-46da-4444-5555-example.
    ::

      response = client.delete_web_acl(
          ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          WebACLId='example-46da-4444-5555-example',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_xss_match_set(**kwargs)

    

    Permanently deletes an  XssMatchSet . You can't delete an ``XssMatchSet`` if it's still used in any ``Rules`` or if it still contains any  XssMatchTuple objects.

     

    If you just want to remove an ``XssMatchSet`` from a ``Rule`` , use  UpdateRule .

     

    To permanently delete an ``XssMatchSet`` from AWS WAF, perform the following steps:

     

     
    * Update the ``XssMatchSet`` to remove filters, if any. For more information, see  UpdateXssMatchSet . 
     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of a ``DeleteXssMatchSet`` request. 
     
    * Submit a ``DeleteXssMatchSet`` request. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/DeleteXssMatchSet>`_    


    **Request Syntax** 
    ::

      response = client.delete_xss_match_set(
          XssMatchSetId='string',
          ChangeToken='string'
      )
    :type XssMatchSetId: string
    :param XssMatchSetId: **[REQUIRED]** 

      The ``XssMatchSetId`` of the  XssMatchSet that you want to delete. ``XssMatchSetId`` is returned by  CreateXssMatchSet and by  ListXssMatchSets .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The response to a request to delete an  XssMatchSet from AWS WAF.

        
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``DeleteXssMatchSet`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

    **Examples** 

    The following example deletes an XSS match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    ::

      response = client.delete_xss_match_set(
          ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          XssMatchSetId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: disassociate_web_acl(**kwargs)

    

    Removes a web ACL from the specified resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/DisassociateWebACL>`_    


    **Request Syntax** 
    ::

      response = client.disassociate_web_acl(
          ResourceArn='string'
      )
    :type ResourceArn: string
    :param ResourceArn: **[REQUIRED]** 

      The ARN (Amazon Resource Name) of the resource from which the web ACL is being removed.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

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


  .. py:method:: get_byte_match_set(**kwargs)

    

    Returns the  ByteMatchSet specified by ``ByteMatchSetId`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/GetByteMatchSet>`_    


    **Request Syntax** 
    ::

      response = client.get_byte_match_set(
          ByteMatchSetId='string'
      )
    :type ByteMatchSetId: string
    :param ByteMatchSetId: **[REQUIRED]** 

      The ``ByteMatchSetId`` of the  ByteMatchSet that you want to get. ``ByteMatchSetId`` is returned by  CreateByteMatchSet and by  ListByteMatchSets .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ByteMatchSet': {
                'ByteMatchSetId': 'string',
                'Name': 'string',
                'ByteMatchTuples': [
                    {
                        'FieldToMatch': {
                            'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
                            'Data': 'string'
                        },
                        'TargetString': b'bytes',
                        'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE',
                        'PositionalConstraint': 'EXACTLY'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CONTAINS_WORD'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ByteMatchSet** *(dict) --* 

          Information about the  ByteMatchSet that you specified in the ``GetByteMatchSet`` request. For more information, see the following topics:

           

           
          *  ByteMatchSet : Contains ``ByteMatchSetId`` , ``ByteMatchTuples`` , and ``Name``   
           
          * ``ByteMatchTuples`` : Contains an array of  ByteMatchTuple objects. Each ``ByteMatchTuple`` object contains  FieldToMatch , ``PositionalConstraint`` , ``TargetString`` , and ``TextTransformation``   
           
          *  FieldToMatch : Contains ``Data`` and ``Type``   
           

          
          

          - **ByteMatchSetId** *(string) --* 

            The ``ByteMatchSetId`` for a ``ByteMatchSet`` . You use ``ByteMatchSetId`` to get information about a ``ByteMatchSet`` (see  GetByteMatchSet ), update a ``ByteMatchSet`` (see  UpdateByteMatchSet ), insert a ``ByteMatchSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete a ``ByteMatchSet`` from AWS WAF (see  DeleteByteMatchSet ).

             

             ``ByteMatchSetId`` is returned by  CreateByteMatchSet and by  ListByteMatchSets .

            
          

          - **Name** *(string) --* 

            A friendly name or description of the  ByteMatchSet . You can't change ``Name`` after you create a ``ByteMatchSet`` .

            
          

          - **ByteMatchTuples** *(list) --* 

            Specifies the bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests, the location in requests that you want AWS WAF to search, and other settings.

            
            

            - *(dict) --* 

              The bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to search for in web requests, the location in requests that you want AWS WAF to search, and other settings.

              
              

              - **FieldToMatch** *(dict) --* 

                The part of a web request that you want AWS WAF to search, such as a specified header or a query string. For more information, see  FieldToMatch .

                
                

                - **Type** *(string) --* 

                  The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

                   

                   
                  * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the header in ``Data`` . 
                   
                  * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` . 
                   
                  * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a ``?`` character, if any. 
                   
                  * ``URI`` : The part of a web request that identifies a resource, for example, ``/images/daily-ad.jpg`` . 
                   
                  * ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .  
                   

                  
                

                - **Data** *(string) --* 

                  When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . If the value of ``Type`` is any other value, omit ``Data`` .

                   

                  The name of the header is not case sensitive.

                  
            
              

              - **TargetString** *(bytes) --* 

                The value that you want AWS WAF to search for. AWS WAF searches for the specified string in the part of web requests that you specified in ``FieldToMatch`` . The maximum length of the value is 50 bytes.

                 

                Valid values depend on the values that you specified for ``FieldToMatch`` :

                 

                 
                * ``HEADER`` : The value that you want AWS WAF to search for in the request header that you specified in  FieldToMatch , for example, the value of the ``User-Agent`` or ``Referer`` header. 
                 
                * ``METHOD`` : The HTTP method, which indicates the type of operation specified in the request. CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` . 
                 
                * ``QUERY_STRING`` : The value that you want AWS WAF to search for in the query string, which is the part of a URL that appears after a ``?`` character. 
                 
                * ``URI`` : The value that you want AWS WAF to search for in the part of a URL that identifies a resource, for example, ``/images/daily-ad.jpg`` . 
                 
                * ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .  
                 

                 

                If ``TargetString`` includes alphabetic characters A-Z and a-z, note that the value is case sensitive.

                 

                 **If you're using the AWS WAF API**  

                 

                Specify a base64-encoded version of the value. The maximum length of the value before you base64-encode it is 50 bytes.

                 

                For example, suppose the value of ``Type`` is ``HEADER`` and the value of ``Data`` is ``User-Agent`` . If you want to search the ``User-Agent`` header for the value ``BadBot`` , you base64-encode ``BadBot`` using MIME base64 encoding and include the resulting value, ``QmFkQm90`` , in the value of ``TargetString`` .

                 

                 **If you're using the AWS CLI or one of the AWS SDKs**  

                 

                The value that you want AWS WAF to search for. The SDK automatically base64 encodes the value.

                
              

              - **TextTransformation** *(string) --* 

                Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on ``TargetString`` before inspecting a request for a match.

                 

                 **CMD_LINE**  

                 

                When you're concerned that attackers are injecting an operating system commandline command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

                 

                 
                * Delete the following characters: \ " ' ^ 
                 
                * Delete spaces before the following characters: / ( 
                 
                * Replace the following characters with a space: , ; 
                 
                * Replace multiple spaces with one space 
                 
                * Convert uppercase letters (A-Z) to lowercase (a-z) 
                 

                 

                 **COMPRESS_WHITE_SPACE**  

                 

                Use this option to replace the following characters with a space character (decimal 32):

                 

                 
                * \f, formfeed, decimal 12 
                 
                * \t, tab, decimal 9 
                 
                * \n, newline, decimal 10 
                 
                * \r, carriage return, decimal 13 
                 
                * \v, vertical tab, decimal 11 
                 
                * non-breaking space, decimal 160 
                 

                 

                 ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

                 

                 **HTML_ENTITY_DECODE**  

                 

                Use this option to replace HTML-encoded characters with unencoded characters. ``HTML_ENTITY_DECODE`` performs the following operations:

                 

                 
                * Replaces ``(ampersand)quot;`` with ``"``   
                 
                * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160 
                 
                * Replaces ``(ampersand)lt;`` with a "less than" symbol 
                 
                * Replaces ``(ampersand)gt;`` with ``>``   
                 
                * Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` , with the corresponding characters 
                 
                * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with the corresponding characters 
                 

                 

                 **LOWERCASE**  

                 

                Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

                 

                 **URL_DECODE**  

                 

                Use this option to decode a URL-encoded value.

                 

                 **NONE**  

                 

                Specify ``NONE`` if you don't want to perform any text transformations.

                
              

              - **PositionalConstraint** *(string) --* 

                Within the portion of a web request that you want to search (for example, in the query string, if any), specify where you want AWS WAF to search. Valid values include the following:

                 

                 **CONTAINS**  

                 

                The specified part of the web request must include the value of ``TargetString`` , but the location doesn't matter.

                 

                 **CONTAINS_WORD**  

                 

                The specified part of the web request must include the value of ``TargetString`` , and ``TargetString`` must contain only alphanumeric characters or underscore (A-Z, a-z, 0-9, or _). In addition, ``TargetString`` must be a word, which means one of the following:

                 

                 
                * ``TargetString`` exactly matches the value of the specified part of the web request, such as the value of a header. 
                 
                * ``TargetString`` is at the beginning of the specified part of the web request and is followed by a character other than an alphanumeric character or underscore (_), for example, ``BadBot;`` . 
                 
                * ``TargetString`` is at the end of the specified part of the web request and is preceded by a character other than an alphanumeric character or underscore (_), for example, ``;BadBot`` . 
                 
                * ``TargetString`` is in the middle of the specified part of the web request and is preceded and followed by characters other than alphanumeric characters or underscore (_), for example, ``-BadBot;`` . 
                 

                 

                 **EXACTLY**  

                 

                The value of the specified part of the web request must exactly match the value of ``TargetString`` .

                 

                 **STARTS_WITH**  

                 

                The value of ``TargetString`` must appear at the beginning of the specified part of the web request.

                 

                 **ENDS_WITH**  

                 

                The value of ``TargetString`` must appear at the end of the specified part of the web request.

                
          
        
      
    

    **Examples** 

    The following example returns the details of a byte match set with the ID exampleIDs3t-46da-4fdb-b8d5-abc321j569j5.
    ::

      response = client.get_byte_match_set(
          ByteMatchSetId='exampleIDs3t-46da-4fdb-b8d5-abc321j569j5',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ByteMatchSet': {
              'ByteMatchSetId': 'exampleIDs3t-46da-4fdb-b8d5-abc321j569j5',
              'ByteMatchTuples': [
                  {
                      'FieldToMatch': {
                          'Data': 'referer',
                          'Type': 'HEADER',
                      },
                      'PositionalConstraint': 'CONTAINS',
                      'TargetString': 'badrefer1',
                      'TextTransformation': 'NONE',
                  },
              ],
              'Name': 'ByteMatchNameExample',
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_change_token()

    

    When you want to create, update, or delete AWS WAF objects, get a change token and include the change token in the create, update, or delete request. Change tokens ensure that your application doesn't submit conflicting requests to AWS WAF.

     

    Each create, update, or delete request must use a unique change token. If your application submits a ``GetChangeToken`` request and then submits a second ``GetChangeToken`` request before submitting a create, update, or delete request, the second ``GetChangeToken`` request returns the same value as the first ``GetChangeToken`` request.

     

    When you use a change token in a create, update, or delete request, the status of the change token changes to ``PENDING`` , which indicates that AWS WAF is propagating the change to all AWS WAF servers. Use ``GetChangeTokenStatus`` to determine the status of your change token.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/GetChangeToken>`_    


    **Request Syntax** 
    ::

      response = client.get_change_token()
      
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used in the request. Use this value in a ``GetChangeTokenStatus`` request to get the current status of the request. 

          
    

    **Examples** 

    The following example returns a change token to use for a create, update or delete operation.
    ::

      response = client.get_change_token(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_change_token_status(**kwargs)

    

    Returns the status of a ``ChangeToken`` that you got by calling  GetChangeToken . ``ChangeTokenStatus`` is one of the following values:

     

     
    * ``PROVISIONED`` : You requested the change token by calling ``GetChangeToken`` , but you haven't used it yet in a call to create, update, or delete an AWS WAF object. 
     
    * ``PENDING`` : AWS WAF is propagating the create, update, or delete request to all AWS WAF servers. 
     
    * ``IN_SYNC`` : Propagation is complete. 
     

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/GetChangeTokenStatus>`_    


    **Request Syntax** 
    ::

      response = client.get_change_token_status(
          ChangeToken='string'
      )
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The change token for which you want to get the status. This change token was previously returned in the ``GetChangeToken`` response.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeTokenStatus': 'PROVISIONED'|'PENDING'|'INSYNC'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ChangeTokenStatus** *(string) --* 

          The status of the change token.

          
    

    **Examples** 

    The following example returns the status of a change token with the ID abcd12f2-46da-4fdb-b8d5-fbd4c466928f.
    ::

      response = client.get_change_token_status(
          ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ChangeTokenStatus': 'PENDING',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_geo_match_set(**kwargs)

    

    Returns the  GeoMatchSet that is specified by ``GeoMatchSetId`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/GetGeoMatchSet>`_    


    **Request Syntax** 
    ::

      response = client.get_geo_match_set(
          GeoMatchSetId='string'
      )
    :type GeoMatchSetId: string
    :param GeoMatchSetId: **[REQUIRED]** 

      The ``GeoMatchSetId`` of the  GeoMatchSet that you want to get. ``GeoMatchSetId`` is returned by  CreateGeoMatchSet and by  ListGeoMatchSets .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'GeoMatchSet': {
                'GeoMatchSetId': 'string',
                'Name': 'string',
                'GeoMatchConstraints': [
                    {
                        'Type': 'Country',
                        'Value': 'AF'|'AX'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'|'BH'|'BD'|'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BQ'|'BA'|'BW'|'BV'|'BR'|'IO'|'BN'|'BG'|'BF'|'BI'|'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'|'CG'|'CD'|'CK'|'CR'|'CI'|'HR'|'CU'|'CW'|'CY'|'CZ'|'DK'|'DJ'|'DM'|'DO'|'EC'|'EG'|'SV'|'GQ'|'ER'|'EE'|'ET'|'FK'|'FO'|'FJ'|'FI'|'FR'|'GF'|'PF'|'TF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'|'GR'|'GL'|'GD'|'GP'|'GU'|'GT'|'GG'|'GN'|'GW'|'GY'|'HT'|'HM'|'VA'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'|'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KP'|'KR'|'KW'|'KG'|'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'|'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'|'MT'|'MH'|'MQ'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'|'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'|'NR'|'NP'|'NL'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'|'NF'|'MP'|'NO'|'OM'|'PK'|'PW'|'PS'|'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'RE'|'RO'|'RU'|'RW'|'BL'|'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'|'SC'|'SL'|'SG'|'SX'|'SK'|'SI'|'SB'|'SO'|'ZA'|'GS'|'SS'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'|'CH'|'SY'|'TW'|'TJ'|'TZ'|'TH'|'TL'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'UG'|'UA'|'AE'|'GB'|'US'|'UM'|'UY'|'UZ'|'VU'|'VE'|'VN'|'VG'|'VI'|'WF'|'EH'|'YE'|'ZM'|'ZW'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **GeoMatchSet** *(dict) --* 

          Information about the  GeoMatchSet that you specified in the ``GetGeoMatchSet`` request. This includes the ``Type`` , which for a ``GeoMatchContraint`` is always ``Country`` , as well as the ``Value`` , which is the identifier for a specific country.

          
          

          - **GeoMatchSetId** *(string) --* 

            The ``GeoMatchSetId`` for an ``GeoMatchSet`` . You use ``GeoMatchSetId`` to get information about a ``GeoMatchSet`` (see  GeoMatchSet ), update a ``GeoMatchSet`` (see  UpdateGeoMatchSet ), insert a ``GeoMatchSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete a ``GeoMatchSet`` from AWS WAF (see  DeleteGeoMatchSet ).

             

             ``GeoMatchSetId`` is returned by  CreateGeoMatchSet and by  ListGeoMatchSets .

            
          

          - **Name** *(string) --* 

            A friendly name or description of the  GeoMatchSet . You can't change the name of an ``GeoMatchSet`` after you create it.

            
          

          - **GeoMatchConstraints** *(list) --* 

            An array of  GeoMatchConstraint objects, which contain the country that you want AWS WAF to search for.

            
            

            - *(dict) --* 

              The country from which web requests originate that you want AWS WAF to search for.

              
              

              - **Type** *(string) --* 

                The type of geographical area you want AWS WAF to search for. Currently ``Country`` is the only valid value.

                
              

              - **Value** *(string) --* 

                The country that you want AWS WAF to search for.

                
          
        
      
    

  .. py:method:: get_ip_set(**kwargs)

    

    Returns the  IPSet that is specified by ``IPSetId`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/GetIPSet>`_    


    **Request Syntax** 
    ::

      response = client.get_ip_set(
          IPSetId='string'
      )
    :type IPSetId: string
    :param IPSetId: **[REQUIRED]** 

      The ``IPSetId`` of the  IPSet that you want to get. ``IPSetId`` is returned by  CreateIPSet and by  ListIPSets .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'IPSet': {
                'IPSetId': 'string',
                'Name': 'string',
                'IPSetDescriptors': [
                    {
                        'Type': 'IPV4'|'IPV6',
                        'Value': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **IPSet** *(dict) --* 

          Information about the  IPSet that you specified in the ``GetIPSet`` request. For more information, see the following topics:

           

           
          *  IPSet : Contains ``IPSetDescriptors`` , ``IPSetId`` , and ``Name``   
           
          * ``IPSetDescriptors`` : Contains an array of  IPSetDescriptor objects. Each ``IPSetDescriptor`` object contains ``Type`` and ``Value``   
           

          
          

          - **IPSetId** *(string) --* 

            The ``IPSetId`` for an ``IPSet`` . You use ``IPSetId`` to get information about an ``IPSet`` (see  GetIPSet ), update an ``IPSet`` (see  UpdateIPSet ), insert an ``IPSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete an ``IPSet`` from AWS WAF (see  DeleteIPSet ).

             

             ``IPSetId`` is returned by  CreateIPSet and by  ListIPSets .

            
          

          - **Name** *(string) --* 

            A friendly name or description of the  IPSet . You can't change the name of an ``IPSet`` after you create it.

            
          

          - **IPSetDescriptors** *(list) --* 

            The IP address type (``IPV4`` or ``IPV6`` ) and the IP address range (in CIDR notation) that web requests originate from. If the ``WebACL`` is associated with a CloudFront distribution and the viewer did not use an HTTP proxy or a load balancer to send the request, this is the value of the c-ip field in the CloudFront access logs.

            
            

            - *(dict) --* 

              Specifies the IP address type (``IPV4`` or ``IPV6`` ) and the IP address range (in CIDR format) that web requests originate from.

              
              

              - **Type** *(string) --* 

                Specify ``IPV4`` or ``IPV6`` .

                
              

              - **Value** *(string) --* 

                Specify an IPv4 address by using CIDR notation. For example:

                 

                 
                * To configure AWS WAF to allow, block, or count requests that originated from the IP address 192.0.2.44, specify ``192.0.2.44/32`` . 
                 
                * To configure AWS WAF to allow, block, or count requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify ``192.0.2.0/24`` . 
                 

                 

                For more information about CIDR notation, see the Wikipedia entry `Classless Inter-Domain Routing <https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`__ .

                 

                Specify an IPv6 address by using CIDR notation. For example:

                 

                 
                * To configure AWS WAF to allow, block, or count requests that originated from the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify ``1111:0000:0000:0000:0000:0000:0000:0111/128`` . 
                 
                * To configure AWS WAF to allow, block, or count requests that originated from IP addresses 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify ``1111:0000:0000:0000:0000:0000:0000:0000/64`` . 
                 

                
          
        
      
    

    **Examples** 

    The following example returns the details of an IP match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    ::

      response = client.get_ip_set(
          IPSetId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'IPSet': {
              'IPSetDescriptors': [
                  {
                      'Type': 'IPV4',
                      'Value': '192.0.2.44/32',
                  },
              ],
              'IPSetId': 'example1ds3t-46da-4fdb-b8d5-abc321j569j5',
              'Name': 'MyIPSetFriendlyName',
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


  .. py:method:: get_rate_based_rule(**kwargs)

    

    Returns the  RateBasedRule that is specified by the ``RuleId`` that you included in the ``GetRateBasedRule`` request.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/GetRateBasedRule>`_    


    **Request Syntax** 
    ::

      response = client.get_rate_based_rule(
          RuleId='string'
      )
    :type RuleId: string
    :param RuleId: **[REQUIRED]** 

      The ``RuleId`` of the  RateBasedRule that you want to get. ``RuleId`` is returned by  CreateRateBasedRule and by  ListRateBasedRules .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Rule': {
                'RuleId': 'string',
                'Name': 'string',
                'MetricName': 'string',
                'MatchPredicates': [
                    {
                        'Negated': True|False,
                        'Type': 'IPMatch'|'ByteMatch'|'SqlInjectionMatch'|'GeoMatch'|'SizeConstraint'|'XssMatch'|'RegexMatch',
                        'DataId': 'string'
                    },
                ],
                'RateKey': 'IP',
                'RateLimit': 123
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Rule** *(dict) --* 

          Information about the  RateBasedRule that you specified in the ``GetRateBasedRule`` request.

          
          

          - **RuleId** *(string) --* 

            A unique identifier for a ``RateBasedRule`` . You use ``RuleId`` to get more information about a ``RateBasedRule`` (see  GetRateBasedRule ), update a ``RateBasedRule`` (see  UpdateRateBasedRule ), insert a ``RateBasedRule`` into a ``WebACL`` or delete one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``RateBasedRule`` from AWS WAF (see  DeleteRateBasedRule ).

            
          

          - **Name** *(string) --* 

            A friendly name or description for a ``RateBasedRule`` . You can't change the name of a ``RateBasedRule`` after you create it.

            
          

          - **MetricName** *(string) --* 

            A friendly name or description for the metrics for a ``RateBasedRule`` . The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace. You can't change the name of the metric after you create the ``RateBasedRule`` .

            
          

          - **MatchPredicates** *(list) --* 

            The ``Predicates`` object contains one ``Predicate`` element for each  ByteMatchSet ,  IPSet , or  SqlInjectionMatchSet object that you want to include in a ``RateBasedRule`` .

            
            

            - *(dict) --* 

              Specifies the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , and  SizeConstraintSet objects that you want to add to a ``Rule`` and, for each object, indicates whether you want to negate the settings, for example, requests that do NOT originate from the IP address 192.0.2.44. 

              
              

              - **Negated** *(boolean) --* 

                Set ``Negated`` to ``False`` if you want AWS WAF to allow, block, or count requests based on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow or block requests based on that IP address.

                 

                Set ``Negated`` to ``True`` if you want AWS WAF to allow or block a request based on the negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow, block, or count requests based on all IP addresses *except*  ``192.0.2.44`` .

                
              

              - **Type** *(string) --* 

                The type of predicate in a ``Rule`` , such as ``ByteMatchSet`` or ``IPSet`` .

                
              

              - **DataId** *(string) --* 

                A unique identifier for a predicate in a ``Rule`` , such as ``ByteMatchSetId`` or ``IPSetId`` . The ID is returned by the corresponding ``Create`` or ``List`` command.

                
          
        
          

          - **RateKey** *(string) --* 

            The field that AWS WAF uses to determine if requests are likely arriving from single source and thus subject to rate monitoring. The only valid value for ``RateKey`` is ``IP`` . ``IP`` indicates that requests arriving from the same IP address are subject to the ``RateLimit`` that is specified in the ``RateBasedRule`` .

            
          

          - **RateLimit** *(integer) --* 

            The maximum number of requests, which have an identical value in the field specified by the ``RateKey`` , allowed in a five-minute period. If the number of requests exceeds the ``RateLimit`` and the other predicates specified in the rule are also met, AWS WAF triggers the action that is specified for this rule.

            
      
    

  .. py:method:: get_rate_based_rule_managed_keys(**kwargs)

    

    Returns an array of IP addresses currently being blocked by the  RateBasedRule that is specified by the ``RuleId`` . The maximum number of managed keys that will be blocked is 10,000. If more than 10,000 addresses exceed the rate limit, the 10,000 addresses with the highest rates will be blocked.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/GetRateBasedRuleManagedKeys>`_    


    **Request Syntax** 
    ::

      response = client.get_rate_based_rule_managed_keys(
          RuleId='string',
          NextMarker='string'
      )
    :type RuleId: string
    :param RuleId: **[REQUIRED]** 

      The ``RuleId`` of the  RateBasedRule for which you want to get a list of ``ManagedKeys`` . ``RuleId`` is returned by  CreateRateBasedRule and by  ListRateBasedRules .

      

    
    :type NextMarker: string
    :param NextMarker: 

      A null value and not currently used. Do not include this in your request.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ManagedKeys': [
                'string',
            ],
            'NextMarker': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ManagedKeys** *(list) --* 

          An array of IP addresses that currently are blocked by the specified  RateBasedRule . 

          
          

          - *(string) --* 
      
        

        - **NextMarker** *(string) --* 

          A null value and not currently used.

          
    

  .. py:method:: get_regex_match_set(**kwargs)

    

    Returns the  RegexMatchSet specified by ``RegexMatchSetId`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/GetRegexMatchSet>`_    


    **Request Syntax** 
    ::

      response = client.get_regex_match_set(
          RegexMatchSetId='string'
      )
    :type RegexMatchSetId: string
    :param RegexMatchSetId: **[REQUIRED]** 

      The ``RegexMatchSetId`` of the  RegexMatchSet that you want to get. ``RegexMatchSetId`` is returned by  CreateRegexMatchSet and by  ListRegexMatchSets .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'RegexMatchSet': {
                'RegexMatchSetId': 'string',
                'Name': 'string',
                'RegexMatchTuples': [
                    {
                        'FieldToMatch': {
                            'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
                            'Data': 'string'
                        },
                        'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE',
                        'RegexPatternSetId': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **RegexMatchSet** *(dict) --* 

          Information about the  RegexMatchSet that you specified in the ``GetRegexMatchSet`` request. For more information, see  RegexMatchTuple .

          
          

          - **RegexMatchSetId** *(string) --* 

            The ``RegexMatchSetId`` for a ``RegexMatchSet`` . You use ``RegexMatchSetId`` to get information about a ``RegexMatchSet`` (see  GetRegexMatchSet ), update a ``RegexMatchSet`` (see  UpdateRegexMatchSet ), insert a ``RegexMatchSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete a ``RegexMatchSet`` from AWS WAF (see  DeleteRegexMatchSet ).

             

             ``RegexMatchSetId`` is returned by  CreateRegexMatchSet and by  ListRegexMatchSets .

            
          

          - **Name** *(string) --* 

            A friendly name or description of the  RegexMatchSet . You can't change ``Name`` after you create a ``RegexMatchSet`` .

            
          

          - **RegexMatchTuples** *(list) --* 

            Contains an array of  RegexMatchTuple objects. Each ``RegexMatchTuple`` object contains: 

             

             
            * The part of a web request that you want AWS WAF to inspect, such as a query string or the value of the ``User-Agent`` header.  
             
            * The identifier of the pattern (a regular expression) that you want AWS WAF to look for. For more information, see  RegexPatternSet . 
             
            * Whether to perform any conversions on the request, such as converting it to lowercase, before inspecting it for the specified string. 
             

            
            

            - *(dict) --* 

              The regular expression pattern that you want AWS WAF to search for in web requests, the location in requests that you want AWS WAF to search, and other settings. Each ``RegexMatchTuple`` object contains: 

               

               
              * The part of a web request that you want AWS WAF to inspect, such as a query string or the value of the ``User-Agent`` header.  
               
              * The identifier of the pattern (a regular expression) that you want AWS WAF to look for. For more information, see  RegexPatternSet .  
               
              * Whether to perform any conversions on the request, such as converting it to lowercase, before inspecting it for the specified string. 
               

              
              

              - **FieldToMatch** *(dict) --* 

                Specifies where in a web request to look for the ``RegexPatternSet`` .

                
                

                - **Type** *(string) --* 

                  The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

                   

                   
                  * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the header in ``Data`` . 
                   
                  * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` . 
                   
                  * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a ``?`` character, if any. 
                   
                  * ``URI`` : The part of a web request that identifies a resource, for example, ``/images/daily-ad.jpg`` . 
                   
                  * ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .  
                   

                  
                

                - **Data** *(string) --* 

                  When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . If the value of ``Type`` is any other value, omit ``Data`` .

                   

                  The name of the header is not case sensitive.

                  
            
              

              - **TextTransformation** *(string) --* 

                Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on ``RegexPatternSet`` before inspecting a request for a match.

                 

                 **CMD_LINE**  

                 

                When you're concerned that attackers are injecting an operating system commandline command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

                 

                 
                * Delete the following characters: \ " ' ^ 
                 
                * Delete spaces before the following characters: / ( 
                 
                * Replace the following characters with a space: , ; 
                 
                * Replace multiple spaces with one space 
                 
                * Convert uppercase letters (A-Z) to lowercase (a-z) 
                 

                 

                 **COMPRESS_WHITE_SPACE**  

                 

                Use this option to replace the following characters with a space character (decimal 32):

                 

                 
                * \f, formfeed, decimal 12 
                 
                * \t, tab, decimal 9 
                 
                * \n, newline, decimal 10 
                 
                * \r, carriage return, decimal 13 
                 
                * \v, vertical tab, decimal 11 
                 
                * non-breaking space, decimal 160 
                 

                 

                 ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

                 

                 **HTML_ENTITY_DECODE**  

                 

                Use this option to replace HTML-encoded characters with unencoded characters. ``HTML_ENTITY_DECODE`` performs the following operations:

                 

                 
                * Replaces ``(ampersand)quot;`` with ``"``   
                 
                * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160 
                 
                * Replaces ``(ampersand)lt;`` with a "less than" symbol 
                 
                * Replaces ``(ampersand)gt;`` with ``>``   
                 
                * Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` , with the corresponding characters 
                 
                * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with the corresponding characters 
                 

                 

                 **LOWERCASE**  

                 

                Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

                 

                 **URL_DECODE**  

                 

                Use this option to decode a URL-encoded value.

                 

                 **NONE**  

                 

                Specify ``NONE`` if you don't want to perform any text transformations.

                
              

              - **RegexPatternSetId** *(string) --* 

                The ``RegexPatternSetId`` for a ``RegexPatternSet`` . You use ``RegexPatternSetId`` to get information about a ``RegexPatternSet`` (see  GetRegexPatternSet ), update a ``RegexPatternSet`` (see  UpdateRegexPatternSet ), insert a ``RegexPatternSet`` into a ``RegexMatchSet`` or delete one from a ``RegexMatchSet`` (see  UpdateRegexMatchSet ), and delete an ``RegexPatternSet`` from AWS WAF (see  DeleteRegexPatternSet ).

                 

                 ``RegexPatternSetId`` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .

                
          
        
      
    

  .. py:method:: get_regex_pattern_set(**kwargs)

    

    Returns the  RegexPatternSet specified by ``RegexPatternSetId`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/GetRegexPatternSet>`_    


    **Request Syntax** 
    ::

      response = client.get_regex_pattern_set(
          RegexPatternSetId='string'
      )
    :type RegexPatternSetId: string
    :param RegexPatternSetId: **[REQUIRED]** 

      The ``RegexPatternSetId`` of the  RegexPatternSet that you want to get. ``RegexPatternSetId`` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'RegexPatternSet': {
                'RegexPatternSetId': 'string',
                'Name': 'string',
                'RegexPatternStrings': [
                    'string',
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **RegexPatternSet** *(dict) --* 

          Information about the  RegexPatternSet that you specified in the ``GetRegexPatternSet`` request, including the identifier of the pattern set and the regular expression patterns you want AWS WAF to search for. 

          
          

          - **RegexPatternSetId** *(string) --* 

            The identifier for the ``RegexPatternSet`` . You use ``RegexPatternSetId`` to get information about a ``RegexPatternSet`` , update a ``RegexPatternSet`` , remove a ``RegexPatternSet`` from a ``RegexMatchSet`` , and delete a ``RegexPatternSet`` from AWS WAF.

             

             ``RegexMatchSetId`` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .

            
          

          - **Name** *(string) --* 

            A friendly name or description of the  RegexPatternSet . You can't change ``Name`` after you create a ``RegexPatternSet`` .

            
          

          - **RegexPatternStrings** *(list) --* 

            Specifies the regular expression (regex) patterns that you want AWS WAF to search for, such as ``B[a@]dB[o0]t`` .

            
            

            - *(string) --* 
        
      
    

  .. py:method:: get_rule(**kwargs)

    

    Returns the  Rule that is specified by the ``RuleId`` that you included in the ``GetRule`` request.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/GetRule>`_    


    **Request Syntax** 
    ::

      response = client.get_rule(
          RuleId='string'
      )
    :type RuleId: string
    :param RuleId: **[REQUIRED]** 

      The ``RuleId`` of the  Rule that you want to get. ``RuleId`` is returned by  CreateRule and by  ListRules .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Rule': {
                'RuleId': 'string',
                'Name': 'string',
                'MetricName': 'string',
                'Predicates': [
                    {
                        'Negated': True|False,
                        'Type': 'IPMatch'|'ByteMatch'|'SqlInjectionMatch'|'GeoMatch'|'SizeConstraint'|'XssMatch'|'RegexMatch',
                        'DataId': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Rule** *(dict) --* 

          Information about the  Rule that you specified in the ``GetRule`` request. For more information, see the following topics:

           

           
          *  Rule : Contains ``MetricName`` , ``Name`` , an array of ``Predicate`` objects, and ``RuleId``   
           
          *  Predicate : Each ``Predicate`` object contains ``DataId`` , ``Negated`` , and ``Type``   
           

          
          

          - **RuleId** *(string) --* 

            A unique identifier for a ``Rule`` . You use ``RuleId`` to get more information about a ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule`` from AWS WAF (see  DeleteRule ).

             

             ``RuleId`` is returned by  CreateRule and by  ListRules .

            
          

          - **Name** *(string) --* 

            The friendly name or description for the ``Rule`` . You can't change the name of a ``Rule`` after you create it.

            
          

          - **MetricName** *(string) --* 

            A friendly name or description for the metrics for this ``Rule`` . The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace. You can't change ``MetricName`` after you create the ``Rule`` .

            
          

          - **Predicates** *(list) --* 

            The ``Predicates`` object contains one ``Predicate`` element for each  ByteMatchSet ,  IPSet , or  SqlInjectionMatchSet object that you want to include in a ``Rule`` .

            
            

            - *(dict) --* 

              Specifies the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , and  SizeConstraintSet objects that you want to add to a ``Rule`` and, for each object, indicates whether you want to negate the settings, for example, requests that do NOT originate from the IP address 192.0.2.44. 

              
              

              - **Negated** *(boolean) --* 

                Set ``Negated`` to ``False`` if you want AWS WAF to allow, block, or count requests based on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow or block requests based on that IP address.

                 

                Set ``Negated`` to ``True`` if you want AWS WAF to allow or block a request based on the negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow, block, or count requests based on all IP addresses *except*  ``192.0.2.44`` .

                
              

              - **Type** *(string) --* 

                The type of predicate in a ``Rule`` , such as ``ByteMatchSet`` or ``IPSet`` .

                
              

              - **DataId** *(string) --* 

                A unique identifier for a predicate in a ``Rule`` , such as ``ByteMatchSetId`` or ``IPSetId`` . The ID is returned by the corresponding ``Create`` or ``List`` command.

                
          
        
      
    

    **Examples** 

    The following example returns the details of a rule with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    ::

      response = client.get_rule(
          RuleId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Rule': {
              'MetricName': 'WAFByteHeaderRule',
              'Name': 'WAFByteHeaderRule',
              'Predicates': [
                  {
                      'DataId': 'MyByteMatchSetID',
                      'Negated': False,
                      'Type': 'ByteMatch',
                  },
              ],
              'RuleId': 'example1ds3t-46da-4fdb-b8d5-abc321j569j5',
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_rule_group(**kwargs)

    

    Returns the  RuleGroup that is specified by the ``RuleGroupId`` that you included in the ``GetRuleGroup`` request.

     

    To view the rules in a rule group, use  ListActivatedRulesInRuleGroup .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/GetRuleGroup>`_    


    **Request Syntax** 
    ::

      response = client.get_rule_group(
          RuleGroupId='string'
      )
    :type RuleGroupId: string
    :param RuleGroupId: **[REQUIRED]** 

      The ``RuleGroupId`` of the  RuleGroup that you want to get. ``RuleGroupId`` is returned by  CreateRuleGroup and by  ListRuleGroups .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'RuleGroup': {
                'RuleGroupId': 'string',
                'Name': 'string',
                'MetricName': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **RuleGroup** *(dict) --* 

          Information about the  RuleGroup that you specified in the ``GetRuleGroup`` request. 

          
          

          - **RuleGroupId** *(string) --* 

            A unique identifier for a ``RuleGroup`` . You use ``RuleGroupId`` to get more information about a ``RuleGroup`` (see  GetRuleGroup ), update a ``RuleGroup`` (see  UpdateRuleGroup ), insert a ``RuleGroup`` into a ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``RuleGroup`` from AWS WAF (see  DeleteRuleGroup ).

             

             ``RuleGroupId`` is returned by  CreateRuleGroup and by  ListRuleGroups .

            
          

          - **Name** *(string) --* 

            The friendly name or description for the ``RuleGroup`` . You can't change the name of a ``RuleGroup`` after you create it.

            
          

          - **MetricName** *(string) --* 

            A friendly name or description for the metrics for this ``RuleGroup`` . The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace. You can't change the name of the metric after you create the ``RuleGroup`` .

            
      
    

  .. py:method:: get_sampled_requests(**kwargs)

    

    Gets detailed information about a specified number of requests--a sample--that AWS WAF randomly selects from among the first 5,000 requests that your AWS resource received during a time range that you choose. You can specify a sample size of up to 500 requests, and you can specify any time range in the previous three hours.

     

     ``GetSampledRequests`` returns a time range, which is usually the time range that you specified. However, if your resource (such as a CloudFront distribution) received 5,000 requests before the specified time range elapsed, ``GetSampledRequests`` returns an updated time range. This new time range indicates the actual period during which AWS WAF selected the requests in the sample.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/GetSampledRequests>`_    


    **Request Syntax** 
    ::

      response = client.get_sampled_requests(
          WebAclId='string',
          RuleId='string',
          TimeWindow={
              'StartTime': datetime(2015, 1, 1),
              'EndTime': datetime(2015, 1, 1)
          },
          MaxItems=123
      )
    :type WebAclId: string
    :param WebAclId: **[REQUIRED]** 

      The ``WebACLId`` of the ``WebACL`` for which you want ``GetSampledRequests`` to return a sample of requests.

      

    
    :type RuleId: string
    :param RuleId: **[REQUIRED]** 

       ``RuleId`` is one of three values:

       

       
      * The ``RuleId`` of the ``Rule`` or the ``RuleGroupId`` of the ``RuleGroup`` for which you want ``GetSampledRequests`` to return a sample of requests. 
       
      * ``Default_Action`` , which causes ``GetSampledRequests`` to return a sample of the requests that didn't match any of the rules in the specified ``WebACL`` . 
       

      

    
    :type TimeWindow: dict
    :param TimeWindow: **[REQUIRED]** 

      The start date and time and the end date and time of the range for which you want ``GetSampledRequests`` to return a sample of requests. Specify the date and time in the following format: ``"2016-09-27T14:50Z"`` . You can specify any time range in the previous three hours.

      

    
      - **StartTime** *(datetime) --* **[REQUIRED]** 

        The beginning of the time range from which you want ``GetSampledRequests`` to return a sample of the requests that your AWS resource received. Specify the date and time in the following format: ``"2016-09-27T14:50Z"`` . You can specify any time range in the previous three hours.

        

      
      - **EndTime** *(datetime) --* **[REQUIRED]** 

        The end of the time range from which you want ``GetSampledRequests`` to return a sample of the requests that your AWS resource received. Specify the date and time in the following format: ``"2016-09-27T14:50Z"`` . You can specify any time range in the previous three hours.

        

      
    
    :type MaxItems: integer
    :param MaxItems: **[REQUIRED]** 

      The number of requests that you want AWS WAF to return from among the first 5,000 requests that your AWS resource received during the time range. If your resource received fewer requests than the value of ``MaxItems`` , ``GetSampledRequests`` returns information about all of them. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'SampledRequests': [
                {
                    'Request': {
                        'ClientIP': 'string',
                        'Country': 'string',
                        'URI': 'string',
                        'Method': 'string',
                        'HTTPVersion': 'string',
                        'Headers': [
                            {
                                'Name': 'string',
                                'Value': 'string'
                            },
                        ]
                    },
                    'Weight': 123,
                    'Timestamp': datetime(2015, 1, 1),
                    'Action': 'string',
                    'RuleWithinRuleGroup': 'string'
                },
            ],
            'PopulationSize': 123,
            'TimeWindow': {
                'StartTime': datetime(2015, 1, 1),
                'EndTime': datetime(2015, 1, 1)
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **SampledRequests** *(list) --* 

          A complex type that contains detailed information about each of the requests in the sample.

          
          

          - *(dict) --* 

            The response from a  GetSampledRequests request includes a ``SampledHTTPRequests`` complex type that appears as ``SampledRequests`` in the response syntax. ``SampledHTTPRequests`` contains one ``SampledHTTPRequest`` object for each web request that is returned by ``GetSampledRequests`` .

            
            

            - **Request** *(dict) --* 

              A complex type that contains detailed information about the request.

              
              

              - **ClientIP** *(string) --* 

                The IP address that the request originated from. If the ``WebACL`` is associated with a CloudFront distribution, this is the value of one of the following fields in CloudFront access logs:

                 

                 
                * ``c-ip`` , if the viewer did not use an HTTP proxy or a load balancer to send the request 
                 
                * ``x-forwarded-for`` , if the viewer did use an HTTP proxy or a load balancer to send the request 
                 

                
              

              - **Country** *(string) --* 

                The two-letter country code for the country that the request originated from. For a current list of country codes, see the Wikipedia entry `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ .

                
              

              - **URI** *(string) --* 

                The part of a web request that identifies the resource, for example, ``/images/daily-ad.jpg`` .

                
              

              - **Method** *(string) --* 

                The HTTP method specified in the sampled web request. CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` . 

                
              

              - **HTTPVersion** *(string) --* 

                The HTTP version specified in the sampled web request, for example, ``HTTP/1.1`` .

                
              

              - **Headers** *(list) --* 

                A complex type that contains two values for each header in the sampled web request: the name of the header and the value of the header.

                
                

                - *(dict) --* 

                  The response from a  GetSampledRequests request includes an ``HTTPHeader`` complex type that appears as ``Headers`` in the response syntax. ``HTTPHeader`` contains the names and values of all of the headers that appear in one of the web requests that were returned by ``GetSampledRequests`` . 

                  
                  

                  - **Name** *(string) --* 

                    The name of one of the headers in the sampled web request.

                    
                  

                  - **Value** *(string) --* 

                    The value of one of the headers in the sampled web request.

                    
              
            
          
            

            - **Weight** *(integer) --* 

              A value that indicates how one result in the response relates proportionally to other results in the response. A result that has a weight of ``2`` represents roughly twice as many CloudFront web requests as a result that has a weight of ``1`` .

              
            

            - **Timestamp** *(datetime) --* 

              The time at which AWS WAF received the request from your AWS resource, in Unix time format (in seconds).

              
            

            - **Action** *(string) --* 

              The action for the ``Rule`` that the request matched: ``ALLOW`` , ``BLOCK`` , or ``COUNT`` .

              
            

            - **RuleWithinRuleGroup** *(string) --* 

              This value is returned if the ``GetSampledRequests`` request specifies the ID of a ``RuleGroup`` rather than the ID of an individual rule. ``RuleWithinRuleGroup`` is the rule within the specified ``RuleGroup`` that matched the request listed in the response.

              
        
      
        

        - **PopulationSize** *(integer) --* 

          The total number of requests from which ``GetSampledRequests`` got a sample of ``MaxItems`` requests. If ``PopulationSize`` is less than ``MaxItems`` , the sample includes every request that your AWS resource received during the specified time range.

          
        

        - **TimeWindow** *(dict) --* 

          Usually, ``TimeWindow`` is the time range that you specified in the ``GetSampledRequests`` request. However, if your AWS resource received more than 5,000 requests during the time range that you specified in the request, ``GetSampledRequests`` returns the time range for the first 5,000 requests.

          
          

          - **StartTime** *(datetime) --* 

            The beginning of the time range from which you want ``GetSampledRequests`` to return a sample of the requests that your AWS resource received. Specify the date and time in the following format: ``"2016-09-27T14:50Z"`` . You can specify any time range in the previous three hours.

            
          

          - **EndTime** *(datetime) --* 

            The end of the time range from which you want ``GetSampledRequests`` to return a sample of the requests that your AWS resource received. Specify the date and time in the following format: ``"2016-09-27T14:50Z"`` . You can specify any time range in the previous three hours.

            
      
    

    **Examples** 

    The following example returns detailed information about 100 requests --a sample-- that AWS WAF randomly selects from among the first 5,000 requests that your AWS resource received between the time period 2016-09-27T15:50Z to 2016-09-27T15:50Z.
    ::

      response = client.get_sampled_requests(
          MaxItems=100,
          RuleId='WAFRule-1-Example',
          TimeWindow={
              'EndTime': datetime(2016, 9, 27, 15, 50, 0, 1, 271, 0),
              'StartTime': datetime(2016, 9, 27, 15, 50, 0, 1, 271, 0),
          },
          WebAclId='createwebacl-1472061481310',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'PopulationSize': 50,
          'SampledRequests': [
              {
                  'Action': 'BLOCK',
                  'Request': {
                      'ClientIP': '192.0.2.44',
                      'Country': 'US',
                      'HTTPVersion': 'HTTP/1.1',
                      'Headers': [
                          {
                              'Name': 'User-Agent',
                              'Value': 'BadBot ',
                          },
                      ],
                      'Method': 'HEAD',
                  },
                  'Timestamp': datetime(2016, 9, 27, 14, 55, 0, 1, 271, 0),
                  'Weight': 1,
              },
          ],
          'TimeWindow': {
              'EndTime': datetime(2016, 9, 27, 15, 50, 0, 1, 271, 0),
              'StartTime': datetime(2016, 9, 27, 14, 50, 0, 1, 271, 0),
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_size_constraint_set(**kwargs)

    

    Returns the  SizeConstraintSet specified by ``SizeConstraintSetId`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/GetSizeConstraintSet>`_    


    **Request Syntax** 
    ::

      response = client.get_size_constraint_set(
          SizeConstraintSetId='string'
      )
    :type SizeConstraintSetId: string
    :param SizeConstraintSetId: **[REQUIRED]** 

      The ``SizeConstraintSetId`` of the  SizeConstraintSet that you want to get. ``SizeConstraintSetId`` is returned by  CreateSizeConstraintSet and by  ListSizeConstraintSets .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'SizeConstraintSet': {
                'SizeConstraintSetId': 'string',
                'Name': 'string',
                'SizeConstraints': [
                    {
                        'FieldToMatch': {
                            'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
                            'Data': 'string'
                        },
                        'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE',
                        'ComparisonOperator': 'EQ'|'NE'|'LE'|'LT'|'GE'|'GT',
                        'Size': 123
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **SizeConstraintSet** *(dict) --* 

          Information about the  SizeConstraintSet that you specified in the ``GetSizeConstraintSet`` request. For more information, see the following topics:

           

           
          *  SizeConstraintSet : Contains ``SizeConstraintSetId`` , ``SizeConstraints`` , and ``Name``   
           
          * ``SizeConstraints`` : Contains an array of  SizeConstraint objects. Each ``SizeConstraint`` object contains  FieldToMatch , ``TextTransformation`` , ``ComparisonOperator`` , and ``Size``   
           
          *  FieldToMatch : Contains ``Data`` and ``Type``   
           

          
          

          - **SizeConstraintSetId** *(string) --* 

            A unique identifier for a ``SizeConstraintSet`` . You use ``SizeConstraintSetId`` to get information about a ``SizeConstraintSet`` (see  GetSizeConstraintSet ), update a ``SizeConstraintSet`` (see  UpdateSizeConstraintSet ), insert a ``SizeConstraintSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete a ``SizeConstraintSet`` from AWS WAF (see  DeleteSizeConstraintSet ).

             

             ``SizeConstraintSetId`` is returned by  CreateSizeConstraintSet and by  ListSizeConstraintSets .

            
          

          - **Name** *(string) --* 

            The name, if any, of the ``SizeConstraintSet`` .

            
          

          - **SizeConstraints** *(list) --* 

            Specifies the parts of web requests that you want to inspect the size of.

            
            

            - *(dict) --* 

              Specifies a constraint on the size of a part of the web request. AWS WAF uses the ``Size`` , ``ComparisonOperator`` , and ``FieldToMatch`` to build an expression in the form of "``Size``  ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that expression is true, the ``SizeConstraint`` is considered to match.

              
              

              - **FieldToMatch** *(dict) --* 

                Specifies where in a web request to look for the size constraint.

                
                

                - **Type** *(string) --* 

                  The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

                   

                   
                  * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the header in ``Data`` . 
                   
                  * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` . 
                   
                  * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a ``?`` character, if any. 
                   
                  * ``URI`` : The part of a web request that identifies a resource, for example, ``/images/daily-ad.jpg`` . 
                   
                  * ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .  
                   

                  
                

                - **Data** *(string) --* 

                  When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . If the value of ``Type`` is any other value, omit ``Data`` .

                   

                  The name of the header is not case sensitive.

                  
            
              

              - **TextTransformation** *(string) --* 

                Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

                 

                Note that if you choose ``BODY`` for the value of ``Type`` , you must choose ``NONE`` for ``TextTransformation`` because CloudFront forwards only the first 8192 bytes for inspection. 

                 

                 **NONE**  

                 

                Specify ``NONE`` if you don't want to perform any text transformations.

                 

                 **CMD_LINE**  

                 

                When you're concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

                 

                 
                * Delete the following characters: \ " ' ^ 
                 
                * Delete spaces before the following characters: / ( 
                 
                * Replace the following characters with a space: , ; 
                 
                * Replace multiple spaces with one space 
                 
                * Convert uppercase letters (A-Z) to lowercase (a-z) 
                 

                 

                 **COMPRESS_WHITE_SPACE**  

                 

                Use this option to replace the following characters with a space character (decimal 32):

                 

                 
                * \f, formfeed, decimal 12 
                 
                * \t, tab, decimal 9 
                 
                * \n, newline, decimal 10 
                 
                * \r, carriage return, decimal 13 
                 
                * \v, vertical tab, decimal 11 
                 
                * non-breaking space, decimal 160 
                 

                 

                 ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

                 

                 **HTML_ENTITY_DECODE**  

                 

                Use this option to replace HTML-encoded characters with unencoded characters. ``HTML_ENTITY_DECODE`` performs the following operations:

                 

                 
                * Replaces ``(ampersand)quot;`` with ``"``   
                 
                * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160 
                 
                * Replaces ``(ampersand)lt;`` with a "less than" symbol 
                 
                * Replaces ``(ampersand)gt;`` with ``>``   
                 
                * Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` , with the corresponding characters 
                 
                * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with the corresponding characters 
                 

                 

                 **LOWERCASE**  

                 

                Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

                 

                 **URL_DECODE**  

                 

                Use this option to decode a URL-encoded value.

                
              

              - **ComparisonOperator** *(string) --* 

                The type of comparison you want AWS WAF to perform. AWS WAF uses this in combination with the provided ``Size`` and ``FieldToMatch`` to build an expression in the form of "``Size``  ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that expression is true, the ``SizeConstraint`` is considered to match.

                 

                 **EQ** : Used to test if the ``Size`` is equal to the size of the ``FieldToMatch``  

                 

                 **NE** : Used to test if the ``Size`` is not equal to the size of the ``FieldToMatch``  

                 

                 **LE** : Used to test if the ``Size`` is less than or equal to the size of the ``FieldToMatch``  

                 

                 **LT** : Used to test if the ``Size`` is strictly less than the size of the ``FieldToMatch``  

                 

                 **GE** : Used to test if the ``Size`` is greater than or equal to the size of the ``FieldToMatch``  

                 

                 **GT** : Used to test if the ``Size`` is strictly greater than the size of the ``FieldToMatch``  

                
              

              - **Size** *(integer) --* 

                The size in bytes that you want AWS WAF to compare against the size of the specified ``FieldToMatch`` . AWS WAF uses this in combination with ``ComparisonOperator`` and ``FieldToMatch`` to build an expression in the form of "``Size``  ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that expression is true, the ``SizeConstraint`` is considered to match.

                 

                Valid values for size are 0 - 21474836480 bytes (0 - 20 GB).

                 

                If you specify ``URI`` for the value of ``Type`` , the / in the URI counts as one character. For example, the URI ``/logo.jpg`` is nine characters long.

                
          
        
      
    

    **Examples** 

    The following example returns the details of a size constraint match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    ::

      response = client.get_size_constraint_set(
          SizeConstraintSetId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'SizeConstraintSet': {
              'Name': 'MySampleSizeConstraintSet',
              'SizeConstraintSetId': 'example1ds3t-46da-4fdb-b8d5-abc321j569j5',
              'SizeConstraints': [
                  {
                      'ComparisonOperator': 'GT',
                      'FieldToMatch': {
                          'Type': 'QUERY_STRING',
                      },
                      'Size': 0,
                      'TextTransformation': 'NONE',
                  },
              ],
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_sql_injection_match_set(**kwargs)

    

    Returns the  SqlInjectionMatchSet that is specified by ``SqlInjectionMatchSetId`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/GetSqlInjectionMatchSet>`_    


    **Request Syntax** 
    ::

      response = client.get_sql_injection_match_set(
          SqlInjectionMatchSetId='string'
      )
    :type SqlInjectionMatchSetId: string
    :param SqlInjectionMatchSetId: **[REQUIRED]** 

      The ``SqlInjectionMatchSetId`` of the  SqlInjectionMatchSet that you want to get. ``SqlInjectionMatchSetId`` is returned by  CreateSqlInjectionMatchSet and by  ListSqlInjectionMatchSets .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'SqlInjectionMatchSet': {
                'SqlInjectionMatchSetId': 'string',
                'Name': 'string',
                'SqlInjectionMatchTuples': [
                    {
                        'FieldToMatch': {
                            'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
                            'Data': 'string'
                        },
                        'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        The response to a  GetSqlInjectionMatchSet request.

        
        

        - **SqlInjectionMatchSet** *(dict) --* 

          Information about the  SqlInjectionMatchSet that you specified in the ``GetSqlInjectionMatchSet`` request. For more information, see the following topics:

           

           
          *  SqlInjectionMatchSet : Contains ``Name`` , ``SqlInjectionMatchSetId`` , and an array of ``SqlInjectionMatchTuple`` objects 
           
          *  SqlInjectionMatchTuple : Each ``SqlInjectionMatchTuple`` object contains ``FieldToMatch`` and ``TextTransformation``   
           
          *  FieldToMatch : Contains ``Data`` and ``Type``   
           

          
          

          - **SqlInjectionMatchSetId** *(string) --* 

            A unique identifier for a ``SqlInjectionMatchSet`` . You use ``SqlInjectionMatchSetId`` to get information about a ``SqlInjectionMatchSet`` (see  GetSqlInjectionMatchSet ), update a ``SqlInjectionMatchSet`` (see  UpdateSqlInjectionMatchSet ), insert a ``SqlInjectionMatchSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete a ``SqlInjectionMatchSet`` from AWS WAF (see  DeleteSqlInjectionMatchSet ).

             

             ``SqlInjectionMatchSetId`` is returned by  CreateSqlInjectionMatchSet and by  ListSqlInjectionMatchSets .

            
          

          - **Name** *(string) --* 

            The name, if any, of the ``SqlInjectionMatchSet`` .

            
          

          - **SqlInjectionMatchTuples** *(list) --* 

            Specifies the parts of web requests that you want to inspect for snippets of malicious SQL code.

            
            

            - *(dict) --* 

              Specifies the part of a web request that you want AWS WAF to inspect for snippets of malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.

              
              

              - **FieldToMatch** *(dict) --* 

                Specifies where in a web request to look for snippets of malicious SQL code.

                
                

                - **Type** *(string) --* 

                  The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

                   

                   
                  * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the header in ``Data`` . 
                   
                  * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` . 
                   
                  * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a ``?`` character, if any. 
                   
                  * ``URI`` : The part of a web request that identifies a resource, for example, ``/images/daily-ad.jpg`` . 
                   
                  * ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .  
                   

                  
                

                - **Data** *(string) --* 

                  When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . If the value of ``Type`` is any other value, omit ``Data`` .

                   

                  The name of the header is not case sensitive.

                  
            
              

              - **TextTransformation** *(string) --* 

                Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

                 

                 **CMD_LINE**  

                 

                When you're concerned that attackers are injecting an operating system commandline command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

                 

                 
                * Delete the following characters: \ " ' ^ 
                 
                * Delete spaces before the following characters: / ( 
                 
                * Replace the following characters with a space: , ; 
                 
                * Replace multiple spaces with one space 
                 
                * Convert uppercase letters (A-Z) to lowercase (a-z) 
                 

                 

                 **COMPRESS_WHITE_SPACE**  

                 

                Use this option to replace the following characters with a space character (decimal 32):

                 

                 
                * \f, formfeed, decimal 12 
                 
                * \t, tab, decimal 9 
                 
                * \n, newline, decimal 10 
                 
                * \r, carriage return, decimal 13 
                 
                * \v, vertical tab, decimal 11 
                 
                * non-breaking space, decimal 160 
                 

                 

                 ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

                 

                 **HTML_ENTITY_DECODE**  

                 

                Use this option to replace HTML-encoded characters with unencoded characters. ``HTML_ENTITY_DECODE`` performs the following operations:

                 

                 
                * Replaces ``(ampersand)quot;`` with ``"``   
                 
                * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160 
                 
                * Replaces ``(ampersand)lt;`` with a "less than" symbol 
                 
                * Replaces ``(ampersand)gt;`` with ``>``   
                 
                * Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` , with the corresponding characters 
                 
                * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with the corresponding characters 
                 

                 

                 **LOWERCASE**  

                 

                Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

                 

                 **URL_DECODE**  

                 

                Use this option to decode a URL-encoded value.

                 

                 **NONE**  

                 

                Specify ``NONE`` if you don't want to perform any text transformations.

                
          
        
      
    

    **Examples** 

    The following example returns the details of a SQL injection match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    ::

      response = client.get_sql_injection_match_set(
          SqlInjectionMatchSetId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'SqlInjectionMatchSet': {
              'Name': 'MySQLInjectionMatchSet',
              'SqlInjectionMatchSetId': 'example1ds3t-46da-4fdb-b8d5-abc321j569j5',
              'SqlInjectionMatchTuples': [
                  {
                      'FieldToMatch': {
                          'Type': 'QUERY_STRING',
                      },
                      'TextTransformation': 'URL_DECODE',
                  },
              ],
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: get_web_acl(**kwargs)

    

    Returns the  WebACL that is specified by ``WebACLId`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/GetWebACL>`_    


    **Request Syntax** 
    ::

      response = client.get_web_acl(
          WebACLId='string'
      )
    :type WebACLId: string
    :param WebACLId: **[REQUIRED]** 

      The ``WebACLId`` of the  WebACL that you want to get. ``WebACLId`` is returned by  CreateWebACL and by  ListWebACLs .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'WebACL': {
                'WebACLId': 'string',
                'Name': 'string',
                'MetricName': 'string',
                'DefaultAction': {
                    'Type': 'BLOCK'|'ALLOW'|'COUNT'
                },
                'Rules': [
                    {
                        'Priority': 123,
                        'RuleId': 'string',
                        'Action': {
                            'Type': 'BLOCK'|'ALLOW'|'COUNT'
                        },
                        'OverrideAction': {
                            'Type': 'NONE'|'COUNT'
                        },
                        'Type': 'REGULAR'|'RATE_BASED'|'GROUP'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **WebACL** *(dict) --* 

          Information about the  WebACL that you specified in the ``GetWebACL`` request. For more information, see the following topics:

           

           
          *  WebACL : Contains ``DefaultAction`` , ``MetricName`` , ``Name`` , an array of ``Rule`` objects, and ``WebACLId``   
           
          * ``DefaultAction`` (Data type is  WafAction ): Contains ``Type``   
           
          * ``Rules`` : Contains an array of ``ActivatedRule`` objects, which contain ``Action`` , ``Priority`` , and ``RuleId``   
           
          * ``Action`` : Contains ``Type``   
           

          
          

          - **WebACLId** *(string) --* 

            A unique identifier for a ``WebACL`` . You use ``WebACLId`` to get information about a ``WebACL`` (see  GetWebACL ), update a ``WebACL`` (see  UpdateWebACL ), and delete a ``WebACL`` from AWS WAF (see  DeleteWebACL ).

             

             ``WebACLId`` is returned by  CreateWebACL and by  ListWebACLs .

            
          

          - **Name** *(string) --* 

            A friendly name or description of the ``WebACL`` . You can't change the name of a ``WebACL`` after you create it.

            
          

          - **MetricName** *(string) --* 

            A friendly name or description for the metrics for this ``WebACL`` . The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace. You can't change ``MetricName`` after you create the ``WebACL`` .

            
          

          - **DefaultAction** *(dict) --* 

            The action to perform if none of the ``Rules`` contained in the ``WebACL`` match. The action is specified by the  WafAction object.

            
            

            - **Type** *(string) --* 

              Specifies how you want AWS WAF to respond to requests that match the settings in a ``Rule`` . Valid settings include the following:

               

               
              * ``ALLOW`` : AWS WAF allows requests 
               
              * ``BLOCK`` : AWS WAF blocks requests 
               
              * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for a ``WebACL`` . 
               

              
        
          

          - **Rules** *(list) --* 

            An array that contains the action for each ``Rule`` in a ``WebACL`` , the priority of the ``Rule`` , and the ID of the ``Rule`` .

            
            

            - *(dict) --* 

              The ``ActivatedRule`` object in an  UpdateWebACL request specifies a ``Rule`` that you want to insert or delete, the priority of the ``Rule`` in the ``WebACL`` , and the action that you want AWS WAF to take when a web request matches the ``Rule`` (``ALLOW`` , ``BLOCK`` , or ``COUNT`` ).

               

              To specify whether to insert or delete a ``Rule`` , use the ``Action`` parameter in the  WebACLUpdate data type.

              
              

              - **Priority** *(integer) --* 

                Specifies the order in which the ``Rules`` in a ``WebACL`` are evaluated. Rules with a lower value for ``Priority`` are evaluated before ``Rules`` with a higher value. The value must be a unique integer. If you add multiple ``Rules`` to a ``WebACL`` , the values don't need to be consecutive.

                
              

              - **RuleId** *(string) --* 

                The ``RuleId`` for a ``Rule`` . You use ``RuleId`` to get more information about a ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule`` from AWS WAF (see  DeleteRule ).

                 

                 ``RuleId`` is returned by  CreateRule and by  ListRules .

                
              

              - **Action** *(dict) --* 

                Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the ``Rule`` . Valid values for ``Action`` include the following:

                 

                 
                * ``ALLOW`` : CloudFront responds with the requested object. 
                 
                * ``BLOCK`` : CloudFront responds with an HTTP 403 (Forbidden) status code. 
                 
                * ``COUNT`` : AWS WAF increments a counter of requests that match the conditions in the rule and then continues to inspect the web request based on the remaining rules in the web ACL.  
                 

                 

                The ``Action`` data type within ``ActivatedRule`` is used only when submitting an ``UpdateWebACL`` request. ``ActivatedRule|Action`` is not applicable and therefore not available for ``UpdateRuleGroup`` .

                
                

                - **Type** *(string) --* 

                  Specifies how you want AWS WAF to respond to requests that match the settings in a ``Rule`` . Valid settings include the following:

                   

                   
                  * ``ALLOW`` : AWS WAF allows requests 
                   
                  * ``BLOCK`` : AWS WAF blocks requests 
                   
                  * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for a ``WebACL`` . 
                   

                  
            
              

              - **OverrideAction** *(dict) --* 

                Use the ``OverrideAction`` to test your ``RuleGroup`` .

                 

                Any rule in a ``RuleGroup`` can potentially block a request. If you set the ``OverrideAction`` to ``None`` , the ``RuleGroup`` will block a request if any individual rule in the ``RuleGroup`` matches the request and is configured to block that request. However if you first want to test the ``RuleGroup`` , set the ``OverrideAction`` to ``Count`` . The ``RuleGroup`` will then override any block action specified by individual rules contained within the group. Instead of blocking matching requests, those requests will be counted. You can view a record of counted requests using  GetSampledRequests . 

                 

                The ``OverrideAction`` data type within ``ActivatedRule`` is used only when submitting an ``UpdateRuleGroup`` request. ``ActivatedRule|OverrideAction`` is not applicable and therefore not available for ``UpdateWebACL`` .

                
                

                - **Type** *(string) --* 

                   ``COUNT`` overrides the action specified by the individual rule within a ``RuleGroup`` . If set to ``NONE`` , the rule's action will take place.

                  
            
              

              - **Type** *(string) --* 

                The rule type, either ``REGULAR`` , as defined by  Rule , ``RATE_BASED`` , as defined by  RateBasedRule , or ``GROUP`` , as defined by  RuleGroup . The default is REGULAR. Although this field is optional, be aware that if you try to add a RATE_BASED rule to a web ACL without setting the type, the  UpdateWebACL request will fail because the request tries to add a REGULAR rule with the specified ID, which does not exist. 

                
          
        
      
    

    **Examples** 

    The following example returns the details of a web ACL with the ID createwebacl-1472061481310.
    ::

      response = client.get_web_acl(
          WebACLId='createwebacl-1472061481310',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'WebACL': {
              'DefaultAction': {
                  'Type': 'ALLOW',
              },
              'MetricName': 'CreateExample',
              'Name': 'CreateExample',
              'Rules': [
                  {
                      'Action': {
                          'Type': 'ALLOW',
                      },
                      'Priority': 1,
                      'RuleId': 'WAFRule-1-Example',
                  },
              ],
              'WebACLId': 'createwebacl-1472061481310',
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: get_web_acl_for_resource(**kwargs)

    

    Returns the web ACL for the specified resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/GetWebACLForResource>`_    


    **Request Syntax** 
    ::

      response = client.get_web_acl_for_resource(
          ResourceArn='string'
      )
    :type ResourceArn: string
    :param ResourceArn: **[REQUIRED]** 

      The ARN (Amazon Resource Name) of the resource for which to get the web ACL.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'WebACLSummary': {
                'WebACLId': 'string',
                'Name': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **WebACLSummary** *(dict) --* 

          Information about the web ACL that you specified in the ``GetWebACLForResource`` request. If there is no associated resource, a null WebACLSummary is returned.

          
          

          - **WebACLId** *(string) --* 

            A unique identifier for a ``WebACL`` . You use ``WebACLId`` to get information about a ``WebACL`` (see  GetWebACL ), update a ``WebACL`` (see  UpdateWebACL ), and delete a ``WebACL`` from AWS WAF (see  DeleteWebACL ).

             

             ``WebACLId`` is returned by  CreateWebACL and by  ListWebACLs .

            
          

          - **Name** *(string) --* 

            A friendly name or description of the  WebACL . You can't change the name of a ``WebACL`` after you create it.

            
      
    

  .. py:method:: get_xss_match_set(**kwargs)

    

    Returns the  XssMatchSet that is specified by ``XssMatchSetId`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/GetXssMatchSet>`_    


    **Request Syntax** 
    ::

      response = client.get_xss_match_set(
          XssMatchSetId='string'
      )
    :type XssMatchSetId: string
    :param XssMatchSetId: **[REQUIRED]** 

      The ``XssMatchSetId`` of the  XssMatchSet that you want to get. ``XssMatchSetId`` is returned by  CreateXssMatchSet and by  ListXssMatchSets .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'XssMatchSet': {
                'XssMatchSetId': 'string',
                'Name': 'string',
                'XssMatchTuples': [
                    {
                        'FieldToMatch': {
                            'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
                            'Data': 'string'
                        },
                        'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 

        The response to a  GetXssMatchSet request.

        
        

        - **XssMatchSet** *(dict) --* 

          Information about the  XssMatchSet that you specified in the ``GetXssMatchSet`` request. For more information, see the following topics:

           

           
          *  XssMatchSet : Contains ``Name`` , ``XssMatchSetId`` , and an array of ``XssMatchTuple`` objects 
           
          *  XssMatchTuple : Each ``XssMatchTuple`` object contains ``FieldToMatch`` and ``TextTransformation``   
           
          *  FieldToMatch : Contains ``Data`` and ``Type``   
           

          
          

          - **XssMatchSetId** *(string) --* 

            A unique identifier for an ``XssMatchSet`` . You use ``XssMatchSetId`` to get information about an ``XssMatchSet`` (see  GetXssMatchSet ), update an ``XssMatchSet`` (see  UpdateXssMatchSet ), insert an ``XssMatchSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete an ``XssMatchSet`` from AWS WAF (see  DeleteXssMatchSet ).

             

             ``XssMatchSetId`` is returned by  CreateXssMatchSet and by  ListXssMatchSets .

            
          

          - **Name** *(string) --* 

            The name, if any, of the ``XssMatchSet`` .

            
          

          - **XssMatchTuples** *(list) --* 

            Specifies the parts of web requests that you want to inspect for cross-site scripting attacks.

            
            

            - *(dict) --* 

              Specifies the part of a web request that you want AWS WAF to inspect for cross-site scripting attacks and, if you want AWS WAF to inspect a header, the name of the header.

              
              

              - **FieldToMatch** *(dict) --* 

                Specifies where in a web request to look for cross-site scripting attacks.

                
                

                - **Type** *(string) --* 

                  The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

                   

                   
                  * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the header in ``Data`` . 
                   
                  * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` . 
                   
                  * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a ``?`` character, if any. 
                   
                  * ``URI`` : The part of a web request that identifies a resource, for example, ``/images/daily-ad.jpg`` . 
                   
                  * ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .  
                   

                  
                

                - **Data** *(string) --* 

                  When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . If the value of ``Type`` is any other value, omit ``Data`` .

                   

                  The name of the header is not case sensitive.

                  
            
              

              - **TextTransformation** *(string) --* 

                Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

                 

                 **CMD_LINE**  

                 

                When you're concerned that attackers are injecting an operating system commandline command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

                 

                 
                * Delete the following characters: \ " ' ^ 
                 
                * Delete spaces before the following characters: / ( 
                 
                * Replace the following characters with a space: , ; 
                 
                * Replace multiple spaces with one space 
                 
                * Convert uppercase letters (A-Z) to lowercase (a-z) 
                 

                 

                 **COMPRESS_WHITE_SPACE**  

                 

                Use this option to replace the following characters with a space character (decimal 32):

                 

                 
                * \f, formfeed, decimal 12 
                 
                * \t, tab, decimal 9 
                 
                * \n, newline, decimal 10 
                 
                * \r, carriage return, decimal 13 
                 
                * \v, vertical tab, decimal 11 
                 
                * non-breaking space, decimal 160 
                 

                 

                 ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

                 

                 **HTML_ENTITY_DECODE**  

                 

                Use this option to replace HTML-encoded characters with unencoded characters. ``HTML_ENTITY_DECODE`` performs the following operations:

                 

                 
                * Replaces ``(ampersand)quot;`` with ``"``   
                 
                * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160 
                 
                * Replaces ``(ampersand)lt;`` with a "less than" symbol 
                 
                * Replaces ``(ampersand)gt;`` with ``>``   
                 
                * Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` , with the corresponding characters 
                 
                * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with the corresponding characters 
                 

                 

                 **LOWERCASE**  

                 

                Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

                 

                 **URL_DECODE**  

                 

                Use this option to decode a URL-encoded value.

                 

                 **NONE**  

                 

                Specify ``NONE`` if you don't want to perform any text transformations.

                
          
        
      
    

    **Examples** 

    The following example returns the details of an XSS match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    ::

      response = client.get_xss_match_set(
          XssMatchSetId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'XssMatchSet': {
              'Name': 'MySampleXssMatchSet',
              'XssMatchSetId': 'example1ds3t-46da-4fdb-b8d5-abc321j569j5',
              'XssMatchTuples': [
                  {
                      'FieldToMatch': {
                          'Type': 'QUERY_STRING',
                      },
                      'TextTransformation': 'URL_DECODE',
                  },
              ],
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_activated_rules_in_rule_group(**kwargs)

    

    Returns an array of  ActivatedRule objects.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/ListActivatedRulesInRuleGroup>`_    


    **Request Syntax** 
    ::

      response = client.list_activated_rules_in_rule_group(
          RuleGroupId='string',
          NextMarker='string',
          Limit=123
      )
    :type RuleGroupId: string
    :param RuleGroupId: 

      The ``RuleGroupId`` of the  RuleGroup for which you want to get a list of  ActivatedRule objects.

      

    
    :type NextMarker: string
    :param NextMarker: 

      If you specify a value for ``Limit`` and you have more ``ActivatedRules`` than the value of ``Limit`` , AWS WAF returns a ``NextMarker`` value in the response that allows you to list another group of ``ActivatedRules`` . For the second and subsequent ``ListActivatedRulesInRuleGroup`` requests, specify the value of ``NextMarker`` from the previous response to get information about another batch of ``ActivatedRules`` .

      

    
    :type Limit: integer
    :param Limit: 

      Specifies the number of ``ActivatedRules`` that you want AWS WAF to return for this request. If you have more ``ActivatedRules`` than the number that you specify for ``Limit`` , the response includes a ``NextMarker`` value that you can use to get another batch of ``ActivatedRules`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextMarker': 'string',
            'ActivatedRules': [
                {
                    'Priority': 123,
                    'RuleId': 'string',
                    'Action': {
                        'Type': 'BLOCK'|'ALLOW'|'COUNT'
                    },
                    'OverrideAction': {
                        'Type': 'NONE'|'COUNT'
                    },
                    'Type': 'REGULAR'|'RATE_BASED'|'GROUP'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NextMarker** *(string) --* 

          If you have more ``ActivatedRules`` than the number that you specified for ``Limit`` in the request, the response includes a ``NextMarker`` value. To list more ``ActivatedRules`` , submit another ``ListActivatedRulesInRuleGroup`` request, and specify the ``NextMarker`` value from the response in the ``NextMarker`` value in the next request.

          
        

        - **ActivatedRules** *(list) --* 

          An array of ``ActivatedRules`` objects.

          
          

          - *(dict) --* 

            The ``ActivatedRule`` object in an  UpdateWebACL request specifies a ``Rule`` that you want to insert or delete, the priority of the ``Rule`` in the ``WebACL`` , and the action that you want AWS WAF to take when a web request matches the ``Rule`` (``ALLOW`` , ``BLOCK`` , or ``COUNT`` ).

             

            To specify whether to insert or delete a ``Rule`` , use the ``Action`` parameter in the  WebACLUpdate data type.

            
            

            - **Priority** *(integer) --* 

              Specifies the order in which the ``Rules`` in a ``WebACL`` are evaluated. Rules with a lower value for ``Priority`` are evaluated before ``Rules`` with a higher value. The value must be a unique integer. If you add multiple ``Rules`` to a ``WebACL`` , the values don't need to be consecutive.

              
            

            - **RuleId** *(string) --* 

              The ``RuleId`` for a ``Rule`` . You use ``RuleId`` to get more information about a ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule`` from AWS WAF (see  DeleteRule ).

               

               ``RuleId`` is returned by  CreateRule and by  ListRules .

              
            

            - **Action** *(dict) --* 

              Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the ``Rule`` . Valid values for ``Action`` include the following:

               

               
              * ``ALLOW`` : CloudFront responds with the requested object. 
               
              * ``BLOCK`` : CloudFront responds with an HTTP 403 (Forbidden) status code. 
               
              * ``COUNT`` : AWS WAF increments a counter of requests that match the conditions in the rule and then continues to inspect the web request based on the remaining rules in the web ACL.  
               

               

              The ``Action`` data type within ``ActivatedRule`` is used only when submitting an ``UpdateWebACL`` request. ``ActivatedRule|Action`` is not applicable and therefore not available for ``UpdateRuleGroup`` .

              
              

              - **Type** *(string) --* 

                Specifies how you want AWS WAF to respond to requests that match the settings in a ``Rule`` . Valid settings include the following:

                 

                 
                * ``ALLOW`` : AWS WAF allows requests 
                 
                * ``BLOCK`` : AWS WAF blocks requests 
                 
                * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for a ``WebACL`` . 
                 

                
          
            

            - **OverrideAction** *(dict) --* 

              Use the ``OverrideAction`` to test your ``RuleGroup`` .

               

              Any rule in a ``RuleGroup`` can potentially block a request. If you set the ``OverrideAction`` to ``None`` , the ``RuleGroup`` will block a request if any individual rule in the ``RuleGroup`` matches the request and is configured to block that request. However if you first want to test the ``RuleGroup`` , set the ``OverrideAction`` to ``Count`` . The ``RuleGroup`` will then override any block action specified by individual rules contained within the group. Instead of blocking matching requests, those requests will be counted. You can view a record of counted requests using  GetSampledRequests . 

               

              The ``OverrideAction`` data type within ``ActivatedRule`` is used only when submitting an ``UpdateRuleGroup`` request. ``ActivatedRule|OverrideAction`` is not applicable and therefore not available for ``UpdateWebACL`` .

              
              

              - **Type** *(string) --* 

                 ``COUNT`` overrides the action specified by the individual rule within a ``RuleGroup`` . If set to ``NONE`` , the rule's action will take place.

                
          
            

            - **Type** *(string) --* 

              The rule type, either ``REGULAR`` , as defined by  Rule , ``RATE_BASED`` , as defined by  RateBasedRule , or ``GROUP`` , as defined by  RuleGroup . The default is REGULAR. Although this field is optional, be aware that if you try to add a RATE_BASED rule to a web ACL without setting the type, the  UpdateWebACL request will fail because the request tries to add a REGULAR rule with the specified ID, which does not exist. 

              
        
      
    

  .. py:method:: list_byte_match_sets(**kwargs)

    

    Returns an array of  ByteMatchSetSummary objects.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/ListByteMatchSets>`_    


    **Request Syntax** 
    ::

      response = client.list_byte_match_sets(
          NextMarker='string',
          Limit=123
      )
    :type NextMarker: string
    :param NextMarker: 

      If you specify a value for ``Limit`` and you have more ``ByteMatchSets`` than the value of ``Limit`` , AWS WAF returns a ``NextMarker`` value in the response that allows you to list another group of ``ByteMatchSets`` . For the second and subsequent ``ListByteMatchSets`` requests, specify the value of ``NextMarker`` from the previous response to get information about another batch of ``ByteMatchSets`` .

      

    
    :type Limit: integer
    :param Limit: 

      Specifies the number of ``ByteMatchSet`` objects that you want AWS WAF to return for this request. If you have more ``ByteMatchSets`` objects than the number you specify for ``Limit`` , the response includes a ``NextMarker`` value that you can use to get another batch of ``ByteMatchSet`` objects.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextMarker': 'string',
            'ByteMatchSets': [
                {
                    'ByteMatchSetId': 'string',
                    'Name': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NextMarker** *(string) --* 

          If you have more ``ByteMatchSet`` objects than the number that you specified for ``Limit`` in the request, the response includes a ``NextMarker`` value. To list more ``ByteMatchSet`` objects, submit another ``ListByteMatchSets`` request, and specify the ``NextMarker`` value from the response in the ``NextMarker`` value in the next request.

          
        

        - **ByteMatchSets** *(list) --* 

          An array of  ByteMatchSetSummary objects.

          
          

          - *(dict) --* 

            Returned by  ListByteMatchSets . Each ``ByteMatchSetSummary`` object includes the ``Name`` and ``ByteMatchSetId`` for one  ByteMatchSet .

            
            

            - **ByteMatchSetId** *(string) --* 

              The ``ByteMatchSetId`` for a ``ByteMatchSet`` . You use ``ByteMatchSetId`` to get information about a ``ByteMatchSet`` , update a ``ByteMatchSet`` , remove a ``ByteMatchSet`` from a ``Rule`` , and delete a ``ByteMatchSet`` from AWS WAF.

               

               ``ByteMatchSetId`` is returned by  CreateByteMatchSet and by  ListByteMatchSets .

              
            

            - **Name** *(string) --* 

              A friendly name or description of the  ByteMatchSet . You can't change ``Name`` after you create a ``ByteMatchSet`` .

              
        
      
    

  .. py:method:: list_geo_match_sets(**kwargs)

    

    Returns an array of  GeoMatchSetSummary objects in the response.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/ListGeoMatchSets>`_    


    **Request Syntax** 
    ::

      response = client.list_geo_match_sets(
          NextMarker='string',
          Limit=123
      )
    :type NextMarker: string
    :param NextMarker: 

      If you specify a value for ``Limit`` and you have more ``GeoMatchSet`` s than the value of ``Limit`` , AWS WAF returns a ``NextMarker`` value in the response that allows you to list another group of ``GeoMatchSet`` objects. For the second and subsequent ``ListGeoMatchSets`` requests, specify the value of ``NextMarker`` from the previous response to get information about another batch of ``GeoMatchSet`` objects.

      

    
    :type Limit: integer
    :param Limit: 

      Specifies the number of ``GeoMatchSet`` objects that you want AWS WAF to return for this request. If you have more ``GeoMatchSet`` objects than the number you specify for ``Limit`` , the response includes a ``NextMarker`` value that you can use to get another batch of ``GeoMatchSet`` objects.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextMarker': 'string',
            'GeoMatchSets': [
                {
                    'GeoMatchSetId': 'string',
                    'Name': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NextMarker** *(string) --* 

          If you have more ``GeoMatchSet`` objects than the number that you specified for ``Limit`` in the request, the response includes a ``NextMarker`` value. To list more ``GeoMatchSet`` objects, submit another ``ListGeoMatchSets`` request, and specify the ``NextMarker`` value from the response in the ``NextMarker`` value in the next request.

          
        

        - **GeoMatchSets** *(list) --* 

          An array of  GeoMatchSetSummary objects.

          
          

          - *(dict) --* 

            Contains the identifier and the name of the ``GeoMatchSet`` .

            
            

            - **GeoMatchSetId** *(string) --* 

              The ``GeoMatchSetId`` for an  GeoMatchSet . You can use ``GeoMatchSetId`` in a  GetGeoMatchSet request to get detailed information about an  GeoMatchSet .

              
            

            - **Name** *(string) --* 

              A friendly name or description of the  GeoMatchSet . You can't change the name of an ``GeoMatchSet`` after you create it.

              
        
      
    

  .. py:method:: list_ip_sets(**kwargs)

    

    Returns an array of  IPSetSummary objects in the response.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/ListIPSets>`_    


    **Request Syntax** 
    ::

      response = client.list_ip_sets(
          NextMarker='string',
          Limit=123
      )
    :type NextMarker: string
    :param NextMarker: 

      If you specify a value for ``Limit`` and you have more ``IPSets`` than the value of ``Limit`` , AWS WAF returns a ``NextMarker`` value in the response that allows you to list another group of ``IPSets`` . For the second and subsequent ``ListIPSets`` requests, specify the value of ``NextMarker`` from the previous response to get information about another batch of ``IPSets`` .

      

    
    :type Limit: integer
    :param Limit: 

      Specifies the number of ``IPSet`` objects that you want AWS WAF to return for this request. If you have more ``IPSet`` objects than the number you specify for ``Limit`` , the response includes a ``NextMarker`` value that you can use to get another batch of ``IPSet`` objects.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextMarker': 'string',
            'IPSets': [
                {
                    'IPSetId': 'string',
                    'Name': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NextMarker** *(string) --* 

          If you have more ``IPSet`` objects than the number that you specified for ``Limit`` in the request, the response includes a ``NextMarker`` value. To list more ``IPSet`` objects, submit another ``ListIPSets`` request, and specify the ``NextMarker`` value from the response in the ``NextMarker`` value in the next request.

          
        

        - **IPSets** *(list) --* 

          An array of  IPSetSummary objects.

          
          

          - *(dict) --* 

            Contains the identifier and the name of the ``IPSet`` .

            
            

            - **IPSetId** *(string) --* 

              The ``IPSetId`` for an  IPSet . You can use ``IPSetId`` in a  GetIPSet request to get detailed information about an  IPSet .

              
            

            - **Name** *(string) --* 

              A friendly name or description of the  IPSet . You can't change the name of an ``IPSet`` after you create it.

              
        
      
    

    **Examples** 

    The following example returns an array of up to 100 IP match sets.
    ::

      response = client.list_ip_sets(
          Limit=100,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'IPSets': [
              {
                  'IPSetId': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
                  'Name': 'MyIPSetFriendlyName',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_rate_based_rules(**kwargs)

    

    Returns an array of  RuleSummary objects.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/ListRateBasedRules>`_    


    **Request Syntax** 
    ::

      response = client.list_rate_based_rules(
          NextMarker='string',
          Limit=123
      )
    :type NextMarker: string
    :param NextMarker: 

      If you specify a value for ``Limit`` and you have more ``Rules`` than the value of ``Limit`` , AWS WAF returns a ``NextMarker`` value in the response that allows you to list another group of ``Rules`` . For the second and subsequent ``ListRateBasedRules`` requests, specify the value of ``NextMarker`` from the previous response to get information about another batch of ``Rules`` .

      

    
    :type Limit: integer
    :param Limit: 

      Specifies the number of ``Rules`` that you want AWS WAF to return for this request. If you have more ``Rules`` than the number that you specify for ``Limit`` , the response includes a ``NextMarker`` value that you can use to get another batch of ``Rules`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextMarker': 'string',
            'Rules': [
                {
                    'RuleId': 'string',
                    'Name': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NextMarker** *(string) --* 

          If you have more ``Rules`` than the number that you specified for ``Limit`` in the request, the response includes a ``NextMarker`` value. To list more ``Rules`` , submit another ``ListRateBasedRules`` request, and specify the ``NextMarker`` value from the response in the ``NextMarker`` value in the next request.

          
        

        - **Rules** *(list) --* 

          An array of  RuleSummary objects.

          
          

          - *(dict) --* 

            Contains the identifier and the friendly name or description of the ``Rule`` .

            
            

            - **RuleId** *(string) --* 

              A unique identifier for a ``Rule`` . You use ``RuleId`` to get more information about a ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a ``WebACL`` or delete one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule`` from AWS WAF (see  DeleteRule ).

               

               ``RuleId`` is returned by  CreateRule and by  ListRules .

              
            

            - **Name** *(string) --* 

              A friendly name or description of the  Rule . You can't change the name of a ``Rule`` after you create it.

              
        
      
    

  .. py:method:: list_regex_match_sets(**kwargs)

    

    Returns an array of  RegexMatchSetSummary objects.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/ListRegexMatchSets>`_    


    **Request Syntax** 
    ::

      response = client.list_regex_match_sets(
          NextMarker='string',
          Limit=123
      )
    :type NextMarker: string
    :param NextMarker: 

      If you specify a value for ``Limit`` and you have more ``RegexMatchSet`` objects than the value of ``Limit`` , AWS WAF returns a ``NextMarker`` value in the response that allows you to list another group of ``ByteMatchSets`` . For the second and subsequent ``ListRegexMatchSets`` requests, specify the value of ``NextMarker`` from the previous response to get information about another batch of ``RegexMatchSet`` objects.

      

    
    :type Limit: integer
    :param Limit: 

      Specifies the number of ``RegexMatchSet`` objects that you want AWS WAF to return for this request. If you have more ``RegexMatchSet`` objects than the number you specify for ``Limit`` , the response includes a ``NextMarker`` value that you can use to get another batch of ``RegexMatchSet`` objects.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextMarker': 'string',
            'RegexMatchSets': [
                {
                    'RegexMatchSetId': 'string',
                    'Name': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NextMarker** *(string) --* 

          If you have more ``RegexMatchSet`` objects than the number that you specified for ``Limit`` in the request, the response includes a ``NextMarker`` value. To list more ``RegexMatchSet`` objects, submit another ``ListRegexMatchSets`` request, and specify the ``NextMarker`` value from the response in the ``NextMarker`` value in the next request.

          
        

        - **RegexMatchSets** *(list) --* 

          An array of  RegexMatchSetSummary objects.

          
          

          - *(dict) --* 

            Returned by  ListRegexMatchSets . Each ``RegexMatchSetSummary`` object includes the ``Name`` and ``RegexMatchSetId`` for one  RegexMatchSet .

            
            

            - **RegexMatchSetId** *(string) --* 

              The ``RegexMatchSetId`` for a ``RegexMatchSet`` . You use ``RegexMatchSetId`` to get information about a ``RegexMatchSet`` , update a ``RegexMatchSet`` , remove a ``RegexMatchSet`` from a ``Rule`` , and delete a ``RegexMatchSet`` from AWS WAF.

               

               ``RegexMatchSetId`` is returned by  CreateRegexMatchSet and by  ListRegexMatchSets .

              
            

            - **Name** *(string) --* 

              A friendly name or description of the  RegexMatchSet . You can't change ``Name`` after you create a ``RegexMatchSet`` .

              
        
      
    

  .. py:method:: list_regex_pattern_sets(**kwargs)

    

    Returns an array of  RegexPatternSetSummary objects.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/ListRegexPatternSets>`_    


    **Request Syntax** 
    ::

      response = client.list_regex_pattern_sets(
          NextMarker='string',
          Limit=123
      )
    :type NextMarker: string
    :param NextMarker: 

      If you specify a value for ``Limit`` and you have more ``RegexPatternSet`` objects than the value of ``Limit`` , AWS WAF returns a ``NextMarker`` value in the response that allows you to list another group of ``RegexPatternSet`` objects. For the second and subsequent ``ListRegexPatternSets`` requests, specify the value of ``NextMarker`` from the previous response to get information about another batch of ``RegexPatternSet`` objects.

      

    
    :type Limit: integer
    :param Limit: 

      Specifies the number of ``RegexPatternSet`` objects that you want AWS WAF to return for this request. If you have more ``RegexPatternSet`` objects than the number you specify for ``Limit`` , the response includes a ``NextMarker`` value that you can use to get another batch of ``RegexPatternSet`` objects.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextMarker': 'string',
            'RegexPatternSets': [
                {
                    'RegexPatternSetId': 'string',
                    'Name': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NextMarker** *(string) --* 

          If you have more ``RegexPatternSet`` objects than the number that you specified for ``Limit`` in the request, the response includes a ``NextMarker`` value. To list more ``RegexPatternSet`` objects, submit another ``ListRegexPatternSets`` request, and specify the ``NextMarker`` value from the response in the ``NextMarker`` value in the next request.

          
        

        - **RegexPatternSets** *(list) --* 

          An array of  RegexPatternSetSummary objects.

          
          

          - *(dict) --* 

            Returned by  ListRegexPatternSets . Each ``RegexPatternSetSummary`` object includes the ``Name`` and ``RegexPatternSetId`` for one  RegexPatternSet .

            
            

            - **RegexPatternSetId** *(string) --* 

              The ``RegexPatternSetId`` for a ``RegexPatternSet`` . You use ``RegexPatternSetId`` to get information about a ``RegexPatternSet`` , update a ``RegexPatternSet`` , remove a ``RegexPatternSet`` from a ``RegexMatchSet`` , and delete a ``RegexPatternSet`` from AWS WAF.

               

               ``RegexPatternSetId`` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .

              
            

            - **Name** *(string) --* 

              A friendly name or description of the  RegexPatternSet . You can't change ``Name`` after you create a ``RegexPatternSet`` .

              
        
      
    

  .. py:method:: list_resources_for_web_acl(**kwargs)

    

    Returns an array of resources associated with the specified web ACL.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/ListResourcesForWebACL>`_    


    **Request Syntax** 
    ::

      response = client.list_resources_for_web_acl(
          WebACLId='string'
      )
    :type WebACLId: string
    :param WebACLId: **[REQUIRED]** 

      The unique identifier (ID) of the web ACL for which to list the associated resources.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResourceArns': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ResourceArns** *(list) --* 

          An array of ARNs (Amazon Resource Names) of the resources associated with the specified web ACL. An array with zero elements is returned if there are no resources associated with the web ACL.

          
          

          - *(string) --* 
      
    

  .. py:method:: list_rule_groups(**kwargs)

    

    Returns an array of  RuleGroup objects.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/ListRuleGroups>`_    


    **Request Syntax** 
    ::

      response = client.list_rule_groups(
          NextMarker='string',
          Limit=123
      )
    :type NextMarker: string
    :param NextMarker: 

      If you specify a value for ``Limit`` and you have more ``RuleGroups`` than the value of ``Limit`` , AWS WAF returns a ``NextMarker`` value in the response that allows you to list another group of ``RuleGroups`` . For the second and subsequent ``ListRuleGroups`` requests, specify the value of ``NextMarker`` from the previous response to get information about another batch of ``RuleGroups`` .

      

    
    :type Limit: integer
    :param Limit: 

      Specifies the number of ``RuleGroups`` that you want AWS WAF to return for this request. If you have more ``RuleGroups`` than the number that you specify for ``Limit`` , the response includes a ``NextMarker`` value that you can use to get another batch of ``RuleGroups`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextMarker': 'string',
            'RuleGroups': [
                {
                    'RuleGroupId': 'string',
                    'Name': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NextMarker** *(string) --* 

          If you have more ``RuleGroups`` than the number that you specified for ``Limit`` in the request, the response includes a ``NextMarker`` value. To list more ``RuleGroups`` , submit another ``ListRuleGroups`` request, and specify the ``NextMarker`` value from the response in the ``NextMarker`` value in the next request.

          
        

        - **RuleGroups** *(list) --* 

          An array of  RuleGroup objects.

          
          

          - *(dict) --* 

            Contains the identifier and the friendly name or description of the ``RuleGroup`` .

            
            

            - **RuleGroupId** *(string) --* 

              A unique identifier for a ``RuleGroup`` . You use ``RuleGroupId`` to get more information about a ``RuleGroup`` (see  GetRuleGroup ), update a ``RuleGroup`` (see  UpdateRuleGroup ), insert a ``RuleGroup`` into a ``WebACL`` or delete one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``RuleGroup`` from AWS WAF (see  DeleteRuleGroup ).

               

               ``RuleGroupId`` is returned by  CreateRuleGroup and by  ListRuleGroups .

              
            

            - **Name** *(string) --* 

              A friendly name or description of the  RuleGroup . You can't change the name of a ``RuleGroup`` after you create it.

              
        
      
    

  .. py:method:: list_rules(**kwargs)

    

    Returns an array of  RuleSummary objects.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/ListRules>`_    


    **Request Syntax** 
    ::

      response = client.list_rules(
          NextMarker='string',
          Limit=123
      )
    :type NextMarker: string
    :param NextMarker: 

      If you specify a value for ``Limit`` and you have more ``Rules`` than the value of ``Limit`` , AWS WAF returns a ``NextMarker`` value in the response that allows you to list another group of ``Rules`` . For the second and subsequent ``ListRules`` requests, specify the value of ``NextMarker`` from the previous response to get information about another batch of ``Rules`` .

      

    
    :type Limit: integer
    :param Limit: 

      Specifies the number of ``Rules`` that you want AWS WAF to return for this request. If you have more ``Rules`` than the number that you specify for ``Limit`` , the response includes a ``NextMarker`` value that you can use to get another batch of ``Rules`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextMarker': 'string',
            'Rules': [
                {
                    'RuleId': 'string',
                    'Name': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NextMarker** *(string) --* 

          If you have more ``Rules`` than the number that you specified for ``Limit`` in the request, the response includes a ``NextMarker`` value. To list more ``Rules`` , submit another ``ListRules`` request, and specify the ``NextMarker`` value from the response in the ``NextMarker`` value in the next request.

          
        

        - **Rules** *(list) --* 

          An array of  RuleSummary objects.

          
          

          - *(dict) --* 

            Contains the identifier and the friendly name or description of the ``Rule`` .

            
            

            - **RuleId** *(string) --* 

              A unique identifier for a ``Rule`` . You use ``RuleId`` to get more information about a ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a ``WebACL`` or delete one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule`` from AWS WAF (see  DeleteRule ).

               

               ``RuleId`` is returned by  CreateRule and by  ListRules .

              
            

            - **Name** *(string) --* 

              A friendly name or description of the  Rule . You can't change the name of a ``Rule`` after you create it.

              
        
      
    

    **Examples** 

    The following example returns an array of up to 100 rules.
    ::

      response = client.list_rules(
          Limit=100,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Rules': [
              {
                  'Name': 'WAFByteHeaderRule',
                  'RuleId': 'WAFRule-1-Example',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_size_constraint_sets(**kwargs)

    

    Returns an array of  SizeConstraintSetSummary objects.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/ListSizeConstraintSets>`_    


    **Request Syntax** 
    ::

      response = client.list_size_constraint_sets(
          NextMarker='string',
          Limit=123
      )
    :type NextMarker: string
    :param NextMarker: 

      If you specify a value for ``Limit`` and you have more ``SizeConstraintSets`` than the value of ``Limit`` , AWS WAF returns a ``NextMarker`` value in the response that allows you to list another group of ``SizeConstraintSets`` . For the second and subsequent ``ListSizeConstraintSets`` requests, specify the value of ``NextMarker`` from the previous response to get information about another batch of ``SizeConstraintSets`` .

      

    
    :type Limit: integer
    :param Limit: 

      Specifies the number of ``SizeConstraintSet`` objects that you want AWS WAF to return for this request. If you have more ``SizeConstraintSets`` objects than the number you specify for ``Limit`` , the response includes a ``NextMarker`` value that you can use to get another batch of ``SizeConstraintSet`` objects.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextMarker': 'string',
            'SizeConstraintSets': [
                {
                    'SizeConstraintSetId': 'string',
                    'Name': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NextMarker** *(string) --* 

          If you have more ``SizeConstraintSet`` objects than the number that you specified for ``Limit`` in the request, the response includes a ``NextMarker`` value. To list more ``SizeConstraintSet`` objects, submit another ``ListSizeConstraintSets`` request, and specify the ``NextMarker`` value from the response in the ``NextMarker`` value in the next request.

          
        

        - **SizeConstraintSets** *(list) --* 

          An array of  SizeConstraintSetSummary objects.

          
          

          - *(dict) --* 

            The ``Id`` and ``Name`` of a ``SizeConstraintSet`` .

            
            

            - **SizeConstraintSetId** *(string) --* 

              A unique identifier for a ``SizeConstraintSet`` . You use ``SizeConstraintSetId`` to get information about a ``SizeConstraintSet`` (see  GetSizeConstraintSet ), update a ``SizeConstraintSet`` (see  UpdateSizeConstraintSet ), insert a ``SizeConstraintSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete a ``SizeConstraintSet`` from AWS WAF (see  DeleteSizeConstraintSet ).

               

               ``SizeConstraintSetId`` is returned by  CreateSizeConstraintSet and by  ListSizeConstraintSets .

              
            

            - **Name** *(string) --* 

              The name of the ``SizeConstraintSet`` , if any.

              
        
      
    

    **Examples** 

    The following example returns an array of up to 100 size contraint match sets.
    ::

      response = client.list_size_constraint_sets(
          Limit=100,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'SizeConstraintSets': [
              {
                  'Name': 'MySampleSizeConstraintSet',
                  'SizeConstraintSetId': 'example1ds3t-46da-4fdb-b8d5-abc321j569j5',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_sql_injection_match_sets(**kwargs)

    

    Returns an array of  SqlInjectionMatchSet objects.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/ListSqlInjectionMatchSets>`_    


    **Request Syntax** 
    ::

      response = client.list_sql_injection_match_sets(
          NextMarker='string',
          Limit=123
      )
    :type NextMarker: string
    :param NextMarker: 

      If you specify a value for ``Limit`` and you have more  SqlInjectionMatchSet objects than the value of ``Limit`` , AWS WAF returns a ``NextMarker`` value in the response that allows you to list another group of ``SqlInjectionMatchSets`` . For the second and subsequent ``ListSqlInjectionMatchSets`` requests, specify the value of ``NextMarker`` from the previous response to get information about another batch of ``SqlInjectionMatchSets`` .

      

    
    :type Limit: integer
    :param Limit: 

      Specifies the number of  SqlInjectionMatchSet objects that you want AWS WAF to return for this request. If you have more ``SqlInjectionMatchSet`` objects than the number you specify for ``Limit`` , the response includes a ``NextMarker`` value that you can use to get another batch of ``Rules`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextMarker': 'string',
            'SqlInjectionMatchSets': [
                {
                    'SqlInjectionMatchSetId': 'string',
                    'Name': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        The response to a  ListSqlInjectionMatchSets request.

        
        

        - **NextMarker** *(string) --* 

          If you have more  SqlInjectionMatchSet objects than the number that you specified for ``Limit`` in the request, the response includes a ``NextMarker`` value. To list more ``SqlInjectionMatchSet`` objects, submit another ``ListSqlInjectionMatchSets`` request, and specify the ``NextMarker`` value from the response in the ``NextMarker`` value in the next request.

          
        

        - **SqlInjectionMatchSets** *(list) --* 

          An array of  SqlInjectionMatchSetSummary objects.

          
          

          - *(dict) --* 

            The ``Id`` and ``Name`` of a ``SqlInjectionMatchSet`` .

            
            

            - **SqlInjectionMatchSetId** *(string) --* 

              A unique identifier for a ``SqlInjectionMatchSet`` . You use ``SqlInjectionMatchSetId`` to get information about a ``SqlInjectionMatchSet`` (see  GetSqlInjectionMatchSet ), update a ``SqlInjectionMatchSet`` (see  UpdateSqlInjectionMatchSet ), insert a ``SqlInjectionMatchSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete a ``SqlInjectionMatchSet`` from AWS WAF (see  DeleteSqlInjectionMatchSet ).

               

               ``SqlInjectionMatchSetId`` is returned by  CreateSqlInjectionMatchSet and by  ListSqlInjectionMatchSets .

              
            

            - **Name** *(string) --* 

              The name of the ``SqlInjectionMatchSet`` , if any, specified by ``Id`` .

              
        
      
    

    **Examples** 

    The following example returns an array of up to 100 SQL injection match sets.
    ::

      response = client.list_sql_injection_match_sets(
          Limit=100,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'SqlInjectionMatchSets': [
              {
                  'Name': 'MySQLInjectionMatchSet',
                  'SqlInjectionMatchSetId': 'example1ds3t-46da-4fdb-b8d5-abc321j569j5',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_subscribed_rule_groups(**kwargs)

    

    Returns an array of  RuleGroup objects that you are subscribed to.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/ListSubscribedRuleGroups>`_    


    **Request Syntax** 
    ::

      response = client.list_subscribed_rule_groups(
          NextMarker='string',
          Limit=123
      )
    :type NextMarker: string
    :param NextMarker: 

      If you specify a value for ``Limit`` and you have more ``ByteMatchSets`` subscribed rule groups than the value of ``Limit`` , AWS WAF returns a ``NextMarker`` value in the response that allows you to list another group of subscribed rule groups. For the second and subsequent ``ListSubscribedRuleGroupsRequest`` requests, specify the value of ``NextMarker`` from the previous response to get information about another batch of subscribed rule groups.

      

    
    :type Limit: integer
    :param Limit: 

      Specifies the number of subscribed rule groups that you want AWS WAF to return for this request. If you have more objects than the number you specify for ``Limit`` , the response includes a ``NextMarker`` value that you can use to get another batch of objects.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextMarker': 'string',
            'RuleGroups': [
                {
                    'RuleGroupId': 'string',
                    'Name': 'string',
                    'MetricName': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NextMarker** *(string) --* 

          If you have more objects than the number that you specified for ``Limit`` in the request, the response includes a ``NextMarker`` value. To list more objects, submit another ``ListSubscribedRuleGroups`` request, and specify the ``NextMarker`` value from the response in the ``NextMarker`` value in the next request.

          
        

        - **RuleGroups** *(list) --* 

          An array of  RuleGroup objects.

          
          

          - *(dict) --* 

            A summary of the rule groups you are subscribed to.

            
            

            - **RuleGroupId** *(string) --* 

              A unique identifier for a ``RuleGroup`` .

              
            

            - **Name** *(string) --* 

              A friendly name or description of the ``RuleGroup`` . You can't change the name of a ``RuleGroup`` after you create it.

              
            

            - **MetricName** *(string) --* 

              A friendly name or description for the metrics for this ``RuleGroup`` . The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can't contain whitespace. You can't change the name of the metric after you create the ``RuleGroup`` .

              
        
      
    

  .. py:method:: list_web_acls(**kwargs)

    

    Returns an array of  WebACLSummary objects in the response.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/ListWebACLs>`_    


    **Request Syntax** 
    ::

      response = client.list_web_acls(
          NextMarker='string',
          Limit=123
      )
    :type NextMarker: string
    :param NextMarker: 

      If you specify a value for ``Limit`` and you have more ``WebACL`` objects than the number that you specify for ``Limit`` , AWS WAF returns a ``NextMarker`` value in the response that allows you to list another group of ``WebACL`` objects. For the second and subsequent ``ListWebACLs`` requests, specify the value of ``NextMarker`` from the previous response to get information about another batch of ``WebACL`` objects.

      

    
    :type Limit: integer
    :param Limit: 

      Specifies the number of ``WebACL`` objects that you want AWS WAF to return for this request. If you have more ``WebACL`` objects than the number that you specify for ``Limit`` , the response includes a ``NextMarker`` value that you can use to get another batch of ``WebACL`` objects.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextMarker': 'string',
            'WebACLs': [
                {
                    'WebACLId': 'string',
                    'Name': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NextMarker** *(string) --* 

          If you have more ``WebACL`` objects than the number that you specified for ``Limit`` in the request, the response includes a ``NextMarker`` value. To list more ``WebACL`` objects, submit another ``ListWebACLs`` request, and specify the ``NextMarker`` value from the response in the ``NextMarker`` value in the next request.

          
        

        - **WebACLs** *(list) --* 

          An array of  WebACLSummary objects.

          
          

          - *(dict) --* 

            Contains the identifier and the name or description of the  WebACL .

            
            

            - **WebACLId** *(string) --* 

              A unique identifier for a ``WebACL`` . You use ``WebACLId`` to get information about a ``WebACL`` (see  GetWebACL ), update a ``WebACL`` (see  UpdateWebACL ), and delete a ``WebACL`` from AWS WAF (see  DeleteWebACL ).

               

               ``WebACLId`` is returned by  CreateWebACL and by  ListWebACLs .

              
            

            - **Name** *(string) --* 

              A friendly name or description of the  WebACL . You can't change the name of a ``WebACL`` after you create it.

              
        
      
    

    **Examples** 

    The following example returns an array of up to 100 web ACLs.
    ::

      response = client.list_web_acls(
          Limit=100,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'WebACLs': [
              {
                  'Name': 'WebACLexample',
                  'WebACLId': 'webacl-1472061481310',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_xss_match_sets(**kwargs)

    

    Returns an array of  XssMatchSet objects.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/ListXssMatchSets>`_    


    **Request Syntax** 
    ::

      response = client.list_xss_match_sets(
          NextMarker='string',
          Limit=123
      )
    :type NextMarker: string
    :param NextMarker: 

      If you specify a value for ``Limit`` and you have more  XssMatchSet objects than the value of ``Limit`` , AWS WAF returns a ``NextMarker`` value in the response that allows you to list another group of ``XssMatchSets`` . For the second and subsequent ``ListXssMatchSets`` requests, specify the value of ``NextMarker`` from the previous response to get information about another batch of ``XssMatchSets`` .

      

    
    :type Limit: integer
    :param Limit: 

      Specifies the number of  XssMatchSet objects that you want AWS WAF to return for this request. If you have more ``XssMatchSet`` objects than the number you specify for ``Limit`` , the response includes a ``NextMarker`` value that you can use to get another batch of ``Rules`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextMarker': 'string',
            'XssMatchSets': [
                {
                    'XssMatchSetId': 'string',
                    'Name': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 

        The response to a  ListXssMatchSets request.

        
        

        - **NextMarker** *(string) --* 

          If you have more  XssMatchSet objects than the number that you specified for ``Limit`` in the request, the response includes a ``NextMarker`` value. To list more ``XssMatchSet`` objects, submit another ``ListXssMatchSets`` request, and specify the ``NextMarker`` value from the response in the ``NextMarker`` value in the next request.

          
        

        - **XssMatchSets** *(list) --* 

          An array of  XssMatchSetSummary objects.

          
          

          - *(dict) --* 

            The ``Id`` and ``Name`` of an ``XssMatchSet`` .

            
            

            - **XssMatchSetId** *(string) --* 

              A unique identifier for an ``XssMatchSet`` . You use ``XssMatchSetId`` to get information about a ``XssMatchSet`` (see  GetXssMatchSet ), update an ``XssMatchSet`` (see  UpdateXssMatchSet ), insert an ``XssMatchSet`` into a ``Rule`` or delete one from a ``Rule`` (see  UpdateRule ), and delete an ``XssMatchSet`` from AWS WAF (see  DeleteXssMatchSet ).

               

               ``XssMatchSetId`` is returned by  CreateXssMatchSet and by  ListXssMatchSets .

              
            

            - **Name** *(string) --* 

              The name of the ``XssMatchSet`` , if any, specified by ``Id`` .

              
        
      
    

    **Examples** 

    The following example returns an array of up to 100 XSS match sets.
    ::

      response = client.list_xss_match_sets(
          Limit=100,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'XssMatchSets': [
              {
                  'Name': 'MySampleXssMatchSet',
                  'XssMatchSetId': 'example1ds3t-46da-4fdb-b8d5-abc321j569j5',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: update_byte_match_set(**kwargs)

    

    Inserts or deletes  ByteMatchTuple objects (filters) in a  ByteMatchSet . For each ``ByteMatchTuple`` object, you specify the following values: 

     

     
    * Whether to insert or delete the object from the array. If you want to change a ``ByteMatchSetUpdate`` object, you delete the existing object and add a new one. 
     
    * The part of a web request that you want AWS WAF to inspect, such as a query string or the value of the ``User-Agent`` header.  
     
    * The bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to look for. For more information, including how you specify the values for the AWS WAF API and the AWS CLI or SDKs, see ``TargetString`` in the  ByteMatchTuple data type.  
     
    * Where to look, such as at the beginning or the end of a query string. 
     
    * Whether to perform any conversions on the request, such as converting it to lowercase, before inspecting it for the specified string. 
     

     

    For example, you can add a ``ByteMatchSetUpdate`` object that matches web requests in which ``User-Agent`` headers contain the string ``BadBot`` . You can then configure AWS WAF to block those requests.

     

    To create and configure a ``ByteMatchSet`` , perform the following steps:

     

     
    * Create a ``ByteMatchSet.`` For more information, see  CreateByteMatchSet . 
     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of an ``UpdateByteMatchSet`` request. 
     
    * Submit an ``UpdateByteMatchSet`` request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the value that you want AWS WAF to watch for. 
     

     

    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the `AWS WAF Developer Guide <http://docs.aws.amazon.com/waf/latest/developerguide/>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/UpdateByteMatchSet>`_    


    **Request Syntax** 
    ::

      response = client.update_byte_match_set(
          ByteMatchSetId='string',
          ChangeToken='string',
          Updates=[
              {
                  'Action': 'INSERT'|'DELETE',
                  'ByteMatchTuple': {
                      'FieldToMatch': {
                          'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
                          'Data': 'string'
                      },
                      'TargetString': b'bytes',
                      'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE',
                      'PositionalConstraint': 'EXACTLY'|'STARTS_WITH'|'ENDS_WITH'|'CONTAINS'|'CONTAINS_WORD'
                  }
              },
          ]
      )
    :type ByteMatchSetId: string
    :param ByteMatchSetId: **[REQUIRED]** 

      The ``ByteMatchSetId`` of the  ByteMatchSet that you want to update. ``ByteMatchSetId`` is returned by  CreateByteMatchSet and by  ListByteMatchSets .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    :type Updates: list
    :param Updates: **[REQUIRED]** 

      An array of ``ByteMatchSetUpdate`` objects that you want to insert into or delete from a  ByteMatchSet . For more information, see the applicable data types:

       

       
      *  ByteMatchSetUpdate : Contains ``Action`` and ``ByteMatchTuple``   
       
      *  ByteMatchTuple : Contains ``FieldToMatch`` , ``PositionalConstraint`` , ``TargetString`` , and ``TextTransformation``   
       
      *  FieldToMatch : Contains ``Data`` and ``Type``   
       

      

    
      - *(dict) --* 

        In an  UpdateByteMatchSet request, ``ByteMatchSetUpdate`` specifies whether to insert or delete a  ByteMatchTuple and includes the settings for the ``ByteMatchTuple`` .

        

      
        - **Action** *(string) --* **[REQUIRED]** 

          Specifies whether to insert or delete a  ByteMatchTuple .

          

        
        - **ByteMatchTuple** *(dict) --* **[REQUIRED]** 

          Information about the part of a web request that you want AWS WAF to inspect and the value that you want AWS WAF to search for. If you specify ``DELETE`` for the value of ``Action`` , the ``ByteMatchTuple`` values must exactly match the values in the ``ByteMatchTuple`` that you want to delete from the ``ByteMatchSet`` .

          

        
          - **FieldToMatch** *(dict) --* **[REQUIRED]** 

            The part of a web request that you want AWS WAF to search, such as a specified header or a query string. For more information, see  FieldToMatch .

            

          
            - **Type** *(string) --* **[REQUIRED]** 

              The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

               

               
              * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the header in ``Data`` . 
               
              * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` . 
               
              * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a ``?`` character, if any. 
               
              * ``URI`` : The part of a web request that identifies a resource, for example, ``/images/daily-ad.jpg`` . 
               
              * ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .  
               

              

            
            - **Data** *(string) --* 

              When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . If the value of ``Type`` is any other value, omit ``Data`` .

               

              The name of the header is not case sensitive.

              

            
          
          - **TargetString** *(bytes) --* **[REQUIRED]** 

            The value that you want AWS WAF to search for. AWS WAF searches for the specified string in the part of web requests that you specified in ``FieldToMatch`` . The maximum length of the value is 50 bytes.

             

            Valid values depend on the values that you specified for ``FieldToMatch`` :

             

             
            * ``HEADER`` : The value that you want AWS WAF to search for in the request header that you specified in  FieldToMatch , for example, the value of the ``User-Agent`` or ``Referer`` header. 
             
            * ``METHOD`` : The HTTP method, which indicates the type of operation specified in the request. CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` . 
             
            * ``QUERY_STRING`` : The value that you want AWS WAF to search for in the query string, which is the part of a URL that appears after a ``?`` character. 
             
            * ``URI`` : The value that you want AWS WAF to search for in the part of a URL that identifies a resource, for example, ``/images/daily-ad.jpg`` . 
             
            * ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .  
             

             

            If ``TargetString`` includes alphabetic characters A-Z and a-z, note that the value is case sensitive.

             

             **If you're using the AWS WAF API**  

             

            Specify a base64-encoded version of the value. The maximum length of the value before you base64-encode it is 50 bytes.

             

            For example, suppose the value of ``Type`` is ``HEADER`` and the value of ``Data`` is ``User-Agent`` . If you want to search the ``User-Agent`` header for the value ``BadBot`` , you base64-encode ``BadBot`` using MIME base64 encoding and include the resulting value, ``QmFkQm90`` , in the value of ``TargetString`` .

             

             **If you're using the AWS CLI or one of the AWS SDKs**  

             

            The value that you want AWS WAF to search for. The SDK automatically base64 encodes the value.

            

          
          - **TextTransformation** *(string) --* **[REQUIRED]** 

            Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on ``TargetString`` before inspecting a request for a match.

             

             **CMD_LINE**  

             

            When you're concerned that attackers are injecting an operating system commandline command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

             

             
            * Delete the following characters: \ " ' ^ 
             
            * Delete spaces before the following characters: / ( 
             
            * Replace the following characters with a space: , ; 
             
            * Replace multiple spaces with one space 
             
            * Convert uppercase letters (A-Z) to lowercase (a-z) 
             

             

             **COMPRESS_WHITE_SPACE**  

             

            Use this option to replace the following characters with a space character (decimal 32):

             

             
            * \f, formfeed, decimal 12 
             
            * \t, tab, decimal 9 
             
            * \n, newline, decimal 10 
             
            * \r, carriage return, decimal 13 
             
            * \v, vertical tab, decimal 11 
             
            * non-breaking space, decimal 160 
             

             

             ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

             

             **HTML_ENTITY_DECODE**  

             

            Use this option to replace HTML-encoded characters with unencoded characters. ``HTML_ENTITY_DECODE`` performs the following operations:

             

             
            * Replaces ``(ampersand)quot;`` with ``"``   
             
            * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160 
             
            * Replaces ``(ampersand)lt;`` with a "less than" symbol 
             
            * Replaces ``(ampersand)gt;`` with ``>``   
             
            * Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` , with the corresponding characters 
             
            * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with the corresponding characters 
             

             

             **LOWERCASE**  

             

            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

             

             **URL_DECODE**  

             

            Use this option to decode a URL-encoded value.

             

             **NONE**  

             

            Specify ``NONE`` if you don't want to perform any text transformations.

            

          
          - **PositionalConstraint** *(string) --* **[REQUIRED]** 

            Within the portion of a web request that you want to search (for example, in the query string, if any), specify where you want AWS WAF to search. Valid values include the following:

             

             **CONTAINS**  

             

            The specified part of the web request must include the value of ``TargetString`` , but the location doesn't matter.

             

             **CONTAINS_WORD**  

             

            The specified part of the web request must include the value of ``TargetString`` , and ``TargetString`` must contain only alphanumeric characters or underscore (A-Z, a-z, 0-9, or _). In addition, ``TargetString`` must be a word, which means one of the following:

             

             
            * ``TargetString`` exactly matches the value of the specified part of the web request, such as the value of a header. 
             
            * ``TargetString`` is at the beginning of the specified part of the web request and is followed by a character other than an alphanumeric character or underscore (_), for example, ``BadBot;`` . 
             
            * ``TargetString`` is at the end of the specified part of the web request and is preceded by a character other than an alphanumeric character or underscore (_), for example, ``;BadBot`` . 
             
            * ``TargetString`` is in the middle of the specified part of the web request and is preceded and followed by characters other than alphanumeric characters or underscore (_), for example, ``-BadBot;`` . 
             

             

             **EXACTLY**  

             

            The value of the specified part of the web request must exactly match the value of ``TargetString`` .

             

             **STARTS_WITH**  

             

            The value of ``TargetString`` must appear at the beginning of the specified part of the web request.

             

             **ENDS_WITH**  

             

            The value of ``TargetString`` must appear at the end of the specified part of the web request.

            

          
        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``UpdateByteMatchSet`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

    **Examples** 

    The following example deletes a ByteMatchTuple object (filters) in an byte match set with the ID exampleIDs3t-46da-4fdb-b8d5-abc321j569j5.
    ::

      response = client.update_byte_match_set(
          ByteMatchSetId='exampleIDs3t-46da-4fdb-b8d5-abc321j569j5',
          ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          Updates=[
              {
                  'Action': 'DELETE',
                  'ByteMatchTuple': {
                      'FieldToMatch': {
                          'Data': 'referer',
                          'Type': 'HEADER',
                      },
                      'PositionalConstraint': 'CONTAINS',
                      'TargetString': 'badrefer1',
                      'TextTransformation': 'NONE',
                  },
              },
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: update_geo_match_set(**kwargs)

    

    Inserts or deletes  GeoMatchConstraint objects in an ``GeoMatchSet`` . For each ``GeoMatchConstraint`` object, you specify the following values: 

     

     
    * Whether to insert or delete the object from the array. If you want to change an ``GeoMatchConstraint`` object, you delete the existing object and add a new one. 
     
    * The ``Type`` . The only valid value for ``Type`` is ``Country`` . 
     
    * The ``Value`` , which is a two character code for the country to add to the ``GeoMatchConstraint`` object. Valid codes are listed in  GeoMatchConstraint$Value . 
     

     

    To create and configure an ``GeoMatchSet`` , perform the following steps:

     

     
    * Submit a  CreateGeoMatchSet request. 
     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of an  UpdateGeoMatchSet request. 
     
    * Submit an ``UpdateGeoMatchSet`` request to specify the country that you want AWS WAF to watch for. 
     

     

    When you update an ``GeoMatchSet`` , you specify the country that you want to add and/or the country that you want to delete. If you want to change a country, you delete the existing country and add the new one.

     

    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the `AWS WAF Developer Guide <http://docs.aws.amazon.com/waf/latest/developerguide/>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/UpdateGeoMatchSet>`_    


    **Request Syntax** 
    ::

      response = client.update_geo_match_set(
          GeoMatchSetId='string',
          ChangeToken='string',
          Updates=[
              {
                  'Action': 'INSERT'|'DELETE',
                  'GeoMatchConstraint': {
                      'Type': 'Country',
                      'Value': 'AF'|'AX'|'AL'|'DZ'|'AS'|'AD'|'AO'|'AI'|'AQ'|'AG'|'AR'|'AM'|'AW'|'AU'|'AT'|'AZ'|'BS'|'BH'|'BD'|'BB'|'BY'|'BE'|'BZ'|'BJ'|'BM'|'BT'|'BO'|'BQ'|'BA'|'BW'|'BV'|'BR'|'IO'|'BN'|'BG'|'BF'|'BI'|'KH'|'CM'|'CA'|'CV'|'KY'|'CF'|'TD'|'CL'|'CN'|'CX'|'CC'|'CO'|'KM'|'CG'|'CD'|'CK'|'CR'|'CI'|'HR'|'CU'|'CW'|'CY'|'CZ'|'DK'|'DJ'|'DM'|'DO'|'EC'|'EG'|'SV'|'GQ'|'ER'|'EE'|'ET'|'FK'|'FO'|'FJ'|'FI'|'FR'|'GF'|'PF'|'TF'|'GA'|'GM'|'GE'|'DE'|'GH'|'GI'|'GR'|'GL'|'GD'|'GP'|'GU'|'GT'|'GG'|'GN'|'GW'|'GY'|'HT'|'HM'|'VA'|'HN'|'HK'|'HU'|'IS'|'IN'|'ID'|'IR'|'IQ'|'IE'|'IM'|'IL'|'IT'|'JM'|'JP'|'JE'|'JO'|'KZ'|'KE'|'KI'|'KP'|'KR'|'KW'|'KG'|'LA'|'LV'|'LB'|'LS'|'LR'|'LY'|'LI'|'LT'|'LU'|'MO'|'MK'|'MG'|'MW'|'MY'|'MV'|'ML'|'MT'|'MH'|'MQ'|'MR'|'MU'|'YT'|'MX'|'FM'|'MD'|'MC'|'MN'|'ME'|'MS'|'MA'|'MZ'|'MM'|'NA'|'NR'|'NP'|'NL'|'NC'|'NZ'|'NI'|'NE'|'NG'|'NU'|'NF'|'MP'|'NO'|'OM'|'PK'|'PW'|'PS'|'PA'|'PG'|'PY'|'PE'|'PH'|'PN'|'PL'|'PT'|'PR'|'QA'|'RE'|'RO'|'RU'|'RW'|'BL'|'SH'|'KN'|'LC'|'MF'|'PM'|'VC'|'WS'|'SM'|'ST'|'SA'|'SN'|'RS'|'SC'|'SL'|'SG'|'SX'|'SK'|'SI'|'SB'|'SO'|'ZA'|'GS'|'SS'|'ES'|'LK'|'SD'|'SR'|'SJ'|'SZ'|'SE'|'CH'|'SY'|'TW'|'TJ'|'TZ'|'TH'|'TL'|'TG'|'TK'|'TO'|'TT'|'TN'|'TR'|'TM'|'TC'|'TV'|'UG'|'UA'|'AE'|'GB'|'US'|'UM'|'UY'|'UZ'|'VU'|'VE'|'VN'|'VG'|'VI'|'WF'|'EH'|'YE'|'ZM'|'ZW'
                  }
              },
          ]
      )
    :type GeoMatchSetId: string
    :param GeoMatchSetId: **[REQUIRED]** 

      The ``GeoMatchSetId`` of the  GeoMatchSet that you want to update. ``GeoMatchSetId`` is returned by  CreateGeoMatchSet and by  ListGeoMatchSets .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    :type Updates: list
    :param Updates: **[REQUIRED]** 

      An array of ``GeoMatchSetUpdate`` objects that you want to insert into or delete from an  GeoMatchSet . For more information, see the applicable data types:

       

       
      *  GeoMatchSetUpdate : Contains ``Action`` and ``GeoMatchConstraint``   
       
      *  GeoMatchConstraint : Contains ``Type`` and ``Value``   You can have only one ``Type`` and ``Value`` per ``GeoMatchConstraint`` . To add multiple countries, include multiple ``GeoMatchSetUpdate`` objects in your request. 
       

      

    
      - *(dict) --* 

        Specifies the type of update to perform to an  GeoMatchSet with  UpdateGeoMatchSet .

        

      
        - **Action** *(string) --* **[REQUIRED]** 

          Specifies whether to insert or delete a country with  UpdateGeoMatchSet .

          

        
        - **GeoMatchConstraint** *(dict) --* **[REQUIRED]** 

          The country from which web requests originate that you want AWS WAF to search for.

          

        
          - **Type** *(string) --* **[REQUIRED]** 

            The type of geographical area you want AWS WAF to search for. Currently ``Country`` is the only valid value.

            

          
          - **Value** *(string) --* **[REQUIRED]** 

            The country that you want AWS WAF to search for.

            

          
        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``UpdateGeoMatchSet`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

  .. py:method:: update_ip_set(**kwargs)

    

    Inserts or deletes  IPSetDescriptor objects in an ``IPSet`` . For each ``IPSetDescriptor`` object, you specify the following values: 

     

     
    * Whether to insert or delete the object from the array. If you want to change an ``IPSetDescriptor`` object, you delete the existing object and add a new one. 
     
    * The IP address version, ``IPv4`` or ``IPv6`` .  
     
    * The IP address in CIDR notation, for example, ``192.0.2.0/24`` (for the range of IP addresses from ``192.0.2.0`` to ``192.0.2.255`` ) or ``192.0.2.44/32`` (for the individual IP address ``192.0.2.44`` ).  
     

     

    AWS WAF supports /8, /16, /24, and /32 IP address ranges for IPv4, and /24, /32, /48, /56, /64 and /128 for IPv6. For more information about CIDR notation, see the Wikipedia entry `Classless Inter-Domain Routing <https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`__ .

     

    IPv6 addresses can be represented using any of the following formats:

     

     
    * 1111:0000:0000:0000:0000:0000:0000:0111/128 
     
    * 1111:0:0:0:0:0:0:0111/128 
     
    * 1111::0111/128 
     
    * 1111::111/128 
     

     

    You use an ``IPSet`` to specify which web requests you want to allow or block based on the IP addresses that the requests originated from. For example, if you're receiving a lot of requests from one or a small number of IP addresses and you want to block the requests, you can create an ``IPSet`` that specifies those IP addresses, and then configure AWS WAF to block the requests. 

     

    To create and configure an ``IPSet`` , perform the following steps:

     

     
    * Submit a  CreateIPSet request. 
     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of an  UpdateIPSet request. 
     
    * Submit an ``UpdateIPSet`` request to specify the IP addresses that you want AWS WAF to watch for. 
     

     

    When you update an ``IPSet`` , you specify the IP addresses that you want to add and/or the IP addresses that you want to delete. If you want to change an IP address, you delete the existing IP address and add the new one.

     

    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the `AWS WAF Developer Guide <http://docs.aws.amazon.com/waf/latest/developerguide/>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/UpdateIPSet>`_    


    **Request Syntax** 
    ::

      response = client.update_ip_set(
          IPSetId='string',
          ChangeToken='string',
          Updates=[
              {
                  'Action': 'INSERT'|'DELETE',
                  'IPSetDescriptor': {
                      'Type': 'IPV4'|'IPV6',
                      'Value': 'string'
                  }
              },
          ]
      )
    :type IPSetId: string
    :param IPSetId: **[REQUIRED]** 

      The ``IPSetId`` of the  IPSet that you want to update. ``IPSetId`` is returned by  CreateIPSet and by  ListIPSets .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    :type Updates: list
    :param Updates: **[REQUIRED]** 

      An array of ``IPSetUpdate`` objects that you want to insert into or delete from an  IPSet . For more information, see the applicable data types:

       

       
      *  IPSetUpdate : Contains ``Action`` and ``IPSetDescriptor``   
       
      *  IPSetDescriptor : Contains ``Type`` and ``Value``   
       

      

    
      - *(dict) --* 

        Specifies the type of update to perform to an  IPSet with  UpdateIPSet .

        

      
        - **Action** *(string) --* **[REQUIRED]** 

          Specifies whether to insert or delete an IP address with  UpdateIPSet .

          

        
        - **IPSetDescriptor** *(dict) --* **[REQUIRED]** 

          The IP address type (``IPV4`` or ``IPV6`` ) and the IP address range (in CIDR notation) that web requests originate from.

          

        
          - **Type** *(string) --* **[REQUIRED]** 

            Specify ``IPV4`` or ``IPV6`` .

            

          
          - **Value** *(string) --* **[REQUIRED]** 

            Specify an IPv4 address by using CIDR notation. For example:

             

             
            * To configure AWS WAF to allow, block, or count requests that originated from the IP address 192.0.2.44, specify ``192.0.2.44/32`` . 
             
            * To configure AWS WAF to allow, block, or count requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify ``192.0.2.0/24`` . 
             

             

            For more information about CIDR notation, see the Wikipedia entry `Classless Inter-Domain Routing <https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`__ .

             

            Specify an IPv6 address by using CIDR notation. For example:

             

             
            * To configure AWS WAF to allow, block, or count requests that originated from the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify ``1111:0000:0000:0000:0000:0000:0000:0111/128`` . 
             
            * To configure AWS WAF to allow, block, or count requests that originated from IP addresses 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify ``1111:0000:0000:0000:0000:0000:0000:0000/64`` . 
             

            

          
        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``UpdateIPSet`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

    **Examples** 

    The following example deletes an IPSetDescriptor object in an IP match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    ::

      response = client.update_ip_set(
          ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          IPSetId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
          Updates=[
              {
                  'Action': 'DELETE',
                  'IPSetDescriptor': {
                      'Type': 'IPV4',
                      'Value': '192.0.2.44/32',
                  },
              },
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: update_rate_based_rule(**kwargs)

    

    Inserts or deletes  Predicate objects in a rule and updates the ``RateLimit`` in the rule. 

     

    Each ``Predicate`` object identifies a predicate, such as a  ByteMatchSet or an  IPSet , that specifies the web requests that you want to block or count. The ``RateLimit`` specifies the number of requests every five minutes that triggers the rule.

     

    If you add more than one predicate to a ``RateBasedRule`` , a request must match all the predicates and exceed the ``RateLimit`` to be counted or blocked. For example, suppose you add the following to a ``RateBasedRule`` :

     

     
    * An ``IPSet`` that matches the IP address ``192.0.2.44/32``   
     
    * A ``ByteMatchSet`` that matches ``BadBot`` in the ``User-Agent`` header 
     

     

    Further, you specify a ``RateLimit`` of 15,000.

     

    You then add the ``RateBasedRule`` to a ``WebACL`` and specify that you want to block requests that satisfy the rule. For a request to be blocked, it must come from the IP address 192.0.2.44 *and* the ``User-Agent`` header in the request must contain the value ``BadBot`` . Further, requests that match these two conditions much be received at a rate of more than 15,000 every five minutes. If the rate drops below this limit, AWS WAF no longer blocks the requests.

     

    As a second example, suppose you want to limit requests to a particular page on your site. To do this, you could add the following to a ``RateBasedRule`` :

     

     
    * A ``ByteMatchSet`` with ``FieldToMatch`` of ``URI``   
     
    * A ``PositionalConstraint`` of ``STARTS_WITH``   
     
    * A ``TargetString`` of ``login``   
     

     

    Further, you specify a ``RateLimit`` of 15,000.

     

    By adding this ``RateBasedRule`` to a ``WebACL`` , you could limit requests to your login page without affecting the rest of your site.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/UpdateRateBasedRule>`_    


    **Request Syntax** 
    ::

      response = client.update_rate_based_rule(
          RuleId='string',
          ChangeToken='string',
          Updates=[
              {
                  'Action': 'INSERT'|'DELETE',
                  'Predicate': {
                      'Negated': True|False,
                      'Type': 'IPMatch'|'ByteMatch'|'SqlInjectionMatch'|'GeoMatch'|'SizeConstraint'|'XssMatch'|'RegexMatch',
                      'DataId': 'string'
                  }
              },
          ],
          RateLimit=123
      )
    :type RuleId: string
    :param RuleId: **[REQUIRED]** 

      The ``RuleId`` of the ``RateBasedRule`` that you want to update. ``RuleId`` is returned by ``CreateRateBasedRule`` and by  ListRateBasedRules .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    :type Updates: list
    :param Updates: **[REQUIRED]** 

      An array of ``RuleUpdate`` objects that you want to insert into or delete from a  RateBasedRule . 

      

    
      - *(dict) --* 

        Specifies a ``Predicate`` (such as an ``IPSet`` ) and indicates whether you want to add it to a ``Rule`` or delete it from a ``Rule`` .

        

      
        - **Action** *(string) --* **[REQUIRED]** 

          Specify ``INSERT`` to add a ``Predicate`` to a ``Rule`` . Use ``DELETE`` to remove a ``Predicate`` from a ``Rule`` .

          

        
        - **Predicate** *(dict) --* **[REQUIRED]** 

          The ID of the ``Predicate`` (such as an ``IPSet`` ) that you want to add to a ``Rule`` .

          

        
          - **Negated** *(boolean) --* **[REQUIRED]** 

            Set ``Negated`` to ``False`` if you want AWS WAF to allow, block, or count requests based on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow or block requests based on that IP address.

             

            Set ``Negated`` to ``True`` if you want AWS WAF to allow or block a request based on the negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow, block, or count requests based on all IP addresses *except*  ``192.0.2.44`` .

            

          
          - **Type** *(string) --* **[REQUIRED]** 

            The type of predicate in a ``Rule`` , such as ``ByteMatchSet`` or ``IPSet`` .

            

          
          - **DataId** *(string) --* **[REQUIRED]** 

            A unique identifier for a predicate in a ``Rule`` , such as ``ByteMatchSetId`` or ``IPSetId`` . The ID is returned by the corresponding ``Create`` or ``List`` command.

            

          
        
      
  
    :type RateLimit: integer
    :param RateLimit: **[REQUIRED]** 

      The maximum number of requests, which have an identical value in the field specified by the ``RateKey`` , allowed in a five-minute period. If the number of requests exceeds the ``RateLimit`` and the other predicates specified in the rule are also met, AWS WAF triggers the action that is specified for this rule.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``UpdateRateBasedRule`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

  .. py:method:: update_regex_match_set(**kwargs)

    

    Inserts or deletes  RegexMatchTuple objects (filters) in a  RegexMatchSet . For each ``RegexMatchSetUpdate`` object, you specify the following values: 

     

     
    * Whether to insert or delete the object from the array. If you want to change a ``RegexMatchSetUpdate`` object, you delete the existing object and add a new one. 
     
    * The part of a web request that you want AWS WAF to inspectupdate, such as a query string or the value of the ``User-Agent`` header.  
     
    * The identifier of the pattern (a regular expression) that you want AWS WAF to look for. For more information, see  RegexPatternSet .  
     
    * Whether to perform any conversions on the request, such as converting it to lowercase, before inspecting it for the specified string. 
     

     

    For example, you can create a ``RegexPatternSet`` that matches any requests with ``User-Agent`` headers that contain the string ``B[a@]dB[o0]t`` . You can then configure AWS WAF to reject those requests.

     

    To create and configure a ``RegexMatchSet`` , perform the following steps:

     

     
    * Create a ``RegexMatchSet.`` For more information, see  CreateRegexMatchSet . 
     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of an ``UpdateRegexMatchSet`` request. 
     
    * Submit an ``UpdateRegexMatchSet`` request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the identifier of the ``RegexPatternSet`` that contain the regular expression patters you want AWS WAF to watch for. 
     

     

    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the `AWS WAF Developer Guide <http://docs.aws.amazon.com/waf/latest/developerguide/>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/UpdateRegexMatchSet>`_    


    **Request Syntax** 
    ::

      response = client.update_regex_match_set(
          RegexMatchSetId='string',
          Updates=[
              {
                  'Action': 'INSERT'|'DELETE',
                  'RegexMatchTuple': {
                      'FieldToMatch': {
                          'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
                          'Data': 'string'
                      },
                      'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE',
                      'RegexPatternSetId': 'string'
                  }
              },
          ],
          ChangeToken='string'
      )
    :type RegexMatchSetId: string
    :param RegexMatchSetId: **[REQUIRED]** 

      The ``RegexMatchSetId`` of the  RegexMatchSet that you want to update. ``RegexMatchSetId`` is returned by  CreateRegexMatchSet and by  ListRegexMatchSets .

      

    
    :type Updates: list
    :param Updates: **[REQUIRED]** 

      An array of ``RegexMatchSetUpdate`` objects that you want to insert into or delete from a  RegexMatchSet . For more information, see  RegexMatchTuple .

      

    
      - *(dict) --* 

        In an  UpdateRegexMatchSet request, ``RegexMatchSetUpdate`` specifies whether to insert or delete a  RegexMatchTuple and includes the settings for the ``RegexMatchTuple`` .

        

      
        - **Action** *(string) --* **[REQUIRED]** 

          Specifies whether to insert or delete a  RegexMatchTuple .

          

        
        - **RegexMatchTuple** *(dict) --* **[REQUIRED]** 

          Information about the part of a web request that you want AWS WAF to inspect and the identifier of the regular expression (regex) pattern that you want AWS WAF to search for. If you specify ``DELETE`` for the value of ``Action`` , the ``RegexMatchTuple`` values must exactly match the values in the ``RegexMatchTuple`` that you want to delete from the ``RegexMatchSet`` .

          

        
          - **FieldToMatch** *(dict) --* **[REQUIRED]** 

            Specifies where in a web request to look for the ``RegexPatternSet`` .

            

          
            - **Type** *(string) --* **[REQUIRED]** 

              The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

               

               
              * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the header in ``Data`` . 
               
              * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` . 
               
              * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a ``?`` character, if any. 
               
              * ``URI`` : The part of a web request that identifies a resource, for example, ``/images/daily-ad.jpg`` . 
               
              * ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .  
               

              

            
            - **Data** *(string) --* 

              When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . If the value of ``Type`` is any other value, omit ``Data`` .

               

              The name of the header is not case sensitive.

              

            
          
          - **TextTransformation** *(string) --* **[REQUIRED]** 

            Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on ``RegexPatternSet`` before inspecting a request for a match.

             

             **CMD_LINE**  

             

            When you're concerned that attackers are injecting an operating system commandline command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

             

             
            * Delete the following characters: \ " ' ^ 
             
            * Delete spaces before the following characters: / ( 
             
            * Replace the following characters with a space: , ; 
             
            * Replace multiple spaces with one space 
             
            * Convert uppercase letters (A-Z) to lowercase (a-z) 
             

             

             **COMPRESS_WHITE_SPACE**  

             

            Use this option to replace the following characters with a space character (decimal 32):

             

             
            * \f, formfeed, decimal 12 
             
            * \t, tab, decimal 9 
             
            * \n, newline, decimal 10 
             
            * \r, carriage return, decimal 13 
             
            * \v, vertical tab, decimal 11 
             
            * non-breaking space, decimal 160 
             

             

             ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

             

             **HTML_ENTITY_DECODE**  

             

            Use this option to replace HTML-encoded characters with unencoded characters. ``HTML_ENTITY_DECODE`` performs the following operations:

             

             
            * Replaces ``(ampersand)quot;`` with ``"``   
             
            * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160 
             
            * Replaces ``(ampersand)lt;`` with a "less than" symbol 
             
            * Replaces ``(ampersand)gt;`` with ``>``   
             
            * Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` , with the corresponding characters 
             
            * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with the corresponding characters 
             

             

             **LOWERCASE**  

             

            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

             

             **URL_DECODE**  

             

            Use this option to decode a URL-encoded value.

             

             **NONE**  

             

            Specify ``NONE`` if you don't want to perform any text transformations.

            

          
          - **RegexPatternSetId** *(string) --* **[REQUIRED]** 

            The ``RegexPatternSetId`` for a ``RegexPatternSet`` . You use ``RegexPatternSetId`` to get information about a ``RegexPatternSet`` (see  GetRegexPatternSet ), update a ``RegexPatternSet`` (see  UpdateRegexPatternSet ), insert a ``RegexPatternSet`` into a ``RegexMatchSet`` or delete one from a ``RegexMatchSet`` (see  UpdateRegexMatchSet ), and delete an ``RegexPatternSet`` from AWS WAF (see  DeleteRegexPatternSet ).

             

             ``RegexPatternSetId`` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .

            

          
        
      
  
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``UpdateRegexMatchSet`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

  .. py:method:: update_regex_pattern_set(**kwargs)

    

    Inserts or deletes ``RegexPatternString`` objects in a  RegexPatternSet . For each ``RegexPatternString`` object, you specify the following values: 

     

     
    * Whether to insert or delete the ``RegexPatternString`` . 
     
    * The regular expression pattern that you want to insert or delete. For more information, see  RegexPatternSet .  
     

     

    For example, you can create a ``RegexPatternString`` such as ``B[a@]dB[o0]t`` . AWS WAF will match this ``RegexPatternString`` to:

     

     
    * BadBot 
     
    * BadB0t 
     
    * B@dBot 
     
    * B@dB0t 
     

     

    To create and configure a ``RegexPatternSet`` , perform the following steps:

     

     
    * Create a ``RegexPatternSet.`` For more information, see  CreateRegexPatternSet . 
     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of an ``UpdateRegexPatternSet`` request. 
     
    * Submit an ``UpdateRegexPatternSet`` request to specify the regular expression pattern that you want AWS WAF to watch for. 
     

     

    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the `AWS WAF Developer Guide <http://docs.aws.amazon.com/waf/latest/developerguide/>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/UpdateRegexPatternSet>`_    


    **Request Syntax** 
    ::

      response = client.update_regex_pattern_set(
          RegexPatternSetId='string',
          Updates=[
              {
                  'Action': 'INSERT'|'DELETE',
                  'RegexPatternString': 'string'
              },
          ],
          ChangeToken='string'
      )
    :type RegexPatternSetId: string
    :param RegexPatternSetId: **[REQUIRED]** 

      The ``RegexPatternSetId`` of the  RegexPatternSet that you want to update. ``RegexPatternSetId`` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .

      

    
    :type Updates: list
    :param Updates: **[REQUIRED]** 

      An array of ``RegexPatternSetUpdate`` objects that you want to insert into or delete from a  RegexPatternSet .

      

    
      - *(dict) --* 

        In an  UpdateRegexPatternSet request, ``RegexPatternSetUpdate`` specifies whether to insert or delete a ``RegexPatternString`` and includes the settings for the ``RegexPatternString`` .

        

      
        - **Action** *(string) --* **[REQUIRED]** 

          Specifies whether to insert or delete a ``RegexPatternString`` .

          

        
        - **RegexPatternString** *(string) --* **[REQUIRED]** 

          Specifies the regular expression (regex) pattern that you want AWS WAF to search for, such as ``B[a@]dB[o0]t`` .

          

        
      
  
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``UpdateRegexPatternSet`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

  .. py:method:: update_rule(**kwargs)

    

    Inserts or deletes  Predicate objects in a ``Rule`` . Each ``Predicate`` object identifies a predicate, such as a  ByteMatchSet or an  IPSet , that specifies the web requests that you want to allow, block, or count. If you add more than one predicate to a ``Rule`` , a request must match all of the specifications to be allowed, blocked, or counted. For example, suppose you add the following to a ``Rule`` : 

     

     
    * A ``ByteMatchSet`` that matches the value ``BadBot`` in the ``User-Agent`` header 
     
    * An ``IPSet`` that matches the IP address ``192.0.2.44``   
     

     

    You then add the ``Rule`` to a ``WebACL`` and specify that you want to block requests that satisfy the ``Rule`` . For a request to be blocked, the ``User-Agent`` header in the request must contain the value ``BadBot``  *and* the request must originate from the IP address 192.0.2.44.

     

    To create and configure a ``Rule`` , perform the following steps:

     

     
    * Create and update the predicates that you want to include in the ``Rule`` . 
     
    * Create the ``Rule`` . See  CreateRule . 
     
    * Use ``GetChangeToken`` to get the change token that you provide in the ``ChangeToken`` parameter of an  UpdateRule request. 
     
    * Submit an ``UpdateRule`` request to add predicates to the ``Rule`` . 
     
    * Create and update a ``WebACL`` that contains the ``Rule`` . See  CreateWebACL . 
     

     

    If you want to replace one ``ByteMatchSet`` or ``IPSet`` with another, you delete the existing one and add the new one.

     

    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the `AWS WAF Developer Guide <http://docs.aws.amazon.com/waf/latest/developerguide/>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/UpdateRule>`_    


    **Request Syntax** 
    ::

      response = client.update_rule(
          RuleId='string',
          ChangeToken='string',
          Updates=[
              {
                  'Action': 'INSERT'|'DELETE',
                  'Predicate': {
                      'Negated': True|False,
                      'Type': 'IPMatch'|'ByteMatch'|'SqlInjectionMatch'|'GeoMatch'|'SizeConstraint'|'XssMatch'|'RegexMatch',
                      'DataId': 'string'
                  }
              },
          ]
      )
    :type RuleId: string
    :param RuleId: **[REQUIRED]** 

      The ``RuleId`` of the ``Rule`` that you want to update. ``RuleId`` is returned by ``CreateRule`` and by  ListRules .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    :type Updates: list
    :param Updates: **[REQUIRED]** 

      An array of ``RuleUpdate`` objects that you want to insert into or delete from a  Rule . For more information, see the applicable data types:

       

       
      *  RuleUpdate : Contains ``Action`` and ``Predicate``   
       
      *  Predicate : Contains ``DataId`` , ``Negated`` , and ``Type``   
       
      *  FieldToMatch : Contains ``Data`` and ``Type``   
       

      

    
      - *(dict) --* 

        Specifies a ``Predicate`` (such as an ``IPSet`` ) and indicates whether you want to add it to a ``Rule`` or delete it from a ``Rule`` .

        

      
        - **Action** *(string) --* **[REQUIRED]** 

          Specify ``INSERT`` to add a ``Predicate`` to a ``Rule`` . Use ``DELETE`` to remove a ``Predicate`` from a ``Rule`` .

          

        
        - **Predicate** *(dict) --* **[REQUIRED]** 

          The ID of the ``Predicate`` (such as an ``IPSet`` ) that you want to add to a ``Rule`` .

          

        
          - **Negated** *(boolean) --* **[REQUIRED]** 

            Set ``Negated`` to ``False`` if you want AWS WAF to allow, block, or count requests based on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow or block requests based on that IP address.

             

            Set ``Negated`` to ``True`` if you want AWS WAF to allow or block a request based on the negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an ``IPSet`` includes the IP address ``192.0.2.44`` , AWS WAF will allow, block, or count requests based on all IP addresses *except*  ``192.0.2.44`` .

            

          
          - **Type** *(string) --* **[REQUIRED]** 

            The type of predicate in a ``Rule`` , such as ``ByteMatchSet`` or ``IPSet`` .

            

          
          - **DataId** *(string) --* **[REQUIRED]** 

            A unique identifier for a predicate in a ``Rule`` , such as ``ByteMatchSetId`` or ``IPSetId`` . The ID is returned by the corresponding ``Create`` or ``List`` command.

            

          
        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``UpdateRule`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

    **Examples** 

    The following example deletes a Predicate object in a rule with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    ::

      response = client.update_rule(
          ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          RuleId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
          Updates=[
              {
                  'Action': 'DELETE',
                  'Predicate': {
                      'DataId': 'MyByteMatchSetID',
                      'Negated': False,
                      'Type': 'ByteMatch',
                  },
              },
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: update_rule_group(**kwargs)

    

    Inserts or deletes  ActivatedRule objects in a ``RuleGroup`` .

     

    You can only insert ``REGULAR`` rules into a rule group.

     

    You can have a maximum of ten rules per rule group.

     

    To create and configure a ``RuleGroup`` , perform the following steps:

     

     
    * Create and update the ``Rules`` that you want to include in the ``RuleGroup`` . See  CreateRule . 
     
    * Use ``GetChangeToken`` to get the change token that you provide in the ``ChangeToken`` parameter of an  UpdateRuleGroup request. 
     
    * Submit an ``UpdateRuleGroup`` request to add ``Rules`` to the ``RuleGroup`` . 
     
    * Create and update a ``WebACL`` that contains the ``RuleGroup`` . See  CreateWebACL . 
     

     

    If you want to replace one ``Rule`` with another, you delete the existing one and add the new one.

     

    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the `AWS WAF Developer Guide <http://docs.aws.amazon.com/waf/latest/developerguide/>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/UpdateRuleGroup>`_    


    **Request Syntax** 
    ::

      response = client.update_rule_group(
          RuleGroupId='string',
          Updates=[
              {
                  'Action': 'INSERT'|'DELETE',
                  'ActivatedRule': {
                      'Priority': 123,
                      'RuleId': 'string',
                      'Action': {
                          'Type': 'BLOCK'|'ALLOW'|'COUNT'
                      },
                      'OverrideAction': {
                          'Type': 'NONE'|'COUNT'
                      },
                      'Type': 'REGULAR'|'RATE_BASED'|'GROUP'
                  }
              },
          ],
          ChangeToken='string'
      )
    :type RuleGroupId: string
    :param RuleGroupId: **[REQUIRED]** 

      The ``RuleGroupId`` of the  RuleGroup that you want to update. ``RuleGroupId`` is returned by  CreateRuleGroup and by  ListRuleGroups .

      

    
    :type Updates: list
    :param Updates: **[REQUIRED]** 

      An array of ``RuleGroupUpdate`` objects that you want to insert into or delete from a  RuleGroup .

       

      You can only insert ``REGULAR`` rules into a rule group.

       

      The ``Action`` data type within ``ActivatedRule`` is used only when submitting an ``UpdateWebACL`` request. ``ActivatedRule|Action`` is not applicable and therefore not available for ``UpdateRuleGroup`` .

      

    
      - *(dict) --* 

        Specifies an ``ActivatedRule`` and indicates whether you want to add it to a ``RuleGroup`` or delete it from a ``RuleGroup`` .

        

      
        - **Action** *(string) --* **[REQUIRED]** 

          Specify ``INSERT`` to add an ``ActivatedRule`` to a ``RuleGroup`` . Use ``DELETE`` to remove an ``ActivatedRule`` from a ``RuleGroup`` .

          

        
        - **ActivatedRule** *(dict) --* **[REQUIRED]** 

          The ``ActivatedRule`` object specifies a ``Rule`` that you want to insert or delete, the priority of the ``Rule`` in the ``WebACL`` , and the action that you want AWS WAF to take when a web request matches the ``Rule`` (``ALLOW`` , ``BLOCK`` , or ``COUNT`` ).

          

        
          - **Priority** *(integer) --* **[REQUIRED]** 

            Specifies the order in which the ``Rules`` in a ``WebACL`` are evaluated. Rules with a lower value for ``Priority`` are evaluated before ``Rules`` with a higher value. The value must be a unique integer. If you add multiple ``Rules`` to a ``WebACL`` , the values don't need to be consecutive.

            

          
          - **RuleId** *(string) --* **[REQUIRED]** 

            The ``RuleId`` for a ``Rule`` . You use ``RuleId`` to get more information about a ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule`` from AWS WAF (see  DeleteRule ).

             

             ``RuleId`` is returned by  CreateRule and by  ListRules .

            

          
          - **Action** *(dict) --* 

            Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the ``Rule`` . Valid values for ``Action`` include the following:

             

             
            * ``ALLOW`` : CloudFront responds with the requested object. 
             
            * ``BLOCK`` : CloudFront responds with an HTTP 403 (Forbidden) status code. 
             
            * ``COUNT`` : AWS WAF increments a counter of requests that match the conditions in the rule and then continues to inspect the web request based on the remaining rules in the web ACL.  
             

             

            The ``Action`` data type within ``ActivatedRule`` is used only when submitting an ``UpdateWebACL`` request. ``ActivatedRule|Action`` is not applicable and therefore not available for ``UpdateRuleGroup`` .

            

          
            - **Type** *(string) --* **[REQUIRED]** 

              Specifies how you want AWS WAF to respond to requests that match the settings in a ``Rule`` . Valid settings include the following:

               

               
              * ``ALLOW`` : AWS WAF allows requests 
               
              * ``BLOCK`` : AWS WAF blocks requests 
               
              * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for a ``WebACL`` . 
               

              

            
          
          - **OverrideAction** *(dict) --* 

            Use the ``OverrideAction`` to test your ``RuleGroup`` .

             

            Any rule in a ``RuleGroup`` can potentially block a request. If you set the ``OverrideAction`` to ``None`` , the ``RuleGroup`` will block a request if any individual rule in the ``RuleGroup`` matches the request and is configured to block that request. However if you first want to test the ``RuleGroup`` , set the ``OverrideAction`` to ``Count`` . The ``RuleGroup`` will then override any block action specified by individual rules contained within the group. Instead of blocking matching requests, those requests will be counted. You can view a record of counted requests using  GetSampledRequests . 

             

            The ``OverrideAction`` data type within ``ActivatedRule`` is used only when submitting an ``UpdateRuleGroup`` request. ``ActivatedRule|OverrideAction`` is not applicable and therefore not available for ``UpdateWebACL`` .

            

          
            - **Type** *(string) --* **[REQUIRED]** 

               ``COUNT`` overrides the action specified by the individual rule within a ``RuleGroup`` . If set to ``NONE`` , the rule's action will take place.

              

            
          
          - **Type** *(string) --* 

            The rule type, either ``REGULAR`` , as defined by  Rule , ``RATE_BASED`` , as defined by  RateBasedRule , or ``GROUP`` , as defined by  RuleGroup . The default is REGULAR. Although this field is optional, be aware that if you try to add a RATE_BASED rule to a web ACL without setting the type, the  UpdateWebACL request will fail because the request tries to add a REGULAR rule with the specified ID, which does not exist. 

            

          
        
      
  
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``UpdateRuleGroup`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

  .. py:method:: update_size_constraint_set(**kwargs)

    

    Inserts or deletes  SizeConstraint objects (filters) in a  SizeConstraintSet . For each ``SizeConstraint`` object, you specify the following values: 

     

     
    * Whether to insert or delete the object from the array. If you want to change a ``SizeConstraintSetUpdate`` object, you delete the existing object and add a new one. 
     
    * The part of a web request that you want AWS WAF to evaluate, such as the length of a query string or the length of the ``User-Agent`` header. 
     
    * Whether to perform any transformations on the request, such as converting it to lowercase, before checking its length. Note that transformations of the request body are not supported because the AWS resource forwards only the first ``8192`` bytes of your request to AWS WAF. 
     
    * A ``ComparisonOperator`` used for evaluating the selected part of the request against the specified ``Size`` , such as equals, greater than, less than, and so on. 
     
    * The length, in bytes, that you want AWS WAF to watch for in selected part of the request. The length is computed after applying the transformation. 
     

     

    For example, you can add a ``SizeConstraintSetUpdate`` object that matches web requests in which the length of the ``User-Agent`` header is greater than 100 bytes. You can then configure AWS WAF to block those requests.

     

    To create and configure a ``SizeConstraintSet`` , perform the following steps:

     

     
    * Create a ``SizeConstraintSet.`` For more information, see  CreateSizeConstraintSet . 
     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of an ``UpdateSizeConstraintSet`` request. 
     
    * Submit an ``UpdateSizeConstraintSet`` request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the value that you want AWS WAF to watch for. 
     

     

    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the `AWS WAF Developer Guide <http://docs.aws.amazon.com/waf/latest/developerguide/>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/UpdateSizeConstraintSet>`_    


    **Request Syntax** 
    ::

      response = client.update_size_constraint_set(
          SizeConstraintSetId='string',
          ChangeToken='string',
          Updates=[
              {
                  'Action': 'INSERT'|'DELETE',
                  'SizeConstraint': {
                      'FieldToMatch': {
                          'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
                          'Data': 'string'
                      },
                      'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE',
                      'ComparisonOperator': 'EQ'|'NE'|'LE'|'LT'|'GE'|'GT',
                      'Size': 123
                  }
              },
          ]
      )
    :type SizeConstraintSetId: string
    :param SizeConstraintSetId: **[REQUIRED]** 

      The ``SizeConstraintSetId`` of the  SizeConstraintSet that you want to update. ``SizeConstraintSetId`` is returned by  CreateSizeConstraintSet and by  ListSizeConstraintSets .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    :type Updates: list
    :param Updates: **[REQUIRED]** 

      An array of ``SizeConstraintSetUpdate`` objects that you want to insert into or delete from a  SizeConstraintSet . For more information, see the applicable data types:

       

       
      *  SizeConstraintSetUpdate : Contains ``Action`` and ``SizeConstraint``   
       
      *  SizeConstraint : Contains ``FieldToMatch`` , ``TextTransformation`` , ``ComparisonOperator`` , and ``Size``   
       
      *  FieldToMatch : Contains ``Data`` and ``Type``   
       

      

    
      - *(dict) --* 

        Specifies the part of a web request that you want to inspect the size of and indicates whether you want to add the specification to a  SizeConstraintSet or delete it from a ``SizeConstraintSet`` .

        

      
        - **Action** *(string) --* **[REQUIRED]** 

          Specify ``INSERT`` to add a  SizeConstraintSetUpdate to a  SizeConstraintSet . Use ``DELETE`` to remove a ``SizeConstraintSetUpdate`` from a ``SizeConstraintSet`` .

          

        
        - **SizeConstraint** *(dict) --* **[REQUIRED]** 

          Specifies a constraint on the size of a part of the web request. AWS WAF uses the ``Size`` , ``ComparisonOperator`` , and ``FieldToMatch`` to build an expression in the form of "``Size``  ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that expression is true, the ``SizeConstraint`` is considered to match.

          

        
          - **FieldToMatch** *(dict) --* **[REQUIRED]** 

            Specifies where in a web request to look for the size constraint.

            

          
            - **Type** *(string) --* **[REQUIRED]** 

              The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

               

               
              * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the header in ``Data`` . 
               
              * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` . 
               
              * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a ``?`` character, if any. 
               
              * ``URI`` : The part of a web request that identifies a resource, for example, ``/images/daily-ad.jpg`` . 
               
              * ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .  
               

              

            
            - **Data** *(string) --* 

              When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . If the value of ``Type`` is any other value, omit ``Data`` .

               

              The name of the header is not case sensitive.

              

            
          
          - **TextTransformation** *(string) --* **[REQUIRED]** 

            Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

             

            Note that if you choose ``BODY`` for the value of ``Type`` , you must choose ``NONE`` for ``TextTransformation`` because CloudFront forwards only the first 8192 bytes for inspection. 

             

             **NONE**  

             

            Specify ``NONE`` if you don't want to perform any text transformations.

             

             **CMD_LINE**  

             

            When you're concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

             

             
            * Delete the following characters: \ " ' ^ 
             
            * Delete spaces before the following characters: / ( 
             
            * Replace the following characters with a space: , ; 
             
            * Replace multiple spaces with one space 
             
            * Convert uppercase letters (A-Z) to lowercase (a-z) 
             

             

             **COMPRESS_WHITE_SPACE**  

             

            Use this option to replace the following characters with a space character (decimal 32):

             

             
            * \f, formfeed, decimal 12 
             
            * \t, tab, decimal 9 
             
            * \n, newline, decimal 10 
             
            * \r, carriage return, decimal 13 
             
            * \v, vertical tab, decimal 11 
             
            * non-breaking space, decimal 160 
             

             

             ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

             

             **HTML_ENTITY_DECODE**  

             

            Use this option to replace HTML-encoded characters with unencoded characters. ``HTML_ENTITY_DECODE`` performs the following operations:

             

             
            * Replaces ``(ampersand)quot;`` with ``"``   
             
            * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160 
             
            * Replaces ``(ampersand)lt;`` with a "less than" symbol 
             
            * Replaces ``(ampersand)gt;`` with ``>``   
             
            * Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` , with the corresponding characters 
             
            * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with the corresponding characters 
             

             

             **LOWERCASE**  

             

            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

             

             **URL_DECODE**  

             

            Use this option to decode a URL-encoded value.

            

          
          - **ComparisonOperator** *(string) --* **[REQUIRED]** 

            The type of comparison you want AWS WAF to perform. AWS WAF uses this in combination with the provided ``Size`` and ``FieldToMatch`` to build an expression in the form of "``Size``  ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that expression is true, the ``SizeConstraint`` is considered to match.

             

             **EQ** : Used to test if the ``Size`` is equal to the size of the ``FieldToMatch``  

             

             **NE** : Used to test if the ``Size`` is not equal to the size of the ``FieldToMatch``  

             

             **LE** : Used to test if the ``Size`` is less than or equal to the size of the ``FieldToMatch``  

             

             **LT** : Used to test if the ``Size`` is strictly less than the size of the ``FieldToMatch``  

             

             **GE** : Used to test if the ``Size`` is greater than or equal to the size of the ``FieldToMatch``  

             

             **GT** : Used to test if the ``Size`` is strictly greater than the size of the ``FieldToMatch``  

            

          
          - **Size** *(integer) --* **[REQUIRED]** 

            The size in bytes that you want AWS WAF to compare against the size of the specified ``FieldToMatch`` . AWS WAF uses this in combination with ``ComparisonOperator`` and ``FieldToMatch`` to build an expression in the form of "``Size``  ``ComparisonOperator`` size in bytes of ``FieldToMatch`` ". If that expression is true, the ``SizeConstraint`` is considered to match.

             

            Valid values for size are 0 - 21474836480 bytes (0 - 20 GB).

             

            If you specify ``URI`` for the value of ``Type`` , the / in the URI counts as one character. For example, the URI ``/logo.jpg`` is nine characters long.

            

          
        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``UpdateSizeConstraintSet`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

    **Examples** 

    The following example deletes a SizeConstraint object (filters) in a size constraint set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    ::

      response = client.update_size_constraint_set(
          ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          SizeConstraintSetId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
          Updates=[
              {
                  'Action': 'DELETE',
                  'SizeConstraint': {
                      'ComparisonOperator': 'GT',
                      'FieldToMatch': {
                          'Type': 'QUERY_STRING',
                      },
                      'Size': 0,
                      'TextTransformation': 'NONE',
                  },
              },
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: update_sql_injection_match_set(**kwargs)

    

    Inserts or deletes  SqlInjectionMatchTuple objects (filters) in a  SqlInjectionMatchSet . For each ``SqlInjectionMatchTuple`` object, you specify the following values:

     

     
    * ``Action`` : Whether to insert the object into or delete the object from the array. To change a ``SqlInjectionMatchTuple`` , you delete the existing object and add a new one. 
     
    * ``FieldToMatch`` : The part of web requests that you want AWS WAF to inspect and, if you want AWS WAF to inspect a header, the name of the header. 
     
    * ``TextTransformation`` : Which text transformation, if any, to perform on the web request before inspecting the request for snippets of malicious SQL code. 
     

     

    You use ``SqlInjectionMatchSet`` objects to specify which CloudFront requests you want to allow, block, or count. For example, if you're receiving requests that contain snippets of SQL code in the query string and you want to block the requests, you can create a ``SqlInjectionMatchSet`` with the applicable settings, and then configure AWS WAF to block the requests. 

     

    To create and configure a ``SqlInjectionMatchSet`` , perform the following steps:

     

     
    * Submit a  CreateSqlInjectionMatchSet request. 
     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of an  UpdateIPSet request. 
     
    * Submit an ``UpdateSqlInjectionMatchSet`` request to specify the parts of web requests that you want AWS WAF to inspect for snippets of SQL code. 
     

     

    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the `AWS WAF Developer Guide <http://docs.aws.amazon.com/waf/latest/developerguide/>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/UpdateSqlInjectionMatchSet>`_    


    **Request Syntax** 
    ::

      response = client.update_sql_injection_match_set(
          SqlInjectionMatchSetId='string',
          ChangeToken='string',
          Updates=[
              {
                  'Action': 'INSERT'|'DELETE',
                  'SqlInjectionMatchTuple': {
                      'FieldToMatch': {
                          'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
                          'Data': 'string'
                      },
                      'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                  }
              },
          ]
      )
    :type SqlInjectionMatchSetId: string
    :param SqlInjectionMatchSetId: **[REQUIRED]** 

      The ``SqlInjectionMatchSetId`` of the ``SqlInjectionMatchSet`` that you want to update. ``SqlInjectionMatchSetId`` is returned by  CreateSqlInjectionMatchSet and by  ListSqlInjectionMatchSets .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    :type Updates: list
    :param Updates: **[REQUIRED]** 

      An array of ``SqlInjectionMatchSetUpdate`` objects that you want to insert into or delete from a  SqlInjectionMatchSet . For more information, see the applicable data types:

       

       
      *  SqlInjectionMatchSetUpdate : Contains ``Action`` and ``SqlInjectionMatchTuple``   
       
      *  SqlInjectionMatchTuple : Contains ``FieldToMatch`` and ``TextTransformation``   
       
      *  FieldToMatch : Contains ``Data`` and ``Type``   
       

      

    
      - *(dict) --* 

        Specifies the part of a web request that you want to inspect for snippets of malicious SQL code and indicates whether you want to add the specification to a  SqlInjectionMatchSet or delete it from a ``SqlInjectionMatchSet`` .

        

      
        - **Action** *(string) --* **[REQUIRED]** 

          Specify ``INSERT`` to add a  SqlInjectionMatchSetUpdate to a  SqlInjectionMatchSet . Use ``DELETE`` to remove a ``SqlInjectionMatchSetUpdate`` from a ``SqlInjectionMatchSet`` .

          

        
        - **SqlInjectionMatchTuple** *(dict) --* **[REQUIRED]** 

          Specifies the part of a web request that you want AWS WAF to inspect for snippets of malicious SQL code and, if you want AWS WAF to inspect a header, the name of the header.

          

        
          - **FieldToMatch** *(dict) --* **[REQUIRED]** 

            Specifies where in a web request to look for snippets of malicious SQL code.

            

          
            - **Type** *(string) --* **[REQUIRED]** 

              The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

               

               
              * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the header in ``Data`` . 
               
              * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` . 
               
              * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a ``?`` character, if any. 
               
              * ``URI`` : The part of a web request that identifies a resource, for example, ``/images/daily-ad.jpg`` . 
               
              * ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .  
               

              

            
            - **Data** *(string) --* 

              When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . If the value of ``Type`` is any other value, omit ``Data`` .

               

              The name of the header is not case sensitive.

              

            
          
          - **TextTransformation** *(string) --* **[REQUIRED]** 

            Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

             

             **CMD_LINE**  

             

            When you're concerned that attackers are injecting an operating system commandline command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

             

             
            * Delete the following characters: \ " ' ^ 
             
            * Delete spaces before the following characters: / ( 
             
            * Replace the following characters with a space: , ; 
             
            * Replace multiple spaces with one space 
             
            * Convert uppercase letters (A-Z) to lowercase (a-z) 
             

             

             **COMPRESS_WHITE_SPACE**  

             

            Use this option to replace the following characters with a space character (decimal 32):

             

             
            * \f, formfeed, decimal 12 
             
            * \t, tab, decimal 9 
             
            * \n, newline, decimal 10 
             
            * \r, carriage return, decimal 13 
             
            * \v, vertical tab, decimal 11 
             
            * non-breaking space, decimal 160 
             

             

             ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

             

             **HTML_ENTITY_DECODE**  

             

            Use this option to replace HTML-encoded characters with unencoded characters. ``HTML_ENTITY_DECODE`` performs the following operations:

             

             
            * Replaces ``(ampersand)quot;`` with ``"``   
             
            * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160 
             
            * Replaces ``(ampersand)lt;`` with a "less than" symbol 
             
            * Replaces ``(ampersand)gt;`` with ``>``   
             
            * Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` , with the corresponding characters 
             
            * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with the corresponding characters 
             

             

             **LOWERCASE**  

             

            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

             

             **URL_DECODE**  

             

            Use this option to decode a URL-encoded value.

             

             **NONE**  

             

            Specify ``NONE`` if you don't want to perform any text transformations.

            

          
        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The response to an  UpdateSqlInjectionMatchSets request.

        
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``UpdateSqlInjectionMatchSet`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

    **Examples** 

    The following example deletes a SqlInjectionMatchTuple object (filters) in a SQL injection match set with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    ::

      response = client.update_sql_injection_match_set(
          ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          SqlInjectionMatchSetId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
          Updates=[
              {
                  'Action': 'DELETE',
                  'SqlInjectionMatchTuple': {
                      'FieldToMatch': {
                          'Type': 'QUERY_STRING',
                      },
                      'TextTransformation': 'URL_DECODE',
                  },
              },
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: update_web_acl(**kwargs)

    

    Inserts or deletes  ActivatedRule objects in a ``WebACL`` . Each ``Rule`` identifies web requests that you want to allow, block, or count. When you update a ``WebACL`` , you specify the following values:

     

     
    * A default action for the ``WebACL`` , either ``ALLOW`` or ``BLOCK`` . AWS WAF performs the default action if a request doesn't match the criteria in any of the ``Rules`` in a ``WebACL`` . 
     
    * The ``Rules`` that you want to add and/or delete. If you want to replace one ``Rule`` with another, you delete the existing ``Rule`` and add the new one. 
     
    * For each ``Rule`` , whether you want AWS WAF to allow requests, block requests, or count requests that match the conditions in the ``Rule`` . 
     
    * The order in which you want AWS WAF to evaluate the ``Rules`` in a ``WebACL`` . If you add more than one ``Rule`` to a ``WebACL`` , AWS WAF evaluates each request against the ``Rules`` in order based on the value of ``Priority`` . (The ``Rule`` that has the lowest value for ``Priority`` is evaluated first.) When a web request matches all of the predicates (such as ``ByteMatchSets`` and ``IPSets`` ) in a ``Rule`` , AWS WAF immediately takes the corresponding action, allow or block, and doesn't evaluate the request against the remaining ``Rules`` in the ``WebACL`` , if any.  
     

     

    To create and configure a ``WebACL`` , perform the following steps:

     

     
    * Create and update the predicates that you want to include in ``Rules`` . For more information, see  CreateByteMatchSet ,  UpdateByteMatchSet ,  CreateIPSet ,  UpdateIPSet ,  CreateSqlInjectionMatchSet , and  UpdateSqlInjectionMatchSet . 
     
    * Create and update the ``Rules`` that you want to include in the ``WebACL`` . For more information, see  CreateRule and  UpdateRule . 
     
    * Create a ``WebACL`` . See  CreateWebACL . 
     
    * Use ``GetChangeToken`` to get the change token that you provide in the ``ChangeToken`` parameter of an  UpdateWebACL request. 
     
    * Submit an ``UpdateWebACL`` request to specify the ``Rules`` that you want to include in the ``WebACL`` , to specify the default action, and to associate the ``WebACL`` with a CloudFront distribution.  
     

     

    Be aware that if you try to add a RATE_BASED rule to a web ACL without setting the rule type when first creating the rule, the  UpdateWebACL request will fail because the request tries to add a REGULAR rule (the default rule type) with the specified ID, which does not exist. 

     

    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the `AWS WAF Developer Guide <http://docs.aws.amazon.com/waf/latest/developerguide/>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/UpdateWebACL>`_    


    **Request Syntax** 
    ::

      response = client.update_web_acl(
          WebACLId='string',
          ChangeToken='string',
          Updates=[
              {
                  'Action': 'INSERT'|'DELETE',
                  'ActivatedRule': {
                      'Priority': 123,
                      'RuleId': 'string',
                      'Action': {
                          'Type': 'BLOCK'|'ALLOW'|'COUNT'
                      },
                      'OverrideAction': {
                          'Type': 'NONE'|'COUNT'
                      },
                      'Type': 'REGULAR'|'RATE_BASED'|'GROUP'
                  }
              },
          ],
          DefaultAction={
              'Type': 'BLOCK'|'ALLOW'|'COUNT'
          }
      )
    :type WebACLId: string
    :param WebACLId: **[REQUIRED]** 

      The ``WebACLId`` of the  WebACL that you want to update. ``WebACLId`` is returned by  CreateWebACL and by  ListWebACLs .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    :type Updates: list
    :param Updates: 

      An array of updates to make to the  WebACL .

       

      An array of ``WebACLUpdate`` objects that you want to insert into or delete from a  WebACL . For more information, see the applicable data types:

       

       
      *  WebACLUpdate : Contains ``Action`` and ``ActivatedRule``   
       
      *  ActivatedRule : Contains ``Action`` , ``Priority`` , ``RuleId`` , and ``Type`` . The ``OverrideAction`` data type within ``ActivatedRule`` is used only when submitting an ``UpdateRuleGroup`` request. ``ActivatedRule|OverrideAction`` is not applicable and therefore not available for ``UpdateWebACL`` .  
       
      *  WafAction : Contains ``Type``   
       

      

    
      - *(dict) --* 

        Specifies whether to insert a ``Rule`` into or delete a ``Rule`` from a ``WebACL`` .

        

      
        - **Action** *(string) --* **[REQUIRED]** 

          Specifies whether to insert a ``Rule`` into or delete a ``Rule`` from a ``WebACL`` .

          

        
        - **ActivatedRule** *(dict) --* **[REQUIRED]** 

          The ``ActivatedRule`` object in an  UpdateWebACL request specifies a ``Rule`` that you want to insert or delete, the priority of the ``Rule`` in the ``WebACL`` , and the action that you want AWS WAF to take when a web request matches the ``Rule`` (``ALLOW`` , ``BLOCK`` , or ``COUNT`` ).

          

        
          - **Priority** *(integer) --* **[REQUIRED]** 

            Specifies the order in which the ``Rules`` in a ``WebACL`` are evaluated. Rules with a lower value for ``Priority`` are evaluated before ``Rules`` with a higher value. The value must be a unique integer. If you add multiple ``Rules`` to a ``WebACL`` , the values don't need to be consecutive.

            

          
          - **RuleId** *(string) --* **[REQUIRED]** 

            The ``RuleId`` for a ``Rule`` . You use ``RuleId`` to get more information about a ``Rule`` (see  GetRule ), update a ``Rule`` (see  UpdateRule ), insert a ``Rule`` into a ``WebACL`` or delete a one from a ``WebACL`` (see  UpdateWebACL ), or delete a ``Rule`` from AWS WAF (see  DeleteRule ).

             

             ``RuleId`` is returned by  CreateRule and by  ListRules .

            

          
          - **Action** *(dict) --* 

            Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the ``Rule`` . Valid values for ``Action`` include the following:

             

             
            * ``ALLOW`` : CloudFront responds with the requested object. 
             
            * ``BLOCK`` : CloudFront responds with an HTTP 403 (Forbidden) status code. 
             
            * ``COUNT`` : AWS WAF increments a counter of requests that match the conditions in the rule and then continues to inspect the web request based on the remaining rules in the web ACL.  
             

             

            The ``Action`` data type within ``ActivatedRule`` is used only when submitting an ``UpdateWebACL`` request. ``ActivatedRule|Action`` is not applicable and therefore not available for ``UpdateRuleGroup`` .

            

          
            - **Type** *(string) --* **[REQUIRED]** 

              Specifies how you want AWS WAF to respond to requests that match the settings in a ``Rule`` . Valid settings include the following:

               

               
              * ``ALLOW`` : AWS WAF allows requests 
               
              * ``BLOCK`` : AWS WAF blocks requests 
               
              * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for a ``WebACL`` . 
               

              

            
          
          - **OverrideAction** *(dict) --* 

            Use the ``OverrideAction`` to test your ``RuleGroup`` .

             

            Any rule in a ``RuleGroup`` can potentially block a request. If you set the ``OverrideAction`` to ``None`` , the ``RuleGroup`` will block a request if any individual rule in the ``RuleGroup`` matches the request and is configured to block that request. However if you first want to test the ``RuleGroup`` , set the ``OverrideAction`` to ``Count`` . The ``RuleGroup`` will then override any block action specified by individual rules contained within the group. Instead of blocking matching requests, those requests will be counted. You can view a record of counted requests using  GetSampledRequests . 

             

            The ``OverrideAction`` data type within ``ActivatedRule`` is used only when submitting an ``UpdateRuleGroup`` request. ``ActivatedRule|OverrideAction`` is not applicable and therefore not available for ``UpdateWebACL`` .

            

          
            - **Type** *(string) --* **[REQUIRED]** 

               ``COUNT`` overrides the action specified by the individual rule within a ``RuleGroup`` . If set to ``NONE`` , the rule's action will take place.

              

            
          
          - **Type** *(string) --* 

            The rule type, either ``REGULAR`` , as defined by  Rule , ``RATE_BASED`` , as defined by  RateBasedRule , or ``GROUP`` , as defined by  RuleGroup . The default is REGULAR. Although this field is optional, be aware that if you try to add a RATE_BASED rule to a web ACL without setting the type, the  UpdateWebACL request will fail because the request tries to add a REGULAR rule with the specified ID, which does not exist. 

            

          
        
      
  
    :type DefaultAction: dict
    :param DefaultAction: 

      A default action for the web ACL, either ALLOW or BLOCK. AWS WAF performs the default action if a request doesn't match the criteria in any of the rules in a web ACL.

      

    
      - **Type** *(string) --* **[REQUIRED]** 

        Specifies how you want AWS WAF to respond to requests that match the settings in a ``Rule`` . Valid settings include the following:

         

         
        * ``ALLOW`` : AWS WAF allows requests 
         
        * ``BLOCK`` : AWS WAF blocks requests 
         
        * ``COUNT`` : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You can't specify ``COUNT`` for the default action for a ``WebACL`` . 
         

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``UpdateWebACL`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

    **Examples** 

    The following example deletes an ActivatedRule object in a WebACL with the ID webacl-1472061481310.
    ::

      response = client.update_web_acl(
          ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          DefaultAction={
              'Type': 'ALLOW',
          },
          Updates=[
              {
                  'Action': 'DELETE',
                  'ActivatedRule': {
                      'Action': {
                          'Type': 'ALLOW',
                      },
                      'Priority': 1,
                      'RuleId': 'WAFRule-1-Example',
                  },
              },
          ],
          WebACLId='webacl-1472061481310',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: update_xss_match_set(**kwargs)

    

    Inserts or deletes  XssMatchTuple objects (filters) in an  XssMatchSet . For each ``XssMatchTuple`` object, you specify the following values:

     

     
    * ``Action`` : Whether to insert the object into or delete the object from the array. To change a ``XssMatchTuple`` , you delete the existing object and add a new one. 
     
    * ``FieldToMatch`` : The part of web requests that you want AWS WAF to inspect and, if you want AWS WAF to inspect a header, the name of the header. 
     
    * ``TextTransformation`` : Which text transformation, if any, to perform on the web request before inspecting the request for cross-site scripting attacks. 
     

     

    You use ``XssMatchSet`` objects to specify which CloudFront requests you want to allow, block, or count. For example, if you're receiving requests that contain cross-site scripting attacks in the request body and you want to block the requests, you can create an ``XssMatchSet`` with the applicable settings, and then configure AWS WAF to block the requests. 

     

    To create and configure an ``XssMatchSet`` , perform the following steps:

     

     
    * Submit a  CreateXssMatchSet request. 
     
    * Use  GetChangeToken to get the change token that you provide in the ``ChangeToken`` parameter of an  UpdateIPSet request. 
     
    * Submit an ``UpdateXssMatchSet`` request to specify the parts of web requests that you want AWS WAF to inspect for cross-site scripting attacks. 
     

     

    For more information about how to use the AWS WAF API to allow or block HTTP requests, see the `AWS WAF Developer Guide <http://docs.aws.amazon.com/waf/latest/developerguide/>`__ .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/UpdateXssMatchSet>`_    


    **Request Syntax** 
    ::

      response = client.update_xss_match_set(
          XssMatchSetId='string',
          ChangeToken='string',
          Updates=[
              {
                  'Action': 'INSERT'|'DELETE',
                  'XssMatchTuple': {
                      'FieldToMatch': {
                          'Type': 'URI'|'QUERY_STRING'|'HEADER'|'METHOD'|'BODY',
                          'Data': 'string'
                      },
                      'TextTransformation': 'NONE'|'COMPRESS_WHITE_SPACE'|'HTML_ENTITY_DECODE'|'LOWERCASE'|'CMD_LINE'|'URL_DECODE'
                  }
              },
          ]
      )
    :type XssMatchSetId: string
    :param XssMatchSetId: **[REQUIRED]** 

      The ``XssMatchSetId`` of the ``XssMatchSet`` that you want to update. ``XssMatchSetId`` is returned by  CreateXssMatchSet and by  ListXssMatchSets .

      

    
    :type ChangeToken: string
    :param ChangeToken: **[REQUIRED]** 

      The value returned by the most recent call to  GetChangeToken .

      

    
    :type Updates: list
    :param Updates: **[REQUIRED]** 

      An array of ``XssMatchSetUpdate`` objects that you want to insert into or delete from a  XssMatchSet . For more information, see the applicable data types:

       

       
      *  XssMatchSetUpdate : Contains ``Action`` and ``XssMatchTuple``   
       
      *  XssMatchTuple : Contains ``FieldToMatch`` and ``TextTransformation``   
       
      *  FieldToMatch : Contains ``Data`` and ``Type``   
       

      

    
      - *(dict) --* 

        Specifies the part of a web request that you want to inspect for cross-site scripting attacks and indicates whether you want to add the specification to an  XssMatchSet or delete it from an ``XssMatchSet`` .

        

      
        - **Action** *(string) --* **[REQUIRED]** 

          Specify ``INSERT`` to add a  XssMatchSetUpdate to an  XssMatchSet . Use ``DELETE`` to remove a ``XssMatchSetUpdate`` from an ``XssMatchSet`` .

          

        
        - **XssMatchTuple** *(dict) --* **[REQUIRED]** 

          Specifies the part of a web request that you want AWS WAF to inspect for cross-site scripting attacks and, if you want AWS WAF to inspect a header, the name of the header.

          

        
          - **FieldToMatch** *(dict) --* **[REQUIRED]** 

            Specifies where in a web request to look for cross-site scripting attacks.

            

          
            - **Type** *(string) --* **[REQUIRED]** 

              The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

               

               
              * ``HEADER`` : A specified request header, for example, the value of the ``User-Agent`` or ``Referer`` header. If you choose ``HEADER`` for the type, specify the name of the header in ``Data`` . 
               
              * ``METHOD`` : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: ``DELETE`` , ``GET`` , ``HEAD`` , ``OPTIONS`` , ``PATCH`` , ``POST`` , and ``PUT`` . 
               
              * ``QUERY_STRING`` : A query string, which is the part of a URL that appears after a ``?`` character, if any. 
               
              * ``URI`` : The part of a web request that identifies a resource, for example, ``/images/daily-ad.jpg`` . 
               
              * ``BODY`` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first ``8192`` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .  
               

              

            
            - **Data** *(string) --* 

              When the value of ``Type`` is ``HEADER`` , enter the name of the header that you want AWS WAF to search, for example, ``User-Agent`` or ``Referer`` . If the value of ``Type`` is any other value, omit ``Data`` .

               

              The name of the header is not case sensitive.

              

            
          
          - **TextTransformation** *(string) --* **[REQUIRED]** 

            Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on ``FieldToMatch`` before inspecting a request for a match.

             

             **CMD_LINE**  

             

            When you're concerned that attackers are injecting an operating system commandline command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

             

             
            * Delete the following characters: \ " ' ^ 
             
            * Delete spaces before the following characters: / ( 
             
            * Replace the following characters with a space: , ; 
             
            * Replace multiple spaces with one space 
             
            * Convert uppercase letters (A-Z) to lowercase (a-z) 
             

             

             **COMPRESS_WHITE_SPACE**  

             

            Use this option to replace the following characters with a space character (decimal 32):

             

             
            * \f, formfeed, decimal 12 
             
            * \t, tab, decimal 9 
             
            * \n, newline, decimal 10 
             
            * \r, carriage return, decimal 13 
             
            * \v, vertical tab, decimal 11 
             
            * non-breaking space, decimal 160 
             

             

             ``COMPRESS_WHITE_SPACE`` also replaces multiple spaces with one space.

             

             **HTML_ENTITY_DECODE**  

             

            Use this option to replace HTML-encoded characters with unencoded characters. ``HTML_ENTITY_DECODE`` performs the following operations:

             

             
            * Replaces ``(ampersand)quot;`` with ``"``   
             
            * Replaces ``(ampersand)nbsp;`` with a non-breaking space, decimal 160 
             
            * Replaces ``(ampersand)lt;`` with a "less than" symbol 
             
            * Replaces ``(ampersand)gt;`` with ``>``   
             
            * Replaces characters that are represented in hexadecimal format, ``(ampersand)#xhhhh;`` , with the corresponding characters 
             
            * Replaces characters that are represented in decimal format, ``(ampersand)#nnnn;`` , with the corresponding characters 
             

             

             **LOWERCASE**  

             

            Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

             

             **URL_DECODE**  

             

            Use this option to decode a URL-encoded value.

             

             **NONE**  

             

            Specify ``NONE`` if you don't want to perform any text transformations.

            

          
        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ChangeToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 

        The response to an  UpdateXssMatchSets request.

        
        

        - **ChangeToken** *(string) --* 

          The ``ChangeToken`` that you used to submit the ``UpdateXssMatchSet`` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

          
    

    **Examples** 

    The following example deletes an XssMatchTuple object (filters) in an XssMatchSet with the ID example1ds3t-46da-4fdb-b8d5-abc321j569j5.
    ::

      response = client.update_xss_match_set(
          ChangeToken='abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          Updates=[
              {
                  'Action': 'DELETE',
                  'XssMatchTuple': {
                      'FieldToMatch': {
                          'Type': 'QUERY_STRING',
                      },
                      'TextTransformation': 'URL_DECODE',
                  },
              },
          ],
          XssMatchSetId='example1ds3t-46da-4fdb-b8d5-abc321j569j5',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'ChangeToken': 'abcd12f2-46da-4fdb-b8d5-fbd4c466928f',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

==========
Paginators
==========


The available paginators are:
