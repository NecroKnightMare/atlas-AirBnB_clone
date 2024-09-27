#!/bin/usr/python3

import cmd

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
    
    if __name__ == '__main__':
        HBNBCommand().cmdloop()