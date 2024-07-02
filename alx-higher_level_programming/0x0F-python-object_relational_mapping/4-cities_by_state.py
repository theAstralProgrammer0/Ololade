#!/usr/bin/python3
"""This module is a script that lists all `cities` from the database
   `hbtn_0e_4_usa`
"""
import MySQLdb
import sys
import textwrap


def cities_by_state(username, password, host, port, dbname):
    """This function connects to the locally hosted database and queries it
       for the desired `cities` using the `id` of the `states` their related to
    """
    connection = MySQLdb.connect(user=username,
                                 passwd=password,
                                 host=host,
                                 port=port,
                                 db=dbname)

    cursor = connection.cursor()

    sqlexp = """SELECT DISTINCT c.id, c.name, s.name FROM cities c
                JOIN states s ON c.state_id = s.id
                ORDER BY c.id ASC
             """

    cursor.execute(sqlexp)

    results = cursor.fetchall()
    for result in results:
        print(result)

    cursor.close()
    connection.close()


if __name__ == "__main__":
    host = 'localhost'
    port = 3306

    args = sys.argv
    username = args[1]
    password = args[2]
    dbname = args[3]

    cities_by_state(username, password, host, port, dbname)
