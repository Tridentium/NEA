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
# mydb.commit()

# mycursor.execute("""CREATE TABLE Question
#                    (id INT AUTO_INCREMENT PRIMARY KEY,
#                   molecule_name VARCHAR(255),
#                   question_datetime DATETIME,
#                   user_id INT,
#                   outcome BOOL,
#                   FOREIGN KEY (user_id) REFERENCES Student(id));
#                   """)

# mydb.commit()

def createUser(user_name, password, first_name, last_name, email, user_class, teacher_bool):

    mydb = mysql.connector.connect(
      host="localhost",
      user="Admin",
      password="Perfectnova123!",
      database = "testerdb"
      )   

    if teacher_bool:
      teacher_bool = 1
    else:
      teacher_bool = 0
    
    mycursor = mydb.cursor()
    mycursor.execute(f"""INSERT INTO Student (user_name, password, email, first_name, last_name, user_class, Teacher)
                     VALUES('{user_name}', '{password}', '{email}', '{first_name}', '{last_name}', '{user_class}', '{teacher_bool}');""")
    mydb.commit()
    
def returnUserPassword(user_name):
  
    mydb = mysql.connector.connect(
      host="localhost",
      user="Admin",
      password="Perfectnova123!",
      database = "testerdb"
      )   

    mycursor = mydb.cursor()
    mycursor.execute(f"""SELECT password FROM Student WHERE user_name = '{user_name}'""")
    return mycursor.fetchall()[0][0]

def returnUserEmail(user_name):
  
    mydb = mysql.connector.connect(
      host="localhost",
      user="Admin",
      password="Perfectnova123!",
      database = "testerdb"
      )   

    mycursor = mydb.cursor()
    mycursor.execute(f"""SELECT email FROM Student WHERE user_name = '{user_name}'""")
    return mycursor.fetchall()[0][0]

def returnUserClass(user_name):
  
    mydb = mysql.connector.connect(
      host="localhost",
      user="Admin",
      password="Perfectnova123!",
      database = "testerdb"
      )   

    mycursor = mydb.cursor()
    mycursor.execute(f"""SELECT user_class FROM Student WHERE user_name = '{user_name}'""")
    return mycursor.fetchall()[0][0]

def returnUserID(user_name):
  
    mydb = mysql.connector.connect(
      host="localhost",
      user="Admin",
      password="Perfectnova123!",
      database = "testerdb"
      )   

    mycursor = mydb.cursor()
    mycursor.execute(f"""SELECT id FROM Student WHERE user_name = '{user_name}'""")
    return mycursor.fetchall()[0][0]

def returnUserTeacherStatus(user_name):
  
    mydb = mysql.connector.connect(
      host="localhost",
      user="Admin",
      password="Perfectnova123!",
      database = "testerdb"
      )   

    mycursor = mydb.cursor()
    mycursor.execute(f"""SELECT Teacher FROM Student WHERE user_name = '{user_name}'""")
    return mycursor.fetchall()[0][0]

def createQuestion(molecule_name, question_datetime, user_id, outcome):

    mydb = mysql.connector.connect(
      host="localhost",
      user="Admin",
      password="Perfectnova123!",
      database = "testerdb"
      )   

    mycursor = mydb.cursor()
    mycursor.execute(f"""INSERT INTO Question (molecule_name, question_datetime, user_id, outcome)
                     VALUES('{molecule_name}', '{question_datetime}', '{user_id}', '{outcome}');""")
    mydb.commit()

def getQuestionsAnsweredByUser(user_name):
  mydb = mysql.connector.connect(
    host="localhost",
    user="Admin",
    password="Perfectnova123!",
    database = "testerdb"
    )   

  mycursor = mydb.cursor()
  mycursor.execute(f"""SELECT Question.molecule_name, Question.outcome FROM Question, Student WHERE Question.user_id = Student.id AND Student.user_name = '{user_name}' LIMIT 5""")
  return mycursor.fetchall()

def getStudentsByClass(user_class):
  mydb = mysql.connector.connect(
    host="localhost",
    user="Admin",
    password="Perfectnova123!",
    database = "testerdb"
    )   

  mycursor = mydb.cursor()
  mycursor.execute(f"""SELECT user_name FROM Student WHERE user_class= '{user_class}'""")
  return mycursor.fetchall()

def getExistingStudentNames():
  mydb = mysql.connector.connect(
    host="localhost",
    user="Admin",
    password="Perfectnova123!",
    database = "testerdb"
    )   

  mycursor = mydb.cursor()
  mycursor.execute(f"""SELECT user_name FROM Student""")
  usernameList = []
  for i in mycursor.fetchall():
    usernameList.append(i[0])
  return usernameList
