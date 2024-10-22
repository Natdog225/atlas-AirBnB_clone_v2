#!/usr/bin/python3
"""
Amenity class that inherits from BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel
    Public class attributes:
        name: string - empty string
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(*args, **kwargs)
        else:
            super().__init__()
            self.name = ""