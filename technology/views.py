from django.shortcuts import render
from technology.models import Technology
# Create your views here.
from course.models import Course


def technology(request,tech):
    try:
        tech = Technology.objects.filter(title=tech)
    except Technology.DoesNotExist:
        tech = None
#    try:
#        courses = Course.objects.filter()
    return render(request, 'technology.html', {'tech': tech})
