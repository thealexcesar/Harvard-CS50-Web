from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def index(request):
    return HttpResponse("<h1 style=\"background:#f9d8a8\">Hello, world!</h1><p style=\"font-family:sans-serif\">Using Django.</p>")
def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")