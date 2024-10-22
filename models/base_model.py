#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime, timezone
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from models import storage

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initiates a new model"""
        print(f"Initializing {self.__class__.__name__}")
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now(timezone.utc)
            self.updated_at = datetime.now(timezone.utc)
            print(f"Created new instance with id: {self.id}")
        else:
            print(f"Initializing from kwargs: {kwargs}")
            for key, value in kwargs.items():
                if key not in ['__class__', 'created_at', 'updated_at']:
                    setattr(self, key, value)
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f%z")
            else:
                self.created_at = datetime.now(timezone.utc)
            if "updated_at" in kwargs:
                self.updated_at = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f%z")
            else:
                self.updated_at = datetime.now(timezone.utc)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
                print(f"Generated new id: {self.id}")

        print(f"Final attributes: {self.__dict__}")
        storage.new(self)



    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        import models
        self.updated_at = datetime.now(timezone.utc)
        models.storage.save()
        
    def to_dict(self):
        """Convert instance into dict format"""
        print(f"Converting {self.__class__.__name__} to dict")
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
            
        if hasattr(self, 'created_at') and isinstance(self.created_at, datetime):
            dictionary['created_at'] = self.created_at.isoformat(timespec='microseconds')
        elif 'created_at' not in dictionary:
            dictionary['created_at'] = datetime.now(timezone.utc).isoformat(timespec='microseconds')

        if hasattr(self, 'updated_at') and isinstance(self.updated_at, datetime):
            dictionary['updated_at'] = self.updated_at.isoformat(timespec='microseconds')
        elif 'updated_at' not in dictionary:
            dictionary['updated_at'] = datetime.now(timezone.utc).isoformat(timespec='microseconds')
            
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']

        print(f"Dictionary created: {dictionary}")
        return dictionary



    def delete(self):
        """Delete the current instance from the storage"""
        import models
        models.storage.delete(self)
