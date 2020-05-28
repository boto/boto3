.. _guide_session:

Session
=======

Overview
---------

A session manages state about a particular configuration. By default, a session is created for you when needed. However, it is possible and recommended to maintain your own session in some scenarios. Sessions typically store:

* Credentials
* Region
* Other configurations related to your profile


Default session
----------------

Boto3 acts as a proxy to the default session, which is created automatically when you create a low-level client or resource client:: 

    import boto3

    # Using the default session
    sqs = boto3.client('sqs')
    s3 = boto3.resource('s3')


Custom session
---------------

It is also possible to manage your own session and create low-level clients or resource clients from it::


    import boto3
    import boto3.session

    # Create your own session
    my_session = boto3.session.Session()

    # Now we can create low-level clients or resource clients from our custom session
    sqs = my_session.client('sqs')
    s3 = my_session.resource('s3')


Session configurations
------------------------

You can configure each session with specific credentials, region information, or profiles. The most common configurations you might use are: 

* ``aws_access_key_id``: a specific AWS access key ID
* ``aws_secret_access_key``: a specific AWS secret access key
* ``region_name``: the region where you want to create new connections
* ``profile_name``: the profile you want to use when creating your session


.. note:: 
    Only set the ``profile_name`` parameter when a specific profile is required for your session. If you want to use the default profile, don’t set the ``profile_name`` parameter at all. If the ``profile_name`` parameter is not set *and* there is no default profile, an empty config dictionary will be used. 

    For a detailed list of per session configurations, please see the `Session core reference <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html>`_.


Multi-threading/multi-processing with sessions
-----------------------------------------------

Similar to ``Resource`` objects, ``Session`` objects are not thread safe and should not be shared across threads and processes. A new ``Session`` object should be created for each thread or process::


    import boto3
    import boto3.session
    import threading

    class MyTask(threading.Thread):
        def run(self):
            # Here we'll create a new session per thread
            session = boto3.session.Session()
            
            # Next, we'll create a resource client using our thread's session object
            s3 = session.resource('s3')
            
            # Put your thread-safe code here

