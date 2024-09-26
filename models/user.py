#!/bin/usr/python3

from base_model import BaseModel

class User(BaseModel):
    def __init__(self):
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        
