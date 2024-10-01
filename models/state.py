#!/usr/bin/python3

from models.base_model import BaseModel

'''
State class that inherits from BaseModel
'''


class State(BaseModel):
    '''
    State class that inherits from BaseModel
    
    Attr:
        name: state string
    '''

    def __init__(self, *args, **kwargs):
        """
        Initializes a new State instance.
        """
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")  # Access name from kwargs
        name = ""