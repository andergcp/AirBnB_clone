#!usr/bin/env python3
"""
BaseModel from another one by using a dictionary
"""
import os
import json


class FileStorage:
    """ serializes to JSON file and deserializes JSON file to instance """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        self.__objects = obj

    def save(self):
        """ serialzes __objects to the JSON file (path: __file_path) """
        with open(self.__file_path, "w", encoding="utf-8") as write_file:
            json.dump(self.__objects, write_file)

    def reload(self):
        """ check if file.json exist & deserializes JSON file to __objects """
        if os.path.isfile(self.__file_path) is True:
            with open(self.__file_path, "r", encoding="utf-8") as read_file:
                self.__objects = json.load(read_file)
