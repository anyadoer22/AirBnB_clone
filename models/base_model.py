#!/usr/bin/python3
# base_model.py - module to define the base class
# Authors: Richard Anyadoe and Simon Tagbor
"""Defines the base class with which other subclasses inherit"""

import uuid
from datetime import datetime
import models

class BaseModel(object):
    """The base class of the Airbnb project
    this class sets attributes that are common to all future subclasses
    """
    def __init__(self, *args, **kwargs):
        """Ininitalise a new BaseModel

        Args:
            args (any): unused
            kwargs (dict): key/value pair of attributes to set
        """
        ptrn = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for k, v in  kwargs.items():
                if  k == "created_at" or k == "updated":
                    self.__dict__[k] = datetime.strptime(v, ptrn)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """overide default string method"""
        return "[{}] [{}] [{}]".format(
            self.__class__.__name__,
            self.id, self.__dict__)

    def save(self):
        """update datetime atribute of updated_at to current time
        when method is called"""
        self.updated_at = datetime.today()
        models.storage.save()


    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        specialdir = self.__dict__.copy()
        specialdir["__class__"] = "{}".format(self.__class__.__name__)
        specialdir["updated_at"] = self.updated_at.isoformat()
        specialdir["created_at"] = self.created_at.isoformat()
        return specialdir

