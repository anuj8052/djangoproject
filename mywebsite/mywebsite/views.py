from django.http import HttpResponse
from django.shortcuts import render


def HomePage(request):
    data = {
        'title': 'Home New',
        'body_title': 'Welcome to django-website!',
        # adding list to use for loop
        'clist': ['PHP', 'Python', 'Django'],
        'student_details': [
            {'name': 'pradeep', 'phone': 8948013408},
            {'name': 'Anuj', 'phone': 1234567890}
        ]
    }
    
    return render(request, "index.html", data)

def aboutUs(request):
    return HttpResponse("Welcome to mywebsite!")

def Course(request):
    return HttpResponse('Welcome to mywebsite')

def CourseDetails(request, courseId):
    return HttpResponse(courseId)
