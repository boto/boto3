.. _guide_quickstart:

Quickstart
==========
Getting started with Boto 3 is easy, but requires a few steps.

.. important:: On January 10th, 2020, Boto 3 will no longer support 
   Python 2.6 or Python 3.3. After this date, Boto 3 will require 
   Python 2.7, Python 3.4, or a later version to successfully use 
   Boto 3. For more information, see 
   *Using Boto 3 with Python 2.6 or Python 3.3* 
   later in this topic, and the 
   `deprecation announcement in this blog post <https://aws.amazon.com/blogs/developer/deprecation-of-python-2-6-and-python-3-3-in-botocore-boto3-and-the-aws-cli/>`_.

Installation
------------
Install the latest Boto 3 release via :command:`pip`::

    pip install boto3

You may also install a specific version::

    pip install boto3==1.0.0

.. note::

   The latest development version can always be found on
   `GitHub <https://github.com/boto/boto3>`_.

Configuration
-------------
Before you can begin using Boto 3, you should set up authentication
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

Using Boto 3
------------
To use Boto 3, you must first import it and tell it what service you are
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

Using Boto 3 with Python 2.6 or Python 3.3
------------------------------------------

On January 10th, 2020, Boto 3 will no longer support Python 2.6 or 
Python 3.3. After this date, Boto 3 will require Python 2.7, Python 3.4, 
or a later version to successfully use Boto 3. For more information, 
see the 
`deprecation announcement in this blog post <https://aws.amazon.com/blogs/developer/deprecation-of-python-2-6-and-python-3-3-in-botocore-boto3-and-the-aws-cli/>`_.

Boto 3 requires an installation of Python to run. This Python 
installation can be any supported version of Python. 
Because Python 2.6 and Python 3.3 will no longer be supported and will 
no longer receive security updates, we encourage you to upgrade to 
Python 2.7, Python 3.4, or a later version.

To continue using Python 2.6 or Python 3.3 with Boto 3, you must 
"pin" to a Boto 3 version as described later in this section. 

.. important:: Using an older version of Boto 3 prevents you from 
   accessing new AWS services and features that were added to Boto 3 
   after the date your older version was initially released. 
   We recommend that whenever possible, you instead upgrade your 
   Boto 3 installation to a supported version and also use a newer 
   version of Boto 3.

You can force pip to download a Boto 3 version that is compatible 
with Python 2.6 or Python 3.3 by running a command that specifies 
``boto3==1.9.x``, where ``x`` is the specific version of Boto 3 
that you want to pin. For example, to pin to Boto 3 version 1.9.239::

    pip install --upgrade boto3==1.9.239

Boto 3 versions 1.10 and later will not support Python 2.6 or Python 3.3.

For a list of available Boto 3 version numbers, see 
`boto3 Releases <https://github.com/boto/boto3/releases>`_ on GitHub.

