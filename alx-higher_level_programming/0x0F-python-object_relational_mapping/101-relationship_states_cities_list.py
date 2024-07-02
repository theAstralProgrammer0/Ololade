#!/usr/bin/python3
"""This module contains a script that lists all `State` objects, and
   corresponding `City` objects, contained in the database `hbtn_0e_101_usa`
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State


def state_city_rel(uri):
    """This function accesses the database and prints the state and city
       info.
       Format:
            <state id>: <state name>
                <city id>: <city name>
       Arg:
        uri - Uniform Resource Identifier
    """
    engine = create_engine(uri, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State)\
                    .outerjoin(City)\
                    .order_by(State.id)\
                    .all()
    # states = session.query(State)\
    #                 .join(City, isouter=True)\
    #                 .order_by(State.id)\
    #                 .all()

    i = 0
    while i < len(states):
        state = states[i]
        print("{}: {}".format(state.id,
                              state.name
                              ))
        j = 0
        while j < len(state.cities):
            city = state.cities[j]
            print("\t{}: {}".format(city.id,
                                    city.name
                                    ))
            j += 1
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
