from django.shortcuts import render
from technology.models import Technology
# Create your views here.
#from course.models import Course


def home(request):
    try:
        technologies = Technology.objects.all()
    except Technology.DoesNotExist:
        technologies = None
    return render(request, 'home.html', {'technologies': technologies})