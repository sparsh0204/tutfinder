from django.conf.urls import url
from .views import course

urlpatterns = [
#    url(r'^course/$',course, name = 'course'),
    url(r'^tutorial/(?P<slug>\D+)/(?P<course_slug>\w+)/$', course, name='course'),
#    url(r'^(?P<course_slug>\w+)/$',course, name = 'course'),
]