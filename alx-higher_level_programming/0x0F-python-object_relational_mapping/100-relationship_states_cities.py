#!/usr/bin/python3
"""This module contains a python script that creates the `State`
   “California” with the `City` “San Francisco” from the database
   `hbtn_0e_100_usa`: (100-relationship_states_cities.py)
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State


def state_city_rel(uri, s_name, c_name):
    """This function instantiates new `State` and `City` objects, relates the
       new `city` to the new `state`, and adds both entries to the database
    """
    engine = create_engine(uri)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    _state = State(name=s_name)
    _city = City(name=c_name)
    _state.cities.append(_city)
    session.add(_state)

    # _state = State(name=s_name)
    # _city = City(name=c_name, state=_state)
    # session.add(_city)
    # session.add(_state)

    session.commit()
    session.close()


if __name__ == "__main__" and len(argv) == 4:
    dialect = 'mysql'
    dbapi = 'mysqldb'
    user, pwd, dbname = argv[1:]
    host = 'localhost'
    port = 3306
    s_name = 'California'
    c_name = 'San Francisco'

    uri = "{}+{}://{}:{}@{}:{}/{}".format(dialect,
                                          dbapi,
                                          user,
                                          pwd,
                                          host,
                                          port,
                                          dbname
                                          )

    state_city_rel(uri, s_name, c_name)
