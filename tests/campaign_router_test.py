import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_campaigns():
    response = client.get("/campaigns/")
    assert response.status_code == 200
    assert "data" in response.json()

def test_create_campaign():
    payload = {
        "name": "Test Campaign",
        "description": "A test campaign.",
        "start_date": "2025-07-01",
        "end_date": "2025-08-01",
        # Add other required fields as per your Campaign model
    }
    response = client.post("/campaigns/", json=payload)
    assert response.status_code == 200
    assert "created" in response.json()["text"].lower()

def test_update_campaign_by_id():
    campaign_id = 1
    payload = {"name": "Updated Campaign"}
    response = client.patch(f"/campaigns/{campaign_id}", json=payload)
    assert response.status_code == 200
    assert "updated" in response.json()["text"].lower()

def test_delete_campaign_by_id():
    campaign_id = 1
    response = client.delete(f"/campaigns/{campaign_id}")
    assert response.status_code == 200
    assert "deleted" in response.json()["text"].lower()
