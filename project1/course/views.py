from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
        return HttpResponse('<h1 style="color:green;">Home Page </h1>')
def learn_django(request):
        return HttpResponse("Hello Welcome to the world of Django")
def learn_py(request):
        return HttpResponse("Hello welcome to the world of Python")