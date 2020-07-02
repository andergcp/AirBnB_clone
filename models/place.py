#!/usr/bin/env python3
""" class inherit from basemodel """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ public class attribute """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = []
