from django.conf.urls import url
from .views import technology

urlpatterns = [
#    url(r'^panel/person/(?P<person_id>[0-9]+)$', 'apps.panel.views.person_form', name='panel_person_form'),
    url(r'^tutorial/(?P<tech>\w+)/$', technology, name='technology'),
#    url(r'^tutorial/(?<tech>$',course, name = 'course'),
]