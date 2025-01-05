import pyodbc 
cnxn = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};"
                      "Server=localhost;"
                      "Database=NEATestDb;"
                      "Trusted_Connection=yes;"
                      "TrustServerCertificate:yes;"
                      "Encrypt:no;")


cursor = cnxn.cursor()
cursor.execute('SELECT * FROM Table')

for row in cursor:
    print('row = %r' % (row,))