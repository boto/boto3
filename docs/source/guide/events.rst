Extensibility guide
===================

All of Boto3's resource and client classes are generated at runtime.
This means that you cannot directly inherit and then extend the
functionality of these classes because they do not exist until the
program actually starts running.


However it is still possible to extend the functionality of classes through
Boto3's event system.


An introduction to the event system
-----------------------------------

Boto3's event system allows users to register a function to a specific event.
Then once the running program reaches a line that emits that specific event,
Boto3 will call every function registered to the event in the order in which
they were registered.

When Boto3 calls each of these registered functions, it will call each of them
with a specific set of keyword arguments that are associated with that event.
Then once the registered function is called, the function may modify the
keyword arguments passed to that function or return a value. Here is an
example of how the event system works::

    import boto3

    s3 = boto3.client('s3')

    # Access the event system on the S3 client
    event_system = s3.meta.events

    # Create a function 
    def add_my_bucket(params, **kwargs):
        # Add the name of the bucket you want to default to.
        if 'Bucket' not in params:
            params['Bucket'] = 'amzn-s3-demo-bucket'

    # Register the function to an event
    event_system.register('provide-client-params.s3.ListObjectsV2', add_my_bucket)

    response = s3.list_objects_v2()

In this example, the handler ``add_my_bucket`` is registered such that the
handler will inject the value ``'amzn-s3-demo-bucket'`` for the ``Bucket``
parameter whenever the ``list_objects_v2`` client call is made without the
``Bucket`` parameter. Note that if the same ``list_objects_v2`` call is made
without the ``Bucket`` parameter and the registered handler, it will result in
a validation error.

Here are the takeaways from this example:

* All clients have their own event system that you can use to fire events
  and register functions. You can access the event system through the
  ``meta.events`` attribute on the client.
* All functions registered to the event system must have ``**kwargs`` in
  the function signature. This is because emitting an event can have any
  number of keyword arguments emitted alongside it, and so if your
  function is called without ``**kwargs``, its signature will have to
  match every keyword argument emitted by the event. This also allows for
  more keyword arguments to be added to the emitted event in the future
  without breaking existing handlers.
* To register a function to an event, call the ``register`` method on the
  event system with the name of the event you want to register the
  function to and the function handle. Note that if you register the event
  after the event is emitted, the function will not be called unless the
  event is emitted again. In the example, the ``add_my_bucket`` handler
  was registered to the ``'provide-client-params.s3.ListObjectsV2'`` event,
  which is an event that can be used to inject and modify parameters passed
  in by the client method. To read more about the event refer to
  `provide-client-params`_


A hierarchical structure
------------------------

The event system also provides a hierarchy for registering events such that
you can register a function to a set of events depending on the event name
hierarchy.

An event name can have its own hierarchy by specifying ``.`` in its name. For
example, take the event name ``'general.specific.more_specific'``. When
this event is emitted, the registered functions will be called in the order
from most specific to least specific registration. So in this example, the
functions will be called in the following order:

1) Functions registered to ``'general.specific.more_specific'``
2) Functions registered to ``'general.specific'``
3) Functions registered to ``'general'``

Here is a deeper example of how the event system works with respect to
its hierarchical structure::

    import boto3

    s3 = boto3.client('s3')

    # Access the event system on the S3 client
    event_system = s3.meta.events

    def add_my_general_bucket(params, **kwargs):
        if 'Bucket' not in params:
            params['Bucket'] = 'amzn-s3-demo-bucket1'

    def add_my_specific_bucket(params, **kwargs):
        if 'Bucket' not in params:
            params['Bucket'] = 'amzn-s3-demo-bucket2'

    event_system.register('provide-client-params.s3', add_my_general_bucket)
    event_system.register('provide-client-params.s3.ListObjectsV2', add_my_specific_bucket)

    list_obj_response = s3.list_objects_v2()
    put_obj_response = s3.put_object(Key='mykey', Body=b'my body')

In this example, the ``list_objects_v2`` method call will use the
``'amzn-s3-demo-bucket2'`` for the bucket instead of
``'amzn-s3-demo-bucket1'`` because the ``add_my_specific_bucket`` method was
registered to the ``'provide-client-params.s3.ListObjectsV2'`` event which is
more specific than the ``'provide-client-params.s3'`` event. Thus, the
``add_my_specific_bucket`` function is called before the
``add_my_general_bucket`` function is called when the event is emitted.

However for the ``put_object`` call, the bucket used is
``'amzn-s3-demo-bucket1'``. This is because the event emitted for the
``put_object`` client call is ``'provide-client-params.s3.PutObject'`` and the
``add_my_general_bucket`` method is called via its registration to
``'provide-client-params.s3'``. The
``'provide-client-params.s3.ListObjectsV2'`` event is never emitted so the
registered ``add_my_specific_bucket`` function is never called.


Wildcard matching
-----------------

Another aspect of Boto3's event system is that it has the capability
to do wildcard matching using the ``'*'`` notation. Here is an example
of using wildcards in the event system::

    import boto3

    s3 = boto3.client('s3')

    # Access the event system on the S3 client
    event_system = s3.meta.events

    def add_my_wildcard_bucket(params, **kwargs):
        if 'Bucket' not in params:
            params['Bucket'] = 'amzn-s3-demo-bucket'

    event_system.register('provide-client-params.s3.*', add_my_wildcard_bucket)
    response = s3.list_objects_v2()


The ``'*'`` allows you to register to a group of events without having to
know the actual name of the event. This is useful when you have to apply
the same handler in multiple places. Also note that if the wildcard is used,
it must be isolated. It does not handle globbing with additional characters.
So in the previous example, if the ``my_wildcard_function`` was registered
to ``'provide-client-params.s3.*objects'``, the handler would not be
called because it will consider ``'provide-client-params.s3.*objects'`` to be
a specific event.

The wildcard also respects the hierarchical structure of the event system.
If another handler was registered to the ``'provide-client-params.s3'`` event,
the ``add_my_wildcard_bucket`` would be called first because it is registered
to ``'provide-client-params.s3.*'`` which is more specific than the event
``'provide-client.s3'``.


Isolation of event systems
--------------------------

The event system in Boto3 has the notion of isolation:
all clients maintain their own set of registered handlers. For example if a
handler is registered to one client's event system, it will not be registered
to another client's event system::

    import boto3

    client1 = boto3.client('s3')
    client2 = boto3.client('s3')

    def add_my_bucket(params, **kwargs):
        if 'Bucket' not in params:
            params['Bucket'] = 'amzn-s3-demo-bucket1'

    def add_my_other_bucket(params, **kwargs):
        if 'Bucket' not in params:
            params['Bucket'] = 'amzn-s3-demo-bucket2'

    client1.meta.events.register(
        'provide-client-params.s3.ListObjectsV2', add_my_bucket)
    client2.meta.events.register(
        'provide-client-params.s3.ListObjectsV2', add_my_other_bucket)

    client1_response = client1.list_objects_v2()
    client2_response = client2.list_objects_v2()


Thanks to the isolation of clients' event systems, ``client1`` will inject
``'amzn-s3-demo-bucket1'`` for its ``list_objects_v2`` method call while
``client2`` will inject ``'amzn-s3-demo-bucket2'`` for its ``list_objects_v2``
method call because ``add_my_bucket`` was registered to ``client1`` while
``add_my_other_bucket`` was registered to ``client2``.


Boto3 specific events
---------------------

Boto3 emits a set of events that users can register to
customize clients or resources and modify the behavior of method calls.

Here is a table of events that users of Boto3 can register handlers to. More
information about each event can be found in the corresponding sections below:

.. note::

  Events with a ``*`` in their order number are conditionally emitted while
  all others are always emitted. An explanation of all 3 conditional events is
  provided below.

  ``2 *`` - ``creating-resource-class`` is emitted ONLY when using a service resource.

  ``8 *`` - ``after-call`` is emitted once the API response is received.

  ``9 *`` - ``after-call-error`` is emitted when an unsuccessful API response is received.

+-----------------------------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Event Name                  | Order | Emit Location                                                                                                                                            |
+=============================+=======+==========================================================================================================================================================+
| ``creating-client-class``   | 1     | `Location <https://github.com/search?q=repo%3Aboto%2Fbotocore+creating-client-class+path%3A%2F%5Ebotocore%5C%2Fclient%5C.py%2F&type=code>`__             |
+-----------------------------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``creating-resource-class`` | 2 *   | `Location <https://github.com/search?q=repo%3Aboto%2Fboto3+creating-resource-class+path%3A%2F%5Eboto3%5C%2Fresources%5C%2Ffactory%5C.py%2F&type=code>`__ |
+-----------------------------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``provide-client-params``   | 3     | `Location <https://github.com/search?q=repo%3Aboto%2Fbotocore+provide-client-params+path%3A%2F%5Ebotocore%5C%2Fclient%5C.py%2F&type=code>`__             |
+-----------------------------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``before-call``             | 4     | `Location <https://github.com/search?q=repo%3Aboto%2Fbotocore+before-call+path%3A%2F%5Ebotocore%5C%2Fclient%5C.py%2F&type=code>`__                       |
+-----------------------------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``request-created``         | 5     | `Location <https://github.com/search?q=repo%3Aboto%2Fbotocore+request-created+path%3A%2F%5Ebotocore%5C%2Fendpoint%5C.py%2F&type=code>`__                 |
+-----------------------------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``before-send``             | 6     | `Location <https://github.com/search?q=repo%3Aboto%2Fbotocore+before-send+path%3A%2F%5Ebotocore%5C%2Fendpoint%5C.py%2F&type=code>`__                     |
+-----------------------------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``needs-retry``             | 7     | `Location <https://github.com/search?q=repo%3Aboto%2Fbotocore+needs-retry+path%3A%2F%5Ebotocore%5C%2Fendpoint%5C.py%2F&type=code>`__                     |
+-----------------------------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``after-call``              | 8 *   | `Location <https://github.com/search?q=repo%3Aboto%2Fbotocore+after-call.+path%3A%2F%5Ebotocore%5C%2Fclient%5C.py%2F&type=code>`__                       |
+-----------------------------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``after-call-error``        | 9 *   | `Location <https://github.com/search?q=repo%3Aboto%2Fbotocore+after-call-error+path%3A%2F%5Ebotocore%5C%2Fclient%5C.py%2F&type=code>`__                  |
+-----------------------------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::
  If any of the following keywords are included in an event's full name, you'll need
  to replace it with the corresponding value:

  * ``service-name`` - The value used to instantiate a client as in ``boto3.client('service-name')``.
  * ``operation-name`` - The underlying API operation name of the corresponding client method. To access
    the operation API name, retrieve the value from the ``client.meta.method_to_api_mapping`` dictionary 
    using the name of the desired client method as the key.
  * ``resource-name`` - The name of the resource class such as ``ServiceResource``.
  


`creating-client-class`
~~~~~~~~~~~~~~~~~~~~~~~

:Full Event Name:
  ``'creating-client-class.service-name'``

:Description:
  This event is emitted upon creation of the client class for a service. The
  client class for a service is not created until the first instantiation of
  the client class. Use this event for adding methods to the client class
  or adding classes for the client class to inherit from.

:Keyword Arguments Emitted:

  :type class_attributes: ``dict``
  :param class_attributes: A dictionary where the keys are the names of the
    attributes of the class and the values are the actual attributes of
    the class.

  :type base_classes: ``list``
  :param base_classes: A list of classes that the client class will inherit
    from where the order of inheritance is the same as the order of the list.

:Expected Return Value: ``None``

:Example:
  Here is an example of how to add a method to the client class::

    from boto3.session import Session
    
    def custom_method(self):
        print('This is my custom method')

    def add_custom_method(class_attributes, **kwargs):
        class_attributes['my_method'] = custom_method

    session = Session()
    session.events.register('creating-client-class.s3', add_custom_method)

    client = session.client('s3')
    client.my_method()

  This should output::

    This is my custom method
    

  Here is an example of how to add a new class for the client class to
  inherit from::

    from boto3.session import Session

    class MyClass(object):
        def __init__(self, *args, **kwargs):
            super(MyClass, self).__init__(*args, **kwargs)
            print('Client instantiated!')

    def add_custom_class(base_classes, **kwargs):
        base_classes.insert(0, MyClass)

    session = Session()
    session.events.register('creating-client-class.s3', add_custom_class)

    client = session.client('s3')

  This should output::

    Client instantiated!


`creating-resource-class`
~~~~~~~~~~~~~~~~~~~~~~~~~

:Full Event Name:
  ``'creating-resource-class.service-name.resource-name'``

:Description:
  This event is emitted upon creation of the resource class. The
  resource class is not created until the first instantiation of
  the resource class. Use this event for adding methods to the resource
  class or adding classes for the resource class to inherit from.

:Keyword Arguments Emitted:

  :type class_attributes: ``dict``
  :param class_attributes: A dictionary where the keys are the names of the
    attributes of the class and the values are the actual attributes of
    the class.

  :type base_classes: ``list``
  :param base_classes: A list of classes that the resource class will inherit
    from where the order of inheritance is the same as the order of the list.

:Expected Return Value: ``None``

:Example:
  Here is an example of how to add a method to a resource class::

    from boto3.session import Session
    
    def custom_method(self):
        print('This is my custom method')

    def add_custom_method(class_attributes, **kwargs):
        class_attributes['my_method'] = custom_method

    session = Session()
    session.events.register('creating-resource-class.s3.ServiceResource',
                            add_custom_method)

    resource = session.resource('s3')
    resource.my_method()

  This should output::

    This is my custom method
    

  Here is an example of how to add a new class for a resource class to
  inherit from::

    from boto3.session import Session

    class MyClass(object):
        def __init__(self, *args, **kwargs):
            super(MyClass, self).__init__(*args, **kwargs)
            print('Resource instantiated!')

    def add_custom_class(base_classes, **kwargs):
        base_classes.insert(0, MyClass)

    session = Session()
    session.events.register('creating-resource-class.s3.ServiceResource',
                            add_custom_class)

    resource = session.resource('s3')

  This should output::

    Resource instantiated!


`provide-client-params`
~~~~~~~~~~~~~~~~~~~~~~~

:Full Event Name:
  ``'provide-client-params.service-name.operation-name'``

:Description:
  This event is emitted before operation parameters are validated and built 
  into the HTTP request that will be sent over the wire. Use this event to 
  inject or modify parameters.

:Keyword Arguments Emitted:

  :type params: ``dict``
  :param params: A dictionary containing key value pairs consisting of the parameters 
    passed through to the client method.

  :type model: ``botocore.model.OperationModel``
  :param model: A model representing the underlying API operation of the
    client method.

:Expected Return Value: ``None`` or return a ``dict`` containing
  parameters to use when making the request.

:Example:
  Here is an example of how to inject a parameter using the event::

    import boto3

    s3 = boto3.client('s3')

    # Access the event system on the S3 client
    event_system = s3.meta.events

    # Create a function
    def add_my_bucket(params, **kwargs):
        # Add the name of the bucket you want to default to.
        if 'Bucket' not in params:
            params['Bucket'] = 'amzn-s3-demo-bucket'

    # Register the function to an event
    event_system.register('provide-client-params.s3.ListObjectsV2', add_my_bucket)

    response = s3.list_objects_v2()


`before-call`
~~~~~~~~~~~~~

:Full Event Name:
  ``'before-call.service-name.operation-name'``

:Description:
  This event is emitted just before creating and sending the HTTP request. 
  Use this event for modifying various HTTP request components prior to the request 
  being created. A response tuple may optionally be returned to trigger a short-circuit 
  and prevent the request from being made. This is useful for testing and is how the 
  `botocore stubber <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/stubber.html>`_
  mocks responses.

:Keyword Arguments Emitted:

  :type model: ``botocore.model.OperationModel``
  :param model: A model representing the underlying API operation of the
    client method.

  :type params: ``dict``
  :param params: A dictionary containing key value pairs for various components of 
    an HTTP request such as ``url_path``, ``host_prefix``, ``query_string``, ``headers``, 
    ``body``, and ``method``.

  :type request_signer: ``botocore.signers.RequestSigner``
  :param request_signer: An object to sign requests before they are sent over
    the wire using one of the authentication mechanisms defined in ``auth.py``.

:Expected Return Value: ``None`` or a ``tuple`` that includes both the ``botocore.awsrequest.AWSResponse``
  and a ``dict`` that represents the parsed response described by the model.

:Example:
  Here is an example of how to add a custom header before making an API call::

    import boto3

    s3 = boto3.client('s3')

    # Access the event system on the S3 client
    event_system = s3.meta.events

    # Create a function that adds a custom header and prints all headers.
    def add_custom_header_before_call(model, params, request_signer, **kwargs):
        params['headers']['my-custom-header'] = 'header-info'
        headers = params['headers']
        print(f'param headers: {headers}')

    #  Register the function to an event.
    event_system.register('before-call.s3.ListBuckets', add_custom_header_before_call)

    s3.list_buckets()

  This should output::

    param headers: { ... , 'my-custom-header': 'header-info'}


`request-created`
~~~~~~~~~~~~~~~~~

:Full Event Name:
  ``'request-created.service-name.operation-name'``

:Description:
  This event is emitted just after the request is created and triggers request signing.

:Keyword Arguments Emitted:

  :type request: ``botocore.awsrequest.AWSRequest``
  :param request: An AWSRequest object which represents the request that was
    created given some params and an operation model.

  :type operation_name: ``str``
  :param operation_name: The name of the service operation model i.e. ``ListObjectsV2``.

:Expected Return Value: ``None``

:Example:
  Here is an example of how to inspect the request once it's created::

    import boto3

    s3 = boto3.client('s3')

    # Access the event system on the S3 client
    event_system = s3.meta.events

    # Create a function that prints the request information.
    def inspect_request_created(request, operation_name, **kwargs):
        print('Request Info:')
        print(f'method: {request.method}')
        print(f'url: {request.url}')
        print(f'data: {request.data}')
        print(f'params: {request.params}')
        print(f'auth_path: {request.auth_path}')
        print(f'stream_output: {request.stream_output}')
        print(f'headers: {request.headers}')
        print(f'operation_name: {operation_name}')

    # Register the function to an event
    event_system.register('request-created.s3.ListObjectsV2', inspect_request_created)

    response = s3.list_objects_v2(Bucket='amzn-s3-demo-bucket')

  This should output::

    Request Info:
    method: GET
    url: https://amzn-s3-demo-bucket.s3 ...
    data: ...
    params: { ... }
    auth_path: ...
    stream_output: ...
    headers: ...
    operation_name: ListObjectsV2


`before-send`
~~~~~~~~~~~~~

:Full Event Name:
  ``'before-send.service-name.operation-name'``

:Description:
  This event is emitted when the operation has been fully serialized, signed,
  and is ready to be sent over the wire. This event allows the finalized
  request to be inspected and allows a response to be returned that fulfills
  the request. If no response is returned botocore will fulfill the request
  as normal.

:Keyword Arguments Emitted:

  :type request: ``botocore.awsrequest.AWSPreparedRequest``
  :param request: A data class representing a finalized request to be sent over the wire.

:Expected Return Value: ``None`` or an instance of ``botocore.awsrequest.AWSResponse``.

:Example:
  Here is an example of how to register a function that allows you to inspect
  the prepared request before it's sent::

    import boto3

    s3 = boto3.client('s3')

    # Access the event system on the S3 client
    event_system = s3.meta.events

    # Create a function that inspects the prepared request.
    def inspect_request_before_send(request, **kwargs):
        print(f'request: {request}')

    # Register the function to an event
    event_system.register('before-send.s3.ListBuckets', inspect_request_before_send)

    s3.list_buckets()

  This should output::

    request: <AWSPreparedRequest ... >


`needs-retry`
~~~~~~~~~~~~~

:Full Event Name:
  ``'needs-retry.service-name.operation-name'``

:Description:
  This event is emitted before checking if the most recent request needs to be retried.
  Use this event to define custom retry behavior when the configurable  
  `retry modes <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/retries.html>`_ 
  are not sufficient.

:Keyword Arguments Emitted:

  :type response: ``tuple``
  :param response: A tuple that includes both the ``botocore.awsrequest.AWSResponse``
    and a ``dict`` that represents the parsed response described by the model.

  :type endpoint: ``botocore.endpoint.Endpoint``
  :param endpoint:  Represents an endpoint for a particular service.

  :type operation: ``botocore.model.OperationModel``
  :param operation: A model representing the underlying API operation of the
    client method.

  :type attempts: ``int``
  :param attempts: A number representing the amount of retries that have been attempted.

  :type caught_exception: ``Exception`` | ``None``
  :param caught_exception: The exception raised after making an api call. If there was no
    exception, this will be None.

  :type request_dict: ``dict``
  :param request_dict: A dictionary containing key value pairs for various components of 
    an HTTP request such as ``url_path``, ``host_prefix``, ``query_string``, ``headers``, 
    ``body``, and ``method``.

:Expected Return Value: Return ``None`` if no retry is needed, or return an ``int`` representing the 
  retry delay in seconds.

:Example:
  Here is an example of how to add custom retry behavior::

    import boto3

    s3 = boto3.client('s3')

    # Access the event system on the S3 client
    event_system = s3.meta.events

    # Create a handler that determines retry behavior.
    def needs_retry_handler(**kwargs):
        # Implement custom retry logic
        if some_condition:
            return None
        else:
            return some_delay

    # Register the function to an event
    event_system.register('needs-retry', needs_retry_handler)

    s3.list_buckets()


`after-call`
~~~~~~~~~~~~

:Full Event Name:
  ``'after-call.service-name.operation-name'``

:Description:
  This event is emitted just after the service client makes an API call. This
  event allows developers to postprocess or inspect the API response according
  to the specific requirements of their application if needed.

:Keyword Arguments Emitted:

  :type http_response: ``botocore.awsrequest.AWSResponse``
  :param http_response: A data class representing an HTTP response received from the server.

  :type parsed: ``dict``
  :param params: A parsed version of the AWSResponse in the form of
    a python dictionary.

  :type model: ``botocore.model.OperationModel``
  :param model: A model representing the underlying API operation of the
    client method.

:Expected Return Value: ``None``

:Example:
  Here is an example that inspects args emitted from the ``after-call`` event::

    import boto3

    s3 = boto3.client('s3')

    # Access the event system on the S3 client
    event_system = s3.meta.events

    # Create a function that prints the after-call event args.
    def print_after_call_args(http_response, parsed, model, **kwargs):
        print(f'http_response: {http_response}')
        print(f'parsed: {parsed}')
        print(f'model: {model.name}')

    # Register the function to an event
    event_system.register('after-call.s3.ListObjectsV2', print_after_call_args)

    s3.list_objects_v2(Bucket='amzn-s3-demo-bucket')

  This should output::

    http_response: <botocore.awsrequest.AWSResponse object at ...>
    parsed: { ... }
    model: ListObjectsV2


`after-call-error`
~~~~~~~~~~~~~~~~~~

:Full Event Name:
  ``'after-call-error.service-name.operation-name'``

:Description:
  This event is emitted upon receiving an error after making an API call.
  This event provides information about any errors encountered during the
  operation and allows listeners to take corrective actions if necessary.

:Keyword Arguments Emitted:

  :type exception: ``Exception``
  :param exception: The exception raised after making an api call.

:Expected Return Value: ``None``

:Example:
  Here is an example we use the ``before-send`` to mimic a bad response which
  triggers the ``after-call-error`` event and prints the exception::

    import boto3

    s3 = boto3.client('s3')

    # Access the event system on the S3 client
    event_system = s3.meta.events

    # Prints the detected exception.
    def print_after_call_error_args(exception, **kwargs):
        if exception is not None:
            print(f'Exception Detected: {exception}')

    # Mocks an exception raised when making an API call.
    def list_objects_v2_bad_response(**kwargs):
        raise Exception("This is a test exception.")

    event_system.register('before-send.s3.ListBuckets', list_objects_v2_bad_response)
    event_system.register('after-call-error.s3.ListBuckets', print_after_call_error_args)

    s3.list_buckets()

  This should output::

    Exception Detected: This is a test exception.
    # Stack Trace
    Exception: This is a test exception.
