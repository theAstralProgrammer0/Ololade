#!/usr/bin/python3
"""This module lists all states from the database `hbtn_0e_0_usa`
   non-interatively
"""
import MySQLdb
import sys


def select_states(username, password, host, port, dbname):
    """This function selects the `id` and `name` columns in the `states` table
       and displays them in ascending order of the `id`
    """
    connection = MySQLdb.connect(
                                user=username,
                                passwd=password,
                                host=host,
                                port=port,
                                db=dbname)
    cursor = connection.cursor()

    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

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
    select_states(username, password, host, port, dbname)
