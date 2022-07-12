from django.shortcuts import render
from django.http import HttpResponse

# This function takes a request from the user and displays elements on to the polls page. polls.html can be found under the templates folder.
def poll_index(request):
    return render(request, "polls.html")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
    