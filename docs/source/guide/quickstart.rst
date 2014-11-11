.. _guide_quickstart:

Quickstart
==========
Getting started with Boto 3 is easy, but requires a few steps.

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
