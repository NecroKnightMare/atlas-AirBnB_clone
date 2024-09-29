#!/usr/bin/env python3

import uuid
from datetime import datetime

class BaseModel:
    """
    Serves as a base class for all models in the HBNB application.
    Provides common attributes and methods for other classes to inherit.
    """
    
    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.
        
        :param args: Argument list (not used)
        :param kwargs: Keyword arguments representing attributes
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the Base instance.
        
        :return: String representation of the object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self, storage):
        """
        Updates the 'updated_at' attribute with the current date/time and saves the object.
        
        :param storage: Storage object to save the model
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Converts the object's attributes to a dictionary representation.
        
        :return: Dictionary representation of the object
        """
        dict_repr = self.__dict__.copy()
        dict_repr['__class__'] = self.__class__.__name__
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        return dict_repr
