#!/usr/bin/python3
import uuid
from datetime import datetime

'''
Module for AirBnB console

'''


class BaseModel:
    '''
    Base class for all AirBnB models.
    
    Attributes:
        id (str): Unique identifier for the object.
        created_at (datetime): Date and time the object was created.
        updated_at (datetime): Date and time the object was last updated.
    '''

    def __init__(self, *args, **kwargs):
        '''
        Initializes a new BaseModel instance.
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        '''
        Returns a string representation of the BaseModel instance.
        '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''
        Updates the 'updated_at' attribute with the current datetime.
        '''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''
        Returns a dictionary representation of the BaseModel instance.
        '''
        dict_repr = self.__dict__.copy()
        dict_repr['__class__'] = self.__class__.__name__
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        return dict_repr