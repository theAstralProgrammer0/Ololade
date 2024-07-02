#!/usr/bin/python3
"""This module is a script that lists all `State` objects whose `name` has
   the character `a` from the database `hbtn_0e_6_usa`
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


def fetch_filter_a(url):
    """This is a function that fetches the `State` objects whose `name` has
       the character `a` from the database
    """
    engine = create_engine(url, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).all()

    for state in states:
        if (state):
            print("{}: {}".format(state.id, state.name))
        else:
            print("Nothing")

    session.close()


if __name__ == "__main__":
    dialect = 'mysql'
    dbapi = 'mysqldb'
    user = argv[1]
    pwd = argv[2]
    host = 'localhost'
    port = 3306
    dbname = argv[3]

    url = "{}+{}://{}:{}@{}:{}/{}".format(dialect,
                                          dbapi,
                                          user,
                                          pwd,
                                          host,
                                          port,
                                          dbname)
    fetch_filter_a(url)
