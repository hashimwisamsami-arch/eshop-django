from django.shortcuts import render
from django.http import HttpResponse

def home(request): #/django/home
    return HttpResponse("<h1>Home Page</h1>")

def about(request):#/django/about
    return HttpResponse("<h1>About Page</h1>")