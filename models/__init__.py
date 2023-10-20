#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from .engine.file_storage import FileStorage
from .engine.db_storage import DBStorage


storageType = getenv('HBNB_TYPE_STORAGE')
if storageType == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
