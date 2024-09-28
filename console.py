#!/bin/usr/python3

import cmd
import json
import os
import uuid
from datetime import datetime
from models import storage


'''
entry point to the Command interpreter or prompt
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
        '''
        use nathans functions here and update
        '''


if __name__ == '__main__':
    storage.reload()  # Call reload here
    HBNBCommand().cmdloop()