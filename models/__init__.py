#!/usr/bin/python3
"""
This is the "models" module.
"""

import os
from models.engine.file_storage import FileStorage

storage_t = os.environ.get('HBNB_TYPE_STORAGE')

if storage_t == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    storage = FileStorage()

# Import all models after storage is initialized
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

storage.reload()
