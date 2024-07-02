#!/usr/bin/python3
"""This module is a script that adds the `State` object “Louisiana” to the
   database `hbtn_0e_6_usa`
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


def add_state(url, state):
    """This is a function creates a new `State` instance whose `name` field is
       “Louisiana”, persists it to the database and prints its `id`
    """
    engine = create_engine(url, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    newstate = State()
    newstate.name = state

    session.add(newstate)

    session.commit()

    print("{}".format(newstate.id))

    session.close()


if __name__ == "__main__":
    dialect = 'mysql'
    dbapi = 'mysqldb'
    user = argv[1]
    pwd = argv[2]
    host = 'localhost'
    port = 3306
    dbname = argv[3]
    state = 'Louisiana'

    url = "{}+{}://{}:{}@{}:{}/{}".format(dialect,
                                          dbapi,
                                          user,
                                          pwd,
                                          host,
                                          port,
                                          dbname)

    add_state(url, state)