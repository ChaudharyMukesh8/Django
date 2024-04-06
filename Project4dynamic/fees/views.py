from django.shortcuts import render
from datetime import datetime


# Create your views here.
def fees_django(request):
        d = datetime.now()
        return render(request, 'fees/feesone.html',{'dt':d})

        

        # return render(request,'fees/feesone.html',{'nm':'Django is a framework of python '})
def fees_python(request):
        data = {'stu1':{'name':'Mukesh','roll':101},'stu2':{'name':'Ritik','roll':102},'stu3':{'name':'shri','roll':103},'stu4':{'name':'Abhi','roll':104},}
        return render(request,'fees/feestwo.html',{'data':data})
        # return render(request,'fees/feestwo.html',{'nm': 'Hello How are you'})

