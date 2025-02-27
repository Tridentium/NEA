import mysql.connector

# Commented functions were run to generate each individual table

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="Admin",
#   password="MantasNEApwd987!",
#   database = "testerdb"
# )

# mycursor = mydb.cursor()

# mycursor.execute("""CREATE TABLE Student
#                  (id INT AUTO_INCREMENT PRIMARY KEY,
#                  user_name VARCHAR(255),
#                  password VARCHAR(255),
#                  email VARCHAR(255),
#                  first_name VARCHAR(255),
#                  last_name VARCHAR(255),
#                  user_class VARCHAR(255),
#                  Teacher TINYINT);
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

# Define a function to create a user during the registration process
def createUser(user_name, password, first_name, last_name, email, user_class, teacher_bool):

    # Connect to the database
    mydb = mysql.connector.connect(
      host="localhost",
      user="Admin",
      password="MantasNEApwd987!",
      database = "testerdb"
      )   

    # Convert the teacher_bool to a storable value
    if teacher_bool:
      teacher_bool = 1
    else:
      teacher_bool = 0
    
    # Create the user using the provided values
    mycursor = mydb.cursor()
    mycursor.execute("""INSERT INTO Student (user_name, password, email, first_name, last_name, user_class, Teacher)
                     VALUES(%s, %s, %s, %s, %s, %s, %s);""",
                     (user_name, password, email, first_name, last_name, user_class, teacher_bool,))
    mydb.commit()

# Define a function to return the password of a specific user
def returnUserPassword(user_name):

    # Connect to the database
    mydb = mysql.connector.connect(
      host="localhost",
      user="Admin",
      password="MantasNEApwd987!",
      database = "testerdb"
      )   

    # Return the password of the provided user
    mycursor = mydb.cursor()
    mycursor.execute("""SELECT password FROM Student WHERE user_name = %s""", (user_name,))
    return mycursor.fetchall()[0][0]

# Define a function to return the email of a specific user
def returnUserEmail(user_name):

    # Connect to the database
    mydb = mysql.connector.connect(
      host="localhost",
      user="Admin",
      password="MantasNEApwd987!",
      database = "testerdb"
      )   

    # Return the email of the provided user
    mycursor = mydb.cursor()
    mycursor.execute("""SELECT email FROM Student WHERE user_name = %s""", (user_name,))
    return mycursor.fetchall()[0][0]

# Define a function to return the class of a specific user
def returnUserClass(user_name):

    # Connect to the database
    mydb = mysql.connector.connect(
      host="localhost",
      user="Admin",
      password="MantasNEApwd987!",
      database = "testerdb"
      )   

    # Return the class of the provided user
    mycursor = mydb.cursor()
    mycursor.execute("""SELECT user_class FROM Student WHERE user_name = %s""", (user_name,))
    return mycursor.fetchall()[0][0]

# Define a function to return the ID of a specific user
def returnUserID(user_name):

    # Connect to the database
    mydb = mysql.connector.connect(
      host="localhost",
      user="Admin",
      password="MantasNEApwd987!",
      database = "testerdb"
      )   

    # Return the ID of the provided user
    mycursor = mydb.cursor()
    mycursor.execute("""SELECT id FROM Student WHERE user_name = %s""", (user_name,))
    return mycursor.fetchall()[0][0]

# Define a function to return whether or not a certain user is a teacher
def returnUserTeacherStatus(user_name):

    # Connect to the database
    mydb = mysql.connector.connect(
      host="localhost",
      user="Admin",
      password="MantasNEApwd987!",
      database = "testerdb"
      )   

    # Return teacher status of the provided user
    mycursor = mydb.cursor()
    mycursor.execute("""SELECT Teacher FROM Student WHERE user_name = %s""", (user_name,))
    return mycursor.fetchall()[0][0]

# Define a function to create a question
def createQuestion(molecule_name, question_datetime, user_id, outcome):

    # Connect to the database
    mydb = mysql.connector.connect(
      host="localhost",
      user="Admin",
      password="MantasNEApwd987!",
      database = "testerdb"
      )   

    # Create the question and commit the change to the database
    mycursor = mydb.cursor()
    mycursor.execute("""INSERT INTO Question (molecule_name, question_datetime, user_id, outcome)
                     VALUES(%s, %s, %s, %s);""",
                     (molecule_name, question_datetime, user_id, outcome,))
    mydb.commit()

# Define a function to return the questions answered by a specific user
def getQuestionsAnsweredByUser(user_name):
  
  # Connect to the database
  mydb = mysql.connector.connect(
    host="localhost",
    user="Admin",
    password="MantasNEApwd987!",
    database = "testerdb"
    )   

  # Return the last 5 questions answered by the specified user
  mycursor = mydb.cursor()
  mycursor.execute("""SELECT Question.molecule_name, Question.outcome FROM Question, Student WHERE Question.user_id = Student.id AND Student.user_name = %s LIMIT 5""", (user_name,))
  return mycursor.fetchall()

# Define a function to return the students in a class
def getStudentsByClass(user_class):
  
  # Connect to the database
  mydb = mysql.connector.connect(
    host="localhost",
    user="Admin",
    password="MantasNEApwd987!",
    database = "testerdb"
    )   

  # Return the list of students in the specified class
  mycursor = mydb.cursor()
  mycursor.execute("""SELECT user_name FROM Student WHERE user_class= %s""", (user_class,))
  return mycursor.fetchall()

# Define a function to get a list of all assigned student names for validation during login
def getExistingStudentNames():
  
  # Connect to the database
  mydb = mysql.connector.connect(
    host="localhost",
    user="Admin",
    password="MantasNEApwd987!",
    database = "testerdb"
    )   

  # Retrieve and return the list of usernames as a list
  mycursor = mydb.cursor()
  mycursor.execute("""SELECT user_name FROM Student""")
  usernameList = []
  for i in mycursor.fetchall():
    usernameList.append(i[0])
  return usernameList