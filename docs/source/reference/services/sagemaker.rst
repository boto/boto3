

*********
SageMaker
*********

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: SageMaker.Client

  A low-level client representing Amazon SageMaker Service::

    
    import boto3
    
    client = boto3.client('sagemaker')

  
  These are the available methods:
  
  *   :py:meth:`~SageMaker.Client.add_tags`

  
  *   :py:meth:`~SageMaker.Client.can_paginate`

  
  *   :py:meth:`~SageMaker.Client.create_endpoint`

  
  *   :py:meth:`~SageMaker.Client.create_endpoint_config`

  
  *   :py:meth:`~SageMaker.Client.create_model`

  
  *   :py:meth:`~SageMaker.Client.create_notebook_instance`

  
  *   :py:meth:`~SageMaker.Client.create_presigned_notebook_instance_url`

  
  *   :py:meth:`~SageMaker.Client.create_training_job`

  
  *   :py:meth:`~SageMaker.Client.delete_endpoint`

  
  *   :py:meth:`~SageMaker.Client.delete_endpoint_config`

  
  *   :py:meth:`~SageMaker.Client.delete_model`

  
  *   :py:meth:`~SageMaker.Client.delete_notebook_instance`

  
  *   :py:meth:`~SageMaker.Client.delete_tags`

  
  *   :py:meth:`~SageMaker.Client.describe_endpoint`

  
  *   :py:meth:`~SageMaker.Client.describe_endpoint_config`

  
  *   :py:meth:`~SageMaker.Client.describe_model`

  
  *   :py:meth:`~SageMaker.Client.describe_notebook_instance`

  
  *   :py:meth:`~SageMaker.Client.describe_training_job`

  
  *   :py:meth:`~SageMaker.Client.generate_presigned_url`

  
  *   :py:meth:`~SageMaker.Client.get_paginator`

  
  *   :py:meth:`~SageMaker.Client.get_waiter`

  
  *   :py:meth:`~SageMaker.Client.list_endpoint_configs`

  
  *   :py:meth:`~SageMaker.Client.list_endpoints`

  
  *   :py:meth:`~SageMaker.Client.list_models`

  
  *   :py:meth:`~SageMaker.Client.list_notebook_instances`

  
  *   :py:meth:`~SageMaker.Client.list_tags`

  
  *   :py:meth:`~SageMaker.Client.list_training_jobs`

  
  *   :py:meth:`~SageMaker.Client.start_notebook_instance`

  
  *   :py:meth:`~SageMaker.Client.stop_notebook_instance`

  
  *   :py:meth:`~SageMaker.Client.stop_training_job`

  
  *   :py:meth:`~SageMaker.Client.update_endpoint`

  
  *   :py:meth:`~SageMaker.Client.update_endpoint_weights_and_capacities`

  
  *   :py:meth:`~SageMaker.Client.update_notebook_instance`

  

  .. py:method:: add_tags(**kwargs)

    

    Adds or overwrites one or more tags for the specified Amazon SageMaker resource. You can add tags to notebook instances, training jobs, models, endpoint configurations, and endpoints. 

     

    Each tag consists of a key and an optional value. Tag keys must be unique per resource. For more information about tags, see `Using Cost Allocation Tags <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what>`__ in the *AWS Billing and Cost Management User Guide* . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/AddTags>`_    


    **Request Syntax** 
    ::

      response = client.add_tags(
          ResourceArn='string',
          Tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type ResourceArn: string
    :param ResourceArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the resource that you want to tag. 

      

    
    :type Tags: list
    :param Tags: **[REQUIRED]** 

      An array of ``Tag`` objects. Each tag is a key-value pair. Only the ``key`` parameter is required. If you don't specify a value, Amazon SageMaker sets the value to an empty string. 

      

    
      - *(dict) --* 

        Describes a tag. 

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The tag key.

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          The tag value.

          

        
      
  
    
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

          A list of tags associated with the Amazon SageMaker resource.

          
          

          - *(dict) --* 

            Describes a tag. 

            
            

            - **Key** *(string) --* 

              The tag key.

              
            

            - **Value** *(string) --* 

              The tag value.

              
        
      
    

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


  .. py:method:: create_endpoint(**kwargs)

    

    Creates an endpoint using the endpoint configuration specified in the request. Amazon SageMaker uses the endpoint to provision resources and deploy models. You create the endpoint configuration with the `CreateEndpointConfig <http://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpointConfig.html>`__ API. 

     

    .. note::

       

      Use this API only for hosting models using Amazon SageMaker hosting services. 

       

     

    The endpoint name must be unique within an AWS Region in your AWS account. 

     

    When it receives the request, Amazon SageMaker creates the endpoint, launches the resources (ML compute instances), and deploys the model(s) on them. 

     

    When Amazon SageMaker receives the request, it sets the endpoint status to ``Creating`` . After it creates the endpoint, it sets the status to ``InService`` . Amazon SageMaker can then process incoming requests for inferences. To check the status of an endpoint, use the `DescribeEndpoint <http://docs.aws.amazon.com/sagemaker/latest/dg/API_DescribeEndpoint.html>`__ API.

     

    For an example, see `Exercise 1\: Using the K-Means Algorithm Provided by Amazon SageMaker <http://docs.aws.amazon.com/sagemaker/latest/dg/ex1.html>`__ . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateEndpoint>`_    


    **Request Syntax** 
    ::

      response = client.create_endpoint(
          EndpointName='string',
          EndpointConfigName='string',
          Tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type EndpointName: string
    :param EndpointName: **[REQUIRED]** 

      The name of the endpoint. The name must be unique within an AWS Region in your AWS account.

      

    
    :type EndpointConfigName: string
    :param EndpointConfigName: **[REQUIRED]** 

      The name of an endpoint configuration. For more information, see `CreateEndpointConfig <http://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpointConfig.html>`__ . 

      

    
    :type Tags: list
    :param Tags: 

      An array of key-value pairs. For more information, see `Using Cost Allocation Tags <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what>`__ in the *AWS Billing and Cost Management User Guide* . 

      

    
      - *(dict) --* 

        Describes a tag. 

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The tag key.

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          The tag value.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'EndpointArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **EndpointArn** *(string) --* 

          The Amazon Resource Name (ARN) of the endpoint.

          
    

  .. py:method:: create_endpoint_config(**kwargs)

    

    Creates an endpoint configuration that Amazon SageMaker hosting services uses to deploy models. In the configuration, you identify one or more models, created using the ``CreateModel`` API, to deploy and the resources that you want Amazon SageMaker to provision. Then you call the `CreateEndpoint <http://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpoint.html>`__ API. 

     

    .. note::

       

      Use this API only if you want to use Amazon SageMaker hosting services to deploy models into production. 

       

     

    In the request, you define one or more ``ProductionVariant`` s, each of which identifies a model. Each ``ProductionVariant`` parameter also describes the resources that you want Amazon SageMaker to provision. This includes the number and type of ML compute instances to deploy. 

     

    If you are hosting multiple models, you also assign a ``VariantWeight`` to specify how much traffic you want to allocate to each model. For example, suppose that you want to host two models, A and B, and you assign traffic weight 2 for model A and 1 for model B. Amazon SageMaker distributes two-thirds of the traffic to Model A, and one-third to model B. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateEndpointConfig>`_    


    **Request Syntax** 
    ::

      response = client.create_endpoint_config(
          EndpointConfigName='string',
          ProductionVariants=[
              {
                  'VariantName': 'string',
                  'ModelName': 'string',
                  'InitialInstanceCount': 123,
                  'InstanceType': 'ml.c4.2xlarge'|'ml.c4.8xlarge'|'ml.c4.xlarge'|'ml.c5.2xlarge'|'ml.c5.9xlarge'|'ml.c5.xlarge'|'ml.m4.xlarge'|'ml.p2.xlarge'|'ml.p3.2xlarge'|'ml.t2.medium',
                  'InitialVariantWeight': ...
              },
          ],
          Tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type EndpointConfigName: string
    :param EndpointConfigName: **[REQUIRED]** 

      The name of the endpoint configuration. You specify this name in a `CreateEndpoint <http://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpoint.html>`__ request. 

      

    
    :type ProductionVariants: list
    :param ProductionVariants: **[REQUIRED]** 

      An array of ``ProductionVariant`` objects, one for each model that you want to host at this endpoint.

      

    
      - *(dict) --* 

        Identifies a model that you want to host and the resources to deploy for hosting it. If you are deploying multiple models, tell Amazon SageMaker how to distribute traffic among the models by specifying variant weights. 

        

      
        - **VariantName** *(string) --* **[REQUIRED]** 

          The name of the production variant.

          

        
        - **ModelName** *(string) --* **[REQUIRED]** 

          The name of the model that you want to host. This is the name that you specified when creating the model.

          

        
        - **InitialInstanceCount** *(integer) --* **[REQUIRED]** 

          Number of instances to launch initially.

          

        
        - **InstanceType** *(string) --* **[REQUIRED]** 

          The ML compute instance type.

          

        
        - **InitialVariantWeight** *(float) --* 

          Determines initial traffic distribution among all of the models that you specify in the endpoint configuration. The traffic to a production variant is determined by the ratio of the ``VariantWeight`` to the sum of all ``VariantWeight`` values across all ProductionVariants. If unspecified, it defaults to 1.0. 

          

        
      
  
    :type Tags: list
    :param Tags: 

      An array of key-value pairs. For more information, see `Using Cost Allocation Tags <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what>`__ in the *AWS Billing and Cost Management User Guide* . 

      

    
      - *(dict) --* 

        Describes a tag. 

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The tag key.

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          The tag value.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'EndpointConfigArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **EndpointConfigArn** *(string) --* 

          The Amazon Resource Name (ARN) of the endpoint configuration. 

          
    

  .. py:method:: create_model(**kwargs)

    

    Creates a model in Amazon SageMaker. In the request, you name the model and describe one or more containers. For each container, you specify the docker image containing inference code, artifacts (from prior training), and custom environment map that the inference code uses when you deploy the model into production. 

     

    Use this API to create a model only if you want to use Amazon SageMaker hosting services. To host your model, you create an endpoint configuration with the ``CreateEndpointConfig`` API, and then create an endpoint with the ``CreateEndpoint`` API. 

     

    Amazon SageMaker then deploys all of the containers that you defined for the model in the hosting environment. 

     

    In the ``CreateModel`` request, you must define at least one container with the ``PrimaryContainer`` parameter. You can optionally specify additional containers with the ``SupplementalContainers`` parameter. 

     

    In the request, you also provide an IAM role that Amazon SageMaker can assume to access model artifacts and docker image for deployment on ML compute hosting instances. In addition, you also use the IAM role to manage permissions the inference code needs. For example, if the inference code access any other AWS resources, you grant necessary permissions via this role.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateModel>`_    


    **Request Syntax** 
    ::

      response = client.create_model(
          ModelName='string',
          PrimaryContainer={
              'ContainerHostname': 'string',
              'Image': 'string',
              'ModelDataUrl': 'string',
              'Environment': {
                  'string': 'string'
              }
          },
          SupplementalContainers=[
              {
                  'ContainerHostname': 'string',
                  'Image': 'string',
                  'ModelDataUrl': 'string',
                  'Environment': {
                      'string': 'string'
                  }
              },
          ],
          ExecutionRoleArn='string',
          Tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type ModelName: string
    :param ModelName: **[REQUIRED]** 

      The name of the new model.

      

    
    :type PrimaryContainer: dict
    :param PrimaryContainer: **[REQUIRED]** 

      The location of the primary docker image containing inference code, associated artifacts, and custom environment map that the inference code uses when the model is deployed into production. 

      

    
      - **ContainerHostname** *(string) --* 

        The DNS host name for the container after Amazon SageMaker deploys it.

        

      
      - **Image** *(string) --* **[REQUIRED]** 

        The Amazon EC2 Container Registry (Amazon ECR) path where inference code is stored. If you are using your own custom algorithm instead of an algorithm provided by Amazon SageMaker, the inference code must meet Amazon SageMaker requirements. For more information, see `Using Your Own Algorithms with Amazon SageMaker <http://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html>`__  

        

      
      - **ModelDataUrl** *(string) --* 

        The S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix). 

        

      
      - **Environment** *(dict) --* 

        The environment variables to set in the Docker container. Each key and value in the ``Environment`` string to string map can have length of up to 1024. We support up to 16 entries in the map. 

        

      
        - *(string) --* 

        
          - *(string) --* 

          
    
  
    
    :type SupplementalContainers: list
    :param SupplementalContainers: 

      The additional optional containers to deploy.

      

    
      - *(dict) --* 

        Describes the container, as part of model definition.

        

      
        - **ContainerHostname** *(string) --* 

          The DNS host name for the container after Amazon SageMaker deploys it.

          

        
        - **Image** *(string) --* **[REQUIRED]** 

          The Amazon EC2 Container Registry (Amazon ECR) path where inference code is stored. If you are using your own custom algorithm instead of an algorithm provided by Amazon SageMaker, the inference code must meet Amazon SageMaker requirements. For more information, see `Using Your Own Algorithms with Amazon SageMaker <http://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html>`__  

          

        
        - **ModelDataUrl** *(string) --* 

          The S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix). 

          

        
        - **Environment** *(dict) --* 

          The environment variables to set in the Docker container. Each key and value in the ``Environment`` string to string map can have length of up to 1024. We support up to 16 entries in the map. 

          

        
          - *(string) --* 

          
            - *(string) --* 

            
      
    
      
  
    :type ExecutionRoleArn: string
    :param ExecutionRoleArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the IAM role that Amazon SageMaker can assume to access model artifacts and docker image for deployment on ML compute instances. Deploying on ML compute instances is part of model hosting. For more information, see `Amazon SageMaker Roles <http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html>`__ . 

      

    
    :type Tags: list
    :param Tags: 

      An array of key-value pairs. For more information, see `Using Cost Allocation Tags <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what>`__ in the *AWS Billing and Cost Management User Guide* . 

      

    
      - *(dict) --* 

        Describes a tag. 

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The tag key.

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          The tag value.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ModelArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ModelArn** *(string) --* 

          The ARN of the model created in Amazon SageMaker.

          
    

  .. py:method:: create_notebook_instance(**kwargs)

    

    Creates an Amazon SageMaker notebook instance. A notebook instance is an ML compute instance running on a Jupyter notebook. 

     

    In a ``CreateNotebookInstance`` request, you specify the type of ML compute instance that you want to run. Amazon SageMaker launches the instance, installs common libraries that you can use to explore datasets for model training, and attaches an ML storage volume to the notebook instance. 

     

    Amazon SageMaker also provides a set of example notebooks. Each notebook demonstrates how to use Amazon SageMaker with a specific an algorithm or with a machine learning framework. 

     

    After receiving the request, Amazon SageMaker does the following:

     

     
    * Creates a network interface in the Amazon SageMaker VPC. 
     
    * (Option) If you specified ``SubnetId`` , creates a network interface in your own VPC, which is inferred from the subnet ID that you provide in the input. When creating this network interface, Amazon SageMaker attaches the security group that you specified in the request to the network interface that it creates in your VPC. 
     
    * Launches an EC2 instance of the type specified in the request in the Amazon SageMaker VPC. If you specified ``SubnetId`` of your VPC, Amazon SageMaker specifies both network interfaces when launching this instance. This enables inbound traffic from your own VPC to the notebook instance, assuming that the security groups allow it. 
     

     

    After creating the notebook instance, Amazon SageMaker returns its Amazon Resource Name (ARN).

     

    After Amazon SageMaker creates the notebook instance, you can connect to the Jupyter server and work in Jupyter notebooks. For example, you can write code to explore a dataset that you can use for model training, train a model, host models by creating Amazon SageMaker endpoints, and validate hosted models. 

     

    For more information, see `How It Works <http://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works.html>`__ . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateNotebookInstance>`_    


    **Request Syntax** 
    ::

      response = client.create_notebook_instance(
          NotebookInstanceName='string',
          InstanceType='ml.t2.medium'|'ml.m4.xlarge'|'ml.p2.xlarge',
          SubnetId='string',
          SecurityGroupIds=[
              'string',
          ],
          RoleArn='string',
          KmsKeyId='string',
          Tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type NotebookInstanceName: string
    :param NotebookInstanceName: **[REQUIRED]** 

      The name of the new notebook instance.

      

    
    :type InstanceType: string
    :param InstanceType: **[REQUIRED]** 

      The type of ML compute instance to launch for the notebook instance.

      

    
    :type SubnetId: string
    :param SubnetId: 

      The ID of the subnet in a VPC to which you would like to have a connectivity from your ML compute instance. 

      

    
    :type SecurityGroupIds: list
    :param SecurityGroupIds: 

      The VPC security group IDs, in the form sg-xxxxxxxx. The security groups must be for the same VPC as specified in the subnet. 

      

    
      - *(string) --* 

      
  
    :type RoleArn: string
    :param RoleArn: **[REQUIRED]** 

      When you send any requests to AWS resources from the notebook instance, Amazon SageMaker assumes this role to perform tasks on your behalf. You must grant this role necessary permissions so Amazon SageMaker can perform these tasks. The policy must allow the Amazon SageMaker service principal (sagemaker.amazonaws.com) permissions to assume this role. For more information, see `Amazon SageMaker Roles <http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html>`__ . 

      

    
    :type KmsKeyId: string
    :param KmsKeyId: 

      If you provide a AWS KMS key ID, Amazon SageMaker uses it to encrypt data at rest on the ML storage volume that is attached to your notebook instance. 

      

    
    :type Tags: list
    :param Tags: 

      A list of tags to associate with the notebook instance. You can add tags later by using the ``CreateTags`` API.

      

    
      - *(dict) --* 

        Describes a tag. 

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The tag key.

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          The tag value.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NotebookInstanceArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NotebookInstanceArn** *(string) --* 

          The Amazon Resource Name (ARN) of the notebook instance. 

          
    

  .. py:method:: create_presigned_notebook_instance_url(**kwargs)

    

    Returns a URL that you can use to connect to the Juypter server from a notebook instance. In the Amazon SageMaker console, when you choose ``Open`` next to a notebook instance, Amazon SageMaker opens a new tab showing the Jupyter server home page from the notebook instance. The console uses this API to get the URL and show the page. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreatePresignedNotebookInstanceUrl>`_    


    **Request Syntax** 
    ::

      response = client.create_presigned_notebook_instance_url(
          NotebookInstanceName='string',
          SessionExpirationDurationInSeconds=123
      )
    :type NotebookInstanceName: string
    :param NotebookInstanceName: **[REQUIRED]** 

      The name of the notebook instance.

      

    
    :type SessionExpirationDurationInSeconds: integer
    :param SessionExpirationDurationInSeconds: 

      The duration of the session, in seconds. The default is 12 hours.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'AuthorizedUrl': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **AuthorizedUrl** *(string) --* 

          A JSON object that contains the URL string. 

          
    

  .. py:method:: create_training_job(**kwargs)

    

    Starts a model training job. After training completes, Amazon SageMaker saves the resulting model artifacts to an Amazon S3 location that you specify. 

     

    If you choose to host your model using Amazon SageMaker hosting services, you can use the resulting model artifacts as part of the model. You can also use the artifacts in a deep learning service other than Amazon SageMaker, provided that you know how to use them for inferences. 

     

    In the request body, you provide the following: 

     

     
    * ``AlgorithmSpecification`` - Identifies the training algorithm to use.  
     
    * ``HyperParameters`` - Specify these algorithm-specific parameters to influence the quality of the final model. For a list of hyperparameters for each training algorithm provided by Amazon SageMaker, see `Algorithms <http://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__ .  
     
    * ``InputDataConfig`` - Describes the training dataset and the Amazon S3 location where it is stored. 
     
    * ``OutputDataConfig`` - Identifies the Amazon S3 location where you want Amazon SageMaker to save the results of model training.   
     
    * ``ResourceConfig`` - Identifies the resources, ML compute instances, and ML storage volumes to deploy for model training. In distributed training, you specify more than one instance.  
     
    * ``RoleARN`` - The Amazon Resource Number (ARN) that Amazon SageMaker assumes to perform tasks on your behalf during model training. You must grant this role the necessary permissions so that Amazon SageMaker can successfully complete model training.  
     
    * ``StoppingCondition`` - Sets a duration for training. Use this parameter to cap model training costs.  
     

     

    For more information about Amazon SageMaker, see `How It Works <http://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works.html>`__ . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateTrainingJob>`_    


    **Request Syntax** 
    ::

      response = client.create_training_job(
          TrainingJobName='string',
          HyperParameters={
              'string': 'string'
          },
          AlgorithmSpecification={
              'TrainingImage': 'string',
              'TrainingInputMode': 'Pipe'|'File'
          },
          RoleArn='string',
          InputDataConfig=[
              {
                  'ChannelName': 'string',
                  'DataSource': {
                      'S3DataSource': {
                          'S3DataType': 'ManifestFile'|'S3Prefix',
                          'S3Uri': 'string',
                          'S3DataDistributionType': 'FullyReplicated'|'ShardedByS3Key'
                      }
                  },
                  'ContentType': 'string',
                  'CompressionType': 'None'|'Gzip',
                  'RecordWrapperType': 'None'|'RecordIO'
              },
          ],
          OutputDataConfig={
              'KmsKeyId': 'string',
              'S3OutputPath': 'string'
          },
          ResourceConfig={
              'InstanceType': 'ml.m4.xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
              'InstanceCount': 123,
              'VolumeSizeInGB': 123
          },
          StoppingCondition={
              'MaxRuntimeInSeconds': 123
          },
          Tags=[
              {
                  'Key': 'string',
                  'Value': 'string'
              },
          ]
      )
    :type TrainingJobName: string
    :param TrainingJobName: **[REQUIRED]** 

      The name of the training job. The name must be unique within an AWS Region in an AWS account. It appears in the Amazon SageMaker console. 

      

    
    :type HyperParameters: dict
    :param HyperParameters: 

      Algorithm-specific parameters. You set hyperparameters before you start the learning process. Hyperparameters influence the quality of the model. For a list of hyperparameters for each training algorithm provided by Amazon SageMaker, see `Algorithms <http://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__ . 

       

      You can specify a maximum of 100 hyperparameters. Each hyperparameter is a key-value pair. Each key and value is limited to 256 characters, as specified by the ``Length Constraint`` . 

      

    
      - *(string) --* 

      
        - *(string) --* 

        
  

    :type AlgorithmSpecification: dict
    :param AlgorithmSpecification: **[REQUIRED]** 

      The registry path of the Docker image that contains the training algorithm and algorithm-specific metadata, including the input mode. For more information about algorithms provided by Amazon SageMaker, see `Algorithms <http://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__ . For information about providing your own algorithms, see `Bring Your Own Algorithms <http://docs.aws.amazon.com/sagemaker/latest/dg/adv-topics-own-algo.html>`__ . 

      

    
      - **TrainingImage** *(string) --* **[REQUIRED]** 

        The registry path of the Docker image that contains the training algorithm. For information about using your own algorithms, see `Docker Registry Paths for Algorithms Provided by Amazon SageMaker <http://docs.aws.amazon.com/sagemaker/latest/dg/algos-docker-registry-paths.html>`__ . 

        

      
      - **TrainingInputMode** *(string) --* **[REQUIRED]** 

        The input mode that the algorithm supports. For the input modes that Amazon SageMaker algorithms support, see `Algorithms <http://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__ . If an algorithm supports the ``File`` input mode, Amazon SageMaker downloads the training data from S3 to the provisioned ML storage Volume, and mounts the directory to docker volume for training container. If an algorithm supports the ``Pipe`` input mode, Amazon SageMaker streams data directly from S3 to the container. 

         

        In File mode, make sure you provision ML storage volume with sufficient capacity to accomodate the data download from S3. In addition to the training data, the ML storage volume also stores the output model. The algorithm container use ML storage volume to also store intermediate information, if any. 

         

        For distributed algorithms using File mode, training data is distributed uniformly, and your training duration is predictable if the input data objects size is approximately same. Amazon SageMaker does not split the files any further for model training. If the object sizes are skewed, training won't be optimal as the data distribution is also skewed where one host in a training cluster is overloaded, thus becoming bottleneck in training. 

        

      
    
    :type RoleArn: string
    :param RoleArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf. 

       

      During model training, Amazon SageMaker needs your permission to read input data from an S3 bucket, download a Docker image that contains training code, write model artifacts to an S3 bucket, write logs to Amazon CloudWatch Logs, and publish metrics to Amazon CloudWatch. You grant permissions for all of these tasks to an IAM role. For more information, see `Amazon SageMaker Roles <http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html>`__ . 

      

    
    :type InputDataConfig: list
    :param InputDataConfig: **[REQUIRED]** 

      An array of ``Channel`` objects. Each channel is a named input source. ``InputDataConfig`` describes the input data and its location. 

       

      Algorithms can accept input data from one or more channels. For example, an algorithm might have two channels of input data, ``training_data`` and ``validation_data`` . The configuration for each channel provides the S3 location where the input data is stored. It also provides information about the stored data: the MIME type, compression method, and whether the data is wrapped in RecordIO format. 

       

      Depending on the input mode that the algorithm supports, Amazon SageMaker either copies input data files from an S3 bucket to a local directory in the Docker container, or makes it available as input streams. 

      

    
      - *(dict) --* 

        A channel is a named input source that training algorithms can consume. 

        

      
        - **ChannelName** *(string) --* **[REQUIRED]** 

          The name of the channel. 

          

        
        - **DataSource** *(dict) --* **[REQUIRED]** 

          The location of the channel data.

          

        
          - **S3DataSource** *(dict) --* **[REQUIRED]** 

            The S3 location of the data source that is associated with a channel.

            

          
            - **S3DataType** *(string) --* **[REQUIRED]** 

              If you choose ``S3Prefix`` , ``S3Uri`` identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for model training. 

               

              If you choose ``ManifestFile`` , ``S3Uri`` identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for model training. 

              

            
            - **S3Uri** *(string) --* **[REQUIRED]** 

              Depending on the value specified for the ``S3DataType`` , identifies either a key name prefix or a manifest. For example: 

               

               
              * A key name prefix might look like this: ``s3://bucketname/exampleprefix`` .  
               
              * A manifest might look like this: ``s3://bucketname/example.manifest``   The manifest is an S3 object which is a JSON file with the following format:   ``[``    ``{"prefix": "s3://customer_bucket/some/prefix/"},``    ``"relative/path/to/custdata-1",``    ``"relative/path/custdata-2",``    ``...``    ``]``   The preceding JSON matches the following ``s3Uris`` :   ``s3://customer_bucket/some/prefix/relative/path/to/custdata-1``    ``s3://customer_bucket/some/prefix/relative/path/custdata-1``    ``...``   The complete set of ``s3uris`` in this manifest constitutes the input data for the channel for this datasource. The object that each ``s3uris`` points to must readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.  
               

              

            
            - **S3DataDistributionType** *(string) --* 

              If you want Amazon SageMaker to replicate the entire dataset on each ML compute instance that is launched for model training, specify ``FullyReplicated`` . 

               

              If you want Amazon SageMaker to replicate a subset of data on each ML compute instance that is launched for model training, specify ``ShardedByS3Key`` . If there are *n* ML compute instances launched for a training job, each instance gets approximately 1/*n* of the number of S3 objects. In this case, model training on each machine uses only the subset of training data. 

               

              Don't choose more ML compute instances for training than available S3 objects. If you do, some nodes won't get any data and you will pay for nodes that aren't getting any training data. This applies in both FILE and PIPE modes. Keep this in mind when developing algorithms. 

               

              In distributed training, where you use multiple ML compute EC2 instances, you might choose ``ShardedByS3Key`` . If the algorithm requires copying training data to the ML storage volume (when ``TrainingInputMode`` is set to ``File`` ), this copies 1/*n* of the number of objects. 

              

            
          
        
        - **ContentType** *(string) --* 

          The MIME type of the data.

          

        
        - **CompressionType** *(string) --* 

          If training data is compressed, the compression type. The default value is ``None`` . ``CompressionType`` is used only in PIPE input mode. In FILE mode, leave this field unset or set it to None.

          

        
        - **RecordWrapperType** *(string) --* 

          

           

          Specify RecordIO as the value when input data is in raw format but the training algorithm requires the RecordIO format, in which caseAmazon SageMaker wraps each individual S3 object in a RecordIO record. If the input data is already in RecordIO format, you don't need to set this attribute. For more information, see `Create a Dataset Using RecordIO <https://mxnet.incubator.apache.org/how_to/recordio.html?highlight=im2rec>`__ . 

           

          In FILE mode, leave this field unset or set it to None.

           

          

          

        
      
  
    :type OutputDataConfig: dict
    :param OutputDataConfig: **[REQUIRED]** 

      Specifies the path to the S3 bucket where you want to store model artifacts. Amazon SageMaker creates subfolders for the artifacts. 

      

    
      - **KmsKeyId** *(string) --* 

        The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. 

         

        .. note::

           

          If the configuration of the output S3 bucket requires server-side encryption for objects, and you don't provide the KMS key ID, Amazon SageMaker uses the default service key. For more information, see `KMS-Managed Encryption Keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ in Amazon Simple Storage Service developer guide.

           

         

        .. note::

           

          The KMS key policy must grant permission to the IAM role you specify in your ``CreateTrainingJob`` request. `Using Key Policies in AWS KMS <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ in the AWS Key Management Service Developer Guide. 

           

        

      
      - **S3OutputPath** *(string) --* **[REQUIRED]** 

        Identifies the S3 path where you want Amazon SageMaker to store the model artifacts. For example, ``s3://bucket-name/key-name-prefix`` . 

        

      
    
    :type ResourceConfig: dict
    :param ResourceConfig: **[REQUIRED]** 

      The resources, including the ML compute instances and ML storage volumes, to use for model training. 

       

      ML storage volumes store model artifacts and incremental states. Training algorithms might also use ML storage volumes for scratch space. If you want Amazon SageMaker to use the ML storage volume to store the training data, choose ``File`` as the ``TrainingInputMode`` in the algorithm specification. For distributed training algorithms, specify an instance count greater than 1.

      

    
      - **InstanceType** *(string) --* **[REQUIRED]** 

        The ML compute instance type. 

        

      
      - **InstanceCount** *(integer) --* **[REQUIRED]** 

        The number of ML compute instances to use. For distributed training, provide a value greater than 1. 

        

      
      - **VolumeSizeInGB** *(integer) --* **[REQUIRED]** 

        The size of the ML storage volume that you want to provision. 

         

        ML storage volumes store model artifacts and incremental states. Training algorithms might also use the ML storage volume for scratch space. If you want to store the training data in the ML storage volume, choose ``File`` as the ``TrainingInputMode`` in the algorithm specification. 

         

        You must specify sufficient ML storage for your scenario. 

         

        .. note::

           

          Amazon SageMaker supports only the General Purpose SSD (gp2) ML storage volume type. 

           

        

      
    
    :type StoppingCondition: dict
    :param StoppingCondition: **[REQUIRED]** 

      Sets a duration for training. Use this parameter to cap model training costs. To stop a job, Amazon SageMaker sends the algorithm the ``SIGTERM`` signal, which delays job termination for 120 seconds. Algorithms might use this 120-second window to save the model artifacts. 

       

      When Amazon SageMaker terminates a job because the stopping condition has been met, training algorithms provided by Amazon SageMaker save the intermediate results of the job. This intermediate data is a valid model artifact. You can use it to create a model using the ``CreateModel`` API. 

      

    
      - **MaxRuntimeInSeconds** *(integer) --* 

        The maximum length of time, in seconds, that the training job can run. If model training does not complete during this time, Amazon SageMaker ends the job. If value is not specified, default value is 1 day. Maximum value is 5 days.

        

      
    
    :type Tags: list
    :param Tags: 

      An array of key-value pairs. For more information, see `Using Cost Allocation Tags <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what>`__ in the *AWS Billing and Cost Management User Guide* . 

      

    
      - *(dict) --* 

        Describes a tag. 

        

      
        - **Key** *(string) --* **[REQUIRED]** 

          The tag key.

          

        
        - **Value** *(string) --* **[REQUIRED]** 

          The tag value.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TrainingJobArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TrainingJobArn** *(string) --* 

          The Amazon Resource Name (ARN) of the training job.

          
    

  .. py:method:: delete_endpoint(**kwargs)

    

    Deletes an endpoint. Amazon SageMaker frees up all of the resources that were deployed when the endpoint was created. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DeleteEndpoint>`_    


    **Request Syntax** 
    ::

      response = client.delete_endpoint(
          EndpointName='string'
      )
    :type EndpointName: string
    :param EndpointName: **[REQUIRED]** 

      The name of the endpoint that you want to delete.

      

    
    
    :returns: None

  .. py:method:: delete_endpoint_config(**kwargs)

    

    Deletes an endpoint configuration. The ``DeleteEndpoingConfig`` API deletes only the specified configuration. It does not delete endpoints created using the configuration. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DeleteEndpointConfig>`_    


    **Request Syntax** 
    ::

      response = client.delete_endpoint_config(
          EndpointConfigName='string'
      )
    :type EndpointConfigName: string
    :param EndpointConfigName: **[REQUIRED]** 

      The name of the endpoint configuration that you want to delete.

      

    
    
    :returns: None

  .. py:method:: delete_model(**kwargs)

    

    Deletes a model. The ``DeleteModel`` API deletes only the model entry that was created in Amazon SageMaker when you called the `CreateModel <http://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateModel.html>`__ API. It does not delete model artifacts, inference code, or the IAM role that you specified when creating the model. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DeleteModel>`_    


    **Request Syntax** 
    ::

      response = client.delete_model(
          ModelName='string'
      )
    :type ModelName: string
    :param ModelName: **[REQUIRED]** 

      The name of the model to delete.

      

    
    
    :returns: None

  .. py:method:: delete_notebook_instance(**kwargs)

    

    Deletes an Amazon SageMaker notebook instance. Before you can delete a notebook instance, you must call the ``StopNotebookInstance`` API. 

     

    .. warning::

       

      When you delete a notebook instance, you lose all of your data. Amazon SageMaker removes the ML compute instance, and deletes the ML storage volume and the network interface associated with the notebook instance. 

       

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DeleteNotebookInstance>`_    


    **Request Syntax** 
    ::

      response = client.delete_notebook_instance(
          NotebookInstanceName='string'
      )
    :type NotebookInstanceName: string
    :param NotebookInstanceName: **[REQUIRED]** 

      The name of the Amazon SageMaker notebook instance to delete.

      

    
    
    :returns: None

  .. py:method:: delete_tags(**kwargs)

    

    Deletes the specified tags from an Amazon SageMaker resource.

     

    To list a resource's tags, use the ``ListTags`` API. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DeleteTags>`_    


    **Request Syntax** 
    ::

      response = client.delete_tags(
          ResourceArn='string',
          TagKeys=[
              'string',
          ]
      )
    :type ResourceArn: string
    :param ResourceArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the resource whose tags you want to delete.

      

    
    :type TagKeys: list
    :param TagKeys: **[REQUIRED]** 

      An array or one or more tag keys to delete.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: describe_endpoint(**kwargs)

    

    Returns the description of an endpoint.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeEndpoint>`_    


    **Request Syntax** 
    ::

      response = client.describe_endpoint(
          EndpointName='string'
      )
    :type EndpointName: string
    :param EndpointName: **[REQUIRED]** 

      The name of the endpoint.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'EndpointName': 'string',
            'EndpointArn': 'string',
            'EndpointConfigName': 'string',
            'ProductionVariants': [
                {
                    'VariantName': 'string',
                    'CurrentWeight': ...,
                    'DesiredWeight': ...,
                    'CurrentInstanceCount': 123,
                    'DesiredInstanceCount': 123
                },
            ],
            'EndpointStatus': 'OutOfService'|'Creating'|'Updating'|'RollingBack'|'InService'|'Deleting'|'Failed',
            'FailureReason': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'LastModifiedTime': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **EndpointName** *(string) --* 

          Name of the endpoint.

          
        

        - **EndpointArn** *(string) --* 

          The Amazon Resource Name (ARN) of the endpoint.

          
        

        - **EndpointConfigName** *(string) --* 

          The name of the endpoint configuration associated with this endpoint.

          
        

        - **ProductionVariants** *(list) --* 

          An array of ProductionVariant objects, one for each model hosted behind this endpoint. 

          
          

          - *(dict) --* 

            Describes weight and capacities for a production variant associated with an endpoint. If you sent a request to the ``UpdateWeightAndCapacities`` API and the endpoint status is ``Updating`` , you get different desired and current values. 

            
            

            - **VariantName** *(string) --* 

              The name of the variant.

              
            

            - **CurrentWeight** *(float) --* 

              The weight associated with the variant.

              
            

            - **DesiredWeight** *(float) --* 

              The requested weight, as specified in the ``UpdateWeightAndCapacities`` request. 

              
            

            - **CurrentInstanceCount** *(integer) --* 

              The number of instances associated with the variant.

              
            

            - **DesiredInstanceCount** *(integer) --* 

              The number of instances requested in the ``UpdateWeightAndCapacities`` request. 

              
        
      
        

        - **EndpointStatus** *(string) --* 

          The status of the endpoint.

          
        

        - **FailureReason** *(string) --* 

          If the status of the endpoint is ``Failed`` , the reason why it failed. 

          
        

        - **CreationTime** *(datetime) --* 

          A timestamp that shows when the endpoint was created.

          
        

        - **LastModifiedTime** *(datetime) --* 

          A timestamp that shows when the endpoint was last modified.

          
    

  .. py:method:: describe_endpoint_config(**kwargs)

    

    Returns the description of an endpoint configuration created using the ``CreateEndpointConfig`` API.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeEndpointConfig>`_    


    **Request Syntax** 
    ::

      response = client.describe_endpoint_config(
          EndpointConfigName='string'
      )
    :type EndpointConfigName: string
    :param EndpointConfigName: **[REQUIRED]** 

      The name of the endpoint configuration.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'EndpointConfigName': 'string',
            'EndpointConfigArn': 'string',
            'ProductionVariants': [
                {
                    'VariantName': 'string',
                    'ModelName': 'string',
                    'InitialInstanceCount': 123,
                    'InstanceType': 'ml.c4.2xlarge'|'ml.c4.8xlarge'|'ml.c4.xlarge'|'ml.c5.2xlarge'|'ml.c5.9xlarge'|'ml.c5.xlarge'|'ml.m4.xlarge'|'ml.p2.xlarge'|'ml.p3.2xlarge'|'ml.t2.medium',
                    'InitialVariantWeight': ...
                },
            ],
            'CreationTime': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **EndpointConfigName** *(string) --* 

          Name of the Amazon SageMaker endpoint configuration.

          
        

        - **EndpointConfigArn** *(string) --* 

          The Amazon Resource Name (ARN) of the endpoint configuration.

          
        

        - **ProductionVariants** *(list) --* 

          An array of ``ProductionVariant`` objects, one for each model that you want to host at this endpoint.

          
          

          - *(dict) --* 

            Identifies a model that you want to host and the resources to deploy for hosting it. If you are deploying multiple models, tell Amazon SageMaker how to distribute traffic among the models by specifying variant weights. 

            
            

            - **VariantName** *(string) --* 

              The name of the production variant.

              
            

            - **ModelName** *(string) --* 

              The name of the model that you want to host. This is the name that you specified when creating the model.

              
            

            - **InitialInstanceCount** *(integer) --* 

              Number of instances to launch initially.

              
            

            - **InstanceType** *(string) --* 

              The ML compute instance type.

              
            

            - **InitialVariantWeight** *(float) --* 

              Determines initial traffic distribution among all of the models that you specify in the endpoint configuration. The traffic to a production variant is determined by the ratio of the ``VariantWeight`` to the sum of all ``VariantWeight`` values across all ProductionVariants. If unspecified, it defaults to 1.0. 

              
        
      
        

        - **CreationTime** *(datetime) --* 

          A timestamp that shows when the endpoint configuration was created.

          
    

  .. py:method:: describe_model(**kwargs)

    

    Describes a model that you created using the ``CreateModel`` API.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeModel>`_    


    **Request Syntax** 
    ::

      response = client.describe_model(
          ModelName='string'
      )
    :type ModelName: string
    :param ModelName: **[REQUIRED]** 

      The name of the model.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ModelName': 'string',
            'PrimaryContainer': {
                'ContainerHostname': 'string',
                'Image': 'string',
                'ModelDataUrl': 'string',
                'Environment': {
                    'string': 'string'
                }
            },
            'SupplementalContainers': [
                {
                    'ContainerHostname': 'string',
                    'Image': 'string',
                    'ModelDataUrl': 'string',
                    'Environment': {
                        'string': 'string'
                    }
                },
            ],
            'ExecutionRoleArn': 'string',
            'CreationTime': datetime(2015, 1, 1),
            'ModelArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ModelName** *(string) --* 

          Name of the Amazon SageMaker model.

          
        

        - **PrimaryContainer** *(dict) --* 

          The location of the primary inference code, associated artifacts, and custom environment map that the inference code uses when it is deployed in production. 

          
          

          - **ContainerHostname** *(string) --* 

            The DNS host name for the container after Amazon SageMaker deploys it.

            
          

          - **Image** *(string) --* 

            The Amazon EC2 Container Registry (Amazon ECR) path where inference code is stored. If you are using your own custom algorithm instead of an algorithm provided by Amazon SageMaker, the inference code must meet Amazon SageMaker requirements. For more information, see `Using Your Own Algorithms with Amazon SageMaker <http://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html>`__  

            
          

          - **ModelDataUrl** *(string) --* 

            The S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix). 

            
          

          - **Environment** *(dict) --* 

            The environment variables to set in the Docker container. Each key and value in the ``Environment`` string to string map can have length of up to 1024. We support up to 16 entries in the map. 

            
            

            - *(string) --* 
              

              - *(string) --* 
        
      
      
        

        - **SupplementalContainers** *(list) --* 

          The description of additional optional containers that you defined when creating the model.

          
          

          - *(dict) --* 

            Describes the container, as part of model definition.

            
            

            - **ContainerHostname** *(string) --* 

              The DNS host name for the container after Amazon SageMaker deploys it.

              
            

            - **Image** *(string) --* 

              The Amazon EC2 Container Registry (Amazon ECR) path where inference code is stored. If you are using your own custom algorithm instead of an algorithm provided by Amazon SageMaker, the inference code must meet Amazon SageMaker requirements. For more information, see `Using Your Own Algorithms with Amazon SageMaker <http://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html>`__  

              
            

            - **ModelDataUrl** *(string) --* 

              The S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix). 

              
            

            - **Environment** *(dict) --* 

              The environment variables to set in the Docker container. Each key and value in the ``Environment`` string to string map can have length of up to 1024. We support up to 16 entries in the map. 

              
              

              - *(string) --* 
                

                - *(string) --* 
          
        
        
      
        

        - **ExecutionRoleArn** *(string) --* 

          The Amazon Resource Name (ARN) of the IAM role that you specified for the model.

          
        

        - **CreationTime** *(datetime) --* 

          A timestamp that shows when the model was created.

          
        

        - **ModelArn** *(string) --* 

          The Amazon Resource Name (ARN) of the model.

          
    

  .. py:method:: describe_notebook_instance(**kwargs)

    

    Returns information about a notebook instance.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeNotebookInstance>`_    


    **Request Syntax** 
    ::

      response = client.describe_notebook_instance(
          NotebookInstanceName='string'
      )
    :type NotebookInstanceName: string
    :param NotebookInstanceName: **[REQUIRED]** 

      The name of the notebook instance that you want information about.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NotebookInstanceArn': 'string',
            'NotebookInstanceName': 'string',
            'NotebookInstanceStatus': 'Pending'|'InService'|'Stopping'|'Stopped'|'Failed'|'Deleting',
            'FailureReason': 'string',
            'Url': 'string',
            'InstanceType': 'ml.t2.medium'|'ml.m4.xlarge'|'ml.p2.xlarge',
            'SubnetId': 'string',
            'SecurityGroups': [
                'string',
            ],
            'RoleArn': 'string',
            'KmsKeyId': 'string',
            'NetworkInterfaceId': 'string',
            'LastModifiedTime': datetime(2015, 1, 1),
            'CreationTime': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NotebookInstanceArn** *(string) --* 

          The Amazon Resource Name (ARN) of the notebook instance.

          
        

        - **NotebookInstanceName** *(string) --* 

          Name of the Amazon SageMaker notebook instance. 

          
        

        - **NotebookInstanceStatus** *(string) --* 

          The status of the notebook instance.

          
        

        - **FailureReason** *(string) --* 

          If staus is failed, the reason it failed.

          
        

        - **Url** *(string) --* 

          The URL that you use to connect to the Jupyter notebook that is running in your notebook instance. 

          
        

        - **InstanceType** *(string) --* 

          The type of ML compute instance running on the notebook instance.

          
        

        - **SubnetId** *(string) --* 

          The ID of the VPC subnet.

          
        

        - **SecurityGroups** *(list) --* 

          The IDs of the VPC security groups.

          
          

          - *(string) --* 
      
        

        - **RoleArn** *(string) --* 

          Amazon Resource Name (ARN) of the IAM role associated with the instance. 

          
        

        - **KmsKeyId** *(string) --* 

          AWS KMS key ID Amazon SageMaker uses to encrypt data when storing it on the ML storage volume attached to the instance. 

          
        

        - **NetworkInterfaceId** *(string) --* 

          Network interface IDs that Amazon SageMaker created at the time of creating the instance. 

          
        

        - **LastModifiedTime** *(datetime) --* 

          A timestamp. Use this parameter to retrieve the time when the notebook instance was last modified. 

          
        

        - **CreationTime** *(datetime) --* 

          A timestamp. Use this parameter to return the time when the notebook instance was created

          
    

  .. py:method:: describe_training_job(**kwargs)

    

    Returns information about a training job.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeTrainingJob>`_    


    **Request Syntax** 
    ::

      response = client.describe_training_job(
          TrainingJobName='string'
      )
    :type TrainingJobName: string
    :param TrainingJobName: **[REQUIRED]** 

      The name of the training job.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TrainingJobName': 'string',
            'TrainingJobArn': 'string',
            'ModelArtifacts': {
                'S3ModelArtifacts': 'string'
            },
            'TrainingJobStatus': 'InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
            'SecondaryStatus': 'Starting'|'Downloading'|'Training'|'Uploading'|'Stopping'|'Stopped'|'MaxRuntimeExceeded'|'Completed'|'Failed',
            'FailureReason': 'string',
            'HyperParameters': {
                'string': 'string'
            },
            'AlgorithmSpecification': {
                'TrainingImage': 'string',
                'TrainingInputMode': 'Pipe'|'File'
            },
            'RoleArn': 'string',
            'InputDataConfig': [
                {
                    'ChannelName': 'string',
                    'DataSource': {
                        'S3DataSource': {
                            'S3DataType': 'ManifestFile'|'S3Prefix',
                            'S3Uri': 'string',
                            'S3DataDistributionType': 'FullyReplicated'|'ShardedByS3Key'
                        }
                    },
                    'ContentType': 'string',
                    'CompressionType': 'None'|'Gzip',
                    'RecordWrapperType': 'None'|'RecordIO'
                },
            ],
            'OutputDataConfig': {
                'KmsKeyId': 'string',
                'S3OutputPath': 'string'
            },
            'ResourceConfig': {
                'InstanceType': 'ml.m4.xlarge'|'ml.m4.4xlarge'|'ml.m4.10xlarge'|'ml.c4.xlarge'|'ml.c4.2xlarge'|'ml.c4.8xlarge'|'ml.p2.xlarge'|'ml.p2.8xlarge'|'ml.p2.16xlarge'|'ml.p3.2xlarge'|'ml.p3.8xlarge'|'ml.p3.16xlarge'|'ml.c5.xlarge'|'ml.c5.2xlarge'|'ml.c5.4xlarge'|'ml.c5.9xlarge'|'ml.c5.18xlarge',
                'InstanceCount': 123,
                'VolumeSizeInGB': 123
            },
            'StoppingCondition': {
                'MaxRuntimeInSeconds': 123
            },
            'CreationTime': datetime(2015, 1, 1),
            'TrainingStartTime': datetime(2015, 1, 1),
            'TrainingEndTime': datetime(2015, 1, 1),
            'LastModifiedTime': datetime(2015, 1, 1)
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TrainingJobName** *(string) --* 

          Name of the model training job. 

          
        

        - **TrainingJobArn** *(string) --* 

          The Amazon Resource Name (ARN) of the training job.

          
        

        - **ModelArtifacts** *(dict) --* 

          Information about the Amazon S3 location that is configured for storing model artifacts. 

          
          

          - **S3ModelArtifacts** *(string) --* 

            The path of the S3 object that contains the model artifacts. For example, ``s3://bucket-name/keynameprefix/model.tar.gz`` .

            
      
        

        - **TrainingJobStatus** *(string) --* 

          The status of the training job. 

           

          For the ``InProgress`` status, Amazon SageMaker can return these secondary statuses:

           

           
          * Starting - Preparing for training. 
           
          * Downloading - Optional stage for algorithms that support File training input mode. It indicates data is being downloaded to ML storage volumes. 
           
          * Training - Training is in progress. 
           
          * Uploading - Training is complete and model upload is in progress. 
           

           

          For the ``Stopped`` training status, Amazon SageMaker can return these secondary statuses:

           

           
          * MaxRuntimeExceeded - Job stopped as a result of maximum allowed runtime exceeded. 
           

          
        

        - **SecondaryStatus** *(string) --* 

          Provides granular information about the system state. For more information, see ``TrainingJobStatus`` . 

          
        

        - **FailureReason** *(string) --* 

          If the training job failed, the reason it failed. 

          
        

        - **HyperParameters** *(dict) --* 

          Algorithm-specific parameters. 

          
          

          - *(string) --* 
            

            - *(string) --* 
      
    
        

        - **AlgorithmSpecification** *(dict) --* 

          Information about the algorithm used for training, and algorithm metadata. 

          
          

          - **TrainingImage** *(string) --* 

            The registry path of the Docker image that contains the training algorithm. For information about using your own algorithms, see `Docker Registry Paths for Algorithms Provided by Amazon SageMaker <http://docs.aws.amazon.com/sagemaker/latest/dg/algos-docker-registry-paths.html>`__ . 

            
          

          - **TrainingInputMode** *(string) --* 

            The input mode that the algorithm supports. For the input modes that Amazon SageMaker algorithms support, see `Algorithms <http://docs.aws.amazon.com/sagemaker/latest/dg/algos.html>`__ . If an algorithm supports the ``File`` input mode, Amazon SageMaker downloads the training data from S3 to the provisioned ML storage Volume, and mounts the directory to docker volume for training container. If an algorithm supports the ``Pipe`` input mode, Amazon SageMaker streams data directly from S3 to the container. 

             

            In File mode, make sure you provision ML storage volume with sufficient capacity to accomodate the data download from S3. In addition to the training data, the ML storage volume also stores the output model. The algorithm container use ML storage volume to also store intermediate information, if any. 

             

            For distributed algorithms using File mode, training data is distributed uniformly, and your training duration is predictable if the input data objects size is approximately same. Amazon SageMaker does not split the files any further for model training. If the object sizes are skewed, training won't be optimal as the data distribution is also skewed where one host in a training cluster is overloaded, thus becoming bottleneck in training. 

            
      
        

        - **RoleArn** *(string) --* 

          The AWS Identity and Access Management (IAM) role configured for the training job. 

          
        

        - **InputDataConfig** *(list) --* 

          An array of ``Channel`` objects that describes each data input channel. 

          
          

          - *(dict) --* 

            A channel is a named input source that training algorithms can consume. 

            
            

            - **ChannelName** *(string) --* 

              The name of the channel. 

              
            

            - **DataSource** *(dict) --* 

              The location of the channel data.

              
              

              - **S3DataSource** *(dict) --* 

                The S3 location of the data source that is associated with a channel.

                
                

                - **S3DataType** *(string) --* 

                  If you choose ``S3Prefix`` , ``S3Uri`` identifies a key name prefix. Amazon SageMaker uses all objects with the specified key name prefix for model training. 

                   

                  If you choose ``ManifestFile`` , ``S3Uri`` identifies an object that is a manifest file containing a list of object keys that you want Amazon SageMaker to use for model training. 

                  
                

                - **S3Uri** *(string) --* 

                  Depending on the value specified for the ``S3DataType`` , identifies either a key name prefix or a manifest. For example: 

                   

                   
                  * A key name prefix might look like this: ``s3://bucketname/exampleprefix`` .  
                   
                  * A manifest might look like this: ``s3://bucketname/example.manifest``   The manifest is an S3 object which is a JSON file with the following format:   ``[``    ``{"prefix": "s3://customer_bucket/some/prefix/"},``    ``"relative/path/to/custdata-1",``    ``"relative/path/custdata-2",``    ``...``    ``]``   The preceding JSON matches the following ``s3Uris`` :   ``s3://customer_bucket/some/prefix/relative/path/to/custdata-1``    ``s3://customer_bucket/some/prefix/relative/path/custdata-1``    ``...``   The complete set of ``s3uris`` in this manifest constitutes the input data for the channel for this datasource. The object that each ``s3uris`` points to must readable by the IAM role that Amazon SageMaker uses to perform tasks on your behalf.  
                   

                  
                

                - **S3DataDistributionType** *(string) --* 

                  If you want Amazon SageMaker to replicate the entire dataset on each ML compute instance that is launched for model training, specify ``FullyReplicated`` . 

                   

                  If you want Amazon SageMaker to replicate a subset of data on each ML compute instance that is launched for model training, specify ``ShardedByS3Key`` . If there are *n* ML compute instances launched for a training job, each instance gets approximately 1/*n* of the number of S3 objects. In this case, model training on each machine uses only the subset of training data. 

                   

                  Don't choose more ML compute instances for training than available S3 objects. If you do, some nodes won't get any data and you will pay for nodes that aren't getting any training data. This applies in both FILE and PIPE modes. Keep this in mind when developing algorithms. 

                   

                  In distributed training, where you use multiple ML compute EC2 instances, you might choose ``ShardedByS3Key`` . If the algorithm requires copying training data to the ML storage volume (when ``TrainingInputMode`` is set to ``File`` ), this copies 1/*n* of the number of objects. 

                  
            
          
            

            - **ContentType** *(string) --* 

              The MIME type of the data.

              
            

            - **CompressionType** *(string) --* 

              If training data is compressed, the compression type. The default value is ``None`` . ``CompressionType`` is used only in PIPE input mode. In FILE mode, leave this field unset or set it to None.

              
            

            - **RecordWrapperType** *(string) --* 

              

               

              Specify RecordIO as the value when input data is in raw format but the training algorithm requires the RecordIO format, in which caseAmazon SageMaker wraps each individual S3 object in a RecordIO record. If the input data is already in RecordIO format, you don't need to set this attribute. For more information, see `Create a Dataset Using RecordIO <https://mxnet.incubator.apache.org/how_to/recordio.html?highlight=im2rec>`__ . 

               

              In FILE mode, leave this field unset or set it to None.

               

              

              
        
      
        

        - **OutputDataConfig** *(dict) --* 

          The S3 path where model artifacts that you configured when creating the job are stored. Amazon SageMaker creates subfolders for model artifacts. 

          
          

          - **KmsKeyId** *(string) --* 

            The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption. 

             

            .. note::

               

              If the configuration of the output S3 bucket requires server-side encryption for objects, and you don't provide the KMS key ID, Amazon SageMaker uses the default service key. For more information, see `KMS-Managed Encryption Keys <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html>`__ in Amazon Simple Storage Service developer guide.

               

             

            .. note::

               

              The KMS key policy must grant permission to the IAM role you specify in your ``CreateTrainingJob`` request. `Using Key Policies in AWS KMS <http://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ in the AWS Key Management Service Developer Guide. 

               

            
          

          - **S3OutputPath** *(string) --* 

            Identifies the S3 path where you want Amazon SageMaker to store the model artifacts. For example, ``s3://bucket-name/key-name-prefix`` . 

            
      
        

        - **ResourceConfig** *(dict) --* 

          Resources, including ML compute instances and ML storage volumes, that are configured for model training. 

          
          

          - **InstanceType** *(string) --* 

            The ML compute instance type. 

            
          

          - **InstanceCount** *(integer) --* 

            The number of ML compute instances to use. For distributed training, provide a value greater than 1. 

            
          

          - **VolumeSizeInGB** *(integer) --* 

            The size of the ML storage volume that you want to provision. 

             

            ML storage volumes store model artifacts and incremental states. Training algorithms might also use the ML storage volume for scratch space. If you want to store the training data in the ML storage volume, choose ``File`` as the ``TrainingInputMode`` in the algorithm specification. 

             

            You must specify sufficient ML storage for your scenario. 

             

            .. note::

               

              Amazon SageMaker supports only the General Purpose SSD (gp2) ML storage volume type. 

               

            
      
        

        - **StoppingCondition** *(dict) --* 

          The condition under which to stop the training job. 

          
          

          - **MaxRuntimeInSeconds** *(integer) --* 

            The maximum length of time, in seconds, that the training job can run. If model training does not complete during this time, Amazon SageMaker ends the job. If value is not specified, default value is 1 day. Maximum value is 5 days.

            
      
        

        - **CreationTime** *(datetime) --* 

          A timestamp that indicates when the training job was created.

          
        

        - **TrainingStartTime** *(datetime) --* 

          A timestamp that indicates when training started.

          
        

        - **TrainingEndTime** *(datetime) --* 

          A timestamp that indicates when model training ended.

          
        

        - **LastModifiedTime** *(datetime) --* 

          A timestamp that indicates when the status of the training job was last modified.

          
    

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

        


  .. py:method:: list_endpoint_configs(**kwargs)

    

    Lists endpoint configurations.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListEndpointConfigs>`_    


    **Request Syntax** 
    ::

      response = client.list_endpoint_configs(
          SortBy='Name'|'CreationTime',
          SortOrder='Ascending'|'Descending',
          NextToken='string',
          MaxResults=123,
          NameContains='string',
          CreationTimeBefore=datetime(2015, 1, 1),
          CreationTimeAfter=datetime(2015, 1, 1)
      )
    :type SortBy: string
    :param SortBy: 

      The field to sort results by. The default is ``CreationTime`` .

      

    
    :type SortOrder: string
    :param SortOrder: 

      The sort order for results. The default is ``Ascending`` .

      

    
    :type NextToken: string
    :param NextToken: 

      If the result of the previous ``ListEndpointConfig`` request was truncated, the response includes a ``NextToken`` . To retrieve the next set of endpoint configurations, use the token in the next request. 

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of training jobs to return in the response.

      

    
    :type NameContains: string
    :param NameContains: 

      A string in the endpoint configuration name. This filter returns only endpoint configurations whose name contains the specified string. 

      

    
    :type CreationTimeBefore: datetime
    :param CreationTimeBefore: 

      A filter that returns only endpoint configurations created before the specified time (timestamp).

      

    
    :type CreationTimeAfter: datetime
    :param CreationTimeAfter: 

      A filter that returns only endpoint configurations created after the specified time (timestamp).

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'EndpointConfigs': [
                {
                    'EndpointConfigName': 'string',
                    'EndpointConfigArn': 'string',
                    'CreationTime': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **EndpointConfigs** *(list) --* 

          An array of endpoint configurations.

          
          

          - *(dict) --* 

            Provides summary information for an endpoint configuration.

            
            

            - **EndpointConfigName** *(string) --* 

              The name of the endpoint configuration.

              
            

            - **EndpointConfigArn** *(string) --* 

              The Amazon Resource Name (ARN) of the endpoint configuration.

              
            

            - **CreationTime** *(datetime) --* 

              A timestamp that shows when the endpoint configuration was created.

              
        
      
        

        - **NextToken** *(string) --* 

          If the response is truncated, Amazon SageMaker returns this token. To retrieve the next set of endpoint configurations, use it in the subsequent request 

          
    

  .. py:method:: list_endpoints(**kwargs)

    

    Lists endpoints.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListEndpoints>`_    


    **Request Syntax** 
    ::

      response = client.list_endpoints(
          SortBy='Name'|'CreationTime'|'Status',
          SortOrder='Ascending'|'Descending',
          NextToken='string',
          MaxResults=123,
          NameContains='string',
          CreationTimeBefore=datetime(2015, 1, 1),
          CreationTimeAfter=datetime(2015, 1, 1),
          LastModifiedTimeBefore=datetime(2015, 1, 1),
          LastModifiedTimeAfter=datetime(2015, 1, 1),
          StatusEquals='OutOfService'|'Creating'|'Updating'|'RollingBack'|'InService'|'Deleting'|'Failed'
      )
    :type SortBy: string
    :param SortBy: 

      Sorts the list of results. The default is ``CreationTime`` .

      

    
    :type SortOrder: string
    :param SortOrder: 

      The sort order for results. The default is ``Ascending`` .

      

    
    :type NextToken: string
    :param NextToken: 

      If the result of a ``ListEndpoints`` request was truncated, the response includes a ``NextToken`` . To retrieve the next set of endpoints, use the token in the next request.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of endpoints to return in the response.

      

    
    :type NameContains: string
    :param NameContains: 

      A string in endpoint names. This filter returns only endpoints whose name contains the specified string.

      

    
    :type CreationTimeBefore: datetime
    :param CreationTimeBefore: 

      A filter that returns only endpoints that were created before the specified time (timestamp).

      

    
    :type CreationTimeAfter: datetime
    :param CreationTimeAfter: 

      A filter that returns only endpoints that were created after the specified time (timestamp).

      

    
    :type LastModifiedTimeBefore: datetime
    :param LastModifiedTimeBefore: 

      A filter that returns only endpoints that were modified before the specified timestamp. 

      

    
    :type LastModifiedTimeAfter: datetime
    :param LastModifiedTimeAfter: 

      A filter that returns only endpoints that were modified after the specified timestamp. 

      

    
    :type StatusEquals: string
    :param StatusEquals: 

      A filter that returns only endpoints with the specified status. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Endpoints': [
                {
                    'EndpointName': 'string',
                    'EndpointArn': 'string',
                    'CreationTime': datetime(2015, 1, 1),
                    'LastModifiedTime': datetime(2015, 1, 1),
                    'EndpointStatus': 'OutOfService'|'Creating'|'Updating'|'RollingBack'|'InService'|'Deleting'|'Failed'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Endpoints** *(list) --* 

          An array or endpoint objects. 

          
          

          - *(dict) --* 

            Provides summary information for an endpoint.

            
            

            - **EndpointName** *(string) --* 

              The name of the endpoint.

              
            

            - **EndpointArn** *(string) --* 

              The Amazon Resource Name (ARN) of the endpoint.

              
            

            - **CreationTime** *(datetime) --* 

              A timestamp that shows when the endpoint was created.

              
            

            - **LastModifiedTime** *(datetime) --* 

              A timestamp that shows when the endpoint was last modified.

              
            

            - **EndpointStatus** *(string) --* 

              The status of the endpoint.

              
        
      
        

        - **NextToken** *(string) --* 

          If the response is truncated, Amazon SageMaker returns this token. To retrieve the next set of training jobs, use it in the subsequent request. 

          
    

  .. py:method:: list_models(**kwargs)

    

    Lists models created with the `CreateModel <http://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateModel.html>`__ API.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListModels>`_    


    **Request Syntax** 
    ::

      response = client.list_models(
          SortBy='Name'|'CreationTime',
          SortOrder='Ascending'|'Descending',
          NextToken='string',
          MaxResults=123,
          NameContains='string',
          CreationTimeBefore=datetime(2015, 1, 1),
          CreationTimeAfter=datetime(2015, 1, 1)
      )
    :type SortBy: string
    :param SortBy: 

      Sorts the list of results. The default is ``CreationTime`` .

      

    
    :type SortOrder: string
    :param SortOrder: 

      The sort order for results. The default is ``Ascending`` .

      

    
    :type NextToken: string
    :param NextToken: 

      If the response to a previous ``ListModels`` request was truncated, the response includes a ``NextToken`` . To retrieve the next set of models, use the token in the next request.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of models to return in the response.

      

    
    :type NameContains: string
    :param NameContains: 

      A string in the training job name. This filter returns only models in the training job whose name contains the specified string.

      

    
    :type CreationTimeBefore: datetime
    :param CreationTimeBefore: 

      A filter that returns only models created before the specified time (timestamp).

      

    
    :type CreationTimeAfter: datetime
    :param CreationTimeAfter: 

      A filter that returns only models created after the specified time (timestamp).

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Models': [
                {
                    'ModelName': 'string',
                    'ModelArn': 'string',
                    'CreationTime': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Models** *(list) --* 

          An array of ``ModelSummary`` objects, each of which lists a model.

          
          

          - *(dict) --* 

            Provides summary information about a model.

            
            

            - **ModelName** *(string) --* 

              The name of the model that you want a summary for.

              
            

            - **ModelArn** *(string) --* 

              The Amazon Resource Name (ARN) of the model.

              
            

            - **CreationTime** *(datetime) --* 

              A timestamp that indicates when the model was created.

              
        
      
        

        - **NextToken** *(string) --* 

          If the response is truncated, Amazon SageMaker returns this token. To retrieve the next set of models, use it in the subsequent request. 

          
    

  .. py:method:: list_notebook_instances(**kwargs)

    

    Returns a list of the Amazon SageMaker notebook instances in the requester's account in an AWS Region. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListNotebookInstances>`_    


    **Request Syntax** 
    ::

      response = client.list_notebook_instances(
          NextToken='string',
          MaxResults=123,
          SortBy='Name'|'CreationTime'|'Status',
          SortOrder='Ascending'|'Descending',
          NameContains='string',
          CreationTimeBefore=datetime(2015, 1, 1),
          CreationTimeAfter=datetime(2015, 1, 1),
          LastModifiedTimeBefore=datetime(2015, 1, 1),
          LastModifiedTimeAfter=datetime(2015, 1, 1),
          StatusEquals='Pending'|'InService'|'Stopping'|'Stopped'|'Failed'|'Deleting'
      )
    :type NextToken: string
    :param NextToken: 

      If the previous call to the ``ListNotebookInstances`` is truncated, the response includes a ``NextToken`` . You can use this token in your subsequent ``ListNotebookInstances`` request to fetch the next set of notebook instances. 

       

      .. note::

         

        You might specify a filter or a sort order in your request. When response is truncated, you must use the same values for the filer and sort order in the next request. 

         

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of notebook instances to return.

      

    
    :type SortBy: string
    :param SortBy: 

      The field to sort results by. The default is ``Name`` .

      

    
    :type SortOrder: string
    :param SortOrder: 

      The sort order for results. 

      

    
    :type NameContains: string
    :param NameContains: 

      A string in the notebook instances' name. This filter returns only notebook instances whose name contains the specified string. 

      

    
    :type CreationTimeBefore: datetime
    :param CreationTimeBefore: 

      A filter that returns only notebook instances that were created before the specified time (timestamp). 

      

    
    :type CreationTimeAfter: datetime
    :param CreationTimeAfter: 

      A filter that returns only notebook instances that were created after the specified time (timestamp).

      

    
    :type LastModifiedTimeBefore: datetime
    :param LastModifiedTimeBefore: 

      A filter that returns only notebook instances that were modified before the specified time (timestamp).

      

    
    :type LastModifiedTimeAfter: datetime
    :param LastModifiedTimeAfter: 

      A filter that returns only notebook instances that were modified after the specified time (timestamp).

      

    
    :type StatusEquals: string
    :param StatusEquals: 

      A filter that returns only notebook instances with the specified status.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextToken': 'string',
            'NotebookInstances': [
                {
                    'NotebookInstanceName': 'string',
                    'NotebookInstanceArn': 'string',
                    'NotebookInstanceStatus': 'Pending'|'InService'|'Stopping'|'Stopped'|'Failed'|'Deleting',
                    'Url': 'string',
                    'InstanceType': 'ml.t2.medium'|'ml.m4.xlarge'|'ml.p2.xlarge',
                    'CreationTime': datetime(2015, 1, 1),
                    'LastModifiedTime': datetime(2015, 1, 1)
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NextToken** *(string) --* 

          If the response to the previous ``ListNotebookInstances`` request was truncated, Amazon SageMaker returns this token. To retrieve the next set of notebook instances, use the token in the next request.

          
        

        - **NotebookInstances** *(list) --* 

          An array of ``NotebookInstanceSummary`` objects, one for each notebook instance.

          
          

          - *(dict) --* 

            Provides summary information for an Amazon SageMaker notebook instance.

            
            

            - **NotebookInstanceName** *(string) --* 

              The name of the notebook instance that you want a summary for.

              
            

            - **NotebookInstanceArn** *(string) --* 

              The Amazon Resource Name (ARN) of the notebook instance.

              
            

            - **NotebookInstanceStatus** *(string) --* 

              The status of the notebook instance.

              
            

            - **Url** *(string) --* 

              The URL that you use to connect to the Jupyter instance running in your notebook instance. 

              
            

            - **InstanceType** *(string) --* 

              The type of ML compute instance that the notebook instance is running on.

              
            

            - **CreationTime** *(datetime) --* 

              A timestamp that shows when the notebook instance was created.

              
            

            - **LastModifiedTime** *(datetime) --* 

              A timestamp that shows when the notebook instance was last modified.

              
        
      
    

  .. py:method:: list_tags(**kwargs)

    

    Returns the tags for the specified Amazon SageMaker resource.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListTags>`_    


    **Request Syntax** 
    ::

      response = client.list_tags(
          ResourceArn='string',
          NextToken='string',
          MaxResults=123
      )
    :type ResourceArn: string
    :param ResourceArn: **[REQUIRED]** 

      The Amazon Resource Name (ARN) of the resource whose tags you want to retrieve.

      

    
    :type NextToken: string
    :param NextToken: 

      If the response to the previous ``ListTags`` request is truncated, Amazon SageMaker returns this token. To retrieve the next set of tags, use it in the subsequent request. 

      

    
    :type MaxResults: integer
    :param MaxResults: 

      Maximum number of tags to return.

      

    
    
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
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Tags** *(list) --* 

          An array of ``Tag`` objects, each with a tag key and a value.

          
          

          - *(dict) --* 

            Describes a tag. 

            
            

            - **Key** *(string) --* 

              The tag key.

              
            

            - **Value** *(string) --* 

              The tag value.

              
        
      
        

        - **NextToken** *(string) --* 

          If response is truncated, Amazon SageMaker includes a token in the response. You can use this token in your subsequent request to fetch next set of tokens. 

          
    

  .. py:method:: list_training_jobs(**kwargs)

    

    Lists training jobs.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListTrainingJobs>`_    


    **Request Syntax** 
    ::

      response = client.list_training_jobs(
          NextToken='string',
          MaxResults=123,
          CreationTimeAfter=datetime(2015, 1, 1),
          CreationTimeBefore=datetime(2015, 1, 1),
          LastModifiedTimeAfter=datetime(2015, 1, 1),
          LastModifiedTimeBefore=datetime(2015, 1, 1),
          NameContains='string',
          StatusEquals='InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped',
          SortBy='Name'|'CreationTime'|'Status',
          SortOrder='Ascending'|'Descending'
      )
    :type NextToken: string
    :param NextToken: 

      If the result of the previous ``ListTrainingJobs`` request was truncated, the response includes a ``NextToken`` . To retrieve the next set of training jobs, use the token in the next request. 

      

    
    :type MaxResults: integer
    :param MaxResults: 

      The maximum number of training jobs to return in the response.

      

    
    :type CreationTimeAfter: datetime
    :param CreationTimeAfter: 

      A filter that only training jobs created after the specified time (timestamp).

      

    
    :type CreationTimeBefore: datetime
    :param CreationTimeBefore: 

      A filter that returns only training jobs created before the specified time (timestamp).

      

    
    :type LastModifiedTimeAfter: datetime
    :param LastModifiedTimeAfter: 

      A filter that returns only training jobs modified after the specified time (timestamp).

      

    
    :type LastModifiedTimeBefore: datetime
    :param LastModifiedTimeBefore: 

      A filter that returns only training jobs modified before the specified time (timestamp).

      

    
    :type NameContains: string
    :param NameContains: 

      A string in the training job name. This filter returns only models whose name contains the specified string.

      

    
    :type StatusEquals: string
    :param StatusEquals: 

      A filter that retrieves only training jobs with a specific status.

      

    
    :type SortBy: string
    :param SortBy: 

      The field to sort results by. The default is ``CreationTime`` .

      

    
    :type SortOrder: string
    :param SortOrder: 

      The sort order for results. The default is ``Ascending`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TrainingJobSummaries': [
                {
                    'TrainingJobName': 'string',
                    'TrainingJobArn': 'string',
                    'CreationTime': datetime(2015, 1, 1),
                    'TrainingEndTime': datetime(2015, 1, 1),
                    'LastModifiedTime': datetime(2015, 1, 1),
                    'TrainingJobStatus': 'InProgress'|'Completed'|'Failed'|'Stopping'|'Stopped'
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TrainingJobSummaries** *(list) --* 

          An array of ``TrainingJobSummary`` objects, each listing a training job.

          
          

          - *(dict) --* 

            Provides summary information about a training job.

            
            

            - **TrainingJobName** *(string) --* 

              The name of the training job that you want a summary for.

              
            

            - **TrainingJobArn** *(string) --* 

              The Amazon Resource Name (ARN) of the training job.

              
            

            - **CreationTime** *(datetime) --* 

              A timestamp that shows when the training job was created.

              
            

            - **TrainingEndTime** *(datetime) --* 

              A timestamp that shows when the training job ended. This field is set only if the training job has one of the terminal statuses (``Completed`` , ``Failed`` , or ``Stopped`` ). 

              
            

            - **LastModifiedTime** *(datetime) --* 

              Timestamp when the training job was last modified. 

              
            

            - **TrainingJobStatus** *(string) --* 

              The status of the training job.

              
        
      
        

        - **NextToken** *(string) --* 

          If the response is truncated, Amazon SageMaker returns this token. To retrieve the next set of training jobs, use it in the subsequent request.

          
    

  .. py:method:: start_notebook_instance(**kwargs)

    

    Launches an ML compute instance with the latest version of the libraries and attaches your ML storage volume. After configuring the notebook instance, Amazon SageMaker sets the notebook instance status to ``InService`` . A notebook instance's status must be ``InService`` (is this same as "Running" in the console?) before you can connect to your Jupyter notebook. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/StartNotebookInstance>`_    


    **Request Syntax** 
    ::

      response = client.start_notebook_instance(
          NotebookInstanceName='string'
      )
    :type NotebookInstanceName: string
    :param NotebookInstanceName: **[REQUIRED]** 

      The name of the notebook instance to start.

      

    
    
    :returns: None

  .. py:method:: stop_notebook_instance(**kwargs)

    

    Terminates the ML compute instance. Before terminating the instance, Amazon SageMaker disconnects the ML storage volume from it. Amazon SageMaker preserves the ML storage volume. 

     

    To access data on the ML storage volume for a notebook instance that has been terminated, call the ``StartNotebookInstance`` API. ``StartNotebookInstance`` launches another ML compute instance, configures it, and attaches the preserved ML storage volume so you can continue your work. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/StopNotebookInstance>`_    


    **Request Syntax** 
    ::

      response = client.stop_notebook_instance(
          NotebookInstanceName='string'
      )
    :type NotebookInstanceName: string
    :param NotebookInstanceName: **[REQUIRED]** 

      The name of the notebook instance to terminate.

      

    
    
    :returns: None

  .. py:method:: stop_training_job(**kwargs)

    

    Stops a training job. To stop a job, Amazon SageMaker sends the algorithm the ``SIGTERM`` signal, which delays job termination for 120 seconds. Algorithms might use this 120-second window to save the model artifacts, so the results of the training is not lost. 

     

    Training algorithms provided by Amazon SageMaker save the intermediate results of a model training job. This intermediate data is a valid model artifact. You can use the model artifacts that are saved when Amazon SageMaker stops a training job to create a model. 

     

    When it receives a ``StopTrainingJob`` request, Amazon SageMaker changes the status of the job to ``Stopping`` . After Amazon SageMaker stops the job, it sets the status to ``Stopped`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/StopTrainingJob>`_    


    **Request Syntax** 
    ::

      response = client.stop_training_job(
          TrainingJobName='string'
      )
    :type TrainingJobName: string
    :param TrainingJobName: **[REQUIRED]** 

      The name of the training job to stop.

      

    
    
    :returns: None

  .. py:method:: update_endpoint(**kwargs)

    

    Deploys the new ``EndpointConfig`` specified in the request, switches to using newly created endpoint, and then deletes resources provisioned for the endpoint using the previous ``EndpointConfig`` (there is no availability loss). 

     

    When Amazon SageMaker receives the request, it sets the endpoint status to ``Updating`` . After updating the endpoint, it sets the status to ``InService`` . To check the status of an endpoint, use the `DescribeEndpoint <http://docs.aws.amazon.com/sagemaker/latest/dg/API_DescribeEndpoint.html>`__ API. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/UpdateEndpoint>`_    


    **Request Syntax** 
    ::

      response = client.update_endpoint(
          EndpointName='string',
          EndpointConfigName='string'
      )
    :type EndpointName: string
    :param EndpointName: **[REQUIRED]** 

      The name of the endpoint whose configuration you want to update.

      

    
    :type EndpointConfigName: string
    :param EndpointConfigName: **[REQUIRED]** 

      The name of the new endpoint configuration.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'EndpointArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **EndpointArn** *(string) --* 

          The Amazon Resource Name (ARN) of the endpoint.

          
    

  .. py:method:: update_endpoint_weights_and_capacities(**kwargs)

    

    Updates variant weight, capacity, or both of one or more variants associated with an endpoint. This operation updates weight, capacity, or both for the previously provisioned endpoint. When it receives the request, Amazon SageMaker sets the endpoint status to ``Updating`` . After updating the endpoint, it sets the status to ``InService`` . To check the status of an endpoint, use the `DescribeEndpoint <http://docs.aws.amazon.com/sagemaker/latest/dg/API_DescribeEndpoint.html>`__ API. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/UpdateEndpointWeightsAndCapacities>`_    


    **Request Syntax** 
    ::

      response = client.update_endpoint_weights_and_capacities(
          EndpointName='string',
          DesiredWeightsAndCapacities=[
              {
                  'VariantName': 'string',
                  'DesiredWeight': ...,
                  'DesiredInstanceCount': 123
              },
          ]
      )
    :type EndpointName: string
    :param EndpointName: **[REQUIRED]** 

      The name of an existing Amazon SageMaker endpoint.

      

    
    :type DesiredWeightsAndCapacities: list
    :param DesiredWeightsAndCapacities: **[REQUIRED]** 

      An object that provides new capacity and weight values for a variant.

      

    
      - *(dict) --* 

        Specifies weight and capacity values for a production variant.

        

      
        - **VariantName** *(string) --* **[REQUIRED]** 

          The name of the variant to update.

          

        
        - **DesiredWeight** *(float) --* 

          The variant's weight.

          

        
        - **DesiredInstanceCount** *(integer) --* 

          The variant's capacity.

          

        
      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'EndpointArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **EndpointArn** *(string) --* 

          The Amazon Resource Name (ARN) of the updated endpoint.

          
    

  .. py:method:: update_notebook_instance(**kwargs)

    

    Updates a notebook instance. NotebookInstance updates include upgrading or downgrading the ML compute instance used for your notebook instance to accommodate changes in your workload requirements. You can also update the VPC security groups.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/UpdateNotebookInstance>`_    


    **Request Syntax** 
    ::

      response = client.update_notebook_instance(
          NotebookInstanceName='string',
          InstanceType='ml.t2.medium'|'ml.m4.xlarge'|'ml.p2.xlarge',
          RoleArn='string'
      )
    :type NotebookInstanceName: string
    :param NotebookInstanceName: **[REQUIRED]** 

      The name of the notebook instance to update.

      

    
    :type InstanceType: string
    :param InstanceType: 

      The Amazon ML compute instance type.

      

    
    :type RoleArn: string
    :param RoleArn: 

      Amazon Resource Name (ARN) of the IAM role to associate with the instance.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

==========
Paginators
==========


The available paginators are:


=======
Waiters
=======


The available waiters are:

* :py:class:`SageMaker.Waiter.EndpointDeleted`


* :py:class:`SageMaker.Waiter.EndpointInService`


* :py:class:`SageMaker.Waiter.NotebookInstanceDeleted`


* :py:class:`SageMaker.Waiter.NotebookInstanceInService`


* :py:class:`SageMaker.Waiter.NotebookInstanceStopped`


* :py:class:`SageMaker.Waiter.TrainingJobCompletedOrStopped`



.. py:class:: SageMaker.Waiter.EndpointDeleted

  ::

    
    waiter = client.get_waiter('endpoint_deleted')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`SageMaker.Client.describe_endpoint` every 30 seconds until a successful state is reached. An error is returned after 60 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeEndpoint>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          EndpointName='string',
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type EndpointName: string
    :param EndpointName: **[REQUIRED]** 

      The name of the endpoint.

      

    
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 30

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 60

        

      
    
    
    :returns: None

.. py:class:: SageMaker.Waiter.EndpointInService

  ::

    
    waiter = client.get_waiter('endpoint_in_service')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`SageMaker.Client.describe_endpoint` every 30 seconds until a successful state is reached. An error is returned after 120 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeEndpoint>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          EndpointName='string',
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type EndpointName: string
    :param EndpointName: **[REQUIRED]** 

      The name of the endpoint.

      

    
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 30

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 120

        

      
    
    
    :returns: None

.. py:class:: SageMaker.Waiter.NotebookInstanceDeleted

  ::

    
    waiter = client.get_waiter('notebook_instance_deleted')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`SageMaker.Client.describe_notebook_instance` every 30 seconds until a successful state is reached. An error is returned after 60 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeNotebookInstance>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          NotebookInstanceName='string',
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type NotebookInstanceName: string
    :param NotebookInstanceName: **[REQUIRED]** 

      The name of the notebook instance that you want information about.

      

    
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 30

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 60

        

      
    
    
    :returns: None

.. py:class:: SageMaker.Waiter.NotebookInstanceInService

  ::

    
    waiter = client.get_waiter('notebook_instance_in_service')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`SageMaker.Client.describe_notebook_instance` every 30 seconds until a successful state is reached. An error is returned after 60 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeNotebookInstance>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          NotebookInstanceName='string',
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type NotebookInstanceName: string
    :param NotebookInstanceName: **[REQUIRED]** 

      The name of the notebook instance that you want information about.

      

    
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 30

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 60

        

      
    
    
    :returns: None

.. py:class:: SageMaker.Waiter.NotebookInstanceStopped

  ::

    
    waiter = client.get_waiter('notebook_instance_stopped')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`SageMaker.Client.describe_notebook_instance` every 30 seconds until a successful state is reached. An error is returned after 60 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeNotebookInstance>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          NotebookInstanceName='string',
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type NotebookInstanceName: string
    :param NotebookInstanceName: **[REQUIRED]** 

      The name of the notebook instance that you want information about.

      

    
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 30

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 60

        

      
    
    
    :returns: None

.. py:class:: SageMaker.Waiter.TrainingJobCompletedOrStopped

  ::

    
    waiter = client.get_waiter('training_job_completed_or_stopped')

  
  

  .. py:method:: wait(**kwargs)

    Polls :py:meth:`SageMaker.Client.describe_training_job` every 120 seconds until a successful state is reached. An error is returned after 180 failed checks.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/DescribeTrainingJob>`_    


    **Request Syntax** 
    ::

      waiter.wait(
          TrainingJobName='string',
          WaiterConfig={
              'Delay': 123,
              'MaxAttempts': 123
          }
      )
    :type TrainingJobName: string
    :param TrainingJobName: **[REQUIRED]** 

      The name of the training job.

      

    
    :type WaiterConfig: dict
    :param WaiterConfig: 

      A dictionary that provides parameters to control waiting behavior.

      

    
      - **Delay** *(integer) --* 

        The amount of time in seconds to wait between attempts. Default: 120

        

      
      - **MaxAttempts** *(integer) --* 

        The maximum number of attempts to be made. Default: 180

        

      
    
    
    :returns: None