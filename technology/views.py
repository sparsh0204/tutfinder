from django.shortcuts import render
from .models import Technology
# Create your views here.
from course.models import Course


def technology(request,tech):
    try:
        tech = Technology.objects.get(title=tech)
    except Technology.DoesNotExist:
        tech = None
    try:
         courses = Course.objects.filter(tech=tech)
    except Course.DoesNotExist:
        courses = None
    return render(request, 'technology.html', {'tech': tech, 'courses':courses})
