#!/usr/bin/python3
"""test for databse storage"""
import unittest
import pep8
import json
import os
import MySQLdb
from models.base_model import BaseModel, Base
from models.engine.db_storage import DBStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestDatabaseStorage(unittest.TestCase):
    '''this will test the database'''

    def test_pep8_dbstorage(self):
        """Testing the pep8 linter requirments."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         'Found pep8 style errors')
