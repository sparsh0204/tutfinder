from django.conf.urls import url
from course.views import course

urlpatterns = [
    url(r'^/$',course, name = 'course'),
]