

****************
SageMakerRuntime
****************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: SageMakerRuntime.Client

  A low-level client representing Amazon SageMaker Runtime::

    
    import boto3
    
    client = boto3.client('sagemaker-runtime')

  
  These are the available methods:
  
  *   :py:meth:`~SageMakerRuntime.Client.can_paginate`

  
  *   :py:meth:`~SageMakerRuntime.Client.generate_presigned_url`

  
  *   :py:meth:`~SageMakerRuntime.Client.get_paginator`

  
  *   :py:meth:`~SageMakerRuntime.Client.get_waiter`

  
  *   :py:meth:`~SageMakerRuntime.Client.invoke_endpoint`

  

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

        


  .. py:method:: invoke_endpoint(**kwargs)

    

    After you deploy a model into production using Amazon SageMaker hosting services, your client applications use this API to get inferences from the model hosted at the specified endpoint. 

     

    For an overview of Amazon SageMaker, see `How It Works <http://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works.html>`__  

     

    Amazon SageMaker strips all POST headers except those supported by the API. Amazon SageMaker might add additional headers. You should not rely on the behavior of headers outside those enumerated in the request syntax. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/runtime.sagemaker-2017-05-13/InvokeEndpoint>`_    


    **Request Syntax** 
    ::

      response = client.invoke_endpoint(
          EndpointName='string',
          Body=b'bytes'|file,
          ContentType='string',
          Accept='string'
      )
    :type EndpointName: string
    :param EndpointName: **[REQUIRED]** 

      The name of the endpoint that you specified when you created the endpoint using the `CreateEndpoint <http://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpoint.html>`__ API. 

      

    
    :type Body: bytes or seekable file-like object
    :param Body: **[REQUIRED]** 

      Provides input data, in the format specified in the ``ContentType`` request header. Amazon SageMaker passes all of the data in the body to the model. 

      

    
    :type ContentType: string
    :param ContentType: 

      The MIME type of the input data in the request body.

      

    
    :type Accept: string
    :param Accept: 

      The desired MIME type of the inference in the response.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Body': StreamingBody(),
            'ContentType': 'string',
            'InvokedProductionVariant': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Body** (:class:`.StreamingBody`) -- 

          Includes the inference provided by the model.

          
        

        - **ContentType** *(string) --* 

          The MIME type of the inference returned in the response body.

          
        

        - **InvokedProductionVariant** *(string) --* 

          Identifies the production variant that was invoked.

          
    

==========
Paginators
==========


The available paginators are:
