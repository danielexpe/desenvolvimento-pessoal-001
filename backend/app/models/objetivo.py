from sqlalchemy import Column, String, Text, Integer, ForeignKey, Index
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class ObjetivoVida(BaseModel):
    """Objective model for personal goals."""
    __tablename__ = "objetivos"
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    titulo = Column(String(255), nullable=False)
    descricao = Column(Text, nullable=True)
    
    # Relationships
    user = relationship("User")
    personagens = relationship("PersonagemInspiracao", back_populates="objetivo")
    pontos_fortes = relationship("PontoForte", back_populates="objetivo")
    habilidades = relationship("HabilidadeNecessaria", back_populates="objetivo")
    
    __table_args__ = (
        Index('idx_objetivo_user_id', 'user_id'),
    )