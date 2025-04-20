from django.shortcuts import render
from plumber.models import Questions

def index(request):
    context={

    }
    return render(request, "plumber/index.html", context)

def testing(request):
    que=Questions.objects.all()
    context={
        'que':que,
    }
    return render(request, "plumber/testing.html", context) 
