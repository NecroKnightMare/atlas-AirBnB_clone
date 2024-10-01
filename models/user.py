#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):  # Inherit from BaseModel
    """
    Represents a user in the AirBnB system.

    Attributes:
        email (str): The user's email address.
        password (str): The user's password (hashed in a real application).
        first_name (str): The user's first name.
        last_name (str): The user's last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    # No need for __init__ if it's just setting default attr values, currently at least.