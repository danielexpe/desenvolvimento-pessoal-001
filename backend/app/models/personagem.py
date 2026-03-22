from sqlalchemy import Column, Integer, String
from .base import Base

class PersonagemInspiracao(Base):
    __tablename__ = "personagens"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)  # Add description

