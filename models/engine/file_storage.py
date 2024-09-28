#!/usr/bin/env python3

import json
from ..base_model import BaseModel


class FileStorage:
    """
    Handles serialization of objects to JSON file and deserialization of JSON file to objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of stored objects.
        
        :return: Dictionary of all stored objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.
        
        :param obj: Object to be added
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        obj_dicts = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dicts, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists; otherwise, do nothing).
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dicts = json.load(f)
                for key, value in obj_dicts.items():
                    class_name, obj_id = key.split('.')
                    module = __import__('models.' + class_name.lower(), fromlist=[class_name])
                    class_ = getattr(module, class_name)
                    FileStorage.__objects[key] = class_(**value)
        except FileNotFoundError:
            print(f"Error: File '{FileStorage.__file_path}' not found.")
        except Exception as e:
            print(f"An error occurred during reload: {str(e)}")
