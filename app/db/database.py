from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.settings import get_settings

settings = get_settings()

engine = create_engine(
    url=settings.DB_URL,
)
session = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

# dependecy injection
def get_db():
    _session = session()
    try:
        yield _session
    finally:
        _session.close()
