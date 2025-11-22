from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from ..database import Base


class Bus(Base):
    __tablename__ = "buses"
    
    id = Column(Integer, primary_key=True, index=True)
    number_plate = Column(Integer, unique=True, nullable=False, index=True)
    color = Column(String, nullable=False)
    seats_quantity = Column(Integer, nullable=False)
    
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    def __repr__(self):
        return f"<Bus(id={self.id}, number_plate={self.number_plate})>"