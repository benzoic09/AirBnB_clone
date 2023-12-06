#!/usr/bin/python3
"""review module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review class
    """
    class_name = "Review"
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
