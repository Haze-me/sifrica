"""
Campaign model: Represents a marketing campaign with a name, description, and duration.
"""

from sqlalchemy import Column, String, Date,Boolean
from sqlalchemy.orm import relationship
from database.config.base import Base
from models.db.talent_campaighn_association import TalentCampaighnAssosiatonTable
from sqlalchemy.dialects.postgresql import UUID
import uuid

class CampaignModel(Base):
    __tablename__ = "campaigns_table"


    id = Column(UUID(as_uuid=True), primary_key=True, index=True,default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(String)
    active = Column(Boolean)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    talents = relationship(
        "models.db.talent_model.TalentModel",
        secondary=TalentCampaighnAssosiatonTable,
        back_populates="campaighns"
    )

    def __repr__(self):
        return f"<Campaign(id={self.id}, name='{self.name}')>"
