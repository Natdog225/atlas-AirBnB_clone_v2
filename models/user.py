#!/usr/bin/python3
"""
User class that inherits from BaseModel
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class User(BaseModel, Base):
    """
    User class that inherits from BaseModel and Base
    Public class attributes:
        __tablename__: string - name of the table
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not kwargs:
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""
