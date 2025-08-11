from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Optional

from modules.middleware.middleware import jwt_token_dependecy
from models.enums import MessageTypeEnum

from models.api.api_responses import StandardMessageResponse
from models.api.api_responses import (
    CampaignResponse,
    PaginatedCampaignResponse
)
from models.api.api_requests import CampaignCreateRequest, CampaignUpdateRequest
from database.db_functions.campaighn_functions import (
    get_all_campaigns_paginated,
    get_campaign_by_id,
    create_campaign,
    update_campaign,
    delete_campaign
)

campaign_router = APIRouter(
    prefix="/campaigns",
    redirect_slashes=True,
    dependencies=[Depends(jwt_token_dependecy)]
)

@campaign_router.get(
    "/",
    response_model=StandardMessageResponse[PaginatedCampaignResponse],
    name="Get the campaigns",
    summary="Retrieve a paginated list of campaigns with optional filters",
    description="""
You can control pagination with `count` (max: 30) and `page`.
Filtering options:
- `name`: fuzzy search by campaign name
- `active`: filter by active status

Example:
- `/campaigns?count=20&page=2&name=summer&active=true`
"""
)
def get_campaigns(
    count: int = Query(20, ge=1, le=30),
    page: int = Query(1, ge=1),
    name: Optional[str] = Query(None, description="Fuzzy match for campaign name"),
    active: Optional[bool] = Query(None, description="Filter by active status")
):
    paginated_campaigns = get_all_campaigns_paginated(
        page=page,
        page_size=count,
        name=name,
        active=active
    )
    return StandardMessageResponse(
        message_type=MessageTypeEnum.SUCCESS,
        text="Campaigns retrieved successfully",
        data=paginated_campaigns
    )

@campaign_router.post(
    "/",
    response_model=StandardMessageResponse[CampaignResponse],
    summary="Create a new campaign"
)
def create_campaign_route(payload: CampaignCreateRequest):
    campaign = create_campaign(**payload.dict())
    if not campaign:
        raise HTTPException(status_code=500, detail="Campaign creation failed")
    return StandardMessageResponse(
        message_type=MessageTypeEnum.SUCCESS,
        text="Campaign created successfully",
        data=campaign
    )

@campaign_router.get(
    "/{campaign_id}",
    response_model=StandardMessageResponse[CampaignResponse],
    summary="Get a campaign by ID"
)
def get_campaign_by_id_route(campaign_id: int):
    campaign = get_campaign_by_id(campaign_id)
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return StandardMessageResponse(
        message_type=MessageTypeEnum.SUCCESS,
        text="Campaign found",
        data=campaign
    )

@campaign_router.patch(
    "/{campaign_id}",
    response_model=StandardMessageResponse[CampaignResponse],
    summary="Update a campaign"
)
def update_campaign_by_id(campaign_id: int, payload: CampaignUpdateRequest):
    campaign = update_campaign(campaign_id, **payload.dict(exclude_unset=True))
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found or update failed")
    return StandardMessageResponse(
        message_type=MessageTypeEnum.SUCCESS,
        text="Campaign updated successfully",
        data=campaign
    )

@campaign_router.delete(
    "/{campaign_id}",
    response_model=StandardMessageResponse,
    summary="Delete a campaign"
)
def delete_campaign_by_id(campaign_id: int):
    success = delete_campaign(campaign_id)
    if not success:
        raise HTTPException(status_code=404, detail="Campaign not found or delete failed")
    return StandardMessageResponse(
        message_type=MessageTypeEnum.SUCCESS,
        text="Campaign deleted successfully",
        data=None
    )
