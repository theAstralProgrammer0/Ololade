#!/usr/bin/python3
"""This module contains the class definition of a `State` and an instance
   `Base = declarative_base()`
"""
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """This schema of the `State` Table stored in the database
    """
    __tablename__ = 'states'
    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)

    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
