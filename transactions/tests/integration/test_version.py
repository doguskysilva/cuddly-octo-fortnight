from fastapi.testclient import TestClient


def test_get_version(client: TestClient):
    response = client.get("/version")
    assert response.json() == {"service": "transactions", "version": "0.0.1"}
