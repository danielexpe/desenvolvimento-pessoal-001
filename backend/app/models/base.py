from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, DateTime, func
from datetime import datetime

Base = declarative_base()

class BaseModel(Base):
    """Base model with common columns."""
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)