import pytest
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker
from src.components.settings import Settings
from src.dependencies import get_database, get_settings
from src.main import app
from src.schemas import Base


@pytest.fixture()
def get_settings_override():
    return Settings(database_url="sqlite://")


@pytest.fixture()
def get_database_override(get_settings_override: Settings):
    engine = create_engine(
        get_settings_override.database_url,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    test_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    try:
        db = test_session()
        yield db
    finally:
        db.close()


@pytest.fixture
def client(get_settings_override, get_database_override):
    # override dependencues
    app.dependency_overrides[get_settings] = lambda: get_settings_override
    app.dependency_overrides[get_database] = lambda: get_database_override

    return TestClient(app)
