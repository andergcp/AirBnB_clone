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
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[obj_key] = obj

    def save(self):
        """ serialzes __objects to the JSON file (path: __file_path) """
        with open(self.__file_path, "w", encoding="utf-8") as write_file:
            dict_to_dump = dict()
            for key, value in self.__objects.items():
                dict_to_dump[key] = value.to_dict()
            json.dump(dict_to_dump, write_file)

    def reload(self):
        """ check if file.json exist & deserializes JSON file to __objects """
        try:
            with open(self.__file_path, 'r') as read_file:
                object_dict = json.load(read_file)
            for key, value in object_dict.items():
                repr_obj = eval(value['__class__'])(**value)
                self.__objects[key] = repr_obj
        except Exception:
            pass
