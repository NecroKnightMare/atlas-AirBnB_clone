#!/bin/usr/python3

from models.base_model import BaseModel

'''
review class that inherits from BaseModel
'''

class Review(BaseModel):
    '''
    initiation of review class
    
    Attrs:
        place_id: string - empty string: Place.id
        user_id: string - empty string: User.id
        text: string - empty string
    '''
    def __init__(self):
        place_id = ""
        user_id = ""
        text = ""