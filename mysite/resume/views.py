import re
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    htmlLinks = "<pre><a href = 'http://127.0.0.1:8000'>Home Page</a>      <a href = 'http://127.0.0.1:8000/resume/'>Resume Page</a></pre>"
    htmlTitle = "<center><h1> Home Page </h1></center>"
    return HttpResponse(htmlLinks + htmlTitle)
    

def resume(request):
    return HttpResponse("<center><h1> This is the resume page. </h1></center>")