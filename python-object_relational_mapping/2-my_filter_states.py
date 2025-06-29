#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
Usage: ./2-my_filter_states.py <username> <password> <database> <state_name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Parse command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create cursor and execute query using format (WARNING: not safe from SQL injection)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)

    # Fetch and print all rows
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close connection
    cur.close()
    db.close()
