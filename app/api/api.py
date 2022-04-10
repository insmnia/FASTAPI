from fastapi import APIRouter
from app.api.endpoints.universities import router as university_router

router = APIRouter(prefix="/api")
router.include_router(university_router)