from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()
server_password = os.getenv("SUPABASE_PASS")

SQLALCHEMY_DATABASE_URL = f"postgresql://postgres.xldoknfkntxvhrtsdtuy:{server_password}@aws-1-ap-southeast-2.pooler.supabase.com:6543/postgres"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo = True
)


sessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit= False)

class Base(DeclarativeBase):
    pass