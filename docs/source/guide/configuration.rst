.. _guide_configuration:

Credentials
===========

Boto can be configured in multiple ways. Regardless of the source or sources
that you choose, you **must** have AWS credentials and a region set in
order to make requests.


Interactive Configuration
-------------------------

If you have the `AWS CLI <http://aws.amazon.com/cli/>`_, then you can use
its interactive ``configure`` command to set up your credentials and
default region::

    aws configure

Follow the prompts and it will generate configuration files in the
correct locations for you.

Configuring Credentials
-----------------------

There are two types of configuration data in boto3: credentials and
non-credentials.  Credentials include items such as ``aws_access_key_id``,
``aws_secret_access_key``, and ``aws_session_token``.  Non-credential
configuration includes items such as which ``region`` to use or which
addressing style to use for Amazon S3.  The distinction between
credentials and non-credentials configuration is important because
the lookup process is slightly different.  Boto3 will look in several
additional locations when searching for credentials that do not apply
when searching for non-credential configuration.

The mechanism in which boto3 looks for credentials is to search through
a list of possible locations and stop as soon as it finds credentials.
The order in which Boto3 searches for credentials is:

#. Passing credentials as parameters in the ``boto.client()`` method
#. Passing credentials as parameters when creating a ``Session`` object
#. Environment variables
#. Shared credential file (``~/.aws/credentials``)
#. AWS config file (``~/.aws/config``)
#. Boto2 config file (``/etc/boto.cfg`` and ``~/.boto``)
#. Instance metadata service on an Amazon EC2 instance that has an
   IAM role configured.

Each of those locations is discussed in more detail below.


Method Parameters
~~~~~~~~~~~~~~~~~

The first option for providing credentials to boto3 is passing them
as paramters when creating clients or when creating a ``Session``.
For example::

    import boto3
    client = boto3.client(
        's3',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        aws_session_token=SESSION_TOKN,
    )

    # Or via the Session
    session = boto3.Session(
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        aws_session_token=SESSION_TOKN,
    )

where ``ACCESS_KEY``, ``SECRET_KEY`` and ``SESSION_TOKEN`` are variables
that contain your access key, secret key, and optional session token.
Note that the examples above do not have hard coded credentials.  We
do not recommend hard coding credentials in your source code.  For example::

    # Do not hard code credentials
    client = boto3.client(
        's3',
        # Hard coded strings as credentials, not recommended.
        aws_access_key_id='AKIAIO5FODNN7EXAMPLE',
        aws_secret_access_key='ABCDEF+c2L7yXeGvUyrPgYsDnWRRC1AYEXAMPLE'
    )

Valid uses cases for providing credentials to the ``client()`` method
and ``Session`` objects include:

* Retrieving temporary credentials using AWS STS (such as
  ``sts.get_session_token()``).
* Loading credentials from some external location, e.g the OS keychain.


Environment Variables
~~~~~~~~~~~~~~~~~~~~~

Boto3 will check these environment variables for credentials:

``AWS_ACCESS_KEY_ID``
    The access key for your AWS account.

``AWS_SECRET_ACCESS_KEY``
    The secret key for your AWS account.

``AWS_SESSION_TOKEN``
    The session key for your AWS account.  This is only needed when
    you are using temporary credentials.  The ``AWS_SECURITY_TOKEN``
    environment variable can also be used, but is only supported
    for backwards compatibility purposes.  ``AWS_SESSION_TOKEN`` is
    supported by multiple AWS SDKs besides python.


Shared Credentials File
~~~~~~~~~~~~~~~~~~~~~~~

The shared credentials file has a default location of
``~/.aws/credentials``.  You can change the location of the shared
credentials file by setting the ``AWS_SHARED_CREDENTIALS_FILE``
environment variable.

This file is an INI formatted file with section names
corresponding to profiles.  With each section, the three configuration
variables shown above can be specified: ``aws_access_key_id``,
``aws_secret_access_key``, ``aws_session_token``.  **These are the only
supported values in the shared credential file.**

Below is an minimal example of the shared credentials file::

    [default]
    aws_access_key_id=foo
    aws_secret_access_key=bar
    aws_session_token=baz

The shared credentials file also supports the concept of ``profiles``.
Profiles represent logical groups of configuration.  The shared
credential file can have multiple profiles defined::

    [default]
    aws_access_key_id=foo
    aws_secret_access_key=bar

    [dev]
    aws_access_key_id=foo2
    aws_secret_access_key=bar2

    [prod]
    aws_access_key_id=foo3
    aws_secret_access_key=bar3

You can then specify a profile name via the ``AWS_PROFILE`` environment
variable or the ``profile_name`` argument when creating a Session::

    session = boto3.Session(profile_name='dev')
    # Any clients created from this session will use credentials
    # from the [dev] section of ~/.aws/credentials.
    dev_s3_client = session.client('s3')


AWS Config File
~~~~~~~~~~~~~~~

Boto3 can also load credentials from ``~/.aws/config``.  You can change
this default location by setting the ``AWS_CONFIG_FILE`` environment variable.
The config file is an INI format, with the same keys supported by the
shared credentials file.  The only difference is that profile sections
**must** have the format of ``[profile profile-name]``, except for
the default profile.  For example::

    # Example ~/.aws/config file.
    [default]
    aws_access_key_id=foo
    aws_secret_access_key=bar

    [profile dev]
    aws_access_key_id=foo2
    aws_secret_access_key=bar2

    [profile prod]
    aws_access_key_id=foo3
    aws_secret_access_key=bar3

The reason that section names must start with ``profile`` in the
``~/.aws/config`` file is because there are other sections in this file
that are permitted that aren't profile configurations.

Boto2 Config
~~~~~~~~~~~~

Boto3 will attempt to load credentials from the Boto2 config file.
It will check ``/etc/boto.cfg`` and ``~/.boto``.  Note that
*only* the ``[Credentials]`` section of the boto config file is used.
All other configuration data in the boto config file is ignored.
Example::

    # Example ~/.boto file
    [Credentials]
    aws_access_key_id = foo
    aws_secret_access_key = bar

This credential provider is primarily for backwards compatibility purposes
with boto2.


IAM Role
~~~~~~~~

If you are running on Amazon EC2 and no credentials have been found
by any of the providers above, boto3 will try to load credentials
from the instance metadata service.  In order to take advantage of this
feature, you must have specified an IAM role to use when you launched
your EC2 instance.  For more information on how to configure IAM roles
on EC2 instances, see the `IAM Roles for Amazon EC2`_ guide.

Note that if you've launched an EC2 instance with an IAM role configured,
there's no explicit configuration you need to set in boto3 to use these
credentials.  Boto3 will automatically use IAM role credentials if it does
not find credentials in any of the other places listed above.


Best Practices for Configuring Credentials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're running on an EC2 instance, use AWS IAM roles.  See the
`IAM Roles for Amazon EC2`_ guide for more information on how to set this
up.

If you want to interoperate with multiple AWS SDKs (e.g Java, Javascript,
Ruby, PHP, .NET, AWS CLI, Go, C++), use the shared credentials file
(``~/.aws/credentials``).  By using the shared credentials file, you can use a
single file for credentials that will work in all the AWS SDKs.


Configuration
=============

In addition to credentials, you can also configure non-credential values.  In
general, boto3 follows the same approach used in credential lookup: try various
locations until a value is found.  Boto3 uses these sources for configuration:

* Explicitly passed as the ``config`` paramter when creating a client.
* Environment variables
* The ``~/.aws/config`` file.

Environment Variable Configuration
----------------------------------

``AWS_ACCESS_KEY_ID``
    The access key for your AWS account.

``AWS_SECRET_ACCESS_KEY``
    The secret key for your AWS account.

``AWS_SESSION_TOKEN``
    The session key for your AWS account.  This is only needed when
    you are using temporary credentials.  The ``AWS_SECURITY_TOKEN``
    environment variable can also be used, but is only supported
    for backwards compatibility purposes.  ``AWS_SESSION_TOKEN`` is
    supported by multiple AWS SDKs besides python.

``AWS_DEFAULT_REGION``
    The default region to use, e.g. ``us-west-2``, ``us-west-2``, etc.

``AWS_PROFILE``
    The default profile to use, if any.  If no value is specified, boto3
    will attempt to seach the shared credentials file and the config file
    for the ``default`` profile.

``AWS_CONFIG_FILE``
    The location of the config file used by boto3.  By default this
    value is ``~/.aws/config``.  You only need to set this variable if
    you want to change this location.

``AWS_SHARED_CREDENTIALS_FILE``
    The location of the shared credentials file.  By default this value
    is ``~/.aws/credentials``.  You only need to set this variable if
    you want to change this location.

``AWS_CA_BUNDLE``
    The path to a custom certificate bundle to use when establishing
    SSL/TLS connections.  Boto3 includes a bundled CA bundle it will
    use by default, but you can set this environment variable to use
    a different CA bundle.

``AWS_METADATA_SERVICE_TIMEOUT``
    The number of seconds before a connection to the instance metadata
    service should time out.  When attempting to retrieve credentials
    on an EC2 instance that has been configured with an IAM role,
    a connection to the instance metadata service will time out after
    1 second by default.  If you know you are running on an EC2 instance
    with an IAM role configured, you can increase this value if needed.

``AWS_METADATA_SERVICE_NUM_ATTEMPTS``
    When attempting to retrieve credentials on an EC2 instance that has
    been configured with an IAM role, boto3 will only make one attempt
    to retrieve credentials from the instance metadata service before
    giving up.  If you know your code will be running on an EC2 instance,
    you can increase this value to make boto3 retry multiple times
    before giving up.


Configuration File
~~~~~~~~~~~~~~~~~~

Boto3 will also search the ``~/.aws/config`` file when looking for
configuration values.  You can change the location of this file by
setting the ``AWS_CONFIG_FILE`` environment variable.

This file is an INI formatted file that contains at least one
section: ``[default]``.  You can create multiple profiles (logical
groups of configuration) by creating sections named ``[profile profile-name]``.
If your profile name has spaces, you'll need to surround this value in quotes:
``[profile "my profile name"]``.  Below are all the config variables supported
in the ``~/.aws/config`` file:

``region``
    The default region to use, e.g. ``us-west-2``, ``us-west-2``, etc.
``aws_access_key_id``
    The access key to use.
``aws_secret_access_key``
    The secret access key to use.
``aws_session_token``
    The session token to use.  This is typically only needed when using
    temporary credentials.  Note ``aws_security_token`` is supported for
    backwards compatibility.
``ca_bundle``
    The CA bundle to use.  See the docs above on ``AWS_CA_BUNDLE`` for
    more information.
``metadata_service_timeout``
    The number of seconds before timing out when retrieving data from the
    instance metadata service.  See the docs above on
    ``AWS_METADATA_SERVICE_TIMEOUT`` for more information.
``metadata_service_num_attempts``
    The number of attempts to make before giving up when retrieving data from
    the instance metadata service.  See the docs above on
    ``AWS_METADATA_SERVICE_NUM_ATTEMPTS`` for more information.

.. _IAM Roles for Amazon EC2: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html
