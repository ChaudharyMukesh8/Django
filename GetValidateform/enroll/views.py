from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def showformdata(request):
        if request.method == 'POST':
           fm = StudentRegistration(request.POST)
        #    print(fm)
        #    print("This is coming from post request")
           if fm.is_valid():
            print('form validated')    
            name =  fm.cleaned_data['name']
            email =  fm.cleaned_data['email']
            password = fm.cleaned_data['password']

            print('Name ',name)
            print('email',email)
            print('password',password)
            fm = StudentRegistration()
        else:
            fm = StudentRegistration()
            print("This is coming from get request")
        return render(request,'enroll/userregistration.html',{'form':fm})