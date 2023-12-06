#!/usr/bin/python3
"""amenity module
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """amenity class
    """
    class_name = "Amenity"
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
