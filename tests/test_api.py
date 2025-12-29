from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_summarize_api():
    payload = {
        "text": "These terms apply to users.",
        "url": None,
        "summary_type": "simple"
    }

    response = client.post("/api/summarize", json=payload)

    assert response.status_code == 200
    assert "summary" in response.json()
    assert "key_points" in response.json()
    assert "risk_notes" in response.json()

