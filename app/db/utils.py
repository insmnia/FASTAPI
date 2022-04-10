from app.db.database import Base, engine
from loguru import logger

def create_models():
    logger.info("Creating models...")
    Base.metadata.create_all(bind=engine)
    logger.info("Models created")