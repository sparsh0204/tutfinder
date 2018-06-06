from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    TrackCourseCreateAPIView,
    TrackCourseListAPIView,
    TrackCourseFilteredListAPIView,
    TrackCourseDetailAPIView,
    TrackCourseDeleteAPIView,
    TrackCourseUpdateAPIView,
)


urlpatterns = [

    url(r'^track_course/$', TrackCourseListAPIView.as_view(), name='track_course_list'),
    url(r'^track_courses/(?P<track_slug>[\w-]+)/$', TrackCourseFilteredListAPIView.as_view(), name='track_course_f_list'),
    url(r'^track_course/create/$', TrackCourseCreateAPIView.as_view(), name='track_course_create'),
    url(r'^track_course/(?P<slug>[\w-]+)/$', TrackCourseDetailAPIView.as_view(), name='track_course_detail'),
    url(r'^track_course/(?P<slug>[\w-]+)/edit/$', TrackCourseUpdateAPIView.as_view(), name='track_course_update'),
    url(r'^track_course/(?P<slug>[\w-]+)/delete/$', TrackCourseDeleteAPIView.as_view(), name='track_course_delete'),
    # url(r'^posts/$', "<appname>.views.<function_name>"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
