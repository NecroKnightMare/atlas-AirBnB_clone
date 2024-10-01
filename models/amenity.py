#!/bin/usr/python3

from models.base_model import BaseModel

'''
Amenity inherits from BaseModel
'''

class Amenity(BaseModel):
    '''
    initiation of amenity with an empty string
    ATTR:
        name: string name of city
    '''
    name = ""