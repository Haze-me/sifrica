import bcrypt



def hash_password(password: str = "") -> str:
    """
    Hash a plaintext password using bcrypt with automatic salting.
    """
    return bcrypt.hashpw(password=password.encode(),salt=bcrypt.gensalt()).decode()

def verify_password(stored_passwprd_hash:str,password: str = "") -> bool:
    """
    Verify a plaintext password against the stored hashed password.
    """
    return bcrypt.checkpw(password=password.encode(),hashed_password=stored_passwprd_hash.encode())
