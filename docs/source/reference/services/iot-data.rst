

************
IoTDataPlane
************

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: IoTDataPlane.Client

  A low-level client representing AWS IoT Data Plane::

    
    import boto3
    
    client = boto3.client('iot-data')

  
  These are the available methods:
  
  *   :py:meth:`~IoTDataPlane.Client.can_paginate`

  
  *   :py:meth:`~IoTDataPlane.Client.delete_thing_shadow`

  
  *   :py:meth:`~IoTDataPlane.Client.generate_presigned_url`

  
  *   :py:meth:`~IoTDataPlane.Client.get_paginator`

  
  *   :py:meth:`~IoTDataPlane.Client.get_thing_shadow`

  
  *   :py:meth:`~IoTDataPlane.Client.get_waiter`

  
  *   :py:meth:`~IoTDataPlane.Client.publish`

  
  *   :py:meth:`~IoTDataPlane.Client.update_thing_shadow`

  

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


  .. py:method:: delete_thing_shadow(**kwargs)

    

    Deletes the thing shadow for the specified thing.

     

    For more information, see `DeleteThingShadow <http://docs.aws.amazon.com/iot/latest/developerguide/API_DeleteThingShadow.html>`__ in the *AWS IoT Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-data-2015-05-28/DeleteThingShadow>`_    


    **Request Syntax** 
    ::

      response = client.delete_thing_shadow(
          thingName='string'
      )
    :type thingName: string
    :param thingName: **[REQUIRED]** 

      The name of the thing.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'payload': StreamingBody()
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the DeleteThingShadow operation.

        
        

        - **payload** (:class:`.StreamingBody`) -- 

          The state information, in JSON format.

          
    

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


  .. py:method:: get_thing_shadow(**kwargs)

    

    Gets the thing shadow for the specified thing.

     

    For more information, see `GetThingShadow <http://docs.aws.amazon.com/iot/latest/developerguide/API_GetThingShadow.html>`__ in the *AWS IoT Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-data-2015-05-28/GetThingShadow>`_    


    **Request Syntax** 
    ::

      response = client.get_thing_shadow(
          thingName='string'
      )
    :type thingName: string
    :param thingName: **[REQUIRED]** 

      The name of the thing.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'payload': StreamingBody()
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the GetThingShadow operation.

        
        

        - **payload** (:class:`.StreamingBody`) -- 

          The state information, in JSON format.

          
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: publish(**kwargs)

    

    Publishes state information.

     

    For more information, see `HTTP Protocol <http://docs.aws.amazon.com/iot/latest/developerguide/protocols.html#http>`__ in the *AWS IoT Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-data-2015-05-28/Publish>`_    


    **Request Syntax** 
    ::

      response = client.publish(
          topic='string',
          qos=123,
          payload=b'bytes'|file
      )
    :type topic: string
    :param topic: **[REQUIRED]** 

      The name of the MQTT topic.

      

    
    :type qos: integer
    :param qos: 

      The Quality of Service (QoS) level.

      

    
    :type payload: bytes or seekable file-like object
    :param payload: 

      The state information, in JSON format.

      

    
    
    :returns: None

  .. py:method:: update_thing_shadow(**kwargs)

    

    Updates the thing shadow for the specified thing.

     

    For more information, see `UpdateThingShadow <http://docs.aws.amazon.com/iot/latest/developerguide/API_UpdateThingShadow.html>`__ in the *AWS IoT Developer Guide* .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/iot-data-2015-05-28/UpdateThingShadow>`_    


    **Request Syntax** 
    ::

      response = client.update_thing_shadow(
          thingName='string',
          payload=b'bytes'|file
      )
    :type thingName: string
    :param thingName: **[REQUIRED]** 

      The name of the thing.

      

    
    :type payload: bytes or seekable file-like object
    :param payload: **[REQUIRED]** 

      The state information, in JSON format.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'payload': StreamingBody()
        }
      **Response Structure** 

      

      - *(dict) --* 

        The output from the UpdateThingShadow operation.

        
        

        - **payload** (:class:`.StreamingBody`) -- 

          The state information, in JSON format.

          
    