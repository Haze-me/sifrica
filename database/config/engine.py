from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session
import os
import dotenv

dotenv.load_dotenv()
"""
This is where the engine and connection to the db is created

The db url is defined in the .env file.

Please note the if you uhave issues connecting to postgres
there is ussally another dependicy you'll need to add
because of the specfic dilaect of postgres.

"""

DATABASE_URL = str(os.getenv("DATABASE_URL"))

engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))#Creates a thread scoped session
