#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from datetime import datetime, timezone
import uuid

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
        print("Saving data to file...")
        temp = {}
        for key, val in self.all_objects.items():
            temp[key] = val.to_dict()
        try:
            with open(self.file_path, 'w') as f:
                json.dump(temp, f)
        except Exception as e:
            print(f"Error saving to file: {str(e)}")

    def reload(self):
        try:
            with open(self.file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    obj_class_name = key.split('.')[0]
                    obj_module = __import__(f"models.{obj_class_name.lower()}")
                    obj_class = getattr(obj_module, obj_class_name)
                    obj_id = key.split('.')[-1]
                    obj = obj_class(**val)
                    self.new(obj)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            print("Warning: file.json is empty or contains invalid JSON.")
        except Exception as e:
            print(f"Error reloading from file: {str(e)}")

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside.

        If obj is equal to None, the method should not do anything.
        """
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.all_objects:
                del self.all_objects[key]
                self.save()

    def close(self):
        """Closes the FileStorage"""
        self.reload()
        