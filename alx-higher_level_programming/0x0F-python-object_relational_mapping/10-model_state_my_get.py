#!/usr/bin/python3
"""This module is a script that prints the `State` object's `id` when the
   `name` is passed as argument. It retrieves the info from the database
   `hbtn_0e_6_usa`
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


def get_state_id(url, searchkey):
    """This is a function that fetches the `State` object's id - whose `name`
       has been passed as an argument - from the database
    """
    engine = create_engine(url, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State)\
                   .filter(State.name.like('{}'.format(searchkey)))\
                   .first()

    if (state):
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    dialect = 'mysql'
    dbapi = 'mysqldb'
    user = argv[1]
    pwd = argv[2]
    host = 'localhost'
    port = 3306
    dbname = argv[3]
    searchkey = argv[4]

    url = "{}+{}://{}:{}@{}:{}/{}".format(dialect,
                                          dbapi,
                                          user,
                                          pwd,
                                          host,
                                          port,
                                          dbname)
    get_state_id(url, searchkey)
