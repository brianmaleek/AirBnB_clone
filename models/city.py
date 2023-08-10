#!/usr/bin/python3

"""This module defines a class City"""

from models.base_model import BaseModel


class City(BaseModel):
    """defines a City that inherits from BaseModel."""
    state_id = ""
    name = ""
