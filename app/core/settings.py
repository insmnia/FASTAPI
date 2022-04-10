from pydantic import BaseSettings
import os
from functools import lru_cache


class Settings(BaseSettings):
    DB_URL: str = "postgresql://postgres:8645@localhost/un"
    DEBUG: int = int(os.getenv("DEBUG",1))

    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    return Settings()