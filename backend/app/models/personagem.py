from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class PersonagemInspiracao(Base):
    __tablename__ = 'personagem_inspiracao'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    descricao = Column(String)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    objetivo_vida_id = Column(Integer, ForeignKey('objetivo_vida.id'), nullable=False)
    
    usuario = relationship('Usuario', back_populates='personagens_inspiracao')
    objetivo_vida = relationship('ObjetivoVida', back_populates='personagens_inspiracao')
    
    def __repr__(self):
        return f'<PersonagemInspiracao(nome={self.nome}, descricao={self.descricao})>'
