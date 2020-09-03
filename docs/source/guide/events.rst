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
    event_system.register('provide-client-params.s3.ListObjects', add_my_bucket)

    response = s3.list_objects()

In this example, the handler ``add_my_bucket``
is registered such that the handler will inject the
value ``'mybucket`` for the ``Bucket`` parameter whenever the the
``list_objects`` client call is made without the ``Bucket`` parameter. Note
that if the same ``list_objects`` call is made without the ``Bucket``
parameter and the registered handler, it will result in a validation error.

Here are the takeaways from this example:

* All clients have their own event system that you can use to fire events
  and register functions. You can access the event system through the
  ``meta.events`` attribute on the client.
* All functions registered to the event system must have ``**kwargs`` in
  the function signature. This is because emitting an event can have any
  number of keyword arguments emitted along side it, and so if your
  function is called without ``**kwargs``, its signature will have to
  match every keyword argument emitted by the event. This also allows for
  more keyword arguments to be added to the emitted event in the future
  without breaking existing handlers.
* To register a function to an event, call the ``register`` method on the
  event system with the name of the event you want to register the
  function to and the function handle. Note that if you register the event
  after the event is emitted, the function will not be called unless the
  event is emitted again. In the example, the ``add_my_bucket`` handler
  was registered to the ``'provide-client-params.s3.ListObjects'`` event,
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
    event_system.register('provide-client-params.s3.ListObjects', add_my_specific_bucket)

    list_obj_response = s3.list_objects()
    put_obj_response = s3.put_object(Key='mykey', Body=b'my body')

In this example, the ``list_objects`` method call will use the
``'myspecificbucket'`` for the bucket instead of ``'mybucket'`` because
the ``add_my_specific_bucket`` method was registered to the
``'provide-client-params.s3.ListObjects'`` event which is more specific than
the ``'provide-client-params.s3'`` event. Thus, the
``add_my_specific_bucket`` function is called before the
``add_my_general_bucket`` function is called when the event is emitted.

However for the ``put_object`` call, the bucket used is ``'mybucket'``. This
is because the event emitted for the ``put_object`` client call is
``'provide-client-params.s3.PutObject'`` and the ``add_my_general_bucket``
method is called via its registration to ``'provide-client-params.s3'``. The
``'provide-client-params.s3.ListObjects'`` event is never emitted so the
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
    response = s3.list_objects()


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
        'provide-client-params.s3.ListObjects', add_my_bucket)
    client2.meta.events.register(
        'provide-client-params.s3.ListObjects', add_my_other_bucket)

    client1_response = client1.list_objects()
    client2_response = client2.list_objects()


Thanks to the isolation of clients' event systems, ``client1`` will inject
``'mybucket'`` for its ``list_objects`` method call while ``client2`` will
inject ``'myotherbucket'`` for its ``list_objects`` method call because
``add_my_bucket`` was registered to ``client1`` while ``add_my_other_bucket``
was registered to ``client2``.


Boto3 specific events
---------------------

Boto3 emits a set of events that users can register to
customize clients or resources and modify the behavior of method calls.

Here is the list of events that users of Boto3 can register handlers to:

* ``'creating-client-class``
* ``'creating-resource-class``
* ``'provide-client-params'``


`creating-client-class`
~~~~~~~~~~~~~~~~~~~~~

:Full Event Name:
  ``'creating-client-class.service-name'``

  Note: ``service-name`` refers to the value used to instantiate a client i.e.
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

:Expected Return Value: Do not return anything.

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

  Note: ``service-name`` refers to the value used to instantiate a service
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

:Expected Return Value: Do not return anything.

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

  Note: ``service-name`` refers to the value used to instantiate a client i.e.
  ``boto3.client('service-name')``. ``operation-name`` refers to the
  underlying API operation of the corresponding client method. To access
  the operation API name, retrieve the value from the
  ``client.meta.method_to_api_mapping`` dictionary using the name of the
  desired client method as the key.

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

:Expected Return Value: Do not return anything or return a new dictionary of
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
    event_system.register('provide-client-params.s3.ListObjects', add_my_bucket)

    response = s3.list_objects()

