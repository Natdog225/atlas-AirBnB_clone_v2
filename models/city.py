#!/usr/bin/python3
"""
City class that inherits from BaseModel
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """
    City class that inherits from BaseModel and Base
    Public class attributes:
        __tablename__: string - name of the table
        name: string - empty string
        state_id: string - empty string
        places: relationship with Place class
    """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade="all, delete-orphan", backref="city")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not kwargs:
            self.name = ""
            self.state_id = ""
