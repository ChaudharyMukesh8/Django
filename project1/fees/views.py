from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fees_dj(request):
        return HttpResponse("Hello Django 300 fees")
def fees_python(request):
        return HttpResponse('Hello Mukesh 400 fees')
