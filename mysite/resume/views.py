import re
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

htmlLinks = "<pre><a href = 'http://127.0.0.1:8000'>Home Page</a>      <a href = 'http://127.0.0.1:8000/resume/'>Resume Page</a></pre>"

def index(request):
    htmlHomeTitle = "<center><h1> Home Page </h1></center>"
    return HttpResponse(htmlLinks + htmlHomeTitle)
    

def resume(request):
    htmlResumeTitle = "<center><h1> Resume Page </h1></center>"
    return HttpResponse(htmlLinks + htmlResumeTitle)