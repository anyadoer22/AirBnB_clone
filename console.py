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


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


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

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_all(self, line):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        args = line.split()
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            list_obj = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(list_obj)

    



if __name__ == "__main__":
    HBNBCommand().cmdloop()
