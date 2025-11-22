from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL = "postgresql+psycopg://postgres:tt40254025@localhost:5432/share_memo"

engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def get_db():
    with SessionLocal() as session:
        yield session

