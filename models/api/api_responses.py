from typing import Generic, TypeVar, Optional,List
from pydantic import BaseModel, Field, ConfigDict
from models.enums import MessageTypeEnum,TalentLevelEnum,GeoZoneEnum,GenderEnum
from datetime import datetime
from uuid import UUID
T = TypeVar("T")

class StandardMessageResponse(BaseModel, Generic[T]):
    """
    Generic standard response model for consistent API output across your FastAPI app.

    Use this in your `response_model=` for endpoints to ensure:
    - Consistent response structure across your API.
    - Frontend knows exactly what to expect.
    - Easy validation, testing, and documentation.

    {
        "message_type":"sucesss",
        "text":"login successful"
        "data": {
            ""
        }
    }

    Attributes:
        message_type: Enum value indicating success, failure, warning, or info.
        message_text: Human-readable descriptive message.
        data: Optional payload of any type (dict, list, nested Pydantic model).
    """

    message_type: MessageTypeEnum = Field(..., alias="message_type")
    message_text: str = Field(..., alias="text")
    data: Optional[T] = Field(None, alias="data")

    model_config = ConfigDict(populate_by_name=True)




class JsonWebTokenResponse(BaseModel):
    """
    Response model for returning JWTs in a consistent, documented structure.

    Attributes:
        token_string: The JWT string itself.
    Use in `StandardMessageResponse[JsonWebTokenResponse]` for clean, consistent JWT responses.
    """

    token_string: str = Field(..., alias="token_string")

    model_config = ConfigDict(populate_by_name=True)



class UserResponse(BaseModel):
    """
    Response model for returning user data cleanly from your API.

    Attributes:
        user_id: Unique user identifier (UUID or string).
        username: User's username.
        first_name: User's first name.
        last_name: User's last name.
        roles: List of user's roles.

    Use this when sending user data back to the frontend so you don't return ORM objects directly.
    """

    user_id: UUID = Field(..., alias="user_id")
    username: str = Field(..., alias="username")
    first_name: str = Field(..., alias="first_name")
    last_name: str = Field(..., alias="last_name")
    roles: list[Optional[str]] = Field(default_factory=list, alias="roles")

    model_config = ConfigDict(populate_by_name=True)



class CampaignResponse(BaseModel):
    """
    Response model for returning a single campaign.
    """
    id: UUID
    name: str
    description: Optional[str]
    start_date: datetime
    end_date:datetime
    active: bool
    class Config:

        from_attributes = True






class PaginatedCampaignResponse(BaseModel):
    """
    Response model for listing campaigns with pagination.
    """
    total: int
    page: int
    size: int
    campaigns: List[CampaignResponse]


class CampaignAssignedTalentResponse(BaseModel):
    """
    Talent assigned to a campaign.
    """
    talent_id: UUID
    full_name: str
    email: Optional[str]
    phone: Optional[str]
    school:str
    gender: GenderEnum
    geozone:GeoZoneEnum
    active:bool
    level:TalentLevelEnum

    class Config:
            from_attributes = True


class CampaignWithTalentsResponse(BaseModel):
    """
    Response for a campaign with its assigned talents.
    """
    id: UUID
    name: str
    active: bool
    talents: List[CampaignAssignedTalentResponse]





class TalentResponse(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    age: int
    school: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    gender: GenderEnum
    level: TalentLevelEnum
    geozone: GeoZoneEnum
    active: Optional[bool] = False
    campaighns: Optional[List[CampaignResponse]] = Field(default_factory=list)

    class Config:
        from_attributes = True


class TalentListResponse(BaseModel):
    """
    Paginated list response for talents.
    """
    items: List[TalentResponse]
    total: int
    page: int
    size: int
