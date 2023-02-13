#!/usr/bin/python3
""" contains entry point of the command interpreter """
import cmd
import re
from shlex import split
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

    prompt = '(hbnb) '
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review",
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_EOF(self, line):
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_create(self, line):
        """Create a new instance of BaseModel and print the id"""
        args = parse(line)

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
        args = parse(line)
        obdict = storage.all()
        if len(args) == 0:
            print("** class doesn't exist")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obdict:
            print("** no instance found **")
        else:
            print(obdict["{}.{}".format(args[0], args[1])])

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
                    list_obj.append(obj.__str__())
                elif len(args) == 0:
                    list_obj.append(obj.__str__())
            print(list_obj)

    def do_destroy(self, line):
        """ Usage: destroy <class> <id> or <class>.destroy(<id>)
        Deletes a class instance of a given id"""
        args = parse(line)
        obdict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obdict.keys():
            print("** no instance found **")
        else:
            del obdict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_update(self, line):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
        <class>.update(<id>, <attribute_name>, <attribute_value>) or
        <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        args = parse(line)
        obdict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in obdict.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(args) == 4:
            obj = obdict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = obdict["{}.{}".format(args[0], args[1])]
            for k, v in eval(args[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
