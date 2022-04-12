from app.crud.university import get_universities_by_name
from fastapi import HTTPException
from sqlalchemy.orm import Session
def check_university_exists(session:Session, name:str) -> bool:
    db_university = get_universities_by_name(session,name=name)
    if db_university:
        raise HTTPException(status_code=400,detail="University with this name already exists")