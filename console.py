#!/usr/bin/env python3
""" contains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    """ do_ commands methods """
    def do_quit(self, arg):
        raise SystemExit

    def do_EOF(self, arg):
        raise SystemExit

    """ help_ commands methods """
    def help_quit(self):
        print("Quit command to exit the program\n")

    def help_EOF(self):
        print("EOF command to exit the program\n")

    """ cmd modules """
    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
