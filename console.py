#!/usr/bin/python3

import os
import sys
import cmd
#import logging
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review 

#PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Append the project root to sys.path
#sys.path.append(PROJECT_ROOT)

#logging.basicConfig(level=logging.INFO)
#print(sys.path)

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
    prompt = '(hbnb) '
    
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

    def do_create(self, arg):
        """
        Creates a new instance of a class, saves it, and prints the id
        """
        if not arg:
            print("** class name missing **")
            return

        # Mapping
        class_map = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }

        try:
            cls = class_map[arg]
            obj = cls()
            obj.save()
            print(obj.id)
        except KeyError:
            print("** class doesn't exist **")


    def do_show(self, arg):
        '''
        '''
        args = arg.split()
        if args[0] not in self.class_map:
            print("** class is missing **")
            return
        if not args [0]:
            print("** class doesn't exist **")
            return
        if len (args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return

    def do_destroy(self, arg):
        '''
        '''
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.class_map:
            print("** class doesn't exist **")
            return
        if len (args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        '''
        '''
        if arg and arg not in self.class_map:
            print("** class doesn't exist **")
            return
        objs = storage.all()
        if arg:
            objs = {k: v for k, v in objs.items() if k.startswith(arg)}
        print([str(obj) for obj in obj.values()])

    def do_update(self, arg):
        '''
        '''
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.class_map:
            print("** class doesn't exist **")
            return
        if len < 2 :
            print("** instance id missing **")
            return
        key = f"{args[0]}. {args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3].strip('"')
        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
    
    '''
    this should be good, test is failing with INFO:root:File 'file.json'
    not found. No objects loaded.-Debug other files
    '''
