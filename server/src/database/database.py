from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from src.core.config import settings

DATABASE_URL = settings.DATABASE_URL

my_metadata = MetaData()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

class Base(DeclarativeBase):
    metadata=MetaData(schema="school")


def get_db():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()