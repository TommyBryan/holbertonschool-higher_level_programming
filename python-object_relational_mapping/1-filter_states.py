#!/usr/bin/python3
"""
List all states starting with 'N' from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user = username,
        passwd = password,
        db = db_name
    )

    # Create cursor object
    cursor = db.cursor()

    # Execute SQL query to select states with name starting with 'N'
    cursor.execute("SELECT * FROM states \
                   WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    # Fetch and print each result
    for row in cursor.fetchall():
        print(row)

    # Clean up
    cursor.close()
    db.close()
