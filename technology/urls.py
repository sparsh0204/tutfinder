from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    TechnologyListAPIView,
    TechnologyDetailAPIView,
    TechnologyCreateAPIView,
    TechnologyUpdateAPIView,
    TechnologyDeleteAPIView,
)


urlpatterns = [
    url(r'^$', TechnologyListAPIView.as_view(), name='tech_list'),
    url(r'^create/$', TechnologyCreateAPIView.as_view(), name='tech_create'),
    url(r'^(?P<slug>[\w-]+)/$', TechnologyDetailAPIView.as_view(), name='tech_detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', TechnologyUpdateAPIView.as_view(), name='tech_update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', TechnologyDeleteAPIView.as_view(), name='tech_delete'),
    # url(r'^posts/$', "<appname>.views.<function_name>"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
