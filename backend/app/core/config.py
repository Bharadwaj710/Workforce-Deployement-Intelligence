from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    environment: str
    database_url: str
    embedding_model: str

    class Config:
        env_file=".env"

settings=Settings()