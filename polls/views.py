from django.shortcuts import render

# Create your views here.

def polls(requst):
    return render(requst,'polls.html')