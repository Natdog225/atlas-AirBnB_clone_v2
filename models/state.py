#!/usr/bin/python3

"""
State class that inherits from BaseModel
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """
    State class that inherits from BaseModel and Base
    Public class attributes:
        __tablename__: string - name of the table
        name: string - empty string
        cities: relationship with City class
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan", backref="state")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not kwargs:
            self.name = ""

