from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    TechnologyListAPIView,
    TechnologyDetailAPIView,
    TechnologyCreateAPIView,
    TechnologyUpdateAPIView,
    TechnologyDeleteAPIView,
    CourseCreateAPIView,
    CourseListAPIView,
    CourseTechListAPIView,
    CourseDetailAPIView,
    CourseDeleteAPIView,
    CourseUpdateAPIView,
    # ReviewList,
    # ReviewDetail,
)


urlpatterns = [
    url(r'^technology/$', TechnologyListAPIView.as_view(), name='tech_list'),
    url(r'^technology/create/$', TechnologyCreateAPIView.as_view(), name='tech_create'),
    url(r'^technology/(?P<slug>[\w-]+)/$', TechnologyDetailAPIView.as_view(), name='tech_detail'),
    url(r'^technology/(?P<slug>[\w-]+)/edit/$', TechnologyUpdateAPIView.as_view(), name='tech_update'),
    url(r'^technology/(?P<slug>[\w-]+)/delete/$', TechnologyDeleteAPIView.as_view(), name='tech_delete'),
    # url(r'^posts/$', "<appname>.views.<function_name>"),

    url(r'^course/$', CourseListAPIView.as_view(), name='course_list'),
    url(r'^courses/(?P<tech_slug>[\w-]+)/$', CourseTechListAPIView.as_view(), name='course_tech_list'),
    url(r'^course/create/$', CourseCreateAPIView.as_view(), name='course_create'),
    url(r'^course/(?P<slug>[\w-]+)/$', CourseDetailAPIView.as_view(), name='course_detail'),
    url(r'^course/(?P<slug>[\w-]+)/edit/$', CourseUpdateAPIView.as_view(), name='course_update'),
    url(r'^course/(?P<slug>[\w-]+)/delete/$', CourseDeleteAPIView.as_view(), name='course_delete'),
    # url(r'^posts/$', "<appname>.views.<function_name>"),

    # url(r'^api/technology/(?P<pk>[0-9]+)$', TechnologyDetail.as_view()),
    # url(r'^api/technology/(?P<pk>[0-9]+)$', TechnologyDetail.as_view()),
    # url(r'^api/courses/$',CourseList.as_view() ),
    # url(r'^api/courses/(?P<tech>.+)/$', TechCourseList.as_view()),
    # url(r'^api/reviews/(?P<course>.+)/$', ReviewList.as_view()),
    # url(r'^api/review/(?P<pk>[0-9]+)$', ReviewDetail.as_view()),
    # url('^purchases/(?P<username>.+)/$', PurchaseList.as_view()),
    # url(r'^api/course/$',CourseList.as_view() ),
    # url(r'^api/course/(?P<slug>.+)$', CourseDetail.as_view()),
    # url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^api/$', TechnologyCreateView.as_view(), name="create"),
    # url(r'^api/tutorials/(?P<slug>\D+)/$',CourseListView.as_view(), name='technology'),
    # url(r'^photos/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
    # url(r'^users/$', UserList.as_view()),
    # url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url(r'^get-token/', obtain_auth_token),

]

urlpatterns = format_suffix_patterns(urlpatterns)
