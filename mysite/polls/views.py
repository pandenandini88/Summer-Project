from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def poll_index(request):
    return render(request, "polls.html")

