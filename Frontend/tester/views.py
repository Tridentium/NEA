from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import tester.Molecule as MoleculeGenerator
import tester.SVGtest as SVGGenerator
import tester.DatabaseManagement as models
import tester.utils as utils
from django.urls import reverse
import django.utils.timezone as time
import time as systime
import datetime
import re

# Define index view
def index(request):
    
    # Pass required variables to page
    context = {"userclass": models.returnUserClass(request.session["current_user"]), "user_name": request.session["current_user"]}
    return render(request, "tester/index.html", context)

# Define login view
def login(request):
    
    # If an error message is present, pass it to page, and if not pass nothing
    try:
        context = {"ErrorMessage": request.session["ErrorMessage"]}
    except:
        context = {"ErrorMessage": ""}
    
    # Reset error message to ensure that it isn't repeatedly displayed to the user
    request.session["ErrorMessage"] = ""
    return render(request, "tester/login.html", context)

# Define register view
def register(request):
    
    # If an error message is present, pass it to page, and if not pass nothing
    try:
        context = {"ErrorMessage": request.session["ErrorMessage"]}
    except:
        context = {"ErrorMessage": ""}
    
    # Reset error message to ensure that it isn't repeatedly displayed to the user
    request.session["ErrorMessage"] = ""
    return render(request, "tester/register.html", context)

# Define profile view
def profile(request):
    
    # Access the data associated with the current user
    user_name = request.session["current_user"]
    
    # Determine whether the current user is a teacher to allow them to access their class data page
    if models.returnUserTeacherStatus(request.session["current_user"]):
        teacherclass = models.returnUserClass(request.session["current_user"])
    else:
        teacherclass = ""
    
    # Pass the data to the page
    context = {"user_name" : user_name, "email" : models.returnUserEmail(user_name), "class" : models.returnUserClass(user_name), "teacherclass": teacherclass}
    return render(request, "tester/profile.html", context)

# Define the student data view
def studentdata(request):
    
    # Access the teacher's class and return the list of students in that class
    teacherclass = models.returnUserClass(request.session["current_user"])
    unformattednames = models.getStudentsByClass(teacherclass)
    formattednames = []
    for i in unformattednames:
        formattednames.append(i[0])
    request.session["studentnames"] = formattednames
    
    # If the list of student names if present, pass it to the page
    try:
        studentnames = str(request.session["studentnames"]).replace("'", "")
        studentnames = studentnames.replace("[", "")
        studentnames = studentnames.replace("]", "")
        context = {"studentnames": studentnames}
        
        # If the teacher has selected a student, pass their questions answered to the page
        try:
            requestedstudentdata = str(request.session["requestedstudentdata"]).replace("'", "")
            requestedstudentdata = requestedstudentdata.replace("[", "")
            requestedstudentdata = requestedstudentdata.replace("]", "")
            context["requestedstudentdata"] = requestedstudentdata
        except:
            pass
    except:
        context = {}
    return render(request, "tester/studentdata.html", context)

# Define the test settings view
def testsettings(request):
    return render(request, "tester/testsettings.html", {})

# Define the action of the settestsettings POST request
def settestsettings(request):
    
    # Recieve the data the user has selected on the settings page and save
    selected_length = request.POST["MolLength"]
    valid_groups = request.POST.getlist("FuncGroup[]")
    request.session['list'] = valid_groups
    request.session["requested_length"] = selected_length
    request.session["max_test_length"] = request.POST["TestLength"]
    
    # Reset question number
    request.session["questions_completed"] = 0
    
    # Redirect to the question page
    return HttpResponseRedirect(reverse("tester:question", args=(selected_length, )))

# Define the question view
def question(request, selected_length):
    
    # Access the current question number
    currentQuestionNo = request.session["questions_completed"]
    
    # Access the list of groups defined during the test settings selection
    valid_groups = request.session['list']
    
    # Generate a new molecule using those parameters
    testMolecule = MoleculeGenerator.Molecule(selected_length, valid_groups)
    
    # Generate the new molecule's name
    output = testMolecule.generate()
    
    # If a value is returned from the generation function an error has occured so pass the error and redirect to the testsettings page
    if output:
        context = {"errormessage" : output}
        return render(request, "tester/testsettings.html", context)
    
    else:
        
        # Generate the molecule's name
        nameForPrinting  = testMolecule.outputMolecule()
        
        # Generate the molecule's render as an SVG
        svg = SVGGenerator.createSVG(testMolecule.getLength(), testMolecule)
        
        # Save the SVG and name
        request.session['molecule_name'] = nameForPrinting
        request.session['image'] = svg
        
        # Pass the name, svg and question number to the page
        context = {"molecule_name" : nameForPrinting, "image" : svg, "currentQuestionNo": currentQuestionNo + 1}
        
        return render(request, "tester/question.html", context)

# Define the answerquestion POST request
def answerquestion(request):
    
    # Access and save the user's answer
    user_answer = request.POST.get('Answer', False)
    request.session['user_answer'] = user_answer
    
    # Redirect to the answer page
    return HttpResponseRedirect(reverse("tester:answer"))

# Define the answer view
def answer(request):
    
    # Increment the question number
    request.session["questions_completed"] += 1
    
    # Access the user answer and correct name
    user_answer = request.session['user_answer']
    nameForPrinting = request.session['molecule_name']
    
    # Check if they are equal and store the outcome
    if user_answer.lower() == nameForPrinting.lower():
        outcome = 1
    else:
        outcome = 0
    
    # Get the user's ID and use it to store the information about the question and its result
    user_name = request.session["current_user"]
    user_id = models.returnUserID(user_name)
    current_time = datetime.datetime.fromtimestamp(systime.mktime(systime.gmtime()))
    models.createQuestion(nameForPrinting, current_time, user_id, outcome)
    
    # Access the svg
    svg = request.session['image']
    
    # Change the text on the next question button and the page it links to based on whether the test has ended or not
    if int(request.session["questions_completed"]) < int(request.session["max_test_length"]):
        button_text = "Next Question"
        request.session["test_over"] = "n"
    else:
        button_text = "Finish Test"
        request.session["test_over"] = "y"
    
    # Pass the answer information to the page to be displayed to the user
    context = {"user_answer" : user_answer, "nameForPrinting" : nameForPrinting, "svg" : svg, "button_text" : button_text}
    return render(request, "tester/answer.html", context)

# Define the register account POST process
def registeraccount(request):
    
    # First validation check that the emails and passwords match
    if request.POST["Email"] == request.POST["ConfirmEmail"] and request.POST["Password"] == request.POST["ConfirmPassword"]:
        
        # Second check to validate email format
        if utils.validateEmail(request.POST["Email"]):
            
            # Third check to ensure password format correct (contains at least 1 lowercase letter, uppercase letter and digit)
            pwrd = request.POST["Password"]
            if any(i.isdigit() for i in pwrd) and any(i == i.lower() and not i.isdigit() for i in pwrd) and any(i == i.upper() and not i.isdigit() for i in pwrd):
                
                # Final check to ensure username does not already exist
                if request.POST["Username"] not in models.getExistingStudentNames():
                    
                    # Create user (with error handling to catch unchecked POST checkbox inconsistency)
                    try:
                        models.createUser(request.POST["Username"], 
                                        request.POST["Password"], 
                                        request.POST["Firstname"], 
                                        request.POST["Lastname"],
                                        request.POST["Email"],
                                        request.POST["Class"],
                                        bool(request.POST["TeacherBool"]),)
                        request.session["ErrorMessage"] = ""
                        return HttpResponseRedirect(reverse("tester:login"))
                    except:
                        models.createUser(request.POST["Username"], 
                                        request.POST["Password"], 
                                        request.POST["Firstname"], 
                                        request.POST["Lastname"],
                                        request.POST["Email"],
                                        request.POST["Class"],
                                        False,)
                        request.session["ErrorMessage"] = ""
                        return HttpResponseRedirect(reverse("tester:login"))
                
                # If check failed return appropriate error message and redirects to register page
                else:
                    request.session["ErrorMessage"] = "Username already exists"
                    return HttpResponseRedirect(reverse("tester:register"))
            
            # If check failed return appropriate error message and redirects to register page
            else:
                request.session["ErrorMessage"] = "Password must contain a digit, uppercase and lowercase letter"
                return HttpResponseRedirect(reverse("tester:register"))
        
        # If check failed return appropriate error message and redirects to register page
        else:
            request.session["ErrorMessage"] = "Invalid Email"
            return HttpResponseRedirect(reverse("tester:register"))
    
    # If check failed return appropriate error message and redirects to register page
    elif request.POST["Email"] == request.POST["ConfirmEmail"]:
        request.session["ErrorMessage"] = "Passwords Do Not Match"
        return HttpResponseRedirect(reverse("tester:register"))
    
    # If check failed return appropriate error message and redirects to register page
    else:
        request.session["ErrorMessage"] = "Emails Do Not Match"
        return HttpResponseRedirect(reverse("tester:register"))

# Define the loginaccount POST process
def loginaccount(request):
    
    # Error handling to catch empty inputs
    try:
        
        # Check whether or not password is correct and redirect to the correct page as necessary
        if models.returnUserPassword(request.POST["Username"]) == request.POST["Password"]:
            request.session["current_user"] = request.POST["Username"]
            return HttpResponseRedirect(reverse("tester:profile"))
        else:
            request.session["ErrorMessage"] = "Invalid Username Or Password"
            return HttpResponseRedirect(reverse("tester:login"))
    except:
        request.session["ErrorMessage"] = "Invalid Username Or Password"
        return HttpResponseRedirect(reverse("tester:login"))

# Define the logout process
def logoutaccount(request):
    
    # Clear the current_user value
    request.session["current_user"] = ""
    return HttpResponseRedirect(reverse("tester:login"))

# Define the new question/finish test redirect
def newquestion(request):
    
    # Redirect to question if test not over and to settings page if test is
    if request.session["test_over"] == "n":
        return HttpResponseRedirect(reverse("tester:question", args=(request.session["requested_length"], )))
    else:
        return HttpResponseRedirect(reverse("tester:testsettings"))
    
# Define the getstudentdatafromstudenname view
def getstudentdatafromstudenname(request):
    
    # Store the most recent 5 questions answered by the user in question
    request.session["requestedstudentdata"] = models.getQuestionsAnsweredByUser(request.POST["studentname"])
    return HttpResponseRedirect(reverse("tester:studentdata"))
