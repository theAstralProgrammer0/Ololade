#!/usr/bin/python3
"""This module is a script that takes in the `name` of a state as an argument
   and lists all `cities` of that state, using the database `hbtn_0e_4_usa`
"""
import MySQLdb
import sys


def filter_cities(username, password, host, port, dbname, city_fltr):
    """This function connects to a database and queries it to get the filtered
       `cities`
    """
    connection = MySQLdb.connect(user=username,
                                 passwd=password,
                                 host=host,
                                 port=port,
                                 db=dbname)

    cursor = connection.cursor()

    sqlexp = """SELECT c.name FROM cities c
                JOIN states s
                ON c.state_id = s.id AND s.name LIKE BINARY %s
             """
    cursor.execute(sqlexp, (city_fltr,))

    cities = cursor.fetchall()
    if len(cities):
        i = 0
        while i < len(cities):
            if i < len(cities) - 1:
                print("{}, ".format(cities[i][0]), end="")
            else:
                print("{}".format(cities[i][0]))
            i += 1
    else:
        print()

    cursor.close()
    connection.close()


if __name__ == "__main__":
    host = 'localhost'
    port = 3306

    args = sys.argv
    username = args[1]
    password = args[2]
    dbname = args[3]
    city_fltr = args[4]

    filter_cities(username, password, host, port, dbname, city_fltr)
