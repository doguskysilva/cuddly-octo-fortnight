from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.components.settings import Settings

def get_db_session(settings: Settings):
    engine = create_engine(
        settings.database_url, connect_args={"check_same_thread": False}
    )
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)
