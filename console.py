#!/bin/usr/python3

import cmd
import json
import os
import uuid
from datetime import datetime
from models.storage import storage
from models.base_model import BaseModel


'''
console module or prompt
'''

class HBNBCommand(cmd.Cmd):
    '''
    entry point of the command interpreter
    
        Methods:
            do_quit: quit command to end program
            do_EOF: EOF command to exit program
            emptyline: empty line     
    '''
    prompt = '(hbnb)'
    
    def do_quit(self, arg):
        return True
    
    def do_EOF(self, arg):
        return True
    
    def emptyline(self, arg):
        pass

class BaseModel:
    '''
    create new instance of BaseModel
    '''
    
    def __init__(self, *args, **kwargs):
        '''
        
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
    
    def save(self):
        '''
        
        '''
        self.updated_at = datetime.now()
        storage.save(self)
    
    def to_dict(self):
        '''
        
        '''
        dict_repr = self.__dict__.copy()
        dict_repr['__class__'] = self.__class__.__name__
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        return dict_repr
    
    def __str__(self):
    
        """
        Returns a string representation of the Base instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    class FileStorage:
        """
        Serializes instances to a JSON file and
        deserializes JSON file to instances.

        Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Dictionary to store objects by `<class name>.id`.
        """
        __file_path = "file.json"
        __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        obj_dicts = {
            key: obj.to_dict() for key, obj in FileStorage.__objects.items()
        }
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
                    # Import the class dynamically, preserving the original case... Ideally
                    module = __import__('models.' + class_name.lower(), fromlist=[class_name])
                    class_ = getattr(module, class_name)
                    FileStorage.__objects[key] = class_(**value)
        except FileNotFoundError:
            pass

'''

go through File Storage class and update for Task 7
'''

if __name__ == '__main__':
<<<<<<< HEAD
=======
    storage.reload()  # Call reload here
>>>>>>> refs/remotes/origin/main
    HBNBCommand().cmdloop()