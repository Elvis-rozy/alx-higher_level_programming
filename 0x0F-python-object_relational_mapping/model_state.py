#!/usr/bin/python3
"""
-- Contains the class definition of a State and an instance 
   Base = declarative_base():
-- State class:
-- inherits from Base Tips
-- links to the MySQL table states
-- class attribute id that represents a column of an auto-generated, 
   unique integer, can't be null and is a primary key
-- class attribute name that represents a column of a string with 
   maximum 128 characters and can't be null
-- You must use the module SQLAlchemy
-- Your script should connect to a MySQL server running on 
   localhost at port 3306
-- WARNING: all classes who inherit from Base must be imported 
   before calling Base.metadata.create_all(engine)

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
