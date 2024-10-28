#!/usr/bin/python3
"""
Amenity class that inherits from BaseModel
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Amenity class that inherits from BaseModel and Base
    Public class attributes:
        __tablename__: string - name of the table
        name: string - empty string
        place_amenities: relationship with Place class
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not kwargs:
            self.name = ""
