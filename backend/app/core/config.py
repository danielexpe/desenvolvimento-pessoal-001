import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database
    SQLALCHEMY_DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:senha-mysql@mysql:3306/objetivos_db"
    )
    
    # JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "sua-chave-secreta-super-segura-aqui-nao-use-em-producao")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # App
    APP_NAME: str = "Sistema de Apoio ao Foco em Objetivos Pessoais"
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    
    class Config:
        env_file = ".env"

settings = Settings()