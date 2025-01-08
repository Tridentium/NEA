from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import tester.NEAConceptsTestt as MoleculeGenerator
import tester.SVGtest as SVGGenerator


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
def question(request):
    testMolecule = MoleculeGenerator.Molecule(10)
    testMolecule.generate()
    nameForPrinting  = testMolecule.outputMolecule()
    
    svg = SVGGenerator.createSVG(testMolecule.length, testMolecule)
    
    context = {"molecule_name" : nameForPrinting, "image" : svg}
     
    return render(request, "tester/question.html", context)
def answer(request):
    return render(request, "tester/answer.html", {})
# Create your views here.
