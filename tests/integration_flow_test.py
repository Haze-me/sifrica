
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_signup_login_create_talent_campaign_and_link():
    # 1. Signup
    signup_payload = {
        "username": "testuser1",
        "email": "testuser1@example.com",
        "password": "TestPassword123!"
    }
    signup_response = client.post("/auth/signup", json=signup_payload)
    assert signup_response.status_code == 200
    # 2. Login
    login_payload = {
        "username": "testuser1",
        "password": "TestPassword123!"
    }
    login_response = client.post("/auth/login", data=login_payload)
    assert login_response.status_code == 200
    token = login_response.json().get("access_token")
    assert token
    headers = {"Authorization": f"Bearer {token}"}
    # 3. Create Talent
    talent_payload = {
        "first_name": "Jane",
        "last_name": "Smith",
        "age": 23,
        "school": "Test School",
        "level": "LEVEL_100",
        "email": "jane.smith@example.com",
        "gender": "FEMALE",
        "phone": "08012345679",
        "geozone": "SE",
        "active": True
    }
    talent_response = client.post("/talents/", json=talent_payload, headers=headers)
    assert talent_response.status_code == 200
    talent_id = talent_response.json()["data"]["id"]
    # 4. Create Campaign
    campaign_payload = {
        "name": "Integration Test Campaign",
        "description": "A campaign for integration testing.",
        "start_date": "2025-07-01",
        "end_date": "2025-08-01"
        # Add other required fields as per your Campaign model
    }
    campaign_response = client.post("/campaigns/", json=campaign_payload, headers=headers)
    assert campaign_response.status_code == 200
    campaign_id = campaign_response.json()["data"]["id"]
    # 5. Link Campaign to Talent
    link_response = client.post(f"/talents/{talent_id}/campaigns/{campaign_id}/link", headers=headers)
    assert link_response.status_code == 200
    assert "linked" in link_response.json()["text"].lower()
