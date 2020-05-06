.. _guide_configuration:

Credentials
===========

Boto can be configured in multiple ways. Regardless of the source or sources
that you choose, you **must** have AWS credentials and a region set in
order to make requests.


Interactive configuration
-------------------------

If you have the `AWS CLI <http://aws.amazon.com/cli/>`_, then you can use
its interactive ``configure`` command to set up your credentials and
default region::

    aws configure

Follow the prompts and it will generate configuration files in the
correct locations for you.

Configuring credentials
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
#. Assume Role provider
#. Boto2 config file (``/etc/boto.cfg`` and ``~/.boto``)
#. Instance metadata service on an Amazon EC2 instance that has an
   IAM role configured.

Each of those locations is discussed in more detail below.


Method parameters
~~~~~~~~~~~~~~~~~

The first option for providing credentials to boto3 is passing them
as parameters when creating clients or when creating a ``Session``.
For example::

    import boto3
    client = boto3.client(
        's3',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        aws_session_token=SESSION_TOKEN,
    )

    # Or via the Session
    session = boto3.Session(
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        aws_session_token=SESSION_TOKEN,
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


Environment variables
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


Shared credentials file
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


AWS config file
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


Assume role provider
~~~~~~~~~~~~~~~~~~~~

.. note::

    This is a different set of credentials configuration than using
    IAM roles for EC2 instances, which is discussed in a section
    below.

Within the ``~/.aws/config`` file, you can also configure a profile
to indicate that boto3 should assume a role.  When you do this,
boto3 will automatically make the corresponding ``AssumeRole`` calls
to AWS STS on your behalf.  It will handle in memory caching as well as
refreshing credentials as needed.

You can specify the following configuration values for configuring an
IAM role in boto3. For more information about a particular setting, see
the section `Configuration file`_.

* ``role_arn`` - The ARN of the role you want to assume.
* ``source_profile`` - The boto3 profile that contains credentials we should
  use for the initial ``AssumeRole`` call.
* ``credential_source`` - The resource (Amazon EC2 instance profile, Amazon
  ECS container role, or environment variable) that contains the credentials to
  use for the initial ``AssumeRole`` call.
* ``external_id`` - A unique identifier that is used by third parties to assume
  a role in their customers' accounts.  This maps to the ``ExternalId``
  parameter in the ``AssumeRole`` operation.  This is an optional parameter.
* ``mfa_serial`` - The identification number of the MFA device to use when
  assuming a role.  This is an optional parameter.  Specify this value if the
  trust policy of the role being assumed includes a condition that requires MFA
  authentication. The value is either the serial number for a hardware device
  (such as GAHT12345678) or an Amazon Resource Name (ARN) for a virtual device
  (such as arn:aws:iam::123456789012:mfa/user).
* ``role_session_name`` - The name applied to this assume-role session. This
  value affects the assumed role user ARN  (such as
  arn:aws:sts::123456789012:assumed-role/role_name/role_session_name). This
  maps to the ``RoleSessionName`` parameter in the ``AssumeRole`` operation.
  This is an optional parameter.  If you do not provide this value, a
  session name will be automatically generated.
* ``duration_seconds`` - The length of time in seconds of the role session.

If MFA authentication is not enabled then you only need to specify a
``role_arn`` and a ``source_profile``.

When you specify a profile that has IAM role configuration, boto3 will make an
``AssumeRole`` call to retrieve temporary credentials.  Subsequent boto3 API
calls will use the cached temporary credentials until they expire, in which
case boto3 will automatically refresh credentials.  boto3 does not write these
temporary credentials to disk.  This means that temporary credentials from the
``AssumeRole`` calls are only cached in memory within a single ``Session``.
All clients created from that session will share the same temporary
credentials.

If you specify ``mfa_serial``, then the first time an ``AssumeRole`` call is
made, you will be prompted to enter the MFA code. **Program execution will
block until you enter the MFA code.** You'll need to keep this in mind if
you have an ``mfa_serial`` device configured, but would like to use boto3
in an automated script.

Below is an example configuration for the minimal amount of configuration
needed to configure an assume role profile::

  # In ~/.aws/credentials:
  [development]
  aws_access_key_id=foo
  aws_access_key_id=bar

  # In ~/.aws/config
  [profile crossaccount]
  role_arn=arn:aws:iam:...
  source_profile=development

See `Using IAM Roles`_ for general information on IAM roles.


Assume Role With Web Identity Provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Within the ``~/.aws/config`` file, you can also configure a profile to indicate
that boto3 should assume a role.  When you do this, boto3 will automatically
make the corresponding ``AssumeRoleWithWebIdentity`` calls to AWS STS on your
behalf.  It will handle in memory caching as well as refreshing credentials as
needed.

You can specify the following configuration values for configuring an
IAM role in boto3:


* ``role_arn`` - The ARN of the role you want to assume.
* ``web_identity_token_file`` - The path to a file which contains an OAuth 2.0
  access token or OpenID Connect ID token that is provided by the identity
  provider. The contents of this file will be loaded and passed as the
  ``WebIdentityToken`` argument to the ``AssumeRoleWithWebIdentity`` operation.
* ``role_session_name`` - The name applied to this assume-role session. This
  value affects the assumed role user ARN  (such as
  arn:aws:sts::123456789012:assumed-role/role_name/role_session_name). This
  maps to the ``RoleSessionName`` parameter in the
  ``AssumeRoleWithWebIdentity`` operation.  This is an optional parameter.  If
  you do not provide this value, a session name will be automatically
  generated.

Below is an example configuration for the minimal amount of configuration
needed to configure an assume role with web identity profile::

  # In ~/.aws/config
  [profile web-identity]
  role_arn=arn:aws:iam:...
  web_identity_token_file=/path/to/a/token

This provider can also be configured via the environment:

``AWS_ROLE_ARN``
    The ARN of the role you want to assume.

``AWS_WEB_IDENTITY_TOKEN_FILE``
    The path to the web identity token file.

``AWS_ROLE_SESSION_NAME``
    The name applied to this assume-role session.

.. note::

    These environment variables currently only apply to the assume role with
    web identity provider and do not apply to the general assume role provider
    configuration.


Boto 2 config
~~~~~~~~~~~~

Boto3 will attempt to load credentials from the Boto2 config file.
It first checks the file pointed to by ``BOTO_CONFIG`` if set, otherwise
it will check ``/etc/boto.cfg`` and ``~/.boto``.  Note that
*only* the ``[Credentials]`` section of the boto config file is used.
All other configuration data in the boto config file is ignored.
Example::

    # Example ~/.boto file
    [Credentials]
    aws_access_key_id = foo
    aws_secret_access_key = bar

This credential provider is primarily for backwards compatibility purposes
with boto2.


IAM roles
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


Best practices for configuring credentials
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

* Explicitly passed as the ``config`` parameter when creating a client.
* Environment variables
* The ``~/.aws/config`` file.

Environment variable configuration
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
    The default region to use, e.g. ``us-west-1``, ``us-west-2``, etc.

``AWS_PROFILE``
    The default profile to use, if any.  If no value is specified, boto3
    will attempt to search the shared credentials file and the config file
    for the ``default`` profile.

``AWS_CONFIG_FILE``
    The location of the config file used by boto3.  By default this
    value is ``~/.aws/config``.  You only need to set this variable if
    you want to change this location.

``AWS_SHARED_CREDENTIALS_FILE``
    The location of the shared credentials file.  By default this value
    is ``~/.aws/credentials``.  You only need to set this variable if
    you want to change this location.

``BOTO_CONFIG``
    The location of the boto2 credentials file. This is not set by default.
    You only need to set this variable if want to use credentials stored in
    boto2 format in a location other than ``/etc/boto.cfg`` or ``~/.boto``.

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

``AWS_DATA_PATH``
    A list of **additional** directories to check when loading botocore data.
    You typically do not need to set this value.  There's two built in search
    paths: ``<botocoreroot>/data/`` and ``~/.aws/models``. Setting this
    environment variable indicates additional directories to first check before
    falling back to the built in search paths.  Multiple entries should be
    separated with the ``os.pathsep`` character which is ``:`` on linux and
    ``;`` on windows.

``AWS_STS_REGIONAL_ENDPOINTS``
    Sets STS endpoint resolution logic. See the ``sts_regional_endpoints``
    configuration file section for more information on how to use this.

``AWS_MAX_ATTEMPTS``
    The total number of attempts made for a single request.  For more information,
    see the ``max_attempts`` configuration file section.

``AWS_RETRY_MODE``
    Specifies the types of retries the SDK will use.  For more information,
    see the ``retry_mode`` configuration file section.

Configuration file
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

``api_versions``
    Specifies the API version to use for a particular AWS service.

    The ``api_versions`` settings are nested configuration values that require special
    formatting in the AWS configuration file. If the values are set by the
    AWS CLI or programmatically by an SDK, the formatting is handled
    automatically. If they are set by manually editing the AWS configuration
    file, the required format is shown below. Notice the indentation of each
    value.
    ::

        [default]
        region = us-east-1
        api_versions = 
            ec2 = 2015-03-01
            cloudfront = 2015-09-17

``aws_access_key_id``
    The access key to use.
``aws_secret_access_key``
    The secret access key to use.
``aws_session_token``
    The session token to use. This is typically needed only when using
    temporary credentials. Note ``aws_security_token`` is supported for
    backward compatibility.
``ca_bundle``
    The CA bundle to use. For more information, see the above description
    of the ``AWS_CA_BUNDLE`` environment variable.
``credential_process``
    Specifies an external command to run to generate or retrieve
    authentication credentials. For more information,
    see `Sourcing Credentials with an External Process`_.
``credential_source``
    To invoke an AWS service from an Amazon EC2 instance, you can use
    an IAM role attached to either an EC2 instance profile or an Amazon ECS
    container. In such a scenario, use the ``credential_source`` setting to
    specify where to find the credentials.
    
    The ``credential_source`` and ``source_profile`` settings are mutually
    exclusive.
    
    The following values are supported.

        ``Ec2InstanceMetadata``
            Use the IAM role attached to the Amazon EC2 instance profile.

        ``EcsContainer``
            Use the IAM role attached to the Amazon ECS container.

        ``Environment``
            Retrieve the credentials from environment variables.

``duration_seconds``
    The length of time in seconds of the role session. The value can range
    from 900 seconds (15 minutes) to the maximum session duration setting
    for the role. The default value is 3600 seconds (one hour).
``external_id``
    Unique identifier to pass when making ``AssumeRole`` calls.
``metadata_service_timeout``
    The number of seconds before timing out when retrieving data from the
    instance metadata service.  See the docs above on
    ``AWS_METADATA_SERVICE_TIMEOUT`` for more information.
``metadata_service_num_attempts``
    The number of attempts to make before giving up when retrieving data from
    the instance metadata service.  See the docs above on
    ``AWS_METADATA_SERVICE_NUM_ATTEMPTS`` for more information.
``mfa_serial``
    Serial number of ARN of an MFA device to use when assuming a role.
``parameter_validation``
    Disable parameter validation (default is true; parameters are
    validated by default).  This is a boolean value that can have
    a value of either ``true`` or ``false``.  Whenever you make an
    API call using a client, the parameters you provide are run through
    a set of validation checks including (but not limited to): required
    parameters provided, type checking, no unknown parameters,
    minimum length checks, etc.  You generally should leave parameter
    validation enabled.
``region``
    The default region to use, e.g. ``us-west-1``, ``us-west-2``, etc. When
    specifying a region inline during client initialization, this property
    is named ``region_name``
``role_arn``
    The ARN of the role you want to assume.
``role_session_name``
    The role name to use when assuming a role.  If this value is not
    provided, a session name will be automatically generated.
``web_identity_token_file``
    The path to a file which contains an OAuth 2.0 access token or OpenID
    Connect ID token that is provided by the identity provider. The contents of
    this file will be loaded and passed as the ``WebIdentityToken`` argument to
    the ``AssumeRoleWithWebIdentity`` operation.
``s3``
    Set S3-specific configuration data. Typically, these values do not need
    to be set.
    
    The ``s3`` settings are nested configuration values that require special
    formatting in the AWS configuration file. If the values are set by the
    AWS CLI or programmatically by an SDK, the formatting is handled
    automatically. If they are set by manually editing the AWS configuration
    file, the required format is shown below. Notice the indentation of each
    value.
    ::

        [default]
        region = us-east-1
        s3 = 
            addressing_style = path
            signature_version = s3v4

    * ``addressing_style``: The S3 addressing style. When necessary, Boto
      automatically switches the addressing style to an appropriate value.
      The following values are supported.

        ``auto``
            (Default) Attempts to use ``virtual``, but falls back to ``path`` 
            if necessary.
      
        ``path``
            Bucket name is included in the URI path.

        ``virtual``
            Bucket name is included in the hostname.

    * ``payload_signing_enabled``: Specifies whether to include an SHA-256 
      checksum with Amazon Signature Version 4 payloads. Valid settings are
      ``true`` or ``false``.

      For streaming uploads (``UploadPart`` and ``PutObject``) that use HTTPS
      and include a ``content-md5`` header, this setting is disabled by default.
    * ``signature_version``: The AWS signature version to use when signing 
      requests. When necessary, Boto automatically switches the signature
      version to an appropriate value. The following values are recognized.
    
        ``s3v4``
            (Default) Signature Version 4

        ``s3``
            (Deprecated) Signature Version 2

    * ``use_accelerate_endpoint``: Specifies whether to use the S3 Accelerate
      endpoint. The bucket must be enabled to use S3 Accelerate. Valid settings
      are ``true`` or ``false``. Default: ``false``

      Either ``use_accelerate_endpoint`` or ``use_dualstack_endpoint`` can be
      enabled, but not both.
    * ``use_dualstack_endpoint``: Specifies whether to direct all Amazon S3
      requests to the dual IPv4/IPv6 endpoint for the configured region. Valid
      settings are ``true`` or ``false``. Default: ``false``

      Either ``use_accelerate_endpoint`` or ``use_dualstack_endpoint`` can be
      enabled, but not both.
``source_profile``
    The profile name that contains credentials to use for the initial
    ``AssumeRole`` call.

    The ``credential_source`` and ``source_profile`` settings are mutually
    exclusive.

``sts_regional_endpoints``
    Sets STS endpoint resolution logic. This configuration can also be set
    using the environment variable ``AWS_STS_REGIONAL_ENDPOINTS``. By default,
    this configuration option is set to ``legacy``. Valid values are:

    * ``regional``
        Uses the STS endpoint that corresponds to the configured region. For
        example if the client is configured to use ``us-west-2``, all calls
        to STS will be make to the ``sts.us-west-2.amazonaws.com`` regional
        endpoint instead of the global ``sts.amazonaws.com`` endpoint.

    * ``legacy``
        Uses the global STS endpoint, ``sts.amazonaws.com``, for the following
        configured regions:

        * ``ap-northeast-1``
        * ``ap-south-1``
        * ``ap-southeast-1``
        * ``ap-southeast-2``
        * ``aws-global``
        * ``ca-central-1``
        * ``eu-central-1``
        * ``eu-north-1``
        * ``eu-west-1``
        * ``eu-west-2``
        * ``eu-west-3``
        * ``sa-east-1``
        * ``us-east-1``
        * ``us-east-2``
        * ``us-west-1``
        * ``us-west-2``

        All other regions will use their respective regional endpoint.

``tcp_keepalive``
    Toggles the TCP Keep-Alive socket option used when creating connections.
    By default this value is ``false``; TCP Keep-Alive will not be used
    when creating connections. To enable TCP Keep-Alive set this value to
    ``true``, enabling TCP Keep-Alive with the system default configurations.

``max_attempts``
    An integer representing the maximum number attempts that will be made for
    a single request, including the initial attempt.  For example,
    setting this value to 5 will result in a request being retried up to
    4 times.  If not provided, the number of retries will default to whatever
    is modeled, which is typically 5 total attempts in the ``legacy`` retry mode,
    and 3 in the ``standard`` and ``adaptive`` retry modes.

``retry_mode``
    A string representing the type of retries boto3 will perform.  Value values are:

        * ``legacy`` - The pre-existing retry behavior.  This is default value if
          no retry mode is provided.
        * ``standard`` - A standardized set of retry rules across the AWS SDKs.
          This includes a standard set of errors that are retried as well as
          support for retry quotas, which limit the number of unsuccessful retries
          an SDK can make.  This mode will default the maximum number of attempts
          to 3 unless a ``max_attempts`` is explicitly provided.
        * ``adaptive`` - An experimental retry mode that includes all the
          functionality of ``standard`` mode along with automatic client side
          throttling.  This is a provisional mode that may change behavior
          in the future.


.. _IAM Roles for Amazon EC2: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html
.. _Using IAM Roles: http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html
.. _Sourcing Credentials with an External Process: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sourcing-external.html
