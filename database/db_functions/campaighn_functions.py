from models.api.api_responses import PaginatedCampaignResponse,CampaignResponse
from database.config import CampaignModel
from database.config.engine import SessionLocal
from typing import List, Optional
from uuid import UUID

# Shared pagination utility
def paginate_query(query, page: int = 1, page_size: int = 10):
    return query.offset((page - 1) * page_size).limit(page_size).all()

# ----------------------------
# CAMPAIGN HELPERS
# ----------------------------
def get_campaign_by_id(campaign_id: UUID) -> Optional[CampaignModel]:
    session = SessionLocal()
    try:
        return session.query(CampaignModel).filter_by(id=campaign_id).first()
    finally:
        session.close()

def get_campaigns_by_name_fuzzy(name: str, page: int = 1, page_size: int = 10) -> List[CampaignModel]:
    session = SessionLocal()
    try:
        query = session.query(CampaignModel).filter(CampaignModel.name.ilike(f"%{name}%"))
        return paginate_query(query, page, page_size)
    finally:
        session.close()

def get_campaigns_by_active_status(active: bool, page: int = 1, page_size: int = 10) -> List[CampaignModel]:
    session = SessionLocal()
    try:
        query = session.query(CampaignModel).filter(CampaignModel.active == active)
        return paginate_query(query, page, page_size)
    finally:
        session.close()

def get_all_campaigns_paginated(
    page: int = 1,
    page_size: int = 10,
    name: Optional[str] = None,
    active: Optional[bool] = None
):
    session = SessionLocal()
    try:
        query = session.query(CampaignModel)

        if name:
            query = query.filter(CampaignModel.name.ilike(f"%{name}%"))
        if active is not None:
            query = query.filter(CampaignModel.active == active)

        total = query.count()
        items = paginate_query(query, page, page_size)
        campaigns = [CampaignResponse.from_orm(item) for item in items]
        return PaginatedCampaignResponse(
            total=total,
            page=page,
            size=page_size,
            campaigns=campaigns
        )
    finally:
        session.close()

def create_campaign(
    name: str,
    description: str,
    start_date,
    end_date,
    active: bool = True
) -> Optional[CampaignModel]:
    session = SessionLocal()
    new_campaign = CampaignModel(
        name=name,
        description=description,
        start_date=start_date,
        end_date=end_date,
        active=active
    )
    session.add(new_campaign)
    try:
        session.commit()
        session.refresh(new_campaign)
        return new_campaign
    except Exception as e:
        session.rollback()
        print(f"Error creating campaign: {e}")
        return None
    finally:
        session.close()

def update_campaign(campaign_id: int, **fields) -> Optional[CampaignModel]:
    session = SessionLocal()
    try:
        campaign = session.query(CampaignModel).filter_by(id=campaign_id).first()
        if not campaign:
            return None
        for key, value in fields.items():
            setattr(campaign, key, value)
        session.commit()
        session.refresh(campaign)
        return campaign
    except Exception as e:
        session.rollback()
        print(f"Error updating campaign: {e}")
        return None
    finally:
        session.close()

def delete_campaign(campaign_id: int) -> bool:
    session = SessionLocal()
    try:
        campaign = session.query(CampaignModel).filter_by(id=campaign_id).first()
        if not campaign:
            return False
        session.delete(campaign)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"Error deleting campaign: {e}")
        return False
    finally:
        session.close()

def get_talents_assigned_to_campaign(campaign_id: int, page: int = 1, page_size: int = 10):
    session = SessionLocal()
    try:
        campaign = session.query(CampaignModel).filter_by(id=campaign_id).first()
        if not campaign:
            return []
        return campaign.talents[(page - 1) * page_size : page * page_size]
    finally:
        session.close()
