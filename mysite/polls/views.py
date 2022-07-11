from django.shortcuts import render
from django.http import HttpResponse

# This function takes a request from the user and displays elements on to the polls page. polls.html can be found under the templates folder.
def poll_index(request):
    return render(request, "polls.html")

