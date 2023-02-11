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
    def do_EOF(self, line):
        """EOF help quit."""
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True







if __name__ == "__main__":
    HBNBCommand().cmdloop()
