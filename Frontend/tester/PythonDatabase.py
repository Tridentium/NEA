import sqlite3

cursor = cnxn.cursor()
cursor.execute('SELECT * FROM Table')

for row in cursor:
    print('row = %r' % (row,))