import os
import unittest

import boto3


class TestEndpointUrl(unittest.TestCase):
    def test_default_session_does_not_require_endpoint_url_env_var(self):
        boto3.setup_default_session(
            aws_access_key_id="key", aws_secret_access_key="secret"
        )
        client = boto3.DEFAULT_SESSION.client("s3")
        self.assertTrue(
            client._endpoint.host.endswith("amazonaws.com"),
            "AWS_ENDPOINT_URL env var should not be required",
        )

    def test_default_session_uses_endpoint_url_env_var(self):
        ENDPOINT_URL = "http://endpoint.url"
        os.environ["AWS_ENDPOINT_URL"] = ENDPOINT_URL
        boto3.setup_default_session(
            aws_access_key_id="key", aws_secret_access_key="secret"
        )
        client = boto3.DEFAULT_SESSION.client("s3")
        self.assertTrue(
            client._endpoint.host == ENDPOINT_URL,
            "AWS_ENDPOINT_URL env var not used when set",
        )
        del os.environ["AWS_ENDPOINT_URL"]


# eof
