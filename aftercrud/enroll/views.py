from django.shortcuts import render
from .forms import StudentRegistartion

# Create your views here.

def showformdata(request):
  fm = StudentRegistartion()
  return render(request, 'enroll/userregistration.html', {'form':fm} )
