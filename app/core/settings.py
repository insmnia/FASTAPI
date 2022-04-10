from pydantic import BaseSettings
import os
from functools import lru_cache


class Settings(BaseSettings):
    DB_URL: str
    DEBUG: int

    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    return Settings()