#!/usr/bin/env python3
"""  Defines all common attributes/methods for other classes
"""
import models
import uuid
from models import storage
from datetime import datetime, timedelta
from importlib import reload


class BaseModel:

  def __init__(self, *args, **kwargs):
    """ class constructor """
    if len(kwargs) == 0:
      #Instantiation when there is not a dict
      #for creating the new instance.
      self.id = str(uuid.uuid4())
      self.created_at = datetime.now()
      self.updated_at = self.created_at
      storage.new(self)

    else:
      #Instantiation from a dict
      for key,value in kwargs.items():
        if key == 'updated_at' or key == 'created_at':
            new_value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
            setattr(self, key, new_value)
        elif key is not '__class__':
            setattr(self, key, value)

  def __str__(self):
    '''Setting str representation'''
    #Expected return:
    #[<class name>] (<self.id>) <self.__dict__>
    return '[{}] ({}) <{}>'.format(self.__class__.__name__, self.id, self.__dict__)

  def save(self):
    """ Updates the public instance attribute updated_at with the current datetime
    """
    self.updated_at = datetime.now()
    storage.save()

  def to_dict(self):
    """ Returns a dictionary containing all keys/values of __dict__ of the instance
    """
    dictionary = self.__dict__
    dictionary.update({'__class__' : self.__class__.__name__})
    dictionary['created_at'] = self.created_at.isoformat()
    dictionary['updated_at'] = self.updated_at.isoformat()
    return dictionary
