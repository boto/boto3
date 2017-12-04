

*******************************
ServerlessApplicationRepository
*******************************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: ServerlessApplicationRepository.Client

  A low-level client representing AWSServerlessApplicationRepository::

    
    import boto3
    
    client = boto3.client('serverlessrepo')

  
  These are the available methods:
  
  *   :py:meth:`~ServerlessApplicationRepository.Client.can_paginate`

  
  *   :py:meth:`~ServerlessApplicationRepository.Client.create_application`

  
  *   :py:meth:`~ServerlessApplicationRepository.Client.create_application_version`

  
  *   :py:meth:`~ServerlessApplicationRepository.Client.create_cloud_formation_change_set`

  
  *   :py:meth:`~ServerlessApplicationRepository.Client.generate_presigned_url`

  
  *   :py:meth:`~ServerlessApplicationRepository.Client.get_application`

  
  *   :py:meth:`~ServerlessApplicationRepository.Client.get_application_policy`

  
  *   :py:meth:`~ServerlessApplicationRepository.Client.get_paginator`

  
  *   :py:meth:`~ServerlessApplicationRepository.Client.get_waiter`

  
  *   :py:meth:`~ServerlessApplicationRepository.Client.list_application_versions`

  
  *   :py:meth:`~ServerlessApplicationRepository.Client.list_applications`

  
  *   :py:meth:`~ServerlessApplicationRepository.Client.put_application_policy`

  
  *   :py:meth:`~ServerlessApplicationRepository.Client.update_application`

  

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


  .. py:method:: create_application(**kwargs)

    Creates an application, optionally including an AWS SAM file to create the first application version in the same call.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/CreateApplication>`_    


    **Request Syntax** 
    ::

      response = client.create_application(
          Author='string',
          Description='string',
          Labels=[
              'string',
          ],
          LicenseBody='string',
          LicenseUrl='string',
          Name='string',
          ReadmeBody='string',
          ReadmeUrl='string',
          SemanticVersion='string',
          SourceCodeUrl='string',
          SpdxLicenseId='string',
          TemplateBody='string',
          TemplateUrl='string'
      )
    :type Author: string
    :param Author: The name of the author publishing the app.\nMin Length=1. Max Length=127.\nPattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";

    
    :type Description: string
    :param Description: The description of the application.\nMin Length=1. Max Length=256

    
    :type Labels: list
    :param Labels: Labels to improve discovery of apps in search results.\nMin Length=1. Max Length=127. Maximum number of labels: 10\nPattern: "^[a-zA-Z0-9+\\-_:\\/@]+$";

    
      - *(string) --* 

      
  
    :type LicenseBody: string
    :param LicenseBody: A raw text file that contains the license of the app that matches the spdxLicenseID of your application.\nMax size 5 MB

    
    :type LicenseUrl: string
    :param LicenseUrl: A link to a license file of the app that matches the spdxLicenseID of your application.\nMax size 5 MB

    
    :type Name: string
    :param Name: The name of the application you want to publish.\nMin Length=1. Max Length=140\nPattern: "[a-zA-Z0-9\\-]+";

    
    :type ReadmeBody: string
    :param ReadmeBody: A raw text Readme file that contains a more detailed description of the application and how it works in markdown language.\nMax size 5 MB

    
    :type ReadmeUrl: string
    :param ReadmeUrl: A link to the Readme file that contains a more detailed description of the application and how it works in markdown language.\nMax size 5 MB

    
    :type SemanticVersion: string
    :param SemanticVersion: The semantic version of the application:\n\n https://semver.org/

    
    :type SourceCodeUrl: string
    :param SourceCodeUrl: A link to a public repository for the source code of your application.

    
    :type SpdxLicenseId: string
    :param SpdxLicenseId: A valid identifier from https://spdx.org/licenses/ .

    
    :type TemplateBody: string
    :param TemplateBody: The raw packaged SAM template of your application.

    
    :type TemplateUrl: string
    :param TemplateUrl: A link to the packaged SAM template of your application.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ApplicationId': 'string',
            'Author': 'string',
            'CreationTime': 'string',
            'Description': 'string',
            'Labels': [
                'string',
            ],
            'LicenseUrl': 'string',
            'Name': 'string',
            'ReadmeUrl': 'string',
            'SpdxLicenseId': 'string',
            'Version': {
                'ApplicationId': 'string',
                'CreationTime': 'string',
                'ParameterDefinitions': [
                    {
                        'AllowedPattern': 'string',
                        'AllowedValues': [
                            'string',
                        ],
                        'ConstraintDescription': 'string',
                        'DefaultValue': 'string',
                        'Description': 'string',
                        'MaxLength': 123,
                        'MaxValue': 123,
                        'MinLength': 123,
                        'MinValue': 123,
                        'Name': 'string',
                        'NoEcho': True|False,
                        'ReferencedByResources': [
                            'string',
                        ],
                        'Type': 'string'
                    },
                ],
                'SemanticVersion': 'string',
                'SourceCodeUrl': 'string',
                'TemplateUrl': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* 201 response
        

        - **ApplicationId** *(string) --* The application Amazon Resource Name (ARN).
        

        - **Author** *(string) --* The name of the author publishing the app.\nMin Length=1. Max Length=127.\nPattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";
        

        - **CreationTime** *(string) --* The date/time this resource was created.
        

        - **Description** *(string) --* The description of the application.\nMin Length=1. Max Length=256
        

        - **Labels** *(list) --* Labels to improve discovery of apps in search results.\nMin Length=1. Max Length=127. Maximum number of labels: 10\nPattern: "^[a-zA-Z0-9+\\-_:\\/@]+$";
          

          - *(string) --* 
      
        

        - **LicenseUrl** *(string) --* A link to a license file of the app that matches the spdxLicenseID of your application.\nMax size 5 MB
        

        - **Name** *(string) --* The name of the application.\nMin Length=1. Max Length=140\nPattern: "[a-zA-Z0-9\\-]+";
        

        - **ReadmeUrl** *(string) --* A link to the Readme file that contains a more detailed description of the application and how it works in markdown language.\nMax size 5 MB
        

        - **SpdxLicenseId** *(string) --* A valid identifier from https://spdx.org/licenses/.
        

        - **Version** *(dict) --* Version information about the application.
          

          - **ApplicationId** *(string) --* The application Amazon Resource Name (ARN).
          

          - **CreationTime** *(string) --* The date/time this resource was created.
          

          - **ParameterDefinitions** *(list) --* Array of parameter types supported by the application.
            

            - *(dict) --* Parameters supported by the application.
              

              - **AllowedPattern** *(string) --* A regular expression that represents the patterns to allow for String types.
              

              - **AllowedValues** *(list) --* Array containing the list of values allowed for the parameter.
                

                - *(string) --* 
            
              

              - **ConstraintDescription** *(string) --* A string that explains a constraint when the constraint is violated. For example, without a constraint description,\n a parameter that has an allowed pattern of [A-Za-z0-9]+ displays the following error message when the user\n specifies an invalid value:\n\n Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+ \n \nBy adding a constraint description, such as "must contain only uppercase and lowercase letters, and numbers," you can display\n the following customized error message:\n\n Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters and numbers.
              

              - **DefaultValue** *(string) --* A value of the appropriate type for the template to use if no value is specified when a stack is created.\n If you define constraints for the parameter, you must specify a value that adheres to those constraints.
              

              - **Description** *(string) --* A string of up to 4,000 characters that describes the parameter.
              

              - **MaxLength** *(integer) --* An integer value that determines the largest number of characters you want to allow for String types.
              

              - **MaxValue** *(integer) --* A numeric value that determines the largest numeric value you want to allow for Number types.
              

              - **MinLength** *(integer) --* An integer value that determines the smallest number of characters you want to allow for String types.
              

              - **MinValue** *(integer) --* A numeric value that determines the smallest numeric value you want to allow for Number types.
              

              - **Name** *(string) --* The name of the parameter.
              

              - **NoEcho** *(boolean) --* Whether to mask the parameter value whenever anyone makes a call that describes the stack. If you set the\n value to true, the parameter value is masked with asterisks (*****).
              

              - **ReferencedByResources** *(list) --* A list of SAM resources that use this parameter.
                

                - *(string) --* 
            
              

              - **Type** *(string) --* The type of the parameter.\nValid values: String | Number | List| CommaDelimitedList \n \n\n String : A literal string.\nFor example, users could specify "MyUserName" .\n\n Number : An integer or float. AWS CloudFormation validates the parameter value as a number; however, when you use the\n parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a string.\nFor example, users could specify "8888" .\n\n List: An array of integers or floats that are separated by commas. AWS CloudFormation validates the parameter value as numbers; however, when\n you use the parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a list of strings.\nFor example, users could specify "80,20", and a Ref results in ["80","20"] .\n\n CommaDelimitedList : An array of literal strings that are separated by commas. The total number of strings should be one more than the total number of commas.\n Also, each member string is space-trimmed.\nFor example, users could specify "test,dev,prod", and a Ref results in ["test","dev","prod"] .
          
        
          

          - **SemanticVersion** *(string) --* The semantic version of the application:\n\n https://semver.org/
          

          - **SourceCodeUrl** *(string) --* A link to a public repository for the source code of your application.
          

          - **TemplateUrl** *(string) --* A link to the packaged SAM template of your application.
      
    

  .. py:method:: create_application_version(**kwargs)

    Creates an application version.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/CreateApplicationVersion>`_    


    **Request Syntax** 
    ::

      response = client.create_application_version(
          ApplicationId='string',
          SemanticVersion='string',
          SourceCodeUrl='string',
          TemplateBody='string',
          TemplateUrl='string'
      )
    :type ApplicationId: string
    :param ApplicationId: **[REQUIRED]** The id of the application to create a new version for

    
    :type SemanticVersion: string
    :param SemanticVersion: **[REQUIRED]** The semantic version of the new version

    
    :type SourceCodeUrl: string
    :param SourceCodeUrl: A link to a public repository for the source code of your application.

    
    :type TemplateBody: string
    :param TemplateBody: The raw packaged SAM template of your application.

    
    :type TemplateUrl: string
    :param TemplateUrl: A link to the packaged SAM template of your application.

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ApplicationId': 'string',
            'CreationTime': 'string',
            'ParameterDefinitions': [
                {
                    'AllowedPattern': 'string',
                    'AllowedValues': [
                        'string',
                    ],
                    'ConstraintDescription': 'string',
                    'DefaultValue': 'string',
                    'Description': 'string',
                    'MaxLength': 123,
                    'MaxValue': 123,
                    'MinLength': 123,
                    'MinValue': 123,
                    'Name': 'string',
                    'NoEcho': True|False,
                    'ReferencedByResources': [
                        'string',
                    ],
                    'Type': 'string'
                },
            ],
            'SemanticVersion': 'string',
            'SourceCodeUrl': 'string',
            'TemplateUrl': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 201 response
        

        - **ApplicationId** *(string) --* The application Amazon Resource Name (ARN).
        

        - **CreationTime** *(string) --* The date/time this resource was created.
        

        - **ParameterDefinitions** *(list) --* Array of parameter types supported by the application.
          

          - *(dict) --* Parameters supported by the application.
            

            - **AllowedPattern** *(string) --* A regular expression that represents the patterns to allow for String types.
            

            - **AllowedValues** *(list) --* Array containing the list of values allowed for the parameter.
              

              - *(string) --* 
          
            

            - **ConstraintDescription** *(string) --* A string that explains a constraint when the constraint is violated. For example, without a constraint description,\n a parameter that has an allowed pattern of [A-Za-z0-9]+ displays the following error message when the user\n specifies an invalid value:\n\n Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+ \n \nBy adding a constraint description, such as "must contain only uppercase and lowercase letters, and numbers," you can display\n the following customized error message:\n\n Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters and numbers.
            

            - **DefaultValue** *(string) --* A value of the appropriate type for the template to use if no value is specified when a stack is created.\n If you define constraints for the parameter, you must specify a value that adheres to those constraints.
            

            - **Description** *(string) --* A string of up to 4,000 characters that describes the parameter.
            

            - **MaxLength** *(integer) --* An integer value that determines the largest number of characters you want to allow for String types.
            

            - **MaxValue** *(integer) --* A numeric value that determines the largest numeric value you want to allow for Number types.
            

            - **MinLength** *(integer) --* An integer value that determines the smallest number of characters you want to allow for String types.
            

            - **MinValue** *(integer) --* A numeric value that determines the smallest numeric value you want to allow for Number types.
            

            - **Name** *(string) --* The name of the parameter.
            

            - **NoEcho** *(boolean) --* Whether to mask the parameter value whenever anyone makes a call that describes the stack. If you set the\n value to true, the parameter value is masked with asterisks (*****).
            

            - **ReferencedByResources** *(list) --* A list of SAM resources that use this parameter.
              

              - *(string) --* 
          
            

            - **Type** *(string) --* The type of the parameter.\nValid values: String | Number | List| CommaDelimitedList \n \n\n String : A literal string.\nFor example, users could specify "MyUserName" .\n\n Number : An integer or float. AWS CloudFormation validates the parameter value as a number; however, when you use the\n parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a string.\nFor example, users could specify "8888" .\n\n List: An array of integers or floats that are separated by commas. AWS CloudFormation validates the parameter value as numbers; however, when\n you use the parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a list of strings.\nFor example, users could specify "80,20", and a Ref results in ["80","20"] .\n\n CommaDelimitedList : An array of literal strings that are separated by commas. The total number of strings should be one more than the total number of commas.\n Also, each member string is space-trimmed.\nFor example, users could specify "test,dev,prod", and a Ref results in ["test","dev","prod"] .
        
      
        

        - **SemanticVersion** *(string) --* The semantic version of the application:\n\n https://semver.org/
        

        - **SourceCodeUrl** *(string) --* A link to a public repository for the source code of your application.
        

        - **TemplateUrl** *(string) --* A link to the packaged SAM template of your application.
    

  .. py:method:: create_cloud_formation_change_set(**kwargs)

    Creates an AWS CloudFormation ChangeSet for the given application.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/CreateCloudFormationChangeSet>`_    


    **Request Syntax** 
    ::

      response = client.create_cloud_formation_change_set(
          ApplicationId='string',
          ParameterOverrides=[
              {
                  'Name': 'string',
                  'Value': 'string'
              },
          ],
          SemanticVersion='string',
          StackName='string'
      )
    :type ApplicationId: string
    :param ApplicationId: **[REQUIRED]** The id of the application to create the ChangeSet for

    
    :type ParameterOverrides: list
    :param ParameterOverrides: A list of parameter values for the parameters of the application.

    
      - *(dict) --* Parameter value of the application.

      
        - **Name** *(string) --* The key associated with the parameter. If you don't specify a key and value for a particular parameter, AWS CloudFormation\n uses the default value that is specified in your template.

        
        - **Value** *(string) --* The input value associated with the parameter.

        
      
  
    :type SemanticVersion: string
    :param SemanticVersion: The semantic version of the application:\n\n https://semver.org/

    
    :type StackName: string
    :param StackName: The name or the unique ID of the stack for which you are creating a change set. AWS CloudFormation generates\n the change set by comparing this stack's information with the information that you submit, such as a modified\n template or different parameter input values. \nConstraints: Minimum length of 1.\nPattern: ([a-zA-Z][-a-zA-Z0-9]*)|(arn:\b(aws|aws-us-gov|aws-cn)\b:[-a-zA-Z0-9:/._+]*)

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ApplicationId': 'string',
            'ChangeSetId': 'string',
            'SemanticVersion': 'string',
            'StackId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 201 response
        

        - **ApplicationId** *(string) --* The application Amazon Resource Name (ARN).
        

        - **ChangeSetId** *(string) --* The ARN of the change set.\nLength Constraints: Minimum length of 1.\nPattern: arn:[-a-zA-Z0-9:/]*
        

        - **SemanticVersion** *(string) --* The semantic version of the application:\n\n https://semver.org/
        

        - **StackId** *(string) --* The unique ID of the stack.
    

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


  .. py:method:: get_application(**kwargs)

    Gets the specified application.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/GetApplication>`_    


    **Request Syntax** 
    ::

      response = client.get_application(
          ApplicationId='string',
          SemanticVersion='string'
      )
    :type ApplicationId: string
    :param ApplicationId: **[REQUIRED]** The id of the application to get

    
    :type SemanticVersion: string
    :param SemanticVersion: The semantic version of the application to get

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ApplicationId': 'string',
            'Author': 'string',
            'CreationTime': 'string',
            'Description': 'string',
            'Labels': [
                'string',
            ],
            'LicenseUrl': 'string',
            'Name': 'string',
            'ReadmeUrl': 'string',
            'SpdxLicenseId': 'string',
            'Version': {
                'ApplicationId': 'string',
                'CreationTime': 'string',
                'ParameterDefinitions': [
                    {
                        'AllowedPattern': 'string',
                        'AllowedValues': [
                            'string',
                        ],
                        'ConstraintDescription': 'string',
                        'DefaultValue': 'string',
                        'Description': 'string',
                        'MaxLength': 123,
                        'MaxValue': 123,
                        'MinLength': 123,
                        'MinValue': 123,
                        'Name': 'string',
                        'NoEcho': True|False,
                        'ReferencedByResources': [
                            'string',
                        ],
                        'Type': 'string'
                    },
                ],
                'SemanticVersion': 'string',
                'SourceCodeUrl': 'string',
                'TemplateUrl': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* Success
        

        - **ApplicationId** *(string) --* The application Amazon Resource Name (ARN).
        

        - **Author** *(string) --* The name of the author publishing the app.\nMin Length=1. Max Length=127.\nPattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";
        

        - **CreationTime** *(string) --* The date/time this resource was created.
        

        - **Description** *(string) --* The description of the application.\nMin Length=1. Max Length=256
        

        - **Labels** *(list) --* Labels to improve discovery of apps in search results.\nMin Length=1. Max Length=127. Maximum number of labels: 10\nPattern: "^[a-zA-Z0-9+\\-_:\\/@]+$";
          

          - *(string) --* 
      
        

        - **LicenseUrl** *(string) --* A link to a license file of the app that matches the spdxLicenseID of your application.\nMax size 5 MB
        

        - **Name** *(string) --* The name of the application.\nMin Length=1. Max Length=140\nPattern: "[a-zA-Z0-9\\-]+";
        

        - **ReadmeUrl** *(string) --* A link to the Readme file that contains a more detailed description of the application and how it works in markdown language.\nMax size 5 MB
        

        - **SpdxLicenseId** *(string) --* A valid identifier from https://spdx.org/licenses/.
        

        - **Version** *(dict) --* Version information about the application.
          

          - **ApplicationId** *(string) --* The application Amazon Resource Name (ARN).
          

          - **CreationTime** *(string) --* The date/time this resource was created.
          

          - **ParameterDefinitions** *(list) --* Array of parameter types supported by the application.
            

            - *(dict) --* Parameters supported by the application.
              

              - **AllowedPattern** *(string) --* A regular expression that represents the patterns to allow for String types.
              

              - **AllowedValues** *(list) --* Array containing the list of values allowed for the parameter.
                

                - *(string) --* 
            
              

              - **ConstraintDescription** *(string) --* A string that explains a constraint when the constraint is violated. For example, without a constraint description,\n a parameter that has an allowed pattern of [A-Za-z0-9]+ displays the following error message when the user\n specifies an invalid value:\n\n Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+ \n \nBy adding a constraint description, such as "must contain only uppercase and lowercase letters, and numbers," you can display\n the following customized error message:\n\n Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters and numbers.
              

              - **DefaultValue** *(string) --* A value of the appropriate type for the template to use if no value is specified when a stack is created.\n If you define constraints for the parameter, you must specify a value that adheres to those constraints.
              

              - **Description** *(string) --* A string of up to 4,000 characters that describes the parameter.
              

              - **MaxLength** *(integer) --* An integer value that determines the largest number of characters you want to allow for String types.
              

              - **MaxValue** *(integer) --* A numeric value that determines the largest numeric value you want to allow for Number types.
              

              - **MinLength** *(integer) --* An integer value that determines the smallest number of characters you want to allow for String types.
              

              - **MinValue** *(integer) --* A numeric value that determines the smallest numeric value you want to allow for Number types.
              

              - **Name** *(string) --* The name of the parameter.
              

              - **NoEcho** *(boolean) --* Whether to mask the parameter value whenever anyone makes a call that describes the stack. If you set the\n value to true, the parameter value is masked with asterisks (*****).
              

              - **ReferencedByResources** *(list) --* A list of SAM resources that use this parameter.
                

                - *(string) --* 
            
              

              - **Type** *(string) --* The type of the parameter.\nValid values: String | Number | List| CommaDelimitedList \n \n\n String : A literal string.\nFor example, users could specify "MyUserName" .\n\n Number : An integer or float. AWS CloudFormation validates the parameter value as a number; however, when you use the\n parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a string.\nFor example, users could specify "8888" .\n\n List: An array of integers or floats that are separated by commas. AWS CloudFormation validates the parameter value as numbers; however, when\n you use the parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a list of strings.\nFor example, users could specify "80,20", and a Ref results in ["80","20"] .\n\n CommaDelimitedList : An array of literal strings that are separated by commas. The total number of strings should be one more than the total number of commas.\n Also, each member string is space-trimmed.\nFor example, users could specify "test,dev,prod", and a Ref results in ["test","dev","prod"] .
          
        
          

          - **SemanticVersion** *(string) --* The semantic version of the application:\n\n https://semver.org/
          

          - **SourceCodeUrl** *(string) --* A link to a public repository for the source code of your application.
          

          - **TemplateUrl** *(string) --* A link to the packaged SAM template of your application.
      
    

  .. py:method:: get_application_policy(**kwargs)

    Gets the policy for the specified application.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/GetApplicationPolicy>`_    


    **Request Syntax** 
    ::

      response = client.get_application_policy(
          ApplicationId='string'
      )
    :type ApplicationId: string
    :param ApplicationId: **[REQUIRED]** The id of the application to get policy for

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Statements': [
                {
                    'Actions': [
                        'string',
                    ],
                    'Principals': [
                        'string',
                    ],
                    'StatementId': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* Success
        

        - **Statements** *(list) --* Array of policy statements applied to the application.
          

          - *(dict) --* Policy statement applied to the application.
            

            - **Actions** *(list) --* A list of supported actions:\n\n GetApplication \n \n\n CreateCloudFormationChangeSet \n \n\n ListApplicationVersions \n \n\n SearchApplications \n \n\n Deploy (Note: This action enables all other actions above.)
              

              - *(string) --* 
          
            

            - **Principals** *(list) --* An AWS account ID, or * to make the application public.
              

              - *(string) --* 
          
            

            - **StatementId** *(string) --* A unique ID for the statement.
        
      
    

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

        


  .. py:method:: list_application_versions(**kwargs)

    Lists versions for the specified application.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/ListApplicationVersions>`_    


    **Request Syntax** 
    ::

      response = client.list_application_versions(
          ApplicationId='string',
          MaxItems=123,
          NextToken='string'
      )
    :type ApplicationId: string
    :param ApplicationId: **[REQUIRED]** The id of the application to list

    
    :type MaxItems: integer
    :param MaxItems: The total number of items to return

    
    :type NextToken: string
    :param NextToken: A token to specify where to start paginating

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextToken': 'string',
            'Versions': [
                {
                    'ApplicationId': 'string',
                    'CreationTime': 'string',
                    'SemanticVersion': 'string',
                    'SourceCodeUrl': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* Success
        

        - **NextToken** *(string) --* The token to request the next page of results.
        

        - **Versions** *(list) --* Array of version summaries for the application.
          

          - *(dict) --* Application version summary.
            

            - **ApplicationId** *(string) --* The application Amazon Resource Name (ARN).
            

            - **CreationTime** *(string) --* The date/time this resource was created.
            

            - **SemanticVersion** *(string) --* The semantic version of the application:\n\n https://semver.org/
            

            - **SourceCodeUrl** *(string) --* A link to a public repository for the source code of your application.
        
      
    

  .. py:method:: list_applications(**kwargs)

    Lists applications owned by the requester.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/ListApplications>`_    


    **Request Syntax** 
    ::

      response = client.list_applications(
          MaxItems=123,
          NextToken='string'
      )
    :type MaxItems: integer
    :param MaxItems: The total number of items to return

    
    :type NextToken: string
    :param NextToken: A token to specify where to start paginating

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Applications': [
                {
                    'ApplicationId': 'string',
                    'Author': 'string',
                    'CreationTime': 'string',
                    'Description': 'string',
                    'Labels': [
                        'string',
                    ],
                    'Name': 'string',
                    'SpdxLicenseId': 'string'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* Success
        

        - **Applications** *(list) --* Array of application summaries.
          

          - *(dict) --* Summary of details about the application.
            

            - **ApplicationId** *(string) --* The application ARN.
            

            - **Author** *(string) --* The name of the author publishing the app\nMin Length=1. Max Length=127.\nPattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";
            

            - **CreationTime** *(string) --* The date/time this resource was created.
            

            - **Description** *(string) --* The description of the application.\nMin Length=1. Max Length=256
            

            - **Labels** *(list) --* Labels to improve discovery of apps in search results.\nMin Length=1. Max Length=127. Maximum number of labels: 10\nPattern: "^[a-zA-Z0-9+\\-_:\\/@]+$";
              

              - *(string) --* 
          
            

            - **Name** *(string) --* The name of the application.\nMin Length=1. Max Length=140\nPattern: "[a-zA-Z0-9\\-]+";
            

            - **SpdxLicenseId** *(string) --* A valid identifier from https://spdx.org/licenses/ .
        
      
        

        - **NextToken** *(string) --* The token to request the next page of results.
    

  .. py:method:: put_application_policy(**kwargs)

    Puts the policy for the specified application.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/PutApplicationPolicy>`_    


    **Request Syntax** 
    ::

      response = client.put_application_policy(
          ApplicationId='string',
          Statements=[
              {
                  'Actions': [
                      'string',
                  ],
                  'Principals': [
                      'string',
                  ],
                  'StatementId': 'string'
              },
          ]
      )
    :type ApplicationId: string
    :param ApplicationId: **[REQUIRED]** The id of the application to put policy for

    
    :type Statements: list
    :param Statements: Array of policy statements applied to the application.

    
      - *(dict) --* Policy statement applied to the application.

      
        - **Actions** *(list) --* A list of supported actions:\n\n GetApplication \n \n\n CreateCloudFormationChangeSet \n \n\n ListApplicationVersions \n \n\n SearchApplications \n \n\n Deploy (Note: This action enables all other actions above.)

        
          - *(string) --* 

          
      
        - **Principals** *(list) --* An AWS account ID, or * to make the application public.

        
          - *(string) --* 

          
      
        - **StatementId** *(string) --* A unique ID for the statement.

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Statements': [
                {
                    'Actions': [
                        'string',
                    ],
                    'Principals': [
                        'string',
                    ],
                    'StatementId': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* Success
        

        - **Statements** *(list) --* Array of policy statements applied to the application.
          

          - *(dict) --* Policy statement applied to the application.
            

            - **Actions** *(list) --* A list of supported actions:\n\n GetApplication \n \n\n CreateCloudFormationChangeSet \n \n\n ListApplicationVersions \n \n\n SearchApplications \n \n\n Deploy (Note: This action enables all other actions above.)
              

              - *(string) --* 
          
            

            - **Principals** *(list) --* An AWS account ID, or * to make the application public.
              

              - *(string) --* 
          
            

            - **StatementId** *(string) --* A unique ID for the statement.
        
      
    

  .. py:method:: update_application(**kwargs)

    Updates the specified application.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/UpdateApplication>`_    


    **Request Syntax** 
    ::

      response = client.update_application(
          ApplicationId='string',
          Author='string',
          Description='string',
          Labels=[
              'string',
          ],
          ReadmeBody='string',
          ReadmeUrl='string'
      )
    :type ApplicationId: string
    :param ApplicationId: **[REQUIRED]** The id of the application to update

    
    :type Author: string
    :param Author: The name of the author publishing the app.\nMin Length=1. Max Length=127.\nPattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";

    
    :type Description: string
    :param Description: The description of the application.\nMin Length=1. Max Length=256

    
    :type Labels: list
    :param Labels: Labels to improve discovery of apps in search results.\nMin Length=1. Max Length=127. Maximum number of labels: 10\nPattern: "^[a-zA-Z0-9+\\-_:\\/@]+$";

    
      - *(string) --* 

      
  
    :type ReadmeBody: string
    :param ReadmeBody: A raw text Readme file that contains a more detailed description of the application and how it works in markdown language.\nMax size 5 MB

    
    :type ReadmeUrl: string
    :param ReadmeUrl: A link to the Readme file that contains a more detailed description of the application and how it works in markdown language.\nMax size 5 MB

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ApplicationId': 'string',
            'Author': 'string',
            'CreationTime': 'string',
            'Description': 'string',
            'Labels': [
                'string',
            ],
            'LicenseUrl': 'string',
            'Name': 'string',
            'ReadmeUrl': 'string',
            'SpdxLicenseId': 'string',
            'Version': {
                'ApplicationId': 'string',
                'CreationTime': 'string',
                'ParameterDefinitions': [
                    {
                        'AllowedPattern': 'string',
                        'AllowedValues': [
                            'string',
                        ],
                        'ConstraintDescription': 'string',
                        'DefaultValue': 'string',
                        'Description': 'string',
                        'MaxLength': 123,
                        'MaxValue': 123,
                        'MinLength': 123,
                        'MinValue': 123,
                        'Name': 'string',
                        'NoEcho': True|False,
                        'ReferencedByResources': [
                            'string',
                        ],
                        'Type': 'string'
                    },
                ],
                'SemanticVersion': 'string',
                'SourceCodeUrl': 'string',
                'TemplateUrl': 'string'
            }
        }
      **Response Structure** 

      

      - *(dict) --* Success
        

        - **ApplicationId** *(string) --* The application Amazon Resource Name (ARN).
        

        - **Author** *(string) --* The name of the author publishing the app.\nMin Length=1. Max Length=127.\nPattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";
        

        - **CreationTime** *(string) --* The date/time this resource was created.
        

        - **Description** *(string) --* The description of the application.\nMin Length=1. Max Length=256
        

        - **Labels** *(list) --* Labels to improve discovery of apps in search results.\nMin Length=1. Max Length=127. Maximum number of labels: 10\nPattern: "^[a-zA-Z0-9+\\-_:\\/@]+$";
          

          - *(string) --* 
      
        

        - **LicenseUrl** *(string) --* A link to a license file of the app that matches the spdxLicenseID of your application.\nMax size 5 MB
        

        - **Name** *(string) --* The name of the application.\nMin Length=1. Max Length=140\nPattern: "[a-zA-Z0-9\\-]+";
        

        - **ReadmeUrl** *(string) --* A link to the Readme file that contains a more detailed description of the application and how it works in markdown language.\nMax size 5 MB
        

        - **SpdxLicenseId** *(string) --* A valid identifier from https://spdx.org/licenses/.
        

        - **Version** *(dict) --* Version information about the application.
          

          - **ApplicationId** *(string) --* The application Amazon Resource Name (ARN).
          

          - **CreationTime** *(string) --* The date/time this resource was created.
          

          - **ParameterDefinitions** *(list) --* Array of parameter types supported by the application.
            

            - *(dict) --* Parameters supported by the application.
              

              - **AllowedPattern** *(string) --* A regular expression that represents the patterns to allow for String types.
              

              - **AllowedValues** *(list) --* Array containing the list of values allowed for the parameter.
                

                - *(string) --* 
            
              

              - **ConstraintDescription** *(string) --* A string that explains a constraint when the constraint is violated. For example, without a constraint description,\n a parameter that has an allowed pattern of [A-Za-z0-9]+ displays the following error message when the user\n specifies an invalid value:\n\n Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+ \n \nBy adding a constraint description, such as "must contain only uppercase and lowercase letters, and numbers," you can display\n the following customized error message:\n\n Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters and numbers.
              

              - **DefaultValue** *(string) --* A value of the appropriate type for the template to use if no value is specified when a stack is created.\n If you define constraints for the parameter, you must specify a value that adheres to those constraints.
              

              - **Description** *(string) --* A string of up to 4,000 characters that describes the parameter.
              

              - **MaxLength** *(integer) --* An integer value that determines the largest number of characters you want to allow for String types.
              

              - **MaxValue** *(integer) --* A numeric value that determines the largest numeric value you want to allow for Number types.
              

              - **MinLength** *(integer) --* An integer value that determines the smallest number of characters you want to allow for String types.
              

              - **MinValue** *(integer) --* A numeric value that determines the smallest numeric value you want to allow for Number types.
              

              - **Name** *(string) --* The name of the parameter.
              

              - **NoEcho** *(boolean) --* Whether to mask the parameter value whenever anyone makes a call that describes the stack. If you set the\n value to true, the parameter value is masked with asterisks (*****).
              

              - **ReferencedByResources** *(list) --* A list of SAM resources that use this parameter.
                

                - *(string) --* 
            
              

              - **Type** *(string) --* The type of the parameter.\nValid values: String | Number | List| CommaDelimitedList \n \n\n String : A literal string.\nFor example, users could specify "MyUserName" .\n\n Number : An integer or float. AWS CloudFormation validates the parameter value as a number; however, when you use the\n parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a string.\nFor example, users could specify "8888" .\n\n List: An array of integers or floats that are separated by commas. AWS CloudFormation validates the parameter value as numbers; however, when\n you use the parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a list of strings.\nFor example, users could specify "80,20", and a Ref results in ["80","20"] .\n\n CommaDelimitedList : An array of literal strings that are separated by commas. The total number of strings should be one more than the total number of commas.\n Also, each member string is space-trimmed.\nFor example, users could specify "test,dev,prod", and a Ref results in ["test","dev","prod"] .
          
        
          

          - **SemanticVersion** *(string) --* The semantic version of the application:\n\n https://semver.org/
          

          - **SourceCodeUrl** *(string) --* A link to a public repository for the source code of your application.
          

          - **TemplateUrl** *(string) --* A link to the packaged SAM template of your application.
      
    