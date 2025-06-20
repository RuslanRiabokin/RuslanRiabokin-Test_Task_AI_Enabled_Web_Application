import sys
import os
from main import app
from fastapi.testclient import TestClient
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

client = TestClient(app)


def test_post_api_ask_success():
    """
        Test that the /api/ask endpoint returns a valid JSON
        response with an 'answer' field for a known question.
        """
    response = client.post("/api/ask", json={"question": "Що таке API?"})
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert isinstance(data["answer"], str)
