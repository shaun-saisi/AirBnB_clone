#!/usr/bin/python3
"""This is the main base model
"""
from models import storage
from datetime import datetime
import uuid

class BaseModel:
    """All classes will be inheriting from this class"""

    def __init__(self, *args, **kwargs):
        """Used to initialize instance attributes
        
        Args:
            *args: The arguments
            **kwargs: Dictionary of keyword arguments
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def to_dict(self):
        """Returns a dictionary containing object information"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict

    def save(self):
        """Updates the updated_at attribute"""
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """Returns the official representation"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

