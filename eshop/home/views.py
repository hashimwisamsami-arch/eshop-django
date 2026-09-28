from django.shortcuts import render
from django.http import HttpResponse

def home(request): #/django/home
    return render(request,"home/home.html")

def about(request):#/django/about
    return render(request,"home/about.html")