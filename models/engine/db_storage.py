#!/usr/bin/python3
"""New engine for a DB storage"""
from sqlalchemy import create_engine


class DBStorage:
    """Class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://HBNB_MYSQL_USER:HBNB_MYSQL_PWD@HBNB_MYSQL_HOST/HBNB_MYSQL_DB',
        pool_pre_ping=True)

    def all(self, cls=None):
        """Query the current database session"""
    
    def new(self, obj):
        """Add the obj to the current database session"""

    def save(self):
        """Commit allchanges of the current database session"""

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""

    def reload(self):
        """Create all tables in the database"""
        