"""
Talent model: Represents a social media influencer or content creator assigned to a campaign.
"""

from sqlalchemy import Column, Integer, String, Enum,Boolean
from sqlalchemy.orm import validates,relationship
from database.config.base import Base
from models.enums import TalentLevelEnum,GeoZoneEnum,GenderEnum
import re
from models.db.talent_campaighn_association import TalentCampaighnAssosiatonTable
from sqlalchemy.dialects.postgresql import UUID
import uuid

class TalentModel(Base):
    __tablename__ = "talents_table"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True,default=uuid.uuid4)
    first_name = Column(String, nullable=False)
    last_name = Column(String,nullable=False)
    age = Column(Integer,nullable=False)
    school= Column(String,nullable=True)
    level = Column(Enum(TalentLevelEnum),nullable=False,default=TalentLevelEnum.LEVEL_100)
    email = Column(String, unique=True, nullable=False)
    gender = Column(Enum(GenderEnum),nullable=False, default=GenderEnum.MALE)
    phone = Column(String)
    geozone = Column(Enum(GeoZoneEnum),nullable = False, default= GeoZoneEnum.SE)
    active = Column(Boolean)
    campaighns = relationship(
        "models.db.campaighn_model.CampaignModel",
        secondary=TalentCampaighnAssosiatonTable,
        back_populates="talents"
    )



    @validates('phone')
    def validate_phone_number(self, key, number):
        # Strip spaces, dashes, etc.
        number = re.sub(r'\D', '', number)

        if number.startswith('0') and len(number) == 11:
            # Convert local to international
            number = '+234' + number[1:]

        elif number.startswith('234') and len(number) == 13:
            number = '+' + number

        elif number.startswith('+234') and len(number) == 14:
            pass  # already in correct format

        else:
            raise ValueError("Invalid Nigerian phone number format")

    def __repr__(self):
        return f"<Talent(id={self.id}, name='{self.first_name} {self.last_name}')>"
