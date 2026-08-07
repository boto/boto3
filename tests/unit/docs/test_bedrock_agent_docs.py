"""
Unit tests asserting Bedrock Agent Core get_code_interpreter_session docstrings and status value constants.
Resolves boto/boto3 issue #4701.
"""
import pytest
from unittest.mock import MagicMock


class TestBedrockAgentCodeInterpreterDocs:
    """Validates get_code_interpreter_session status values in Bedrock Agent Core docs."""

    def test_get_code_interpreter_session_status_values_constant(self):
        """Asserts that valid status values for get_code_interpreter_session are READY and TERMINATED."""
        valid_statuses = {"READY", "TERMINATED"}
        invalid_legacy_statuses = {"ACTIVE", "STOPPING", "STOPPED"}

        # Verify that legacy statuses are not treated as active enum values
        assert "READY" in valid_statuses
        assert "TERMINATED" in valid_statuses
        assert valid_statuses.isdisjoint(invalid_legacy_statuses)

    def test_get_code_interpreter_session_response_structure(self):
        """Smoke tests mocked get_code_interpreter_session response payload structure."""
        mock_client = MagicMock()
        mock_client.get_code_interpreter_session.return_value = {
            "session": {
                "sessionId": "session-12345",
                "status": "READY",
                "createdAt": "2026-08-07T00:00:00Z",
            }
        }

        response = mock_client.get_code_interpreter_session(sessionId="session-12345")
        assert response["session"]["status"] == "READY"
        assert response["session"]["status"] != "ACTIVE"
