#!/bin/usr/python3

from models.base_model import BaseModel

'''
City inherits from BaseModel
'''

class City(BaseModel):
    '''
    initiation of city with an empty string
    ATTR:
        state_id: string of state identification
        name: string name of city
    '''
    state_id = ""
    name = ""