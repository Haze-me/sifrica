import pytest
from datetime import datetime, timedelta, timezone
from modules.middleware.token import GenerateJWT, VerifyJWT
from modules.middleware import JsonWebToken  # adjust import to your structure

def test_generate_and_verify_jwt_valid():
    payload = JsonWebToken(
        user_id="user_123",
        email="user@example.com",
        exp=datetime.now(timezone.utc) + timedelta(minutes=5),
        roles=["admin", "editor"]
    )

    token = GenerateJWT(payload)
    assert isinstance(token, str) and len(token) > 0, "Generated token should be a non-empty string"

    result = VerifyJWT(token)
    assert result["error"] is None, "Valid JWT should not produce an error"
    decoded_payload = result["payload"]

    assert decoded_payload["user_id"] == payload.user_id
    assert decoded_payload["email"] == payload.email
    assert decoded_payload["roles"] == payload.roles
    assert isinstance(decoded_payload["exp"], int), "'exp' should be integer epoch"

def test_verify_jwt_expired():
    expired_payload = JsonWebToken(
        user_id="expired_user",
        email="expired@example.com",
        exp=datetime.now() - timedelta(minutes=1),
        roles=["viewer"]
    )

    token = GenerateJWT(expired_payload)
    result = VerifyJWT(token)
    assert result["error"] == "expired token", "Should detect expired token"
    assert result["payload"] is None, "Payload should be None when token expired"

def test_verify_jwt_invalid():
    invalid_token = "this.is.not.a.valid.token"
    result = VerifyJWT(invalid_token)
    assert result["error"] == "invalid token", "Should detect invalid token"
    assert result["payload"] is None, "Payload should be None for invalid token"

if __name__ == "__main__":
    pytest.main()
