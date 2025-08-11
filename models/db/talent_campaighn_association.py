from database.config.base import Base
from sqlalchemy import Column,ForeignKey,Table

TalentCampaighnAssosiatonTable = Table(
"talent_campaighn",
Base.metadata,
Column("talent_id",ForeignKey('talents_table.id',ondelete='CASCADE'),primary_key=True),
 Column("campaighn_id",ForeignKey('campaigns_table.id',ondelete='CASCADE'),primary_key=True),
)

class TalentCampaignAssociation(Base):
    __table__ = TalentCampaighnAssosiatonTable
