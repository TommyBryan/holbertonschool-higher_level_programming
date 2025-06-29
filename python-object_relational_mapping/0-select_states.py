#!/usr/bin/python3
"""
List all states form the database hbtn_0e_0_usa.
Connects using MySQLdb and prints rows sorted by id.
"""


import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL database on localhost:3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        password=mysql_password,
        db= database_name
    )

    # Create a cursor to execute queries
    cursor = db.cursor()

    # Execute query: select all states ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print results
    for row in cursor.fetchall():
        print(row)

    # Clean up
    cursor.close()
    db.close()
