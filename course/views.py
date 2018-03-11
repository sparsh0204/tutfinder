from django.shortcuts import render
from technology.models import Technology
# Create your views here.
from course.models import Course


def course(request, slug, course_slug):
    print('yz')
    try:
        tech = Technology.objects.get(slug=slug)
    except Technology.DoesNotExist:
        tech = None
    try:
        course_obj = Course.objects.get(slug=course_slug)
    except Course.DoesNotExist:
        print('bmv')
        course_obj = None
    print('hbj')
    print(course_obj)
    return render(request, 'course.html', {'course': course_obj})
