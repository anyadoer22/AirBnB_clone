#!/usr/bin/python3 env
"""Process instances using JSON"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """Serialize instances to a JSON file
    this will operate as a storage engine

    Attributess:
         __file_path: path to json file
        __objects (dict): store objects by class name
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj in the __object with key obj_classname.id"""
        clsname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(clsname, obj.id)] = obj

    def save(self):
       allobjs = FileStorage.__objects
       all_objdicts = {obj: allobjs[obj].to_dict() for obj in allobjs.keys()}
       with open(FileStorage.__file_path, "w") as f:
           json.dump(all_objdicts, f)
    def reload(self):
        """Deserialize the Json File"""
        try:
            with open(FileStorage.__file_path) as f:
                all_objdicts =  json.load(f)
                for obj in all_objdicts.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
