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
    # selected_choice.votes = F("votes") + 1
    # selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse("tester:question", args=(selected_length,)))
def question(request, selected_length):
    testMolecule = MoleculeGenerator.Molecule(selected_length)
    testMolecule.generate()
    nameForPrinting  = testMolecule.outputMolecule()
    
    svg = SVGGenerator.createSVG(testMolecule.length, testMolecule)
    
    context = {"molecule_name" : nameForPrinting, "image" : svg}
     
    return render(request, "tester/question.html", context)
def answer(request):
    return render(request, "tester/answer.html", {})
# Create your views here.
