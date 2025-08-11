"""
Performance model: Represents daily metrics (impressions and clicks) for a talent on a specific day.
"""

from sqlalchemy import Column, Integer, Date, ForeignKeyConstraint,and_
from sqlalchemy.orm import relationship,foreign
from database.config.base import Base
from models.db.talent_campaighn_association import TalentCampaighnAssosiatonTable,TalentCampaignAssociation
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid
class Performance(Base):
    __tablename__ = "performances"

    id = Column(UUID(as_uuid=True), primary_key=True,unique=True,default=uuid.uuid4)
    talent_id = Column(UUID(as_uuid=True), nullable=False)
    campaighn_id = Column(UUID(as_uuid=True), nullable=False)
    impressions = Column(Integer, default=0)
    clicks = Column(Integer, default=0)
    date = Column(Date,default=datetime.now())

    # Set up a foreign key constraint to the association table
    __table_args__ = (
        ForeignKeyConstraint(
            ["talent_id", "campaighn_id"],
            [TalentCampaighnAssosiatonTable.c.talent_id, TalentCampaighnAssosiatonTable.c.campaighn_id],
            ondelete="CASCADE"
        ),
    )

    # Optional: create relationship to the association row
    talent_campaign_link = relationship(
        TalentCampaignAssociation,
        primaryjoin=and_(
            talent_id == foreign(TalentCampaighnAssosiatonTable.c.talent_id),
            campaighn_id == foreign(TalentCampaighnAssosiatonTable.c.campaighn_id),
        ),
        viewonly=True,
        uselist=False,
    )

    def __repr__(self):
        return f"<Performance(id={self.id}, date={self.date}, clicks={self.clicks})>"
