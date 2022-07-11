import re
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# This function takes a request from the user and displays elements on to the home page. home.html can be found under the templates folder.
def index(request):
    return render(request, "home.html")
    

# This function takes a request from the user and displays elements on to the resume page. resume.html can be found under the templates folder.
def resume(request):
    return render(request, "resume.html")

