from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import tester.NEAConceptsTestt as MoleculeGenerator
import tester.SVGtest as SVGGenerator
import tester.models as models
from django.urls import reverse
import django.utils.timezone as time


def index(request):
    return render(request, "tester/index.html", {})

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
    user = models.User.objects.get(user_name = request.session["current_user"])    
    context = {"user_name" : user.user_name, "email" : user.email, "class" : user.user_class}
    return render(request, "tester/profile.html", context)

def studentdata(request):
    return render(request, "tester/studentdata.html", {})

def testsettings(request):
    return render(request, "tester/testsettings.html", {})

def settestsettings(request):
    
    selected_length = request.POST["MolLengt    h"]
    valid_groups = request.POST.getlist("FuncGroup[]")
    request.session['list'] = valid_groups
    request.session["requested_length"] = selected_length
    return HttpResponseRedirect(reverse("tester:question", args=(selected_length, )))

def question(request, selected_length):
    
    valid_groups = request.session['list']
    testMolecule = MoleculeGenerator.Molecule(selected_length, valid_groups)
    testMolecule.generate()
    nameForPrinting  = testMolecule.outputMolecule()
    
    svg = SVGGenerator.createSVG(testMolecule.length, testMolecule)
    
    request.session['molecule_name'] = nameForPrinting
    request.session['image'] = svg
    
    current_user = models.User.objects.get(user_name = request.session["current_user"])
    current_user.most_recent_question = models.Question(molecule_name = nameForPrinting, question_date = time.datetime)
    
    context = {"molecule_name" : nameForPrinting, "image" : svg}
     
    return render(request, "tester/question.html", context)

def answerquestion(request):
    user_answer = request.POST.get('Answer', False)
    request.session['user_answer'] = user_answer
    current_user = models.User.objects.get(request.session["current_user"])
    return HttpResponseRedirect(reverse("tester:answer"))


def answer(request):
    user_answer = request.session['user_answer']
    nameForPrinting = request.session['molecule_name']
    svg = request.session['image']
    context = {"user_answer" : user_answer, "nameForPrinting" : nameForPrinting, "svg" : svg}
    return render(request, "tester/answer.html", context)

def registeraccount(request):
    if request.POST["Email"] == request.POST["ConfirmEmail"] and request.POST["Password"] == request.POST["ConfirmPassword"]:
        user = models.User(
            user_name = request.POST["Username"], 
            password = request.POST["Password"],
            first_name = request.POST["Firstname"],
            last_name = request.POST["Lastname"],
            email = request.POST["Email"],
            user_class = request.POST["class"],)
        user.save()
        print(user.id)
        request.session["ErrorMessage"] = ""
        return HttpResponseRedirect(reverse("tester:login"))
    elif request.POST["Email"] == request.POST["ConfirmEmail"]:
        request.session["ErrorMessage"] = "Passwords Do Not Match"
        return HttpResponseRedirect(reverse("tester:register"))
    else:
        request.session["ErrorMessage"] = "Emails Do Not Match"
        return HttpResponseRedirect(reverse("tester:register"))

def loginaccount(request):
    try:
        if models.User.objects.get(user_name = request.POST["Username"]).password == request.POST["Password"]:
            request.session["current_user"] = request.POST["Username"]
            return HttpResponseRedirect(reverse("tester:profile"))
        else:
            request.session["ErrorMessage"] = "Invalid Username Or Password"
            return HttpResponseRedirect(reverse("tester:login"))
    except:
        request.session["ErrorMessage"] = "Invalid Username Or Password"
        return HttpResponseRedirect(reverse("tester:login"))

def newquestion(request):
        return HttpResponseRedirect(reverse("tester:question", args=(request.session["requested_length"], )))

# Create your views here.
