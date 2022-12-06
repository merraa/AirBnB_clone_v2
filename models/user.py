#!/usr/bin/python3
"""This is the user class"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review
from models.place import Place


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
        places: relationship to place
        reviews: relationship to review
    """

    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship('Place', cascade='all, delete',
                          backref='user')
    reviews = relationship('Review', cascade='all, delete',
                           backref='user')
