from django.shortcuts import render

# Create your views here.

def home(requst):
    return render(requst,'weather_find_page.html')