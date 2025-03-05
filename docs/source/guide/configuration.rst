.. _guide_configuration:

Configuration
=============

Overview
---------
Boto3 looks at various configuration locations until it finds configuration values. Boto3 adheres to the following lookup order when searching through sources for configuration values:

* A ``Config`` object that's created and passed as the ``config`` parameter when creating a client
* Environment variables
* The ``~/.aws/config`` file

.. note::

    Configurations are not wholly atomic. This means configuration values set in your AWS config file can be singularly overwritten by setting a specific environment variable or through the use of a ``Config`` object.

For details about credential configuration, see the :ref:`guide_credentials` guide. 


Using the Config object
-----------------------
This option is for configuring client-specific configurations that affect the behavior of your specific client object only. As described earlier, there are options used here that will supersede those found in other configuration locations:

* ``region_name`` (string) - The AWS Region used in instantiating the client. If used, this takes precedence over environment variable and configuration file values. But it doesn't overwrite a ``region_name`` value *explicitly* passed to individual service methods.
* ``signature_version`` (string) - The signature version used when signing requests. Note that the default version is Signature Version 4. If you're using a presigned URL with an expiry of greater than 7 days, you should specify Signature Version 2.
* ``s3`` (related configurations; dictionary) - Amazon S3 service-specific configurations. For more information, see the `Botocore config reference <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html>`_.
* ``proxies`` (dictionary) - Each entry maps a protocol name to the proxy server Boto3 should use to communicate using that protocol. See :ref:`specify_proxies` for more information.
* ``proxies_config`` (dictionary) - Additional proxy configuration settings. For more information, see :ref:`configure_proxies`.
* ``retries`` (dictionary) - Client retry behavior configuration options that include retry mode and maximum retry attempts. For more information, see the :ref:`guide_retries` guide.  


For more information about additional options, or for a complete list of options, see the `Config reference <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html>`_.

To set these configuration options, create a ``Config`` object with the options you want, and then pass them into your client.

.. code-block:: python

    import boto3
    from botocore.config import Config

    my_config = Config(
        region_name = 'us-west-2',
        signature_version = 'v4',
        retries = {
            'max_attempts': 10,
            'mode': 'standard'
        }
    )

    client = boto3.client('kinesis', config=my_config)


Using proxies
~~~~~~~~~~~~~
With Boto3, you can use proxies as intermediaries between your code and AWS. Proxies can provide functions such as filtering, security, firewalls, and privacy assurance.

.. _specify_proxies:

Specifying proxy servers
''''''''''''''''''''''''

You can specify proxy servers to be used for connections when using specific protocols. The ``proxies`` option in the ``Config`` object is a dictionary in which each entry maps a protocol to the address and port number of the proxy server for that protocol.

In the following example, a proxy list is set up to use ``proxy.amazon.com``, port 6502 as the proxy for all HTTP requests by default. HTTPS requests use port 2010 on ``proxy.amazon.org`` instead.


.. code-block:: python

    import boto3
    from botocore.config import Config

    proxy_definitions = {
        'http': 'http://proxy.amazon.com:6502',
        'https': 'https://proxy.amazon.org:2010'
    }

    my_config = Config(
        region_name='us-east-2',
        signature_version='v4',
        proxies=proxy_definitions
    )

    client = boto3.client('kinesis', config=my_config)

Alternatively, you can use the ``HTTP_PROXY`` and ``HTTPS_PROXY`` environment variables to specify proxy servers.  Proxy servers specified using the ``proxies`` option in the ``Config`` object will override proxy servers specified using environment variables.

.. _configure_proxies:

Configuring proxies
'''''''''''''''''''
You can configure how Boto3 uses proxies by specifying the ``proxies_config`` option, which is a dictionary that specifies the values of several proxy options by name.  There are three keys in this dictionary: ``proxy_ca_bundle``, ``proxy_client_cert``, and ``proxy_use_forwarding_for_https``. For more information about these keys, see the `Botocore config reference <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>`_.

.. code-block:: python

    import boto3
    from botocore.config import Config

    proxy_definitions = {
        'http': 'http://proxy.amazon.com:6502',
        'https': 'https://proxy.amazon.org:2010'
    }

    my_config = Config(
        region_name='us-east-2',
        signature_version='v4',
        proxies=proxy_definitions,
        proxies_config={
            'proxy_client_cert': '/path/of/certificate'
        }
    )

    client = boto3.client('kinesis', config=my_config)

With the addition of the ``proxies_config`` option shown here, the proxy will use the specified certificate file for authentication when using the HTTPS proxy.

Using client context parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Some services have configuration settings that are specific to their clients. These settings are called client context parameters. Please refer to the ``Client Context Parameters`` section of a service client's documentation for a list of available parameters and information on how to use them.

.. _configure_client_context:

Configuring client context parameters
'''''''''''''''''''''''''''''''''''''
You can configure client context parameters by passing a dictionary of key-value pairs to the ``client_context_params`` parameter in your ``Config``. Invalid parameter values or parameters that are not modeled by the service will be ignored.

.. code-block:: python

    import boto3
    from botocore.config import Config

    my_config = Config(
        region_name='us-east-2',
        client_context_params={
            'my_great_context_param': 'foo'
        }
    )

    client = boto3.client('kinesis', config=my_config)

Boto3 does not support setting ``client_context_params`` per request. Differing configurations will require creation of a new client.

Using environment variables 
---------------------------
You can set configuration settings using system-wide environment variables. These configurations are global and will affect all clients created unless you override them with a ``Config`` object.

.. note::
    Only the configuration settings listed below can be set using environment variables.


``AWS_ACCESS_KEY_ID``
    The access key for your AWS account.

``AWS_SECRET_ACCESS_KEY``
    The secret key for your AWS account.

``AWS_SESSION_TOKEN``
    The session key for your AWS account. This is only needed when
    you are using temporary credentials. The ``AWS_SECURITY_TOKEN``
    environment variable can also be used, but is only supported
    for backward-compatibility purposes.  ``AWS_SESSION_TOKEN`` is
    supported by multiple AWS SDKs in addition to Boto3.

``AWS_DEFAULT_REGION``
    The default AWS Region to use, for example, ``us-west-1`` or ``us-west-2``.

``AWS_PROFILE``
    The default profile to use, if any.  If no value is specified, Boto3
    attempts to search the shared credentials file and the config file
    for the ``default`` profile.

``AWS_CONFIG_FILE``
    The location of the config file used by Boto3.  By default this
    value is ``~/.aws/config``.  You only need to set this variable if
    you want to change this location.

``AWS_SHARED_CREDENTIALS_FILE``
    The location of the shared credentials file.  By default this value
    is ``~/.aws/credentials``.  You only need to set this variable if
    you want to change this location.

``BOTO_CONFIG``
    The location of the Boto2 credentials file. This is not set by default.
    You only need to set this variable if you want to use credentials stored in
    Boto2 format in a location other than ``/etc/boto.cfg`` or ``~/.boto``.

``AWS_CA_BUNDLE``
    The path to a custom certificate bundle to use when establishing
    SSL/TLS connections.  Boto3 includes a CA bundle that it
    uses by default, but you can set this environment variable to use
    a different CA bundle.

``AWS_METADATA_SERVICE_TIMEOUT``
    The number of seconds before a connection to the instance metadata
    service should time out.  When attempting to retrieve credentials
    on an Amazon EC2 instance that is configured with an IAM role,
    a connection to the instance metadata service will time out after
    1 second by default.  If you know you're running on an EC2 instance
    with an IAM role configured, you can increase this value if needed.

``AWS_METADATA_SERVICE_NUM_ATTEMPTS``
    When attempting to retrieve credentials on an Amazon EC2 instance that has
    been configured with an IAM role, Boto3 will make only one attempt
    to retrieve credentials from the instance metadata service before
    giving up.  If you know your code will be running on an EC2 instance,
    you can increase this value to make Boto3 retry multiple times
    before giving up.

``AWS_DATA_PATH``
    A list of **additional** directories to check when loading botocore data.
    You typically don't need to set this value.  There are two built-in search
    paths: ``<botocoreroot>/data/`` and ``~/.aws/models``. Setting this
    environment variable indicates additional directories to check first before
    falling back to the built-in search paths.  Multiple entries should be
    separated with the ``os.pathsep`` character, which is ``:`` on Linux and
    ``;`` on Windows.

``AWS_STS_REGIONAL_ENDPOINTS``
    Sets AWS STS endpoint resolution logic. See the ``sts_regional_endpoints``
    configuration file section for more information on how to use this.

``AWS_MAX_ATTEMPTS``
    The total number of attempts made for a single request.  For more information,
    see the ``max_attempts`` configuration file section.

``AWS_RETRY_MODE``
    Specifies the types of retries the SDK will use.  For more information,
    see the ``retry_mode`` configuration file section.

``AWS_SDK_UA_APP_ID``
    AppId is an optional application specific identifier that can be set.
    When set it will be appended to the User-Agent header of every request
    in the form of App/{AppId}.

``AWS_SIGV4A_SIGNING_REGION_SET``
    A comma-delimited list of regions to sign when signing with SigV4a.  For more
    information, see the ``sigv4a_signing_region_set`` configuration file section.

``AWS_REQUEST_CHECKSUM_CALCULATION``
    Determines when a checksum will be calculated for request payloads. For more
    information, see the ``request_checksum_calculation`` configuration file section.


``AWS_RESPONSE_CHECKSUM_VALIDATION``
    Determines when checksum validation will be performed on response payloads. For more
    information, see the ``response_checksum_validation`` configuration file section.


Using a configuration file
--------------------------

Boto3 will also search the ``~/.aws/config`` file when looking for
configuration values.  You can change the location of this file by
setting the ``AWS_CONFIG_FILE`` environment variable.

This file is an INI-formatted file that contains at least one
section: ``[default]``.  You can create multiple profiles (logical
groups of configuration) by creating sections named ``[profile profile-name]``.
If your profile name has spaces, you need to surround this value with quotation marks:
``[profile "my profile name"]``.  The following are all the config variables supported
in the ``~/.aws/config`` file.

``api_versions``
    Specifies the API version to use for a particular AWS service.

    The ``api_versions`` settings are nested configuration values that require special
    formatting in the AWS configuration file. If the values are set by the
    AWS CLI or programmatically by an SDK, the formatting is handled
    automatically. If you set them by manually editing the AWS configuration
    file, the following is the required format. Notice the indentation of each
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
    The CA bundle to use. For more information, see the previous description
    of the ``AWS_CA_BUNDLE`` environment variable.
``credential_process``
    Specifies an external command to run to generate or retrieve
    authentication credentials. For more information,
    see `Sourcing credentials with an external process`_.
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
    instance metadata service.  For more information, see the previous documentation on
    ``AWS_METADATA_SERVICE_TIMEOUT``.
``metadata_service_num_attempts``
    The number of attempts to make before giving up when retrieving data from
    the instance metadata service.  For more information, see the previous documentation on
    ``AWS_METADATA_SERVICE_NUM_ATTEMPTS``.
``mfa_serial``
    Serial number of the Amazon Resource Name (ARN) of a multi-factor authentication (MFA) device to use when assuming a role.
``parameter_validation``
    Disable parameter validation (default is true, parameters are
    validated).  This is a Boolean value that
    is either ``true`` or ``false``.  Whenever you make an
    API call using a client, the parameters you provide are run through
    a set of validation checks, including (but not limited to) required
    parameters provided, type checking, no unknown parameters,
    minimum length checks, and so on.  Typically, you should leave parameter
    validation enabled.
``region``
    The default AWS Region to use, for example, ``us-west-1`` or ``us-west-2``. When
    specifying a Region inline during client initialization, this property
    is named ``region_name``.
``role_arn``
    The ARN of the role you want to assume.
``role_session_name``
    The role name to use when assuming a role.  If this value is not
    provided, a session name will be automatically generated.
``web_identity_token_file``
    The path to a file that contains an OAuth 2.0 access token or OpenID
    Connect ID token that is provided by the identity provider. The contents of
    this file will be loaded and passed as the ``WebIdentityToken`` argument to
    the ``AssumeRoleWithWebIdentity`` operation.
``s3``
    Set Amazon S3-specific configuration data. Typically, these values do not need
    to be set.

    The ``s3`` settings are nested configuration values that require special
    formatting in the AWS configuration file. If the values are set by the
    AWS CLI or programmatically by an SDK, the formatting is handled
    automatically. If you set them manually by editing the AWS configuration
    file, the following is the required format. Notice the indentation of each
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

    * ``use_accelerate_endpoint``: Specifies whether to use the Amazon S3 Accelerate
      endpoint. The bucket must be enabled to use S3 Accelerate. Valid settings
      are ``true`` or ``false``. Default: ``false``

      Either ``use_accelerate_endpoint`` or ``use_dualstack_endpoint`` can be
      enabled, but not both.
    * ``use_dualstack_endpoint``: Specifies whether to direct all Amazon S3
      requests to the dual IPv4/IPv6 endpoint for the configured Region. Valid
      settings are ``true`` or ``false``. Default: ``false``

      Either ``use_accelerate_endpoint`` or ``use_dualstack_endpoint`` can be
      enabled, but not both.
``source_profile``
    The profile name that contains credentials to use for the initial
    ``AssumeRole`` call.

    The ``credential_source`` and ``source_profile`` settings are mutually
    exclusive.

``sts_regional_endpoints``
    Sets AWS STS endpoint resolution logic. This configuration can also be set
    using the environment variable ``AWS_STS_REGIONAL_ENDPOINTS``. By default,
    this configuration option is set to ``legacy``. Valid values are the following:

    * ``regional``
        Uses the STS endpoint that corresponds to the configured Region. For
        example, if the client is configured to use ``us-west-2``, all calls
        to STS will be made to the ``sts.us-west-2.amazonaws.com`` regional
        endpoint instead of the global ``sts.amazonaws.com`` endpoint.

    * ``legacy``
        Uses the global STS endpoint, ``sts.amazonaws.com``, for the following
        configured Regions:

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

        All other Regions will use their respective regional endpoint.

``tcp_keepalive``
    Toggles the TCP Keep-Alive socket option used when creating connections.
    By default this value is ``false``; TCP Keepalive will not be used
    when creating connections. To enable TCP Keepalive with the system default configurations,
    set this value to ``true``.

``max_attempts``
    An integer representing the maximum number of attempts that will be made for
    a single request, including the initial attempt.  For example,
    setting this value to 5 will result in a request being retried up to
    4 times.  If not provided, the number of retries will default to whatever
    is modeled, which is typically 5 total attempts in the ``legacy`` retry mode,
    and 3 in the ``standard`` and ``adaptive`` retry modes.

``retry_mode``
    A string representing the type of retries Boto3 will perform.  Valid values are the following:

        * ``legacy`` - The preexisting retry behavior.  This is the default value if
          no retry mode is provided.
        * ``standard`` - A standardized set of retry rules across the AWS SDKs.
          This includes a standard set of errors that are retried and
          support for retry quotas, which limit the number of unsuccessful retries
          an SDK can make.  This mode will default the maximum number of attempts
          to 3 unless a ``max_attempts`` is explicitly provided.
        * ``adaptive`` - An experimental retry mode that includes all the
          functionality of ``standard`` mode with automatic client-side
          throttling.  This is a provisional mode whose behavior might change.

``sigv4a_signing_region_set``
    A comma-delimited list of regions use when signing with SigV4a. If this is not set,
    the SDK will check if the service has modeled a default; if none is found, this will
    default to ``*``.

``request_checksum_calculation``
    Determines when a checksum will be calculated for request payloads. Valid values are:

    * ``when_supported`` -- When set, a checksum will be calculated for
      all request payloads of operations modeled with the ``httpChecksum``
      trait where ``requestChecksumRequired`` is ``true`` or a
      ``requestAlgorithmMember`` is modeled.

    * ``when_required`` -- When set, a checksum will only be calculated
      for request payloads of operations modeled with the ``httpChecksum``
      trait where ``requestChecksumRequired`` is ``true`` or where a
      ``requestAlgorithmMember`` is modeled and supplied.

``response_checksum_validation``
    Determines when checksum validation will be performed on response payloads. Valid values are:

    * ``when_supported`` -- When set, checksum validation is performed on
      all response payloads of operations modeled with the ``httpChecksum``
      trait where ``responseAlgorithms`` is modeled, except when no modeled
      checksum algorithms are supported.

    * ``when_required`` -- When set, checksum validation is not performed
      on response payloads of operations unless the checksum algorithm is
      supported and the ``requestValidationModeMember`` member is set to ``ENABLED``.

``use_dualstack_endpoint``
    When ``true``, dualstack endpoint resolution is enabled.  Valid values are ``true`` or ``false``.  Default : ``false``.

.. _IAM Roles for Amazon EC2: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html
.. _Using IAM Roles: http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html
.. _Sourcing Credentials with an External Process: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sourcing-external.html


Using Account ID-Based Endpoints
--------------------------------
Boto3 supports account ID-based endpoints, which improve performance and scalability by using your AWS account ID to streamline request routing for services that support this feature. When Boto3 resolves credentials containing an account ID, it automatically constructs an account ID-based endpoint instead of a regional endpoint.

Account ID-based endpoints follow this format:

.. code-block:: shell

    https://<account-id>.myservice.<region>.amazonaws.com


* ``<account-id>`` is the AWS account ID sourced from your credentials.
* ``<region>`` is the AWS region where the request is being made.


Supported Credential Providers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Boto3 can automatically construct account ID-based endpoints by sourcing the AWS account ID from the following places:

* Credentials set using the ``boto3.client()`` method
* Credentials set when creating a ``Session`` object
* Environment variables
* Assume role provider
* Assume role with web identity provider
* AWS IAM Identity Center credential provider
* Shared credential file (``~/.aws/credentials``)
* AWS config file (``~/.aws/config``)
* Container credential provider

You can read more about these locations in the :ref:`guide_credentials` guide.


Configuring Account ID
~~~~~~~~~~~~~~~~~~~~~~

You can provide an account ID along with your AWS credentials using one of the following:

Passing it as a parameter when creating clients:

.. code-block:: python

    import boto3

    client = boto3.client(
        'dynamodb',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        aws_account_id=ACCOUNT_ID
    )

Passing it as a parameter when creating a ``Session`` object:

.. code-block:: python

    import boto3

    session = boto3.Session(
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        aws_account_id=ACCOUNT_ID
    )

Setting an environment variable:

.. code-block:: shell

    export AWS_ACCESS_KEY_ID=<ACCESS_KEY>
    export AWS_SECRET_ACCESS_KEY=<SECRET_KEY>
    export AWS_ACCOUNT_ID=<ACCOUNT_ID>

Setting it in the shared credentials or config file:

.. code-block:: ini

    [default]
    aws_access_key_id=foo
    aws_secret_access_key=bar
    aws_account_id=baz


Configuring Endpoint Routing Behavior
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The account ID endpoint mode is a setting that can be used to turn off account ID-based endpoint routing if necessary.

Valid values are:

* ``preferred`` – The endpoint should include account ID if available.
* ``disabled`` – A resolved endpoint doesn't include account ID.
* ``required`` – The endpoint must include account ID. If the account ID isn't available, the SDK throws an error.

.. note::

    The default behavior in Boto3 is ``preferred``.


You can configure the setting using one of the following:

Setting it in the ``Config`` object when creating clients:

.. code-block:: python

    import boto3
    from botocore.config import Config

    my_config = Config(
        account_id_endpoint_mode = 'disabled'
    )

    client = boto3.client('dynamodb', config=my_config)

Setting an environment variable:

.. code-block:: shell

    export AWS_ACCOUNT_ID_ENDPOINT_MODE=disabled

Setting it in the shared credentials or config file:

.. code-block:: ini

    [default]
    account_id_endpoint_mode=disabled