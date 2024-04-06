from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
        return HttpResponse('<h1 style="color:red;">Home page</h1>')
def learn_django(request):
        return HttpResponse('<h1>Hello Mukesh Chaudhary</h1>')

def learn_format(request):
        n = '<h1>Mukesh Chaudhary</h1>'
        return HttpResponse(f'My name is {n}')
