from django.shortcuts import render
from enroll.models import Student
# Create your views here.

def studentinfo(request):
        stud = Student.objects.get(pk=3)
#    stud = Student.objects.all() # this is used for showing all data... 
       
# for retrieving some specific data
#    print('My output',stud) 
# for debugging purpose only
        return render(request,'enroll/studentdetail.html',{'stu':stud})    