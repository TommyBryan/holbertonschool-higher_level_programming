import sqlite3

"""
Local Memory DB
conn = sqlite3.connect(':memory:')
"""
#  Connect to database
conn = sqlite3.connect('customer.db')

#  Create cursor
cursor = conn.cursor()

cursor.execute("INSERT INTO customers VALUES (Tommyb)")
#  Commit our command
conn.commit()

#  Close our connection
conn.close()
