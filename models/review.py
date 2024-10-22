#!/usr/bin/python3

"""
State class that inherits from BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that inherits from BaseModel
    Public class attributes:
        name: string - empty string
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(*args, **kwargs)
        else:
            super().__init__()
            self.name = ""