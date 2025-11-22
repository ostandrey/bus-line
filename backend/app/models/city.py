from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from ..database import Base


class City(Base):
    __tablename__ = "cities"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False, index=True)
    lon = Column(Float, nullable=False, nullable=False)
    lat = Column(Float, nullable=False, nullable=False)
    
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    
    def __repr__(self):
        return f"<City(id={self.id}, name={self.name})>"