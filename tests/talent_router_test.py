import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_talents():
    response = client.get("/talents/")
    assert response.status_code == 200
    assert "data" in response.json()

def test_create_talent():
    payload = {
        "first_name": "John",
        "last_name": "Doe",
        "age": 22,
        "school": "Test University",
        "level": "LEVEL_100",
        "email": "john.doe@example.com",
        "gender": "MALE",
        "phone": "08012345678",
        "geozone": "SE",
        "active": True
    }
    response = client.post("/talents/", json=payload)
    assert response.status_code == 200
    assert response.json()["text"] == "Talent created successfully"

def test_link_talent_to_campaign():
    # These IDs should exist in your test DB or be mocked
    talent_id = 1
    campaign_id = 1
    response = client.post(f"/talents/{talent_id}/campaigns/{campaign_id}/link")
    assert response.status_code == 200
    assert response.json()["text"] == "Talent linked to campaign successfully"

def test_update_talent_by_id():
    talent_id = 1
    payload = {"first_name": "Jane"}
    response = client.patch(f"/talents/{talent_id}", json=payload)
    assert response.status_code == 200
    assert response.json()["text"] == "Talent updated successfully"

def test_delete_talent_by_id():
    talent_id = 1
    response = client.delete(f"/talents/{talent_id}")
    assert response.status_code == 200
    assert response.json()["text"] == "Talent deleted successfully"
