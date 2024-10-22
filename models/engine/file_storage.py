#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

import json
import os
import models


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.__class__.__name__ + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        try:
            temp = {}
            for key, val in self.all().items():
                if val is not None:
                    if hasattr(val, 'to_dict'):
                        dict_repr = val.to_dict()
                        temp[key] = dict_repr
                    else:
                        temp[key] = str(val)  # Fallback to string representation
            
            with open(self.__file_path, 'w') as f:
                json.dump(temp, f)
        except Exception as e:
            if isinstance(e, AttributeError):
                pass

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            if os.path.exists(self.__file_path):
                with open(self.__file_path, 'r') as f:
                    temp = json.load(f)
                    for key, val in temp.items():
                        if val is not None:
                            try:
                                obj_cls_name, obj_id = key.split('.')
                                obj_module = __import__(f"models.{obj_cls_name.lower()}", fromlist=[obj_cls_name])
                                obj_cls = getattr(obj_module, obj_cls_name)
                                obj = obj_cls(**val)
                                self.new(obj)
                            except Exception as e:
                                print(f"Error loading object {key}: {e}")
        except Exception as e:
            print(f"Failed to reload objects from {self.__file_path}: {e}")


    def delete(self, obj=None):
        """Deletes an object from the storage dictionary"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()
