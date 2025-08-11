from fastapi import Request, HTTPException
from modules.middleware.token import VerifyJWT

class JsonWebTokenAuthDependency:
    def __init__(self):
        pass

    def __call__(self, request: Request):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Missing or invalid Authorization header")

        token = auth_header.split(" ")[1]
        payload = VerifyJWT(token_string=token)

        # Validate BEFORE accessing 'payload'
        if "error" in payload:
            if payload["error"] == "expired token":
                raise HTTPException(status_code=401, detail="Expired Token")
            if payload["error"] == "invalid token":
                raise HTTPException(status_code=401, detail="Invalid Token")    


        # Now it is safe to access
        request.state.user = payload["payload"]

jwt_token_dependecy = JsonWebTokenAuthDependency()
