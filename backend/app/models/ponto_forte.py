from sqlalchemy import Column, Integer, String
from .base import Base

class PontoForte(Base):
    __tablename__ = "pontos_fortes"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
