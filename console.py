#!/usr/bin/python3
""" this is the launch point of our CLI
which imports and customize the cmd.Cmd class
"""



import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from dotenv import load_dotenv
import os
from models import storage
import sys

load_dotenv()

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
    """ our reimplementation of cmd.Cmd """
    prompt = '(hbnb) 'if sys.__stdin__.isatty() else ''


    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id.

        Handles missing class names, invalid class names, and missing
        required attributes.
        """
        try:
            args = shlex.split(arg)
            if len(args) == 0:
                print("** Class name missing. **")
                return
            class_name = args[0]
            if class_name not in model_classes.keys():
                print(f"** Class '{class_name}' not found. **")
                print("Available classes:", list(model_classes.keys()))
                return

            kwargs = {}
            for param in args[1:]:
                if "=" not in param:
                    continue
                key, value = param.split("=", 1)
                if (value.startswith('"') and value.endswith('"')) or \
                (value.startswith("'") and value.endswith("'")):
                    value = value[1:-1]
                if isinstance(value, str):
                    value = value.replace("_", " ")
                if value.lower() in ['true', 'false']:
                    value = value.lower() == 'true'
                elif '.' in value:
                    try:
                        value = float(value)
                    except ValueError:
                        pass
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        pass
                kwargs[key] = value

            # Additional checks for required attributes
            if class_name == 'State' and 'name' not in kwargs:
                print("** State name is required. **")
                return
            if class_name == 'City' and ('state_id' not in kwargs or 'name' not in kwargs):
                print("** City state_id and name are required. **")
                return

            model_class = model_classes.get(class_name)
            new_obj = model_class(**kwargs)
            storage.new(new_obj)
            storage.save()
            print(new_obj.id)

        except ValueError:
            print("** Invalid input. Please check the arguments. **")
        except Exception as e:
            print(f"** An error occurred: {e} **")


    def do_show(self, args):
        'outputs representation of an instance given the class name and id'
        instance = self.get_instance(args)
        if instance is None:
            return
        else:
            print(instance)

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
    

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformat command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        _cmd = _cls = _id = _args = ''  # initialize line elements

        # scan for general formating - i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:  # parse line left to right
            pline = line[:]  # parsed line

            # isolate <class name>
            _cls = pline[:pline.find('.')]

            # isolate and validate <command>
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in HBNBCommand.dot_cmds:
                raise Exception

            # if parantheses contain arguments, parse them
            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                # partition args: (<id>, [<delim>], [<*args>])
                pline = pline.partition(', ')  # pline convert to tuple

                # isolate _id, stripping quotes
                _id = pline[0].replace('\"', '')

                # if arguments exist beyond _id
                pline = pline[2].strip()  # pline is now str
                if pline:
                    # check for *args or **kwargs
                    if pline[0] == '{' and pline[-1] == '}' and type(eval(pline)) == dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')
                        # _args = _args.replace('\"', '')
                line = ' '.join([_cmd, _cls, _id, _args])

        except Exception:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop


if __name__ == '__main__':
    HBNBCommand().cmdloop()
