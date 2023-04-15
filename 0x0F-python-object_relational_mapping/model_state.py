#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative_base()

"""
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, MetaData

meta_data = MetaData()
the_base = declarative_base(metadata=meta_data)

class State(the_base):
    """
    Class with id and name attributes of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
