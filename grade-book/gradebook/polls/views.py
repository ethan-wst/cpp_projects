from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Course

def index(request):
    list_of_courses = Course.objects.order_by("-course_number")
    template = loader.get_template("polls/index.html")
    context = {
        "Courses": list_of_courses,
    }
    return HttpResponse(template.render(context, request))

def course (request, course_number):
    response = "Your course number is #%s"
    return HttpResponse(response % course_number)

