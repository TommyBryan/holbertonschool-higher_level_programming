#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
where name matches the argument (safe from SQL injection).
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    # Execute a safe query using parameterized inputs
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch and print results
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
