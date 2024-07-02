#!/usr/bin/python3
"""This module is a script that lists all `State` objects from the database
   `hbtn_0e_6_usa`
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


def fetch_all(url):
    """This is a function that fetches all `State` objects from the database"""
    # create engine
    engine = create_engine(url, pool_pre_ping=True)
    # create all schemas from metadata
    Base.metadata.create_all(engine)
    # create session (bind to engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # use session.query(ObjSchema)
    states = session.query(State).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

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
    fetch_all(url)
