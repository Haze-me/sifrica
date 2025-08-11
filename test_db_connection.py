import os
from sqlalchemy import create_engine, text
import dotenv

# Load environment variables
dotenv.load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

print("Testing PostgreSQL connection...")
print(f"Database URL: {DATABASE_URL}")

try:
    # Create engine
    engine = create_engine(DATABASE_URL)
    
    # Test connection
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        version = result.fetchone()[0]
        print(f"✅ Connection successful!")
        print(f"PostgreSQL version: {version}")
        
        # Test if we can see existing tables
        result = connection.execute(text("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public';
        """))
        tables = result.fetchall()
        print(f"Existing tables: {[table[0] for table in tables]}")
        
except Exception as e:
    print(f"❌ Connection failed: {e}")
    print("\nPossible issues:")
    print("1. Check if the database URL is correct")
    print("2. Ensure psycopg2-binary is installed")
    print("3. Check if the database server is accessible")
    print("4. Verify username/password are correct")