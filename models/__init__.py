#!/usr/bin/python3
"""This is used to inittialise the packages
"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
