#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from datetime import datetime
import uuid
from models.base_model import BaseModel

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""

    def __init__(self):
        self.file_path = 'file.json'
        self.all_objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return self.all_objects
        else:
            filtered_objects = {key: value for key, value in self.all_objects.items()
                                if isinstance(value, cls)}
            return filtered_objects

    def new(self, obj):
        if not hasattr(obj, '__dict__'):
            raise TypeError("'obj' must be an instance of BaseModel")
        obj.id = str(uuid.uuid4())
        self.all_objects[str(type(obj).__name__) + '.' + obj.id] = obj
        return obj

    def save(self):
        """Saves storage dictionary to file"""
        temp = {}
        for key, val in self.all_objects.items():
            temp[key] = val.to_dict()
        with open(self.file_path, 'w') as f:
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.file_path, 'r') as f:
                temp = json.load(f)
            for key, val in temp.items():
                val["created_at"] = datetime.strptime(val["created_at"], "%Y-%m-%dT%H:%M:%S.%f%z")
                val["updated_at"] = datetime.strptime(val["updated_at"], "%Y-%m-%dT%H:%M:%S.%f%z")
                obj_class = eval(key.split('.')[0])
                obj_id = key.split('.')[-1]
                obj = obj_class(**val)
                self.new(obj)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from the storage dictionary"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.all_objects:
                del self.all_objects[key]
                self.save()

    def close(self):
        """Closes the FileStorage"""
        pass
