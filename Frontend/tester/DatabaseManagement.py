import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Admin",
  password="Perfectnova123!",
  database = "testerdb"
)

mycursor = mydb.cursor()

# mycursor.execute("""CREATE TABLE Student
#                  (id INT AUTO_INCREMENT PRIMARY KEY,
#                  user_name VARCHAR(255),
#                  password VARCHAR(255),
#                  email VARCHAR(255),
#                  first_name VARCHAR(255),
#                  last_name VARCHAR(255),
#                  user_class VARCHAR(255));
#                  """)

def createUser(user_name, password, first_name, last_name, email, user_class):

    mydb = mysql.connector.connect(
      host="localhost",
      user="Admin",
      password="Perfectnova123!",
      database = "testerdb"
      )   

    mycursor = mydb.cursor()
    mycursor.execute(f"""INSERT INTO Student (user_name, password, email, first_name, last_name, user_class)
                     VALUES('{user_name}', '{password}', '{first_name}', '{last_name}', '{email}', '{user_class}');""")
    mydb.commit()
    
print(mycursor.execute("""INSERT INTO Student (user_name, password, email, first_name, last_name, user_class)
                       VALUES('TestUser', 'abc', 'value@gmail.com', 'FirstName', 'LastName', 'Class1');"""))
mydb.commit()
mycursor.execute("""DELETE FROM Student WHERE id != 1""")
print(mycursor.fetchall())