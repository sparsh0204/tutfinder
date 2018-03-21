from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TechnologyList, TechnologyDetail, CourseList, CourseDetail
#from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = {
    url(r'^api/technology/$', TechnologyList.as_view()),
    url(r'^api/technology/(?P<pk>[0-9]+)$', TechnologyDetail.as_view()),
    url(r'^api/course/$',CourseList.as_view() ),
    url(r'^api/course/(?P<pk>[0-9]+)$', CourseDetail.as_view()),
#    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
#    url(r'^api/$', TechnologyCreateView.as_view(), name="create"),
#    url(r'^api/tutorials/(?P<slug>\D+)/$',CourseListView.as_view(), name='technology'),
#    url(r'^photos/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
#    url(r'^users/$', UserList.as_view()),
#    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
#    url(r'^get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)
