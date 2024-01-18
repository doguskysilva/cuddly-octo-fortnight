from functools import lru_cache
import logging
from typing import Annotated

from fastapi import Depends
from src.components.settings import Settings
from src.components.database import get_db_session

@lru_cache
def settings():
    return Settings()

def logger():
    return logging.getLogger()

def database(settings: Annotated[Settings, Depends(settings)]):
    session = get_db_session(settings)
    db = session()
    try:
        yield db
    finally:
        db.close()


