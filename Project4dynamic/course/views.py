from django.shortcuts import render

# Create your views here.
def learn_django(request):
        # coursename = {'fname':'laravel'}
        cname = 'django'
        duration = '4 month'
        seats = 10
        django_details={'nm':cname,'du':duration,'st':seats}
        # return render(request,'course/courseone.html',coursename)
        return render(request ,'course/courseone.html',django_details)

def learn_python(request):
        # coursename = {'cname':'python with django'}
        # return render(request,'course/coursetwo.html',coursename)
        student = {'names': ['Mukesh','Ritik','Ravi','Shri']}
        return render(request, 'course/courseone.html',student)