#!/usr/bin/env python3
""" contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    classes = ['BaseModel', 'User', 'State', 'City',
               'Amenity', 'Place', 'Review']

    """ do_ commands methods """
    def do_quit(self, arg):
        raise SystemExit

    def do_EOF(self, arg):
        raise SystemExit

    def do_create(self, arg):
        """ Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        # try:
        #     new_instance = eval(arg + "()")
        #     new_instance.save()
        #     print(new_instance.id)
        # except:
        #     print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the str repr of an instance based on the cls bane and id """
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        if args_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
            # try:
            #     eval(name)
            # except:
            #     print("** class doesn't exist **")
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        try:
            objs = storage.all()
            obj_key = args_list[0] + '.' + args_list[1]
            print(objs[obj_key])
        except Exception:
            print('** no instance found **')
        # else:
        #     try:
        #         eval(id_number)
        #     except:
        #         print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        """
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        if args_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        try:
            obj_key = args_list[0] + '.' + args_list[1]
            del storage.all()[obj_key]
            storage.save()
        except Exception:
            print('** no instance found **')

        # else:
        #     try:
        #         eval(cls_name)
        #     except:
        #         print("** class doesn't exist **")
        # if not id_number:
        #     print("** instance id missing **")
        # else:
        #     try:
        #         eval(id_number)
        #     except:
        #         print("** no instance found **")

    def do_all(self, cls_name):
        """ Prints all string representation of all instances
        based or not on the class name
        """
        objs_dict = storage.all()
        objs_list = []
        for key, value in objs_dict.items():
            if not cls_name:
                objs_list.append(str(value))
            elif cls_name not in self.classes:
                print("** class doesn't exist **")
                return
            else:
                if key.split('.')[0] == cls_name:
                    objs_list.append(str(value))
        if not objs_list:
            return
        print(objs_list)

        # try:
        #     eval(cls_name)
        # except:
        #     print("** class doesn't exist **")

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)
        """
        if not args:
            print("** class name missing **")
            return
        splited_args = args.split()
        if splited_args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(splited_args) < 2:
            print('** instance id missing **')
            return
        try:
            key_obj = splited_args[0] + '.' + splited_args[1]
            obj = storage.all()[key_obj]
        except Exception:
            print('** no instance found **')
            return
        if len(splited_args) < 3:
            print('** attribute name missing **')
            return
        if len(splited_args) < 4:
            print('** value missing **')
            return
        setattr(obj, str(splited_args[2]), str(splited_args[3][1:-1]))
        storage.save()
        # try:
        #     eval(cls_name)
        # except:
        #     print("** class doesn't exist **")

    def help_quit(self):
        print("Quit command to exit the program\n")

    def help_EOF(self):
        print("EOF command to exit the program\n")

    def help_create(self):
        print("Create <class name> to create a new instance of that class")

    def help_show(self):
        print("Show command: print str rep of instance (cls name and id)")

    def help_destroy(self):
        print("Destroy command: deletes an instance based of cls name and id")

    def help_all(self):
        print("All command: print all str repr of all instances ")

    def help_update(self):
        print("Update command: updates an instance")

    """ cmd modules """
    def emptyline(self):
        '''Empty line'''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
