import os
from contextlib import contextmanager
from urllib.parse import quote_plus

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT", "5432")
db_name = os.getenv("DB_NAME")

# Check if PostgreSQL credentials exist, otherwise fallback to SQLite
if db_user and db_pass and db_name:
    user_enc = quote_plus(db_user)
    pass_enc = quote_plus(db_pass)
    DATABASE_URL = f"postgresql://{user_enc}:{pass_enc}@{db_host}:{db_port}/{db_name}"
else:
    DATABASE_URL = "sqlite:///./mydb.sqlite3"

# Create the SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
    if DATABASE_URL.startswith("sqlite")
    else {},
)

# Create a configured session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative base for model classes
Base = declarative_base()


@contextmanager
def get_db_session():
    """
    Dependency to get a database session.
    Yields a database session and ensures it is closed after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
