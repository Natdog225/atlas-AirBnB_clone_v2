#!/usr/bin/python3
"""
This is the "models" module.
"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()

# Create a BaseModel instance and save it to create the file.json file
bm = BaseModel()
bm.save()

storage.reload()