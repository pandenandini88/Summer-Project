import re
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    htmlString = "<h1>Some Title</h1><a href = 'http://127.0.0.1:8000/resume/'>Resume Page</a>"
    return HttpResponse(htmlString)
    

def resume(request):
    return HttpResponse("<h1> This is the resume page. </h1>")