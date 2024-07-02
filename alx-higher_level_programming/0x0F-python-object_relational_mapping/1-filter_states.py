#!/usr/bin/python3
"""This module lists all states with a `name` starting with 'N' from the
   database `hbtn_0e_0_usa` non-interactively
"""
import MySQLdb
import sys


def filter_states(username, password, host, port, dbname):
    """This function creates a connection to a MySQL database host server
       (localhost) at port 3306 and executes the SQL Expression to obtain the
       desired result
    """
    connection = MySQLdb.connect(
                                user=username,
                                passwd=password,
                                host=host,
                                port=port,
                                db=dbname)
    cursor = connection.cursor()

    sqlexp = """SELECT id, name FROM states
                WHERE name LIKE BINARY %s
                ORDER BY id ASC
            """
    cursor.execute(sqlexp, ('N%',))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()


if __name__ == "__main__":
    args = sys.argv
    username = args[1]
    password = args[2]
    host = 'localhost'
    port = 3306
    dbname = args[3]
    filter_states(username, password, host, port, dbname)
