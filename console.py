#!/usr/bin/python3
""" this is the launch point of our CLI
which imports and customize the cmd.Cmd class
"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

model_classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Place': Place,
        'Amenity': Amenity,
        'Review': Review
        }


class HBNBCommand(cmd.Cmd):
    """ our reimplementation of cmd.Cmd
    """
    prompt = '(hbnb) '

    def do_create(self, arg):
        'creates a new instance of BaseModel'
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in model_classes.keys():
            print("** class doesn't exist **")
            return
        else:
            model_class = model_classes.get(args[0])
            new_obj = model_class()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, args):
        'outputs representation of an instance given the class name and id'
        instance = self.get_instance(args)
        if instance is None:
            return
        else:
            print(str(instance))

    def do_destroy(self, arg):
        'delete instance given by the class name and id'
        instance = self.get_instance(arg)
        if instance is None:
            return
        else:
            key = models.storage.construct_key(instance)
            models.storage.all().pop(key)
            models.storage.save()

    def do_all(self, args):
        """ outputs string representations for every existing
        instance or for all of a class
        """
        obj_list = []

        if not args:
            for value in models.storage.all().values():
                obj_list.append(str(value))
        else:
            class_given = args.split()
            class_given = class_given[0]
            if class_given in model_classes.keys():
                for key, value in models.storage.all().items():
                    if key.startswith(class_given):
                        obj_list.append(str(value))
            else:
                print("** class doesn't exist **")
                return

        print(obj_list)

    def do_update(self, arg):
        """ updates the instance given by class_name and id.
        usage: update <class> <id> <attr> "<val>"
        """

        instance = self.get_instance(arg)
        if instance is None:
            return

        attr_val = self.parse_attributes(arg)
        if attr_val is None:
            return

        attr = attr_val[0]
        value = attr_val[1]

        if hasattr(instance, attr):
            attr_type = type(getattr(instance, attr))

            try:
                value = attr_type(value)
            except (ValueError, TypeError):
                print("** value given could not be typecast correctly **")
                value = getattr(instance, attr)

            setattr(instance, attr, value)
            instance.save()
        else:
            print("** no such attribute found **")

    def do_quit(self, arg):
        'exit this CLI instance hbnb'
        quit()

    do_EOF = do_quit

    def emptyline(self):
        pass

    def parse_attributes(self, args):
        'returns an touple with attribute and value'

        attr = args.split()
        attr = attr[2] if len(attr) > 2 else None
        if args.find('"') > 0:
            value = args.split('"')
            value = value[1] if len(value) > 1 else None
        elif args.find("'") > 0:
            value = args.split("'")
            value = value[1] if len(value) > 1 else None
        else:
            value = args.split()
            value = value[3] if len(value) > 3 else None

        if attr is None:
            print('** attribute name missing **')
            return None
        elif value is None:
            print('** value missing **')
            return None
        else:
            return (attr, value)

    def get_instance(self, args):
        args = args.split()
        class_name = args[0] if len(args) > 0 else None
        id_num = args[1] if len(args) > 1 else None

        if class_name is None:
            print('** class name missing **')
            return None
        elif class_name not in model_classes.keys():
            print("** class doesn't exist **")
            return None
        elif id_num is None:
            print('** instance id missing **')
            return None
        else:
            key = class_name + "." + id_num
            instance = models.storage.all().get(key)
            if instance is None:
                print('** no instance found **')
                return None
            return instance


if __name__ == '__main__':
    HBNBCommand().cmdloop()