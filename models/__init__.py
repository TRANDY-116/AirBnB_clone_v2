#!/usr/bin/python3
"""
This module initializes storage based on the environment variable HBNB_TYPE_STORAGE.
"""

import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

# Set HBNB_TYPE_STORAGE environment variable to 'db' or 'fs' accordingly

if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()

