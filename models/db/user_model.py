from database.config.base import Base
from sqlalchemy import Column,String
from sqlalchemy.dialects.postgresql import UUID
import uuid
class UserModel(Base):
    __tablename__ = "users_table"
    id = Column(UUID(as_uuid=True),primary_key= True,index= True,nullable=False,default=uuid.uuid4)
    username = Column(String,unique=True)
    email = Column(String,unique=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)



    def __repr__(self):
        return f"<User username={self.username}>"
