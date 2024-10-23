#!/usr/bin/python3
"""
User class that inherits from BaseModel
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """
    User class that inherits from BaseModel and Base
    Public class attributes:
        __tablename__: string - name of the table
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
        places: relationship with Place class
        reviews: relationship with Review class
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=True)
    password = Column(String(128), nullable=True)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", cascade="all, delete-orphan", backref="user")
    reviews = relationship("Review", cascade="all, delete-orphan", backref="user")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not kwargs:
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""
