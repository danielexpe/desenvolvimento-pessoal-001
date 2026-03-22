from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

class Atividade(Base):
    __tablename__ = "atividades"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String)
    frequencia = Column(String)  # Define the frequency of the activity