#!/usr/bin/python3

import sys
import os

# Get the absolute path to the project's root directory
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Append the project root to sys.path
sys.path.append(PROJECT_ROOT) 

import cmd
import logging
from models import storage
from models.base_model import BaseModel


logging.basicConfig(level=logging.INFO)
print(sys.path)

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
        '''
        quits program
        '''
        return True
    
    def do_EOF(self, arg):
        '''
        ends file
        '''
        print()
        return True
    
    def emptyline(self, arg):
        '''
        passes empty line
        '''
        pass

    def create(self, arg):
        '''

        '''
        if not arg:
            print("**class is missing**")
            return
        try:
            clss = globals()[arg]
            if not issubclass(clss, BaseModel):
                raise KeyError
            obj = clss()
            obj.save()
            print(obj.id)
        except KeyError:
            print("* class doesn't exist **")


if __name__ == '__main__':
    storage.reload()
    HBNBCommand().cmdloop()
    
    '''
    this should be good, test is failing with INFO:root:File 'file.json'
    not found. No objects loaded.-Debug other files
    '''
