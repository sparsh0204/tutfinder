from django.conf.urls import url
from .views import technology
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = {
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^photos/$', CreateView.as_view(), name="create"),
#    url(r'^photos/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
#    url(r'^users/$', UserList.as_view()),
#    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url(r'^get-token/', obtain_auth_token),
#    url(r'^panel/person/(?P<person_id>[0-9]+)$', 'apps.panel.views.person_form', name='panel_person_form'),
    url(r'^tutorials/(?P<slug>\D+)/$', technology, name='technology'),

#    url(r'^tutorial/(?<tech>$',course, name = 'course'),
}

urlpatterns = format_suffix_patterns(urlpatterns)