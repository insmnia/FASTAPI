from app.db.database import Base
from sqlalchemy import Column, Integer, String

class University(Base):
    __tablename__ = "universities"

    id = Column(Integer,primary_key=True,index=True)
    country = Column(String(length=40),index=True)
    name = Column(String(length=40),unique=True)
    