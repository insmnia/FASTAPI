from pydantic import BaseModel

class UniversityBase(BaseModel):
    name: str
    country: str

class UniversityCreate(UniversityBase):
    pass

class University(UniversityBase):
    _id: int

    class Config:
        orm_mode = True