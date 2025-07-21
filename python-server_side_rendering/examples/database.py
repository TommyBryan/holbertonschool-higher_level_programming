import sqlite3

"""
Local Memory DB
conn = sqlite3.connect(':memory:')
"""
#  Connect to database
conn = sqlite3.connect('customer.db')

#  Create cursor
cursor = conn.cursor()

#  Create table
cursor.execute("""CREATE TABLE customers (
               first_name text,
               last_name text,
               email text
            )""")

"""
Data types:
NULL
INTEGER
REAL
TEXT
BLOB
"""

#  Commit our command
conn.commit()

#  Close our connection
conn.close()
