import sqlite3

"""
Local Memory DB
conn = sqlite3.connect(':memory:')
"""
#  Connect to database
conn = sqlite3.connect('customer.db')

#  Create cursor
cursor = conn.cursor()

# Query the Database
cursor.execute("SELECT * FROM customers")
#  print(cursor.fetchone())
#  print(cursor.fetchmany(3))
#  print(cursor.fetchall())

items = cursor.fetchall()
"""
print(items)
print("command executed successfully..")
"""
for item in items:
    print(item[0] + " | " + item[1] + " | "
    " | " + item[2])

#  Commit our command
conn.commit()

#  Close our connection
conn.close()
