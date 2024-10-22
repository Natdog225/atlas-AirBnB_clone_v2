#!/usr/bin/python3
"""
This is the "models" module.
"""

import os
from .engine.file_storage import FileStorage
from .engine.db_storage import DBStorage

storage_t = os.environ.get('HBNB_TYPE_STORAGE')

if storage_t == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
