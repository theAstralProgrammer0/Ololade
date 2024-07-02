#!/usr/bin/python3
"""This is a module that contains the class definition of the City Schema"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """This class descibes a City object in the database"""
    __tablename__ = 'cities'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                unique=True,
                nullable=False
                )

    name = Column(String(128), nullable=False)

    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      autoincrement=False,
                      nullable=False
                      )

