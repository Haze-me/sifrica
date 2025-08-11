import pytest
from modules.hashing.hashing import hash_password, verify_password

def test_hash_and_verify_password():
    password = "myS3cretP@ss"
    wrong_password = "notMyS3cretP@ss"

    hashed_password = hash_password(password)

    # Hash should not be None or empty
    assert hashed_password, "Hash should not be empty"

    # Hash should not be equal to plaintext
    assert hashed_password != password, "Hash should not be the same as the plaintext password"

    # Verifying the correct password should return True
    assert verify_password(hashed_password, password) == True, "Correct password should verify successfully"

    # Verifying an incorrect password should return False
    assert verify_password(hashed_password, wrong_password) == False, "Incorrect password should fail verification"

    # Ensure hashes are unique due to salting
    another_hashed_password = hash_password(password)
    assert hashed_password != another_hashed_password, "Hashes of the same password should differ due to salting"
    # Both should still verify correctly
    assert verify_password(another_hashed_password, password) == True, "Second hash should verify with the password"

if __name__ == "__main__":
    pytest.main()
