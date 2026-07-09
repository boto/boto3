.. Copyright 2010-2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _guide_bedrock:

#########################
Amazon Bedrock Runtime
#########################

.. contents:: **Topics**
    :depth: 2
    :local:

Overview
--------

`Amazon Bedrock <https://aws.amazon.com/bedrock/>`_ is a fully managed service that provides
access to foundation models (FMs) from leading AI companies through a unified API. This guide
covers common use cases for the ``bedrock-runtime`` client using the
`Converse API <https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html>`_,
which is the recommended approach for conversational use cases.

Prerequisites
~~~~~~~~~~~~~

Before getting started, ensure you have:

* An AWS account with Amazon Bedrock access enabled
* Model access granted for your desired foundation model in the
  `Bedrock console <https://console.aws.amazon.com/bedrock/home#/modelaccess>`_
* Boto3 installed and configured with appropriate IAM permissions

The examples below use ``us.anthropic.claude-opus-4-6-v1:0``. You can substitute any
`supported model ID <https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html>`_.

.. _bedrock_converse:

Send a message with the Converse API
--------------------------------------

The Converse API provides a unified interface across all supported models and handles the
message format automatically. It is the recommended API for text-based conversational use cases.

.. code-block:: python

    import boto3

    client = boto3.client("bedrock-runtime", region_name="us-east-1")

    response = client.converse(
        modelId="us.anthropic.claude-opus-4-6-v1:0",
        messages=[
            {
                "role": "user",
                "content": [{"text": "What is Amazon Bedrock?"}],
            }
        ],
        inferenceConfig={
            "maxTokens": 512,
            "temperature": 0.7,
        },
    )

    print(response["output"]["message"]["content"][0]["text"])

.. _bedrock_system_prompt:

Use a system prompt
---------------------

You can include a system prompt to set the model's behavior and context.

.. code-block:: python

    import boto3

    client = boto3.client("bedrock-runtime", region_name="us-east-1")

    response = client.converse(
        modelId="us.anthropic.claude-opus-4-6-v1:0",
        system=[
            {"text": "You are a helpful assistant that responds concisely."}
        ],
        messages=[
            {
                "role": "user",
                "content": [{"text": "Explain what an S3 bucket is."}],
            }
        ],
    )

    print(response["output"]["message"]["content"][0]["text"])

.. _bedrock_multi_turn:

Multi-turn conversation
-----------------------

The Converse API supports multi-turn conversations by passing the conversation history in the
``messages`` parameter.

.. code-block:: python

    import boto3

    client = boto3.client("bedrock-runtime", region_name="us-east-1")

    messages = [
        {"role": "user", "content": [{"text": "What is AWS Lambda?"}]},
        {
            "role": "assistant",
            "content": [
                {
                    "text": "AWS Lambda is a serverless compute service that runs your code "
                    "in response to events without requiring you to manage servers."
                }
            ],
        },
        {"role": "user", "content": [{"text": "How does it differ from EC2?"}]},
    ]

    response = client.converse(
        modelId="us.anthropic.claude-opus-4-6-v1:0",
        messages=messages,
    )

    print(response["output"]["message"]["content"][0]["text"])

.. _bedrock_streaming:

Stream a response
-----------------

Use ``converse_stream`` to receive the model's response incrementally as it is generated.
This is useful for displaying responses in real time.

.. code-block:: python

    import boto3

    client = boto3.client("bedrock-runtime", region_name="us-east-1")

    response = client.converse_stream(
        modelId="us.anthropic.claude-opus-4-6-v1:0",
        messages=[
            {
                "role": "user",
                "content": [{"text": "Write a short poem about cloud computing."}],
            }
        ],
    )

    stream = response.get("stream")
    if stream:
        for event in stream:
            if "contentBlockDelta" in event:
                delta = event["contentBlockDelta"]["delta"]
                if "text" in delta:
                    print(delta["text"], end="", flush=True)
    print()  # newline after streaming completes

.. _bedrock_cross_region:

Cross-region inference
----------------------

Cross-region inference routes requests across multiple AWS Regions for higher throughput and
availability during peak demand. To enable it, prefix your model ID with the inference profile
prefix (e.g., ``us.`` for the US geography).

.. code-block:: python

    import boto3

    # Use us-east-1 as the entry point; Bedrock routes to the optimal region automatically
    client = boto3.client("bedrock-runtime", region_name="us-east-1")

    response = client.converse(
        modelId="us.anthropic.claude-opus-4-6-v1:0",  # note the "us." prefix
        messages=[
            {
                "role": "user",
                "content": [{"text": "Summarize the benefits of cross-region inference."}],
            }
        ],
    )

    print(response["output"]["message"]["content"][0]["text"])

.. note::

    Cross-region inference profiles are available for select models. See
    `Supported Regions and models <https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html>`_
    for the full list.

.. _bedrock_error_handling:

Error handling
--------------

Handle common Bedrock errors such as throttling and model-specific exceptions.

.. code-block:: python

    import boto3
    from botocore.exceptions import ClientError

    client = boto3.client("bedrock-runtime", region_name="us-east-1")

    try:
        response = client.converse(
            modelId="us.anthropic.claude-opus-4-6-v1:0",
            messages=[
                {"role": "user", "content": [{"text": "Hello!"}]}
            ],
        )
        print(response["output"]["message"]["content"][0]["text"])

    except client.exceptions.ThrottlingException:
        print("Request was throttled. Consider adding retry logic with exponential backoff.")
    except client.exceptions.ModelNotReadyException:
        print("The model is not ready. Ensure model access is enabled in the Bedrock console.")
    except ClientError as e:
        print(f"Unexpected error: {e.response['Error']['Message']}")
