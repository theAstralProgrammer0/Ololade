#!/usr/bin/python3
"""This is a module that prints all the cities associated to a state"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine


def print_cities(url):
    """This function prints all the cities using the state_id"""
    engine = create_engine(url, pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id.asc()).all()
    for city in cities:
        print("{}: ({}) {}".format(session.query(State)
                                          .filter(State.id == city.state_id)
                                          .first()
                                          .name, city.id, city.name))


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
    print_cities(url)
