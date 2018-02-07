from django.shortcuts import render
from technology.models import Technology
# Create your views here.
from course.models import Course


def course(request,tech):

    return render(request, 'course.html', {'tech': tech})
