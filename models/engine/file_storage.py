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
        #print(f"Added {obj.__class__.__name__} with id {obj.id} to storage")

    def save(self):
        """Saves storage dictionary to file"""
        try:
            temp = {}
            for key, val in self.all().items():
                print(f"Converting {key} to dict")
                temp[key] = val.to_dict()
            
            with open(FileStorage.__file_path, 'w') as f:
                json.dump(temp, f)
            print(f"Data saved to {self.__file_path}")
        except Exception as e:
            print(f"Error saving data: {str(e)}")
            pass

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            if os.path.exists(self.__file_path):
                with open(self.__file_path, 'r') as f:
                    temp = json.load(f)
                    #print(f"Loaded {len(temp)} objects from file")
                    for key, val in temp.items():
                        obj_cls_name, obj_id = key.split('.')
                        #obj_cls = globals()[obj_cls_name]
                        obj_module = __import__(f"models.{obj_cls_name.lower()}")
                        obj_cls = getattr(obj_module, obj_cls_name)
                        obj = obj_cls(**val)
                        #print(val)
                        self.new(obj)
                #print(f"Data loaded from {self.__file_path}")
            #else:
                #print(f"No file found at {self.__file_path}")
        except Exception as e:
            pass
            #print(f"Error loading data: {str(e)}")

    def delete(self, obj=None):
        """Deletes an object from the storage dictionary"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                print(f"Deleted {key} from storage")
                self.save()
