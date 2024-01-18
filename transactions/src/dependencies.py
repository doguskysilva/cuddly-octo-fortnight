import logging
from functools import lru_cache
from typing import Annotated

from fastapi import Depends
from src.components.database import get_db_session
from src.components.settings import Settings


@lru_cache
def get_settings():
    return Settings()


def get_logger():
    return logging.getLogger()


def get_database(settings: Annotated[Settings, Depends(get_settings)]):
    session = get_db_session(settings)
    db = session()
    try:
        yield db
    finally:
        db.close()
