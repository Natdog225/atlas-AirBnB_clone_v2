#!/usr/bin/python3
"""
City class that inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'state_id' not in kwargs:
            self.state_id = ""
        if 'name' not in kwargs:
            self.name = ""
