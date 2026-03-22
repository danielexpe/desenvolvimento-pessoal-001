from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel:
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)