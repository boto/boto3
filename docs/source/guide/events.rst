Extensibility Guide
===================

All of Boto3's resource and client classes are generated at runtime.
This means that you cannot directly inherit and then extend the
functionality of these classes because they do not exist until the
program actually starts running.


However it is still possible to extend the functionality of classes through
Boto3's event system.


An Introduction to the Event System
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
    def my_function(my_list, **kwargs):
        my_list.append('Called registered function')

    # Register the function to an event
    event_system.register('myevent', my_function)

    orig_list = ['Before the event']

    # Emit the event with the keyword argument my_list
    event_system.emit('myevent', my_list=orig_list)
    
    orig_list.append('After the event')

    print(orig_list)

Here is the output from running this example::

   ['Before the event', 'Called registered function', 'After the event']

Here are the takeaways from this example:

* All clients have their own event system that you can use to fire events
  and register functions. You can access the event system through the
  ``meta.events`` attribute on the client.
* All functions registered to the event system must have ``**kwargs`` in
  the function signature. This is because emitting an event can have any
  number of keyword arguments emitted along side it, and so if your
  function is called without ``**kwargs``, its signature will have to
  match every keyword argument emitted by the event.
* To register a function to an event, call the ``register`` method on the
  event system with the name of the event you want to register the
  function to and the function handle. Note that if you register the event
  after the event is emitted, the function will not be called unless the
  event is emitted again.
* To emit an event, call the event system's ``emit`` method with any
  set of keyword arguments you want to be emitted. It will then call any
  function registered to the event.

A Hierarchical Structure
------------------------

The event system also provides a hierarchy for registering events such that
you can register a function to a set of events depending on the event name
heirarchy.

An event name can have its own heirachy by specifying ``.`` in its name. For
example, take the event name ``'general.specific.more_specific'``. When
this event is emitted, the registered functions will be called in the order
from most specific to least specific registration. So in this example, the
functions will be called in the following order:

1) Functions registered to ``'general.specific.more_specific'``
2) Functions registered to ``'general.specific'``
3) Functions registered to ``'general'``

Here is a deeper example of how the event system works with respect to
its hierarchial structure::

    import boto3

    s3 = boto3.client('s3')

    # Access the event system on the S3 client
    event_system = s3.meta.events

    def my_general_function(my_list, **kwargs):
        my_list.append('Called my general function')

    def my_specific_function(my_list, **kwargs):
        my_list.append('Called my specific function')

    event_system.register('general', my_general_function)
    event_system.register('general.specific', my_specific_function)

    events_called = []
    event_system.emit('general', my_list=events_called)
    print(events_called)

    events_called = []    
    event_system.emit('general.specific', my_list=events_called)
    print(events_called)

Here is the output from running this example::

    ['Called my general function']
    ['Called my specific function', 'Called my general function']

As expected, when the event ``'general'`` was emitted, only when the
``my_general_function`` hander was called. However when the more specific event
``'general.specific'`` was emitted, the ``my_specific_function`` and
``my_general_function`` handlers were called in that order.


Wildcard Matching
-----------------

Another aspect of Boto3's event system is that it has the capability
to do wildcard matching using the ``'*'`` notation. Here is an example
of using wildcards in the event system::

    import boto3

    s3 = boto3.client('s3')

    # Access the event system on the S3 client
    event_system = s3.meta.events

    def my_general_function(my_list, **kwargs):
        my_list.append('Called my general function')

    def my_wildcard_function(my_list, **kwargs):
        my_list.append('Called my wildcard function')

    event_system.register('general', my_general_function)
    event_system.register('general.*', my_wildcard_function)

    events_called = []
    event_system.emit('general', my_list=events_called)
    print(events_called)

    events_called = []    
    event_system.emit('general.specific', my_list=events_called)
    print(events_called)

    events_called = []    
    event_system.emit('general.other_specific', my_list=events_called)
    print(events_called)

Here is the output from running this example::

    ['Called my general function']
    ['Called my wildcard function', 'Called my general function']
    ['Called my wildcard function', 'Called my general function']

The ``'*'`` allows you to register to a group of events without having to
know the actual name of the event. This is useful when you have to apply
the same handler in multiple places. Also note that if the wildcard is used,
it must be isolated. It does not handling globbing with additional characters.
So in the previous example, if the ``my_wildcard_function`` was registered
to ``'general.*specific'``, the handler would not be called because it will
consider ``'general.*specific'`` to be a specific event.

The wildcard also respects the hierarchical structure of the event system.
So as shown in the previous example, the ``my_wildcard_function`` handler
was called first because it is registered to a more specific event than the
``my_function`` handler.


Isolation of Event Emitter
--------------------------

The event system in Boto3 has the notion of isolation: registering of handlers
and emitting of events for one event emitter should not affect another
event emitter.

In the previous sections, we registered and emitted events from the
``client.meta.events`` attribute. The ``events`` references the client's
event emitter. An event emitters is the event system for a client and is
created upon instantiation of the client. Also, note that one client's event
emitter is isolated from another client's event emitter. For example::

    import boto3

    client1 = boto3.client('s3')
    client2 = boto3.client('s3')

    def my_first_function(my_list, **kwargs):
        my_list.append('Called my first function')

    def my_second_function(my_list, **kwargs):
        my_list.append('Called my second function')

    client1.meta.events.register('event', my_first_function)
    client2.meta.events.register('event', my_second_function)

    events_called = []
    client1.meta.events.emit('event', my_list=events_called)
    print(events_called)

    events_called = []
    client2.meta.events.emit('event', my_list=events_called)
    print(events_called)

Here is the output for the code sample::

    ['Called my first function']
    ['Called my second function']

As shown in the code sample, when a client emits an event with its event
emitter, it only called handlers registered to that event and event emitter.

When clients are created, their event emitters are created by copying the
event emitter from the session that created the client. Note the session's
event emitter is accessed by its ``events`` attribute. So client event
emitters will actually inherit the session's registered handlers when the
client is instantiated. However after instantiation of the client, the
session's and client's event emitters are seperate. Here is a code sample
that illustrates this::

    import boto3
    from boto3.session import Session


    def my_session_function(my_list, **kwargs):
        my_list.append('Called my session function')

    def my_other_session_function(my_list, **kwargs):
        my_list.append('Called my other session function')

    def my_client_function(my_list, **kwargs):
        my_list.append('Called my client function')

    session = Session()
    session.events.register('event', my_session_function)

    client = session.client('s3')
    # Register a new handler to the client.
    client.meta.events.register('event', my_client_function)

    # Register a new handler after instantiation of the client.
    session.events.register('event', my_other_session_function)

    events_called = []
    client.meta.events.emit('event', my_list=events_called)
    print(events_called)

    events_called = []
    session.events.emit('event', my_list=events_called)
    print(events_called)


Here is the output for this code sample::

  ['Called my session function', 'Called my client function']
  ['Called my session function', 'Called my other session function']


As expected, the client inherited the ``my_session_function`` registration
because it was registered to the session prior to instantiation of the
client. However, upon instantiation of the client, the event emitters of both
the session and the client are isolated. The ``my_client_function`` was only
registered to the client's event emitter so it was only called when the
client emitted ``'event'``. Likewise, the ``my_other_session_function`` was
registered after the creation of the client so it was only called when the
session emitted ``'event'``.


Boto3 Specific Events
---------------------

In the examples from the previous sections, they relied on creating and
emitting your own event, which is a completely valid thing to do. However
you probably will want to hook into internal processes of boto3 to alter
functionality. Boto3 emits a set of events that users can register to
customize clients or resources and modify the behavior of method calls.

Here is the list of events that users of boto3 can register handlers to:

* ``'creating-client-class``
* ``'creating-resource-class``


creating-client-class
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


creating-resource-class
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
