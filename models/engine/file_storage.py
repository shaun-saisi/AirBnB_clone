#!/usr/bin/python3
""" This module is a fikle storage for the classs
"""

import os
import datetime
import json

class FileStorage:
    """ This class is used to store and retrieve data
    """
    __file_path = "file.json"
    __objecrs = {}

    def all(self):
        """return the dictionary objects to the file storage
        """
        return FileStorage.__objects

    def new(self, obj):
        """stes the keys to the objects
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj
    
    def classes(self):
        """Returns  a dictionary for references
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.place import Place
        from models.City import City
        from models.review import Review
        from models.amenity import Amenity

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "Place": Place,
                   "City": City,
                   "Review": Review,
                   "Amenity": Amenity}
        return classes

    def save(self):
        """save object to json format
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            a = {k: v.to_dict () for k, v in FileStorage.__objects.items()}
            json.dump(a, f)

    def attributes (self):
        """ This returns the valid attributes
        """
        attributes = {
                "BasseModel":
                          {"id": str,
                           "created_at": datetime.datetime,
                           "updated_at": datetime.datetime},
                "User":
                        {"email": str,
                         "password": str,
                         "first_name": str,
                         "last_name" : str},
                "State":
                        {"name": str},

                "Place":
                        {"city_id": str,
                         "user_id": str,
                         "name" : str,
                         "description": str,
                      	 "number_rooms": int,
                         "number_bathrooms": int,
                         "max_guest": int,
                         "price_by_night": int,
                         "latitude": float,
                         "longitude": float,
                         "amenity_ids": list}, 
		"City":
                     {"state_id": str,
                      "name": str},
		
		"Review":
           		 {"place_id": str,
                         "user_id": str,
                         "text": str}
		"Amenity":
                     {"name": str},

	}
	return attributes
	
	 def reload(self):
        """Reloads objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict

