from django.shortcuts import render
from .models import Technology
# Create your views here.
from course.models import Course

from rest_framework import generics
from .serializers import TechnologySerializer

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()
def technology(request, slug):
    print(slug)
    print('xyz')
    try:
        tech = Technology.objects.get(slug=slug)
    except Technology.DoesNotExist:
        tech = None
    print(tech)
    try:
         courses = Course.objects.filter(tech=tech)
    except Course.DoesNotExist:
        courses = None
    return render(request, 'technology.html', {'tech': tech, 'courses':courses})
