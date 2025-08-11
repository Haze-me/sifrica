from fastapi import APIRouter, Depends, Query
from modules.middleware.middleware import jwt_token_dependecy
from models.api import (
    StandardMessageResponse,
    SuccessResponse,
    InfoResponse,
    FailureResponse
)
from models.api.api_responses import *
from models.api.api_requests import *
from database.db_functions import talent_functions
from models.enums import MessageTypeEnum, TalentLevelEnum


# -------------------- ROUTER --------------------
talent_router = APIRouter(
    prefix="/talents",
    redirect_slashes=True,
    dependencies=[Depends(jwt_token_dependecy)]
)


# -------------------- GET with search --------------------
@talent_router.get(
    "/",
    response_model=StandardMessageResponse[TalentListResponse],
    name="Search talents",
    summary="Search and paginate talents",
    description="""
Search by first name, last name, phone, email, age, or level. Supports pagination via `count` and `page` query params.
"""
)
def get_talents(
    unique_id: int = Query(None),
    first_name: str = Query(None),
    last_name: str = Query(None),
    phone: str = Query(None),
    email: str = Query(None),
    school: str = Query(None),
    active: bool = Query(None),
    count: int = 20,
    page: int = 1
):
    talents = talent_functions.get_talents(
        unique_id=unique_id,
        page= page,page_size= count,
        first_name=first_name,
        last_name=last_name,
        phone=phone,
        email=email,
        is_active=active,
        school=school,
    )

    return StandardMessageResponse(
        message_type=MessageTypeEnum.SUCCESS,
        text="Talents fetched successfully",
        data= talents,
        )


# -------------------- POST to create --------------------
@talent_router.post(
    "/",
    response_model=StandardMessageResponse[TalentResponse],
    name="Create a talent"
)
def create_talent(talent_data: TalentCreateRequest ):

    talent = talent_functions.create_talent(
    firstname=talent_data.first_name,
    lastname=talent_data.last_name,
    age=talent_data.age,
    level=talent_data.level,
    gender=talent_data.gender,
    phone=talent_data.phone,
    geozone=talent_data.geozone,
    email =talent_data.email,
    school=talent_data.school,
    active= talent_data.active
    )
    return SuccessResponse(
        text="Talent created successfully",
        data=talent
    )

@talent_router.post(
    "/{talent_id}/campaigns/{campaign_id}/link",
    response_model=StandardMessageResponse,
    name="Link talent to campaign"
)
def link_talent_to_campaign(talent_id: int, campaign_id: int):
    updated = talent_functions.link_talent_to_campaign(talent_id, campaign_id)
    return SuccessResponse(
        text="Talent linked to campaign successfully",
        data=updated
    )



# -------------------- PATCH to update and assign campaign --------------------
@talent_router.patch(
    "/{talent_id}",
    response_model=StandardMessageResponse,
    name="Update a talent and assign campaign"
)
def update_talent_by_id(talent_id: int, data: TalentUpdateRequest):
    updated_talent = talent_functions.update_talent(talent_id, **data.dict(exclude_unset=True))
    return SuccessResponse(
        text="Talent updated successfully",
        data= updated_talent
    )


# -------------------- DELETE --------------------
@talent_router.delete(
    "/{talent_id}",
    response_model=SuccessResponse,
    name="Delete a talent"
)
def delete_talent_by_id(talent_id: int):
    talent_functions.delete_talent(talent_id)
    return SuccessResponse(
        text="Talent deleted successfully",
        data=None
    )
