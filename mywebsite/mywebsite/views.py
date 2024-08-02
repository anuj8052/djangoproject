from django.http import HttpResponse
from django.shortcuts import render


def HomePage(request):
    data = {
        'title': 'Home New',
        'body_title': 'Welcome to django-website!'
    }
    return render(request, "index.html", data)

def aboutUs(request):
    return HttpResponse("Welcome to mywebsite!")

def Course(request):
    return HttpResponse('Welcome to mywebsite')

def CourseDetails(request, courseId):
    return HttpResponse(courseId)
