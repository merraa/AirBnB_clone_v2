#!/usr/bin/python3
"""
Databse engine
"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

all_classes = {"City": City,
               "State": State,
               "Place": Place,
               "User": User,
               "Review": Review,
               "Amenity": Amenity}


class DBStorage:
    """
    Handles Database engine
    Attributes:
        __engine: engine for the database
        __session: session of the database
    """

    __engine = None
    __session = None

    def __init__(self):
        """Instantiate
        Create engine for database
        """

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session (self.__session)
        all objects depending of the class name (argument cls)
        Attribute:
            return_dict: dictionary of session objects
            query: queries session
        """
        return_dict = {}
        query = []
        if cls:
            for name, value in all_classes.items():
                if name == cls:
                    query = self.__session.query(value)
                    for obj in query:
                        key = name + '.' + obj.id
                        return_dict[key] = obj
            return return_dict

        else:
            for name, value in all_classes.items():
                query = self.__session.query(value)
                for obj in query:
                    key = name + '.' + obj.id
                    return_dict[key] = obj
        return return_dict

    def new(self, obj):
        """Adds the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session
        """
        self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        session_maker = sessionmaker(bind=self.__engine,
                                     expire_on_commit=False)
        session_scoped = scoped_session(session_maker)
        self.__session = session_scoped()

    def close(self):
        """Private session attribute
        """
        self.__session.close()
