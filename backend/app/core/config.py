from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str
    jwt_secret: str
    algorithm: str = "HS256"

    class Config:
        env_file = ".env"

settings = Settings()