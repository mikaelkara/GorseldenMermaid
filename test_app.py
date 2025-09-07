import json
from unittest.mock import MagicMock, patch

import pytest
from app import diagram_from_text


# Mock the OpenAI response object structure
class MockChoice:
    def __init__(self, content):
        self.message = {"content": content}


class MockResponse:
    def __init__(self, content):
        self.choices = [MockChoice(content)]


# Test cases for the diagram_from_text function
@pytest.mark.parametrize(
    "api_response, expected_output",
    [
        # Case 1: Perfect JSON
        (
            '{"type": "flowchart", "description": "A simple flowchart", "mermaid": "graph TD; A-->B;"}',
            {"type": "flowchart", "description": "A simple flowchart", "mermaid": "graph TD; A-->B;"},
        ),
        # Case 2: JSON wrapped in markdown
        (
            '```json\n{"type": "sequence", "description": "A sequence diagram", "mermaid": "sequenceDiagram; A->>B: Message;"}\n```',
            {"type": "sequence", "description": "A sequence diagram", "mermaid": "sequenceDiagram; A->>B: Message;"},
        ),
        # Case 3: Invalid content (non-JSON)
        (
            "This is not a JSON object.",
            {"type": "", "description": "", "mermaid": ""},
        ),
        # Case 4: Malformed JSON
        (
            '{"type": "flowchart", "description": "A simple flowchart", "mermaid": "graph TD; A-->B;',
            {"type": "", "description": "", "mermaid": ""},
        ),
    ],
)
@patch("app.openai.ChatCompletion.create")
def test_diagram_from_text(mock_create, api_response, expected_output):
    """Test the diagram_from_text function with various API responses."""
    # Configure the mock to return the desired response
    mock_create.return_value = MockResponse(api_response)

    # Call the function with some dummy text
    result = diagram_from_text("some text")

    # Assert that the result is as expected
    assert result == expected_output
