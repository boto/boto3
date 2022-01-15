.. _guide_retries:

Retries
=======

Overview
--------

Your AWS client might see calls to AWS services fail due to unexpected issues on the client side. Or calls might fail due to rate limiting from the AWS service you're attempting to call. In either case, these kinds of failures often don’t require special handling and the call should be made again, often after a brief waiting period. Boto3 provides many features to assist in retrying client calls to AWS services when these kinds of errors or exceptions are experienced.

This guide provides you with details on the following:

* How to find the available retry modes and the differences between each mode
* How to configure your client to use each retry mode and other retry configurations
* How to validate if your client performs a retry attempt

Available retry modes
---------------------

Legacy retry mode
~~~~~~~~~~~~~~~~~~

Legacy mode is the default mode used by any Boto3 client you create. As its name implies, ``legacy mode`` uses an older (v1) retry handler that has limited functionality.

**Legacy mode’s functionality includes:**

* A default value of 5 for maximum retry attempts. This value can be overwritten through the ``max_attempts`` configuration parameter.
* Retry attempts for a limited number of errors/exceptions::

   # General socket/connection errors
   ConnectionError
   ConnectionClosedError
   ReadTimeoutError
   EndpointConnectionError

   # Service-side throttling/limit errors and exceptions
   Throttling
   ThrottlingException
   ThrottledException
   RequestThrottledException
   ProvisionedThroughputExceededException

* Retry attempts on several HTTP status codes, including 429, 500, 502, 503, 504, and 509.
* Any retry attempt will include an exponential backoff by a base factor of 2.


.. note::
   For more information about additional service-specific retry policies, see the following `botocore references in GitHub <https://github.com/boto/botocore/blob/develop/botocore/data/_retry.json>`_.


Standard retry mode
~~~~~~~~~~~~~~~~~~~~

Standard mode is a retry mode that was introduced with the updated retry handler (v2). This mode is a standardization of retry logic and behavior that is consistent with other AWS SDKs. In addition to this standardization, this mode also extends the functionality of retries over that found in legacy mode.

**Standard mode’s functionality includes:**

* A default value of 3 for maximum retry attempts. This value can be overwritten through the ``max_attempts`` configuration parameter.
* Retry attempts for an expanded list of errors/exceptions::

   # Transient errors/exceptions
   RequestTimeout
   RequestTimeoutException
   PriorRequestNotComplete
   ConnectionError
   HTTPClientError

   # Service-side throttling/limit errors and exceptions
   Throttling
   ThrottlingException
   ThrottledException
   RequestThrottledException
   TooManyRequestsException
   ProvisionedThroughputExceededException
   TransactionInProgressException
   RequestLimitExceeded
   BandwidthLimitExceeded
   LimitExceededException
   RequestThrottled
   SlowDown
   EC2ThrottledException

* Retry attempts on nondescriptive, transient error codes. Specifically, these HTTP status codes: 500, 502, 503, 504.
* Any retry attempt will include an exponential backoff by a base factor of 2 for a maximum backoff time of 20 seconds.

Adaptive retry mode
~~~~~~~~~~~~~~~~~~~~

Adaptive retry mode is an experimental retry mode that includes all the features of standard mode. In addition to the standard mode features, adaptive mode also introduces client-side rate limiting through the use of a token bucket and rate-limit variables that are dynamically updated with each retry attempt. This mode offers flexibility in client-side retries that adapts to the error/exception state response from an AWS service.

With each new retry attempt, adaptive mode modifies the rate-limit variables based on the error, exception, or HTTP status code presented in the response from the AWS service. These rate-limit variables are then used to calculate a new call rate for the client. Each exception/error or non-success HTTP response (provided in the list above) from an AWS service updates the rate-limit variables as retries occur until success is reached, the token bucket is exhausted, or the configured maximum attempts value is reached.

.. note::
   Adaptive mode is an experimental mode and is subject to change, both in features and behavior.


Configuring a retry mode
-------------------------

Boto3 includes a variety of both retry configurations as well as configuration methods to consider when creating your client object.

Available configuration options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In Boto3, users can customize two retry configurations:

* ``retry_mode`` - This tells Boto3 which retry mode to use. As described previously, there are three retry modes available: legacy (default), standard, and adaptive.
* ``max_attempts`` - This provides Boto3’s retry handler with a value of maximum retry attempts, where the initial call counts toward the ``max_attempts`` value that you provide.

Defining a retry configuration in your AWS configuration file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This first way to define your retry configuration is to update your global AWS configuration file. The default location for your AWS config file is ``~/.aws/config``. Here’s an example of an AWS config file with the retry configuration options used::

   [myConfigProfile]
   region = us-east-1
   max_attempts = 10
   retry_mode = standard

Any Boto3 script or code that uses your AWS config file inherits these configurations when using your profile, unless otherwise explicitly overwritten by a ``Config`` object when instantiating your client object at runtime. If no configuration options are set, the default retry mode value is ``legacy``, and the default ``max_attempts`` value is 5.

Defining a retry configuration in a Config object for your Boto3 client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The second way to define your retry configuration is to use botocore to enable more flexibility for you to specify your retry configuration using a ``Config`` object that you can pass to your client at runtime. This method is useful if you don't want to configure retry behavior globally with your AWS config file 

Additionally, if your AWS configuration file is configured with retry behavior, but you want to override those global settings, you can use the ``Config`` object to override an individual client object at runtime.

As shown in the following example, the ``Config`` object takes a ``retries`` dictionary where you can supply your two configuration options, ``max_attempts`` and ``mode``, and the values for each.

.. code-block:: python

   config = Config(
      retries = {
         'max_attempts': 10,
         'mode': 'standard'
      }
   )

.. note::
   The AWS configuration file uses ``retry_mode`` and the ``Config`` object uses ``mode``. Although named differently, they both refer to the same retry configuration whose options are legacy (default), standard, and adaptive.

The following is an example of instantiating a ``Config`` object and passing it into an Amazon EC2 client to use at runtime.

.. code-block:: python

   import boto3
   from botocore.config import Config

   config = Config(
      retries = {
         'max_attempts': 10,
         'mode': 'standard'
      }
   )

   ec2 = boto3.client('ec2', config=config)

.. note::
   As mentioned previously, if no configuration options are set, the default mode is ``legacy`` and the default ``max_attempts`` is 5.


Validating retry attempts
--------------------------

To ensure that your retry configuration is correct and working properly, there are a number of ways you can validate that your client's retries are occurring. 

Checking retry attempts in your client logs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you enable Boto3’s logging, you can validate and check your client’s retry attempts in your client’s logs. Notice, however, that you need to enable ``DEBUG`` mode in your logger to see any retry attempts. The client log entries for retry attempts will appear differently, depending on which retry mode you’ve configured.

**If legacy mode is enabled:**

Retry messages are generated by ``botocore.retryhandler``. You’ll see one of three messages:

* *No retry needed*
* *Retry needed, action of: <action_value>*
* *Reached the maximum number of retry attempts: <attempt_num>*


**If standard or adaptive mode is enabled:**

Retry messages are generated by ``botocore.retries.standard``. You’ll see one of three messages:

* *Not retrying request*
* *Retry needed, retrying request after delay of: <delay_value>*
* *Retry needed but retry quota reached, not retrying request*

Checking retry attempts in an AWS service response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can check the number of retry attempts your client has made by parsing the response botocore provides when making a call to an AWS service API. Responses are handled by an underlying botocore module, and formatted into a dictionary that's part of the JSON response object. You can access the number of retry attempts your client has taken by calling the ``RetryAttempts`` key in the ``ResponseMetaData`` dictionary::

   'ResponseMetadata': {
      'RequestId': '1234567890ABCDEF',
      'HostId': 'host ID data will appear here as a hash',
      'HTTPStatusCode': 400,
      'HTTPHeaders': {'header metadata key/values will appear here'},
      'RetryAttempts': 4
   }
