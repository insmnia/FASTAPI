from fastapi import FastAPI
from app.db.utils import create_models
from app.core.settings import get_settings
from app.api.api import router

settings = get_settings()

app = FastAPI(title="Test",debug=settings.DEBUG)

app.add_event_handler('startup',create_models)
app.include_router(router)