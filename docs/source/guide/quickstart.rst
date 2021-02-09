.. _guide_quickstart:

Quickstart
==========

This guide details the steps needed to install or update the AWS SDK for Python.

The SDK is composed of two key Python packages: Botocore (the library providing the low-level
functionality shared between the Python SDK and the AWS CLI) and Boto3 (the package implementing the
Python SDK itself).

.. note::

    Documentation and developers tend to refer to the AWS SDK for Python as "Boto3," and this
    documentation often does so as well.

Installation
------------

To use Boto3, you first need to install it and its dependencies.

.. _quickstart_install_python:

Install or update Python
~~~~~~~~~~~~~~~~~~~~~~~~

Before installing Boto3, install Python 3.6 or later; support for Python 2.7 and Python 3.5 and
earlier is deprecated. After the deprecation date listed for each Python version, new releases of
Boto3 will not include support for that version of Python. For details, including the deprecation
schedule and how to update your project to use Python 3.6, see :ref:`guide_migration_py3`.

For information about how to get the latest version of Python, see the official `Python
documentation <https://www.python.org/downloads/>`_. 

Install Boto3
~~~~~~~~~~~~~

Install the latest Boto3 release via :command:`pip`::

    pip install boto3

If your project requires a specific version of Boto3, or has compatibility concerns with
certain versions, you may provide constraints when installing::

    # Install Boto3 version 1.0 specifically
    pip install boto3==1.0.0

    # Make sure Boto3 is no older than version 1.15.0
    pip install boto3>=1.15.0

    # Avoid versions of Boto3 newer than version 1.15.3
    pip install boto3<=1.15.3

.. note::

   The latest development version of Boto3 is on `GitHub <https://github.com/boto/boto3>`_.

Configuration
-------------

Before using Boto3, you need to set up authentication credentials for your AWS account using either
the `IAM Console <https://console.aws.amazon.com/iam/home>`_ or the AWS CLI. You can either choose
an existing user or create a new one.

For instructions about how to create a user using the IAM Console, see `Creating IAM users
<https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console>`_.
Once the user has been created, see `Managing access keys
<https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey>`_
to learn how to create and retrieve the keys used to authenticate the user.

If you have the `AWS CLI <http://aws.amazon.com/cli/>`_ installed, then you can use the
:command:`aws configure` command to configure your credentials file::

    aws configure

Alternatively, you can create the credentials file yourself. By default, its location is
``~/.aws/credentials``. At a minimum, the credentials file should specify the access key and secret
access key. In this example, the key and secret key for the account are specified the ``default`` profile::

    [default]
    aws_access_key_id = YOUR_ACCESS_KEY
    aws_secret_access_key = YOUR_SECRET_KEY

You may also want to add a default region to the AWS configuration file, which is located by default
at ``~/.aws/config``::

    [default]
    region=us-east-1

Alternatively, you can pass a ``region_name`` when creating clients and resources.

You have now configured credentials for the default profile as well as a default region to use when
creating connections. See :ref:`guide_configuration` for in-depth configuration sources and options.

Using Boto3
------------

To use Boto3, you must first import it and indicate which service or services you're going to use::

    import boto3

    # Let's use Amazon S3
    s3 = boto3.resource('s3')

Now that you have an ``s3`` resource, you can make send requests to the service. The following code uses the ``buckets`` collection to print out all bucket names::

    # Print out bucket names
    for bucket in s3.buckets.all():
        print(bucket.name)

You can also upload and download binary data. For example, the following uploads a new file to S3,
assuming that the bucket ``my-bucket`` already exists::

    # Upload a new file
    data = open('test.jpg', 'rb')
    s3.Bucket('my-bucket').put_object(Key='test.jpg', Body=data)

:ref:`guide_resources` and :ref:`guide_collections` are covered in more detail in the following
sections.
