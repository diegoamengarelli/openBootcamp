from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    directors = Director.objects.all()
    queryset = Film.objects.all()
    
    context = {
        "object_list": queryset,
        "directors": directors
    }
    return render(request, "home.html", context)