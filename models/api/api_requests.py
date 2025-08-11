from typing import Optional,List
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from models.enums import *
from uuid import UUID

class UserLoginRequest(BaseModel):
    """
    Schema for user login requests.

    - Ensures the frontend sends the expected fields.
    - Automatically generates docs in the FastAPI swagger UI.
    - If the frontend devs complain 'API is broken', tell them to read the docs first.
    """

    username: str = Field(..., alias="username")
    password: str = Field(..., alias="password")

    model_config = ConfigDict(populate_by_name=True)



class UserSignupRequest(BaseModel):
    """
    Schema for user signup requests.

    - Same benefits as the login schema.
    - If someone breaks their implementation, it's not your fault.
    - Validates incoming data cleanly before hitting your business logic.
    """

    username: str = Field(..., alias="username")
    password: str = Field(..., alias="password")
    email: str = Field(..., alias="email")
    first_name: Optional[str] = Field(None, alias="first_name")
    last_name: Optional[str] = Field(None, alias="last_name")

    model_config = ConfigDict(populate_by_name=True)


class UserUpdateRequest(BaseModel):
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
    user_id :UUID = Field(alias="user_id")
    username: Optional[str] = Field(None, alias="username")
    first_name: Optional[str] = Field(None, alias="first_name")
    last_name: Optional[str] = Field(None, alias="last_name")
    email: Optional[str] = Field(None, alias="email")
    password: Optional[str] = Field(None, alias="password")
    roles: Optional[List[Optional[str]]] = Field(default=None, alias="roles")

    model_config = ConfigDict(populate_by_name=True)


class CampaignCreateRequest(BaseModel):
    name: str = Field(..., alias="name")
    description: Optional[str] = Field(None, alias="description")
    start_date: datetime = Field(...,alias="start_date")
    end_date: datetime = Field(...,alias="end_date")
    active: bool = Field(default=True, alias="active")


class CampaignUpdateRequest(BaseModel):
    name: Optional[str] = Field(None, alias="name")
    description: Optional[str] = Field(None, alias="description")
    active: Optional[bool] = Field(None, alias="active")

class CampaignAssignTalentsRequest(BaseModel):
    talent_ids: list[int] = Field(..., alias="talent_ids")

class TalentCreateRequest(BaseModel):
    first_name: str = Field(..., alias="first_name")
    last_name: str = Field(..., alias="last_name")
    email: str = Field(..., alias="email")  # Required
    phone: str = Field(..., alias="phone")  # Required
    age: int = Field(..., alias="age")
    gender: GenderEnum = Field(..., alias="gender")
    level: TalentLevelEnum = Field(..., alias="level")
    geozone: GeoZoneEnum = Field(..., alias="geozone")
    school: str = Field(..., alias="school")
    active:bool = Field(...,alias="active")


class TalentUpdateRequest(BaseModel):
    first_name: Optional[str] = Field(None, alias="first_name")
    last_name: Optional[str] = Field(None, alias="last_name")
    email: Optional[str] = Field(None, alias="email")
    phone: Optional[str] = Field(None, alias="phone")
    age: Optional[int] = Field(None, alias="age")
    gender: Optional[GenderEnum] = Field(None, alias="gender")
    level: Optional[TalentLevelEnum] = Field(None, alias="level")
    geozone: Optional[GeoZoneEnum] = Field(None, alias="geozone")
    school: Optional[str] = Field(None, alias="school")
    active: Optional[bool] = Field(None, alias="active")


class TalentAssignCampaignsRequest(BaseModel):
    campaign_ids: list[UUID] = Field(..., alias="campaign_ids")
