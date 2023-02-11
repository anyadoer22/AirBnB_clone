#!/usr/bin/python3
""" contains entry poiny of the command interpreter """
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Implement an entry point for managing models"""

    prompt = '(hbnb)'
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review",
    }

    def do_EOF(self, line):
        """EOF help quit."""
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_create(self, line):
        """Create a new instance of BaseModel and print the id"""
        args = line.split()

        if len(args) == 2:
            objname = args[0]
            clsname = args[1]
            if clsname not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                objname = eval(clsname)()
                print(objname.id)
                storage.save()
        else:
            print("** class name missing **")
    def do_show(self, line):
        """prints the String representation of an instance
        usage: show [classname]  [id]
        """
        args = line.split()






if __name__ == "__main__":
    HBNBCommand().cmdloop()
