from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import tester.NEAConceptsTestt as MoleculeGenerator
import tester.SVGtest as SVGGenerator
import tester.DatabaseManagement as models
import tester.utils as utils
from django.urls import reverse
import django.utils.timezone as time
import time as systime
import datetime
import re

def index(request):
    
    context = {"userclass": models.returnUserClass(request.session["current_user"]), "user_name": request.session["current_user"]}
    return render(request, "tester/index.html", context)

def login(request):
    try:
        context = {"ErrorMessage": request.session["ErrorMessage"]}
    except:
        context = {"ErrorMessage": ""}
    request.session["ErrorMessage"] = ""
    return render(request, "tester/login.html", context)

def register(request):
    try:
        context = {"ErrorMessage": request.session["ErrorMessage"]}
    except:
        context = {"ErrorMessage": ""}
    request.session["ErrorMessage"] = ""
    return render(request, "tester/register.html", context)

def profile(request):
    user_name = request.session["current_user"]
    if models.returnUserTeacherStatus(request.session["current_user"]):
        teacherclass = models.returnUserClass(request.session["current_user"])
    else:
        teacherclass = ""
    context = {"user_name" : user_name, "email" : models.returnUserEmail(user_name), "class" : models.returnUserClass(user_name), "teacherclass": teacherclass}
    return render(request, "tester/profile.html", context)

def studentdata(request):
    
    teacherclass = models.returnUserClass(request.session["current_user"])
    unformattednames = models.getStudentsByClass(teacherclass)
    formattednames = []
    for i in unformattednames:
        formattednames.append(i[0])
    request.session["studentnames"] = formattednames
    
    try:
        studentnames = str(request.session["studentnames"]).replace("'", "")
        studentnames = studentnames.replace("[", "")
        studentnames = studentnames.replace("]", "")
        context = {"studentnames": studentnames}
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

def testsettings(request):
    return render(request, "tester/testsettings.html", {})

def settestsettings(request):
    
    selected_length = request.POST["MolLength"]
    valid_groups = request.POST.getlist("FuncGroup[]")
    request.session['list'] = valid_groups
    request.session["requested_length"] = selected_length
    request.session["max_test_length"] = request.POST["TestLength"]
    request.session["questions_completed"] = 0
    return HttpResponseRedirect(reverse("tester:question", args=(selected_length, )))

def question(request, selected_length):
    
    currentQuestionNo = request.session["questions_completed"]
    
    valid_groups = request.session['list']
    testMolecule = MoleculeGenerator.Molecule(selected_length, valid_groups)
    output = testMolecule.generate()
    if output:
        context = {"errormessage" : output}
        return render(request, "tester/testsettings.html", context)
    else:
        print(testMolecule.functionalGroupName)
        nameForPrinting  = testMolecule.outputMolecule()
        
        svg = SVGGenerator.createSVG(testMolecule.length, testMolecule)
        
        request.session['molecule_name'] = nameForPrinting
        request.session['image'] = svg
        
        context = {"molecule_name" : nameForPrinting, "image" : svg, "currentQuestionNo": currentQuestionNo + 1}
        
        return render(request, "tester/question.html", context)

def answerquestion(request):
    user_answer = request.POST.get('Answer', False)
    request.session['user_answer'] = user_answer
    return HttpResponseRedirect(reverse("tester:answer"))


def answer(request):
    request.session["questions_completed"] += 1
    user_answer = request.session['user_answer']
    nameForPrinting = request.session['molecule_name']
    
    if user_answer.lower() == nameForPrinting.lower():
        outcome = 1
    else:
        outcome = 0
    
    user_name = request.session["current_user"]
    user_id = models.returnUserID(user_name)
    current_time = datetime.datetime.fromtimestamp(systime.mktime(systime.gmtime()))
    print(current_time)
    models.createQuestion(nameForPrinting, current_time, user_id, outcome)
    
    svg = request.session['image']
    if int(request.session["questions_completed"]) < int(request.session["max_test_length"]):
        button_text = "Next Question"
        request.session["test_over"] = "n"
    else:
        button_text = "Finish Test"
        request.session["test_over"] = "y"
    context = {"user_answer" : user_answer, "nameForPrinting" : nameForPrinting, "svg" : svg, "button_text" : button_text}
    
    return render(request, "tester/answer.html", context)

def registeraccount(request):
    if request.POST["Email"] == request.POST["ConfirmEmail"] and request.POST["Password"] == request.POST["ConfirmPassword"]:
        if utils.validateEmail(request.POST["Email"]):
            pwrd = request.POST["Password"]
            if any(i.isdigit() for i in pwrd) and any(i == i.lower() and not i.isdigit() for i in pwrd) and any(i == i.upper() and not i.isdigit() for i in pwrd):
                if request.POST["Username"] not in models.getExistingStudentNames():
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
                else:
                    request.session["ErrorMessage"] = "Username already exists"
                    return HttpResponseRedirect(reverse("tester:register"))
            else:
                request.session["ErrorMessage"] = "Password must contain a digit, uppercase and lowercase letter"
                return HttpResponseRedirect(reverse("tester:register"))
        else:
            request.session["ErrorMessage"] = "Invalid Email"
            return HttpResponseRedirect(reverse("tester:register"))
    elif request.POST["Email"] == request.POST["ConfirmEmail"]:
        request.session["ErrorMessage"] = "Passwords Do Not Match"
        return HttpResponseRedirect(reverse("tester:register"))
    else:
        request.session["ErrorMessage"] = "Emails Do Not Match"
        return HttpResponseRedirect(reverse("tester:register"))

def loginaccount(request):
    try:
        if models.returnUserPassword(request.POST["Username"]) == request.POST["Password"]:
            request.session["current_user"] = request.POST["Username"]
            return HttpResponseRedirect(reverse("tester:profile"))
        else:
            request.session["ErrorMessage"] = "Invalid Username Or Password"
            return HttpResponseRedirect(reverse("tester:login"))
    except:
        request.session["ErrorMessage"] = "Invalid Username Or Password"
        return HttpResponseRedirect(reverse("tester:login"))

def logoutaccount(request):
    
    request.session["current_user"] = ""
    return HttpResponseRedirect(reverse("tester:login"))

def newquestion(request):
    if request.session["test_over"] == "n":
        return HttpResponseRedirect(reverse("tester:question", args=(request.session["requested_length"], )))
    else:
        return HttpResponseRedirect(reverse("tester:testsettings"))
    

def getstudentdatafromstudenname(request):
    request.session["requestedstudentdata"] = models.getQuestionsAnsweredByUser(request.POST["studentname"])
    return HttpResponseRedirect(reverse("tester:studentdata"))
# Create your views here.
