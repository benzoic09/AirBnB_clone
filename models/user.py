#!/usr/bin/python3
"""user module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """user class
    """
    class_name = "User"
    email = ""
    password = ""
    first_name = ""
    last_name = ""
     def __init__(self, *args, **kwargs):
         super().__init__(self, *args, **kwargs)
