import sqlite3

"""
Local Memory DB
conn = sqlite3.connect(':memory:')
"""
#  Connect to database
conn = sqlite3.connect('customer.db')

#  Create cursor
cursor = conn.cursor()

many_customers = [
                    ('Wes', 'Brown', 'wes@gmail.com'),
                    ('Steph', 'Kuewa', 'Steph@gmail.com'),
                    ('Dan', 'Kuso', 'dan@gmail.com'),
                  ]

#  Insert many values to table
cursor.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

""" Insert  single values into table
cursor.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@gmail.com')")
"""

print("command executed successfully..")

#  Commit our command
conn.commit()

#  Close our connection
conn.close()
