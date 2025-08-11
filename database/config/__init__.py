"""
This is the file to make sure the setu the schema

The imports may seem useles but sqlalchemy uses them to
create the schema.
If you watn ta add a table define in the models/db folder
and add the import as shown below

"""

from models.db.user_model import UserModel
from models.db.talent_model import TalentModel
from models.db.campaighn_model import CampaignModel
from models.db.performance_model import Performance
from models.db.talent_campaighn_association import TalentCampaighnAssosiatonTable,TalentCampaignAssociation
from database.config.base import Base
from database.config.engine import engine
def init_db():# This is the intilisation funcion for the db to setup the schema
    Base.metadata.create_all(bind=engine)
