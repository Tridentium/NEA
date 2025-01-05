from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import NEAConceptsTestt as MoleculeGenerator


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
    testMolecule = MoleculeGenerator.Molecule(3)
    testMolecule.generate()
    nameForPrinting  = testMolecule.outputMolecule()
    context = {"molecule_name" : nameForPrinting}
    return render(request, "tester/question.html", context)
def answer(request):
    return render(request, "tester/answer.html", {})
# Create your views here.
