from typing import Optional, Union
from fastapi import APIRouter, Depends, HTTPException
from app.core.schemes.university import University, UniversityCreate
from starlette.status import HTTP_200_OK, HTTP_201_CREATED
from app.core.schemes.university import (
    University as UniversityScheme,
    UniversityCreate as UnivesityCreateScheme
)
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.crud.university import (
    create_university,
    get_universities,
    get_university,
    get_universities_by_country_and_name,
    get_universities_by_name
)

router = APIRouter()

@router.get(
    '/universities/',
    response_model=Union[list[University],University],
    status_code=HTTP_200_OK
)
def list(
    session: Session = Depends(get_db),
    name: Optional[str] = None,
    country: Optional[str] = None
):
    if name and country:
        return get_universities_by_country_and_name(session,name,country)
    return get_universities(session)

@router.post(
    '/universities/',
    status_code=HTTP_201_CREATED
)
def create(
    university: UnivesityCreateScheme,
    session: Session = Depends(get_db)
):
    db_university = get_universities_by_name(session,name=university.name)
    if db_university:
        raise HTTPException(status_code=400,detail="University with this name already exists")
    create_university(session,university)