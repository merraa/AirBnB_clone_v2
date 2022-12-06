#!/usr/bin/python3
"""This is the amenity class"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
        __tablename__: amenities table for database
    """

    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
