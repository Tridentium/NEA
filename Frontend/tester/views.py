from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import tester.NEAConceptsTestt as MoleculeGenerator
import tester.SVGtest as SVGGenerator
from django.urls import reverse


def index(request):
    return render(request, "tester/index.html", {})

def login(request):
    return render(request, "tester/login.html", {})

def register(request):
    return render(request, "tester/register.html", {})

def profile(request):
    return render(request, "tester/profile.html", {})

def studentdata(request):
    return render(request, "tester/studentdata.html", {})

def testsettings(request):
    return render(request, "tester/testsettings.html", {})

def settestsettings(request):
    
    selected_length = request.POST["MolLength"]
    valid_groups = request.POST.getlist("FuncGroup[]")
    request.session['list'] = valid_groups
    return HttpResponseRedirect(reverse("tester:question", args=(selected_length, )))

def question(request, selected_length):
    
    valid_groups = request.session['list']
    testMolecule = MoleculeGenerator.Molecule(selected_length, valid_groups)
    testMolecule.generate()
    nameForPrinting  = testMolecule.outputMolecule()
    
    svg = SVGGenerator.createSVG(testMolecule.length, testMolecule)
    
    request.session['molecule_name'] = nameForPrinting
    request.session['image'] = svg
    
    context = {"molecule_name" : nameForPrinting, "image" : svg}
     
    return render(request, "tester/question.html", context)

def answerquestion(request):
    user_answer = request.POST.get('Answer', False)
    request.session['user_answer'] = user_answer
    return HttpResponseRedirect(reverse("tester:answer"))


def answer(request):
    user_answer = request.session['user_answer']
    nameForPrinting = request.session['molecule_name']
    svg = request.session['image']
    context = {"user_answer" : user_answer, "nameForPrinting" : nameForPrinting, "svg" : svg}
    return render(request, "tester/answer.html", context)
# Create your views here.
