from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "transactions"
    database_url: str = "sqlite:///resources/transactions.db"
