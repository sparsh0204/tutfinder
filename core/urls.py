from django.conf.urls import url
from core.views import home

urlpatterns = [
#    url(r'^api/$', CreateView.as_view(), name="create"),
#    url(r'^photos/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
    url(r'^$', home, name = 'home'),
]