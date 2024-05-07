from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from . import model 

# curl=settings.CURRENT_URL

def index(request):
    return render(request,'index.html') 

def registration(request):
    # if method.registration="GET":
    #     name=model.name.POST.get("name")
    #     email=model.POST.get("email")

    return render(request,'registration.html') 
   