#!/usr/bin/python3
"""This module is a script that takes in arguments and displays all values in
   the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.
   This script provides safety from SQL INJECTION ATTACKS
"""
import MySQLdb
import sys


def my_filter_states(username, password, host, port, dbname, searchkey):
    """This function connects to the locally hosted database and queries it
       securely by providing the `searchkey` as a standalone data, isolated
       from the SQL query
    """
    connection = MySQLdb.connect(user=username,
                                 passwd=password,
                                 host=host,
                                 port=port,
                                 db=dbname)

    cursor = connection.cursor()

    sqlexp = """SELECT id, name FROM states
                WHERE name LIKE BINARY %s"""

    cursor.execute(sqlexp, (searchkey,))

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    connection.close()


if __name__ == "__main__":
    host = 'localhost'
    port = 3306

    args = sys.argv
    username = args[1]
    password = args[2]
    dbname = args[3]
    searchkey = args[4]

    my_filter_states(username, password, host, port, dbname, searchkey)
