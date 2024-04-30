from django.shortcuts import render

# Create your views here.
def home(request,check):
  return render(request,'enroll/home.html',{'ch':check})

# def show_details(request,my_id):
#   return render(request,'enroll/show.html',{'id':my_id})

def show_details(request,my_id):
   if my_id==1:
      student = {'id':my_id,'name':'Mukesh'}
   if my_id==2:
      student = {'id':my_id,'name':'Abhi'}
   if my_id==3:
      student = {'id':my_id,'name':'Ritik'}
   return render(request,'enroll/show.html',student)

def show_subdetails(request,my_id,my_subid):
   if my_id==1 and my_subid==5:
      student = {'id':my_id,'name':'Mukesh','info':'sub Details'}
   if my_id==2 and my_subid==6:
      student = {'id':my_id,'name':'Abhi','info':'sub Details'}
   if my_id==3 and my_subid==7:
      student = {'id':my_id,'name':'Ritik','info':'sub Details'}
   return render(request,'enroll/show.html',student)
