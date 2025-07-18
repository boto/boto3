import boto3

boto3.set_stream_logger('')

client = boto3.client("bedrock-runtime", region_name="eu-west-3")

messages = [
    {
        "role": "user",
        "content": [
            {
                "document": {
                    "format": "txt",
                    "name": "My Document",
                    "source": {
                        "text": "The grass is green. The sky is blue."
                    },
                    "citations": {"enabled": True}
                }
            },
            {"text": "What color is the grass and sky?"}
        ]
    }
]

response = client.converse(
    modelId="eu.anthropic.claude-3-7-sonnet-20250219-v1:0",
    messages=messages,
    inferenceConfig={
        "maxTokens": 1000,
        "temperature": 0.1
    }
)

print(response['output']['message'])

# Append the assistant's response to messages
messages.append(response['output']['message'])

# Add another user message and continue the conversation
messages.append({
    "role": "user",
    "content": [{"text": "What about the sun?"}]
})

response2 = client.converse(
    modelId="eu.anthropic.claude-3-7-sonnet-20250219-v1:0",
    messages=messages,
    inferenceConfig={
        "maxTokens": 1000,
        "temperature": 0.1
    }
)

print(response2)