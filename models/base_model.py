#!/usr/bin/python3
# base_model.py - module to define the base class
# Authors: Richard Anyadoe and Simon Tagbor
"""Defines the base class with which other subclasses inherit"""

import uuid
from datetime import datetime


class BaseModel(object):
    """The base class of the Airbnb project
    this class sets attributes that are common to all future subclasses
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """overide default string method"""
        return "[{}] [{}] [{}]".format(
            self.__class__.__name__,
            self.id, self.__dict__)

    def save(self):
        """update datetime atribute of updated_at to current time
        when method is called"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        self.__dict__[__class__] = "{}".format(self.__class__.__name__)
        for key, value in list(self.__dict__.items()):
            if key ==  "updated_at" or key == "created_at":
                datetime.isoformat(value)
        return self.__dict__
