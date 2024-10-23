import os
from dotenv import load_dotenv

load_dotenv()

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

storage_t = os.environ.get('HBNB_TYPE_STORAGE')

if storage_t == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()

# Import all models AFTER storage is initialized and reloaded
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

import models.storage 
models.storage.storage = storage