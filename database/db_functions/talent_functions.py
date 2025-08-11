from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import or_
from database.config.engine import SessionLocal
from models.db.talent_model import TalentModel
from models.db.campaighn_model import CampaignModel
from models.api.api_responses import *
from models.enums import *
from uuid import UUID

# -------------------- Utility --------------------

def paginate_query(query, page: int = 1, page_size: int = 10):
    return query.offset((page - 1) * page_size).limit(page_size).all()

# -------------------- Create --------------------

def create_talent(
    firstname: str,
    lastname: str,
    age: int,
    level: TalentLevelEnum,
    email: str,
    gender: GenderEnum,
    phone: str,
    geozone:GeoZoneEnum,
    school: str,
    active:bool = False
    ):
    session = SessionLocal()
    try:
        new_talent = TalentModel(
            first_name=firstname,
            last_name=lastname,
            age=age,
            level=level,
            email=email,
            gender=gender,
            phone=phone,
            geozone=geozone,
            school=school,
            active=active ,
        )
        session.add(new_talent)
        session.commit()
        session.refresh(new_talent)
        return TalentResponse.from_orm(new_talent)
    except SQLAlchemyError as e:
        session.rollback()
        print(f"DB Error: {e}")
        return None
    finally:
        session.close()

# -------------------- Get One --------------------

def get_talent_by_id(talent_id: int):
    with SessionLocal() as session:
        return session.query(TalentModel).filter_by(id=talent_id).first()



def get_talents(
    unique_id:UUID,
    email: str = None,
    phone: str = None,
    first_name: str = None,
    last_name: str = None,
    school: str = None,
    is_active: bool = None,
    page: int = 1,
    page_size: int = 10,
) -> TalentListResponse:
    with SessionLocal() as session:
        query = session.query(TalentModel)

        if unique_id is not None:
            query = query.filter(TalentModel.id == unique_id)
        if email is not None:
            query = query.filter(TalentModel.email == email)
        if phone is not None:
            query = query.filter(TalentModel.phone == phone)
        if first_name is not None:
            query = query.filter(TalentModel.first_name.ilike(f"%{first_name}%"))
        if last_name is not None:
            query = query.filter(TalentModel.last_name.ilike(f"%{last_name}%"))
        if school is not None:
            query = query.filter(TalentModel.school.ilike(f"%{school}%"))
        if is_active is not None:
            query = query.filter(TalentModel.active == is_active)

        total = query.count()

        items = (
            query
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )

        return TalentListResponse(
            total=total,
            page=page,
            size=page_size,
            items=[TalentResponse.from_orm(t) for t in items]
        )




# -------------------- Update --------------------

def update_talent(talent_id: UUID, **kwargs):

    with SessionLocal() as session:
        talent = session.query(TalentModel).filter_by(id=talent_id).first()
        if not talent:
            return None
        for key, value in kwargs.items():
            if hasattr(talent, key):
                setattr(talent, key, value)
        try:
            session.commit()
            session.refresh(talent)

            return TalentResponse.from_orm(talent)
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Failed to update talent: {e}")
            return None

# -------------------- Link to Campaign --------------------

def link_talent_to_campaign(talent_id: UUID, campaign_id: int):
    with SessionLocal() as session:
        talent = session.query(TalentModel).filter_by(id=talent_id).first()
        campaign = session.query(CampaignModel).filter_by(id=campaign_id).first()
        if not talent or not campaign:
            return False
        if campaign not in talent.campaighns:
            talent.campaighns.append(campaign)
        try:
            session.commit()
            return True
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Failed to link talent to campaign: {e}")
            return False

# -------------------- Delete --------------------

def delete_talent(talent_id: UUID):
    with SessionLocal() as session:
        talent = session.query(TalentModel).filter_by(id=talent_id).first()
        if not talent:
            return False
        session.delete(talent)
        try:
            session.commit()
            return True
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Failed to delete talent: {e}")
            return False
def get_campaigns_assigned_to_talent(talent_id: UUID, page: int = 1, page_size: int = 10):
    session = SessionLocal()
    try:
        talent = session.query(TalentModel).filter_by(id=talent_id).first()
        if not talent:
            return PaginatedCampaignResponse(total=0, page=page, size=page_size, campaigns=[])

        total = len(talent.campaighns)
        campaigns = talent.campaighns[(page - 1) * page_size : page * page_size]

        return PaginatedCampaignResponse(
            total=total,
            page=page,
            size=page_size,
            campaigns=[CampaignResponse.from_orm(c) for c in campaigns]
        )
    finally:
        session.close()
