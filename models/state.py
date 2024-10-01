#!/bin/usr/python3

from models.base_model import BaseModel

'''
State class that inherits from BaseModel
'''

class State(BaseModel):
    '''
    State class that inherits from BaseModel
    Init of class instance
    
    Attr:
        name: state string
    '''
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__name = name
        print(self.__dict__)