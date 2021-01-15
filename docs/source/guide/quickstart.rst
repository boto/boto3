.. _guide_quickstart:

Quickstart
==========
Getting started with Boto3 is easy, but requires a few steps.

Installation
------------
Prior to using Boto3, you need to install it and its dependencies.

.. _quickstart_install_python:

Install or update Python
~~~~~~~~~~~~~~~~~~~~~~~~
Before installing Boto3, ensure that you're using an up-to-date version of
Python. Unless you have specific reasons to use another version of Python, you
should be using Python 3.7 or later. Boto3 support for Python 2.7 is
deprecated and will end effective July 15, 2021. See :ref:`guide_migration_py3`
for more details, including timeline information and guidance regarding how to
transition to Python 3 if you haven't done so yet.

For more information on how to get the latest version of Python, please refer
to the official `Python documentation <https://www.python.org/downloads/>`_. 

Install Boto3
~~~~~~~~~~~~~
Install the latest Boto3 release via :command:`pip`::

    pip install boto3

You may also install a specific version::

    pip install boto3==1.0.0

.. note::

   The latest development version of Boto3 can always be found on
   `GitHub <https://github.com/boto/boto3>`_.

Configuration
-------------
Before you can begin using Boto3, you should set up authentication
credentials. Credentials for your AWS account can be found in the
`IAM Console <https://console.aws.amazon.com/iam/home>`_. You can
create or use an existing user. Go to manage access keys and
generate a new set of keys.

If you have the `AWS CLI <http://aws.amazon.com/cli/>`_
installed, then you can use it to configure your credentials file::

    aws configure

Alternatively, you can create the credential file yourself. By default,
its location is at ``~/.aws/credentials``::

    [default]
    aws_access_key_id = YOUR_ACCESS_KEY
    aws_secret_access_key = YOUR_SECRET_KEY

You may also want to set a default region. This can be done in the
configuration file. By default, its location is at ``~/.aws/config``::

    [default]
    region=us-east-1

Alternatively, you can pass a ``region_name`` when creating clients
and resources.

This sets up credentials for the default profile as well as a default
region to use when creating connections. See
:ref:`guide_configuration` for in-depth configuration sources and
options.

Using Boto3
------------
To use Boto3, you must first import it and tell it what service you are
going to use::

    import boto3

    # Let's use Amazon S3
    s3 = boto3.resource('s3')

Now that you have an ``s3`` resource, you can make requests and process
responses from the service. The following uses the ``buckets`` collection
to print out all bucket names::

    # Print out bucket names
    for bucket in s3.buckets.all():
        print(bucket.name)

It's also easy to upload and download binary data. For example, the
following uploads a new file to S3. It assumes that the bucket ``my-bucket``
already exists::

    # Upload a new file
    data = open('test.jpg', 'rb')
    s3.Bucket('my-bucket').put_object(Key='test.jpg', Body=data)

:ref:`guide_resources` and :ref:`guide_collections` will be covered in more
detail in the following sections, so don't worry if you do not completely
understand the examples.
