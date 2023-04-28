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

Boto3's event system allows users to register a function to
a specific event. Then once the running program reaches a line that
emits that specific event, Boto3 will call every function
registered to the event in the order in which they were registered.
When Boto3 calls each of these registered functions,
it will call each of them with a specific set of
keyword arguments that are associated with that event.
Then once the registered function
is called, the function may modify the keyword arguments passed to that
function or return a value.
Here is an example of how the event system works::

    import boto3

    s3 = boto3.client('s3')

    # Access the event system on the S3 client
    event_system = s3.meta.events

    # Create a function 
    def add_my_bucket(params, **kwargs):
        # Add the name of the bucket you want to default to.
        if 'Bucket' not in params:
            params['Bucket'] = 'mybucket'

    # Register the function to an event
    event_system.register('provide-client-params.s3.ListObjectsV2', add_my_bucket)

    response = s3.list_objects_v2()

In this example, the handler ``add_my_bucket``
is registered such that the handler will inject the
value ``'mybucket`` for the ``Bucket`` parameter whenever the
``list_objects_v2`` client call is made without the ``Bucket`` parameter. Note
that if the same ``list_objects_v2`` call is made without the ``Bucket``
parameter and the registered handler, it will result in a validation error.

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
            params['Bucket'] = 'mybucket'

    def add_my_specific_bucket(params, **kwargs):
        if 'Bucket' not in params:
            params['Bucket'] = 'myspecificbucket'

    event_system.register('provide-client-params.s3', add_my_general_bucket)
    event_system.register('provide-client-params.s3.ListObjectsV2', add_my_specific_bucket)

    list_obj_response = s3.list_objects_v2()
    put_obj_response = s3.put_object(Key='mykey', Body=b'my body')

In this example, the ``list_objects_v2`` method call will use the
``'myspecificbucket'`` for the bucket instead of ``'mybucket'`` because
the ``add_my_specific_bucket`` method was registered to the
``'provide-client-params.s3.ListObjectsV2'`` event which is more specific than
the ``'provide-client-params.s3'`` event. Thus, the
``add_my_specific_bucket`` function is called before the
``add_my_general_bucket`` function is called when the event is emitted.

However for the ``put_object`` call, the bucket used is ``'mybucket'``. This
is because the event emitted for the ``put_object`` client call is
``'provide-client-params.s3.PutObject'`` and the ``add_my_general_bucket``
method is called via its registration to ``'provide-client-params.s3'``. The
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
            params['Bucket'] = 'mybucket'

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
            params['Bucket'] = 'mybucket'

    def add_my_other_bucket(params, **kwargs):
        if 'Bucket' not in params:
            params['Bucket'] = 'myotherbucket'

    client1.meta.events.register(
        'provide-client-params.s3.ListObjectsV2', add_my_bucket)
    client2.meta.events.register(
        'provide-client-params.s3.ListObjectsV2', add_my_other_bucket)

    client1_response = client1.list_objects_v2()
    client2_response = client2.list_objects_v2()


Thanks to the isolation of clients' event systems, ``client1`` will inject
``'mybucket'`` for its ``list_objects_v2`` method call while ``client2`` will
inject ``'myotherbucket'`` for its ``list_objects_v2`` method call because
``add_my_bucket`` was registered to ``client1`` while ``add_my_other_bucket``
was registered to ``client2``.


Boto3 specific events
---------------------

Boto3 emits a set of events that users can register to
customize clients or resources and modify the behavior of method calls.

Below is a table of events that users of Boto3 can register handlers to. More information
about each event can be found in the corresponding sections below:

+-----------------------------+-------+--------------------------------------------------------------------------------------------------------------------------------------+
| Event Name                  | Order | Emit Location                                                                                                                        |
+=============================+=======+======================================================================================================================================+
| ``creating-client-class``   | 1     | `Location <https://github.com/boto/botocore/blob/aa63a377c6c9a78c87f55e5c0fc6ca6643198f3b/botocore/client.py#LL194C1-L198C10>`_      |
+-----------------------------+-------+--------------------------------------------------------------------------------------------------------------------------------------+
| ``creating-resource-class`` | 2 *   | `Location <https://github.com/boto/boto3/blob/f5d2face1e314388f9dcada7fa13e2326bf54f5a/boto3/resources/factory.py#LL152C1-L157C14>`_ |
+-----------------------------+-------+--------------------------------------------------------------------------------------------------------------------------------------+
| ``provide-client-params``   | 2 *   | `Location <https://github.com/boto/botocore/blob/aa63a377c6c9a78c87f55e5c0fc6ca6643198f3b/botocore/client.py#LL1018C1-L1023C10>`_    |
+-----------------------------+-------+--------------------------------------------------------------------------------------------------------------------------------------+
| ``before-parameter-build``  | 3     | `Location <https://github.com/boto/botocore/blob/892c5bc73606ec02a6eff2522da1decff88d1c48/botocore/client.py#LL1026C1-L1031C10>`_    |
+-----------------------------+-------+--------------------------------------------------------------------------------------------------------------------------------------+
| ``before-call``             | 4     | `Location <https://github.com/boto/botocore/blob/5599853483f89d9d687c60ea071c37cd220d5569/botocore/client.py#LL929C1-L937C10>`_      |
+-----------------------------+-------+--------------------------------------------------------------------------------------------------------------------------------------+
| ``request-created``         | 5     | `Location <https://github.com/boto/botocore/blob/aa63a377c6c9a78c87f55e5c0fc6ca6643198f3b/botocore/endpoint.py#LL131C1-L138C14>`_    |
+-----------------------------+-------+--------------------------------------------------------------------------------------------------------------------------------------+
| ``before-send``             | 6     | `Location <https://github.com/boto/botocore/blob/4691c4d6ac0cc3461fb5c40dc6908222866a525d/botocore/endpoint.py#LL277C1-L278C78>`_    |
+-----------------------------+-------+--------------------------------------------------------------------------------------------------------------------------------------+
| ``needs-retry``             | 7     | `Location <https://github.com/boto/botocore/blob/4691c4d6ac0cc3461fb5c40dc6908222866a525d/botocore/endpoint.py#LL353C1-L362C10>`_    |
+-----------------------------+-------+--------------------------------------------------------------------------------------------------------------------------------------+
| ``after-call``              | 8 *   | `Location <https://github.com/boto/botocore/blob/fc30d05149c248d5e601bea37be422e97c5ad7ee/botocore/client.py#LL947C1-L955C10>`_      |
+-----------------------------+-------+--------------------------------------------------------------------------------------------------------------------------------------+
| ``after-call-error``        | 8 *   | `Location <https://github.com/boto/botocore/blob/892c5bc73606ec02a6eff2522da1decff88d1c48/botocore/client.py#LL968C1-L975C14>`_      |
+-----------------------------+-------+--------------------------------------------------------------------------------------------------------------------------------------+

.. note::

  Events with a \* in their order number are conditionally emitted while all others are always emitted.
  An explination of all 4 conditional events is provided below.

  ``2 *`` - ``creating-resource-class`` is emitted when using a service resource and
  ``provide-client-params`` is emitted when using a service client.

  ``8 *`` - ``after-call`` is emitted when a successful API response is received
  and ``after-call-error`` is emitted when an error is received.


`creating-client-class`
~~~~~~~~~~~~~~~~~~~~~

:Full Event Name:
  ``'creating-client-class.service-name'``

  .. note::

    ``service-name`` refers to the value used to instantiate a client i.e.
    ``boto3.client('service-name')``

:Description:
  This event is emitted upon creation of the client class for a service. The
  client class for a service is not created until the first instantiation of
  the client class. Use this event for adding methods to the client class
  or adding classes for the client class to inherit from.

:Keyword Arguments Emitted:

  :type class_attributes: dict
  :param class_attributes: A dictionary where the keys are the names of the
     attributes of the class and the values are the actual attributes of
     the class.

  :type base_classes: list
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
~~~~~~~~~~~~~~~~~~~~~~~

:Full Event Name:
  ``'creating-resource-class.service-name.resource-name'``

  .. note::

    ``service-name`` refers to the value used to instantiate a service
    resource i.e. ``boto3.resource('service-name')`` and ``resource-name``
    refers to the name of the resource class.


:Description:
  This event is emitted upon creation of the resource class. The
  resource class is not created until the first instantiation of
  the resource class. Use this event for adding methods to the resource
  class or adding classes for the resource class to inherit from.

:Keyword Arguments Emitted:

  :type class_attributes: dict
  :param class_attributes: A dictionary where the keys are the names of the
     attributes of the class and the values are the actual attributes of
     the class.

  :type base_classes: list
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
~~~~~~~~~~~~~~~~~~~~~

:Full Event Name:
  ``'provide-client-params.service-name.operation-name'``

  .. note::

    ``service-name`` refers to the value used to instantiate a client i.e.
    ``boto3.client('service-name')``. ``operation-name`` refers to the
    underlying API operation name of the corresponding client method. 


:Description:
  This event is emitted before validation of the parameters passed to
  client method. Use this event to inject or modify parameters prior
  to the parameters being validated and built into a request that is sent
  over the wire.

:Keyword Arguments Emitted:

  :type params: dict
  :param params: A dictionary where the keys are the names of the
    parameters passed through the client method and the values are the values
    of those parameters.

  :type model: ``botocore.model.OperationModel``
  :param model: A model representing the underlying API operation of the
    client method.

:Expected Return Value: ``None`` or return a new dictionary of
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
            params['Bucket'] = 'mybucket'

    # Register the function to an event
    event_system.register('provide-client-params.s3.ListObjectsV2', add_my_bucket)

    response = s3.list_objects_v2()


`before-parameter-build`
~~~~~~~~~~~~~~~~~~~~~

:Full Event Name:
  ``'before-parameter-build.service-name.operation-name'``

  .. note::

    ``service-name`` refers to the value used to instantiate a client i.e.
    ``boto3.client('service-name')``. ``operation-name`` refers to the
    underlying API operation name of the corresponding client method. 


:Description:
  This event is emitted before the API request parameters are built.
  Use this event to inject or modify parameters after they're validated
  and built into a request that is sent over the wire.

:Keyword Arguments Emitted:

  :type params: dict
  :param params: A dictionary where the keys are the names of the
    parameters passed through the client method and the values are the values
    of those parameters.

  :type model: ``botocore.model.OperationModel``
  :param model: A model representing the underlying API operation of the
    client method.

:Expected Return Value: ``None``

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
            params['Bucket'] = 'mybucket'

    # Register the function to an event
    event_system.register('before-parameter-build.s3.ListObjectsV2', add_my_bucket)

    response = s3.list_objects_v2()


`before-call`
~~~~~~~~~~~~~~~~~~~~~

:Full Event Name:
  ``'before-call.service-name.operation-name'``

  .. note::

    ``service-name`` refers to the value used to instantiate a client i.e.
    ``boto3.client('service-name')``. ``operation-name`` refers to the
    underlying API operation name of the corresponding client method. 



:Description:
  This event is emitted just before creating the HTTP request and allows you to
  modify request parameters prior to the request being created.

:Keyword Arguments Emitted:

  :type model: ``botocore.model.OperationModel``
  :param model: A model representing the underlying API operation of the
    client method.

  :type params: dict
  :param params: A dictionary where the keys are the names of the
    parameters passed through the client method and the values are the values
    of those parameters.

  :type request_signer: ``botocore.signers.RequestSigner``
  :param request_signer: An object to sign requests before they go out over
    the wire using one of the authentication mechanisms defined in ``auth.py``.

:Expected Return Value: ``None``

:Example:
  Here is an example of how to add an additional header before making an API call::

    from boto3.session import Session

    def add_fake_header_before_call(model, params, request_signer, **kwargs):
        params['headers']['fake-header'] = 'fake-info'
        headers = params['headers']
        print(f'param headers: {headers}')


    session = Session()
    session.events.register('before-call.s3.ListBuckets', add_fake_header_before_call)

    client = session.client('s3')
    client.list_buckets()

  This should output::

    param headers: {..., 'fake-header': 'fake-info'}


`request-created`
~~~~~~~~~~~~~~~~~~~~~

:Full Event Name:
  ``'request-created.service-name.operation-name'``

  .. note::

    ``service-name`` refers to the value used to instantiate a client i.e.
    ``boto3.client('service-name')``. ``operation-name`` refers to the
    underlying API operation name of the corresponding client method. 



:Description:
  This event is emitted just after the request is created and before seralization or
  signing is done.

:Keyword Arguments Emitted:

  :type request: ``botocore.awsrequest.AWSRequest``
  :param request: An AWSRequest object which represents the request that was
    created given some params and an operation model.

  :type operation_name: str
  :param operation_name: The name of the service operation model i.e. `ListObjectsV2`.

:Expected Return Value: ``None``

:Example:
  Here is an example of how to inspect the request once it's created::

    from boto3.session import Session

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


    session = Session()
    session.events.register('request-created.s3.ListObjectsV2', inspect_request_created)

    client = session.client('s3')
    client.list_objects_v2(Bucket='my-bucket')

  This should output::

    Request Info:
      method: GET
      url: https://my-bucket.s3...
      data: b'...'
      params: {...}
      auth_path: ...
      stream_output: ...
      headers: ...

    Operation Info:
      operation_name: ListObjectsV2


`before-send`
~~~~~~~~~~~~~~~~~~~~~

:Full Event Name:
  ``'before-send.service-name.operation-name'``

  .. note::

    ``service-name`` refers to the value used to instantiate a client i.e.
    ``boto3.client('service-name')``. ``operation-name`` refers to the
    underlying API operation name of the corresponding client method. 


:Description:
  This event is emitted when the operation has been fully serialized, signed,
  and is ready to be sent across the wire. This event allows the finalized
  request to be inspected and allows a response to be returned that fufills
  the request. If no response is returned botocore will fulfill the request
  as normal.

:Keyword Arguments Emitted:

  :type request: ``botocore.awsrequest.AWSPreparedRequest``
  :param request: An object representing the properties of an HTTP request.

:Expected Return Value: ``None`` or an instance of :class:`.AWSResponse`

:Example:
  Here is an example of how to register a function that allows you to inspect
  the prepared request before it's sent::

    from boto3.session import Session

    def inspect_request_before_send(request, **kwargs):
        print(f'request:\n{request}')


    session = Session()
    session.events.register('before-send.s3.ListBuckets', inspect_request_before_send)

    client = session.client('s3')
    client.list_buckets()

  This should output::

    request:
    <AWSPreparedRequest ... >


`needs-retry`
~~~~~~~~~~~~~~~~~~~~~~~

:Full Event Name:
  ``'needs-retry.service-name.operation-name'``

  .. note::

    ``service-name`` refers to the value used to instantiate a client i.e.
    ``boto3.client('service-name')``. ``operation-name`` refers to the
    underlying API operation name of the corresponding client method. 


:Description:
  This event is emitted before checking if the most recent request needs to be retried.
  Catching this event allows developers to customize retry behavior according to the
  specific requirements of their application, rather than relying solely on Boto3's
  default settings for retries.

:Keyword Arguments Emitted:

  :type response: tuple
  :param response: A tuple that includes both the ``botocore.awsrequest.AWSResponse``
    and a dict that represents the parsed version of the response.

  :type endpoint: ``botocore.endpoint.Endpoint``
  :param endpoint:  Represents an endpoint for a particular service in a specific
    region.

  :type operation: ``botocore.model.OperationModel``
  :param operation: A model representing the underlying API operation of the
    client method.

  :type attempts: int
  :param attempts: A number representing the amount of retries that have been attempted.

  :type caught_exception: ``Exception``
  :param caught_exception: The exception raised after making an api call. If there was no
    exception, this will be None.

  :type request_dict: dict
  :param request_dict: A dictionary containing information related to the attempted API request.

:Expected Return Value: Return ``None`` if no retry is needed, or return an ``int`` representing the retry delay.

:Example:
  Here is an example of how to add a method to a resource class::

    from boto3.session import Session

    def needs_retry_handler(**kwargs):
        # Implement custom retry logic
        if some_condition:
            return None
        else:
            return some_delay

    session = Session()
    session.events.register('needs-retry', needs_retry_handler)

    client = session.client('s3')
    client.list_buckets()


`after-call`
~~~~~~~~~~~~~~~~~~~~~

:Full Event Name:
  ``'after-call.service-name.operation-name'``

  .. note::

    ``service-name`` refers to the value used to instantiate a client i.e.
    ``boto3.client('service-name')``. ``operation-name`` refers to the
    underlying API operation name of the corresponding client method. 


:Description:
  This event is emitted just after the service client makes an API call.
  This event allows developers to post process or inspect the API response according to the
  specific requirements of their application if needed.

:Keyword Arguments Emitted:

  :type http_response: ``botocore.awsrequest.AWSResponse``
  :param http_response: A data class representing an HTTP response received from the server.

  :type parsed: dict
  :param params: A parsed version of the AWSResponse in the form of
    a python dictionary.

  :type model: ``botocore.model.OperationModel``
  :param model: A model representing the underlying API operation of the
    client method.

:Expected Return Value: ``None``

:Example:
  Here is an example that inspects args emitted from the ``after-call`` event::

    from boto3.session import Session

    def print_after_call_args(http_response, parsed, model, **kwargs):
        print(f'http_response:\n{http_response.text}')
        print(f'\nparsed:\n{parsed}')
        print(f'\nmodel:\n{model.name}')

    session = Session()
    session.events.register('after-call.s3.ListObjectsV2', print_after_call_args)

    client = session.client('s3')
    client.list_objects_v2(Bucket='my-bucket')

  This should output::

    http_response:
    ...

    parsed:
    ...

    model:
    ListObjectsV2


`after-call-error`
~~~~~~~~~~~~~~~~~~~~~

:Full Event Name:
  ``'after-call-error.service-name.operation-name'``

  .. note::

    ``service-name`` refers to the value used to instantiate a client i.e.
    ``boto3.client('service-name')``. ``operation-name`` refers to the
    underlying API operation name of the corresponding client method. 


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

    from boto3.session import Session

    def print_after_call_error_args(exception, **kwargs):
        print(f'exception: {exception}')

    def list_objects_v2_bad_response(**kwargs):
        raise Exception("This is a test exception.")

    session = Session()
    session.events.register('before-send.s3.ListBuckets', list_objects_v2_bad_response)
    session.events.register('after-call-error.s3.ListBuckets', print_after_call_error_args)

    client = session.client('s3')
    client.list_buckets()

  This should output::

    exception: This is a test exception.
    # Stack Trace
