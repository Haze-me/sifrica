from typing import Optional,List
from datetime import datetime,timedelta
from pydantic import BaseModel, Field, ConfigDict



class JsonWebToken(BaseModel):
    """
    The payload to be encoded in the response

    Attributes:
        token_string: The JWT string itself.
        expiry: Epoch timestamp indicating token expiration.
        roles: List of roles associated with the user (optional strings).

    Use in `StandardMessageResponse[JsonWebTokenResponse]` for clean, consistent JWT responses.
    """

    user_id:str = Field(...,alias="user_id")
    email:str = Field(...,alias="email")
    exp: datetime = Field(alias="exp",default_factory=lambda:datetime.now() + timedelta(days=28))
    roles: List[Optional[str]] = Field(default_factory=list, alias="roles")

    model_config = ConfigDict(populate_by_name=True)
