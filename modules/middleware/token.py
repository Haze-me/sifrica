import jwt
from jwt import ExpiredSignatureError,InvalidTokenError
import dotenv
import os
from modules.middleware import JsonWebToken
dotenv.load_dotenv()


JWT_SECRET_KEY = str(os.getenv("JWT_SECRET_STRING"))
ALGORITHM = "HS256"

def GenerateJWT(payload: JsonWebToken) -> str:
    payload_dict = payload.model_dump()
    payload_dict["exp"] = int(payload_dict["exp"].timestamp())  # convert datetime -> epoch
    token = jwt.encode(payload=payload_dict, key=JWT_SECRET_KEY, algorithm=ALGORITHM)
    return token


def VerifyJWT(token_string:str) -> dict:
    try:
        decoded_token = jwt.decode(jwt=token_string,key=JWT_SECRET_KEY,algorithms=[ALGORITHM])
        return {"payload":decoded_token,"error":None}
    except ExpiredSignatureError:
        return { "payload":None, "error":"expired token"}

    except InvalidTokenError:
        return { "payload":None, "error":"invalid token"}
