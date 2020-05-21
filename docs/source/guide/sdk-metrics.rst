.. _guide_sdk-metrics:

SDK metrics 
===========

AWS SDK Metrics for Enterprise Support (SDK Metrics) enables Enterprise customers to collect metrics from AWS SDKs on their hosts and clients shared with 
AWS Enterprise Support. SDK Metrics provides information that helps speed up detection and diagnosis of issues occurring in connections 
to AWS services for AWS Enterprise Support customers. 

As telemetry is collected on each host, it is relayed via UDP to 127.0.0.1 (aka localhost), where the CloudWatch agent aggregates the data and sends it 
to the SDK Metrics service. Therefore, to receive metrics, you must add the CloudWatch agent to your instance.

The following steps to set up SDK Metrics pertain to an Amazon EC2 instance running Amazon Linux for a client application that is using the AWS SDK for Python.
SDK Metrics is also available for your production environments if you enable it while configuring the AWS SDK for Python. 

To utilize SDK Metrics, run the latest version of the CloudWatch agent. Learn how to 
`Configure the CloudWatch Agent for SDK Metrics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-SDK-Metrics.html>`__ in the Amazon CloudWatch User Guide.

To set up SDK Metrics with the AWS SDK for Python, follow these instructions:

#. Create an application with an AWS SDK for Python client to use an AWS service.
#. Host your project on an Amazon EC2 instance or in your local environment.
#. Install and use the latest version of Boto3 (AWS SDK for Python).
#. Install and configure a CloudWatch agent on an EC2 instance or in your local environment as described in the `Amazon CloudWatch User Guide <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-SDK-Metrics.html>`__ .
#. Authorize SDK Metrics to collect and send metrics as described in the `Amazon CloudWatch User Guide <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-SDK-Metrics.html>`__ .. 
#. :ref:`csm-enable-agent`.


For more information, see the following:

* :ref:`csm-update-agent`
* :ref:`csm-disable-agent`


.. _csm-enable-agent:

Enable SDK metrics
------------------

By default, SDK Metrics is turned off, and the port is set to 31000. The following are the default parameters.

Enabling SDK Metrics is independent of configuring your credentials to use an AWS service.

You can enable SDK Metrics by setting environment variables or by using the AWS Shared config file.

Option 1: Set environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If :code:`AWS_CSM_ENABLED` is not set, the SDK checks the :code:`AWS_DEFAULT_PROFILE` profile to determine if SDK Metrics is enabled. By default this is set to ``false``.

To turn on SDK Metrics, add the following to your environmental variables.

.. code-block:: shell

    export AWS_CSM_ENABLED=true

:ref:`Other configuration settings<csm-update-agent>` are available. 

Note: Enabling SDK Metrics does not configure your credentials to use an AWS service. 


Option 2: AWS shared config file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If no CSM configuration is found in the environment variables, the SDK looks for your default AWS profile field. If :code:`AWS_DEFAULT_PROFILE` is set to something other than default, update that profile. To enable SDK Metrics, add :code:`csm_enabled` to the shared config file located at :file:`~/.aws/config`.

.. code-block:: ini

    [default]
    csm_enabled = true

    [profile aws_csm]
    csm_enabled = true

:ref:`Other configuration settings<csm-update-agent>` are available. 

Note: Enabling SDK Metrics is independent from configuring your credentials to use an AWS service. You can use a different profile to authenticate. 

.. _csm-update-agent:

Update a CloudWatch agent
-------------------------

To make changes to the port, you need to set the values and then restart any AWS jobs that are currently active.

Option 1: Set environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Most services use the default port. But if your service requires a unique port ID, add ``AWS_CSM_PORT=[port_number]``, to the host's environment variables.

.. code-block:: shell

    export AWS_CSM_ENABLED=true
    export AWS_CSM_PORT=1234


Option 2: AWS shared config file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Most services use the default port. But if your service requires a
unique port ID, add ``csm_port = [port_number]`` to ``~/.aws/config``.

.. code-block:: ini

    [default]
    csm_enabled = false
    csm_port = 1234

    [profile aws_csm]
    csm_enabled = false
    csm_port = 1234

Restart SDK metrics
~~~~~~~~~~~~~~~~~~~

To restart a job, run the following commands.

.. code-block:: shell

    amazon-cloudwatch-agent-ctl –a stop;
    amazon-cloudwatch-agent-ctl –a start;


.. _csm-disable-agent:

Disable SDK metrics
--------------------

To turn off SDK Metrics, remove ``csm_enabled`` from your environment variables, or in your AWS Shared config file located at :file:`~/.aws/config`.
Then restart your CloudWatch agent so that the changes can take effect.

**Environment Variables**

Remove ``AWS_CSM_ENABLED`` from your environment variables or set it to false.

.. code-block:: shell

    unset AWS_CSM_ENABLED


**AWS Shared Config File**

Remove ``csm_enabled`` from the profiles in your AWS Shared config file located at :file:`~/.aws/config`.

.. note:: Environment variables override the AWS Shared config file. If SDK Metrics is enabled in the environment variables, the SDK Metrics remain enabled.

To explicitly opt-out of SDK Metrics set ``csm_enabled`` to false.

.. code-block:: ini

    [default]
    csm_enabled = false

    [profile aws_csm]
    csm_enabled = false

To disable SDK Metrics, use the following command to stop CloudWatch agent. 

.. code-block:: shell

    sudo amazon-cloudwatch-agent-ctl -a stop &&
    echo "Done"
    
If you are using other CloudWatch features, restart CloudWatch Agent with the following command.

.. code-block:: shell

    amazon-cloudwatch-agent-ctl –a start;
    

Restart SDK metrics
~~~~~~~~~~~~~~~~~~~

To restart a SDK Metrics job, run the following commands.

.. code-block:: shell

    amazon-cloudwatch-agent-ctl –a stop;
    amazon-cloudwatch-agent-ctl –a start;

Definitions for SDK metrics
---------------------------

You can use the following descriptions of SDK Metrics to interpret your results. In general, these metrics are available for review
with your Technical Account Manager during regular business reviews. AWS Support resources and your Technical Account Manager 
should have access to SDK Metrics data to help you resolve cases, but if you discover data that is confusing or unexpected, but 
doesn’t seem to be negatively impacting your applications’ performance, it is best to review that data during scheduled 
business reviews.

.. list-table:: 
   :widths: 1 2 
   :header-rows: 1

   * - Metric: 
     - CallCount
     
   * - Definition
     - Total number of successful or failed API calls from your code to AWS services

   * - How to use it
     - Use it as a baseline to correlate with other metrics like errors or throttling.


.. list-table:: 
   :widths: 1 2 
   :header-rows: 1

   * - Metric: 
     - ClientErrorCount 

   * - Definition
     - Number of API calls that fail with client errors (4xx HTTP response codes). *Examples: Throttling, Access denied, S3 bucket does not exist, and Invalid parameter value.*

   * - How to use it
     - Except in certain cases related to throttling (ex. when throttling occurs due to a limit that needs to be increased) this metric can indicate something in your application that needs to be fixed.


.. list-table:: 
   :widths: 1 2 
   :header-rows: 1

   * - Metric: 
     - ConnectionErrorCount 

   * - Definition
     - Number of API calls that fail because of errors connecting to the service. These can be caused by network issues between the customer application and AWS services including load balancers, DNS failures, transit providers. In some cases, AWS issues may result in this error.

   * - How to use it
     - Use this metric to determine whether issues are specific to your application or are caused by your infrastructure and/or network. High ConnectionErrorCount could also indicate short timeout values for API calls.


.. list-table:: 
   :widths: 1 2 
   :header-rows: 1

   * - Metric: 
     - ThrottleCount 

   * - Definition
     - Number of API calls that fail due to throttling by AWS services.

   * - How to use it
     - Use this metric to assess if your application has reached throttle limits, as well as to determine the cause of retries and application latency. Consider distributing calls over a window instead of batching your calls.


.. list-table:: 
   :widths: 1 2 
   :header-rows: 1

   * - Metric: 
     - ServerErrorCount 

   * - Definition
     - Number of API calls that fail due to server errors (5xx HTTP response codes) from AWS Services. These are typically caused by AWS services.

   * - How to use it
     - Determine cause of SDK retries or latency. This metric will not always indicate that AWS services are at fault, as some AWS teams classify latency as an HTTP 503 response. 

.. list-table:: 
   :widths: 1 2 
   :header-rows: 1

   * - Metric: 
     - EndToEndLatency

   * - Definition
     - Total time for your application to make a call using the AWS SDK, inclusive of retries. In other words, regardless of whether it is successful after several attempts, or as soon as a call fails due to an unretriable error.

   * - How to use it
     - Determine how AWS API calls contribute to your application’s overall latency. Higher than expected latency may be caused by issues with network, firewall, or other configuration settings, or by latency that occurs as a result of SDK retries. 

