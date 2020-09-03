.. _guide_error-handling:

Error handling
==============

Overview
--------
Boto3 provides many features to assist in navigating the errors and exceptions that you might encounter when interacting with AWS services.

Specifically, this guide provides details on the following:

* How to find what exceptions could be thrown by both Boto3 and AWS services
* How to catch and handle exceptions thrown by both Boto3 and AWS services
* How to parse error responses from AWS services

Why catch exceptions from AWS and Boto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* *Service limits and quotas* - Your call rate to an AWS service might be too frequent, or you might have reached a specific AWS service quota. In either case, without proper error handling you wouldn’t know or wouldn’t handle them.
* *Parameter validation and checking* - API requirements can change, especially across API versions. Catching these errors helps to identify if there’s an issue with the parameters you provide to any given API call.
* *Proper logging and messaging* - Catching errors and exceptions means you can log them. This can be instrumental in troubleshooting any code you write when interacting with AWS services.

Determining what exceptions to catch
------------------------------------
Exceptions that you might encounter when using Boto3 will come from one of two sources: botocore or the AWS services your client is interacting with.

Botocore exceptions
~~~~~~~~~~~~~~~~~~~
These exceptions are statically defined within the botocore package, a dependency of Boto3. The exceptions are related to issues with client-side behaviors, configurations, or validations. You can generate a list of the statically defined botocore exceptions using the following code:

.. code-block:: python

    import botocore.exceptions

    for key, value in sorted(botocore.exceptions.__dict__.items()):
        if isinstance(value, type):
            print(key)

.. tip::

    .. raw:: html

        <details>
        <summary>Click to see a full list of static exceptions</summary>

    .. code-block:: text

        AliasConflictParameterError
        ApiVersionNotFoundError
        BaseEndpointResolverError
        BotoCoreError
        ChecksumError
        ClientError
        ConfigNotFound
        ConfigParseError
        ConnectTimeoutError
        ConnectionClosedError
        ConnectionError
        CredentialRetrievalError
        DataNotFoundError
        EndpointConnectionError
        EventStreamError
        HTTPClientError
        ImminentRemovalWarning
        IncompleteReadError
        InfiniteLoopConfigError
        InvalidConfigError
        InvalidDNSNameError
        InvalidExpressionError
        InvalidMaxRetryAttemptsError
        InvalidRetryConfigurationError
        InvalidS3AddressingStyleError
        InvalidS3UsEast1RegionalEndpointConfigError
        InvalidSTSRegionalEndpointsConfigError
        MD5UnavailableError
        MetadataRetrievalError
        MissingParametersError
        MissingServiceIdError
        NoCredentialsError
        NoRegionError
        OperationNotPageableError
        PaginationError
        ParamValidationError
        PartialCredentialsError
        ProfileNotFound
        ProxyConnectionError
        RangeError
        ReadTimeoutError
        RefreshWithMFAUnsupportedError
        SSLError
        ServiceNotInRegionError
        StubAssertionError
        StubResponseError
        UnStubbedResponseError
        UndefinedModelAttributeError
        UnknownClientMethodError
        UnknownCredentialError
        UnknownEndpointError
        UnknownKeyError
        UnknownParameterError
        UnknownServiceError
        UnknownServiceStyle
        UnknownSignatureVersionError
        UnseekableStreamError
        UnsupportedS3AccesspointConfigurationError
        UnsupportedS3ArnError
        UnsupportedSignatureVersionError
        UnsupportedTLSVersionWarning
        ValidationError
        WaiterConfigError
        WaiterError

    .. raw:: html

        </details>

.. note::

    You can view available descriptions of the botocore static exceptions `here <https://github.com/boto/botocore/blob/develop/botocore/exceptions.py>`_.

AWS service exceptions
~~~~~~~~~~~~~~~~~~~~~~
AWS service exceptions are caught with the underlying botocore exception, ``ClientError``. After you catch this exception, you can parse through the response for specifics around that error, including the service-specific exception. Exceptions and errors from AWS services vary widely. You can quickly get a list of an AWS service’s exceptions using Boto3.

For a complete list of error responses from the services you’re using, consult the individual service’s `AWS documentation <https://docs.aws.amazon.com/>`_, specifically the error response section of the AWS service’s API reference. These references also provide context around the exceptions and errors.

Catching exceptions when using a low-level client
-------------------------------------------------

Catching botocore exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Botocore exceptions are statically defined in the botocore package. Any Boto3 clients you create will use these same statically defined exception classes. The most common botocore exception you’ll encounter is ``ClientError``. This is a general exception when an error response is provided by an AWS service to your Boto3 client’s request.

Additional client-side issues with SSL negotiation, client misconfiguration, or AWS service validation errors will also throw botocore exceptions. Here’s a generic example of how you might catch botocore exceptions.

.. code-block:: python

    import botocore
    import boto3

    client = boto3.client('aws_service_name')

    try:
        client.some_api_call(SomeParam='some_param')

    except botocore.exceptions.ClientError as error:
        # Put your error handling logic here
        raise error

    except botocore.exceptions.ParamValidationError as error:
        raise ValueError('The parameters you provided are incorrect: {}'.format(error))

Parsing error responses and catching exceptions from AWS services
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlike botocore exceptions, AWS service exceptions aren't statically defined in Boto3. This is due to errors and exceptions from AWS services varying widely and being subject to change. To properly catch an exception from an AWS service, you must parse the error response from the service. The error response provided to your client from the AWS service follows a common structure and is minimally processed and not obfuscated by Boto3.

Using Boto3, the error response from an AWS service will look similar to a success response, except that an ``Error`` nested dictionary will appear with the ``ResponseMetadata`` nested dictionary. Here is an example of what an error response might look like::

    {
        'Error': {
            'Code': 'SomeServiceException',
            'Message': 'Details/context around the exception or error'
        },
        'ResponseMetadata': {
            'RequestId': '1234567890ABCDEF',
            'HostId': 'host ID data will appear here as a hash',
            'HTTPStatusCode': 400,
            'HTTPHeaders': {'header metadata key/values will appear here'},
            'RetryAttempts': 0
        }
    }

Boto3 classifies all AWS service errors and exceptions as ``ClientError`` exceptions. When attempting to catch AWS service exceptions, one way is to catch ``ClientError`` and then parse the error response for the AWS service-specific exception.

Using Amazon Kinesis as an example service, you can use Boto3 to catch the exception ``LimitExceededException`` and insert your own logging message when your code experiences request throttling from the AWS service.

.. code-block:: python

    import botocore
    import boto3
    import logging

    # Set up our logger
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()

    client = boto3.client('kinesis')

    try:
        logger.info('Calling DescribeStream API on myDataStream')
        client.describe_stream(StreamName='myDataStream')

    except botocore.exceptions.ClientError as error:
        if error.response['Error']['Code'] == 'LimitExceededException':
            logger.warn('API call limit exceeded; backing off and retrying...')
        else:
            raise error

.. note::

    The Boto3 ``standard`` retry mode will catch throttling errors and exceptions, and will back off and retry them for you.

Additionally, you can also access some of the dynamic service-side exceptions from the client’s exception property. Using the previous example, you would need to modify only the ``except`` clause.

.. code-block:: python

    except client.exceptions.LimitExceedException as error:
        logger.warn('API call limit exceeded; backing off and retrying...')

.. note::

    Catching exceptions through ``ClientError`` and parsing for error codes is still the best way to catch **all** service-side exceptions and errors.

Catching exceptions when using a resource client
------------------------------------------------

When using ``Resource`` classes to interact with certain AWS services, catching exceptions and errors is a similar experience to using a low-level client.

Parsing for error responses uses the same exact methodology outlined in the low-level client section. Catching exceptions through the client’s ``exceptions`` property is slightly different, as you’ll need to access the client’s ``meta`` property to get to the exceptions.

.. code-block:: python

    client.meta.client.exceptions.SomeServiceException

Using Amazon S3 as an example resource service, you can use the client’s exception property to catch the ``BucketAlreadyExists`` exception. And you can still parse the error response to get the bucket name that's passed in the original request.

.. code-block:: python

    import botocore
    import boto3

    client = boto3.resource('s3')

    try:
        client.create_bucket(BucketName='myTestBucket')

    except client.meta.client.exceptions.BucketAlreadyExists as err:
        print("Bucket {} already exists!".format(err.response['Error']['BucketName']))
        raise err

Discerning useful information from error responses
--------------------------------------------------
As stated previously in this guide, for details and context around specific AWS service exceptions, see the individual service’s `AWS documentation <https://docs.aws.amazon.com/>`_, specifically the error response section of the AWS service’s API reference.

Botocore exceptions will have detailed error messaging when those exceptions are thrown. These error messages provide details and context around the specific exception thrown. Descriptions of these exceptions can be viewed `here <https://github.com/boto/botocore/blob/develop/botocore/exceptions.py>`_.

Outside of specific error or exception details and messaging, you might want to extract additional metadata from error responses:

* *Exception class and error message* - You can use this data to build logic around, or in response to, these errors and exceptions.
* *Request ID and HTTP status code* - AWS service exceptions might still be vague or lacking in details. If this occurs, contacting customer support and providing the AWS service name, error, error message, and request ID could allow a support engineer to further look into your issue.

Using a low-level Amazon SQS client, here’s an example of catching a generic or vague exception from the AWS service, and parsing out useful metadata from the error response.

.. code-block:: python

    import botocore
    import boto3

    client = boto3.client('sqs')
    queue_url = 'SQS_QUEUE_URL'

    try:
        client.send_message(QueueUrl=queue_url, MessageBody=('some_message')

    except botocore.exceptions.ClientError as err:
        if err.response['Error']['Code'] == 'InternalError': # Generic error
            # We grab the message, request ID, and HTTP code to give to customer support
            print('Error Message: {}'.format(err.response['Error']['Message']))
            print('Request ID: {}'.format(err.response['ResponseMetadata']['RequestId']))
            print('Http code: {}'.format(err.response['ResponseMetadata']['HTTPStatusCode']))
        else:
            raise err
