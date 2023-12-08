#!/usr/bin/python3
"""base_model template for all classes
"""
import uuid
from datetime import datetime
from datetime import date
from datetime import time
from models import storage


class BaseModel:
    """BaseModel class
    """
    class_name = 'BaseModel'

    def __init__(self, *args, **kwargs):
        """initialises each unique instance with a different
        unique Id, created_at time and updated_at time
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "created_at":
                    bit1, bit2 = value.split("T")
                    year, month, day = bit1.split("-")
                    bit2, mic = bit2.split(".")
                    hour, minute, second = bit2.split(":")
                    _date = date(int(year), int(month), int(day))
                    _time = time(int(hour), int(minute), int(second), int(mic))
                    val = datetime.combine(_date, _time)
                    self.created_at = val
                elif key == "updated_at":
                    bit1, bit2 = value.split("T")
                    year, month, day = bit1.split("-")
                    bit2, mic = bit2.split(".")
                    hour, minute, second = bit2.split(":")
                    _date = date(int(year), int(month), int(day))
                    _time = time(int(hour), int(minute), int(second), int(mic))
                    val = datetime.combine(_date, _time)
                    self.updated_at = val
                else:
                    setattr(self, key, value)
                """elif key == 'id':
                    self.id = value
                elif key == 'name':
                    self.name = value
                elif key == 'my_number':
                    self.my_number = value"""
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """returns a nicely printable instance
        """
        return "[{}] ({}) {}".format(self.class_name, self.id, self.__dict__)

    def save(self):
        """updates the instance variable when saving the instance
        e.g before exiting the program
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the particular instance
        """
        dictionary = {}
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                dictionary[key] = value.isoformat()
            else:
                dictionary[key] = value
        dictionary['__class__'] = self.class_name
        return dictionary
