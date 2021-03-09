.. _guide_credentials:

Credentials
============

Overview
---------

Boto3 credentials can be configured in multiple ways. Regardless of the source or sources that you choose, you *must* have both AWS credentials and an AWS Region set in order to make requests.


Interactive configuration
--------------------------

If you have the `AWS CLI <http://aws.amazon.com/cli/>`_, then you can use its interactive ``configure`` command to set up your credentials and default region:

.. code-block:: shell

    aws configure

Follow the prompts and it will generate configuration files in the correct locations for you.


Configuring credentials
------------------------

There are two types of configuration data in Boto3: credentials and non-credentials. Credentials include items such as ``aws_access_key_id``, ``aws_secret_access_key``, and ``aws_session_token``. Non-credential configuration includes items such as which region to use or which addressing style to use for Amazon S3. For more information on how to configure non-credential configurations, see the :ref:`guide_configuration` guide.

Boto3 will look in several locations when searching for credentials. The mechanism in which Boto3 looks for credentials is to search through a list of possible locations and stop as soon as it finds credentials. The order in which Boto3 searches for credentials is:

#. Passing credentials as parameters in the ``boto.client()`` method
#. Passing credentials as parameters when creating a ``Session`` object
#. Environment variables
#. Shared credential file (``~/.aws/credentials``)
#. AWS config file (``~/.aws/config``)
#. Assume Role provider
#. Boto2 config file (``/etc/boto.cfg`` and ``~/.boto``)
#. Instance metadata service on an Amazon EC2 instance that has an IAM role configured.

Each of those locations is discussed in more detail below.


Passing credentials as parameters
----------------------------------

There are valid use cases for providing credentials to the ``client()`` method and ``Session`` object, these include:

* Retrieving temporary credentials using AWS STS (such as ``sts.get_session_token()``).
* Loading credentials from some external location, e.g the OS keychain.


The first option for providing credentials to Boto3 is passing them as parameters when creating clients:

.. code-block:: python

    import boto3

    client = boto3.client(
        's3',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        aws_session_token=SESSION_TOKEN
    )


The second option for providing credentials to Boto3 is passing them as parameters when creating a ``Session`` object:

.. code-block:: python

    import boto3

    session = boto3.Session(
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        aws_session_token=SESSION_TOKEN
    )


.. warning:: 

    ``ACCESS_KEY``, ``SECRET_KEY``, and ``SESSION_TOKEN`` are variables that contain your access key, secret key, and optional session token. Note that the examples above do not have hard coded credentials. We do **not** recommend hard coding credentials in your source code. 


Environment variables
----------------------

Boto3 will check these environment variables for credentials:

* ``AWS_ACCESS_KEY_ID`` - The access key for your AWS account.
* ``AWS_SECRET_ACCESS_KEY`` - The secret key for your AWS account.
* ``AWS_SESSION_TOKEN`` - The session key for your AWS account. This is only needed when you are using temporary credentials. The ``AWS_SECURITY_TOKEN`` environment variable can also be used, but is only supported for backwards compatibility purposes. ``AWS_SESSION_TOKEN`` is supported by multiple AWS SDKs besides python.


Shared credentials file
---------------------------

The shared credentials file has a default location of ``~/.aws/credentials``. You can change the location of the shared credentials file by setting the ``AWS_SHARED_CREDENTIALS_FILE`` environment variable.

This file is an INI formatted file with section names corresponding to profiles. With each section, the three configuration variables shown above can be specified: ``aws_access_key_id``, ``aws_secret_access_key``, ``aws_session_token``. *These are the only supported values in the shared credential file.*

Below is an minimal example of the shared credentials file:

.. code-block:: ini

    [default]
    aws_access_key_id=foo
    aws_secret_access_key=bar
    aws_session_token=baz

The shared credentials file also supports the concept of profiles. Profiles represent logical groups of configuration. The shared credential file can have multiple profiles:

.. code-block:: ini

    [default]
    aws_access_key_id=foo
    aws_secret_access_key=bar

    [dev]
    aws_access_key_id=foo2
    aws_secret_access_key=bar2

    [prod]
    aws_access_key_id=foo3
    aws_secret_access_key=bar3


You can then specify a profile name via the ``AWS_PROFILE`` environment variable or the ``profile_name`` argument when creating a ``Session``. For example, we can create a Session using the “dev” profile and any clients created from this session will use the “dev” credentials:

.. code-block:: python

    import boto3

    session = boto3.Session(profile_name='dev')
    dev_s3_client = session.client('s3')



AWS config file
----------------

Boto3 can also load credentials from ``~/.aws/config``. You can change this default location by setting the ``AWS_CONFIG_FILE`` environment variable. The config file is an INI format, with the same keys supported by the shared credentials file. The only difference is that profile sections *must* have the format of ``[profile profile-name]``, except for the default profile:

.. code-block:: ini

    [default]
    aws_access_key_id=foo
    aws_secret_access_key=bar

    [profile dev]
    aws_access_key_id=foo2
    aws_secret_access_key=bar2

    [profile prod]
    aws_access_key_id=foo3
    aws_secret_access_key=bar3

The reason that section names must start with profile in the ``~/.aws/config`` file is because there are other sections in this file that are permitted that aren't profile configurations.


Assume role provider
---------------------

.. note::

    This is a different set of credentials configuration than using IAM roles for EC2 instances, which is discussed in a section below.

Within the ``~/.aws/config`` file, you can also configure a profile to indicate that Boto3 should assume a role. When you do this, Boto3 will automatically make the corresponding AssumeRole calls to AWS STS on your behalf. It will handle in-memory caching as well as refreshing credentials as needed.

You can specify the following configuration values for configuring an IAM role in Boto3. For more information about a particular setting, see the :ref:`guide_configuration` section.

* ``role_arn`` - The ARN of the role you want to assume.
* ``source_profile`` - The boto3 profile that contains credentials we should use for the initial AssumeRole call.
* ``credential_source`` - The resource (Amazon EC2 instance profile, Amazon ECS container role, or environment variable) that contains the credentials to use for the initial AssumeRole call.
* ``external_id`` - A unique identifier that is used by third parties to assume a role in their customers' accounts. This maps to the ``ExternalId`` parameter in the AssumeRole operation. This is an optional parameter.
* ``mfa_serial`` - The identification number of the MFA device to use when assuming a role. This is an optional parameter. Specify this value if the trust policy of the role being assumed includes a condition that requires MFA authentication. The value is either the serial number for a hardware device (such as GAHT12345678) or an Amazon Resource Name (ARN) for a virtual device (such as *arn:aws:iam::123456789012:mfa/user*).
* ``role_session_name`` - The name applied to this assume-role session. This value affects the assumed role user ARN (such as *arn:aws:sts::123456789012:assumed-role/role_name/role_session_name*). This maps to the RoleSessionName parameter in the AssumeRole operation. This is an optional parameter. If you do not provide this value, a session name will be automatically generated.
* ``duration_seconds`` - The length of time in seconds of the role session.

If MFA authentication is not enabled then you only need to specify a ``role_arn`` and a ``source_profile``.

When you specify a profile that has an IAM role configuration, Boto3 will make an ``AssumeRole`` call to retrieve temporary credentials. Subsequent Boto3 API calls will use the cached temporary credentials until they expire, in which case Boto3 will then automatically refresh the credentials. 

Please note that Boto3 does not write these temporary credentials to disk. This means that temporary credentials from the ``AssumeRole`` calls are only cached in-memory within a single session. All clients created from that session will share the same temporary credentials.

If you specify ``mfa_serial``, then the first time an ``AssumeRole`` call is made, you will be prompted to enter the MFA code. **Program execution will block until you enter the MFA code.** You'll need to keep this in mind if you have an ``mfa_serial`` device configured, but would like to use Boto3 in an automated script.

Below is an example configuration for the minimal amount of configuration needed to configure an assume role profile:

.. code-block:: ini

    # In ~/.aws/credentials:
    [development]
    aws_access_key_id=foo
    aws_access_key_id=bar

    # In ~/.aws/config
    [profile crossaccount]
    role_arn=arn:aws:iam:...
    source_profile=development


See Using `IAM Roles <http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html>`_ for general information on IAM roles.


Assume Role With Web Identity Provider
-----------------------------------------

Within the ``~/.aws/config`` file, you can also configure a profile to indicate that Boto3 should assume a role. When you do this, Boto3 will automatically make the corresponding ``AssumeRoleWithWebIdentity`` calls to AWS STS on your behalf. It will handle in-memory caching as well as refreshing credentials, as needed.

You can specify the following configuration values for configuring an IAM role in Boto3:

* ``role_arn`` - The ARN of the role you want to assume.
* ``web_identity_token_file`` - The path to a file which contains an OAuth 2.0 access token or OpenID Connect ID token that is provided by the identity provider. The contents of this file will be loaded and passed as the ``WebIdentityToken`` argument to the ``AssumeRoleWithWebIdentity`` operation.
* ``role_session_name`` - The name applied to this assume-role session. This value affects the assumed role user ARN (such as *arn:aws:sts::123456789012:assumed-role/role_name/role_session_name*). This maps to the ``RoleSessionName`` parameter in the ``AssumeRoleWithWebIdentity`` operation. This is an optional parameter. If you do not provide this value, a session name will be automatically generated.

Below is an example configuration for the minimal amount of configuration needed to configure an assume role with web identity profile:

.. code-block:: ini

    # In ~/.aws/config
    [profile web-identity]
    role_arn=arn:aws:iam:...
    web_identity_token_file=/path/to/a/token

This provider can also be configured via environment variables:

* ``AWS_ROLE_ARN`` - The ARN of the role you want to assume.
* ``AWS_WEB_IDENTITY_TOKEN_FILE`` - The path to the web identity token file.
* ``AWS_ROLE_SESSION_NAME`` - The name applied to this assume-role session.

.. note:: 

    These environment variables currently only apply to the assume role with web identity provider and do not apply to the general assume role provider configuration.


Boto 2 config
---------------

Boto3 will attempt to load credentials from the Boto2 config file. It first checks the file pointed to by ``BOTO_CONFIG`` if set, otherwise it will check ``/etc/boto.cfg`` and ``~/.boto``. Note that only the ``[Credentials]`` section of the boto config file is used. All other configuration data in the boto config file is ignored.

.. code-block:: ini

    # Example ~/.boto file
    [Credentials]
    aws_access_key_id = foo
    aws_secret_access_key = bar

.. note:: 
    
    This credential provider is primarily for backwards compatibility purposes with Boto2.


IAM roles
-----------

If you are running on Amazon EC2 and no credentials have been found by any of the providers above, Boto3 will try to load credentials from the instance metadata service. In order to take advantage of this feature, you must have specified an IAM role to use when you launched your EC2 instance. 

For more information on how to configure IAM roles on EC2 instances, see the `IAM Roles for Amazon EC2 <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html>`_ guide.

Note that if you've launched an EC2 instance with an IAM role configured, there's no explicit configuration you need to set in Boto3 to use these credentials. Boto3 will automatically use IAM role credentials if it does not find credentials in any of the other places listed previously.


Best practices for configuring credentials
--------------------------------------------

If you're running on an EC2 instance, use AWS IAM roles. See the `IAM Roles for Amazon EC2 <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html>`_ guide for more information on how to set this up.

If you want to interoperate with multiple AWS SDKs (e.g Java, Javascript, Ruby, PHP, .NET, AWS CLI, Go, C++), use the shared credentials file (``~/.aws/credentials``). By using the shared credentials file, you can use a single file for credentials that will work in all AWS SDKs.
