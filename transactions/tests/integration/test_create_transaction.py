from fastapi.testclient import TestClient

def test_create_transaction(client: TestClient):
    payload = {
        "customer_id": "a80fdc63-d71f-4a4e-a697-f607b940c0ae",
        "amount": 42.00,
        "origin": "app"
    }

    response = client.post("/transactions", json=payload)

    assert response.status_code == 201
    assert response.json() == None
