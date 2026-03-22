from sqlalchemy import Column, Integer, String
from .base import Base

class HabilidadeNecessaria(Base):
    __tablename__ = "habilidades"
    id = Column(Integer, primary_key=True, index=True)
    nivel_atual = Column(Integer)
    nivel_desejado = Column(Integer)
