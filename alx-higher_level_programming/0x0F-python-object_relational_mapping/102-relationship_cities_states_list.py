#!/usr/bin/python3
"""This module contains a script that lists all `State` objects, and
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State


def state_city_rel(uri):
    """This function accesses the database and prints the state and city
    """
    engine = create_engine(uri, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    cities = session.query(City)\
                    .join(State)\
                    .filter(City.state_id == State.id)\
                    .order_by(City.id)\
                    .all()

    i = 0
    while i < len(cities):
        city = cities[i]
        print("{}: {} -> {}".format(city.id,
                                    city.name,
                                    city.state.name
                                    ))
        i += 1

    session.commit()
    session.close()


if __name__ == "__main__" and len(argv) == 4:
    dialect = 'mysql'
    dbapi = 'mysqldb'
    host = 'localhost'
    port = 3306
    user, pwd, dbname = argv[1:]

    uri = "{}+{}://{}:{}@{}:{}/{}".format(dialect,
                                          dbapi,
                                          user,
                                          pwd,
                                          host,
                                          port,
                                          dbname
                                          )

    state_city_rel(uri)
