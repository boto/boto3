

**************
ServiceCatalog
**************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: ServiceCatalog.Client

  A low-level client representing AWS Service Catalog::

    
    import boto3
    
    client = boto3.client('servicecatalog')

  
  These are the available methods:
  
  *   :py:meth:`~ServiceCatalog.Client.accept_portfolio_share`

  
  *   :py:meth:`~ServiceCatalog.Client.associate_principal_with_portfolio`

  
  *   :py:meth:`~ServiceCatalog.Client.associate_product_with_portfolio`

  
  *   :py:meth:`~ServiceCatalog.Client.associate_tag_option_with_resource`

  
  *   :py:meth:`~ServiceCatalog.Client.can_paginate`

  
  *   :py:meth:`~ServiceCatalog.Client.copy_product`

  
  *   :py:meth:`~ServiceCatalog.Client.create_constraint`

  
  *   :py:meth:`~ServiceCatalog.Client.create_portfolio`

  
  *   :py:meth:`~ServiceCatalog.Client.create_portfolio_share`

  
  *   :py:meth:`~ServiceCatalog.Client.create_product`

  
  *   :py:meth:`~ServiceCatalog.Client.create_provisioning_artifact`

  
  *   :py:meth:`~ServiceCatalog.Client.create_tag_option`

  
  *   :py:meth:`~ServiceCatalog.Client.delete_constraint`

  
  *   :py:meth:`~ServiceCatalog.Client.delete_portfolio`

  
  *   :py:meth:`~ServiceCatalog.Client.delete_portfolio_share`

  
  *   :py:meth:`~ServiceCatalog.Client.delete_product`

  
  *   :py:meth:`~ServiceCatalog.Client.delete_provisioning_artifact`

  
  *   :py:meth:`~ServiceCatalog.Client.describe_constraint`

  
  *   :py:meth:`~ServiceCatalog.Client.describe_copy_product_status`

  
  *   :py:meth:`~ServiceCatalog.Client.describe_portfolio`

  
  *   :py:meth:`~ServiceCatalog.Client.describe_product`

  
  *   :py:meth:`~ServiceCatalog.Client.describe_product_as_admin`

  
  *   :py:meth:`~ServiceCatalog.Client.describe_product_view`

  
  *   :py:meth:`~ServiceCatalog.Client.describe_provisioned_product`

  
  *   :py:meth:`~ServiceCatalog.Client.describe_provisioning_artifact`

  
  *   :py:meth:`~ServiceCatalog.Client.describe_provisioning_parameters`

  
  *   :py:meth:`~ServiceCatalog.Client.describe_record`

  
  *   :py:meth:`~ServiceCatalog.Client.describe_tag_option`

  
  *   :py:meth:`~ServiceCatalog.Client.disassociate_principal_from_portfolio`

  
  *   :py:meth:`~ServiceCatalog.Client.disassociate_product_from_portfolio`

  
  *   :py:meth:`~ServiceCatalog.Client.disassociate_tag_option_from_resource`

  
  *   :py:meth:`~ServiceCatalog.Client.generate_presigned_url`

  
  *   :py:meth:`~ServiceCatalog.Client.get_paginator`

  
  *   :py:meth:`~ServiceCatalog.Client.get_waiter`

  
  *   :py:meth:`~ServiceCatalog.Client.list_accepted_portfolio_shares`

  
  *   :py:meth:`~ServiceCatalog.Client.list_constraints_for_portfolio`

  
  *   :py:meth:`~ServiceCatalog.Client.list_launch_paths`

  
  *   :py:meth:`~ServiceCatalog.Client.list_portfolio_access`

  
  *   :py:meth:`~ServiceCatalog.Client.list_portfolios`

  
  *   :py:meth:`~ServiceCatalog.Client.list_portfolios_for_product`

  
  *   :py:meth:`~ServiceCatalog.Client.list_principals_for_portfolio`

  
  *   :py:meth:`~ServiceCatalog.Client.list_provisioning_artifacts`

  
  *   :py:meth:`~ServiceCatalog.Client.list_record_history`

  
  *   :py:meth:`~ServiceCatalog.Client.list_resources_for_tag_option`

  
  *   :py:meth:`~ServiceCatalog.Client.list_tag_options`

  
  *   :py:meth:`~ServiceCatalog.Client.provision_product`

  
  *   :py:meth:`~ServiceCatalog.Client.reject_portfolio_share`

  
  *   :py:meth:`~ServiceCatalog.Client.scan_provisioned_products`

  
  *   :py:meth:`~ServiceCatalog.Client.search_products`

  
  *   :py:meth:`~ServiceCatalog.Client.search_products_as_admin`

  
  *   :py:meth:`~ServiceCatalog.Client.terminate_provisioned_product`

  
  *   :py:meth:`~ServiceCatalog.Client.update_constraint`

  
  *   :py:meth:`~ServiceCatalog.Client.update_portfolio`

  
  *   :py:meth:`~ServiceCatalog.Client.update_product`

  
  *   :py:meth:`~ServiceCatalog.Client.update_provisioned_product`

  
  *   :py:meth:`~ServiceCatalog.Client.update_provisioning_artifact`

  
  *   :py:meth:`~ServiceCatalog.Client.update_tag_option`

  

  .. py:method:: accept_portfolio_share(**kwargs)

    

    Accepts an offer to share the specified portfolio.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/AcceptPortfolioShare>`_    


    **Request Syntax** 
    ::

      response = client.accept_portfolio_share(
          AcceptLanguage='string',
          PortfolioId='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type PortfolioId: string
    :param PortfolioId: **[REQUIRED]** 

      The portfolio identifier.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: associate_principal_with_portfolio(**kwargs)

    

    Associates the specified principal ARN with the specified portfolio.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/AssociatePrincipalWithPortfolio>`_    


    **Request Syntax** 
    ::

      response = client.associate_principal_with_portfolio(
          AcceptLanguage='string',
          PortfolioId='string',
          PrincipalARN='string',
          PrincipalType='IAM'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type PortfolioId: string
    :param PortfolioId: **[REQUIRED]** 

      The portfolio identifier.

      

    
    :type PrincipalARN: string
    :param PrincipalARN: **[REQUIRED]** 

      The ARN of the principal (IAM user, role, or group).

      

    
    :type PrincipalType: string
    :param PrincipalType: **[REQUIRED]** 

      The principal type. The supported value is ``IAM`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: associate_product_with_portfolio(**kwargs)

    

    Associates the specified product with the specified portfolio.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/AssociateProductWithPortfolio>`_    


    **Request Syntax** 
    ::

      response = client.associate_product_with_portfolio(
          AcceptLanguage='string',
          ProductId='string',
          PortfolioId='string',
          SourcePortfolioId='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type ProductId: string
    :param ProductId: **[REQUIRED]** 

      The product identifier.

      

    
    :type PortfolioId: string
    :param PortfolioId: **[REQUIRED]** 

      The portfolio identifier.

      

    
    :type SourcePortfolioId: string
    :param SourcePortfolioId: 

      The identifier of the source portfolio.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: associate_tag_option_with_resource(**kwargs)

    

    Associate the specified TagOption with the specified portfolio or product.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/AssociateTagOptionWithResource>`_    


    **Request Syntax** 
    ::

      response = client.associate_tag_option_with_resource(
          ResourceId='string',
          TagOptionId='string'
      )
    :type ResourceId: string
    :param ResourceId: **[REQUIRED]** 

      The resource identifier.

      

    
    :type TagOptionId: string
    :param TagOptionId: **[REQUIRED]** 

      The TagOption identifier.

      

    
    
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


  .. py:method:: copy_product(**kwargs)

    

    Copies the specified source product to the specified target product or a new product.

     

    You can copy a product to the same account or another account. You can copy a product to the same region or another region.

     

    This operation is performed asynchronously. To track the progress of the operation, use  DescribeCopyProductStatus .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/CopyProduct>`_    


    **Request Syntax** 
    ::

      response = client.copy_product(
          AcceptLanguage='string',
          SourceProductArn='string',
          TargetProductId='string',
          TargetProductName='string',
          SourceProvisioningArtifactIdentifiers=[
              {
                  'string': 'string'
              },
          ],
          CopyOptions=[
              'CopyTags',
          ],
          IdempotencyToken='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type SourceProductArn: string
    :param SourceProductArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the source product.

      

    
    :type TargetProductId: string
    :param TargetProductId: 

      The identifier of the target product. By default, a new product is created.

      

    
    :type TargetProductName: string
    :param TargetProductName: 

      A name for the target product. The default is the name of the source product.

      

    
    :type SourceProvisioningArtifactIdentifiers: list
    :param SourceProvisioningArtifactIdentifiers: 

      The identifiers of the provisioning artifacts (also known as versions) of the product to copy. By default, all provisioning artifacts are copied.

      

    
      - *(dict) --* 

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
  
    :type CopyOptions: list
    :param CopyOptions: 

      The copy options. If the value is ``CopyTags`` , the tags from the source product are copied to the target product.

      

    
      - *(string) --* 

      
  
    :type IdempotencyToken: string
    :param IdempotencyToken: **[REQUIRED]** 

      A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request. 

      This field is autopopulated if not provided.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CopyProductToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CopyProductToken** *(string) --* 

          The token to use to track the progress of the operation.

          
    

  .. py:method:: create_constraint(**kwargs)

    

    Creates a constraint.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/CreateConstraint>`_    


    **Request Syntax** 
    ::

      response = client.create_constraint(
          AcceptLanguage='string',
          PortfolioId='string',
          ProductId='string',
          Parameters='string',
          Type='string',
          Description='string',
          IdempotencyToken='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type PortfolioId: string
    :param PortfolioId: **[REQUIRED]** 

      The portfolio identifier.

      

    
    :type ProductId: string
    :param ProductId: **[REQUIRED]** 

      The product identifier.

      

    
    :type Parameters: string
    :param Parameters: **[REQUIRED]** 

      The constraint parameters, in JSON format. The syntax depends on the constraint type as follows:

        LAUNCH  

      Specify the ``RoleArn`` property as follows:

       

      \"RoleArn\" : \"arn:aws:iam::123456789012:role/LaunchRole\"

        NOTIFICATION  

      Specify the ``NotificationArns`` property as follows:

       

      \"NotificationArns\" : [\"arn:aws:sns:us-east-1:123456789012:Topic\"]

        TEMPLATE  

      Specify the ``Rules`` property. For more information, see `Template Constraint Rules <http://docs.aws.amazon.com/servicecatalog/latest/adminguide/reference-template_constraint_rules.html>`__ .

        

    
    :type Type: string
    :param Type: **[REQUIRED]** 

      The type of constraint.

       

       
      * ``LAUNCH``   
       
      * ``NOTIFICATION``   
       
      * ``TEMPLATE``   
       

      

    
    :type Description: string
    :param Description: 

      The description of the constraint.

      

    
    :type IdempotencyToken: string
    :param IdempotencyToken: **[REQUIRED]** 

      A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.

      This field is autopopulated if not provided.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ConstraintDetail': {
                'ConstraintId': 'string',
                'Type': 'string',
                'Description': 'string',
                'Owner': 'string'
            },
            'ConstraintParameters': 'string',
            'Status': 'AVAILABLE'|'CREATING'|'FAILED'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ConstraintDetail** *(dict) --* 

          Information about the constraint.

          
          

          - **ConstraintId** *(string) --* 

            The identifier of the constraint.

            
          

          - **Type** *(string) --* 

            The type of constraint.

             

             
            * ``LAUNCH``   
             
            * ``NOTIFICATION``   
             
            * ``TEMPLATE``   
             

            
          

          - **Description** *(string) --* 

            The description of the constraint.

            
          

          - **Owner** *(string) --* 

            The owner of the constraint.

            
      
        

        - **ConstraintParameters** *(string) --* 

          The constraint parameters.

          
        

        - **Status** *(string) --* 

          The status of the current request.

          
    

  .. py:method:: create_portfolio(**kwargs)

    

    Creates a portfolio.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/CreatePortfolio>`_    


    **Request Syntax** 
    ::

      response = client.create_portfolio(
          AcceptLanguage='string',
          DisplayName='string',
          Description='string',
          ProviderName='string',
          Tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ],
          IdempotencyToken='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type DisplayName: string
    :param DisplayName: **[REQUIRED]** 

      The name to use for display purposes.

      

    
    :type Description: string
    :param Description: 

      The description of the portfolio.

      

    
    :type ProviderName: string
    :param ProviderName: **[REQUIRED]** 

      The name of the portfolio provider.

      

    
    :type Tags: list
    :param Tags: 

      The tags to associate with the portfolio.

      

    
      - *(dict) --* 

        Information about a tag. A tag is a key-value pair. Tags are entirely discretionary and are propagated to the resources created when provisioning a product.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The tag key.

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          The value for this key.

          

        
      
  
    :type IdempotencyToken: string
    :param IdempotencyToken: **[REQUIRED]** 

      A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.

      This field is autopopulated if not provided.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'PortfolioDetail': {
                'Id': 'string',
                'ARN': 'string',
                'DisplayName': 'string',
                'Description': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'ProviderName': 'string'
            },
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **PortfolioDetail** *(dict) --* 

          Information about the portfolio.

          
          

          - **Id** *(string) --* 

            The portfolio identifier.

            
          

          - **ARN** *(string) --* 

            The ARN assigned to the portfolio.

            
          

          - **DisplayName** *(string) --* 

            The name to use for display purposes.

            
          

          - **Description** *(string) --* 

            The description of the portfolio.

            
          

          - **CreatedTime** *(datetime) --* 

            The UTC timestamp of the creation time.

            
          

          - **ProviderName** *(string) --* 

            The name of the portfolio provider.

            
      
        

        - **Tags** *(list) --* 

          Information about the tags associated with the portfolio.

          
          

          - *(dict) --* 

            Information about a tag. A tag is a key-value pair. Tags are entirely discretionary and are propagated to the resources created when provisioning a product.

            
            

            - **Key** *(string) --* 

              The tag key.

              
            

            - **Value** *(string) --* 

              The value for this key.

              
        
      
    

  .. py:method:: create_portfolio_share(**kwargs)

    

    Shares the specified portfolio with the specified account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/CreatePortfolioShare>`_    


    **Request Syntax** 
    ::

      response = client.create_portfolio_share(
          AcceptLanguage='string',
          PortfolioId='string',
          AccountId='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type PortfolioId: string
    :param PortfolioId: **[REQUIRED]** 

      The portfolio identifier.

      

    
    :type AccountId: string
    :param AccountId: **[REQUIRED]** 

      The AWS account ID.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: create_product(**kwargs)

    

    Creates a product.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/CreateProduct>`_    


    **Request Syntax** 
    ::

      response = client.create_product(
          AcceptLanguage='string',
          Name='string',
          Owner='string',
          Description='string',
          Distributor='string',
          SupportDescription='string',
          SupportEmail='string',
          SupportUrl='string',
          ProductType='CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE',
          Tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ],
          ProvisioningArtifactParameters={
              'Name': 'string',
              'Description': 'string',
              'Info': {
                  'string': 'string'
              },
              'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR'
          },
          IdempotencyToken='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the product.

      

    
    :type Owner: string
    :param Owner: **[REQUIRED]** 

      The owner of the product.

      

    
    :type Description: string
    :param Description: 

      The description of the product.

      

    
    :type Distributor: string
    :param Distributor: 

      The distributor of the product.

      

    
    :type SupportDescription: string
    :param SupportDescription: 

      The support information about the product.

      

    
    :type SupportEmail: string
    :param SupportEmail: 

      The contact email for product support.

      

    
    :type SupportUrl: string
    :param SupportUrl: 

      The contact URL for product support.

      

    
    :type ProductType: string
    :param ProductType: **[REQUIRED]** 

      The type of product.

      

    
    :type Tags: list
    :param Tags: 

      The tags to associate with the product.

      

    
      - *(dict) --* 

        Information about a tag. A tag is a key-value pair. Tags are entirely discretionary and are propagated to the resources created when provisioning a product.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The tag key.

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          The value for this key.

          

        
      
  
    :type ProvisioningArtifactParameters: dict
    :param ProvisioningArtifactParameters: **[REQUIRED]** 

      The configuration of the provisioning artifact.

      

    
      - **Name** *(string) --* 

        The name of the provisioning artifact (for example, v1 v2beta). No spaces are allowed.

        

      
      - **Description** *(string) --* 

        The description of the provisioning artifact, including how it differs from the previous provisioning artifact.

        

      
      - **Info** *(dict) --* **[REQUIRED]** 

        The URL of the CloudFormation template in Amazon S3. Specify the URL in JSON format as follows:

         

         ``"LoadTemplateFromURL": "https://s3.amazonaws.com/cf-templates-ozkq9d3hgiq2-us-east-1/..."``  

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
      - **Type** *(string) --* 

        The type of provisioning artifact.

         

         
        * ``CLOUD_FORMATION_TEMPLATE`` - AWS CloudFormation template 
         
        * ``MARKETPLACE_AMI`` - AWS Marketplace AMI 
         
        * ``MARKETPLACE_CAR`` - AWS Marketplace Clusters and AWS Resources 
         

        

      
    
    :type IdempotencyToken: string
    :param IdempotencyToken: **[REQUIRED]** 

      A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.

      This field is autopopulated if not provided.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ProductViewDetail': {
                'ProductViewSummary': {
                    'Id': 'string',
                    'ProductId': 'string',
                    'Name': 'string',
                    'Owner': 'string',
                    'ShortDescription': 'string',
                    'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE',
                    'Distributor': 'string',
                    'HasDefaultPath': True|False,
                    'SupportEmail': 'string',
                    'SupportDescription': 'string',
                    'SupportUrl': 'string'
                },
                'Status': 'AVAILABLE'|'CREATING'|'FAILED',
                'ProductARN': 'string',
                'CreatedTime': datetime(2015, 1, 1)
            },
            'ProvisioningArtifactDetail': {
                'Id': 'string',
                'Name': 'string',
                'Description': 'string',
                'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR',
                'CreatedTime': datetime(2015, 1, 1),
                'Active': True|False
            },
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ProductViewDetail** *(dict) --* 

          Information about the product view.

          
          

          - **ProductViewSummary** *(dict) --* 

            Summary information about the product view.

            
            

            - **Id** *(string) --* 

              The product view identifier.

              
            

            - **ProductId** *(string) --* 

              The product identifier.

              
            

            - **Name** *(string) --* 

              The name of the product.

              
            

            - **Owner** *(string) --* 

              The owner of the product. Contact the product administrator for the significance of this value.

              
            

            - **ShortDescription** *(string) --* 

              Short description of the product.

              
            

            - **Type** *(string) --* 

              The product type. Contact the product administrator for the significance of this value. If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

              
            

            - **Distributor** *(string) --* 

              The distributor of the product. Contact the product administrator for the significance of this value.

              
            

            - **HasDefaultPath** *(boolean) --* 

              Indicates whether the product has a default path. If the product does not have a default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is not required, and the output of  ProductViewSummary can be used directly with  DescribeProvisioningParameters .

              
            

            - **SupportEmail** *(string) --* 

              The email contact information to obtain support for this Product.

              
            

            - **SupportDescription** *(string) --* 

              The description of the support for this Product.

              
            

            - **SupportUrl** *(string) --* 

              The URL information to obtain support for this Product.

              
        
          

          - **Status** *(string) --* 

            The status of the product.

             

             
            * ``AVAILABLE`` - The product is ready for use. 
             
            * ``CREATING`` - Product creation has started; the product is not ready for use. 
             
            * ``FAILED`` - An action failed. 
             

            
          

          - **ProductARN** *(string) --* 

            The ARN of the product.

            
          

          - **CreatedTime** *(datetime) --* 

            The UTC timestamp of the creation time.

            
      
        

        - **ProvisioningArtifactDetail** *(dict) --* 

          Information about the provisioning artifact.

          
          

          - **Id** *(string) --* 

            The identifier of the provisioning artifact.

            
          

          - **Name** *(string) --* 

            The name of the provisioning artifact.

            
          

          - **Description** *(string) --* 

            The description of the provisioning artifact.

            
          

          - **Type** *(string) --* 

            The type of provisioning artifact.

             

             
            * ``CLOUD_FORMATION_TEMPLATE`` - AWS CloudFormation template 
             
            * ``MARKETPLACE_AMI`` - AWS Marketplace AMI 
             
            * ``MARKETPLACE_CAR`` - AWS Marketplace Clusters and AWS Resources 
             

            
          

          - **CreatedTime** *(datetime) --* 

            The UTC timestamp of the creation time.

            
          

          - **Active** *(boolean) --* 

            Indicates whether the product version is active.

            
      
        

        - **Tags** *(list) --* 

          Information about the tags associated with the product.

          
          

          - *(dict) --* 

            Information about a tag. A tag is a key-value pair. Tags are entirely discretionary and are propagated to the resources created when provisioning a product.

            
            

            - **Key** *(string) --* 

              The tag key.

              
            

            - **Value** *(string) --* 

              The value for this key.

              
        
      
    

  .. py:method:: create_provisioning_artifact(**kwargs)

    

    Creates a provisioning artifact (also known as a version) for the specified product.

     

    You cannot create a provisioning artifact for a product that was shared with you.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/CreateProvisioningArtifact>`_    


    **Request Syntax** 
    ::

      response = client.create_provisioning_artifact(
          AcceptLanguage='string',
          ProductId='string',
          Parameters={
              'Name': 'string',
              'Description': 'string',
              'Info': {
                  'string': 'string'
              },
              'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR'
          },
          IdempotencyToken='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type ProductId: string
    :param ProductId: **[REQUIRED]** 

      The product identifier.

      

    
    :type Parameters: dict
    :param Parameters: **[REQUIRED]** 

      The configuration for the provisioning artifact.

      

    
      - **Name** *(string) --* 

        The name of the provisioning artifact (for example, v1 v2beta). No spaces are allowed.

        

      
      - **Description** *(string) --* 

        The description of the provisioning artifact, including how it differs from the previous provisioning artifact.

        

      
      - **Info** *(dict) --* **[REQUIRED]** 

        The URL of the CloudFormation template in Amazon S3. Specify the URL in JSON format as follows:

         

         ``"LoadTemplateFromURL": "https://s3.amazonaws.com/cf-templates-ozkq9d3hgiq2-us-east-1/..."``  

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
      - **Type** *(string) --* 

        The type of provisioning artifact.

         

         
        * ``CLOUD_FORMATION_TEMPLATE`` - AWS CloudFormation template 
         
        * ``MARKETPLACE_AMI`` - AWS Marketplace AMI 
         
        * ``MARKETPLACE_CAR`` - AWS Marketplace Clusters and AWS Resources 
         

        

      
    
    :type IdempotencyToken: string
    :param IdempotencyToken: **[REQUIRED]** 

      A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.

      This field is autopopulated if not provided.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ProvisioningArtifactDetail': {
                'Id': 'string',
                'Name': 'string',
                'Description': 'string',
                'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR',
                'CreatedTime': datetime(2015, 1, 1),
                'Active': True|False
            },
            'Info': {
                'string': 'string'
            },
            'Status': 'AVAILABLE'|'CREATING'|'FAILED'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ProvisioningArtifactDetail** *(dict) --* 

          Information about the provisioning artifact.

          
          

          - **Id** *(string) --* 

            The identifier of the provisioning artifact.

            
          

          - **Name** *(string) --* 

            The name of the provisioning artifact.

            
          

          - **Description** *(string) --* 

            The description of the provisioning artifact.

            
          

          - **Type** *(string) --* 

            The type of provisioning artifact.

             

             
            * ``CLOUD_FORMATION_TEMPLATE`` - AWS CloudFormation template 
             
            * ``MARKETPLACE_AMI`` - AWS Marketplace AMI 
             
            * ``MARKETPLACE_CAR`` - AWS Marketplace Clusters and AWS Resources 
             

            
          

          - **CreatedTime** *(datetime) --* 

            The UTC timestamp of the creation time.

            
          

          - **Active** *(boolean) --* 

            Indicates whether the product version is active.

            
      
        

        - **Info** *(dict) --* 

          The URL of the CloudFormation template in Amazon S3, in JSON format.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **Status** *(string) --* 

          The status of the current request.

          
    

  .. py:method:: create_tag_option(**kwargs)

    

    Creates a TagOption.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/CreateTagOption>`_    


    **Request Syntax** 
    ::

      response = client.create_tag_option(
          Key='string',
          Value='string'
      )
    :type Key: string
    :param Key: **[REQUIRED]** 

      The TagOption key.

      

    
    :type Value: string
    :param Value: **[REQUIRED]** 

      The TagOption value.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TagOptionDetail': {
                'Key': 'string',
                'Value': 'string',
                'Active': True|False,
                'Id': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TagOptionDetail** *(dict) --* 

          Information about the TagOption.

          
          

          - **Key** *(string) --* 

            The TagOption key.

            
          

          - **Value** *(string) --* 

            The TagOption value.

            
          

          - **Active** *(boolean) --* 

            The TagOption active state.

            
          

          - **Id** *(string) --* 

            The TagOption identifier.

            
      
    

  .. py:method:: delete_constraint(**kwargs)

    

    Deletes the specified constraint.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DeleteConstraint>`_    


    **Request Syntax** 
    ::

      response = client.delete_constraint(
          AcceptLanguage='string',
          Id='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type Id: string
    :param Id: **[REQUIRED]** 

      The identifier of the constraint.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_portfolio(**kwargs)

    

    Deletes the specified portfolio.

     

    You cannot delete a portfolio if it was shared with you or if it has associated products, users, constraints, or shared accounts.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DeletePortfolio>`_    


    **Request Syntax** 
    ::

      response = client.delete_portfolio(
          AcceptLanguage='string',
          Id='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type Id: string
    :param Id: **[REQUIRED]** 

      The portfolio identifier.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_portfolio_share(**kwargs)

    

    Stops sharing the specified portfolio with the specified account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DeletePortfolioShare>`_    


    **Request Syntax** 
    ::

      response = client.delete_portfolio_share(
          AcceptLanguage='string',
          PortfolioId='string',
          AccountId='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type PortfolioId: string
    :param PortfolioId: **[REQUIRED]** 

      The portfolio identifier.

      

    
    :type AccountId: string
    :param AccountId: **[REQUIRED]** 

      The AWS account ID.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_product(**kwargs)

    

    Deletes the specified product.

     

    You cannot delete a product if it was shared with you or is associated with a portfolio.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DeleteProduct>`_    


    **Request Syntax** 
    ::

      response = client.delete_product(
          AcceptLanguage='string',
          Id='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type Id: string
    :param Id: **[REQUIRED]** 

      The product identifier.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: delete_provisioning_artifact(**kwargs)

    

    Deletes the specified provisioning artifact (also known as a version) for the specified product.

     

    You cannot delete a provisioning artifact associated with a product that was shared with you. You cannot delete the last provisioning artifact for a product, because a product must have at least one provisioning artifact.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DeleteProvisioningArtifact>`_    


    **Request Syntax** 
    ::

      response = client.delete_provisioning_artifact(
          AcceptLanguage='string',
          ProductId='string',
          ProvisioningArtifactId='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type ProductId: string
    :param ProductId: **[REQUIRED]** 

      The product identifier.

      

    
    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: **[REQUIRED]** 

      The identifier of the provisioning artifact.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: describe_constraint(**kwargs)

    

    Gets information about the specified constraint.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeConstraint>`_    


    **Request Syntax** 
    ::

      response = client.describe_constraint(
          AcceptLanguage='string',
          Id='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type Id: string
    :param Id: **[REQUIRED]** 

      The identifier of the constraint.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ConstraintDetail': {
                'ConstraintId': 'string',
                'Type': 'string',
                'Description': 'string',
                'Owner': 'string'
            },
            'ConstraintParameters': 'string',
            'Status': 'AVAILABLE'|'CREATING'|'FAILED'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ConstraintDetail** *(dict) --* 

          Information about the constraint.

          
          

          - **ConstraintId** *(string) --* 

            The identifier of the constraint.

            
          

          - **Type** *(string) --* 

            The type of constraint.

             

             
            * ``LAUNCH``   
             
            * ``NOTIFICATION``   
             
            * ``TEMPLATE``   
             

            
          

          - **Description** *(string) --* 

            The description of the constraint.

            
          

          - **Owner** *(string) --* 

            The owner of the constraint.

            
      
        

        - **ConstraintParameters** *(string) --* 

          The constraint parameters.

          
        

        - **Status** *(string) --* 

          The status of the current request.

          
    

  .. py:method:: describe_copy_product_status(**kwargs)

    

    Gets the status of the specified copy product operation.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeCopyProductStatus>`_    


    **Request Syntax** 
    ::

      response = client.describe_copy_product_status(
          AcceptLanguage='string',
          CopyProductToken='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type CopyProductToken: string
    :param CopyProductToken: **[REQUIRED]** 

      The token for the copy product operation. This token is returned by  CopyProduct .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CopyProductStatus': 'SUCCEEDED'|'IN_PROGRESS'|'FAILED',
            'TargetProductId': 'string',
            'StatusDetail': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CopyProductStatus** *(string) --* 

          The status of the copy product operation.

          
        

        - **TargetProductId** *(string) --* 

          The identifier of the copied product.

          
        

        - **StatusDetail** *(string) --* 

          The status message.

          
    

  .. py:method:: describe_portfolio(**kwargs)

    

    Gets information about the specified portfolio.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribePortfolio>`_    


    **Request Syntax** 
    ::

      response = client.describe_portfolio(
          AcceptLanguage='string',
          Id='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type Id: string
    :param Id: **[REQUIRED]** 

      The portfolio identifier.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'PortfolioDetail': {
                'Id': 'string',
                'ARN': 'string',
                'DisplayName': 'string',
                'Description': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'ProviderName': 'string'
            },
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'TagOptions': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Active': True|False,
                    'Id': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **PortfolioDetail** *(dict) --* 

          Information about the portfolio.

          
          

          - **Id** *(string) --* 

            The portfolio identifier.

            
          

          - **ARN** *(string) --* 

            The ARN assigned to the portfolio.

            
          

          - **DisplayName** *(string) --* 

            The name to use for display purposes.

            
          

          - **Description** *(string) --* 

            The description of the portfolio.

            
          

          - **CreatedTime** *(datetime) --* 

            The UTC timestamp of the creation time.

            
          

          - **ProviderName** *(string) --* 

            The name of the portfolio provider.

            
      
        

        - **Tags** *(list) --* 

          Information about the tags associated with the portfolio.

          
          

          - *(dict) --* 

            Information about a tag. A tag is a key-value pair. Tags are entirely discretionary and are propagated to the resources created when provisioning a product.

            
            

            - **Key** *(string) --* 

              The tag key.

              
            

            - **Value** *(string) --* 

              The value for this key.

              
        
      
        

        - **TagOptions** *(list) --* 

          Information about the TagOptions associated with the portfolio.

          
          

          - *(dict) --* 

            Information about a TagOption.

            
            

            - **Key** *(string) --* 

              The TagOption key.

              
            

            - **Value** *(string) --* 

              The TagOption value.

              
            

            - **Active** *(boolean) --* 

              The TagOption active state.

              
            

            - **Id** *(string) --* 

              The TagOption identifier.

              
        
      
    

  .. py:method:: describe_product(**kwargs)

    

    Gets information about the specified product.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeProduct>`_    


    **Request Syntax** 
    ::

      response = client.describe_product(
          AcceptLanguage='string',
          Id='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type Id: string
    :param Id: **[REQUIRED]** 

      The product identifier.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ProductViewSummary': {
                'Id': 'string',
                'ProductId': 'string',
                'Name': 'string',
                'Owner': 'string',
                'ShortDescription': 'string',
                'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE',
                'Distributor': 'string',
                'HasDefaultPath': True|False,
                'SupportEmail': 'string',
                'SupportDescription': 'string',
                'SupportUrl': 'string'
            },
            'ProvisioningArtifacts': [
                {
                    'Id': 'string',
                    'Name': 'string',
                    'Description': 'string',
                    'CreatedTime': datetime(2015, 1, 1)
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ProductViewSummary** *(dict) --* 

          Summary information about the product view.

          
          

          - **Id** *(string) --* 

            The product view identifier.

            
          

          - **ProductId** *(string) --* 

            The product identifier.

            
          

          - **Name** *(string) --* 

            The name of the product.

            
          

          - **Owner** *(string) --* 

            The owner of the product. Contact the product administrator for the significance of this value.

            
          

          - **ShortDescription** *(string) --* 

            Short description of the product.

            
          

          - **Type** *(string) --* 

            The product type. Contact the product administrator for the significance of this value. If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

            
          

          - **Distributor** *(string) --* 

            The distributor of the product. Contact the product administrator for the significance of this value.

            
          

          - **HasDefaultPath** *(boolean) --* 

            Indicates whether the product has a default path. If the product does not have a default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is not required, and the output of  ProductViewSummary can be used directly with  DescribeProvisioningParameters .

            
          

          - **SupportEmail** *(string) --* 

            The email contact information to obtain support for this Product.

            
          

          - **SupportDescription** *(string) --* 

            The description of the support for this Product.

            
          

          - **SupportUrl** *(string) --* 

            The URL information to obtain support for this Product.

            
      
        

        - **ProvisioningArtifacts** *(list) --* 

          Information about the provisioning artifacts for the specified product.

          
          

          - *(dict) --* 

            Information about a provisioning artifact. A provisioning artifact is also known as a product version.

            
            

            - **Id** *(string) --* 

              The identifier of the provisioning artifact.

              
            

            - **Name** *(string) --* 

              The name of the provisioning artifact.

              
            

            - **Description** *(string) --* 

              The description of the provisioning artifact.

              
            

            - **CreatedTime** *(datetime) --* 

              The UTC timestamp of the creation time.

              
        
      
    

  .. py:method:: describe_product_as_admin(**kwargs)

    

    Gets information about the specified product. This operation is run with administrator access.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeProductAsAdmin>`_    


    **Request Syntax** 
    ::

      response = client.describe_product_as_admin(
          AcceptLanguage='string',
          Id='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type Id: string
    :param Id: **[REQUIRED]** 

      The product identifier.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ProductViewDetail': {
                'ProductViewSummary': {
                    'Id': 'string',
                    'ProductId': 'string',
                    'Name': 'string',
                    'Owner': 'string',
                    'ShortDescription': 'string',
                    'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE',
                    'Distributor': 'string',
                    'HasDefaultPath': True|False,
                    'SupportEmail': 'string',
                    'SupportDescription': 'string',
                    'SupportUrl': 'string'
                },
                'Status': 'AVAILABLE'|'CREATING'|'FAILED',
                'ProductARN': 'string',
                'CreatedTime': datetime(2015, 1, 1)
            },
            'ProvisioningArtifactSummaries': [
                {
                    'Id': 'string',
                    'Name': 'string',
                    'Description': 'string',
                    'CreatedTime': datetime(2015, 1, 1),
                    'ProvisioningArtifactMetadata': {
                        'string': 'string'
                    }
                },
            ],
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'TagOptions': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Active': True|False,
                    'Id': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ProductViewDetail** *(dict) --* 

          Information about the product view.

          
          

          - **ProductViewSummary** *(dict) --* 

            Summary information about the product view.

            
            

            - **Id** *(string) --* 

              The product view identifier.

              
            

            - **ProductId** *(string) --* 

              The product identifier.

              
            

            - **Name** *(string) --* 

              The name of the product.

              
            

            - **Owner** *(string) --* 

              The owner of the product. Contact the product administrator for the significance of this value.

              
            

            - **ShortDescription** *(string) --* 

              Short description of the product.

              
            

            - **Type** *(string) --* 

              The product type. Contact the product administrator for the significance of this value. If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

              
            

            - **Distributor** *(string) --* 

              The distributor of the product. Contact the product administrator for the significance of this value.

              
            

            - **HasDefaultPath** *(boolean) --* 

              Indicates whether the product has a default path. If the product does not have a default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is not required, and the output of  ProductViewSummary can be used directly with  DescribeProvisioningParameters .

              
            

            - **SupportEmail** *(string) --* 

              The email contact information to obtain support for this Product.

              
            

            - **SupportDescription** *(string) --* 

              The description of the support for this Product.

              
            

            - **SupportUrl** *(string) --* 

              The URL information to obtain support for this Product.

              
        
          

          - **Status** *(string) --* 

            The status of the product.

             

             
            * ``AVAILABLE`` - The product is ready for use. 
             
            * ``CREATING`` - Product creation has started; the product is not ready for use. 
             
            * ``FAILED`` - An action failed. 
             

            
          

          - **ProductARN** *(string) --* 

            The ARN of the product.

            
          

          - **CreatedTime** *(datetime) --* 

            The UTC timestamp of the creation time.

            
      
        

        - **ProvisioningArtifactSummaries** *(list) --* 

          Information about the provisioning artifacts (also known as versions) for the specified product.

          
          

          - *(dict) --* 

            Summary information about a provisioning artifact (also known as a version) for a product.

            
            

            - **Id** *(string) --* 

              The identifier of the provisioning artifact.

              
            

            - **Name** *(string) --* 

              The name of the provisioning artifact.

              
            

            - **Description** *(string) --* 

              The description of the provisioning artifact.

              
            

            - **CreatedTime** *(datetime) --* 

              The UTC timestamp of the creation time.

              
            

            - **ProvisioningArtifactMetadata** *(dict) --* 

              The metadata for the provisioning artifact. This is used with AWS Marketplace products.

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
        
      
        

        - **Tags** *(list) --* 

          Information about the tags associated with the product.

          
          

          - *(dict) --* 

            Information about a tag. A tag is a key-value pair. Tags are entirely discretionary and are propagated to the resources created when provisioning a product.

            
            

            - **Key** *(string) --* 

              The tag key.

              
            

            - **Value** *(string) --* 

              The value for this key.

              
        
      
        

        - **TagOptions** *(list) --* 

          Information about the TagOptions associated with the product.

          
          

          - *(dict) --* 

            Information about a TagOption.

            
            

            - **Key** *(string) --* 

              The TagOption key.

              
            

            - **Value** *(string) --* 

              The TagOption value.

              
            

            - **Active** *(boolean) --* 

              The TagOption active state.

              
            

            - **Id** *(string) --* 

              The TagOption identifier.

              
        
      
    

  .. py:method:: describe_product_view(**kwargs)

    

    Gets information about the specified product.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeProductView>`_    


    **Request Syntax** 
    ::

      response = client.describe_product_view(
          AcceptLanguage='string',
          Id='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type Id: string
    :param Id: **[REQUIRED]** 

      The product view identifier.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ProductViewSummary': {
                'Id': 'string',
                'ProductId': 'string',
                'Name': 'string',
                'Owner': 'string',
                'ShortDescription': 'string',
                'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE',
                'Distributor': 'string',
                'HasDefaultPath': True|False,
                'SupportEmail': 'string',
                'SupportDescription': 'string',
                'SupportUrl': 'string'
            },
            'ProvisioningArtifacts': [
                {
                    'Id': 'string',
                    'Name': 'string',
                    'Description': 'string',
                    'CreatedTime': datetime(2015, 1, 1)
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ProductViewSummary** *(dict) --* 

          Summary information about the product.

          
          

          - **Id** *(string) --* 

            The product view identifier.

            
          

          - **ProductId** *(string) --* 

            The product identifier.

            
          

          - **Name** *(string) --* 

            The name of the product.

            
          

          - **Owner** *(string) --* 

            The owner of the product. Contact the product administrator for the significance of this value.

            
          

          - **ShortDescription** *(string) --* 

            Short description of the product.

            
          

          - **Type** *(string) --* 

            The product type. Contact the product administrator for the significance of this value. If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

            
          

          - **Distributor** *(string) --* 

            The distributor of the product. Contact the product administrator for the significance of this value.

            
          

          - **HasDefaultPath** *(boolean) --* 

            Indicates whether the product has a default path. If the product does not have a default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is not required, and the output of  ProductViewSummary can be used directly with  DescribeProvisioningParameters .

            
          

          - **SupportEmail** *(string) --* 

            The email contact information to obtain support for this Product.

            
          

          - **SupportDescription** *(string) --* 

            The description of the support for this Product.

            
          

          - **SupportUrl** *(string) --* 

            The URL information to obtain support for this Product.

            
      
        

        - **ProvisioningArtifacts** *(list) --* 

          Information about the provisioning artifacts for the product.

          
          

          - *(dict) --* 

            Information about a provisioning artifact. A provisioning artifact is also known as a product version.

            
            

            - **Id** *(string) --* 

              The identifier of the provisioning artifact.

              
            

            - **Name** *(string) --* 

              The name of the provisioning artifact.

              
            

            - **Description** *(string) --* 

              The description of the provisioning artifact.

              
            

            - **CreatedTime** *(datetime) --* 

              The UTC timestamp of the creation time.

              
        
      
    

  .. py:method:: describe_provisioned_product(**kwargs)

    

    Gets information about the specified provisioned product.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeProvisionedProduct>`_    


    **Request Syntax** 
    ::

      response = client.describe_provisioned_product(
          AcceptLanguage='string',
          Id='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type Id: string
    :param Id: **[REQUIRED]** 

      The provisioned product identifier.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ProvisionedProductDetail': {
                'Name': 'string',
                'Arn': 'string',
                'Type': 'string',
                'Id': 'string',
                'Status': 'AVAILABLE'|'UNDER_CHANGE'|'TAINTED'|'ERROR',
                'StatusMessage': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'IdempotencyToken': 'string',
                'LastRecordId': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ProvisionedProductDetail** *(dict) --* 

          Information about the provisioned product.

          
          

          - **Name** *(string) --* 

            The user-friendly name of the provisioned product.

            
          

          - **Arn** *(string) --* 

            The ARN of the provisioned product.

            
          

          - **Type** *(string) --* 

            The type of provisioned product. The supported value is ``CFN_STACK`` .

            
          

          - **Id** *(string) --* 

            The identifier of the provisioned product.

            
          

          - **Status** *(string) --* 

            The current status of the provisioned product.

             

             
            * ``AVAILABLE`` - Stable state, ready to perform any operation. The most recent operation succeeded and completed. 
             
            * ``UNDER_CHANGE`` - Transitive state, operations performed might not have valid results. Wait for an ``AVAILABLE`` status before performing operations. 
             
            * ``TAINTED`` - Stable state, ready to perform any operation. The stack has completed the requested operation but is not exactly what was requested. For example, a request to update to a new version failed and the stack rolled back to the current version. 
             
            * ``ERROR`` - An unexpected error occurred, the provisioned product exists but the stack is not running. For example, CloudFormation received a parameter value that was not valid and could not launch the stack. 
             

            
          

          - **StatusMessage** *(string) --* 

            The current status message of the provisioned product.

            
          

          - **CreatedTime** *(datetime) --* 

            The UTC timestamp of the creation time.

            
          

          - **IdempotencyToken** *(string) --* 

            A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.

            
          

          - **LastRecordId** *(string) --* 

            The record identifier of the last request performed on this provisioned product.

            
      
    

  .. py:method:: describe_provisioning_artifact(**kwargs)

    

    Gets information about the specified provisioning artifact (also known as a version) for the specified product.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeProvisioningArtifact>`_    


    **Request Syntax** 
    ::

      response = client.describe_provisioning_artifact(
          AcceptLanguage='string',
          ProvisioningArtifactId='string',
          ProductId='string',
          Verbose=True|False
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: **[REQUIRED]** 

      The identifier of the provisioning artifact.

      

    
    :type ProductId: string
    :param ProductId: **[REQUIRED]** 

      The product identifier.

      

    
    :type Verbose: boolean
    :param Verbose: 

      Indicates whether a verbose level of detail is enabled.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ProvisioningArtifactDetail': {
                'Id': 'string',
                'Name': 'string',
                'Description': 'string',
                'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR',
                'CreatedTime': datetime(2015, 1, 1),
                'Active': True|False
            },
            'Info': {
                'string': 'string'
            },
            'Status': 'AVAILABLE'|'CREATING'|'FAILED'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ProvisioningArtifactDetail** *(dict) --* 

          Information about the provisioning artifact.

          
          

          - **Id** *(string) --* 

            The identifier of the provisioning artifact.

            
          

          - **Name** *(string) --* 

            The name of the provisioning artifact.

            
          

          - **Description** *(string) --* 

            The description of the provisioning artifact.

            
          

          - **Type** *(string) --* 

            The type of provisioning artifact.

             

             
            * ``CLOUD_FORMATION_TEMPLATE`` - AWS CloudFormation template 
             
            * ``MARKETPLACE_AMI`` - AWS Marketplace AMI 
             
            * ``MARKETPLACE_CAR`` - AWS Marketplace Clusters and AWS Resources 
             

            
          

          - **CreatedTime** *(datetime) --* 

            The UTC timestamp of the creation time.

            
          

          - **Active** *(boolean) --* 

            Indicates whether the product version is active.

            
      
        

        - **Info** *(dict) --* 

          The URL of the CloudFormation template in Amazon S3.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **Status** *(string) --* 

          The status of the current request.

          
    

  .. py:method:: describe_provisioning_parameters(**kwargs)

    

    Gets information about the configuration required to provision the specified product using the specified provisioning artifact.

     

    If the output contains a TagOption key with an empty list of values, there is a TagOption conflict for that key. The end user cannot take action to fix the conflict, and launch is not blocked. In subsequent calls to  ProvisionProduct , do not include conflicted TagOption keys as tags, or this will cause the error "Parameter validation failed: Missing required parameter in Tags[*N* ]:*Value* " and tag the provisioned product with the value ``sc-tagoption-conflict-portfolioId-productId`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeProvisioningParameters>`_    


    **Request Syntax** 
    ::

      response = client.describe_provisioning_parameters(
          AcceptLanguage='string',
          ProductId='string',
          ProvisioningArtifactId='string',
          PathId='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type ProductId: string
    :param ProductId: **[REQUIRED]** 

      The product identifier.

      

    
    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: **[REQUIRED]** 

      The identifier of the provisioning artifact.

      

    
    :type PathId: string
    :param PathId: 

      The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use  ListLaunchPaths .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ProvisioningArtifactParameters': [
                {
                    'ParameterKey': 'string',
                    'DefaultValue': 'string',
                    'ParameterType': 'string',
                    'IsNoEcho': True|False,
                    'Description': 'string',
                    'ParameterConstraints': {
                        'AllowedValues': [
                            'string',
                        ]
                    }
                },
            ],
            'ConstraintSummaries': [
                {
                    'Type': 'string',
                    'Description': 'string'
                },
            ],
            'UsageInstructions': [
                {
                    'Type': 'string',
                    'Value': 'string'
                },
            ],
            'TagOptions': [
                {
                    'Key': 'string',
                    'Values': [
                        'string',
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ProvisioningArtifactParameters** *(list) --* 

          Information about the parameters used to provision the product.

          
          

          - *(dict) --* 

            Information about a parameter used to provision a product.

            
            

            - **ParameterKey** *(string) --* 

              The parameter key.

              
            

            - **DefaultValue** *(string) --* 

              The default value.

              
            

            - **ParameterType** *(string) --* 

              The parameter type.

              
            

            - **IsNoEcho** *(boolean) --* 

              If this value is true, the value for this parameter is obfuscated from view when the parameter is retrieved. This parameter is used to hide sensitive information.

              
            

            - **Description** *(string) --* 

              The description of the parameter.

              
            

            - **ParameterConstraints** *(dict) --* 

              Constraints that the administrator has put on a parameter.

              
              

              - **AllowedValues** *(list) --* 

                The values that the administrator has allowed for the parameter.

                
                

                - *(string) --* 
            
          
        
      
        

        - **ConstraintSummaries** *(list) --* 

          Information about the constraints used to provision the product.

          
          

          - *(dict) --* 

            Summary information about a constraint.

            
            

            - **Type** *(string) --* 

              The type of constraint.

               

               
              * ``LAUNCH``   
               
              * ``NOTIFICATION``   
               
              * ``TEMPLATE``   
               

              
            

            - **Description** *(string) --* 

              The description of the constraint.

              
        
      
        

        - **UsageInstructions** *(list) --* 

          Any additional metadata specifically related to the provisioning of the product. For example, see the ``Version`` field of the CloudFormation template.

          
          

          - *(dict) --* 

            Additional information provided by the administrator.

            
            

            - **Type** *(string) --* 

              The usage instruction type for the value.

              
            

            - **Value** *(string) --* 

              The usage instruction value for this type.

              
        
      
        

        - **TagOptions** *(list) --* 

          Information about the TagOptions associated with the resource.

          
          

          - *(dict) --* 

            Summary information about a TagOption.

            
            

            - **Key** *(string) --* 

              The TagOption key.

              
            

            - **Values** *(list) --* 

              The TagOption value.

              
              

              - *(string) --* 
          
        
      
    

  .. py:method:: describe_record(**kwargs)

    

    Gets information about the specified request operation.

     

    Use this operation after calling a request operation (for example,  ProvisionProduct ,  TerminateProvisionedProduct , or  UpdateProvisionedProduct ). 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeRecord>`_    


    **Request Syntax** 
    ::

      response = client.describe_record(
          AcceptLanguage='string',
          Id='string',
          PageToken='string',
          PageSize=123
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type Id: string
    :param Id: **[REQUIRED]** 

      The record identifier of the provisioned product. This identifier is returned by the request operation.

      

    
    :type PageToken: string
    :param PageToken: 

      The page token for the next set of results. To retrieve the first set of results, use null.

      

    
    :type PageSize: integer
    :param PageSize: 

      The maximum number of items to return with this call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'RecordDetail': {
                'RecordId': 'string',
                'ProvisionedProductName': 'string',
                'Status': 'CREATED'|'IN_PROGRESS'|'IN_PROGRESS_IN_ERROR'|'SUCCEEDED'|'FAILED',
                'CreatedTime': datetime(2015, 1, 1),
                'UpdatedTime': datetime(2015, 1, 1),
                'ProvisionedProductType': 'string',
                'RecordType': 'string',
                'ProvisionedProductId': 'string',
                'ProductId': 'string',
                'ProvisioningArtifactId': 'string',
                'PathId': 'string',
                'RecordErrors': [
                    {
                        'Code': 'string',
                        'Description': 'string'
                    },
                ],
                'RecordTags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            },
            'RecordOutputs': [
                {
                    'OutputKey': 'string',
                    'OutputValue': 'string',
                    'Description': 'string'
                },
            ],
            'NextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **RecordDetail** *(dict) --* 

          Information about the product.

          
          

          - **RecordId** *(string) --* 

            The identifier of the record.

            
          

          - **ProvisionedProductName** *(string) --* 

            The user-friendly name of the provisioned product.

            
          

          - **Status** *(string) --* 

            The status of the provisioned product.

             

             
            * ``CREATED`` - The request was created but the operation has not started. 
             
            * ``IN_PROGRESS`` - The requested operation is in progress. 
             
            * ``IN_PROGRESS_IN_ERROR`` - The provisioned product is under change but the requested operation failed and some remediation is occurring. For example, a rollback. 
             
            * ``SUCCEEDED`` - The requested operation has successfully completed. 
             
            * ``FAILED`` - The requested operation has unsuccessfully completed. Investigate using the error messages returned. 
             

            
          

          - **CreatedTime** *(datetime) --* 

            The UTC timestamp of the creation time.

            
          

          - **UpdatedTime** *(datetime) --* 

            The time when the record was last updated.

            
          

          - **ProvisionedProductType** *(string) --* 

            The type of provisioned product. The supported value is ``CFN_STACK`` .

            
          

          - **RecordType** *(string) --* 

            The record type for this record.

             

             
            * ``PROVISION_PRODUCT``   
             
            * ``UPDATE_PROVISIONED_PRODUCT``   
             
            * ``TERMINATE_PROVISIONED_PRODUCT``   
             

            
          

          - **ProvisionedProductId** *(string) --* 

            The identifier of the provisioned product.

            
          

          - **ProductId** *(string) --* 

            The product identifier.

            
          

          - **ProvisioningArtifactId** *(string) --* 

            The identifier of the provisioning artifact.

            
          

          - **PathId** *(string) --* 

            The path identifier.

            
          

          - **RecordErrors** *(list) --* 

            The errors that occurred while processing the request.

            
            

            - *(dict) --* 

              The error code and description resulting from an operation.

              
              

              - **Code** *(string) --* 

                The numeric value of the error.

                
              

              - **Description** *(string) --* 

                The description of the error.

                
          
        
          

          - **RecordTags** *(list) --* 

            The tags associated with this record.

            
            

            - *(dict) --* 

              A tag associated with the record, stored as a key-value pair.

              
              

              - **Key** *(string) --* 

                The key for this tag.

                
              

              - **Value** *(string) --* 

                The value for this tag.

                
          
        
      
        

        - **RecordOutputs** *(list) --* 

          Information about the product created as the result of a request. For example, the output for a CloudFormation-backed product that creates an S3 bucket would include the S3 bucket URL.

          
          

          - *(dict) --* 

            The output for the product created as the result of a request. For example, the output for a CloudFormation-backed product that creates an S3 bucket would include the S3 bucket URL.

            
            

            - **OutputKey** *(string) --* 

              The output key.

              
            

            - **OutputValue** *(string) --* 

              The output value.

              
            

            - **Description** *(string) --* 

              The description of the output.

              
        
      
        

        - **NextPageToken** *(string) --* 

          The page token to use to retrieve the next set of results. If there are no additional results, this value is null.

          
    

  .. py:method:: describe_tag_option(**kwargs)

    

    Gets information about the specified TagOption.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeTagOption>`_    


    **Request Syntax** 
    ::

      response = client.describe_tag_option(
          Id='string'
      )
    :type Id: string
    :param Id: **[REQUIRED]** 

      The TagOption identifier.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TagOptionDetail': {
                'Key': 'string',
                'Value': 'string',
                'Active': True|False,
                'Id': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TagOptionDetail** *(dict) --* 

          Information about the TagOption.

          
          

          - **Key** *(string) --* 

            The TagOption key.

            
          

          - **Value** *(string) --* 

            The TagOption value.

            
          

          - **Active** *(boolean) --* 

            The TagOption active state.

            
          

          - **Id** *(string) --* 

            The TagOption identifier.

            
      
    

  .. py:method:: disassociate_principal_from_portfolio(**kwargs)

    

    Disassociates a previously associated principal ARN from a specified portfolio.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DisassociatePrincipalFromPortfolio>`_    


    **Request Syntax** 
    ::

      response = client.disassociate_principal_from_portfolio(
          AcceptLanguage='string',
          PortfolioId='string',
          PrincipalARN='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type PortfolioId: string
    :param PortfolioId: **[REQUIRED]** 

      The portfolio identifier.

      

    
    :type PrincipalARN: string
    :param PrincipalARN: **[REQUIRED]** 

      The ARN of the principal (IAM user, role, or group).

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: disassociate_product_from_portfolio(**kwargs)

    

    Disassociates the specified product from the specified portfolio. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DisassociateProductFromPortfolio>`_    


    **Request Syntax** 
    ::

      response = client.disassociate_product_from_portfolio(
          AcceptLanguage='string',
          ProductId='string',
          PortfolioId='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type ProductId: string
    :param ProductId: **[REQUIRED]** 

      The product identifier.

      

    
    :type PortfolioId: string
    :param PortfolioId: **[REQUIRED]** 

      The portfolio identifier.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: disassociate_tag_option_from_resource(**kwargs)

    

    Disassociates the specified TagOption from the specified resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DisassociateTagOptionFromResource>`_    


    **Request Syntax** 
    ::

      response = client.disassociate_tag_option_from_resource(
          ResourceId='string',
          TagOptionId='string'
      )
    :type ResourceId: string
    :param ResourceId: **[REQUIRED]** 

      The resource identifier.

      

    
    :type TagOptionId: string
    :param TagOptionId: **[REQUIRED]** 

      The TagOption identifier.

      

    
    
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

        


  .. py:method:: list_accepted_portfolio_shares(**kwargs)

    

    Lists all portfolios for which sharing was accepted by this account.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListAcceptedPortfolioShares>`_    


    **Request Syntax** 
    ::

      response = client.list_accepted_portfolio_shares(
          AcceptLanguage='string',
          PageToken='string',
          PageSize=123
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type PageToken: string
    :param PageToken: 

      The page token for the next set of results. To retrieve the first set of results, use null.

      

    
    :type PageSize: integer
    :param PageSize: 

      The maximum number of items to return with this call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'PortfolioDetails': [
                {
                    'Id': 'string',
                    'ARN': 'string',
                    'DisplayName': 'string',
                    'Description': 'string',
                    'CreatedTime': datetime(2015, 1, 1),
                    'ProviderName': 'string'
                },
            ],
            'NextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **PortfolioDetails** *(list) --* 

          Information about the portfolios.

          
          

          - *(dict) --* 

            Information about a portfolio.

            
            

            - **Id** *(string) --* 

              The portfolio identifier.

              
            

            - **ARN** *(string) --* 

              The ARN assigned to the portfolio.

              
            

            - **DisplayName** *(string) --* 

              The name to use for display purposes.

              
            

            - **Description** *(string) --* 

              The description of the portfolio.

              
            

            - **CreatedTime** *(datetime) --* 

              The UTC timestamp of the creation time.

              
            

            - **ProviderName** *(string) --* 

              The name of the portfolio provider.

              
        
      
        

        - **NextPageToken** *(string) --* 

          The page token to use to retrieve the next set of results. If there are no additional results, this value is null.

          
    

  .. py:method:: list_constraints_for_portfolio(**kwargs)

    

    Lists the constraints for the specified portfolio and product.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListConstraintsForPortfolio>`_    


    **Request Syntax** 
    ::

      response = client.list_constraints_for_portfolio(
          AcceptLanguage='string',
          PortfolioId='string',
          ProductId='string',
          PageSize=123,
          PageToken='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type PortfolioId: string
    :param PortfolioId: **[REQUIRED]** 

      The portfolio identifier.

      

    
    :type ProductId: string
    :param ProductId: 

      The product identifier.

      

    
    :type PageSize: integer
    :param PageSize: 

      The maximum number of items to return with this call.

      

    
    :type PageToken: string
    :param PageToken: 

      The page token for the next set of results. To retrieve the first set of results, use null.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ConstraintDetails': [
                {
                    'ConstraintId': 'string',
                    'Type': 'string',
                    'Description': 'string',
                    'Owner': 'string'
                },
            ],
            'NextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ConstraintDetails** *(list) --* 

          Information about the constraints.

          
          

          - *(dict) --* 

            Information about a constraint.

            
            

            - **ConstraintId** *(string) --* 

              The identifier of the constraint.

              
            

            - **Type** *(string) --* 

              The type of constraint.

               

               
              * ``LAUNCH``   
               
              * ``NOTIFICATION``   
               
              * ``TEMPLATE``   
               

              
            

            - **Description** *(string) --* 

              The description of the constraint.

              
            

            - **Owner** *(string) --* 

              The owner of the constraint.

              
        
      
        

        - **NextPageToken** *(string) --* 

          The page token to use to retrieve the next set of results. If there are no additional results, this value is null.

          
    

  .. py:method:: list_launch_paths(**kwargs)

    

    Lists the paths to the specified product. A path is how the user has access to a specified product, and is necessary when provisioning a product. A path also determines the constraints put on the product.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListLaunchPaths>`_    


    **Request Syntax** 
    ::

      response = client.list_launch_paths(
          AcceptLanguage='string',
          ProductId='string',
          PageSize=123,
          PageToken='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type ProductId: string
    :param ProductId: **[REQUIRED]** 

      The product identifier.

      

    
    :type PageSize: integer
    :param PageSize: 

      The maximum number of items to return with this call.

      

    
    :type PageToken: string
    :param PageToken: 

      The page token for the next set of results. To retrieve the first set of results, use null.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'LaunchPathSummaries': [
                {
                    'Id': 'string',
                    'ConstraintSummaries': [
                        {
                            'Type': 'string',
                            'Description': 'string'
                        },
                    ],
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'Name': 'string'
                },
            ],
            'NextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **LaunchPathSummaries** *(list) --* 

          Information about the launch path.

          
          

          - *(dict) --* 

            Summary information about a product path for a user.

            
            

            - **Id** *(string) --* 

              The identifier of the product path.

              
            

            - **ConstraintSummaries** *(list) --* 

              The constraints on the portfolio-product relationship.

              
              

              - *(dict) --* 

                Summary information about a constraint.

                
                

                - **Type** *(string) --* 

                  The type of constraint.

                   

                   
                  * ``LAUNCH``   
                   
                  * ``NOTIFICATION``   
                   
                  * ``TEMPLATE``   
                   

                  
                

                - **Description** *(string) --* 

                  The description of the constraint.

                  
            
          
            

            - **Tags** *(list) --* 

              The tags associated with this product path.

              
              

              - *(dict) --* 

                Information about a tag. A tag is a key-value pair. Tags are entirely discretionary and are propagated to the resources created when provisioning a product.

                
                

                - **Key** *(string) --* 

                  The tag key.

                  
                

                - **Value** *(string) --* 

                  The value for this key.

                  
            
          
            

            - **Name** *(string) --* 

              The name of the portfolio to which the user was assigned.

              
        
      
        

        - **NextPageToken** *(string) --* 

          The page token to use to retrieve the next set of results. If there are no additional results, this value is null.

          
    

  .. py:method:: list_portfolio_access(**kwargs)

    

    Lists the account IDs that have access to the specified portfolio.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListPortfolioAccess>`_    


    **Request Syntax** 
    ::

      response = client.list_portfolio_access(
          AcceptLanguage='string',
          PortfolioId='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type PortfolioId: string
    :param PortfolioId: **[REQUIRED]** 

      The portfolio identifier.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AccountIds': [
                'string',
            ],
            'NextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **AccountIds** *(list) --* 

          Information about the AWS accounts with access to the portfolio.

          
          

          - *(string) --* 
      
        

        - **NextPageToken** *(string) --* 

          The page token to use to retrieve the next set of results. If there are no additional results, this value is null.

          
    

  .. py:method:: list_portfolios(**kwargs)

    

    Lists all portfolios in the catalog.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListPortfolios>`_    


    **Request Syntax** 
    ::

      response = client.list_portfolios(
          AcceptLanguage='string',
          PageToken='string',
          PageSize=123
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type PageToken: string
    :param PageToken: 

      The page token for the next set of results. To retrieve the first set of results, use null.

      

    
    :type PageSize: integer
    :param PageSize: 

      The maximum number of items to return with this call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'PortfolioDetails': [
                {
                    'Id': 'string',
                    'ARN': 'string',
                    'DisplayName': 'string',
                    'Description': 'string',
                    'CreatedTime': datetime(2015, 1, 1),
                    'ProviderName': 'string'
                },
            ],
            'NextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **PortfolioDetails** *(list) --* 

          Information about the portfolios.

          
          

          - *(dict) --* 

            Information about a portfolio.

            
            

            - **Id** *(string) --* 

              The portfolio identifier.

              
            

            - **ARN** *(string) --* 

              The ARN assigned to the portfolio.

              
            

            - **DisplayName** *(string) --* 

              The name to use for display purposes.

              
            

            - **Description** *(string) --* 

              The description of the portfolio.

              
            

            - **CreatedTime** *(datetime) --* 

              The UTC timestamp of the creation time.

              
            

            - **ProviderName** *(string) --* 

              The name of the portfolio provider.

              
        
      
        

        - **NextPageToken** *(string) --* 

          The page token to use to retrieve the next set of results. If there are no additional results, this value is null.

          
    

  .. py:method:: list_portfolios_for_product(**kwargs)

    

    Lists all portfolios that the specified product is associated with.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListPortfoliosForProduct>`_    


    **Request Syntax** 
    ::

      response = client.list_portfolios_for_product(
          AcceptLanguage='string',
          ProductId='string',
          PageToken='string',
          PageSize=123
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type ProductId: string
    :param ProductId: **[REQUIRED]** 

      The product identifier.

      

    
    :type PageToken: string
    :param PageToken: 

      The page token for the next set of results. To retrieve the first set of results, use null.

      

    
    :type PageSize: integer
    :param PageSize: 

      The maximum number of items to return with this call.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'PortfolioDetails': [
                {
                    'Id': 'string',
                    'ARN': 'string',
                    'DisplayName': 'string',
                    'Description': 'string',
                    'CreatedTime': datetime(2015, 1, 1),
                    'ProviderName': 'string'
                },
            ],
            'NextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **PortfolioDetails** *(list) --* 

          Information about the portfolios.

          
          

          - *(dict) --* 

            Information about a portfolio.

            
            

            - **Id** *(string) --* 

              The portfolio identifier.

              
            

            - **ARN** *(string) --* 

              The ARN assigned to the portfolio.

              
            

            - **DisplayName** *(string) --* 

              The name to use for display purposes.

              
            

            - **Description** *(string) --* 

              The description of the portfolio.

              
            

            - **CreatedTime** *(datetime) --* 

              The UTC timestamp of the creation time.

              
            

            - **ProviderName** *(string) --* 

              The name of the portfolio provider.

              
        
      
        

        - **NextPageToken** *(string) --* 

          The page token to use to retrieve the next set of results. If there are no additional results, this value is null.

          
    

  .. py:method:: list_principals_for_portfolio(**kwargs)

    

    Lists all principal ARNs associated with the specified portfolio.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListPrincipalsForPortfolio>`_    


    **Request Syntax** 
    ::

      response = client.list_principals_for_portfolio(
          AcceptLanguage='string',
          PortfolioId='string',
          PageSize=123,
          PageToken='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type PortfolioId: string
    :param PortfolioId: **[REQUIRED]** 

      The portfolio identifier.

      

    
    :type PageSize: integer
    :param PageSize: 

      The maximum number of items to return with this call.

      

    
    :type PageToken: string
    :param PageToken: 

      The page token for the next set of results. To retrieve the first set of results, use null.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Principals': [
                {
                    'PrincipalARN': 'string',
                    'PrincipalType': 'IAM'
                },
            ],
            'NextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Principals** *(list) --* 

          The IAM principals (users or roles) associated with the portfolio.

          
          

          - *(dict) --* 

            Information about a principal.

            
            

            - **PrincipalARN** *(string) --* 

              The ARN of the principal (IAM user, role, or group).

              
            

            - **PrincipalType** *(string) --* 

              The principal type. The supported value is ``IAM`` .

              
        
      
        

        - **NextPageToken** *(string) --* 

          The page token to use to retrieve the next set of results. If there are no additional results, this value is null.

          
    

  .. py:method:: list_provisioning_artifacts(**kwargs)

    

    Lists all provisioning artifacts (also known as versions) for the specified product.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListProvisioningArtifacts>`_    


    **Request Syntax** 
    ::

      response = client.list_provisioning_artifacts(
          AcceptLanguage='string',
          ProductId='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type ProductId: string
    :param ProductId: **[REQUIRED]** 

      The product identifier.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ProvisioningArtifactDetails': [
                {
                    'Id': 'string',
                    'Name': 'string',
                    'Description': 'string',
                    'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR',
                    'CreatedTime': datetime(2015, 1, 1),
                    'Active': True|False
                },
            ],
            'NextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ProvisioningArtifactDetails** *(list) --* 

          Information about the provisioning artifacts.

          
          

          - *(dict) --* 

            Information about a provisioning artifact (also known as a version) for a product.

            
            

            - **Id** *(string) --* 

              The identifier of the provisioning artifact.

              
            

            - **Name** *(string) --* 

              The name of the provisioning artifact.

              
            

            - **Description** *(string) --* 

              The description of the provisioning artifact.

              
            

            - **Type** *(string) --* 

              The type of provisioning artifact.

               

               
              * ``CLOUD_FORMATION_TEMPLATE`` - AWS CloudFormation template 
               
              * ``MARKETPLACE_AMI`` - AWS Marketplace AMI 
               
              * ``MARKETPLACE_CAR`` - AWS Marketplace Clusters and AWS Resources 
               

              
            

            - **CreatedTime** *(datetime) --* 

              The UTC timestamp of the creation time.

              
            

            - **Active** *(boolean) --* 

              Indicates whether the product version is active.

              
        
      
        

        - **NextPageToken** *(string) --* 

          The page token to use to retrieve the next set of results. If there are no additional results, this value is null.

          
    

  .. py:method:: list_record_history(**kwargs)

    

    Lists the specified requests or all performed requests.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListRecordHistory>`_    


    **Request Syntax** 
    ::

      response = client.list_record_history(
          AcceptLanguage='string',
          AccessLevelFilter={
              'Key': 'Account'|'Role'|'User',
              'Value': 'string'
          },
          SearchFilter={
              'Key': 'string',
              'Value': 'string'
          },
          PageSize=123,
          PageToken='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type AccessLevelFilter: dict
    :param AccessLevelFilter: 

      The access level to use to obtain results. The default is ``User`` .

      

    
      - **Key** *(string) --* 

        The access level.

         

         
        * ``Account`` - Filter results based on the account. 
         
        * ``Role`` - Filter results based on the federated role of the specified user. 
         
        * ``User`` - Filter results based on the specified user. 
         

        

      
      - **Value** *(string) --* 

        The user to which the access level applies. The only supported value is ``Self`` .

        

      
    
    :type SearchFilter: dict
    :param SearchFilter: 

      The search filter to scope the results.

      

    
      - **Key** *(string) --* 

        The filter key.

         

         
        * ``product`` - Filter results based on the specified product identifier. 
         
        * ``provisionedproduct`` - Filter results based on the provisioned product identifier. 
         

        

      
      - **Value** *(string) --* 

        The filter value.

        

      
    
    :type PageSize: integer
    :param PageSize: 

      The maximum number of items to return with this call.

      

    
    :type PageToken: string
    :param PageToken: 

      The page token for the next set of results. To retrieve the first set of results, use null.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'RecordDetails': [
                {
                    'RecordId': 'string',
                    'ProvisionedProductName': 'string',
                    'Status': 'CREATED'|'IN_PROGRESS'|'IN_PROGRESS_IN_ERROR'|'SUCCEEDED'|'FAILED',
                    'CreatedTime': datetime(2015, 1, 1),
                    'UpdatedTime': datetime(2015, 1, 1),
                    'ProvisionedProductType': 'string',
                    'RecordType': 'string',
                    'ProvisionedProductId': 'string',
                    'ProductId': 'string',
                    'ProvisioningArtifactId': 'string',
                    'PathId': 'string',
                    'RecordErrors': [
                        {
                            'Code': 'string',
                            'Description': 'string'
                        },
                    ],
                    'RecordTags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ]
                },
            ],
            'NextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **RecordDetails** *(list) --* 

          The records, in reverse chronological order.

          
          

          - *(dict) --* 

            Information about a request operation.

            
            

            - **RecordId** *(string) --* 

              The identifier of the record.

              
            

            - **ProvisionedProductName** *(string) --* 

              The user-friendly name of the provisioned product.

              
            

            - **Status** *(string) --* 

              The status of the provisioned product.

               

               
              * ``CREATED`` - The request was created but the operation has not started. 
               
              * ``IN_PROGRESS`` - The requested operation is in progress. 
               
              * ``IN_PROGRESS_IN_ERROR`` - The provisioned product is under change but the requested operation failed and some remediation is occurring. For example, a rollback. 
               
              * ``SUCCEEDED`` - The requested operation has successfully completed. 
               
              * ``FAILED`` - The requested operation has unsuccessfully completed. Investigate using the error messages returned. 
               

              
            

            - **CreatedTime** *(datetime) --* 

              The UTC timestamp of the creation time.

              
            

            - **UpdatedTime** *(datetime) --* 

              The time when the record was last updated.

              
            

            - **ProvisionedProductType** *(string) --* 

              The type of provisioned product. The supported value is ``CFN_STACK`` .

              
            

            - **RecordType** *(string) --* 

              The record type for this record.

               

               
              * ``PROVISION_PRODUCT``   
               
              * ``UPDATE_PROVISIONED_PRODUCT``   
               
              * ``TERMINATE_PROVISIONED_PRODUCT``   
               

              
            

            - **ProvisionedProductId** *(string) --* 

              The identifier of the provisioned product.

              
            

            - **ProductId** *(string) --* 

              The product identifier.

              
            

            - **ProvisioningArtifactId** *(string) --* 

              The identifier of the provisioning artifact.

              
            

            - **PathId** *(string) --* 

              The path identifier.

              
            

            - **RecordErrors** *(list) --* 

              The errors that occurred while processing the request.

              
              

              - *(dict) --* 

                The error code and description resulting from an operation.

                
                

                - **Code** *(string) --* 

                  The numeric value of the error.

                  
                

                - **Description** *(string) --* 

                  The description of the error.

                  
            
          
            

            - **RecordTags** *(list) --* 

              The tags associated with this record.

              
              

              - *(dict) --* 

                A tag associated with the record, stored as a key-value pair.

                
                

                - **Key** *(string) --* 

                  The key for this tag.

                  
                

                - **Value** *(string) --* 

                  The value for this tag.

                  
            
          
        
      
        

        - **NextPageToken** *(string) --* 

          The page token to use to retrieve the next set of results. If there are no additional results, this value is null.

          
    

  .. py:method:: list_resources_for_tag_option(**kwargs)

    

    Lists the resources associated with the specified TagOption.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListResourcesForTagOption>`_    


    **Request Syntax** 
    ::

      response = client.list_resources_for_tag_option(
          TagOptionId='string',
          ResourceType='string',
          PageSize=123,
          PageToken='string'
      )
    :type TagOptionId: string
    :param TagOptionId: **[REQUIRED]** 

      The TagOption identifier.

      

    
    :type ResourceType: string
    :param ResourceType: 

      The resource type.

       

       
      * ``Portfolio``   
       
      * ``Product``   
       

      

    
    :type PageSize: integer
    :param PageSize: 

      The maximum number of items to return with this call.

      

    
    :type PageToken: string
    :param PageToken: 

      The page token for the next set of results. To retrieve the first set of results, use null.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ResourceDetails': [
                {
                    'Id': 'string',
                    'ARN': 'string',
                    'Name': 'string',
                    'Description': 'string',
                    'CreatedTime': datetime(2015, 1, 1)
                },
            ],
            'PageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ResourceDetails** *(list) --* 

          Information about the resources.

          
          

          - *(dict) --* 

            Information about a resource.

            
            

            - **Id** *(string) --* 

              The identifier of the resource.

              
            

            - **ARN** *(string) --* 

              The ARN of the resource.

              
            

            - **Name** *(string) --* 

              The name of the resource.

              
            

            - **Description** *(string) --* 

              The description of the resource.

              
            

            - **CreatedTime** *(datetime) --* 

              The creation time of the resource.

              
        
      
        

        - **PageToken** *(string) --* 

          The page token for the next set of results. To retrieve the first set of results, use null.

          
    

  .. py:method:: list_tag_options(**kwargs)

    

    Lists the specified TagOptions or all TagOptions.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ListTagOptions>`_    


    **Request Syntax** 
    ::

      response = client.list_tag_options(
          Filters={
              'Key': 'string',
              'Value': 'string',
              'Active': True|False
          },
          PageSize=123,
          PageToken='string'
      )
    :type Filters: dict
    :param Filters: 

      The search filters. If no search filters are specified, the output includes all TagOptions.

      

    
      - **Key** *(string) --* 

        The TagOption key.

        

      
      - **Value** *(string) --* 

        The TagOption value.

        

      
      - **Active** *(boolean) --* 

        The active state.

        

      
    
    :type PageSize: integer
    :param PageSize: 

      The maximum number of items to return with this call.

      

    
    :type PageToken: string
    :param PageToken: 

      The page token for the next set of results. To retrieve the first set of results, use null.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TagOptionDetails': [
                {
                    'Key': 'string',
                    'Value': 'string',
                    'Active': True|False,
                    'Id': 'string'
                },
            ],
            'PageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TagOptionDetails** *(list) --* 

          Information about the TagOptions.

          
          

          - *(dict) --* 

            Information about a TagOption.

            
            

            - **Key** *(string) --* 

              The TagOption key.

              
            

            - **Value** *(string) --* 

              The TagOption value.

              
            

            - **Active** *(boolean) --* 

              The TagOption active state.

              
            

            - **Id** *(string) --* 

              The TagOption identifier.

              
        
      
        

        - **PageToken** *(string) --* 

          The page token for the next set of results. To retrieve the first set of results, use null.

          
    

  .. py:method:: provision_product(**kwargs)

    

    Provisions the specified product.

     

    A provisioned product is a resourced instance of a product. For example, provisioning a product based on a CloudFormation template launches a CloudFormation stack and its underlying resources. You can check the status of this request using  DescribeRecord .

     

    If the request contains a tag key with an empty list of values, there is a tag conflict for that key. Do not include conflicted keys as tags, or this will cause the error "Parameter validation failed: Missing required parameter in Tags[*N* ]:*Value* ".

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ProvisionProduct>`_    


    **Request Syntax** 
    ::

      response = client.provision_product(
          AcceptLanguage='string',
          ProductId='string',
          ProvisioningArtifactId='string',
          PathId='string',
          ProvisionedProductName='string',
          ProvisioningParameters=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ],
          Tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ],
          NotificationArns=[
              'string',
          ],
          ProvisionToken='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type ProductId: string
    :param ProductId: **[REQUIRED]** 

      The product identifier.

      

    
    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: **[REQUIRED]** 

      The identifier of the provisioning artifact.

      

    
    :type PathId: string
    :param PathId: 

      The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use  ListLaunchPaths .

      

    
    :type ProvisionedProductName: string
    :param ProvisionedProductName: **[REQUIRED]** 

      A user-friendly name for the provisioned product. This value must be unique for the AWS account and cannot be updated after the product is provisioned.

      

    
    :type ProvisioningParameters: list
    :param ProvisioningParameters: 

      Parameters specified by the administrator that are required for provisioning the product.

      

    
      - *(dict) --* 

        Information about a parameter used to provision a product.

        

      
        - **Key** *(string) --* 

          The parameter key.

          

        
        - **Value** *(string) --* 

          The parameter value.

          

        
      
  
    :type Tags: list
    :param Tags: 

      The tags to use as provisioning options.

      

    
      - *(dict) --* 

        Information about a tag. A tag is a key-value pair. Tags are entirely discretionary and are propagated to the resources created when provisioning a product.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The tag key.

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          The value for this key.

          

        
      
  
    :type NotificationArns: list
    :param NotificationArns: 

      Passed to CloudFormation. The SNS topic ARNs to which to publish stack-related events.

      

    
      - *(string) --* 

      
  
    :type ProvisionToken: string
    :param ProvisionToken: **[REQUIRED]** 

      An idempotency token that uniquely identifies the provisioning request.

      This field is autopopulated if not provided.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'RecordDetail': {
                'RecordId': 'string',
                'ProvisionedProductName': 'string',
                'Status': 'CREATED'|'IN_PROGRESS'|'IN_PROGRESS_IN_ERROR'|'SUCCEEDED'|'FAILED',
                'CreatedTime': datetime(2015, 1, 1),
                'UpdatedTime': datetime(2015, 1, 1),
                'ProvisionedProductType': 'string',
                'RecordType': 'string',
                'ProvisionedProductId': 'string',
                'ProductId': 'string',
                'ProvisioningArtifactId': 'string',
                'PathId': 'string',
                'RecordErrors': [
                    {
                        'Code': 'string',
                        'Description': 'string'
                    },
                ],
                'RecordTags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **RecordDetail** *(dict) --* 

          Information about the result of  ProvisionProduct .

          
          

          - **RecordId** *(string) --* 

            The identifier of the record.

            
          

          - **ProvisionedProductName** *(string) --* 

            The user-friendly name of the provisioned product.

            
          

          - **Status** *(string) --* 

            The status of the provisioned product.

             

             
            * ``CREATED`` - The request was created but the operation has not started. 
             
            * ``IN_PROGRESS`` - The requested operation is in progress. 
             
            * ``IN_PROGRESS_IN_ERROR`` - The provisioned product is under change but the requested operation failed and some remediation is occurring. For example, a rollback. 
             
            * ``SUCCEEDED`` - The requested operation has successfully completed. 
             
            * ``FAILED`` - The requested operation has unsuccessfully completed. Investigate using the error messages returned. 
             

            
          

          - **CreatedTime** *(datetime) --* 

            The UTC timestamp of the creation time.

            
          

          - **UpdatedTime** *(datetime) --* 

            The time when the record was last updated.

            
          

          - **ProvisionedProductType** *(string) --* 

            The type of provisioned product. The supported value is ``CFN_STACK`` .

            
          

          - **RecordType** *(string) --* 

            The record type for this record.

             

             
            * ``PROVISION_PRODUCT``   
             
            * ``UPDATE_PROVISIONED_PRODUCT``   
             
            * ``TERMINATE_PROVISIONED_PRODUCT``   
             

            
          

          - **ProvisionedProductId** *(string) --* 

            The identifier of the provisioned product.

            
          

          - **ProductId** *(string) --* 

            The product identifier.

            
          

          - **ProvisioningArtifactId** *(string) --* 

            The identifier of the provisioning artifact.

            
          

          - **PathId** *(string) --* 

            The path identifier.

            
          

          - **RecordErrors** *(list) --* 

            The errors that occurred while processing the request.

            
            

            - *(dict) --* 

              The error code and description resulting from an operation.

              
              

              - **Code** *(string) --* 

                The numeric value of the error.

                
              

              - **Description** *(string) --* 

                The description of the error.

                
          
        
          

          - **RecordTags** *(list) --* 

            The tags associated with this record.

            
            

            - *(dict) --* 

              A tag associated with the record, stored as a key-value pair.

              
              

              - **Key** *(string) --* 

                The key for this tag.

                
              

              - **Value** *(string) --* 

                The value for this tag.

                
          
        
      
    

  .. py:method:: reject_portfolio_share(**kwargs)

    

    Rejects an offer to share the specified portfolio.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/RejectPortfolioShare>`_    


    **Request Syntax** 
    ::

      response = client.reject_portfolio_share(
          AcceptLanguage='string',
          PortfolioId='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type PortfolioId: string
    :param PortfolioId: **[REQUIRED]** 

      The portfolio identifier.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: scan_provisioned_products(**kwargs)

    

    Lists the provisioned products that are available (not terminated).

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/ScanProvisionedProducts>`_    


    **Request Syntax** 
    ::

      response = client.scan_provisioned_products(
          AcceptLanguage='string',
          AccessLevelFilter={
              'Key': 'Account'|'Role'|'User',
              'Value': 'string'
          },
          PageSize=123,
          PageToken='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type AccessLevelFilter: dict
    :param AccessLevelFilter: 

      The access level to use to obtain results. The default is ``User`` .

      

    
      - **Key** *(string) --* 

        The access level.

         

         
        * ``Account`` - Filter results based on the account. 
         
        * ``Role`` - Filter results based on the federated role of the specified user. 
         
        * ``User`` - Filter results based on the specified user. 
         

        

      
      - **Value** *(string) --* 

        The user to which the access level applies. The only supported value is ``Self`` .

        

      
    
    :type PageSize: integer
    :param PageSize: 

      The maximum number of items to return with this call.

      

    
    :type PageToken: string
    :param PageToken: 

      The page token for the next set of results. To retrieve the first set of results, use null.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ProvisionedProducts': [
                {
                    'Name': 'string',
                    'Arn': 'string',
                    'Type': 'string',
                    'Id': 'string',
                    'Status': 'AVAILABLE'|'UNDER_CHANGE'|'TAINTED'|'ERROR',
                    'StatusMessage': 'string',
                    'CreatedTime': datetime(2015, 1, 1),
                    'IdempotencyToken': 'string',
                    'LastRecordId': 'string'
                },
            ],
            'NextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ProvisionedProducts** *(list) --* 

          Information about the provisioned products.

          
          

          - *(dict) --* 

            Information about a provisioned product.

            
            

            - **Name** *(string) --* 

              The user-friendly name of the provisioned product.

              
            

            - **Arn** *(string) --* 

              The ARN of the provisioned product.

              
            

            - **Type** *(string) --* 

              The type of provisioned product. The supported value is ``CFN_STACK`` .

              
            

            - **Id** *(string) --* 

              The identifier of the provisioned product.

              
            

            - **Status** *(string) --* 

              The current status of the provisioned product.

               

               
              * ``AVAILABLE`` - Stable state, ready to perform any operation. The most recent operation succeeded and completed. 
               
              * ``UNDER_CHANGE`` - Transitive state, operations performed might not have valid results. Wait for an ``AVAILABLE`` status before performing operations. 
               
              * ``TAINTED`` - Stable state, ready to perform any operation. The stack has completed the requested operation but is not exactly what was requested. For example, a request to update to a new version failed and the stack rolled back to the current version. 
               
              * ``ERROR`` - An unexpected error occurred, the provisioned product exists but the stack is not running. For example, CloudFormation received a parameter value that was not valid and could not launch the stack. 
               

              
            

            - **StatusMessage** *(string) --* 

              The current status message of the provisioned product.

              
            

            - **CreatedTime** *(datetime) --* 

              The UTC timestamp of the creation time.

              
            

            - **IdempotencyToken** *(string) --* 

              A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.

              
            

            - **LastRecordId** *(string) --* 

              The record identifier of the last request performed on this provisioned product.

              
        
      
        

        - **NextPageToken** *(string) --* 

          The page token to use to retrieve the next set of results. If there are no additional results, this value is null.

          
    

  .. py:method:: search_products(**kwargs)

    

    Gets information about the products to which the caller has access.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/SearchProducts>`_    


    **Request Syntax** 
    ::

      response = client.search_products(
          AcceptLanguage='string',
          Filters={
              'string': [
                  'string',
              ]
          },
          PageSize=123,
          SortBy='Title'|'VersionCount'|'CreationDate',
          SortOrder='ASCENDING'|'DESCENDING',
          PageToken='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type Filters: dict
    :param Filters: 

      The search filters. If no search filters are specified, the output includes all products to which the caller has access.

      

    
      - *(string) --* 

      
        - *(list) --* 

        
          - *(string) --* 

          
      
  

    :type PageSize: integer
    :param PageSize: 

      The maximum number of items to return with this call.

      

    
    :type SortBy: string
    :param SortBy: 

      The sort field. If no value is specified, the results are not sorted.

      

    
    :type SortOrder: string
    :param SortOrder: 

      The sort order. If no value is specified, the results are not sorted.

      

    
    :type PageToken: string
    :param PageToken: 

      The page token for the next set of results. To retrieve the first set of results, use null.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ProductViewSummaries': [
                {
                    'Id': 'string',
                    'ProductId': 'string',
                    'Name': 'string',
                    'Owner': 'string',
                    'ShortDescription': 'string',
                    'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE',
                    'Distributor': 'string',
                    'HasDefaultPath': True|False,
                    'SupportEmail': 'string',
                    'SupportDescription': 'string',
                    'SupportUrl': 'string'
                },
            ],
            'ProductViewAggregations': {
                'string': [
                    {
                        'Value': 'string',
                        'ApproximateCount': 123
                    },
                ]
            },
            'NextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ProductViewSummaries** *(list) --* 

          Information about the product views.

          
          

          - *(dict) --* 

            Summary information about a product view.

            
            

            - **Id** *(string) --* 

              The product view identifier.

              
            

            - **ProductId** *(string) --* 

              The product identifier.

              
            

            - **Name** *(string) --* 

              The name of the product.

              
            

            - **Owner** *(string) --* 

              The owner of the product. Contact the product administrator for the significance of this value.

              
            

            - **ShortDescription** *(string) --* 

              Short description of the product.

              
            

            - **Type** *(string) --* 

              The product type. Contact the product administrator for the significance of this value. If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

              
            

            - **Distributor** *(string) --* 

              The distributor of the product. Contact the product administrator for the significance of this value.

              
            

            - **HasDefaultPath** *(boolean) --* 

              Indicates whether the product has a default path. If the product does not have a default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is not required, and the output of  ProductViewSummary can be used directly with  DescribeProvisioningParameters .

              
            

            - **SupportEmail** *(string) --* 

              The email contact information to obtain support for this Product.

              
            

            - **SupportDescription** *(string) --* 

              The description of the support for this Product.

              
            

            - **SupportUrl** *(string) --* 

              The URL information to obtain support for this Product.

              
        
      
        

        - **ProductViewAggregations** *(dict) --* 

          The product view aggregations.

          
          

          - *(string) --* 
            

            - *(list) --* 
              

              - *(dict) --* 

                A single product view aggregation value/count pair, containing metadata about each product to which the calling user has access.

                
                

                - **Value** *(string) --* 

                  The value of the product view aggregation.

                  
                

                - **ApproximateCount** *(integer) --* 

                  An approximate count of the products that match the value.

                  
            
          
      
    
        

        - **NextPageToken** *(string) --* 

          The page token to use to retrieve the next set of results. If there are no additional results, this value is null.

          
    

  .. py:method:: search_products_as_admin(**kwargs)

    

    Gets information about the products for the specified portfolio or all products.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/SearchProductsAsAdmin>`_    


    **Request Syntax** 
    ::

      response = client.search_products_as_admin(
          AcceptLanguage='string',
          PortfolioId='string',
          Filters={
              'string': [
                  'string',
              ]
          },
          SortBy='Title'|'VersionCount'|'CreationDate',
          SortOrder='ASCENDING'|'DESCENDING',
          PageToken='string',
          PageSize=123,
          ProductSource='ACCOUNT'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type PortfolioId: string
    :param PortfolioId: 

      The portfolio identifier.

      

    
    :type Filters: dict
    :param Filters: 

      The search filters. If no search filters are specified, the output includes all products to which the administrator has access.

      

    
      - *(string) --* 

      
        - *(list) --* 

        
          - *(string) --* 

          
      
  

    :type SortBy: string
    :param SortBy: 

      The sort field. If no value is specified, the results are not sorted.

      

    
    :type SortOrder: string
    :param SortOrder: 

      The sort order. If no value is specified, the results are not sorted.

      

    
    :type PageToken: string
    :param PageToken: 

      The page token for the next set of results. To retrieve the first set of results, use null.

      

    
    :type PageSize: integer
    :param PageSize: 

      The maximum number of items to return with this call.

      

    
    :type ProductSource: string
    :param ProductSource: 

      Access level of the source of the product.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ProductViewDetails': [
                {
                    'ProductViewSummary': {
                        'Id': 'string',
                        'ProductId': 'string',
                        'Name': 'string',
                        'Owner': 'string',
                        'ShortDescription': 'string',
                        'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE',
                        'Distributor': 'string',
                        'HasDefaultPath': True|False,
                        'SupportEmail': 'string',
                        'SupportDescription': 'string',
                        'SupportUrl': 'string'
                    },
                    'Status': 'AVAILABLE'|'CREATING'|'FAILED',
                    'ProductARN': 'string',
                    'CreatedTime': datetime(2015, 1, 1)
                },
            ],
            'NextPageToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ProductViewDetails** *(list) --* 

          Information about the product views.

          
          

          - *(dict) --* 

            Information about a product view.

            
            

            - **ProductViewSummary** *(dict) --* 

              Summary information about the product view.

              
              

              - **Id** *(string) --* 

                The product view identifier.

                
              

              - **ProductId** *(string) --* 

                The product identifier.

                
              

              - **Name** *(string) --* 

                The name of the product.

                
              

              - **Owner** *(string) --* 

                The owner of the product. Contact the product administrator for the significance of this value.

                
              

              - **ShortDescription** *(string) --* 

                Short description of the product.

                
              

              - **Type** *(string) --* 

                The product type. Contact the product administrator for the significance of this value. If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

                
              

              - **Distributor** *(string) --* 

                The distributor of the product. Contact the product administrator for the significance of this value.

                
              

              - **HasDefaultPath** *(boolean) --* 

                Indicates whether the product has a default path. If the product does not have a default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is not required, and the output of  ProductViewSummary can be used directly with  DescribeProvisioningParameters .

                
              

              - **SupportEmail** *(string) --* 

                The email contact information to obtain support for this Product.

                
              

              - **SupportDescription** *(string) --* 

                The description of the support for this Product.

                
              

              - **SupportUrl** *(string) --* 

                The URL information to obtain support for this Product.

                
          
            

            - **Status** *(string) --* 

              The status of the product.

               

               
              * ``AVAILABLE`` - The product is ready for use. 
               
              * ``CREATING`` - Product creation has started; the product is not ready for use. 
               
              * ``FAILED`` - An action failed. 
               

              
            

            - **ProductARN** *(string) --* 

              The ARN of the product.

              
            

            - **CreatedTime** *(datetime) --* 

              The UTC timestamp of the creation time.

              
        
      
        

        - **NextPageToken** *(string) --* 

          The page token to use to retrieve the next set of results. If there are no additional results, this value is null.

          
    

  .. py:method:: terminate_provisioned_product(**kwargs)

    

    Terminates the specified provisioned product.

     

    This operation does not delete any records associated with the provisioned product.

     

    You can check the status of this request using  DescribeRecord .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/TerminateProvisionedProduct>`_    


    **Request Syntax** 
    ::

      response = client.terminate_provisioned_product(
          ProvisionedProductName='string',
          ProvisionedProductId='string',
          TerminateToken='string',
          IgnoreErrors=True|False,
          AcceptLanguage='string'
      )
    :type ProvisionedProductName: string
    :param ProvisionedProductName: 

      The name of the provisioned product. You cannot specify both ``ProvisionedProductName`` and ``ProvisionedProductId`` .

      

    
    :type ProvisionedProductId: string
    :param ProvisionedProductId: 

      The identifier of the provisioned product. You cannot specify both ``ProvisionedProductName`` and ``ProvisionedProductId`` .

      

    
    :type TerminateToken: string
    :param TerminateToken: **[REQUIRED]** 

      An idempotency token that uniquely identifies the termination request. This token is only valid during the termination process. After the provisioned product is terminated, subsequent requests to terminate the same provisioned product always return **ResourceNotFound** .

      This field is autopopulated if not provided.

    
    :type IgnoreErrors: boolean
    :param IgnoreErrors: 

      If set to true, AWS Service Catalog stops managing the specified provisioned product even if it cannot delete the underlying resources.

      

    
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'RecordDetail': {
                'RecordId': 'string',
                'ProvisionedProductName': 'string',
                'Status': 'CREATED'|'IN_PROGRESS'|'IN_PROGRESS_IN_ERROR'|'SUCCEEDED'|'FAILED',
                'CreatedTime': datetime(2015, 1, 1),
                'UpdatedTime': datetime(2015, 1, 1),
                'ProvisionedProductType': 'string',
                'RecordType': 'string',
                'ProvisionedProductId': 'string',
                'ProductId': 'string',
                'ProvisioningArtifactId': 'string',
                'PathId': 'string',
                'RecordErrors': [
                    {
                        'Code': 'string',
                        'Description': 'string'
                    },
                ],
                'RecordTags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **RecordDetail** *(dict) --* 

          Information about the result of this request.

          
          

          - **RecordId** *(string) --* 

            The identifier of the record.

            
          

          - **ProvisionedProductName** *(string) --* 

            The user-friendly name of the provisioned product.

            
          

          - **Status** *(string) --* 

            The status of the provisioned product.

             

             
            * ``CREATED`` - The request was created but the operation has not started. 
             
            * ``IN_PROGRESS`` - The requested operation is in progress. 
             
            * ``IN_PROGRESS_IN_ERROR`` - The provisioned product is under change but the requested operation failed and some remediation is occurring. For example, a rollback. 
             
            * ``SUCCEEDED`` - The requested operation has successfully completed. 
             
            * ``FAILED`` - The requested operation has unsuccessfully completed. Investigate using the error messages returned. 
             

            
          

          - **CreatedTime** *(datetime) --* 

            The UTC timestamp of the creation time.

            
          

          - **UpdatedTime** *(datetime) --* 

            The time when the record was last updated.

            
          

          - **ProvisionedProductType** *(string) --* 

            The type of provisioned product. The supported value is ``CFN_STACK`` .

            
          

          - **RecordType** *(string) --* 

            The record type for this record.

             

             
            * ``PROVISION_PRODUCT``   
             
            * ``UPDATE_PROVISIONED_PRODUCT``   
             
            * ``TERMINATE_PROVISIONED_PRODUCT``   
             

            
          

          - **ProvisionedProductId** *(string) --* 

            The identifier of the provisioned product.

            
          

          - **ProductId** *(string) --* 

            The product identifier.

            
          

          - **ProvisioningArtifactId** *(string) --* 

            The identifier of the provisioning artifact.

            
          

          - **PathId** *(string) --* 

            The path identifier.

            
          

          - **RecordErrors** *(list) --* 

            The errors that occurred while processing the request.

            
            

            - *(dict) --* 

              The error code and description resulting from an operation.

              
              

              - **Code** *(string) --* 

                The numeric value of the error.

                
              

              - **Description** *(string) --* 

                The description of the error.

                
          
        
          

          - **RecordTags** *(list) --* 

            The tags associated with this record.

            
            

            - *(dict) --* 

              A tag associated with the record, stored as a key-value pair.

              
              

              - **Key** *(string) --* 

                The key for this tag.

                
              

              - **Value** *(string) --* 

                The value for this tag.

                
          
        
      
    

  .. py:method:: update_constraint(**kwargs)

    

    Updates the specified constraint.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/UpdateConstraint>`_    


    **Request Syntax** 
    ::

      response = client.update_constraint(
          AcceptLanguage='string',
          Id='string',
          Description='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type Id: string
    :param Id: **[REQUIRED]** 

      The identifier of the constraint.

      

    
    :type Description: string
    :param Description: 

      The updated description of the constraint.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ConstraintDetail': {
                'ConstraintId': 'string',
                'Type': 'string',
                'Description': 'string',
                'Owner': 'string'
            },
            'ConstraintParameters': 'string',
            'Status': 'AVAILABLE'|'CREATING'|'FAILED'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ConstraintDetail** *(dict) --* 

          Information about the constraint.

          
          

          - **ConstraintId** *(string) --* 

            The identifier of the constraint.

            
          

          - **Type** *(string) --* 

            The type of constraint.

             

             
            * ``LAUNCH``   
             
            * ``NOTIFICATION``   
             
            * ``TEMPLATE``   
             

            
          

          - **Description** *(string) --* 

            The description of the constraint.

            
          

          - **Owner** *(string) --* 

            The owner of the constraint.

            
      
        

        - **ConstraintParameters** *(string) --* 

          The constraint parameters.

          
        

        - **Status** *(string) --* 

          The status of the current request.

          
    

  .. py:method:: update_portfolio(**kwargs)

    

    Updates the specified portfolio.

     

    You cannot update a product that was shared with you.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/UpdatePortfolio>`_    


    **Request Syntax** 
    ::

      response = client.update_portfolio(
          AcceptLanguage='string',
          Id='string',
          DisplayName='string',
          Description='string',
          ProviderName='string',
          AddTags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ],
          RemoveTags=[
              'string',
          ]
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type Id: string
    :param Id: **[REQUIRED]** 

      The portfolio identifier.

      

    
    :type DisplayName: string
    :param DisplayName: 

      The name to use for display purposes.

      

    
    :type Description: string
    :param Description: 

      The updated description of the portfolio.

      

    
    :type ProviderName: string
    :param ProviderName: 

      The updated name of the portfolio provider.

      

    
    :type AddTags: list
    :param AddTags: 

      The tags to add.

      

    
      - *(dict) --* 

        Information about a tag. A tag is a key-value pair. Tags are entirely discretionary and are propagated to the resources created when provisioning a product.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The tag key.

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          The value for this key.

          

        
      
  
    :type RemoveTags: list
    :param RemoveTags: 

      The tags to remove.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'PortfolioDetail': {
                'Id': 'string',
                'ARN': 'string',
                'DisplayName': 'string',
                'Description': 'string',
                'CreatedTime': datetime(2015, 1, 1),
                'ProviderName': 'string'
            },
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **PortfolioDetail** *(dict) --* 

          Information about the portfolio.

          
          

          - **Id** *(string) --* 

            The portfolio identifier.

            
          

          - **ARN** *(string) --* 

            The ARN assigned to the portfolio.

            
          

          - **DisplayName** *(string) --* 

            The name to use for display purposes.

            
          

          - **Description** *(string) --* 

            The description of the portfolio.

            
          

          - **CreatedTime** *(datetime) --* 

            The UTC timestamp of the creation time.

            
          

          - **ProviderName** *(string) --* 

            The name of the portfolio provider.

            
      
        

        - **Tags** *(list) --* 

          Information about the tags associated with the portfolio.

          
          

          - *(dict) --* 

            Information about a tag. A tag is a key-value pair. Tags are entirely discretionary and are propagated to the resources created when provisioning a product.

            
            

            - **Key** *(string) --* 

              The tag key.

              
            

            - **Value** *(string) --* 

              The value for this key.

              
        
      
    

  .. py:method:: update_product(**kwargs)

    

    Updates the specified product.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/UpdateProduct>`_    


    **Request Syntax** 
    ::

      response = client.update_product(
          AcceptLanguage='string',
          Id='string',
          Name='string',
          Owner='string',
          Description='string',
          Distributor='string',
          SupportDescription='string',
          SupportEmail='string',
          SupportUrl='string',
          AddTags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ],
          RemoveTags=[
              'string',
          ]
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type Id: string
    :param Id: **[REQUIRED]** 

      The product identifier.

      

    
    :type Name: string
    :param Name: 

      The updated product name.

      

    
    :type Owner: string
    :param Owner: 

      The updated owner of the product.

      

    
    :type Description: string
    :param Description: 

      The updated description of the product.

      

    
    :type Distributor: string
    :param Distributor: 

      The updated distributor of the product.

      

    
    :type SupportDescription: string
    :param SupportDescription: 

      The updated support description for the product.

      

    
    :type SupportEmail: string
    :param SupportEmail: 

      The updated support email for the product.

      

    
    :type SupportUrl: string
    :param SupportUrl: 

      The updated support URL for the product.

      

    
    :type AddTags: list
    :param AddTags: 

      The tags to add to the product.

      

    
      - *(dict) --* 

        Information about a tag. A tag is a key-value pair. Tags are entirely discretionary and are propagated to the resources created when provisioning a product.

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The tag key.

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          The value for this key.

          

        
      
  
    :type RemoveTags: list
    :param RemoveTags: 

      The tags to remove from the product.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ProductViewDetail': {
                'ProductViewSummary': {
                    'Id': 'string',
                    'ProductId': 'string',
                    'Name': 'string',
                    'Owner': 'string',
                    'ShortDescription': 'string',
                    'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE',
                    'Distributor': 'string',
                    'HasDefaultPath': True|False,
                    'SupportEmail': 'string',
                    'SupportDescription': 'string',
                    'SupportUrl': 'string'
                },
                'Status': 'AVAILABLE'|'CREATING'|'FAILED',
                'ProductARN': 'string',
                'CreatedTime': datetime(2015, 1, 1)
            },
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ProductViewDetail** *(dict) --* 

          Information about the product view.

          
          

          - **ProductViewSummary** *(dict) --* 

            Summary information about the product view.

            
            

            - **Id** *(string) --* 

              The product view identifier.

              
            

            - **ProductId** *(string) --* 

              The product identifier.

              
            

            - **Name** *(string) --* 

              The name of the product.

              
            

            - **Owner** *(string) --* 

              The owner of the product. Contact the product administrator for the significance of this value.

              
            

            - **ShortDescription** *(string) --* 

              Short description of the product.

              
            

            - **Type** *(string) --* 

              The product type. Contact the product administrator for the significance of this value. If this value is ``MARKETPLACE`` , the product was created by AWS Marketplace.

              
            

            - **Distributor** *(string) --* 

              The distributor of the product. Contact the product administrator for the significance of this value.

              
            

            - **HasDefaultPath** *(boolean) --* 

              Indicates whether the product has a default path. If the product does not have a default path, call  ListLaunchPaths to disambiguate between paths. Otherwise,  ListLaunchPaths is not required, and the output of  ProductViewSummary can be used directly with  DescribeProvisioningParameters .

              
            

            - **SupportEmail** *(string) --* 

              The email contact information to obtain support for this Product.

              
            

            - **SupportDescription** *(string) --* 

              The description of the support for this Product.

              
            

            - **SupportUrl** *(string) --* 

              The URL information to obtain support for this Product.

              
        
          

          - **Status** *(string) --* 

            The status of the product.

             

             
            * ``AVAILABLE`` - The product is ready for use. 
             
            * ``CREATING`` - Product creation has started; the product is not ready for use. 
             
            * ``FAILED`` - An action failed. 
             

            
          

          - **ProductARN** *(string) --* 

            The ARN of the product.

            
          

          - **CreatedTime** *(datetime) --* 

            The UTC timestamp of the creation time.

            
      
        

        - **Tags** *(list) --* 

          Information about the tags associated with the product.

          
          

          - *(dict) --* 

            Information about a tag. A tag is a key-value pair. Tags are entirely discretionary and are propagated to the resources created when provisioning a product.

            
            

            - **Key** *(string) --* 

              The tag key.

              
            

            - **Value** *(string) --* 

              The value for this key.

              
        
      
    

  .. py:method:: update_provisioned_product(**kwargs)

    

    Requests updates to the configuration of the specified provisioned product.

     

    If there are tags associated with the object, they cannot be updated or added. Depending on the specific updates requested, this operation can update with no interruption, with some interruption, or replace the provisioned product entirely.

     

    You can check the status of this request using  DescribeRecord .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/UpdateProvisionedProduct>`_    


    **Request Syntax** 
    ::

      response = client.update_provisioned_product(
          AcceptLanguage='string',
          ProvisionedProductName='string',
          ProvisionedProductId='string',
          ProductId='string',
          ProvisioningArtifactId='string',
          PathId='string',
          ProvisioningParameters=[
              {
                  'Key': 'string',
                  'Value': 'string',
                  'UsePreviousValue': True|False
              },
          ],
          UpdateToken='string'
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type ProvisionedProductName: string
    :param ProvisionedProductName: 

      The updated name of the provisioned product. You cannot specify both ``ProvisionedProductName`` and ``ProvisionedProductId`` .

      

    
    :type ProvisionedProductId: string
    :param ProvisionedProductId: 

      The identifier of the provisioned product. You cannot specify both ``ProvisionedProductName`` and ``ProvisionedProductId`` .

      

    
    :type ProductId: string
    :param ProductId: 

      The identifier of the provisioned product.

      

    
    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: 

      The identifier of the provisioning artifact.

      

    
    :type PathId: string
    :param PathId: 

      The new path identifier. This value is optional if the product has a default path, and required if the product has more than one path.

      

    
    :type ProvisioningParameters: list
    :param ProvisioningParameters: 

      The new parameters.

      

    
      - *(dict) --* 

        The parameter key-value pair used to update a provisioned product.

        

      
        - **Key** *(string) --* 

          The parameter key.

          

        
        - **Value** *(string) --* 

          The parameter value.

          

        
        - **UsePreviousValue** *(boolean) --* 

          If set to true, ``Value`` is ignored and the previous parameter value is kept.

          

        
      
  
    :type UpdateToken: string
    :param UpdateToken: **[REQUIRED]** 

      The idempotency token that uniquely identifies the provisioning update rquest.

      This field is autopopulated if not provided.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'RecordDetail': {
                'RecordId': 'string',
                'ProvisionedProductName': 'string',
                'Status': 'CREATED'|'IN_PROGRESS'|'IN_PROGRESS_IN_ERROR'|'SUCCEEDED'|'FAILED',
                'CreatedTime': datetime(2015, 1, 1),
                'UpdatedTime': datetime(2015, 1, 1),
                'ProvisionedProductType': 'string',
                'RecordType': 'string',
                'ProvisionedProductId': 'string',
                'ProductId': 'string',
                'ProvisioningArtifactId': 'string',
                'PathId': 'string',
                'RecordErrors': [
                    {
                        'Code': 'string',
                        'Description': 'string'
                    },
                ],
                'RecordTags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **RecordDetail** *(dict) --* 

          Information about the result of the request.

          
          

          - **RecordId** *(string) --* 

            The identifier of the record.

            
          

          - **ProvisionedProductName** *(string) --* 

            The user-friendly name of the provisioned product.

            
          

          - **Status** *(string) --* 

            The status of the provisioned product.

             

             
            * ``CREATED`` - The request was created but the operation has not started. 
             
            * ``IN_PROGRESS`` - The requested operation is in progress. 
             
            * ``IN_PROGRESS_IN_ERROR`` - The provisioned product is under change but the requested operation failed and some remediation is occurring. For example, a rollback. 
             
            * ``SUCCEEDED`` - The requested operation has successfully completed. 
             
            * ``FAILED`` - The requested operation has unsuccessfully completed. Investigate using the error messages returned. 
             

            
          

          - **CreatedTime** *(datetime) --* 

            The UTC timestamp of the creation time.

            
          

          - **UpdatedTime** *(datetime) --* 

            The time when the record was last updated.

            
          

          - **ProvisionedProductType** *(string) --* 

            The type of provisioned product. The supported value is ``CFN_STACK`` .

            
          

          - **RecordType** *(string) --* 

            The record type for this record.

             

             
            * ``PROVISION_PRODUCT``   
             
            * ``UPDATE_PROVISIONED_PRODUCT``   
             
            * ``TERMINATE_PROVISIONED_PRODUCT``   
             

            
          

          - **ProvisionedProductId** *(string) --* 

            The identifier of the provisioned product.

            
          

          - **ProductId** *(string) --* 

            The product identifier.

            
          

          - **ProvisioningArtifactId** *(string) --* 

            The identifier of the provisioning artifact.

            
          

          - **PathId** *(string) --* 

            The path identifier.

            
          

          - **RecordErrors** *(list) --* 

            The errors that occurred while processing the request.

            
            

            - *(dict) --* 

              The error code and description resulting from an operation.

              
              

              - **Code** *(string) --* 

                The numeric value of the error.

                
              

              - **Description** *(string) --* 

                The description of the error.

                
          
        
          

          - **RecordTags** *(list) --* 

            The tags associated with this record.

            
            

            - *(dict) --* 

              A tag associated with the record, stored as a key-value pair.

              
              

              - **Key** *(string) --* 

                The key for this tag.

                
              

              - **Value** *(string) --* 

                The value for this tag.

                
          
        
      
    

  .. py:method:: update_provisioning_artifact(**kwargs)

    

    Updates the specified provisioning artifact (also known as a version) for the specified product.

     

    You cannot update a provisioning artifact for a product that was shared with you.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/UpdateProvisioningArtifact>`_    


    **Request Syntax** 
    ::

      response = client.update_provisioning_artifact(
          AcceptLanguage='string',
          ProductId='string',
          ProvisioningArtifactId='string',
          Name='string',
          Description='string',
          Active=True|False
      )
    :type AcceptLanguage: string
    :param AcceptLanguage: 

      The language code.

       

       
      * ``en`` - English (default) 
       
      * ``jp`` - Japanese 
       
      * ``zh`` - Chinese 
       

      

    
    :type ProductId: string
    :param ProductId: **[REQUIRED]** 

      The product identifier.

      

    
    :type ProvisioningArtifactId: string
    :param ProvisioningArtifactId: **[REQUIRED]** 

      The identifier of the provisioning artifact.

      

    
    :type Name: string
    :param Name: 

      The updated name of the provisioning artifact.

      

    
    :type Description: string
    :param Description: 

      The updated description of the provisioning artifact.

      

    
    :type Active: boolean
    :param Active: 

      Indicates whether the product version is active.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ProvisioningArtifactDetail': {
                'Id': 'string',
                'Name': 'string',
                'Description': 'string',
                'Type': 'CLOUD_FORMATION_TEMPLATE'|'MARKETPLACE_AMI'|'MARKETPLACE_CAR',
                'CreatedTime': datetime(2015, 1, 1),
                'Active': True|False
            },
            'Info': {
                'string': 'string'
            },
            'Status': 'AVAILABLE'|'CREATING'|'FAILED'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ProvisioningArtifactDetail** *(dict) --* 

          Information about the provisioning artifact.

          
          

          - **Id** *(string) --* 

            The identifier of the provisioning artifact.

            
          

          - **Name** *(string) --* 

            The name of the provisioning artifact.

            
          

          - **Description** *(string) --* 

            The description of the provisioning artifact.

            
          

          - **Type** *(string) --* 

            The type of provisioning artifact.

             

             
            * ``CLOUD_FORMATION_TEMPLATE`` - AWS CloudFormation template 
             
            * ``MARKETPLACE_AMI`` - AWS Marketplace AMI 
             
            * ``MARKETPLACE_CAR`` - AWS Marketplace Clusters and AWS Resources 
             

            
          

          - **CreatedTime** *(datetime) --* 

            The UTC timestamp of the creation time.

            
          

          - **Active** *(boolean) --* 

            Indicates whether the product version is active.

            
      
        

        - **Info** *(dict) --* 

          The URL of the CloudFormation template in Amazon S3.

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **Status** *(string) --* 

          The status of the current request.

          
    

  .. py:method:: update_tag_option(**kwargs)

    

    Updates the specified TagOption.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/UpdateTagOption>`_    


    **Request Syntax** 
    ::

      response = client.update_tag_option(
          Id='string',
          Value='string',
          Active=True|False
      )
    :type Id: string
    :param Id: **[REQUIRED]** 

      The TagOption identifier.

      

    
    :type Value: string
    :param Value: 

      The updated value.

      

    
    :type Active: boolean
    :param Active: 

      The updated active state.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TagOptionDetail': {
                'Key': 'string',
                'Value': 'string',
                'Active': True|False,
                'Id': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TagOptionDetail** *(dict) --* 

          Information about the TagOption.

          
          

          - **Key** *(string) --* 

            The TagOption key.

            
          

          - **Value** *(string) --* 

            The TagOption value.

            
          

          - **Active** *(boolean) --* 

            The TagOption active state.

            
          

          - **Id** *(string) --* 

            The TagOption identifier.

            
      
    

==========
Paginators
==========


The available paginators are:
