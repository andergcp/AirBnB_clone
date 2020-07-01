#!/usr/bin/env python3
""" contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

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
        try:
            new_instance = eval(arg + "()")
            new_instance.save()
            print(new_instance.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, name, id_number):
        """Prints the str repr of an instance based on the cls bane and id """
        if not name:
            print("** class name missing **")
        else:
            try:
                eval(name)
            except:
                print("** class doesn't exist **")
        if not id_number:
            print("** instance id missing **")
        else:
            try:
                eval(id_number)
            except:
                print("** no instance found **")

    def do_destroy(self, cls_name, id_number):
        """
        Deletes an instance based on the class name and id
        """
        if not cls_name:
            print("** class name missing **")
        else:
            try:
                eval(cls_name)
            except:
                print("** class doesn't exist **")
        if not id_number:
            print("** instance id missing **")
        else:
            try:
                eval(id_number)
            except:
                print("** no instance found **")

    def do_all(self, cls_name):
        """ Prints all string representation of all instances
        based or not on the class name
        """
        print()
        try:
            eval(cls_name)
        except:
            print("** class doesn't exist **")

    def do_update(self, cls_name, id_number, attr):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)
        """
        if not cls_name:
            print("** class name missing **")
        else:
            try:
                eval(cls_name)
            except:
                print("** class doesn't exist **")

    """ help commands methods """
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
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
