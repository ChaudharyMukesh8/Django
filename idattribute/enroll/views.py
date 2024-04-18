from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def showformdata(request):
        # by default dynamic value in the input fields
        # fm = StudentRegistration(auto_id=True,  label_suffix='  ',initial={'name':'Mukesh','email':'chaudhary@gmail.com' })

        # To Order the fields
        fm= StudentRegistration()
        fm.order_fields(field_order=['email','name'])

        return render(request,'enroll/userregistration.html',{'form':fm})