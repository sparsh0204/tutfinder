from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('core.urls')),
    url(r'^api/technology/', include("technology.urls", namespace='tech')),
    url(r'^api/', include("course.urls", namespace='course')),
    url(r'^api/track', include("track.urls", namespace='track')),
    url(r'^api/', include("track_course.urls", namespace='track_course')),
#    url(r'', include('user.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
