from unicodedata import unidata_version
from sqlalchemy.orm import Session
from app.db.models.university import University
from app.schemes.university import University as UniversityScheme, UniversityCreate as UniversityCreateScheme

def get_university(session: Session, un_id:int):
    return session.query(University).filter_by(id == un_id).first()

def get_universities(session: Session, name:str,country:str):
    query = session.query(University)
    if name:
        query = query.filter_by(name=name)
    if country:
        query = query.filter_by(country=country)
    return query.all()

def get_universities_by_name(session: Session, name:str):
    return session.query(University).filter_by(name=name).first()

def create_university(session: Session, university: UniversityCreateScheme):
    db_university = University(**university.dict())
    session.add(db_university)
    session.commit()
    session.refresh(db_university)
    return db_university