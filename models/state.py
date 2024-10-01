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
    def __init__(self, name):
        self.name = name