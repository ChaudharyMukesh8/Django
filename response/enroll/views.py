from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration
# Create your views here.

def thankyou(request):
    return render(request,'enroll/success.html')

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
            return HttpResponseRedirect('/reg/success/')
           # return render(request,'enroll/success.html',{'nm':name})
            
        else:
            fm = StudentRegistration()
            print("This is coming from get request")
        return render(request,'enroll/userregistration.html',{'form':fm})