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
                print(f"Processing {key} for saving")
                if val is not None:
                    if hasattr(val, 'to_dict'):
                        dict_repr = val.to_dict()
                        print(f"Dict representation of {key}: {dict_repr}")
                        temp[key] = dict_repr
                    else:
                        print(f"Warning: Object {key} does not have a to_dict method")
                        temp[key] = str(val)  # Fallback to string representation
                else:
                    print(f"Warning: Skipping {key} as it's None")
            
            print(f"Final temp dictionary: {temp}")
            
            with open(self.__file_path, 'w') as f:
                json.dump(temp, f)
            print(f"Data saved to {self.__file_path}")
        except Exception as e:
            print(f"Error saving data: {str(e)}")
            print(f"Error type: {type(e).__name__}")
            if isinstance(e, AttributeError):
                print(f"AttributeError details:")
                print(f"Object causing the error: {key if 'key' in locals() else 'Unknown'}")
                print(f"Object attributes: {dir(val) if 'val' in locals() else 'Unknown'}")


    def reload(self):
        """Loads storage dictionary from file"""
        try:
            if os.path.exists(self.__file_path):
                with open(self.__file_path, 'r') as f:
                    temp = json.load(f)
                    print(f"Loaded {len(temp)} objects from file")
                    for key, val in temp.items():
                        if val is not None:
                            try:
                                obj_cls_name, obj_id = key.split('.')
                                obj_module = __import__(f"models.{obj_cls_name.lower()}", fromlist=[obj_cls_name])
                                obj_cls = getattr(obj_module, obj_cls_name)
                                obj = obj_cls(**val)
                                self.new(obj)
                            except (ImportError, AttributeError) as e:
                                print(f"Error creating object for {key}: {str(e)}")
                        else:
                            print(f"Warning: Null value found for key {key}")
                    print(f"Data loaded from {self.__file_path}")
            else:
                print(f"No file found at {self.__file_path}")
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in {self.__file_path}")
        except Exception as e:
            print(f"Error loading data: {str(e)}")


    def delete(self, obj=None):
        """Deletes an object from the storage dictionary"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                print(f"Deleted {key} from storage")
                self.save()
