

***
ACM
***

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: ACM.Client

  A low-level client representing AWS Certificate Manager (ACM)::

    
    import boto3
    
    client = boto3.client('acm')

  
  These are the available methods:
  
  *   :py:meth:`~ACM.Client.add_tags_to_certificate`

  
  *   :py:meth:`~ACM.Client.can_paginate`

  
  *   :py:meth:`~ACM.Client.delete_certificate`

  
  *   :py:meth:`~ACM.Client.describe_certificate`

  
  *   :py:meth:`~ACM.Client.generate_presigned_url`

  
  *   :py:meth:`~ACM.Client.get_certificate`

  
  *   :py:meth:`~ACM.Client.get_paginator`

  
  *   :py:meth:`~ACM.Client.get_waiter`

  
  *   :py:meth:`~ACM.Client.import_certificate`

  
  *   :py:meth:`~ACM.Client.list_certificates`

  
  *   :py:meth:`~ACM.Client.list_tags_for_certificate`

  
  *   :py:meth:`~ACM.Client.remove_tags_from_certificate`

  
  *   :py:meth:`~ACM.Client.request_certificate`

  
  *   :py:meth:`~ACM.Client.resend_validation_email`

  

  .. py:method:: add_tags_to_certificate(**kwargs)

    

    Adds one or more tags to an ACM Certificate. Tags are labels that you can use to identify and organize your AWS resources. Each tag consists of a ``key`` and an optional ``value`` . You specify the certificate on input by its Amazon Resource Name (ARN). You specify the tag by using a key-value pair. 

     

    You can apply a tag to just one certificate if you want to identify a specific characteristic of that certificate, or you can apply the same tag to multiple certificates if you want to filter for a common relationship among those certificates. Similarly, you can apply the same tag to multiple resources if you want to specify a relationship among those resources. For example, you can add the same tag to an ACM Certificate and an Elastic Load Balancing load balancer to indicate that they are both used by the same website. For more information, see `Tagging ACM Certificates <http://docs.aws.amazon.com/acm/latest/userguide/tags.html>`__ . 

     

    To remove one or more tags, use the  RemoveTagsFromCertificate action. To view all of the tags that have been applied to the certificate, use the  ListTagsForCertificate action. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/AddTagsToCertificate>`_    


    **Request Syntax** 
    ::

      response = client.add_tags_to_certificate(
          CertificateArn='string',
          Tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type CertificateArn: string
    :param CertificateArn: **[REQUIRED]** 

      String that contains the ARN of the ACM Certificate to which the tag is to be applied. This must be of the form:

       

       ``arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012``  

       

      For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ . 

      

    
    :type Tags: list
    :param Tags: **[REQUIRED]** 

      The key-value pair that defines the tag. The tag value is optional.

      

    
      - *(dict) --* 

        A key-value pair that identifies or specifies metadata about an ACM resource.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The key of the tag.

          

        
        - **Value** *(string) --* 

          The value of the tag.

          

        
      
  
    
    :returns: None

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


  .. py:method:: delete_certificate(**kwargs)

    

    Deletes a certificate and its associated private key. If this action succeeds, the certificate no longer appears in the list that can be displayed by calling the  ListCertificates action or be retrieved by calling the  GetCertificate action. The certificate will not be available for use by AWS services integrated with ACM. 

     

    .. note::

       

      You cannot delete an ACM Certificate that is being used by another AWS service. To delete a certificate that is in use, the certificate association must first be removed.

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/DeleteCertificate>`_    


    **Request Syntax** 
    ::

      response = client.delete_certificate(
          CertificateArn='string'
      )
    :type CertificateArn: string
    :param CertificateArn: **[REQUIRED]** 

      String that contains the ARN of the ACM Certificate to be deleted. This must be of the form:

       

       ``arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012``  

       

      For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      

    
    
    :returns: None

  .. py:method:: describe_certificate(**kwargs)

    

    Returns detailed metadata about the specified ACM Certificate.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/DescribeCertificate>`_    


    **Request Syntax** 
    ::

      response = client.describe_certificate(
          CertificateArn='string'
      )
    :type CertificateArn: string
    :param CertificateArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the ACM Certificate. The ARN must have the following form:

       

       ``arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012``  

       

      For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Certificate': {
                'CertificateArn': 'string',
                'DomainName': 'string',
                'SubjectAlternativeNames': [
                    'string',
                ],
                'DomainValidationOptions': [
                    {
                        'DomainName': 'string',
                        'ValidationEmails': [
                            'string',
                        ],
                        'ValidationDomain': 'string',
                        'ValidationStatus': 'PENDING_VALIDATION'|'SUCCESS'|'FAILED',
                        'ResourceRecord': {
                            'Name': 'string',
                            'Type': 'CNAME',
                            'Value': 'string'
                        },
                        'ValidationMethod': 'EMAIL'|'DNS'
                    },
                ],
                'Serial': 'string',
                'Subject': 'string',
                'Issuer': 'string',
                'CreatedAt': datetime(2015, 1, 1),
                'IssuedAt': datetime(2015, 1, 1),
                'ImportedAt': datetime(2015, 1, 1),
                'Status': 'PENDING_VALIDATION'|'ISSUED'|'INACTIVE'|'EXPIRED'|'VALIDATION_TIMED_OUT'|'REVOKED'|'FAILED',
                'RevokedAt': datetime(2015, 1, 1),
                'RevocationReason': 'UNSPECIFIED'|'KEY_COMPROMISE'|'CA_COMPROMISE'|'AFFILIATION_CHANGED'|'SUPERCEDED'|'CESSATION_OF_OPERATION'|'CERTIFICATE_HOLD'|'REMOVE_FROM_CRL'|'PRIVILEGE_WITHDRAWN'|'A_A_COMPROMISE',
                'NotBefore': datetime(2015, 1, 1),
                'NotAfter': datetime(2015, 1, 1),
                'KeyAlgorithm': 'RSA_2048'|'RSA_1024'|'RSA_4096'|'EC_prime256v1'|'EC_secp384r1'|'EC_secp521r1',
                'SignatureAlgorithm': 'string',
                'InUseBy': [
                    'string',
                ],
                'FailureReason': 'NO_AVAILABLE_CONTACTS'|'ADDITIONAL_VERIFICATION_REQUIRED'|'DOMAIN_NOT_ALLOWED'|'INVALID_PUBLIC_DOMAIN'|'CAA_ERROR'|'OTHER',
                'Type': 'IMPORTED'|'AMAZON_ISSUED',
                'RenewalSummary': {
                    'RenewalStatus': 'PENDING_AUTO_RENEWAL'|'PENDING_VALIDATION'|'SUCCESS'|'FAILED',
                    'DomainValidationOptions': [
                        {
                            'DomainName': 'string',
                            'ValidationEmails': [
                                'string',
                            ],
                            'ValidationDomain': 'string',
                            'ValidationStatus': 'PENDING_VALIDATION'|'SUCCESS'|'FAILED',
                            'ResourceRecord': {
                                'Name': 'string',
                                'Type': 'CNAME',
                                'Value': 'string'
                            },
                            'ValidationMethod': 'EMAIL'|'DNS'
                        },
                    ]
                },
                'KeyUsages': [
                    {
                        'Name': 'DIGITAL_SIGNATURE'|'NON_REPUDIATION'|'KEY_ENCIPHERMENT'|'DATA_ENCIPHERMENT'|'KEY_AGREEMENT'|'CERTIFICATE_SIGNING'|'CRL_SIGNING'|'ENCIPHER_ONLY'|'DECIPHER_ONLY'|'ANY'|'CUSTOM'
                    },
                ],
                'ExtendedKeyUsages': [
                    {
                        'Name': 'TLS_WEB_SERVER_AUTHENTICATION'|'TLS_WEB_CLIENT_AUTHENTICATION'|'CODE_SIGNING'|'EMAIL_PROTECTION'|'TIME_STAMPING'|'OCSP_SIGNING'|'IPSEC_END_SYSTEM'|'IPSEC_TUNNEL'|'IPSEC_USER'|'ANY'|'NONE'|'CUSTOM',
                        'OID': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Certificate** *(dict) --* 

          Metadata about an ACM certificate.

          
          

          - **CertificateArn** *(string) --* 

            The Amazon Resource Name (ARN) of the certificate. For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the *AWS General Reference* .

            
          

          - **DomainName** *(string) --* 

            The fully qualified domain name for the certificate, such as www.example.com or example.com.

            
          

          - **SubjectAlternativeNames** *(list) --* 

            One or more domain names (subject alternative names) included in the certificate. This list contains the domain names that are bound to the public key that is contained in the certificate. The subject alternative names include the canonical domain name (CN) of the certificate and additional domain names that can be used to connect to the website. 

            
            

            - *(string) --* 
        
          

          - **DomainValidationOptions** *(list) --* 

            Contains information about the initial validation of each domain name that occurs as a result of the  RequestCertificate request. This field exists only when the certificate type is ``AMAZON_ISSUED`` . 

            
            

            - *(dict) --* 

              Contains information about the validation of each domain name in the certificate.

              
              

              - **DomainName** *(string) --* 

                A fully qualified domain name (FQDN) in the certificate. For example, ``www.example.com`` or ``example.com`` . 

                
              

              - **ValidationEmails** *(list) --* 

                A list of email addresses that ACM used to send domain validation emails.

                
                

                - *(string) --* 
            
              

              - **ValidationDomain** *(string) --* 

                The domain name that ACM used to send domain validation emails.

                
              

              - **ValidationStatus** *(string) --* 

                The validation status of the domain name. This can be one of the following values:

                 

                 
                * ``PENDING_VALIDATION``   
                 
                * ```` SUCCESS 
                 
                * ```` FAILED 
                 

                
              

              - **ResourceRecord** *(dict) --* 

                Contains the CNAME record that you add to your DNS database for domain validation. For more information, see `Use DNS to Validate Domain Ownership <http://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html>`__ .

                
                

                - **Name** *(string) --* 

                  The name of the DNS record to create in your domain. This is supplied by ACM.

                  
                

                - **Type** *(string) --* 

                  The type of DNS record. Currently this can be ``CNAME`` .

                  
                

                - **Value** *(string) --* 

                  The value of the CNAME record to add to your DNS database. This is supplied by ACM.

                  
            
              

              - **ValidationMethod** *(string) --* 

                Specifies the domain validation method.

                
          
        
          

          - **Serial** *(string) --* 

            The serial number of the certificate.

            
          

          - **Subject** *(string) --* 

            The name of the entity that is associated with the public key contained in the certificate.

            
          

          - **Issuer** *(string) --* 

            The name of the certificate authority that issued and signed the certificate.

            
          

          - **CreatedAt** *(datetime) --* 

            The time at which the certificate was requested. This value exists only when the certificate type is ``AMAZON_ISSUED`` . 

            
          

          - **IssuedAt** *(datetime) --* 

            The time at which the certificate was issued. This value exists only when the certificate type is ``AMAZON_ISSUED`` . 

            
          

          - **ImportedAt** *(datetime) --* 

            The date and time at which the certificate was imported. This value exists only when the certificate type is ``IMPORTED`` . 

            
          

          - **Status** *(string) --* 

            The status of the certificate.

            
          

          - **RevokedAt** *(datetime) --* 

            The time at which the certificate was revoked. This value exists only when the certificate status is ``REVOKED`` . 

            
          

          - **RevocationReason** *(string) --* 

            The reason the certificate was revoked. This value exists only when the certificate status is ``REVOKED`` . 

            
          

          - **NotBefore** *(datetime) --* 

            The time before which the certificate is not valid.

            
          

          - **NotAfter** *(datetime) --* 

            The time after which the certificate is not valid.

            
          

          - **KeyAlgorithm** *(string) --* 

            The algorithm that was used to generate the public-private key pair.

            
          

          - **SignatureAlgorithm** *(string) --* 

            The algorithm that was used to sign the certificate.

            
          

          - **InUseBy** *(list) --* 

            A list of ARNs for the AWS resources that are using the certificate. A certificate can be used by multiple AWS resources. 

            
            

            - *(string) --* 
        
          

          - **FailureReason** *(string) --* 

            The reason the certificate request failed. This value exists only when the certificate status is ``FAILED`` . For more information, see `Certificate Request Failed <http://docs.aws.amazon.com/acm/latest/userguide/troubleshooting.html#troubleshooting-failed>`__ in the *AWS Certificate Manager User Guide* . 

            
          

          - **Type** *(string) --* 

            The source of the certificate. For certificates provided by ACM, this value is ``AMAZON_ISSUED`` . For certificates that you imported with  ImportCertificate , this value is ``IMPORTED`` . ACM does not provide `managed renewal <http://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html>`__ for imported certificates. For more information about the differences between certificates that you import and those that ACM provides, see `Importing Certificates <http://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html>`__ in the *AWS Certificate Manager User Guide* . 

            
          

          - **RenewalSummary** *(dict) --* 

            Contains information about the status of ACM's `managed renewal <http://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html>`__ for the certificate. This field exists only when the certificate type is ``AMAZON_ISSUED`` .

            
            

            - **RenewalStatus** *(string) --* 

              The status of ACM's `managed renewal <http://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html>`__ of the certificate.

              
            

            - **DomainValidationOptions** *(list) --* 

              Contains information about the validation of each domain name in the certificate, as it pertains to ACM's `managed renewal <http://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html>`__ . This is different from the initial validation that occurs as a result of the  RequestCertificate request. This field exists only when the certificate type is ``AMAZON_ISSUED`` .

              
              

              - *(dict) --* 

                Contains information about the validation of each domain name in the certificate.

                
                

                - **DomainName** *(string) --* 

                  A fully qualified domain name (FQDN) in the certificate. For example, ``www.example.com`` or ``example.com`` . 

                  
                

                - **ValidationEmails** *(list) --* 

                  A list of email addresses that ACM used to send domain validation emails.

                  
                  

                  - *(string) --* 
              
                

                - **ValidationDomain** *(string) --* 

                  The domain name that ACM used to send domain validation emails.

                  
                

                - **ValidationStatus** *(string) --* 

                  The validation status of the domain name. This can be one of the following values:

                   

                   
                  * ``PENDING_VALIDATION``   
                   
                  * ```` SUCCESS 
                   
                  * ```` FAILED 
                   

                  
                

                - **ResourceRecord** *(dict) --* 

                  Contains the CNAME record that you add to your DNS database for domain validation. For more information, see `Use DNS to Validate Domain Ownership <http://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html>`__ .

                  
                  

                  - **Name** *(string) --* 

                    The name of the DNS record to create in your domain. This is supplied by ACM.

                    
                  

                  - **Type** *(string) --* 

                    The type of DNS record. Currently this can be ``CNAME`` .

                    
                  

                  - **Value** *(string) --* 

                    The value of the CNAME record to add to your DNS database. This is supplied by ACM.

                    
              
                

                - **ValidationMethod** *(string) --* 

                  Specifies the domain validation method.

                  
            
          
        
          

          - **KeyUsages** *(list) --* 

            A list of Key Usage X.509 v3 extension objects. Each object is a string value that identifies the purpose of the public key contained in the certificate. Possible extension values include DIGITAL_SIGNATURE, KEY_ENCHIPHERMENT, NON_REPUDIATION, and more.

            
            

            - *(dict) --* 

              The Key Usage X.509 v3 extension defines the purpose of the public key contained in the certificate.

              
              

              - **Name** *(string) --* 

                A string value that contains a Key Usage extension name.

                
          
        
          

          - **ExtendedKeyUsages** *(list) --* 

            Contains a list of Extended Key Usage X.509 v3 extension objects. Each object specifies a purpose for which the certificate public key can be used and consists of a name and an object identifier (OID). 

            
            

            - *(dict) --* 

              The Extended Key Usage X.509 v3 extension defines one or more purposes for which the public key can be used. This is in addition to or in place of the basic purposes specified by the Key Usage extension. 

              
              

              - **Name** *(string) --* 

                The name of an Extended Key Usage value.

                
              

              - **OID** *(string) --* 

                An object identifier (OID) for the extension value. OIDs are strings of numbers separated by periods. The following OIDs are defined in RFC 3280 and RFC 5280. 

                 

                 
                * ``1.3.6.1.5.5.7.3.1 (TLS_WEB_SERVER_AUTHENTICATION)``   
                 
                * ``1.3.6.1.5.5.7.3.2 (TLS_WEB_CLIENT_AUTHENTICATION)``   
                 
                * ``1.3.6.1.5.5.7.3.3 (CODE_SIGNING)``   
                 
                * ``1.3.6.1.5.5.7.3.4 (EMAIL_PROTECTION)``   
                 
                * ``1.3.6.1.5.5.7.3.8 (TIME_STAMPING)``   
                 
                * ``1.3.6.1.5.5.7.3.9 (OCSP_SIGNING)``   
                 
                * ``1.3.6.1.5.5.7.3.5 (IPSEC_END_SYSTEM)``   
                 
                * ``1.3.6.1.5.5.7.3.6 (IPSEC_TUNNEL)``   
                 
                * ``1.3.6.1.5.5.7.3.7 (IPSEC_USER)``   
                 

                
          
        
      
    

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


  .. py:method:: get_certificate(**kwargs)

    

    Retrieves a certificate specified by an ARN and its certificate chain . The chain is an ordered list of certificates that contains the end entity ertificate, intermediate certificates of subordinate CAs, and the root certificate in that order. The certificate and certificate chain are base64 encoded. If you want to decode the certificate to see the individual fields, you can use OpenSSL.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/GetCertificate>`_    


    **Request Syntax** 
    ::

      response = client.get_certificate(
          CertificateArn='string'
      )
    :type CertificateArn: string
    :param CertificateArn: **[REQUIRED]** 

      String that contains a certificate ARN in the following format:

       

       ``arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012``  

       

      For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Certificate': 'string',
            'CertificateChain': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Certificate** *(string) --* 

          String that contains the ACM Certificate represented by the ARN specified at input.

          
        

        - **CertificateChain** *(string) --* 

          The certificate chain that contains the root certificate issued by the certificate authority (CA).

          
    

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

        


  .. py:method:: import_certificate(**kwargs)

    

    Imports a certificate into AWS Certificate Manager (ACM) to use with services that are integrated with ACM. For more information, see `Integrated Services <http://docs.aws.amazon.com/acm/latest/userguide/acm-services.html>`__ . 

     

    .. note::

       

      ACM does not provide `managed renewal <http://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html>`__ for certificates that you import.

       

     

    For more information about importing certificates into ACM, including the differences between certificates that you import and those that ACM provides, see `Importing Certificates <http://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html>`__ in the *AWS Certificate Manager User Guide* . 

     

    In general, you can import almost any valid certificate. However, services integrated with ACM allow only certificate types they support to be associated with their resources. The following guidelines are also important:

     

     
    * You must enter the private key that matches the certificate you are importing. 
     
    * The private key must be unencrypted. You cannot import a private key that is protected by a password or a passphrase. 
     
    * If the certificate you are importing is not self-signed, you must enter its certificate chain. 
     
    * If a certificate chain is included, the issuer must be the subject of one of the certificates in the chain. 
     
    * The certificate, private key, and certificate chain must be PEM-encoded. 
     
    * The current time must be between the ``Not Before`` and ``Not After`` certificate fields. 
     
    * The ``Issuer`` field must not be empty. 
     
    * The OCSP authority URL must not exceed 1000 characters. 
     
    * To import a new certificate, omit the ``CertificateArn`` field. Include this field only when you want to replace a previously imported certificate. 
     
    * When you import a certificate by using the CLI or one of the SDKs, you must specify the certificate, certificate chain, and private key parameters as file names preceded by ``file://`` . For example, you can specify a certificate saved in the ``C:\temp`` folder as ``C:\temp\certificate_to_import.pem`` . If you are making an HTTP or HTTPS Query request, include these parameters as BLOBs.  
     

     

    This operation returns the `Amazon Resource Name (ARN) <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ of the imported certificate.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/ImportCertificate>`_    


    **Request Syntax** 
    ::

      response = client.import_certificate(
          CertificateArn='string',
          Certificate=b'bytes',
          PrivateKey=b'bytes',
          CertificateChain=b'bytes'
      )
    :type CertificateArn: string
    :param CertificateArn: 

      The `Amazon Resource Name (ARN) <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ of an imported certificate to replace. To import a new certificate, omit this field. 

      

    
    :type Certificate: bytes
    :param Certificate: **[REQUIRED]** 

      The certificate to import.

      

    
    :type PrivateKey: bytes
    :param PrivateKey: **[REQUIRED]** 

      The private key that matches the public key in the certificate.

      

    
    :type CertificateChain: bytes
    :param CertificateChain: 

      The PEM encoded certificate chain.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CertificateArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CertificateArn** *(string) --* 

          The `Amazon Resource Name (ARN) <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ of the imported certificate.

          
    

  .. py:method:: list_certificates(**kwargs)

    

    Retrieves a list of certificate ARNs and domain names. You can request that only certificates that match a specific status be listed. You can also filter by specific attributes of the certificate. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/ListCertificates>`_    


    **Request Syntax** 
    ::

      response = client.list_certificates(
          CertificateStatuses=[
              'PENDING_VALIDATION'|'ISSUED'|'INACTIVE'|'EXPIRED'|'VALIDATION_TIMED_OUT'|'REVOKED'|'FAILED',
          ],
          Includes={
              'extendedKeyUsage': [
                  'TLS_WEB_SERVER_AUTHENTICATION'|'TLS_WEB_CLIENT_AUTHENTICATION'|'CODE_SIGNING'|'EMAIL_PROTECTION'|'TIME_STAMPING'|'OCSP_SIGNING'|'IPSEC_END_SYSTEM'|'IPSEC_TUNNEL'|'IPSEC_USER'|'ANY'|'NONE'|'CUSTOM',
              ],
              'keyUsage': [
                  'DIGITAL_SIGNATURE'|'NON_REPUDIATION'|'KEY_ENCIPHERMENT'|'DATA_ENCIPHERMENT'|'KEY_AGREEMENT'|'CERTIFICATE_SIGNING'|'CRL_SIGNING'|'ENCIPHER_ONLY'|'DECIPHER_ONLY'|'ANY'|'CUSTOM',
              ],
              'keyTypes': [
                  'RSA_2048'|'RSA_1024'|'RSA_4096'|'EC_prime256v1'|'EC_secp384r1'|'EC_secp521r1',
              ]
          },
          NextToken='string',
          MaxItems=123
      )
    :type CertificateStatuses: list
    :param CertificateStatuses: 

      Filter the certificate list by status value.

      

    
      - *(string) --* 

      
  
    :type Includes: dict
    :param Includes: 

      Filter the certificate list by one or more of the following values. For more information, see the  Filters structure.

       

       
      * extendedKeyUsage 
       
      * keyUsage 
       
      * keyTypes 
       

      

    
      - **extendedKeyUsage** *(list) --* 

        Specify one or more  ExtendedKeyUsage extension values.

        

      
        - *(string) --* 

        
    
      - **keyUsage** *(list) --* 

        Specify one or more  KeyUsage extension values.

        

      
        - *(string) --* 

        
    
      - **keyTypes** *(list) --* 

        Specify one or more algorithms that can be used to generate key pairs.

        

      
        - *(string) --* 

        
    
    
    :type NextToken: string
    :param NextToken: 

      Use this parameter only when paginating results and only in a subsequent request after you receive a response with truncated results. Set it to the value of ``NextToken`` from the response you just received.

      

    
    :type MaxItems: integer
    :param MaxItems: 

      Use this parameter when paginating results to specify the maximum number of items to return in the response. If additional items exist beyond the number you specify, the ``NextToken`` element is sent in the response. Use this ``NextToken`` value in a subsequent request to retrieve additional items.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextToken': 'string',
            'CertificateSummaryList': [
                {
                    'CertificateArn': 'string',
                    'DomainName': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NextToken** *(string) --* 

          When the list is truncated, this value is present and contains the value to use for the ``NextToken`` parameter in a subsequent pagination request.

          
        

        - **CertificateSummaryList** *(list) --* 

          A list of ACM Certificates.

          
          

          - *(dict) --* 

            This structure is returned in the response object of  ListCertificates action. 

            
            

            - **CertificateArn** *(string) --* 

              Amazon Resource Name (ARN) of the certificate. This is of the form:

               

               ``arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012``  

               

              For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ . 

              
            

            - **DomainName** *(string) --* 

              Fully qualified domain name (FQDN), such as www.example.com or example.com, for the certificate.

              
        
      
    

  .. py:method:: list_tags_for_certificate(**kwargs)

    

    Lists the tags that have been applied to the ACM Certificate. Use the certificate's Amazon Resource Name (ARN) to specify the certificate. To add a tag to an ACM Certificate, use the  AddTagsToCertificate action. To delete a tag, use the  RemoveTagsFromCertificate action. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/ListTagsForCertificate>`_    


    **Request Syntax** 
    ::

      response = client.list_tags_for_certificate(
          CertificateArn='string'
      )
    :type CertificateArn: string
    :param CertificateArn: **[REQUIRED]** 

      String that contains the ARN of the ACM Certificate for which you want to list the tags. This must have the following form:

       

       ``arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012``  

       

      For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ . 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Tags** *(list) --* 

          The key-value pairs that define the applied tags.

          
          

          - *(dict) --* 

            A key-value pair that identifies or specifies metadata about an ACM resource.

            
            

            - **Key** *(string) --* 

              The key of the tag.

              
            

            - **Value** *(string) --* 

              The value of the tag.

              
        
      
    

  .. py:method:: remove_tags_from_certificate(**kwargs)

    

    Remove one or more tags from an ACM Certificate. A tag consists of a key-value pair. If you do not specify the value portion of the tag when calling this function, the tag will be removed regardless of value. If you specify a value, the tag is removed only if it is associated with the specified value. 

     

    To add tags to a certificate, use the  AddTagsToCertificate action. To view all of the tags that have been applied to a specific ACM Certificate, use the  ListTagsForCertificate action. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/RemoveTagsFromCertificate>`_    


    **Request Syntax** 
    ::

      response = client.remove_tags_from_certificate(
          CertificateArn='string',
          Tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type CertificateArn: string
    :param CertificateArn: **[REQUIRED]** 

      String that contains the ARN of the ACM Certificate with one or more tags that you want to remove. This must be of the form:

       

       ``arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012``  

       

      For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ . 

      

    
    :type Tags: list
    :param Tags: **[REQUIRED]** 

      The key-value pair that defines the tag to remove.

      

    
      - *(dict) --* 

        A key-value pair that identifies or specifies metadata about an ACM resource.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The key of the tag.

          

        
        - **Value** *(string) --* 

          The value of the tag.

          

        
      
  
    
    :returns: None

  .. py:method:: request_certificate(**kwargs)

    

    Requests an ACM Certificate for use with other AWS services. To request an ACM Certificate, you must specify the fully qualified domain name (FQDN) for your site in the ``DomainName`` parameter. You can also specify additional FQDNs in the ``SubjectAlternativeNames`` parameter if users can reach your site by using other names. 

     

    For each domain name you specify, email is sent to the domain owner to request approval to issue the certificate. Email is sent to three registered contact addresses in the WHOIS database and to five common system administration addresses formed from the ``DomainName`` you enter or the optional ``ValidationDomain`` parameter. For more information, see `Validate Domain Ownership <http://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate.html>`__ . 

     

    After receiving approval from the domain owner, the ACM Certificate is issued. For more information, see the `AWS Certificate Manager User Guide <http://docs.aws.amazon.com/acm/latest/userguide/>`__ . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/RequestCertificate>`_    


    **Request Syntax** 
    ::

      response = client.request_certificate(
          DomainName='string',
          ValidationMethod='EMAIL'|'DNS',
          SubjectAlternativeNames=[
              'string',
          ],
          IdempotencyToken='string',
          DomainValidationOptions=[
              {
                  'DomainName': 'string',
                  'ValidationDomain': 'string'
              },
          ]
      )
    :type DomainName: string
    :param DomainName: **[REQUIRED]** 

      Fully qualified domain name (FQDN), such as www.example.com, of the site that you want to secure with an ACM Certificate. Use an asterisk (*) to create a wildcard certificate that protects several sites in the same domain. For example, *.example.com protects www.example.com, site.example.com, and images.example.com. 

       

      The first domain name you enter cannot exceed 63 octets, including periods. Each subsequent Subject Alternative Name (SAN), however, can be up to 253 octets in length. 

      

    
    :type ValidationMethod: string
    :param ValidationMethod: 

      The method you want to use to validate your domain.

      

    
    :type SubjectAlternativeNames: list
    :param SubjectAlternativeNames: 

      Additional FQDNs to be included in the Subject Alternative Name extension of the ACM Certificate. For example, add the name www.example.net to a certificate for which the ``DomainName`` field is www.example.com if users can reach your site by using either name. The maximum number of domain names that you can add to an ACM Certificate is 100. However, the initial limit is 10 domain names. If you need more than 10 names, you must request a limit increase. For more information, see `Limits <http://docs.aws.amazon.com/acm/latest/userguide/acm-limits.html>`__ .

       

      The maximum length of a SAN DNS name is 253 octets. The name is made up of multiple labels separated by periods. No label can be longer than 63 octets. Consider the following examples: 

       

       
      * ``(63 octets).(63 octets).(63 octets).(61 octets)`` is legal because the total length is 253 octets (63+1+63+1+63+1+61) and no label exceeds 63 octets. 
       
      * ``(64 octets).(63 octets).(63 octets).(61 octets)`` is not legal because the total length exceeds 253 octets (64+1+63+1+63+1+61) and the first label exceeds 63 octets. 
       
      * ``(63 octets).(63 octets).(63 octets).(62 octets)`` is not legal because the total length of the DNS name (63+1+63+1+63+1+62) exceeds 253 octets. 
       

      

    
      - *(string) --* 

      
  
    :type IdempotencyToken: string
    :param IdempotencyToken: 

      Customer chosen string that can be used to distinguish between calls to ``RequestCertificate`` . Idempotency tokens time out after one hour. Therefore, if you call ``RequestCertificate`` multiple times with the same idempotency token within one hour, ACM recognizes that you are requesting only one certificate and will issue only one. If you change the idempotency token for each call, ACM recognizes that you are requesting multiple certificates.

      

    
    :type DomainValidationOptions: list
    :param DomainValidationOptions: 

      The domain name that you want ACM to use to send you emails so taht your can validate domain ownership.

      

    
      - *(dict) --* 

        Contains information about the domain names that you want ACM to use to send you emails that enable you to validate domain ownership.

        

      
        - **DomainName** *(string) --* **[REQUIRED]** 

          A fully qualified domain name (FQDN) in the certificate request.

          

        
        - **ValidationDomain** *(string) --* **[REQUIRED]** 

          The domain name that you want ACM to use to send you validation emails. This domain name is the suffix of the email addresses that you want ACM to use. This must be the same as the ``DomainName`` value or a superdomain of the ``DomainName`` value. For example, if you request a certificate for ``testing.example.com`` , you can specify ``example.com`` for this value. In that case, ACM sends domain validation emails to the following five addresses:

           

           
          * admin@example.com 
           
          * administrator@example.com 
           
          * hostmaster@example.com 
           
          * postmaster@example.com 
           
          * webmaster@example.com 
           

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CertificateArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CertificateArn** *(string) --* 

          String that contains the ARN of the issued certificate. This must be of the form:

           

           ``arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012``  

          
    

  .. py:method:: resend_validation_email(**kwargs)

    

    Resends the email that requests domain ownership validation. The domain owner or an authorized representative must approve the ACM Certificate before it can be issued. The certificate can be approved by clicking a link in the mail to navigate to the Amazon certificate approval website and then clicking **I Approve** . However, the validation email can be blocked by spam filters. Therefore, if you do not receive the original mail, you can request that the mail be resent within 72 hours of requesting the ACM Certificate. If more than 72 hours have elapsed since your original request or since your last attempt to resend validation mail, you must request a new certificate. For more information about setting up your contact email addresses, see `Configure Email for your Domain <http://docs.aws.amazon.com/acm/latest/userguide/setup-email.html>`__ . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/ResendValidationEmail>`_    


    **Request Syntax** 
    ::

      response = client.resend_validation_email(
          CertificateArn='string',
          Domain='string',
          ValidationDomain='string'
      )
    :type CertificateArn: string
    :param CertificateArn: **[REQUIRED]** 

      String that contains the ARN of the requested certificate. The certificate ARN is generated and returned by the  RequestCertificate action as soon as the request is made. By default, using this parameter causes email to be sent to all top-level domains you specified in the certificate request. The ARN must be of the form: 

       

       ``arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012``  

      

    
    :type Domain: string
    :param Domain: **[REQUIRED]** 

      The fully qualified domain name (FQDN) of the certificate that needs to be validated.

      

    
    :type ValidationDomain: string
    :param ValidationDomain: **[REQUIRED]** 

      The base validation domain that will act as the suffix of the email addresses that are used to send the emails. This must be the same as the ``Domain`` value or a superdomain of the ``Domain`` value. For example, if you requested a certificate for ``site.subdomain.example.com`` and specify a **ValidationDomain** of ``subdomain.example.com`` , ACM sends email to the domain registrant, technical contact, and administrative contact in WHOIS and the following five addresses:

       

       
      * admin@subdomain.example.com 
       
      * administrator@subdomain.example.com 
       
      * hostmaster@subdomain.example.com 
       
      * postmaster@subdomain.example.com 
       
      * webmaster@subdomain.example.com 
       

      

    
    
    :returns: None

==========
Paginators
==========


The available paginators are:

* :py:class:`ACM.Paginator.ListCertificates`



.. py:class:: ACM.Paginator.ListCertificates

  ::

    
    paginator = client.get_paginator('list_certificates')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`ACM.Client.list_certificates`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/ListCertificates>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          CertificateStatuses=[
              'PENDING_VALIDATION'|'ISSUED'|'INACTIVE'|'EXPIRED'|'VALIDATION_TIMED_OUT'|'REVOKED'|'FAILED',
          ],
          Includes={
              'extendedKeyUsage': [
                  'TLS_WEB_SERVER_AUTHENTICATION'|'TLS_WEB_CLIENT_AUTHENTICATION'|'CODE_SIGNING'|'EMAIL_PROTECTION'|'TIME_STAMPING'|'OCSP_SIGNING'|'IPSEC_END_SYSTEM'|'IPSEC_TUNNEL'|'IPSEC_USER'|'ANY'|'NONE'|'CUSTOM',
              ],
              'keyUsage': [
                  'DIGITAL_SIGNATURE'|'NON_REPUDIATION'|'KEY_ENCIPHERMENT'|'DATA_ENCIPHERMENT'|'KEY_AGREEMENT'|'CERTIFICATE_SIGNING'|'CRL_SIGNING'|'ENCIPHER_ONLY'|'DECIPHER_ONLY'|'ANY'|'CUSTOM',
              ],
              'keyTypes': [
                  'RSA_2048'|'RSA_1024'|'RSA_4096'|'EC_prime256v1'|'EC_secp384r1'|'EC_secp521r1',
              ]
          },
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type CertificateStatuses: list
    :param CertificateStatuses: 

      Filter the certificate list by status value.

      

    
      - *(string) --* 

      
  
    :type Includes: dict
    :param Includes: 

      Filter the certificate list by one or more of the following values. For more information, see the  Filters structure.

       

       
      * extendedKeyUsage 
       
      * keyUsage 
       
      * keyTypes 
       

      

    
      - **extendedKeyUsage** *(list) --* 

        Specify one or more  ExtendedKeyUsage extension values.

        

      
        - *(string) --* 

        
    
      - **keyUsage** *(list) --* 

        Specify one or more  KeyUsage extension values.

        

      
        - *(string) --* 

        
    
      - **keyTypes** *(list) --* 

        Specify one or more algorithms that can be used to generate key pairs.

        

      
        - *(string) --* 

        
    
    
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
            'CertificateSummaryList': [
                {
                    'CertificateArn': 'string',
                    'DomainName': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CertificateSummaryList** *(list) --* 

          A list of ACM Certificates.

          
          

          - *(dict) --* 

            This structure is returned in the response object of  ListCertificates action. 

            
            

            - **CertificateArn** *(string) --* 

              Amazon Resource Name (ARN) of the certificate. This is of the form:

               

               ``arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012``  

               

              For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ . 

              
            

            - **DomainName** *(string) --* 

              Fully qualified domain name (FQDN), such as www.example.com or example.com, for the certificate.

              
        
      
    