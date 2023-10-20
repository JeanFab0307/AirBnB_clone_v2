#!/usr/bin/python3
"""New engine for a DB storage"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review



class DBStorage:
    """Class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        storageType = getenv('HBNB_TYPE_STORAGE')   
        db_uri = 'mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db)
        self.__engine = create_engine(db_uri, pool_pre_ping=True)

    def all(self, cls=None):
        """Query the current database session"""
        if not cls:
            pass
        else:
            query = self.__session.query(cls).all()
        return query
            
            
    def new(self, obj):
        """Add the obj to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit allchanges of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
