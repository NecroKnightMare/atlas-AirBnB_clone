#!/bin/usr/python3

import cmd
import logging
import sys
import os 

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            sys.path.append(PROJECT_ROOT)

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

if __name__ == '__main__':
    storage.reload()
    HBNBCommand().cmdloop()
    
    '''
    this should be good, test is failing with INFO:root:File 'file.json'
    not found. No objects loaded.-Debug other files
    '''
