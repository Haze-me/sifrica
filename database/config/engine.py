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


# Fix for SQLAlchemy compatibility - convert postgres:// to postgresql://
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Production vs Development configuration
is_production = os.getenv("ENVIRONMENT") == "production"

# PostgreSQL-optimized engine configuration
engine = create_engine(
    DATABASE_URL, 
    echo=not is_production,    # Disable verbose logging in production
    future=True,
    pool_size=10,              # Connection pool size
    max_overflow=20,           # Allow up to 20 additional connections
    pool_pre_ping=True,        # Verify connections before use
    pool_recycle=3600          # Recycle connections every hour
)

# SessionLocal = scoped_session(
#     sessionmaker(bind=engine, autocommit=False, autoflush=False)
# )