#!/usr/bin/python3
"""
This is the "models" module.
"""

import os
from models.engine.file_storage import FileStorage
import sys

storage_t = os.environ.get('HBNB_TYPE_STORAGE')

if storage_t == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Import all models after storage is initialized
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

storage.reload()

class Storage:
    def __init__(self):
        self.storage = storage

    def new(self, obj):
        self.storage.new(obj)

    def save(self):
        self.storage.save()

    def delete(self, obj=None):
        self.storage.delete(obj)

    def all(self, cls=None):
        return self.storage.all(cls)

    def close(self):
        self.storage.close()

# Create an instance of Storage
storage = Storage()

sys.modules['models.storage'] = storage
