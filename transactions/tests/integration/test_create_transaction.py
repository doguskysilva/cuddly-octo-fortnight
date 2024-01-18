from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from src import repository


def test_create_transaction(client: TestClient, get_database_override: Session):
    payload = {
        "customer_id": "a80fdc63-d71f-4a4e-a697-f607b940c0ae",
        "amount": 42.00,
        "origin": "app",
    }

    response = client.post("/transactions", json=payload)
    transaction = response.json()

    # assert response
    assert response.status_code == 201
    assert "id" in transaction
    assert transaction["customer_id"] == payload["customer_id"]
    assert transaction["origin"] == payload["origin"]
    assert transaction["amount"] == payload["amount"]
    assert transaction["status"] == "in_progress"

    # assert database
    assert (
        repository.transaction_by_id(transaction["id"], get_database_override) != None
    )
