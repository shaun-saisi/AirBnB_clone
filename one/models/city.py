#!/usr/bin/python3
"""Model for a user class with a city object
"""

from models.base_model import BaseModel

class City(BaseModel):
    """For managing city objects
    """
    state_id = ""
    name = ""
