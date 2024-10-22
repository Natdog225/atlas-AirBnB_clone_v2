#!/usr/bin/python3
"""
City class that inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel
    Public class attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(*args, **kwargs)
        else:
            super().__init__()
            self.state_id = ""
            self.name = ""