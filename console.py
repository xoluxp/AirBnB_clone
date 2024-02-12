#!/usr/bin/env python3
"""
Console module for AirBnB clone project
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project"""
    intro = "Welcome to Our Console"
    prompt = '(hbnb) '
    valid_classes = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves and prints the id"""
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return False
        else:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)
            return True

    def do_show(self, arg):
        """ Prints the str rep. of an instance based on name and id"""
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return False
        elif len(args) == 1:
            print("**instance id missing**")
            return False
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                print(storage.all()[key])
                return True
            else:
                print("**no instance found**")
                return False

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save to JSON file)
        """
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return False
        elif len(args) == 1:
            print("** instance id missing **")
            return False
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
                return True
            else:
                print("** no instance found **")
                return False

    def do_all(self, arg):
        """
        Prints all str. rep. of all instances based or not
        on the class name
        """
        args = arg.split(" ")
        objects = storage.all()
        obj_list = []
        if not arg:
            for obj in objects.values():
                obj_list.append(str(obj))
            print(obj_list)
            return True
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return False
        else:
            obj = args[0]
            for obj in objects.values():
                obj_list.append(str(obj))
            print(obj_list)
            return True

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)
        """
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return False
        elif len(args) == 1:
            print("** instance id missing **")
            return False
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
                return False
            elif len(args) == 2:
                print("** attribute name missing **")
                return False
            elif len(args) == 3:
                print("** value missing **")
                return False
            else:
                obj = storage.all()[key]
                attribute_name = args[2]
                attribute_value = args[3]
                setattr(obj, attribute_name, attribute_value)
                obj.save()
                return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
