import re
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# This function takes a request from the user and displays elements on to the home page. home.html can be found under the templates folder.
def index(request):
    """
    This function takes a request from the user and displays elements on to the home page.
    home.html can be found under the templates folder.

    Args:
        request (Django Request): A Django Request

    Returns:
        render: A template to render
    """
    return render(request, "home.html")
    

# This function takes a request from the user and displays elements on to the resume page. resume.html can be found under the templates folder.
def resume(request):
    return render(request, "resume.html")
# This function takes a request from the user and displays elements on to the polls page. polls.html can be found under the templates folder.
