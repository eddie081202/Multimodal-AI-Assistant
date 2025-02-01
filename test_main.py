from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ask_endpoint():
    # Test text-only query
    response = client.post(
        "/ask",
        json={"query": "What is machine learning?"}
    )
    assert response.status_code == 200
    assert "machine learning" in response.json()["answer"].lower()
