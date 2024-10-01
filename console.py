#!/usr/bin/python3
"""
This module provides a console interface for interacting with the AirBnB clone data model.
"""

import os
import sys
import cmd
from models import storage
from models.base_model import BaseModel

# Explicitly import your models
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


'''
console module or prompt
'''


class HBNBCommand(cmd.Cmd):
    '''
    Entry point of the command interpreter.

    Methods:
        do_quit: quit command to end program
        do_EOF: EOF command to exit program
        emptyline: Handles an empty line input
        do_create: Creates a new instance of a class, saves it, and prints the id
        do_show: Prints the string representation of an instance
        do_destroy: Deletes an instance
        do_all: Prints all string representation of all instances based or not on name
        do_update: Updates an instance based on name and id
    '''
    prompt = '(hbnb) '

    # Moved it up so other classes can use it.
    class_map = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def do_quit(self, arg):
        '''
        Quits the program.
        '''
        return True

    def do_EOF(self, arg):
        '''
        Exits the program on EOF (Ctrl+D).
        '''
        print()
        return True

    def onecmd(self, line):
        """
        Override the onecmd method to handle empty lines.
        """
        if not line.strip():
            return self.emptyline(line)  # Force it to use emptyline
        else:
            return super().onecmd(line) 

    def emptyline(self, arg):
        """
        Handles an empty line or a line with only spaces (does nothing).
        """
        pass

    def do_create(self,arg):
        """
        Creates a new instance of a class, saves it, and prints the id
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            cls = self.class_map[arg]
            obj = cls()
            obj.save()
            print(obj.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.class_map:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.class_map:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")

        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
        else:
            obj = storage.all()[key]  # Get the object
            storage.destroy(obj)     # Call the destroy method on FileStorage

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        """
        if arg and arg not in self.class_map:
            print("** class doesn't exist **")
        else:
            objs = storage.all()
            if arg:
                objs = {k: v for k, v in objs.items() if k.startswith(arg)}
            print([str(obj) for obj in objs.values()])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.class_map:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = storage.all()[key]
                attr_name = args[2]
                attr_value = args[3].strip('"')

                # Attempt type casting (Real basic currently, will need to update it eventually)
                try:
                    attr_value = int(attr_value)
                except ValueError:
                    try:
                        attr_value = float(attr_value)
                    except ValueError:
                        pass  # Keep it as a string if casting fails

                setattr(obj, attr_name, attr_value)
                obj.save()


if __name__ == '__main__':
    storage.reload()  # Added back the reload call
    HBNBCommand().cmdloop()
