#!/usr/bin/python3
"""
Review class that inherits from BaseModel
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    """
    Review class that inherits from BaseModel and Base
    Public class attributes:
        __tablename__: string - name of the table
        text: string - empty string
        place_id: string - empty string
        user_id: string - empty string
    """
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not kwargs:
            self.text = ""
            self.place_id = ""
            self.user_id = ""
